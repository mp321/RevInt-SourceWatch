#!/usr/bin/env python3
"""
source_check.py - SF DPH Revenue Integrity multi-program source change-checker.

v1.3. Keeps the v1.2 engine (conditional GETs, robots.txt, redirect guard,
entry types pdf/html/binary/linkpage/bulletin_probe, BLIND_SHELL honesty,
manual entries, master_keys mapping) and adds four things:

  1. Snapshots + diffs. The extracted text of every pdf/html source is stored
     under snapshots/. On CHANGED, a unified before/after diff is written to
     reports/diffs/ with a heuristic list of possible CPT / HCPCS / ICD-10-CM
     codes touched. Git history preserves every prior snapshot.
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
Decision support, not a source of truth. No PHI ever.

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
import io
import json
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
                "NEW_ISSUE", "URL_CHANGED_IN_CONFIG", "REMOVED"}
DIFF_MAX_LINES = 3000

# Heuristic billing-code patterns, applied to changed diff lines only.
RE_HCPCS = re.compile(r"\b[A-Z]\d{4}\b")                  # J7300, S5000, G2012
RE_ICD10 = re.compile(r"\b[A-Z]\d{2}\.[0-9A-Z]{1,4}\b")   # Z30.011
RE_CPT = re.compile(r"\b\d{4}[0-9A-Z]\b")                 # 99213, 0001U
CPT_NOISE = re.compile(r"^(19|20)\d{2,3}$")               # years / year-like


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


def codes_in_diff(diff_lines: list[str]) -> list[str]:
    """Possible billing codes on added/removed lines. Heuristic only."""
    codes: set[str] = set()
    for line in diff_lines:
        if not line or line[0] not in "+-" or line.startswith(("+++", "---")):
            continue
        body = line[1:]
        codes.update(RE_HCPCS.findall(body))
        codes.update(RE_ICD10.findall(body))
        for m in RE_CPT.findall(body):
            if not CPT_NOISE.match(m):
                codes.add(m)
    return sorted(codes)


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
def parse_manual_list(raw: bytes, asset_base: str) -> list[dict]:
    """Parse a portal publication-list JSON into document dicts.

    Generic by design: finds leaf objects mentioning a .pdf, pulls the pdf
    path, a display title, and any revision-date-looking field. Endpoint
    shapes vary; adjust here if a portal needs it.
    """
    data = json.loads(raw.decode("utf-8", errors="replace"))
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
                     "title": title, "url": url, "revision_date": rev})
    return docs


# --------------------------------------------------------- snapshot layer ---
class SnapshotStore:
    """Stores extracted text per source and produces diff reports on change.

    All writes are best-effort: on a read-only filesystem (Vercel) the layer
    degrades to hash-only detection, which matches v1.2 behavior.
    """

    def __init__(self, snap_dir: Path, diff_dir: Path):
        self.snap_dir = snap_dir
        self.diff_dir = diff_dir
        self.written: list[str] = []

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
                codes = codes_in_diff(dl)
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
                    lines += ["## Possible codes touched (heuristic, verify each)",
                              "", ", ".join(codes), ""]
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

    resp = get_with_retry(fetch, entry["url"], {})
    time.sleep(SLEEP)
    if resp["status"] != "200":
        rows.append(row(eid, "UNREACHABLE", f"list endpoint http {resp['status']}"))
        frag[eid] = base.get(eid, {})
        return rows, frag
    try:
        docs = parse_manual_list(resp["content"], entry.get("asset_base", ""))
    except Exception as exc:
        rows.append(row(eid, "UNREACHABLE", f"list endpoint parse error: {exc}"))
        frag[eid] = base.get(eid, {})
        return rows, frag
    if not docs:
        rows.append(row(eid, "CONFIG_TODO",
                        "endpoint returned JSON but no PDF entries were parsed - "
                        "adjust parse_manual_list for this portal shape"))
        frag[eid] = base.get(eid, {})
        return rows, frag

    prev_parent = base.get(eid, {})
    prev_docs = set(prev_parent.get("docs", []))
    seen = []
    limit = int(entry.get("max_docs", 0))
    for d in docs[: limit or len(docs)]:
        cid = f"{eid}--{d['doc_id']}"
        seen.append(d["doc_id"])
        prev = base.get(cid, {})
        try:
            dresp = get_with_retry(fetch, d["url"], prev)
        except requests.RequestException as exc:
            rows.append(row(cid, "UNREACHABLE", f"error:{exc}", url=d["url"]))
            frag[cid] = prev
            continue
        time.sleep(SLEEP)
        sig = signature({"type": "pdf", "id": cid, "url": d["url"]}, dresp)
        verdict, detail = verdict_for({"type": "pdf", "url": d["url"]},
                                      prev, dresp, sig)
        # URL churn (rotating access tokens) is expected on portals; the
        # document identity is the doc_id, so ignore URL_CHANGED_IN_CONFIG.
        if verdict == "URL_CHANGED_IN_CONFIG":
            if sig["text_sha"] != prev.get("text_sha"):
                verdict, detail = "CHANGED", "content text hash differs"
            else:
                verdict, detail = "unchanged", "url token rotated, content same"
        rev_prev = prev.get("revision_date", "")
        if verdict == "unchanged" and (d["revision_date"] or "") != rev_prev:
            verdict = "DATE_CHANGED"
            detail = f"portal revision date '{rev_prev}' -> '{d['revision_date']}'"
        report = snaps.handle(entry["program"], cid, verdict, sig, d["url"],
                              extra={"Title": d["title"],
                                     "Portal revision date": d["revision_date"] or "n/a"})
        if dresp["status"] == "304":
            frag[cid] = {**prev, "checked_at": ts,
                         "revision_date": d["revision_date"] or rev_prev}
        elif dresp["status"] == "200":
            frag[cid] = {"url": d["url"], "title": d["title"],
                         "revision_date": d["revision_date"],
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


def write_dashboard(path: Path, report: dict) -> None:
    by_prog: dict[str, list[dict]] = {}
    for r in report["results"]:
        by_prog.setdefault(r["program"], []).append(r)
    lines = ["# Revenue Integrity Source Watch", "",
             "Automated monitor for the official billing sources behind the",
             "Revenue Integrity registry. Alert tool only, not a source of truth.",
             "Verify every flagged item against the live official source. No PHI.",
             "",
             f"Last run: {report['generated']}  ",
             f"Needs review: {len(report['needs_review'])}",
             "",
             "If Last run is more than 35 days old, the checker itself needs attention.",
             ""]
    for prog, rs in by_prog.items():
        lines += [f"## {prog}", "",
                  "| Source | Verdict | Revision / Page updated | Checked | Diff |",
                  "|---|---|---|---|---|"]
        for r in rs:
            flag = r["verdict"] if r["verdict"] in NEEDS_REVIEW else r["verdict"]
            link = f"[link]({r['url']})" if r.get("url") else ""
            diff = f"[diff]({r['diff_report']})" if r.get("diff_report") else ""
            lines.append(f"| {r['id']} {link} | {flag} | {r.get('page_updated','')} "
                         f"| {r.get('checked_at','')[:10]} | {diff} |")
        lines.append("")
    lines += ["Change log: reports/changes_log.csv in the repository.", ""]
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


def write_run_summary(root: Path, report: dict) -> None:
    try:
        lines = [f"Source watch run {report['generated']} - "
                 f"{len(report['needs_review'])} item(s) need review.", ""]
        for r in report["results"]:
            if r["id"] not in report["needs_review"]:
                continue
            lines.append(f"[{r['program']}] {r['id']} - {r['verdict']}")
            if r.get("url"):
                lines.append(f"  {r['url']}")
            lines.append(f"  detail: {r['detail']}")
            if r.get("diff_report"):
                lines.append(f"  diff: {r['diff_report']}")
            if r.get("master_keys"):
                lines.append(f"  Master rows: {r['master_keys']}")
            if r.get("master_note"):
                lines.append(f"  Master scope: {r['master_note']}")
            lines.append("")
        lines.append("Decision support only - verify against the live official "
                     "source before updating the Master sheet. No PHI.")
        (root / "run_summary.md").write_text("\n".join(lines), encoding="utf-8")
    except OSError:
        pass


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
    snaps = SnapshotStore(snapshots_dir or (root / "snapshots"),
                          out_dir / "diffs")
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
    report = {"generated": now_iso(), "needs_review": review, "results": rows}
    (out_dir / f"check_{stamp}.json").write_text(json.dumps(report, indent=2))
    (out_dir / "latest_report.json").write_text(json.dumps(report, indent=2))
    with (out_dir / f"check_{stamp}.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["id"])
        w.writeheader()
        w.writerows(rows)
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
        write_dashboard(dashboard, report)

    print(f"\nneeds review: {len(review)}  ->  {out_dir}/check_{stamp}.csv")
    if update:
        baseline_path.write_text(json.dumps(new_base, indent=2, sort_keys=True))
        print(f"baseline updated -> {baseline_path}")
    report["new_baseline"] = new_base
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--watchlist", default="watchlist.yaml", type=Path)
    ap.add_argument("--out", default=Path("reports"), type=Path)
    ap.add_argument("--programs", nargs="*", help="subset of program keys")
    ap.add_argument("--update", action="store_true", help="save new baseline")
    ap.add_argument("--dashboard", type=Path, default=None,
                    help="write a markdown status page (e.g. docs/index.md)")
    ap.add_argument("--snapshots", type=Path, default=None,
                    help="snapshot directory (default: ./snapshots)")
    ap.add_argument("--list", action="store_true", help="print watchlist and exit")
    args = ap.parse_args()

    if args.list:
        for e in load_watchlist(args.watchlist, args.programs):
            print(f"{e['program']:16} {e.get('type','html'):15} {e['id']:32} "
                  f"{e.get('url', e.get('url_template',''))}")
        return 0

    report = run(args.watchlist, args.out, args.programs, args.update,
                 snapshots_dir=args.snapshots, dashboard=args.dashboard)
    return 1 if report["needs_review"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
