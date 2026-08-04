# Setup guide

The primary venue is GitHub Actions plus GitHub Pages; those steps live in README.md and need no credentials or third-party accounts. This file covers the optional Vercel venue and notification alternatives. The detection logic (source_check.py plus watchlist.yaml) is identical in every venue; only the runner changes.

## Notification options

- GitHub Issues (in use, zero setup): a flagged script run opens an issue, and GitHub emails everyone watching the repo (must have github email setup).
- Power BI available (e.g. read changes_log.csv from Github via web connection) but requires pro workspace/sharepoint to publish for end-users to access (can set up for personal use as-is).

## End-user visibility

Built and running now: the GitHub Pages dashboard (per-source status, portal revision date, last checked, diff link), the change review page, per-change diff reports with a codes-touched list, the append-only change log, and a GitHub Issue per flagged run.
