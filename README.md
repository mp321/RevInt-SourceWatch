# Revenue Integrity Source Watch

Monitors the official billing sources behind the SF DPH Revenue Integrity registry (Family PACT, Medi-Cal FFS, Managed Medi-Cal, FQHC, Medi-Cal Rx, NCCI) and alerts when one changes. A flag means one thing: a human re-reads that source and, if needed, updates the Master sheet and downstream references (superbills, tipsheets, Epic review). Decision support, not a source of record.

Dashboard: `https://mp321.github.io/RevInt-SourceWatch/` (rebuilt on every run; see the repository above for source and history).

## How it works, in one paragraph

A weekly GitHub Actions run fetches every source in `watchlist.yaml`, extracts and hashes the text, and compares against the last baseline. On a change it stores the new text snapshot, writes a before/after diff report with a heuristic list of possible CPT, HCPCS, and ICD-10-CM codes touched, appends `reports/changes_log.csv`, updates the dashboard page, and opens a GitHub Issue, which emails everyone watching the repo. Git history preserves every prior version of every source, so any two versions can be compared later.

## Two detection layers

1. MCSS first, no code. Subscribe a team inbox to the DHCS Medi-Cal Subscription Service (Family PACT, General Medicine, RHC/FQHC at minimum). It is the official push channel and catches portal updates a scraper structurally cannot.
2. This watcher verifies and archives what changed: normalized-text hashing of PDFs (immune to metadata-only republishes), per-document monitoring of the Family PACT manual list including the portal Revision Date, link-set diffing of index pages (catches re-versioned filenames like a new Superbill), and honest BLIND_SHELL or MANUAL_REVIEW statuses where a plain fetch cannot see content.

## Where to look

| Need | Location |
|---|---|
| Current status of every source | Dashboard: docs/index.md (GitHub Pages) |
| What exactly changed | reports/diffs/*.md (diff plus codes touched) |
| Machine-readable change log | reports/changes_log.csv (Power BI reads this) |
| Email alerts | Watch this repo (Custom > Issues) |
| Feed for Power Automate / Teams | Repo Issues, or commits feed .../commits/main.atom |

## Setup

Runs as a GitHub Action (`.github/workflows/source-watch.yml`, Mondays 14:00 UTC) once Actions write permissions and Pages (branch `main`, folder `/docs`) are enabled in repository Settings; watch the repo (Custom > Issues) for email alerts. The Family PACT manual monitor (`fpact_manual_docs`) needs no secret to run - it self-heals its own read-only token - but `MCWEB_TOKEN` can be pinned as a repository secret if preferred. Full detail on both is in the code comments in `watchlist.yaml` and `source_check.py`.

## Reading an alert

The issue lists each flagged source with its status, link, Master rows to re-verify, and a diff report path when text changed. In the diff, `-` lines were removed and `+` lines added. The codes list is a regex heuristic over changed lines only; expect occasional noise. Always verify against the live official source before acting, then route: provider communication, superbill or tipsheet update, Epic review (charge master, preference lists, claim edits, ICD-10 mappings). Keep Epic build details out of this public repo.

## Local use

    pip install -r requirements.txt
    python source_check.py --list                 # show the watchlist
    python source_check.py --programs fpact       # one program
    python source_check.py --update               # accept current state as baseline
    python source_check.py --update --dashboard docs/index.md
    python source_check.py --dashboard-only       # rebuild docs/index.md from reports/latest_report.json, no network

Exit code 1 when anything needs review.

## Add a source or program

Edit `watchlist.yaml`. Toggle a program with `enabled:`. Entry types: `pdf`, `html`, `binary`, `linkpage` (set `link_pattern`), `bulletin_probe`, `manual_list` (portal JSON endpoint, per-document monitoring). `manual: true` marks sources that cannot be fetched automatically (robots.txt, bot walls); they report MANUAL_REVIEW on a cadence. `master_keys` and `master_note` tie a flag to the Master-sheet rows to re-verify. Versioned artifacts (Superbill, TRI fee schedules, NCCI quarterly files): watch the linking page, not just the file.

## Statuses

NEW, CHANGED (diff written), DATE_CHANGED (revision or page-updated stamp moved without a text change), LINKS_CHANGED, NEW_ISSUE, REMOVED, and URL_CHANGED_IN_CONFIG need review. CHANGED_METADATA_ONLY (a manual_list section whose portal Revision Date or file id moved but whose PDF the run could not fetch, so no text diff) and LIST_TRUNCATED (a manual_list endpoint returned fewer documents than its own aggregate count) also need review. MANUAL_REVIEW, BLIND_SHELL, PROBE_INCONCLUSIVE, CONFIG_TODO, and UNREACHABLE describe sources the run could not fully see. unchanged and metadata_only_unchanged are quiet. The dashboard explains each status in plain language under "Status legend".

## Limits

- The revision date alone is not trusted as the only signal; content hash is authoritative and both are reported.
- mcweb portal pages are client-rendered; without the JSON list endpoint wired up (already done for `fpact_manual_docs`) they stay honestly blind and MCSS covers detection.
- Diffs come from machine-extracted text; dense tables can extract noisily. The alert is still valid; the manual is the reference.
- leginfo and eCFR block automated fetches; those entries are MANUAL_REVIEW by design.

## Optional venue: Vercel signup page and email

The identical checker also runs as a Vercel function with a self-serve email subscription (Resend) and Gist-backed state. See SETUP.md. The GitHub path above is the primary, zero-credential venue; Vercel adds only the self-serve email signup.

## Roadmap (planned, not yet implemented)

Teams incoming webhook post on change; registry-as-a-page (render watchlist.yaml per program on the dashboard); SharePoint mirror via Power Automate; LLM triage step that summarizes a diff in plain language and drafts change notes for affected Master rows, human approved.

## Credit

Built and maintained by [mp321](https://github.com/mp321). Copyright (c) 2026 mp321. Provided as-is for internal use; see this repository for any applicable license terms before reuse elsewhere.
