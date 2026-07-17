# /triage - plain-language triage of the latest source changes

You are triaging change alerts from the SF DPH Revenue Integrity source
watcher (this repo). Decision support only - nothing you write is a source
of record, and nothing may be sent or applied automatically.

## Steps

1. Read `reports/changes_log.csv` and identify the most recent run(s) -
   the `generated` column is chronological; the last rows are the newest.
2. For every row of the latest run with a `diff_report` path, read that
   file in `reports/diffs/`. Also read `reports/latest_report.json` for the
   structured `codes_touched` entries (code, system, direction, confidence,
   page).
3. For each change, produce a short plain-language summary for billing /
   coding staff:
   - What document changed and where (source URL; for PDFs use
     `url#page=N` deep links with the page from the codes table; note when
     which pages moved is stated in the DATE_CHANGED detail).
   - Which billing codes moved: added / removed / both, and the confidence
     level from the report.
   - Cite the diff by line number (e.g. "diff lines 12-18 of
     reports/diffs/<file>.md") for every claim about what changed.
4. Propose registry actions per change: which `registry_keys` /
   `registry_note` scopes to re-verify, and what kind of downstream update
   (superbill, tipsheet, Epic review) the change suggests. Frame every
   proposal as "verify, then update if confirmed" - never as fact.

## Hard rules

- Never invent, infer, or "correct" a billing code that does not appear
  verbatim in a diff report or in `codes_touched`. If a code looks
  truncated or garbled (PDF extraction noise), say so instead of guessing.
- Cite diff line numbers for every code and every quoted change.
- Low-confidence entries must be labeled as such; do not silently promote
  them.
- All output is a DRAFT requiring human verification against the live
  official source before anyone acts on it. Say this at the top of your
  summary.
- Do not modify the registry, watchlist, baselines, or reports; your
  output is analysis text only.
