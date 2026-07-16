"""POST /api/subscribe - add a work email to the alert list.

Body: {"email": "name@sfdph.org"}
Optional env ALLOWED_EMAIL_DOMAINS (comma-separated) restricts signups,
e.g. "sfdph.org". Staff work emails only - never patient information.
"""
from __future__ import annotations

import json
import os
import re
import sys
from http.server import BaseHTTPRequestHandler
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from api._lib import gist_read, gist_write  # noqa: E402

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class handler(BaseHTTPRequestHandler):          # noqa: N801
    def do_POST(self):                          # noqa: N802
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0)) or 0))
            email = str(body.get("email", "")).strip().lower()
        except Exception:
            return self._json(400, {"error": "invalid body"})
        if not EMAIL_RE.match(email):
            return self._json(400, {"error": "invalid email"})
        allowed = os.environ.get("ALLOWED_EMAIL_DOMAINS", "")
        if allowed and email.split("@")[1] not in [d.strip().lower() for d in allowed.split(",")]:
            return self._json(403, {"error": "email domain not allowed"})
        subs = gist_read("subscribers.json", [])
        if email not in subs:
            subs.append(email)
            gist_write({"subscribers.json": subs})
        self._json(200, {"ok": True, "subscribers": len(subs)})

    def _json(self, code, body):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)
