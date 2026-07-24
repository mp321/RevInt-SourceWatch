# Revenue Integrity Source Watch

This repository contins an automated monitoring tool observing official published sources to support SFDPH Revenue Integrity team. Sources currently include: Medi-Cal and Family PACT provider manuals, bulletins, fee schedule pages, All Plan Letters, FQHC/RHC material and the NCCI Medicaid edit files. A script re-reads the same sources on a scheduled cadence and records what changed since the previous check, to enable easy identification of changes. 

A flag means one thing: a person re-reads that source and, if it matters, updates the downstream references (superbill, tipsheet, Epic review). **Always review and validate anything here against the live official source before using it or acting on it.** Decision support, not a source of record.

Dashboard: `https://mp321.github.io/RevInt-SourceWatch/` (rebuilt by every script run; this repository holds the code, the reports and the full history).

## How it works, in one paragraph

Once a week a scheduled script run fetches the sources in `watchlist.yaml`, extracts and hashes the text, and compares it with the last stored baseline. When something changes, it writes a before/after report showing exactly what changed (with a heuristic list of possible CPT, HCPCS and ICD-10-CM codes touched), rebuilds the dashboard page, and opens a GitHub Issue for the run - which is what emails everyone watching this repo. Every prior version of every source is kept and can be referenced if needed.

## The DHCS manuals are the centerpiece

For the Family PACT payer program, the script reads the provider portal's Manuals Revision Date column per section, plus the full text of each section (PDF format), plus the "Page updated" date stamped on each page inside the PDF. A flag can therefore say not just "this manual section changed" but which pages changed since the last check. Family PACT manuals are all included; the same level of capture can be extended to the other Medi-Cal manual communities (inpatient/outpatient, clinics and hospitals, FQHC/rural) as they are added (some have 200+ pdf manuals so likely on will be added on request or proven value-add before implementation).

## Two detection layers

1. **MCSS first, no code.** The Medi-Cal Subscription Service (MCSS) is DHCS's own free email service, and many of the updates covered here are announced through it first. Subscribe a team inbox at the MCSS site - `https://camcss.powerappsportals.com/` - and select the relevant subscriptions (Family PACT, General Medicine, and RHC/FQHC at minimum). It is the official push channel and it catches portal updates a script structurally cannot see.

2. **This watcher, as a supplement.** It does not replace MCSS. What it adds is tracking and archiving of specifically what changed on the sources included in `watchlist.yaml`: text-based change detection for PDFs (so a metadata-only republish does not raise a false alarm), per-section monitoring of the Family PACT manual list, link-set diffing of index pages (which catches a re-versioned filename), a stored snapshot of every prior version, and honest "can't see this page" statuses where automated checking is blocked.

**Maintenance.** Sources move. When an agency changes a URL, retires a page or reorganizes a portal, the matching entry in `watchlist.yaml` has to be updated before that source is monitored again - treat anything reported unreachable for more than one check as unwatched until it is fixed. Coverage is limited to what is listed in `watchlist.yaml`, which is why MCSS stays the primary channel.

## Where to look

| Need | Location |
|---|---|
| Current status of every source | Dashboard: docs/index.md (published site) |
| Team-friendly review of recent changes | Change review page: docs/changes.md (/changes.html on the site) |
| What exactly changed | reports/diffs/*.md (written the first time a text change is detected; empty so far) |
| Machine-readable change log | reports/changes_log.csv (Power BI reads this) |
| Notification when something changes | A GitHub Issue per flagged run; watch this repo (Custom > Issues) to be emailed |
| Feed for other tools | Repo Issues, or the commits feed .../commits/main.atom |

Heads-up: some watched sources (the DHCS fee schedules, NCCI quarterly files) are direct file downloads - clicking those links downloads an Excel or zip file instead of opening a page. The dashboard labels them.

## Reading a flagged item

Each flagged item lists the source with its status, a link, what happened (for a changed index page, every added or removed file URL on its own row), a "Codes touched" section (added / removed, with `url#page=N` deep links for PDFs), and a link to the exact before/after diff when text changed. In a diff, `-` lines were removed and `+` lines added. Verify against the live official source first, then route: provider communication, superbill or tipsheet update, Epic review (chargemaster, preference lists, claim edits, ICD-10 mappings). Keep Epic build details out of this public repo.

## Code extraction heuristic

Diff reports carry a structured table of possible billing codes on changed lines: code, system (CPT / HCPCS / ICD-10-CM / modifier), direction (added / removed), confidence, page, and a context excerpt. Every row is a **text heuristic requiring human verification** - it can be wrong or incomplete, especially on table-heavy PDFs.

- HCPCS (`[A-Z]0000`), ICD-10-CM (`A00.0000`), CPT category/PLA suffixes (`0000F/T/U/M`), and `modifier NN` phrases are format-distinctive and always included.
- A bare five-digit number is only counted as CPT when code-ish vocabulary (code, CPT, HCPCS, ICD, procedure, modifier, bill-, unit, TAR, rate) appears on the same or an adjacent line. This filters SF zip codes (941xx), fee amounts, form numbers, and years.
- Confidence: vocabulary on the same line = high; vocabulary only on a neighboring line = medium; distinctive format but no vocabulary = low. When unsure the code is included with low confidence rather than dropped.
- Page numbers come from the extracted PDF text and render as `url#page=N` deep links (browser PDF viewers open that page).

The synthetic regression test for the above is `tests/test_code_extraction.py` (`python -m pytest tests/`).

`.claude/commands/triage.md` adds a `/triage` command for a Claude Code session: it reads the latest diff reports and change log and drafts a plain-language triage with action proposals (citing diff line numbers, never inventing codes). It is run by hand by a person; nothing in the scheduled script run calls a model.

## Setup (the technical details)

The script runs as a GitHub Action (`.github/workflows/source-watch.yml`, Mondays 14:00 UTC) once Actions write permissions and Pages (branch `main`, folder `/docs`) are enabled in repository Settings; watch the repo (Custom > Issues) to be emailed when a run opens an alert issue. The Family PACT manual monitor (`fpact_manual_docs`) needs no secret to run - it self-heals its own read-only token - but `MCWEB_TOKEN` can be pinned as a repository secret if preferred. Full detail on both is in the code comments in `watchlist.yaml` and `source_check.py`.

## Local use

    pip install -r requirements.txt
    python source_check.py --list                 # show the watchlist
    python source_check.py --programs fpact       # run the script for one program
    python source_check.py --update               # accept current state as baseline
    python source_check.py --update --dashboard docs/index.md
    python source_check.py --dashboard-only       # rebuild docs/index.md from reports/latest_report.json, no network

Exit code 1 when anything needs review.

## Add a source or program

Edit `watchlist.yaml`. Toggle a program with `enabled:`. Entry types: `pdf`, `html`, `binary`, `linkpage` (set `link_pattern`), `bulletin_probe`, `manual_list` (portal JSON endpoint, per-document monitoring), `revision_watch` (metadata-only revision-date notices for a whole manual community). `manual: true` marks sources that cannot be fetched automatically (robots.txt, bot walls); they report MANUAL_REVIEW on a cadence. `registry_keys` and `registry_note` tie a flag to the registry rows to re-verify. Versioned artifacts (fee schedules, NCCI quarterly files): watch the linking page, not just the file.

## Statuses

NEW, CHANGED (diff written), DATE_CHANGED (a revision or page-updated stamp moved without a text change - the flag says which pages), LINKS_CHANGED, NEW_ISSUE, REMOVED, and URL_CHANGED_IN_CONFIG need review. CHANGED_METADATA_ONLY (a manual section whose portal Revision Date or file id moved but whose PDF the script could not fetch, so no text diff) and LIST_TRUNCATED (a portal list returned fewer documents than its own count) also need review. MANUAL_REVIEW, BLIND_SHELL, PROBE_INCONCLUSIVE, CONFIG_TODO, and UNREACHABLE describe sources the script could not fully see. unchanged and metadata_only_unchanged are quiet. The dashboard explains each status in plain language under "Status legend".

## Limits

- The revision date alone is not trusted as the only signal; content hash is authoritative and both are reported.
- mcweb portal pages are client-rendered; without the JSON list endpoint wired up (already done for `fpact_manual_docs`) they stay honestly blind and MCSS covers detection.
- Diffs come from machine-extracted text; dense tables can extract noisily. The flag is still valid; the manual is the reference.
- leginfo and eCFR block automated fetches; those entries are MANUAL_REVIEW by design.
- Coverage is only what `watchlist.yaml` lists, and only for as long as those URLs stay valid (see Maintenance above).

## Optional venue: Vercel signup page and email

The same checker can also run as a Vercel function with a self-serve email subscription (Resend) and Gist-backed state, described in SETUP.md. This venue is not in use and has not been verified end to end - treat it as a future option. The GitHub path above is the primary, zero-credential venue.

## Roadmap (planned, not yet implemented)

Extend the per-section manual monitoring to more Medi-Cal manual communities (inpatient/outpatient, clinics and hospitals, FQHC/rural); deeper "what changed" detail per changed page; Teams incoming webhook post on change; registry-as-a-page; self-serve email subscriptions for staff who do not use GitHub; an LLM triage step in the run itself that summarizes a diff in plain language for human approval (today's `/triage` is a manual, human-invoked command).

## Credit, license and disclaimer

Built and maintained by [Michael Phipps](https://github.com/mp321). Released under the MIT license (see [LICENSE](LICENSE)) - free to use, copy and adapt, including commercially. If you reuse or adapt it, a credit line and a link back to this repository are appreciated.

Provided as-is, without warranty of any kind, for general use as decision support. It is not legal, coding or billing advice, and the material it monitors is public agency content that can change or be withdrawn at any time. The live official source always governs; validate before acting.
