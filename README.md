# Revenue Integrity Source Watch

Monitors the official billing sources behind SF DPH Revenue Integrity work (Family PACT, Medi-Cal FFS, Managed Medi-Cal, FQHC, NCCI) and alerts when one changes. A flag means one thing: a human re-reads that source and, if needed, updates the downstream references (superbills, tipsheets, Epic review). Decision support, not a source of record.

Dashboard: `https://mp321.github.io/RevInt-SourceWatch/` (rebuilt on every run; see the repository above for source and history).

## How it works, in one paragraph

Once a week, an automated run fetches every source in `watchlist.yaml`, extracts and hashes the text, and compares against the last baseline. On a change it stores the new text snapshot, writes a before/after report showing exactly what changed (with a heuristic list of possible CPT, HCPCS, and ICD-10-CM codes touched), updates the dashboard page, and sends an email alert to everyone watching the repository. Every prior version of every source is preserved, so any two versions can be compared later.

## The DHCS manuals are the centerpiece

For Family PACT, the watcher monitors the provider portal's Manuals list the way a person would read it: the portal's Revision Date column per section, plus the full text of each section PDF, plus the "Page updated" date stamped on each page inside the PDF. An alert can therefore say not just "this manual section changed" but which pages changed since the last run. Family PACT is wired up first; the same pattern extends to the other Medi-Cal manual communities (inpatient/outpatient, clinics and hospitals, FQHC/rural) as they are added.

## Two detection layers

1. MCSS first, no code. Subscribe a team inbox to the DHCS Medi-Cal Subscription Service (Family PACT, General Medicine, RHC/FQHC at minimum). It is the official push channel and catches portal updates a scraper structurally cannot.
2. This watcher verifies and archives what changed: text-based change detection for PDFs (immune to metadata-only republishes), per-section monitoring of the Family PACT manual list, link-set diffing of index pages (catches re-versioned filenames), and honest "can't see this page" statuses where automated checking is blocked.

## Where to look

| Need | Location |
|---|---|
| Current status of every source | Dashboard: docs/index.md (published site) |
| Team-friendly review of recent changes | Change review page: docs/changes.md (/changes.html on the site) |
| What exactly changed | reports/diffs/*.md (diff plus a structured code table) |
| Machine-readable change log | reports/changes_log.csv (Power BI reads this) |
| Email alerts | Watch this repo (Custom > Issues) |
| Feed for Power Automate / Teams | Repo Issues, or commits feed .../commits/main.atom |

Heads-up: some watched sources (the DHCS fee schedules, NCCI quarterly files) are direct file downloads - clicking those links downloads an Excel or zip file instead of opening a page. The dashboard labels them.

## Reading an alert

Each alert lists the flagged sources with status, link, a "Codes touched" section (added / removed, with `url#page=N` deep links for PDFs), and a link to the exact before/after diff when text changed. In the diff, `-` lines were removed and `+` lines added. Always verify against the live official source before acting, then route: provider communication, superbill or tipsheet update, Epic review (chargemaster, preference lists, claim edits, ICD-10 mappings). Keep Epic build details out of this public repo.

## Code extraction heuristic

Diff reports carry a structured table of possible billing codes on changed lines: code, system (CPT / HCPCS / ICD-10-CM / modifier), direction (added / removed), confidence, page, and a context excerpt. Every row is a **text heuristic requiring human verification** - it can be wrong or incomplete, especially on table-heavy PDFs.

- HCPCS (`[A-Z]0000`), ICD-10-CM (`A00.0000`), CPT category/PLA suffixes (`0000F/T/U/M`), and `modifier NN` phrases are format-distinctive and always included.
- A bare five-digit number is only counted as CPT when code-ish vocabulary (code, CPT, HCPCS, ICD, procedure, modifier, bill-, unit, TAR, rate) appears on the same or an adjacent line. This filters SF zip codes (941xx), fee amounts, form numbers, and years.
- Confidence: vocabulary on the same line = high; vocabulary only on a neighboring line = medium; distinctive format but no vocabulary = low. When unsure the code is included with low confidence rather than dropped.
- Page numbers come from the extracted PDF text and render as `url#page=N` deep links (browser PDF viewers open that page).

The synthetic regression test for the above is `tests/test_code_extraction.py` (`python -m pytest tests/`).

In a Claude Code session, `/triage` reads the latest diff reports and change log and drafts a plain-language triage with action proposals (citing diff line numbers, never inventing codes).

## Setup (the technical details)

Runs as a GitHub Action (`.github/workflows/source-watch.yml`, Mondays 14:00 UTC) once Actions write permissions and Pages (branch `main`, folder `/docs`) are enabled in repository Settings; watch the repo (Custom > Issues) for email alerts. The Family PACT manual monitor (`fpact_manual_docs`) needs no secret to run - it self-heals its own read-only token - but `MCWEB_TOKEN` can be pinned as a repository secret if preferred. Full detail on both is in the code comments in `watchlist.yaml` and `source_check.py`.

## Local use

    pip install -r requirements.txt
    python source_check.py --list                 # show the watchlist
    python source_check.py --programs fpact       # one program
    python source_check.py --update               # accept current state as baseline
    python source_check.py --update --dashboard docs/index.md
    python source_check.py --dashboard-only       # rebuild docs/index.md from reports/latest_report.json, no network

Exit code 1 when anything needs review.

## Add a source or program

Edit `watchlist.yaml`. Toggle a program with `enabled:`. Entry types: `pdf`, `html`, `binary`, `linkpage` (set `link_pattern`), `bulletin_probe`, `manual_list` (portal JSON endpoint, per-document monitoring). `manual: true` marks sources that cannot be fetched automatically (robots.txt, bot walls); they report MANUAL_REVIEW on a cadence. `registry_keys` and `registry_note` tie a flag to the registry rows to re-verify. Versioned artifacts (fee schedules, NCCI quarterly files): watch the linking page, not just the file.

## Statuses

NEW, CHANGED (diff written), DATE_CHANGED (a revision or page-updated stamp moved without a text change - the alert says which pages), LINKS_CHANGED, NEW_ISSUE, REMOVED, and URL_CHANGED_IN_CONFIG need review. CHANGED_METADATA_ONLY (a manual section whose portal Revision Date or file id moved but whose PDF the run could not fetch, so no text diff) and LIST_TRUNCATED (a portal list returned fewer documents than its own count) also need review. MANUAL_REVIEW, BLIND_SHELL, PROBE_INCONCLUSIVE, CONFIG_TODO, and UNREACHABLE describe sources the run could not fully see. unchanged and metadata_only_unchanged are quiet. The dashboard explains each status in plain language under "Status legend".

## Limits

- The revision date alone is not trusted as the only signal; content hash is authoritative and both are reported.
- mcweb portal pages are client-rendered; without the JSON list endpoint wired up (already done for `fpact_manual_docs`) they stay honestly blind and MCSS covers detection.
- Diffs come from machine-extracted text; dense tables can extract noisily. The alert is still valid; the manual is the reference.
- leginfo and eCFR block automated fetches; those entries are MANUAL_REVIEW by design.

## Optional venue: Vercel signup page and email

The identical checker also runs as a Vercel function with a self-serve email subscription (Resend) and Gist-backed state. See SETUP.md. The GitHub path above is the primary, zero-credential venue; Vercel adds only the self-serve email signup.

## Roadmap (planned, not yet implemented)

Extend the per-section manual monitoring to more Medi-Cal manual communities (inpatient/outpatient, clinics and hospitals, FQHC/rural); deeper "what changed" detail per changed page; Teams incoming webhook post on change; registry-as-a-page; SharePoint mirror via Power Automate; LLM triage step that summarizes a diff in plain language, human approved.

## Credit

Built and maintained by [Michael Phipps](https://github.com/mp321). Provided as-is for internal use; see this repository for any applicable license terms before reuse elsewhere.
