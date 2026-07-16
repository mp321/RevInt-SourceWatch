"""GET /api/check - run the source checker (invoked by Vercel Cron).

Query params:
  programs=fpact,fqhc   run a subset (also useful to keep runs short)
  update=0              skip saving the new baseline (default saves it, so
                        each change alerts exactly once; the gist keeps the
                        revision history for audit)
Auth: if CRON_SECRET is set, requires Authorization: Bearer <secret>
(sent automatically by Vercel Cron) or ?token=<secret>.
"""
from __future__ import annotations

import json
import os
import sys
from http.server import BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from api._lib import authorized, gist_read, gist_write, send_alert  # noqa: E402
from source_check import run  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


class handler(BaseHTTPRequestHandler):          # noqa: N801 (Vercel convention)
    def do_GET(self):                           # noqa: N802
        q = {k: v[0] for k, v in parse_qs(urlparse(self.path).query).items()}
        if not authorized(dict(self.headers), q):
            return self._json(401, {"error": "unauthorized"})

        programs = q["programs"].split(",") if q.get("programs") else None
        baseline = gist_read("baseline.json", {})
        report = run(watchlist=ROOT / "watchlist.yaml", out_dir=Path("/tmp/reports"),
                     only=programs, update=False, baseline_override=baseline)

        new_baseline = report.pop("new_baseline")
        files = {"latest_report.json": report}
        if q.get("update", "1") != "0":
            baseline.update(new_baseline)       # partial runs merge, not clobber
            files["baseline.json"] = baseline
        gist_write(files)

        if report["needs_review"]:
            mail = send_alert(report)
        elif os.environ.get("HEARTBEAT") == "1":
            mail = send_alert(report, heartbeat=True)
        else:
            mail = "no changes"
        self._json(200, {"needs_review": report["needs_review"], "mail": mail,
                         "checked": len(report["results"])})

    def _json(self, code: int, body: dict):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)
