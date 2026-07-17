"""Shared helpers for the Vercel functions. Not exposed as an endpoint.

Storage: a private GitHub Gist (env GITHUB_TOKEN + GIST_ID) holds
baseline.json, subscribers.json, and latest_report.json. A gist is free,
reachable from any runtime with plain REST, and keeps revision history -
so every baseline update is itself an auditable diff.

Email: Resend REST API (env RESEND_API_KEY, ALERT_FROM). Optional - if the
key is absent, alerts are skipped and the report is still stored.
"""
from __future__ import annotations

import json
import os

import requests

GIST_API = "https://api.github.com/gists/{gist_id}"


def _gist_headers() -> dict:
    return {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "SFHN-RevInt-source-checker/1.1"}


def gist_read(filename: str, default):
    r = requests.get(GIST_API.format(gist_id=os.environ["GIST_ID"]),
                     headers=_gist_headers(), timeout=30)
    r.raise_for_status()
    f = r.json().get("files", {}).get(filename)
    if not f:
        return default
    content = f["content"]
    if f.get("truncated"):
        content = requests.get(f["raw_url"], timeout=30).text
    try:
        return json.loads(content)
    except Exception:
        return default


def gist_write(files: dict[str, dict | list]) -> None:
    payload = {"files": {name: {"content": json.dumps(data, indent=2)}
                         for name, data in files.items()}}
    r = requests.patch(GIST_API.format(gist_id=os.environ["GIST_ID"]),
                       headers=_gist_headers(), json=payload, timeout=30)
    r.raise_for_status()


def send_alert(report: dict, heartbeat: bool = False) -> str:
    key = os.environ.get("RESEND_API_KEY")
    if not key:
        return "email skipped (no RESEND_API_KEY)"
    subs = gist_read("subscribers.json", [])
    if not subs:
        return "email skipped (no subscribers)"
    changed = [r for r in report["results"] if r["id"] in report["needs_review"]]
    if heartbeat and not changed:
        resp = requests.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {key}"},
            json={"from": os.environ.get("ALERT_FROM", "revint-watch@resend.dev"),
                  "to": subs,
                  "subject": "[RevInt watch] monthly run OK - no changes",
                  "text": (f"Source watch ran {report['generated']}: "
                           f"{len(report['results'])} sources checked, no changes. "
                           "This heartbeat confirms the checker is alive.")},
            timeout=30)
        return f"heartbeat {resp.status_code} to {len(subs)} subscriber(s)"
    lines = [f"Source watch run {report['generated']} - "
             f"{len(changed)} source(s) need review.", ""]
    for r in changed:
        lines += [f"[{r['program']}] {r['id']} - {r['verdict']}",
                  f"  {r['url']}",
                  f"  detail: {r['detail']}"]
        if r.get("master_keys"):
            lines.append(f"  Master rows: {r['master_keys']}")
        if r.get("master_note"):
            lines.append(f"  Master scope: {r['master_note']}")
        lines.append("")
    lines.append("Decision support only - verify against the live official "
                 "source before acting.")
    resp = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {key}"},
        json={"from": os.environ.get("ALERT_FROM", "revint-watch@resend.dev"),
              "to": subs,
              "subject": f"[RevInt watch] {len(changed)} source(s) changed",
              "text": "\n".join(lines)},
        timeout=30)
    return f"email {resp.status_code} to {len(subs)} subscriber(s)"


def authorized(headers, query: dict) -> bool:
    secret = os.environ.get("CRON_SECRET")
    if not secret:
        return True
    auth = headers.get("Authorization", "") or headers.get("authorization", "")
    return auth == f"Bearer {secret}" or query.get("token") == secret
