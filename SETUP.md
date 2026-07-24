# Setup guide

The primary venue is GitHub Actions plus GitHub Pages; those steps live in README.md and need no credentials or third-party accounts. This file covers the optional Vercel venue and notification alternatives. The detection logic (source_check.py plus watchlist.yaml) is identical in every venue; only the runner changes.

## Optional: Vercel venue (self-serve email signup) - not in use, not verified

Written but never run end to end - treat this section as a future option, not a working setup. It would add a hosted /api/check cron and a subscriber list so staff can sign themselves up for email alerts. State lives in a private GitHub Gist (free REST access, every baseline update is an auditable revision). Email would go out via Resend only when something changed.

1. Create a private gist with three files: `baseline.json` (`{}`), `subscribers.json` (`[]`), `latest_report.json` (`{}`). Note the gist ID.
2. Create a GitHub fine-grained token with Gists read and write.
3. Import the repo at vercel.com or run `npx vercel deploy`.
4. Environment variables: `GITHUB_TOKEN`, `GIST_ID` (required), `CRON_SECRET` (recommended; Vercel Cron sends it as a Bearer token), `RESEND_API_KEY` and `ALERT_FROM` (email), `ALLOWED_EMAIL_DOMAINS` such as `sfdph.org`, `HEARTBEAT=1` for a monthly run-OK email.
5. Cron is declared in `vercel.json` (1st of the month). First run: open `https://<app>.vercel.app/api/check?token=<CRON_SECRET>`; the baseline saves automatically. Subset runs: `/api/check?programs=fpact`; partial runs merge into the baseline.
6. Confirm on your Vercel plan before relying on it (not verified in this build): Hobby cron limits, `maxDuration: 300`, `includeFiles` support. If duration caps bite, split into per-program calls.

Limitations of this venue: the filesystem is read-only, so text snapshots and diff reports are not persisted; detection degrades to hash-only, matching v1.2 behavior. The diff feature requires the GitHub Actions or local venue.

## Notification options

- GitHub Issues (in use, zero setup): a flagged script run opens an issue, and GitHub emails everyone watching the repo.
- Resend email (Vercel venue, future): a subscriber-managed list, alert plus optional heartbeat. Nothing is running today.
- Teams incoming webhook (future): one HTTP POST of run_summary.md to a channel; add a `TEAMS_WEBHOOK_URL` env and a short post step in the workflow when wanted.
- Power BI: reads reports/changes_log.csv and reports/sources.csv from the raw GitHub URLs; the step-by-step build sits in dev-prompt.md.

## End-user visibility

Built and running now: the GitHub Pages dashboard (per-source status, portal revision date, last checked, diff link), the change review page, per-change diff reports with a codes-touched list, the append-only change log, and a GitHub Issue per flagged run. Next in order of value: deeper per-page "what changed" detail, Teams webhook, registry-as-a-page.
