"""GET /api/report - return the latest run report (read by the dashboard)."""
from __future__ import annotations

import json
import sys
from http.server import BaseHTTPRequestHandler
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from api._lib import gist_read  # noqa: E402


class handler(BaseHTTPRequestHandler):          # noqa: N801
    def do_GET(self):                           # noqa: N802
        report = gist_read("latest_report.json", {"generated": None, "results": [],
                                                  "needs_review": []})
        data = json.dumps(report).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)
