#!/usr/bin/env python3
"""
source_check.py - SF DPH Revenue Integrity multi-program source change-checker.

v1.3. Keeps the v1.2 engine (conditional GETs, robots.txt, redirect guard,
entry types pdf/html/binary/linkpage/bulletin_probe, BLIND_SHELL honesty,
manual entries, master_keys mapping) and adds four things:

  1. Snapshots + diffs. The extracted text of every pdf/html source is stored
     under snapshots/. On CHANGED, a unified before/after diff is written to
     reports/diffs/ with a structured table of possible CPT / HCPCS /
     ICD-10-CM / modifier codes touched (system, direction, confidence,
     tracked flag from data/tracked_codes.csv, page-anchored PDF deep links).
     Git history preserves every prior snapshot.
  2. manual_list entry type. Points at the JSON endpoint behind a client-
     rendered manual page (e.g. the mcweb Family PACT manual). Every PDF it
     lists is monitored individually: content text hash, the portal Revision
     Date, auto-discovery of NEW documents, and REMOVED flags.
  3. Dashboard. --dashboard PATH writes a markdown status page (for GitHub
     Pages) grouped by program.
  4. Change log. Review-worthy events append to reports/changes_log.csv
     (machine-readable, Power BI friendly) and a run_summary.md is written
     for alerting (GitHub Issue body).

A change verdict means one thing only: a human re-reads that source and, if
needed, updates the Master sheet. Nothing is written to any system of record.
Decision support, not a source of truth.

Run:
  python source_check.py                       # all enabled programs
  python source_check.py --programs fpact      # subset
  python source_check.py --update              # save new baseline after review
  python source_check.py --dashboard docs/index.md
  python source_check.py --list                # show watchlist and exit
Exit code: 1 if anything needs review (usable by cron/CI), else 0.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import html
import io
import json
import os
import re
import sys
import textwrap
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests
import yaml

UA = "SFHN-RevInt-source-checker/1.3"
TIMEOUT = 30
SLEEP = 1.0
SHELL_MIN_CHARS = 400          # visible text below this => JS app shell
DATE_RE = re.compile(r"Page updated:\s*([A-Za-z]+\s+\d{4})")
DEFAULT_LINK_RE = r'href="([^"]+\.pdf[^"]*)"'
NEEDS_REVIEW = {"NEW", "CHANGED", "DATE_CHANGED", "LINKS_CHANGED",
                "NEW_ISSUE", "URL_CHANGED_IN_CONFIG", "REMOVED",
                "CHANGED_METADATA_ONLY", "LIST_TRUNCATED"}
DIFF_MAX_LINES = 3000

# Self-heal: a read-only Directus SPA bakes a static public token into its
# runtime config bundle. If MCWEB_TOKEN is unset or has been rotated, the
# watcher re-reads the current token from this bundle. Never a secret value
# in the repo; the bundle is served anonymously.
DIRECTUS_TOKEN_RE = r'window\.DIRECTUS_TOKEN\s*=\s*"([^"]+)"'

# Heuristic billing-code patterns, applied to changed diff lines only.
# The five-digit CPT pattern is the noisy one (SF zip codes 941xx, fee
# amounts, form numbers all look like CPT codes), so a bare five-digit
# candidate only counts when code-ish vocabulary appears on the same or a
# neighboring changed line, or the code is listed in data/tracked_codes.csv.
# Letter-bearing systems (HCPCS, ICD-10-CM, CPT category/PLA suffixes,
# "modifier NN") are format-distinctive and always included, with confidence
# downgraded when no vocabulary is nearby. Documented in README "Code
# extraction heuristic".
RE_HCPCS = re.compile(r"\b[A-Z]\d{4}\b")                  # J7300, S5000, G2012
RE_ICD10 = re.compile(r"\b[A-Z]\d{2}\.[0-9A-Z]{1,4}\b")   # Z30.011
RE_CPT = re.compile(r"\b\d{5}\b")                         # 99213 (context-gated)
RE_CPT_ALPHA = re.compile(r"\b\d{4}[FTUM]\b")             # 0001U, 1234F
CPT_NOISE = re.compile(r"^(19|20)\d{2,3}$")               # years / year-like
RE_MODIFIER = re.compile(r"\bmodifiers?\s*[-:]?\s*([0-9A-Z]{2})\b", re.I)
CODE_VOCAB = re.compile(
    r"\b(codes?|cpt|hcpcs|icd|procedures?|modifiers?|bill(?:ing|ed|able)?"
    r"|units?|tar|rates?)\b", re.I)
PAGE_MARK = re.compile(r"\[\[page (\d+)\]\]")
_MONTH = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*"
EFFECTIVE_RE = re.compile(
    r"effective\s+(?:date\s*[:\-]?\s*)?"
    rf"({_MONTH}\s+\d{{1,2}},?\s+\d{{4}}|{_MONTH}\s+\d{{4}}"
    r"|\d{1,2}/\d{1,2}/\d{2,4}|\d{4}-\d{2}-\d{2})", re.I)


def load_tracked_codes(path: Path) -> dict[str, dict]:
    """data/tracked_codes.csv (code, description, master_row) -> dict keyed by
    uppercased code. Optional file; empty dict when absent or unreadable."""
    out: dict[str, dict] = {}
    try:
        if not path.exists():
            return out
        with path.open(encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                code = (r.get("code") or "").strip().upper()
                if code:
                    out[code] = {"description": (r.get("description") or "").strip(),
                                 "master_row": (r.get("master_row") or "").strip()}
    except OSError:
        pass
    return out


def snapshot_page_map(snapshot_text: str) -> dict[str, int]:
    """line content -> page number, from the [[page N]] markers that
    pdf_text_and_dates writes into PDF snapshots. First occurrence wins.
    HTML snapshots have no markers and yield an empty map."""
    pages: dict[str, int] = {}
    cur = 0
    for ln in snapshot_text.splitlines():
        m = PAGE_MARK.fullmatch(ln)
        if m:
            cur = int(m.group(1))
            continue
        if cur and ln not in pages:
            pages[ln] = cur
    return pages


def extract_code_entries(diff_lines: list[str], old_text: str = "",
                         new_text: str = "",
                         tracked: dict[str, dict] | None = None) -> list[dict]:
    """Structured billing-code candidates from a unified diff. Heuristic only.

    Returns one dict per (code, system): {code, system, direction
    (added/removed/both), confidence (high/medium/low), tracked (bool),
    master_row, context (line excerpt), page (int or None)}.

    Confidence: tracked or vocab on the same line -> high; vocab only on a
    neighboring changed line -> medium; format-distinctive code with no vocab
    nearby -> low; bare five-digit number with no vocab and not tracked ->
    excluded entirely (zip codes, fee amounts, form numbers).

    Page comes from the nearest preceding [[page N]] marker in the relevant
    snapshot text (old for removed lines, new for added).
    """
    tracked = tracked or {}
    old_pages = snapshot_page_map(old_text)
    new_pages = snapshot_page_map(new_text)
    # Keep context lines and hunk boundaries so the "neighboring line" vocab
    # check means adjacent in the document, not adjacent in the change list.
    body_lines: list[tuple[str, str]] = []          # (sign, body)
    for line in diff_lines:
        if not line or line.startswith(("+++", "---")):
            continue
        if line.startswith("@@"):
            body_lines.append(("@", ""))            # hunk boundary sentinel
        elif line[0] in "+- ":
            body_lines.append((line[0], line[1:]))

    def vocab_level(i: int) -> str:
        """'same' | 'neighbor' | 'none' for body line i."""
        if CODE_VOCAB.search(body_lines[i][1]):
            return "same"
        for j in (i - 1, i + 1):
            if 0 <= j < len(body_lines) and CODE_VOCAB.search(body_lines[j][1]):
                return "neighbor"
        return "none"

    def excerpt(body: str, code: str) -> str:
        body = body.strip()
        if len(body) <= 110:
            return body
        pos = body.find(code)
        start = max(0, pos - 45)
        return ("..." if start else "") + body[start:start + 100] + "..."

    entries: dict[tuple[str, str], dict] = {}

    def add(code: str, system: str, sign: str, i: int, distinctive: bool):
        body = body_lines[i][1]
        code_u = code.upper()
        is_tracked = code_u in tracked
        vl = vocab_level(i)
        if not distinctive and not is_tracked and vl == "none":
            return                                   # bare 5-digit, no context
        if is_tracked or vl == "same":
            conf = "high"
        elif vl == "neighbor":
            conf = "medium"
        else:
            conf = "low"
        page = (new_pages if sign == "+" else old_pages).get(body.strip())
        direction = "added" if sign == "+" else "removed"
        key = (code_u, system)
        e = entries.get(key)
        if not e:
            entries[key] = {
                "code": code_u, "system": system, "direction": direction,
                "confidence": conf, "tracked": is_tracked,
                "master_row": tracked.get(code_u, {}).get("master_row", ""),
                "description": tracked.get(code_u, {}).get("description", ""),
                "context": excerpt(body, code), "page": page,
            }
            return
        if e["direction"] != direction:
            e["direction"] = "both"
        order = {"low": 0, "medium": 1, "high": 2}
        if order[conf] > order[e["confidence"]]:
            e["confidence"] = conf
        if e["page"] is None:
            e["page"] = page

    for i, (sign, body) in enumerate(body_lines):
        if sign not in "+-":
            continue
        icd = set(RE_ICD10.findall(body))
        for c in icd:
            add(c, "ICD-10-CM", sign, i, distinctive=True)
        for c in set(RE_HCPCS.findall(body)):
            # an ICD-10 match like Z30.011 also matches [A-Z]\d{4} across the
            # dot-free prefix on some inputs; skip anything inside an ICD hit
            if any(c in x for x in icd):
                continue
            add(c, "HCPCS", sign, i, distinctive=True)
        for c in set(RE_CPT_ALPHA.findall(body)):
            add(c, "CPT", sign, i, distinctive=True)
        for m in RE_MODIFIER.finditer(body):
            add(m.group(1), "modifier", sign, i, distinctive=True)
        for c in set(RE_CPT.findall(body)):
            if CPT_NOISE.match(c):
                continue
            add(c, "CPT", sign, i, distinctive=False)

    conf_order = {"high": 0, "medium": 1, "low": 2}
    return sorted(entries.values(),
                  key=lambda e: (not e["tracked"], conf_order[e["confidence"]],
                                 e["system"], e["code"]))


def effective_dates_in_diff(diff_lines: list[str]) -> list[str]:
    """Effective-date phrases on added lines, for the comms draft. Heuristic."""
    out: list[str] = []
    for line in diff_lines:
        if line.startswith("+") and not line.startswith("+++"):
            for m in EFFECTIVE_RE.finditer(line[1:]):
                if m.group(1) not in out:
                    out.append(m.group(1))
    return out


def page_link(url: str, page, is_pdf: bool) -> str:
    """Markdown cell for a page reference: a working deep link when the source
    is a PDF (browser viewers honor #page=N), plain text otherwise."""
    if page is None:
        return ""
    if is_pdf and url:
        return f"[p.{page}]({url}#page={page})"
    return f"p.{page}"


def codes_brief(entries: list[dict]) -> str:
    """One-line summary of code entries for CSV cells and log lines."""
    return "; ".join(
        f"{e['code']}({e['system']},{e['direction']}"
        + (",TRACKED" if e["tracked"] else "") + ")" for e in entries)


# ----------------------------------------------------------------- helpers --
class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript", "template"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript", "template") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def html_text(raw: bytes) -> str:
    p = _TextExtractor()
    try:
        p.feed(raw.decode("utf-8", errors="replace"))
    except Exception:
        return ""
    return norm(" ".join(p.parts))


def pdf_text_and_dates(raw: bytes) -> tuple[str, str, str]:
    """Return (normalized_flat_text, page_updated_stamps, line_text).

    line_text keeps line structure per page - that is what snapshots store,
    so diffs are readable. The flat text feeds the hash (unchanged from v1.2,
    so existing baselines stay valid).
    """
    try:
        import pypdf
        rdr = pypdf.PdfReader(io.BytesIO(raw))
        pages = [(rdr.pages[i].extract_text() or "") for i in range(len(rdr.pages))]
        text = norm(" ".join(pages))
        stamps = sorted(set(DATE_RE.findall(" ".join(pages))))
        lines: list[str] = []
        for i, p in enumerate(pages, 1):
            lines.append(f"[[page {i}]]")
            for ln in p.splitlines():
                ln = norm(ln)
                if ln:
                    lines.append(ln)
        return text, "|".join(stamps), "\n".join(lines)
    except Exception:
        return "", "", ""


def sha(data) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "doc"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ------------------------------------------------------------------ fetch ---
class Fetcher:
    def __init__(self) -> None:
        self.sess = requests.Session()
        self.sess.headers.update({"User-Agent": UA})
        self._robots: dict[str, RobotFileParser | None] = {}

    def robots_ok(self, url: str) -> bool:
        host = urlparse(url).netloc
        if host not in self._robots:
            rp = RobotFileParser()
            rp.set_url(f"{urlparse(url).scheme}://{host}/robots.txt")
            try:
                r = self.sess.get(rp.url, timeout=TIMEOUT)
                if r.status_code >= 400:
                    self._robots[host] = None            # no robots -> allowed
                else:
                    rp.parse(r.text.splitlines())
                    self._robots[host] = rp
            except Exception:
                self._robots[host] = None
        rp = self._robots[host]
        return True if rp is None else rp.can_fetch(UA, url)

    def get(self, url: str, prev: dict) -> dict:
        """Conditional GET with same-host redirect guard."""
        if not self.robots_ok(url):
            return {"status": "robots_blocked"}
        headers = {}
        if prev.get("etag"):
            headers["If-None-Match"] = prev["etag"]
        elif prev.get("last_modified"):
            headers["If-Modified-Since"] = prev["last_modified"]
        r = self.sess.get(url, timeout=TIMEOUT, allow_redirects=True,
                          headers=headers)
        start_host = urlparse(url).hostname
        for hop in list(r.history) + [r]:
            if urlparse(hop.url).hostname != start_host:
                return {"status": f"offhost_redirect:{urlparse(hop.url).hostname}"}
        return {
            "status": str(r.status_code),
            "final_url": r.url,
            "etag": r.headers.get("ETag", ""),
            "last_modified": r.headers.get("Last-Modified", ""),
            "content_type": r.headers.get("Content-Type", ""),
            "content": r.content if r.status_code != 304 else b"",
        }

    def _finalize(self, r, url: str) -> dict:
        """Same response-dict shape and same-host redirect guard as get()."""
        start_host = urlparse(url).hostname
        for hop in list(r.history) + [r]:
            if urlparse(hop.url).hostname != start_host:
                return {"status": f"offhost_redirect:{urlparse(hop.url).hostname}"}
        return {
            "status": str(r.status_code),
            "final_url": r.url,
            "etag": r.headers.get("ETag", ""),
            "last_modified": r.headers.get("Last-Modified", ""),
            "content_type": r.headers.get("Content-Type", ""),
            "content": r.content if r.status_code != 304 else b"",
        }

    def get_auth(self, url: str, prev: dict, extra_headers: dict | None = None) -> dict:
        """Conditional GET that also sends per-request headers (e.g. a Bearer
        token for authenticated asset downloads). get() is left untouched so
        every existing entry keeps its exact behavior; only callers that opt
        in (manual_list assets) send credentials, and only to their own host.
        """
        if not self.robots_ok(url):
            return {"status": "robots_blocked"}
        headers = dict(extra_headers or {})
        if prev.get("etag"):
            headers["If-None-Match"] = prev["etag"]
        elif prev.get("last_modified"):
            headers["If-Modified-Since"] = prev["last_modified"]
        r = self.sess.get(url, timeout=TIMEOUT, allow_redirects=True,
                          headers=headers)
        return self._finalize(r, url)

    def post_json(self, url: str, body_dict: dict,
                  extra_headers: dict | None = None) -> dict:
        """POST a JSON body (Directus/GraphQL). Same UA, robots gate, timeout,
        and response-dict shape as get(). Never mutates get()."""
        if not self.robots_ok(url):
            return {"status": "robots_blocked"}
        headers = {"Content-Type": "application/json", **(extra_headers or {})}
        r = self.sess.post(url, json=body_dict, timeout=TIMEOUT,
                           allow_redirects=True, headers=headers)
        return self._finalize(r, url)


# ------------------------------------------------------------- per entry ----
def signature(entry: dict, resp: dict) -> dict:
    """Build the content signature for one fetched entry.

    sig["snapshot_text"] carries line-structured text for the snapshot/diff
    layer. It is never persisted to the baseline.
    """
    raw = resp.get("content", b"")
    etype = entry.get("type", "html")
    ctype = resp.get("content_type", "").lower()
    sig = {"bytes": len(raw), "byte_sha": sha(raw) if raw else "",
           "text_sha": "", "page_updated": "", "links": [], "shell": False,
           "snapshot_text": ""}

    if etype == "pdf" or "application/pdf" in ctype:
        text, stamps, line_text = pdf_text_and_dates(raw)
        sig["text_sha"] = sha(text) if text else sig["byte_sha"]
        sig["page_updated"] = stamps
        sig["snapshot_text"] = line_text
    elif etype == "binary":
        sig["text_sha"] = sig["byte_sha"]
    else:                                            # html / linkpage
        text = html_text(raw)
        sig["shell"] = len(text) < SHELL_MIN_CHARS
        sig["text_sha"] = sha(text)
        sig["snapshot_text"] = "\n".join(textwrap.wrap(text, 100))
        if etype == "linkpage":
            pat = entry.get("link_pattern", DEFAULT_LINK_RE)
            sig["links"] = sorted(set(re.findall(pat,
                                  raw.decode("utf-8", errors="replace"))))
    return sig


def verdict_for(entry: dict, prev: dict, resp: dict, sig: dict) -> tuple[str, str]:
    """Return (verdict, detail)."""
    if resp["status"].startswith(("robots", "offhost", "error")):
        return "UNREACHABLE", resp["status"]
    if resp["status"] == "304":
        return ("BLIND_SHELL" if prev.get("shell") and not entry.get("expect_shell")
                else "unchanged"), "304 not modified"
    if resp["status"] not in ("200",):
        return "UNREACHABLE", f"http {resp['status']}"
    if not prev:
        return "NEW", "no baseline yet"
    if entry.get("url") != prev.get("url"):
        return "URL_CHANGED_IN_CONFIG", f"baseline had {prev.get('url')}"
    if entry.get("type") == "linkpage" and sig["links"] != prev.get("links", []):
        added = [l for l in sig["links"] if l not in prev.get("links", [])]
        gone = [l for l in prev.get("links", []) if l not in sig["links"]]
        return "LINKS_CHANGED", f"+{len(added)} {added[:3]} / -{len(gone)} {gone[:3]}"
    if sig["text_sha"] != prev.get("text_sha"):
        return "CHANGED", "content text hash differs"
    if sig["page_updated"] != prev.get("page_updated", ""):
        return "DATE_CHANGED", f"'{prev.get('page_updated')}' -> '{sig['page_updated']}'"
    if sig["shell"] and not entry.get("expect_shell"):
        return "BLIND_SHELL", ("client-rendered app shell - hash cannot see "
                               "content changes; rely on MCSS / bulletin probe")
    return "unchanged", ""


def probe_bulletin(entry: dict, prev: dict, fetch: Fetcher) -> tuple[str, str, dict]:
    """Probe issueNumber N+1..N+probe_count for a new bulletin."""
    last = int(prev.get("last_seen_issue", entry.get("seed_issue", 0)))
    tmpl = entry["url_template"]
    found, notes = None, []
    for issue in range(last + 1, last + 1 + int(entry.get("probe_count", 3))):
        resp = fetch.get(tmpl.format(issue=issue), prev={})
        time.sleep(SLEEP)
        if resp["status"] != "200":
            notes.append(f"#{issue}:http{resp['status']}")
            continue
        text = html_text(resp.get("content", b""))
        if len(text) >= SHELL_MIN_CHARS:
            found = issue
            break
        notes.append(f"#{issue}:shell({len(text)}ch)")
    state = {"last_seen_issue": found or last, "url": tmpl}
    if found:
        return "NEW_ISSUE", f"issue {found} returned content", state
    return "PROBE_INCONCLUSIVE", ("; ".join(notes) +
            " - portal is client-rendered; MCSS email is the reliable detector"), state


# ------------------------------------------------------ manual_list entry ---
def parse_manual_list(raw: bytes, asset_base: str) -> tuple[list[dict], int | None]:
    """Parse a portal publication-list JSON into (documents, expected_count).

    Two parsers:
      * Directus/GraphQL branch (when the JSON has data.manuals): iterate the
        manuals array directly. doc_id = slug(stem of file.filename_download)
        (stable across revisions), title = manuals.title, url =
        asset_base + /assets/ + file.id, revision_date = file.modified_on as a
        RAW STRING. expected_count comes from manuals_aggregated (truncation
        tripwire). The generic scanner cannot handle this shape: it would emit
        the bare "00letter.pdf" as the URL and miss modified_on entirely
        (its key regex only looks for revis|date|publish|updated).
      * Generic fallback (any other portal): find leaf objects mentioning a
        .pdf and pull the path, a title, and a revision-date-looking field.

    expected_count is None when the endpoint carries no aggregate.
    """
    data = json.loads(raw.decode("utf-8", errors="replace"))

    # ---- Directus / GraphQL branch --------------------------------------
    if (isinstance(data, dict) and isinstance(data.get("data"), dict)
            and isinstance(data["data"].get("manuals"), list)):
        manuals = data["data"]["manuals"]
        expected: int | None = None
        agg = data["data"].get("manuals_aggregated")
        if isinstance(agg, list) and agg:
            try:
                expected = int(agg[0]["count"]["id"])
            except (KeyError, TypeError, ValueError):
                expected = None
        docs: list[dict] = []
        for m in manuals:
            if not isinstance(m, dict):
                continue
            f = m.get("file") or {}
            fid = (f.get("id") or "").strip()
            fname = f.get("filename_download") or ""
            if not fid:
                continue
            stem = Path(fname).stem if fname else fid
            base = asset_base.rstrip("/") if asset_base else ""
            docs.append({
                "doc_id": slug(stem),
                "title": m.get("title") or fname or stem,
                "url": f"{base}/assets/{fid}",
                "revision_date": str(f.get("modified_on") or ""),
                "file_id": fid,
            })
        return docs, expected

    # ---- Generic fallback (unchanged behavior) --------------------------
    leaves: list[dict] = []

    def collect(o):
        if isinstance(o, dict):
            own_pdf = any(isinstance(v, str) and ".pdf" in v.lower() for v in o.values())
            child_pdf = any(isinstance(v, (dict, list)) and ".pdf" in json.dumps(v).lower()
                            for v in o.values())
            if own_pdf and not child_pdf:
                leaves.append(o)
            else:
                for v in o.values():
                    collect(v)
        elif isinstance(o, list):
            for v in o:
                collect(v)

    collect(data)
    docs = []
    for e in leaves:
        url = next((v for v in e.values()
                    if isinstance(v, str) and ".pdf" in v.lower()), None)
        if not url:
            continue
        if url.startswith("/") and asset_base:
            url = asset_base.rstrip("/") + url
        title = next((e[k] for k in ("title", "name", "documentTitle",
                                     "fileName", "label")
                      if isinstance(e.get(k), str)), None) \
            or Path(url.split("?")[0]).name
        rev = ""
        for k, v in e.items():
            if isinstance(v, (str, int)) and re.search(r"revis|date|publish|updated",
                                                       str(k), re.I):
                rev = str(v)
                if re.search(r"revis", str(k), re.I):
                    break
        docs.append({"doc_id": slug(Path(url.split("?")[0]).stem),
                     "title": title, "url": url, "revision_date": rev,
                     "file_id": ""})
    return docs, None


# --------------------------------------------------------- snapshot layer ---
class SnapshotStore:
    """Stores extracted text per source and produces diff reports on change.

    All writes are best-effort: on a read-only filesystem (Vercel) the layer
    degrades to hash-only detection, which matches v1.2 behavior.
    """

    def __init__(self, snap_dir: Path, diff_dir: Path,
                 tracked: dict[str, dict] | None = None):
        self.snap_dir = snap_dir
        self.diff_dir = diff_dir
        self.written: list[str] = []
        self.tracked = tracked or {}
        # per-source structured code candidates and effective-date phrases
        # from the latest CHANGED diff, keyed by the row id (eid / cid)
        self.codes: dict[str, list[dict]] = {}
        self.effective: dict[str, list[str]] = {}

    def _path(self, program: str, eid: str) -> Path:
        return self.snap_dir / program / f"{eid}.txt"

    def handle(self, program: str, eid: str, verdict: str, sig: dict,
               entry_url: str, extra: dict | None = None) -> str:
        """Store snapshot; on CHANGED, write a diff report. Returns report path or ''."""
        text = sig.get("snapshot_text", "")
        if not text:
            return ""
        try:
            p = self._path(program, eid)
            report_path = ""
            if verdict == "CHANGED" and p.exists():
                old = p.read_text(encoding="utf-8")
                dl = list(difflib.unified_diff(
                    old.splitlines(), text.splitlines(),
                    fromfile="previous", tofile="current", lineterm="", n=2))
                codes = extract_code_entries(dl, old, text, self.tracked)
                self.codes[eid] = codes
                self.effective[eid] = effective_dates_in_diff(dl)
                is_pdf = bool(PAGE_MARK.search(text) or PAGE_MARK.search(old))
                if len(dl) > DIFF_MAX_LINES:
                    dl = dl[:DIFF_MAX_LINES] + [
                        "", f"[diff truncated at {DIFF_MAX_LINES} lines; full prior "
                            f"text is in git history of {p}]"]
                self.diff_dir.mkdir(parents=True, exist_ok=True)
                stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
                rp = self.diff_dir / f"{stamp}_{program}--{eid}.md"
                lines = [f"# Change: {eid}", "",
                         f"- Program: {program}",
                         f"- Source: {entry_url}",
                         f"- Detected: {now_iso()}"]
                for k, v in (extra or {}).items():
                    lines.append(f"- {k}: {v}")
                lines += ["",
                          "Verify against the live official source before acting.",
                          "Machine-extracted text; diffs can contain extraction noise.",
                          ""]
                if codes:
                    lines += ["## Possible billing codes touched",
                              "",
                              "Heuristic extraction from changed lines only - "
                              "**verify every row against the live source "
                              "before acting**. Page numbers come from the "
                              "extracted-text snapshot"
                              + (" and link into the PDF." if is_pdf
                                 else "; this source is not a PDF, so no page "
                                      "links.") ,
                              "",
                              "| Code | System | Direction | Confidence | "
                              "Tracked | Page | Context (excerpt) |",
                              "|---|---|---|---|---|---|---|"]
                    for e in codes:
                        tr = (f"**TRACKED** {md_cell(e['master_row'])}".strip()
                              if e["tracked"] else "")
                        lines.append(
                            f"| `{e['code']}` | {e['system']} | {e['direction']} "
                            f"| {e['confidence']} | {tr} "
                            f"| {page_link(entry_url, e['page'], is_pdf)} "
                            f"| {md_cell(e['context'])} |")
                    lines.append("")
                lines += ["## Text diff (previous -> current)", "", "```diff",
                          "\n".join(dl), "```", ""]
                rp.write_text("\n".join(lines), encoding="utf-8")
                report_path = str(rp)
                self.written.append(report_path)
            if verdict in ("NEW", "CHANGED"):
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(text, encoding="utf-8")
            return report_path
        except OSError:
            return ""    # read-only venue: hash-only mode


# -------------------------------------------------------------------- run ---
def get_with_retry(fetch: Fetcher, url: str, prev: dict, tries: int = 2) -> dict:
    for attempt in range(tries):
        try:
            return fetch.get(url, prev)
        except requests.RequestException:
            if attempt + 1 == tries:
                raise
            time.sleep(3)


def get_with_retry_auth(fetch: Fetcher, url: str, prev: dict,
                        headers: dict, tries: int = 2) -> dict:
    for attempt in range(tries):
        try:
            return fetch.get_auth(url, prev, headers)
        except requests.RequestException:
            if attempt + 1 == tries:
                raise
            time.sleep(3)


def read_bundle_token(fetch: Fetcher, url: str, pattern: str | None) -> str:
    """Read a static public token out of a SPA runtime-config bundle. Returns
    the token or "". Never logs the value."""
    try:
        resp = fetch.get(url, {})
        if resp.get("status") != "200":
            return ""
        text = resp.get("content", b"").decode("utf-8", errors="replace")
        m = re.search(pattern or DIRECTUS_TOKEN_RE, text)
        return m.group(1).strip() if m else ""
    except Exception:
        return ""


def auth_headers(token: str) -> dict:
    """Wrap a token as an Authorization header. Accepts a bare token or a
    value that already includes the scheme."""
    if not token:
        return {}
    value = token if token.lower().startswith("bearer ") else f"Bearer {token}"
    return {"Authorization": value}


def load_watchlist(path: Path, only: list[str] | None) -> list[dict]:
    cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
    entries = []
    for program, block in cfg.get("programs", {}).items():
        if only and program not in only:
            continue
        if not only and not block.get("enabled", True):
            continue
        for e in block.get("entries", []):
            e["program"] = program
            entries.append(e)
    return entries


def check_manual_list(entry: dict, base: dict, fetch: Fetcher, snaps: SnapshotStore,
                      ts: str) -> tuple[list[dict], dict]:
    """Process one manual_list entry. Returns (rows, new_base_fragment)."""
    eid, program = entry["id"], entry["program"]
    rows: list[dict] = []
    frag: dict = {}

    def row(rid, verdict, detail, url="", page_updated="", report=""):
        return {"program": program, "id": rid, "checked_at": ts,
                "type": "manual_list", "verdict": verdict, "detail": detail,
                "page_updated": page_updated, "shell": "", "http": "",
                "url": url or entry.get("url", ""),
                "master_keys": ";".join(entry.get("master_keys", [])),
                "master_note": entry.get("master_note", ""),
                "note": entry.get("note", ""), "diff_report": report}

    if not entry.get("url"):
        rows.append(row(eid, "CONFIG_TODO",
                        "manual_list url is empty - paste the portal JSON "
                        "endpoint (README: one-time DevTools step)"))
        frag[eid] = base.get(eid, {})
        return rows, frag

    portal = entry.get("portal_page") or entry.get("url", "")

    # -- credential resolution: env secret preferred, static bundle token as
    #    a self-healing fallback (read-only Directus SPAs bake a public token
    #    into their runtime config; if MCWEB_TOKEN is unset/rotated we re-read
    #    the current one). No token value is ever logged or stored.
    env_name = entry.get("auth_header_env")
    token = (os.environ.get(env_name) or "").strip() if env_name else ""
    bundle_url = entry.get("token_bundle_url")
    bundle_re = entry.get("token_bundle_re")
    used_bundle = False
    if not token and bundle_url:
        token = read_bundle_token(fetch, bundle_url, bundle_re)
        used_bundle = bool(token)
    hdrs = auth_headers(token)
    method = (entry.get("method") or "GET").upper()

    def list_fetch(h):
        for attempt in range(2):
            try:
                if method == "POST":
                    return fetch.post_json(entry["url"],
                                           entry.get("graphql_body") or {}, h)
                return fetch.get_auth(entry["url"], {}, h)
            except requests.RequestException:
                if attempt == 1:
                    raise
                time.sleep(3)

    try:
        resp = list_fetch(hdrs)
    except requests.RequestException as exc:
        rows.append(row(eid, "UNREACHABLE", f"list endpoint error: {exc}"))
        frag[eid] = base.get(eid, {})
        return rows, frag
    time.sleep(SLEEP)
    # Self-heal: an auth failure with the env token means it was rotated; pull
    # the fresh public token from the bundle and retry once.
    if resp["status"] in ("400", "401", "403") and not used_bundle and bundle_url:
        token = read_bundle_token(fetch, bundle_url, bundle_re)
        if token:
            hdrs, used_bundle = auth_headers(token), True
            try:
                resp = list_fetch(hdrs)
            except requests.RequestException as exc:
                rows.append(row(eid, "UNREACHABLE", f"list endpoint error: {exc}"))
                frag[eid] = base.get(eid, {})
                return rows, frag
            time.sleep(SLEEP)

    if resp["status"] != "200":
        hint = ("" if hdrs else " (no credential: set MCWEB_TOKEN or a "
                "token_bundle_url)")
        rows.append(row(eid, "UNREACHABLE",
                        f"list endpoint http {resp['status']}{hint}", url=portal))
        frag[eid] = base.get(eid, {})
        return rows, frag
    try:
        docs, expected = parse_manual_list(resp["content"], entry.get("asset_base", ""))
    except Exception as exc:
        rows.append(row(eid, "UNREACHABLE", f"list endpoint parse error: {exc}"))
        frag[eid] = base.get(eid, {})
        return rows, frag
    if not docs:
        rows.append(row(eid, "CONFIG_TODO",
                        "endpoint returned JSON but no documents were parsed - "
                        "adjust parse_manual_list for this portal shape", url=portal))
        frag[eid] = base.get(eid, {})
        return rows, frag

    # Truncation tripwire: the aggregate must equal the array length, else the
    # list came back short (paging/filter regression) and we flag the parent.
    if expected is not None and expected != len(docs):
        rows.append(row(eid, "LIST_TRUNCATED",
                        f"aggregate count {expected} != {len(docs)} parsed docs; "
                        "list may be truncated or filtered - verify the portal",
                        url=portal))

    prev_parent = base.get(eid, {})
    prev_docs = set(prev_parent.get("docs", []))
    seen = []
    limit = int(entry.get("max_docs", 0))
    for d in docs[: limit or len(docs)]:
        cid = f"{eid}--{d['doc_id']}"
        seen.append(d["doc_id"])
        prev = base.get(cid, {})
        try:
            dresp = get_with_retry_auth(fetch, d["url"], prev, hdrs)
        except requests.RequestException as exc:
            rows.append(row(cid, "UNREACHABLE", f"error:{exc}", url=d["url"],
                            page_updated=d["revision_date"]))
            frag[cid] = prev
            continue
        time.sleep(SLEEP)
        status = dresp["status"]

        # Degrade path: the list is readable but the asset is not (token scoped
        # to collections, not directus_files). Do NOT cry UNREACHABLE - the
        # portal metadata still tells us whether the section moved. Compare the
        # raw revision_date and file.id; this comparison runs even though the
        # fetch failed (previously it was skipped on any non-200).
        if status in ("401", "403"):
            rev_prev = prev.get("revision_date", "")
            fid_prev = prev.get("file_id", "")
            meta_changed = ((d["revision_date"] or "") != rev_prev
                            or (d.get("file_id", "") != fid_prev))
            if not prev:
                verdict = "CHANGED_METADATA_ONLY"
                detail = (f"assets blocked (http {status}); metadata recorded, "
                          f"no baseline yet. No text diff - read the section at "
                          f"{portal}")
            elif meta_changed:
                verdict = "CHANGED_METADATA_ONLY"
                detail = (f"assets blocked (http {status}); portal revision "
                          f"'{rev_prev}' -> '{d['revision_date']}' (file.id "
                          f"{'changed' if d.get('file_id','') != fid_prev else 'same'}). "
                          f"No text diff available - read the section at {portal}")
            else:
                verdict = "metadata_only_unchanged"
                detail = f"assets blocked (http {status}); portal metadata unchanged"
            frag[cid] = {**prev, "url": d["url"], "title": d["title"],
                         "revision_date": d["revision_date"],
                         "file_id": d.get("file_id", ""), "checked_at": ts}
            rows.append(row(cid, verdict, detail, url=d["url"],
                            page_updated=d["revision_date"]))
            continue

        sig = signature({"type": "pdf", "id": cid, "url": d["url"]}, dresp)
        verdict, detail = verdict_for({"type": "pdf", "url": d["url"]},
                                      prev, dresp, sig)
        # URL churn (a new file.id per revision) is expected on portals; the
        # document identity is the doc_id, so resolve URL_CHANGED_IN_CONFIG by
        # content hash instead.
        if verdict == "URL_CHANGED_IN_CONFIG":
            if sig["text_sha"] != prev.get("text_sha"):
                verdict, detail = "CHANGED", "content text hash differs"
            else:
                verdict, detail = "unchanged", "url token rotated, content same"
        # A metadata-only seed carries revision_date + file.id but no text_sha.
        # The first successful fetch establishes the hash: keep it quiet ONLY
        # when the portal metadata still matches the seed; a metadata drift is
        # a real change and must stay flagged.
        hash_pending = bool(prev) and not prev.get("text_sha") and prev.get("revision_date")
        meta_same = ((d["revision_date"] or "") == prev.get("revision_date", "")
                     and d.get("file_id", "") == prev.get("file_id", ""))
        if verdict == "CHANGED" and hash_pending and meta_same:
            verdict, detail = "unchanged", "seed baseline hash established"
        rev_prev = prev.get("revision_date", "")
        if verdict == "unchanged" and (d["revision_date"] or "") != rev_prev:
            verdict = "DATE_CHANGED"
            detail = f"portal revision date '{rev_prev}' -> '{d['revision_date']}'"
        report = snaps.handle(entry["program"], cid, verdict, sig, d["url"],
                              extra={"Title": d["title"],
                                     "Portal revision date": d["revision_date"] or "n/a"})
        if status == "304":
            frag[cid] = {**prev, "checked_at": ts,
                         "revision_date": d["revision_date"] or rev_prev,
                         "file_id": d.get("file_id", "") or prev.get("file_id", "")}
        elif status == "200":
            frag[cid] = {"url": d["url"], "title": d["title"],
                         "revision_date": d["revision_date"],
                         "file_id": d.get("file_id", ""),
                         **{k: sig[k] for k in ("text_sha", "byte_sha",
                                                "page_updated", "links", "shell")},
                         "etag": dresp.get("etag", ""),
                         "last_modified": dresp.get("last_modified", ""),
                         "checked_at": ts}
        else:
            frag[cid] = prev
        rows.append(row(cid, verdict, detail, url=d["url"],
                        page_updated=d["revision_date"] or sig.get("page_updated", ""),
                        report=report))

    for gone in sorted(prev_docs - set(seen)):
        rows.append(row(f"{eid}--{gone}", "REMOVED",
                        "document no longer in the portal list"))
    frag[eid] = {"url": entry["url"], "docs": seen, "checked_at": ts}
    return rows, frag


# --------------------------------------------------------------- dashboard --
# GitHub Pages serves the /docs folder only, so a repo-relative link like
# reports/diffs/x.md 404s on the published site, and viewed on github.com it
# resolves relative to docs/ (also wrong). Every generated link is therefore
# an absolute github.com URL. OWNER/REPO comes from the GITHUB_REPOSITORY env
# var that Actions always sets, with a hardcoded fallback for local runs.
REPO_FALLBACK = "mp321/RevInt-SourceWatch"


def repo_slug() -> str:
    return (os.environ.get("GITHUB_REPOSITORY") or "").strip() or REPO_FALLBACK


def blob_url(rel_path: str) -> str:
    return f"https://github.com/{repo_slug()}/blob/main/{rel_path}"


def tree_url(rel_path: str) -> str:
    return f"https://github.com/{repo_slug()}/tree/main/{rel_path}"


def pages_home_url() -> str:
    owner, _, repo = repo_slug().partition("/")
    return f"https://{owner}.github.io/{repo}/"


def repo_rel(p: str) -> str:
    """Reduce a diff-report path (absolute on some venues) to the repo-relative
    posix path git tracks, e.g. reports/diffs/x.md."""
    parts = Path(p).parts
    if "reports" in parts:
        parts = parts[parts.index("reports"):]
    return "/".join(parts)


def md_cell(s) -> str:
    """Free text -> safe on one markdown line. detail can carry '|' (multiple
    page_updated stamps are '|'-joined and get embedded in DATE_CHANGED
    details), '<...>' (requests exception reprs), and newlines; unescaped
    they break GFM tables and get eaten as HTML. That is why v1.3 omitted
    detail from the dashboard instead of escaping it."""
    s = re.sub(r"\s+", " ", str(s)).strip()
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace("|", "&#124;"))


def esc(s) -> str:
    """HTML-escape free text for the <details> fine-print blocks."""
    return html.escape(re.sub(r"\s+", " ", str(s)).strip(), quote=True)


QUIET = {"unchanged", "metadata_only_unchanged"}
GAPS = {"UNREACHABLE", "CONFIG_TODO"}    # fixable monitoring gaps
CADENCE_NOTE = "Checked by the weekly Monday run (14:00 UTC GitHub Action)."

PROGRAM_NAMES = {
    "fpact": "Family PACT",
    "medi_cal_ffs": "Medi-Cal FFS",
    "managed_medi_cal": "Managed Medi-Cal",
    "fqhc": "FQHC",
    "medi_cal_rx": "Medi-Cal Rx",
    "ncci": "NCCI",
}

TYPE_HOW = {
    "pdf": "The PDF is downloaded (conditional GET - the server may answer "
           "'304 not modified' and skip the download), its text is extracted "
           "and hashed, and the hash is compared with the previous run.",
    "html": "The page is downloaded (conditional GET), scripts and styles are "
            "stripped, and the visible text is hashed and compared with the "
            "previous run.",
    "linkpage": "The page's visible text is hashed AND every file link "
                "matching the entry's pattern is collected; a new or removed "
                "link is flagged even when the page text is unchanged.",
    "binary": "The raw file bytes are hashed and compared; no text is "
              "extracted, so this entry can never produce a text diff.",
    "bulletin_probe": "The checker requests the next few issue numbers of the "
                      "bulletin URL to see whether a new issue returns real "
                      "content.",
    "manual_list": "The portal's JSON list endpoint is queried; every document "
                   "it lists is watched individually (PDF text hash plus the "
                   "portal's revision date). New documents are auto-discovered "
                   "and removals are flagged.",
}

# badge kind -> (label, text color, background). Plain inline-styled spans,
# not emoji: they render identically everywhere Jekyll/kramdown outputs raw
# HTML, need no font support, and read fine to a screen reader.
BADGE_STYLE = {
    "review": ("Needs review", "#7a271a", "#ffebe9"),
    "gap":    ("Can't verify", "#7a4a00", "#fff6e0"),
    "ok":     ("Clear",        "#0f5132", "#e6f4ea"),
    "unknown": ("Unknown",     "#374151", "#f1f3f5"),
}


def badge(kind: str) -> str:
    label, fg, bg = BADGE_STYLE.get(kind, BADGE_STYLE["unknown"])
    return (f'<span style="display:inline-block;padding:.1em .6em;'
            f'border-radius:1em;font-size:.82em;font-weight:600;'
            f'background:{bg};color:{fg};white-space:nowrap">{label}</span>')


# status -> (badge kind, what it means, what the reader should do)
VERDICT_LEGEND: list[tuple[str, str, str, str]] = [
    ("CHANGED", "review",
     "The extracted text of this source differs from the last run.",
     "Open the diff to see the exact lines, re-read that part of the live "
     "source, then verify the listed Master rows (superbill, tipsheet, Epic "
     "review as applicable)."),
    ("NEW", "review",
     "First run for this source; its current state became the baseline.",
     "Skim the source once to confirm it is the right document."),
    ("DATE_CHANGED", "review",
     "A revision or 'page updated' stamp moved but the content text did not.",
     "Open the source and confirm nothing substantive changed; usually a "
     "republish."),
    ("LINKS_CHANGED", "review",
     "The set of files this page links to changed (often a re-versioned "
     "filename, e.g. a new Superbill).",
     "Open the page, find the added or removed file named in Why, and if a "
     "watched file was re-versioned, point watchlist.yaml at the new URL."),
    ("NEW_ISSUE", "review",
     "A probed bulletin issue number returned real content.",
     "Read the new bulletin and triage anything affecting the Master sheet."),
    ("REMOVED", "review",
     "A document disappeared from the portal's list.",
     "Check the portal: retired, renamed, or moved? Update the Master sheet "
     "reference if the section is gone."),
    ("URL_CHANGED_IN_CONFIG", "review",
     "The URL in watchlist.yaml differs from the URL the baseline was built "
     "from.",
     "Confirm the new URL is intentional; the next run with --update "
     "re-baselines it."),
    ("CHANGED_METADATA_ONLY", "review",
     "The portal says this section was revised (new revision date or file id) "
     "but the PDF itself could not be downloaded, so there is no text diff.",
     "Open the section on the portal, re-read it, and verify the listed "
     "Master rows."),
    ("LIST_TRUNCATED", "review",
     "The portal returned fewer documents than its own count claims.",
     "Open the portal list and compare; some sections may be silently "
     "unmonitored until this clears."),
    ("UNREACHABLE", "gap",
     "The fetch failed this run (HTTP error, network error, robots.txt, or an "
     "off-site redirect) - the Why line says which.",
     "If it persists more than one run, open the URL in a browser; the page "
     "may have moved. Then fix watchlist.yaml. Until then this source is "
     "unmonitored."),
    ("MANUAL_REVIEW", "gap",
     "This source cannot be fetched automatically, by design (reason in the "
     "fine print).",
     "Open the link by hand on the cadence given in the fine print; MCSS "
     "email is the push detector."),
    ("BLIND_SHELL", "gap",
     "The page builds its content with JavaScript, so the checker sees only "
     "an empty app shell and cannot detect content changes.",
     "Do not rely on this row for detection; MCSS email covers it. Open the "
     "page yourself when in doubt."),
    ("PROBE_INCONCLUSIVE", "gap",
     "The bulletin probe could not confirm or rule out a new issue "
     "(client-rendered portal).",
     "Nothing to do; MCSS email is the reliable detector for bulletins."),
    ("CONFIG_TODO", "gap",
     "The watchlist entry is incomplete, so nothing is monitored for it yet.",
     "Finish the entry in watchlist.yaml; the Why line says what is missing."),
    ("unchanged", "ok",
     "No change detected.",
     "Nothing to do."),
    ("metadata_only_unchanged", "ok",
     "The PDF is not directly downloadable, but the portal's revision "
     "metadata is unchanged.",
     "Nothing to do."),
]
VERDICT_HELP = {v: (kind, meaning, action)
                for v, kind, meaning, action in VERDICT_LEGEND}


def kind_for(verdict: str) -> str:
    if verdict in VERDICT_HELP:
        return VERDICT_HELP[verdict][0]
    if verdict in NEEDS_REVIEW:
        return "review"
    if verdict in QUIET:
        return "ok"
    return "unknown"


def badge_for(verdict: str) -> str:
    return badge(kind_for(verdict))


def action_for(verdict: str) -> str:
    return VERDICT_HELP.get(verdict, ("", "", "Review the Why text and the "
                                      "fine print for this source."))[2]


def plain_why(r: dict) -> str:
    """One plain-English sentence for the row's detail (verbatim where it is
    already prose, translated where it is a status code)."""
    d = re.sub(r"\s+", " ", str(r.get("detail") or "")).strip()
    if r.get("verdict") == "UNREACHABLE":
        if d.startswith("robots"):
            return "The site's robots.txt forbids automated fetching."
        if d.startswith("offhost_redirect:"):
            return (f"The URL redirected off-site (to {d.split(':', 1)[1]}); "
                    "the checker refuses off-site redirects, so nothing was "
                    "read.")
        if d.startswith("error:"):
            return f"Network error while fetching: {d[len('error:'):]}"
        if d.startswith("http "):
            code = d[len("http "):]
            hint = " - the page is missing or has moved" if code == "404" else ""
            return f"The server answered HTTP {code}{hint}."
    return d


def last_change_map(log_path: Path | None) -> dict[str, tuple[str, str]]:
    """id -> (generated, verdict) of the latest change-log event. The log is
    append-only chronological, so the last row per id wins."""
    out: dict[str, tuple[str, str]] = {}
    if not log_path or not Path(log_path).exists():
        return out
    try:
        with Path(log_path).open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if row.get("id"):
                    out[row["id"]] = (row.get("generated", ""),
                                      row.get("verdict", ""))
    except OSError:
        pass
    return out


def fine_print(r: dict, last_change: dict[str, tuple[str, str]]) -> list[str]:
    """One <details> block of pure HTML (kramdown and GFM both pass raw HTML
    through but do not process markdown inside it, so no markdown in here)."""
    is_manual = r.get("http") == "manual"
    url = r.get("url", "")
    li: list[str] = []
    if url:
        li.append(f'<li><b>URL checked:</b> <a href="{esc(url)}">{esc(url)}</a>'
                  + (" (template; {issue} is the probed issue number)"
                     if r.get("type") == "bulletin_probe" else "") + "</li>")
    else:
        li.append("<li><b>URL checked:</b> none configured yet.</li>")
    if is_manual:
        li.append("<li><b>How:</b> Not fetched automatically. The weekly run "
                  "lists it every time as a standing reminder.</li>")
        li.append(f"<li><b>Why it cannot be auto-checked:</b> "
                  f"{esc(r.get('detail') or 'no reason recorded')}</li>")
        li.append(f'<li><b>What to do instead:</b> Open it yourself: '
                  f'<a href="{esc(url)}">{esc(url)}</a>. Follow the cadence in '
                  f"the reason above; if none is stated, re-read it when "
                  f"program news suggests a change.</li>")
    else:
        how = TYPE_HOW.get(r.get("type", "html"), TYPE_HOW["html"])
        li.append(f"<li><b>How:</b> {how} {CADENCE_NOTE}</li>")
        li.append(f"<li><b>This run:</b> {esc(r.get('verdict', ''))}"
                  + (f" - {esc(r['detail'])}" if r.get("detail") else "")
                  + "</li>")
    if r.get("shell") is True and not is_manual:
        li.append("<li><b>Blind spot:</b> This page is client-rendered - the "
                  "checker sees only the app shell and cannot detect content "
                  "changes. Detection relies on the MCSS email subscription; "
                  f'open the page yourself when in doubt: <a href="{esc(url)}">'
                  f"{esc(url)}</a></li>")
    checked = (r.get("checked_at") or "")[:10]
    li.append(f"<li><b>Last checked:</b> "
              f"{checked if checked else 'never fetched automatically'}</li>")
    lc = last_change.get(r.get("id", ""))
    li.append("<li><b>Last recorded change:</b> "
              + (f"{lc[0][:10]} ({esc(lc[1])})" if lc
                 else "none since the change log began") + "</li>")
    if r.get("note"):
        li.append(f"<li><b>Watchlist note:</b> {esc(r['note'])}</li>")
    keys, scope = r.get("master_keys", ""), r.get("master_note", "")
    if keys or scope:
        li.append("<li><b>Master rows to verify on change:</b> "
                  + " - ".join(x for x in
                               (f"<code>{esc(keys)}</code>" if keys else "",
                                esc(scope) if scope else "") if x) + "</li>")
    else:
        li.append("<li><b>Master rows to verify on change:</b> none mapped in "
                  "the watchlist; triage by judgment.</li>")
    if r.get("diff_report"):
        rel = repo_rel(r["diff_report"])
        li.append(f'<li><b>Latest diff report:</b> <a href="{blob_url(rel)}">'
                  f"{esc(rel)}</a></li>")
    # Loose line-height and left indent so a long run of fine print doesn't
    # read as one dense wall of text; kept inline since Pages markdown does
    # not process a class attribute against an external stylesheet here.
    return (["<details style=\"margin:.3em 0 1.1em 2em\">",
             "<summary>Details: exactly what is checked here, how, and "
             "its caveats</summary>",
             '<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">']
            + li + ["</ul>", "</details>"])


def needs_review_item(r: dict) -> list[str]:
    title = (f"[{r['id']}]({r['url']})" if r.get("url") else f"`{r['id']}`")
    out = [f"- {badge_for(r['verdict'])} `{r['verdict']}` - {title} "
           f"_({PROGRAM_NAMES.get(r['program'], r['program'])})_",
           f"  - **What happened:** {md_cell(plain_why(r)) or 'no detail recorded.'}",
           f"  - **What to do:** {md_cell(action_for(r['verdict']))}"]
    if r.get("diff_report"):
        rel = repo_rel(r["diff_report"])
        out.append(f"  - **Exact change:** [{md_cell(rel)}]({blob_url(rel)})")
    elif r["verdict"] == "CHANGED":
        out.append("  - **Exact change:** no diff was written this run (no "
                   "prior text snapshot to compare against) - compare the "
                   "live source with your last known state.")
    codes = r.get("codes_touched") or []
    if codes:
        url = r.get("url", "")
        is_pdf = any(e["page"] is not None for e in codes)
        shown = codes[:8]
        parts = []
        for e in shown:
            ref = f"`{e['code']}` ({e['system']}, {e['direction']}"
            if e["confidence"] != "high":
                ref += f", {e['confidence']} conf."
            ref += ")"
            if e["tracked"]:
                ref = "**TRACKED** " + ref
            pl = page_link(url, e["page"], is_pdf)
            if pl:
                ref += f" {pl}"
            parts.append(ref)
        more = f" - plus {len(codes) - 8} more in the diff report" \
            if len(codes) > 8 else ""
        out.append("  - **Codes touched (heuristic, verify each):** "
                   + "; ".join(parts) + more)
    if r.get("comms_draft"):
        rel = repo_rel(r["comms_draft"])
        out.append(f"  - **Comms draft (DRAFT - human review required "
                   f"before any distribution):** [{md_cell(rel)}]"
                   f"({blob_url(rel)})")
    if r.get("page_updated"):
        out.append(f"  - **Revision stamp:** {md_cell(r['page_updated'])}")
    keys, scope = r.get("master_keys", ""), r.get("master_note", "")
    if keys or scope:
        out.append("  - **Master rows to verify:** "
                   + " - ".join(x for x in
                                (f"`{md_cell(keys)}`" if keys else "",
                                 md_cell(scope) if scope else "") if x))
    else:
        out.append("  - **Master rows to verify:** none mapped in the "
                   "watchlist; triage by judgment.")
    return out


def write_dashboard(path: Path, report: dict,
                    log_path: Path | None = None) -> None:
    """Render the GitHub Pages status page from a run report.

    Output is deterministic for a given report + change log: programs and
    sources are sorted alphabetically and all links derive from
    GITHUB_REPOSITORY (fallback REPO_FALLBACK), so the weekly commit diff
    stays readable. Plain markdown + raw HTML <details> only - Jekyll's
    default (primer) theme renders it with no client-side build step.
    """
    last_change = last_change_map(log_path)
    results = sorted(report["results"], key=lambda r: (r["program"], r["id"]))
    flagged = [r for r in results if r["verdict"] in NEEDS_REVIEW]
    gaps = [r for r in results if r["verdict"] in GAPS]

    lines = [
        "# Revenue Integrity Source Watch", "",
        "Automated monitor for the official billing sources behind the",
        "Revenue Integrity registry. **Alert tool only, not a source of",
        "record.** Verify every flagged item against the live official source",
        "before acting on it.", "",
        "Each week a GitHub Action fetches every source listed below, compares "
        "it against the copy from the previous run, and flags anything that "
        "changed, disappeared, or could not be checked. A flag here does not "
        "mean the Master sheet is wrong - it means a human should re-read that "
        "source and confirm whether anything downstream needs to change. For "
        f"source definitions, run history, and the full codebase, see the "
        f"[GitHub repository](https://github.com/{repo_slug()}).", "",
        f"**Last run:** {report['generated']} - **Needs review: "
        f"{len(flagged)}**", "",
        "Where to click: "
        f"[change review page]({pages_home_url()}changes.html) · "
        f"[change log (CSV)]({blob_url('reports/changes_log.csv')}) · "
        f"[reports folder]({tree_url('reports')}) (diff reports land in "
        "`reports/diffs/`) · "
        f"[latest raw report (JSON)]({blob_url('reports/latest_report.json')}) · "
        f"[watchlist definition]({blob_url('watchlist.yaml')})", "",
        "Statuses like `CHANGED` or `BLIND_SHELL` are explained in the "
        "[status legend](#status-legend) at the bottom of this page.", "",
    ]

    lines += [f"## Needs review since last run ({len(flagged)})", ""]
    if flagged:
        lines.append("Work this list top to bottom; every item links straight "
                     "to the source and, when text changed, to the exact diff.")
        lines.append("")
        for r in flagged:
            lines += needs_review_item(r)
        lines.append("")
    else:
        lines += [f"{badge('ok')} Nothing needs review from the last run.", ""]

    if gaps:
        lines += [f"### Could not be checked automatically ({len(gaps)})", "",
                  "Monitoring gaps, not confirmed source changes - these "
                  "sources are effectively unwatched until fixed. "
                  "(Permanently manual or blind entries - MANUAL_REVIEW, "
                  "BLIND_SHELL, PROBE_INCONCLUSIVE - are by design and listed "
                  "in their program sections with the reason in the fine "
                  "print.)", ""]
        for r in gaps:
            title = (f"[{r['id']}]({r['url']})" if r.get("url")
                     else f"`{r['id']}`")
            lines += [f"- {badge_for(r['verdict'])} `{r['verdict']}` - {title} "
                      f"_({PROGRAM_NAMES.get(r['program'], r['program'])})_",
                      f"  - **Why:** {md_cell(plain_why(r))}",
                      f"  - **What to do:** {md_cell(action_for(r['verdict']))}"]
        lines.append("")

    def anchor(name: str, prog: str) -> str:
        return re.sub(r"[^a-z0-9]+", "-", f"{name} {prog}".lower()).strip("-")

    progs = sorted({r["program"] for r in results})
    lines += ["## All sources by program", "",
              "Programs on this page (every watched source, including the "
              "quiet ones):", ""]
    for prog in progs:
        rs = [r for r in results if r["program"] == prog]
        name = PROGRAM_NAMES.get(prog, prog)
        n_flag = sum(1 for r in rs if r["verdict"] in NEEDS_REVIEW)
        lines.append(f"- [{name}](#{anchor(name, prog)}) - {len(rs)} source"
                     f"{'s' if len(rs) != 1 else ''}"
                     + (f", {n_flag} needs review" if n_flag else ""))
    lines += ["",
              "Each block: the status line first, then (indented) the source "
              "link and a Details fold-out with exactly what is checked and "
              "its caveats.", ""]
    for prog in progs:
        rs = [r for r in results if r["program"] == prog]
        name = PROGRAM_NAMES.get(prog, prog)
        lines += [f"### {name} (`{prog}`)", ""]
        for r in rs:
            lines.append(f"#### {badge_for(r['verdict'])} {r['id']} - "
                         f"`{r['verdict']}`")
            lines.append("")
            bits = []
            if r.get("url"):
                bits.append(f'<a href="{esc(r["url"])}">Open the source</a>')
            if r.get("page_updated"):
                bits.append(f"revision {esc(r['page_updated'])}")
            checked = (r.get("checked_at") or "")[:10]
            bits.append(f"checked {checked}" if checked
                        else "not fetched automatically")
            if r.get("diff_report"):
                rel = repo_rel(r["diff_report"])
                bits.append(f'<a href="{blob_url(rel)}">text diff</a>')
            lines += [f'<p style="margin:.2em 0 .2em 2em">'
                      f'{" - ".join(bits)}</p>', ""]
            if r["verdict"] not in QUIET:
                lines += [f'<p style="margin:.2em 0 .2em 2em"><b>Why:</b> '
                          f'{esc(plain_why(r)) or "no detail recorded."}</p>',
                          ""]
            lines += fine_print(r, last_change)
            lines.append("")

    lines += ["### Source URLs at a glance", "",
              "Plain list of every URL this page's data comes from.", "",
              "```text"]
    for prog in progs:
        for r in (r for r in results if r["program"] == prog):
            if r.get("url"):
                lines.append(f"{r['id']}: {r['url']}")
    lines += ["```", ""]

    lines += ["## Status legend", ""]
    lines.append('<table style="font-size:.85em;line-height:1.45">')
    lines.append("<tr><th>Status</th><th>Code</th>"
                 "<th>What it means, and what to do</th></tr>")
    for v, kind, meaning, action in VERDICT_LEGEND:
        lines.append(f"<tr><td>{badge(kind)}</td><td><code>{esc(v)}</code></td>"
                     f"<td>{esc(meaning)} <i>{esc(action)}</i></td></tr>")
    lines += ["</table>", ""]

    lines += ["---", "",
              "If the last run shown at the top of this page is more than 35 "
              "days old, this monitor may not be active or may need an "
              "update - notify the maintainer.", "",
              "This page is regenerated on every run by `write_dashboard` in "
              f"[source_check.py]({blob_url('source_check.py')}); edit that, "
              "not this file. Alert tool only - verify against the live "
              "official source.", "",
              f"Built and maintained by "
              f"[Michael Phipps](https://github.com/mp321). See the "
              f"[repository]({f'https://github.com/{repo_slug()}'}) for "
              "source, history, and license terms.", ""]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_changes_page(path: Path, report: dict,
                       log_path: Path | None = None) -> None:
    """Team-facing change review page (docs/changes.md, published on Pages
    next to the dashboard). One block per item needing review: what changed
    in plain language, the exact codes with page-anchored deep links into the
    source, and the full diff. Built for minimal reading - every line points
    at a working URL for the source of truth."""
    results = sorted(report["results"], key=lambda r: (r["program"], r["id"]))
    flagged = [r for r in results if r["verdict"] in NEEDS_REVIEW]
    lines = [
        "# Change review", "",
        f"[Back to the dashboard]({pages_home_url()}) - **run "
        f"{report['generated']}** - {len(flagged)} item(s) to review.", "",
        "Each block below is one flagged source: what happened, which billing "
        "codes moved (heuristic - **verify each against the linked source "
        "before acting**), and a working link to the exact spot in the "
        "official document.", "",
    ]
    if not flagged:
        lines += [f"{badge('ok')} Nothing to review from the last run.", ""]
    for r in flagged:
        prog = PROGRAM_NAMES.get(r["program"], r["program"])
        lines += [f"## {r['id']} - {prog}", "",
                  f"{badge_for(r['verdict'])} `{r['verdict']}` - detected "
                  f"{(r.get('checked_at') or report['generated'])[:10]}", "",
                  f"**What happened:** {md_cell(plain_why(r)) or 'no detail recorded.'}",
                  ""]
        if r.get("url"):
            lines.append(f"**Source of truth:** [{md_cell(r['url'])}]({r['url']})")
            lines.append("")
        codes = r.get("codes_touched") or []
        if codes:
            url = r.get("url", "")
            is_pdf = any(e["page"] is not None for e in codes)
            lines += ["**Codes that moved** (machine-extracted, verify each):",
                      "",
                      "| Code | System | What | Confidence | Tracked "
                      "| Open at |", "|---|---|---|---|---|---|"]
            for e in codes:
                tr = (f"**TRACKED** {md_cell(e['master_row'])}".strip()
                      if e["tracked"] else "")
                where = page_link(url, e["page"], is_pdf) or (
                    f"[source]({url})" if url else "")
                lines.append(f"| `{e['code']}` | {e['system']} "
                             f"| {e['direction']} | {e['confidence']} | {tr} "
                             f"| {where} |")
            lines.append("")
        if r.get("diff_report"):
            rel = repo_rel(r["diff_report"])
            lines.append(f"**Full before/after diff:** [{md_cell(rel)}]"
                         f"({blob_url(rel)})")
            lines.append("")
        if r.get("comms_draft"):
            rel = repo_rel(r["comms_draft"])
            lines.append(f"**Comms draft** (DRAFT - human review required "
                         f"before any distribution): [{md_cell(rel)}]"
                         f"({blob_url(rel)})")
            lines.append("")
        keys, scope = r.get("master_keys", ""), r.get("master_note", "")
        if keys or scope:
            lines.append("**Master rows to verify:** "
                         + " - ".join(x for x in
                                      (f"`{md_cell(keys)}`" if keys else "",
                                       md_cell(scope) if scope else "") if x))
            lines.append("")
    hist = []
    if log_path and Path(log_path).exists():
        try:
            with Path(log_path).open(encoding="utf-8", newline="") as f:
                hist = list(csv.DictReader(f))[-20:]
        except OSError:
            hist = []
    if hist:
        lines += ["## Recent change history (last 20 events)", "",
                  "| Date | Source | Status | Diff |", "|---|---|---|---|"]
        for h in reversed(hist):
            diff = h.get("diff_report", "")
            cell = (f"[diff]({blob_url(repo_rel(diff))})" if diff else "")
            lines.append(f"| {md_cell((h.get('generated') or '')[:10])} "
                         f"| `{md_cell(h.get('id', ''))}` "
                         f"| `{md_cell(h.get('verdict', ''))}` | {cell} |")
        lines.append("")
    lines += ["---", "",
              "Machine-generated review aid; not a source of record. Built "
              "and maintained by [Michael Phipps](https://github.com/mp321).",
              ""]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def append_changes_log(out_dir: Path, report: dict) -> None:
    log = out_dir / "changes_log.csv"
    try:
        new = not log.exists()
        with log.open("a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["generated", "program", "id", "verdict", "detail",
                            "page_updated", "url", "master_keys", "diff_report"])
            for r in report["results"]:
                if r["id"] in report["needs_review"]:
                    w.writerow([report["generated"], r["program"], r["id"],
                                r["verdict"], r["detail"], r.get("page_updated", ""),
                                r.get("url", ""), r.get("master_keys", ""),
                                r.get("diff_report", "")])
    except OSError:
        pass


def _code_ref(e: dict, url: str, is_pdf: bool) -> str:
    """`99213 (CPT, p.4 https://...#page=4)`-style reference for summaries."""
    bits = [e["system"]]
    if e["confidence"] != "high":
        bits.append(f"{e['confidence']} confidence")
    if e["page"] is not None:
        bits.append(f"p.{e['page']} {url}#page={e['page']}" if is_pdf and url
                    else f"p.{e['page']}")
    return f"{e['code']} ({', '.join(bits)})"


def write_run_summary(root: Path, report: dict) -> None:
    try:
        lines = [f"Source watch run {report['generated']} - "
                 f"{len(report['needs_review'])} item(s) need review.",
                 f"Dashboard: {pages_home_url()}", ""]
        for r in report["results"]:
            if r["id"] not in report["needs_review"]:
                continue
            lines.append(f"[{r['program']}] {r['id']} - {r['verdict']}")
            if r.get("url"):
                lines.append(f"  {r['url']}")
            lines.append(f"  detail: {r['detail']}")
            if r.get("diff_report"):
                lines.append(f"  diff: {blob_url(repo_rel(r['diff_report']))}")
            if r.get("master_keys"):
                lines.append(f"  Master rows: {r['master_keys']}")
            if r.get("master_note"):
                lines.append(f"  Master scope: {r['master_note']}")
            codes = r.get("codes_touched") or []
            if codes:
                url = r.get("url", "")
                is_pdf = any(e["page"] is not None for e in codes)
                added = [e for e in codes if e["direction"] in ("added", "both")]
                removed = [e for e in codes if e["direction"] in ("removed", "both")]
                tracked_hits = [e for e in codes if e["tracked"]]
                lines.append("  Codes touched (heuristic - verify each):")
                if added:
                    lines.append("    added:   " + ", ".join(
                        _code_ref(e, url, is_pdf) for e in added))
                if removed:
                    lines.append("    removed: " + ", ".join(
                        _code_ref(e, url, is_pdf) for e in removed))
                if tracked_hits:
                    lines.append("    TRACKED matches: " + ", ".join(
                        f"{e['code']}"
                        + (f" (Master row {e['master_row']})"
                           if e["master_row"] else "")
                        for e in tracked_hits))
            if r.get("comms_draft"):
                lines.append(f"  comms draft (DRAFT, human review required): "
                             f"{blob_url(repo_rel(r['comms_draft']))}")
            lines.append("")
        lines.append("Decision support only - verify against the live official "
                     "source before updating the Master sheet.")
        (root / "run_summary.md").write_text("\n".join(lines), encoding="utf-8")
    except OSError:
        pass


def write_comms_draft(root: Path, r: dict, stamp: str,
                      effective: list[str]) -> str:
    """Draft announcement for billing/coding staff when a CHANGED source
    touches tracked codes. Written to reports/comms/, never sent anywhere.
    Returns the path or ''."""
    try:
        codes = r.get("codes_touched", [])
        tracked = [e for e in codes if e["tracked"]]
        if not tracked:
            return ""
        cdir = root / "reports" / "comms"
        cdir.mkdir(parents=True, exist_ok=True)
        cp = cdir / f"{stamp}_{r['id']}.md"
        url = r.get("url", "")
        is_pdf = any(e["page"] is not None for e in codes)
        prog = PROGRAM_NAMES.get(r["program"], r["program"])
        lines = [
            f"# DRAFT - source change notice: {r['id']}",
            "",
            "> **DRAFT. Machine-generated by the source watcher. Requires "
            "human review and approval before any distribution.** Nothing is "
            "sent automatically. Verify every statement against the live "
            "official source first.",
            "",
            f"**Audience:** billing / coding staff, SF DPH network - "
            f"{prog}", "",
            "## What changed", "",
            f"The official source below was updated (detected "
            f"{r.get('checked_at', '')[:10]}). The billing codes listed here "
            "appeared on changed lines of the document text.", "",
            f"- Source: {url}",
        ]
        if effective:
            lines.append(f"- Possible effective date(s) found in the change: "
                         f"{', '.join(effective)} (verify in the document)")
        else:
            lines.append("- Effective date: not stated on the changed lines - "
                         "check the document.")
        if r.get("diff_report"):
            lines.append(f"- Exact before/after diff: "
                         f"{blob_url(repo_rel(r['diff_report']))}")
        lines += ["", "## Codes affected (tracked)", ""]
        for e in tracked:
            desc = f" - {e['description']}" if e.get("description") else ""
            mrow = (f" (Master row: {e['master_row']})"
                    if e.get("master_row") else "")
            pl = ""
            if e["page"] is not None:
                pl = (f" - see page {e['page']}"
                      + (f": {url}#page={e['page']}" if is_pdf and url else ""))
            lines.append(f"- **{e['code']}** ({e['system']}, {e['direction']})"
                         f"{desc}{mrow}{pl}")
        others = [e for e in codes if not e["tracked"]]
        if others:
            lines += ["", "## Other codes seen on changed lines (unverified "
                          "heuristic)", "",
                      ", ".join(f"{e['code']} ({e['system']}, "
                                f"{e['confidence']} confidence)"
                                for e in others)]
        lines += ["", "## Before acting", "",
                  "1. Open the source link above and re-read the changed "
                  "section.",
                  "2. Confirm each code, direction, and any effective date "
                  "against the document itself - the list above is a text "
                  "heuristic and can be wrong or incomplete.",
                  "3. Route through the normal review chain (Master sheet, "
                  "superbill / tipsheet, Epic review) before telling anyone "
                  "to change billing behavior.", ""]
        cp.write_text("\n".join(lines), encoding="utf-8")
        return str(cp)
    except OSError:
        return ""


def run(watchlist: Path, out_dir: Path, only, update: bool,
        baseline_override: dict | None = None,
        snapshots_dir: Path | None = None,
        dashboard: Path | None = None) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    baseline_path = out_dir / "baseline.json"
    if baseline_override is not None:
        base = baseline_override
    else:
        base = json.loads(baseline_path.read_text()) if baseline_path.exists() else {}

    root = Path(watchlist).resolve().parent
    tracked = load_tracked_codes(root / "data" / "tracked_codes.csv")
    snaps = SnapshotStore(snapshots_dir or (root / "snapshots"),
                          out_dir / "diffs", tracked=tracked)
    fetch = Fetcher()
    rows, new_base, review = [], {}, []
    ts = now_iso()

    for entry in load_watchlist(watchlist, only):
        eid, prev = entry["id"], base.get(entry["id"], {})
        diff_report = ""
        try:
            if entry.get("manual"):
                verdict = "MANUAL_REVIEW"
                detail = entry.get("manual_note", "review by hand on schedule")
                resp, sig = {"status": "manual"}, {}
                new_base[eid] = prev
            elif entry.get("type") == "bulletin_probe":
                verdict, detail, state = probe_bulletin(entry, prev, fetch)
                resp, sig = {"status": "probe", "final_url": entry["url_template"]}, {}
                state["checked_at"] = ts
                new_base[eid] = state
            elif entry.get("type") == "manual_list":
                mrows, frag = check_manual_list(entry, base, fetch, snaps, ts)
                new_base.update(frag)
                for r in mrows:
                    if r["verdict"] in NEEDS_REVIEW:
                        review.append(r["id"])
                    rows.append(r)
                    print(f"{r['verdict']:22} {r['program']:16} {r['id']}")
                continue
            else:
                resp = get_with_retry(fetch, entry["url"], prev)
                time.sleep(SLEEP)
                sig = signature(entry, resp)
                verdict, detail = verdict_for(entry, prev, resp, sig)
                diff_report = snaps.handle(entry["program"], eid, verdict, sig,
                                           entry.get("url", ""))
                if resp["status"] == "304":
                    new_base[eid] = {**prev, "checked_at": ts}
                elif resp["status"] == "200":
                    new_base[eid] = {"url": entry["url"], **{k: sig[k] for k in
                                     ("text_sha", "byte_sha", "page_updated",
                                      "links", "shell")},
                                     "etag": resp.get("etag", ""),
                                     "last_modified": resp.get("last_modified", ""),
                                     "checked_at": ts}
                else:
                    new_base[eid] = prev
        except Exception as exc:                              # noqa: BLE001
            verdict, detail, resp, sig = "UNREACHABLE", f"error:{exc}", {"status": "error"}, {}
            new_base[eid] = prev

        if verdict in NEEDS_REVIEW:
            review.append(eid)
        rows.append({
            "program": entry["program"], "id": eid,
            "checked_at": new_base.get(eid, {}).get("checked_at", ""),
            "type": entry.get("type", "html"), "verdict": verdict,
            "detail": detail, "page_updated": sig.get("page_updated", ""),
            "shell": sig.get("shell", ""), "http": resp.get("status", ""),
            "url": entry.get("url", entry.get("url_template", "")),
            "master_keys": ";".join(entry.get("master_keys", [])),
            "master_note": entry.get("master_note", ""),
            "note": entry.get("note", ""), "diff_report": diff_report,
        })
        print(f"{verdict:22} {entry['program']:16} {eid}")

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    # Attach the structured code candidates from the diff layer to their rows
    # (JSON report and dashboard read them), then draft a comms note for any
    # CHANGED source touching tracked codes. Drafts are files only.
    for r in rows:
        r["codes_touched"] = snaps.codes.get(r["id"], [])
        r["comms_draft"] = ""
        if r["verdict"] == "CHANGED" and any(e["tracked"]
                                             for e in r["codes_touched"]):
            r["comms_draft"] = write_comms_draft(
                root, r, stamp, snaps.effective.get(r["id"], []))
            if r["comms_draft"]:
                print(f"comms draft (needs human review) -> {r['comms_draft']}")
    report = {"generated": now_iso(), "needs_review": review, "results": rows}
    (out_dir / f"check_{stamp}.json").write_text(json.dumps(report, indent=2))
    (out_dir / "latest_report.json").write_text(json.dumps(report, indent=2))
    with (out_dir / f"check_{stamp}.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["id"])
        w.writeheader()
        w.writerows({**r, "codes_touched": codes_brief(r["codes_touched"])}
                    for r in rows)
    append_changes_log(out_dir, report)
    rs = root / "run_summary.md"
    if rs.exists():
        try:
            rs.unlink()
        except OSError:
            pass
    if review:
        write_run_summary(root, report)
    if dashboard:
        write_dashboard(dashboard, report, log_path=out_dir / "changes_log.csv")
        write_changes_page(dashboard.parent / "changes.md", report,
                           log_path=out_dir / "changes_log.csv")

    print(f"\nneeds review: {len(review)}  ->  {out_dir}/check_{stamp}.csv")
    if update:
        baseline_path.write_text(json.dumps(new_base, indent=2, sort_keys=True))
        print(f"baseline updated -> {baseline_path}")
    report["new_baseline"] = new_base
    return report


def seed_manual_list(watchlist: Path, out_dir: Path, entry_id: str) -> int:
    """Prime the baseline for one manual_list entry from its seed CSV so the
    first live run does not flood NEW rows. Seeds metadata only (revision_date
    + file.id per doc); the first live fetch fills the content hash and stays
    quiet as long as the portal metadata still matches the seed.
    """
    entries = load_watchlist(watchlist, None)
    target = next((e for e in entries
                   if e.get("id") == entry_id and e.get("type") == "manual_list"), None)
    if not target:
        print(f"no manual_list entry with id={entry_id} in {watchlist}")
        return 1
    seed_csv = target.get("seed_csv")
    if not seed_csv:
        print(f"entry {entry_id} has no seed_csv field; nothing to seed from")
        return 1
    csv_path = Path(watchlist).resolve().parent / seed_csv
    if not csv_path.exists():
        print(f"seed csv not found: {csv_path}")
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    baseline_path = out_dir / "baseline.json"
    base = json.loads(baseline_path.read_text()) if baseline_path.exists() else {}
    asset_base = (target.get("asset_base", "") or "").rstrip("/")
    ts = now_iso()
    seen, n = [], 0
    with csv_path.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            did = slug(r["doc_id"])
            fid = (r.get("file_id") or "").strip()
            cid = f"{entry_id}--{did}"
            seen.append(did)
            base[cid] = {
                "url": f"{asset_base}/assets/{fid}" if asset_base else f"/assets/{fid}",
                "title": r.get("title", ""),
                "revision_date": r.get("modified_on", ""),
                "file_id": fid,
                "text_sha": "", "byte_sha": "", "page_updated": "",
                "links": [], "shell": False, "etag": "", "last_modified": "",
                "checked_at": ts, "seeded": True,
            }
            n += 1
    base[entry_id] = {"url": target.get("url", ""), "docs": seen, "checked_at": ts}
    baseline_path.write_text(json.dumps(base, indent=2, sort_keys=True))
    print(f"seeded {n} docs for {entry_id} -> {baseline_path}")
    print("metadata-only seed; content hashes fill on the first live run.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--watchlist", default="watchlist.yaml", type=Path)
    ap.add_argument("--out", default=Path("reports"), type=Path)
    ap.add_argument("--programs", nargs="*", help="subset of program keys")
    ap.add_argument("--update", action="store_true", help="save new baseline")
    ap.add_argument("--dashboard", type=Path, default=None,
                    help="write a markdown status page (e.g. docs/index.md)")
    ap.add_argument("--dashboard-only", action="store_true",
                    help="regenerate the dashboard from reports/"
                         "latest_report.json without any network fetch")
    ap.add_argument("--snapshots", type=Path, default=None,
                    help="snapshot directory (default: ./snapshots)")
    ap.add_argument("--list", action="store_true", help="print watchlist and exit")
    ap.add_argument("--seed-manual-list", metavar="ENTRY_ID", default=None,
                    help="prime the baseline for a manual_list entry from its "
                         "seed_csv, then exit (e.g. fpact_manual_docs)")
    args = ap.parse_args()

    if args.list:
        for e in load_watchlist(args.watchlist, args.programs):
            print(f"{e['program']:16} {e.get('type','html'):15} {e['id']:32} "
                  f"{e.get('url', e.get('url_template',''))}")
        return 0

    if args.seed_manual_list:
        return seed_manual_list(args.watchlist, args.out, args.seed_manual_list)

    if args.dashboard_only:
        report_path = args.out / "latest_report.json"
        if not report_path.exists():
            print(f"no report to render: {report_path}")
            return 1
        report = json.loads(report_path.read_text(encoding="utf-8"))
        dash = args.dashboard or Path("docs/index.md")
        write_dashboard(dash, report, log_path=args.out / "changes_log.csv")
        write_changes_page(dash.parent / "changes.md", report,
                           log_path=args.out / "changes_log.csv")
        print(f"dashboard + changes page regenerated from {report_path} "
              f"-> {dash}, {dash.parent / 'changes.md'}")
        return 0

    report = run(args.watchlist, args.out, args.programs, args.update,
                 snapshots_dir=args.snapshots, dashboard=args.dashboard)
    return 1 if report["needs_review"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
