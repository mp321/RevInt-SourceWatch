# Revenue Integrity Source Watch

A weekly change check on the official California Medi-Cal and Family PACT
billing documents. Each run takes a snapshot of every source, compares it
against the previous snapshot, and names exactly what changed: which
document, which page, and when.

It watches provider manuals, program news, fee schedules, All Plan Letters,
RHC/FQHC material, CPSP perinatal billing sections and the NCCI Medicaid edit
files.

Sources are listed in `watchlist.yaml`. On a change the script writes a
before/after diff, lists any billing codes found on the changed lines,
rebuilds the dashboard, and opens a GitHub Issue which is a simple method to
email found changes to the user. Every prior version stays in git.

Verify against the live official source before use.

Dashboard: https://mp321.github.io/RevInt-SourceWatch/ (rebuilt every run;
this repository holds the code and the reports)

## Detection layers

**MCSS is the primary channel.** The Medi-Cal Subscription Service is DHCS's
own free email service and announces most of what is monitored here.
Subscribe at https://camcss.powerappsportals.com/ and select the relevant
subscriptions (Family PACT, General Medicine, RHC/FQHC, Obstetrics).

**This tool is supplemental to MCSS.** What it adds is a
record of exactly what changed: full-text detection for PDFs, so a
metadata-only republish raises no false alarm; per-section monitoring of the
Family PACT, RHC/FQHC and CPSP (Obstetrics program) manual sections; a stored snapshot of every
prior version; and a named status for every source it cannot read, so a monitoring gap shows on the page instead of passing as silence.

## Scope

Manual sections are monitored at two depths, both driven from the DHCS
provider portal's document list and its per-section Revision Date.

**Full text (31 sections).** All 24 Family PACT sections, the four RHC/FQHC
sections inside Clinics and Hospitals, and the three CPSP perinatal sections
inside Obstetrics. Each section PDF is fetched every run and its whole text
hashed, along with the "Page updated" stamp printed on each page. A change
reports the section, the pages whose stamp moved, the before/after diff and
any billing codes on the changed lines.

**Revision date only.** Inpatient Services, Clinics and Hospitals, General
Medicine and Obstetrics hold 115 to 246 sections each, so those communities
are watched by Revision Date alone: the notice names the sections that moved,
with no text and no diff. Any community moves to full text by adding one
watchlist entry, filtered by filename where only part of it is wanted.

A community can run both ways at once. Obstetrics reports date-only notices
across all 172 of its sections while its three CPSP sections are also read in
full, so a CPSP change arrives with its diff and the rest of the manual still
reports which sections moved.

Coverage is exactly what `watchlist.yaml` lists, and only while those URLs keep working. When a source moves, its entry has to be repointed before it is watched again: a source reporting UNREACHABLE for more than one run is not being watched.

## Where to look

| Need | Location |
|---|---|
| Current status of every source | Dashboard (`docs/index.md`) |
| Team-friendly review of recent changes | Change review page (`docs/changes.md`, `/changes.html` on the site) |
| What exactly changed | `reports/diffs/*.md` |
| Machine-readable change log | `reports/changes_log.csv` (Power BI reads this) |
| Source dimension table | `reports/sources.csv` |
| Notification | A GitHub Issue per flagged run |
| Feed for other tools | Repo Issues, or `.../commits/main.atom` |

Some watched sources are direct file downloads (the DHCS fee schedules, the
NCCI quarterly files). Where a landing page exists the dashboard links that
instead and labels the file link separately, so nothing downloads unless
asked.

## Notifications

A run that flags anything opens a GitHub Issue whose body is the run summary.
GitHub emails every account watching the repository, so subscribing is one
click: Watch > Custom > Issues, on an account with a verified email address.
No credentials, no third-party service, no per-user setup beyond that.

The limit is that recipients need a GitHub account. To reach staff who do not
have one, the change log is the integration point: `reports/changes_log.csv`
is append-only with a stable schema, so a Teams incoming webhook or a Power
Automate flow reading that file can post to a channel or distribution list
without touching the checker.

## Reading a flagged item

Each item shows the source, its status, what happened, any billing codes the
text heuristic caught (with `url#page=N` deep links where the PDF opens
directly), and a link to the diff when text changed. In a diff, `-` lines were removed and `+` lines
added.

Finding nothing behind a flag is a normal outcome. Sources republish files,
reshuffle links and migrate pages without changing a word of policy. When the
same source keeps flagging with nothing behind it, tighten or retire its
watchlist entry rather than re-reading it every week; the dashboard shows how
many times a source has flagged recently so the pattern is visible.

## Code extraction heuristic

Diff reports carry a table of possible billing codes on changed lines: code,
system (CPT / HCPCS / ICD-10-CM / modifier), direction, confidence, page, and
a context excerpt. **Every row is a text heuristic requiring human
verification.** It can be wrong or incomplete, especially on table-heavy PDFs.

- HCPCS (`[A-Z]0000`), ICD-10-CM (`A00.0000`), CPT category/PLA suffixes
  (`0000F/T/U/M`) and `modifier NN` phrases are format-distinctive and always
  included.
- A bare five-digit number counts as CPT only when code vocabulary (code,
  CPT, HCPCS, ICD, procedure, modifier, bill-, unit, TAR, rate) appears on the
  same or an adjacent line. This filters SF zip codes (941xx), fee amounts,
  form numbers and years.
- Confidence: vocabulary on the same line is high, on a neighboring line
  medium, distinctive format with no vocabulary low. When unsure, the code is
  included at low confidence rather than dropped.
- Page numbers come from the extracted PDF text and render as `url#page=N`
  deep links, which browser PDF viewers honor. For a PDF that only the checker
  can fetch, the page number is shown without a link.

`tests/test_code_extraction.py` covers this plus the fetch guards that keep a
bad response from being mistaken for a change. Run `python -m pytest tests/`.

`.claude/commands/triage.md` adds a `/triage` command for a Claude Code
session: it reads the latest diffs and change log and drafts a plain-language
triage with action proposals, citing diff line numbers and never inventing
codes. It is run by hand. Nothing in the scheduled run calls a model.

## Running it

**Scheduled.** `.github/workflows/source-watch.yml` runs Mondays 14:00 UTC and
on demand via the Run workflow button. It needs Actions write permissions and
Pages enabled on branch `main`, folder `/docs`, both in repository Settings.
The mcweb manual monitors need no secret; they read the portal's own public
read-only token and re-read it if it rotates. `MCWEB_TOKEN` can be set as a
repository secret to pin a specific token instead.

**Local.**

    pip install -r requirements.txt
    python source_check.py --list                 # show the watchlist
    python source_check.py --programs fpact       # run one program
    python source_check.py --update               # accept current state as baseline
    python source_check.py --update --dashboard docs/index.md
    python source_check.py --dashboard-only       # rebuild docs/ from reports/, no network

Exit code 1 when anything needs review. Everything in `docs/` is generated;
change the writer functions in `source_check.py`, never the pages.

## Adding a source

Edit `watchlist.yaml`. Toggle a program with `enabled:`. Entry types:

| Type | Detects |
|---|---|
| `pdf` | full text change, per-page "Page updated" stamps |
| `html` | page text change |
| `binary` | file changed (no visibility into which rows) |
| `linkpage` | links added or removed (set `link_pattern`) |
| `bulletin_probe` | a new sequentially numbered bulletin |
| `manual_list` | per-document monitoring behind a portal JSON endpoint |
| `revision_watch` | revision-date movement across a whole manual community |

`human_url` points a reader at the landing page when the watched URL is a
direct download. `manual: true` marks a source that cannot be fetched at all;
it reports MANUAL_REVIEW every run, so use it only when the standing reminder
is worth the noise. `registry_note` is free text naming the downstream
follow-up when a source changes; it renders on the pages as "Follow-up" and is
omitted where an entry does not set it. `registry_keys` is an optional id list
for the same purpose, unused so far.

A new entry appears on the dashboard as `not_yet_checked` until the next run
reports on it, so the page always lists the whole watchlist.

Before adding an entry, ask what it can report that someone would act on. An
entry that returns the same status every week trains people to ignore the
dashboard.

## Statuses

Needing review: NEW, CHANGED (diff written), DATE_CHANGED (a revision or
page-updated stamp moved with no text change; the item names the pages),
LINKS_CHANGED, NEW_ISSUE, REMOVED, URL_CHANGED_IN_CONFIG, REVISION_NOTICE,
CHANGED_METADATA_ONLY (portal metadata moved but the PDF could not be
fetched, so no diff), and LIST_TRUNCATED (a portal list returned fewer
documents than its own count).

Not fully visible: MANUAL_REVIEW, BLIND_SHELL, PROBE_INCONCLUSIVE,
CONFIG_TODO, UNREACHABLE.

Quiet: unchanged, metadata_only_unchanged.

Render-only: not_yet_checked, for a watchlist entry the last run did not cover
(usually added since). It never reaches the baseline, the change log or an
alert issue.

The dashboard explains each status under "Status legend".

## Limits

- Content hash is authoritative; a revision date alone is never trusted as
  the only signal. Both are reported.
- Diffs come from machine-extracted text. Dense tables extract noisily. The
  flag is still valid; the manual is the reference.
- A `binary` entry can only report that the file changed, never which rows.
- A response that arrives empty or as a bot-check page reports UNREACHABLE
  and keeps the previous baseline, so it cannot be mistaken for a change. That
  source is unwatched until the fetch works again.
- mcweb portal pages are client-rendered. Without the JSON endpoint wired up,
  an entry stays honestly blind and MCSS covers detection.
- The portal serves manual PDFs from an endpoint that answers only to its own
  token, so those URLs cannot be opened by clicking. The pages show the
  endpoint as plain text and link the portal list to open the section from.
- leginfo statutes and eCFR text are not monitored; both block automated
  fetches. eCFR publishes a public API that would bring Title 42 Part 405 back
  under watch.

## Roadmap

Not yet implemented: full text monitoring for more manual communities;
per-page "what changed" detail in diff reports; the eCFR API entry; a Teams
webhook on change; an LLM triage step inside the run that drafts a
plain-language summary for human approval.

## Credit, license and disclaimer

Built and maintained by [Michael Phipps](https://github.com/mp321). Released
under the MIT license (see [LICENSE](LICENSE)), free to use, copy and adapt,
including commercially. If you reuse or adapt it, a credit line and a link
back to this repository are appreciated.

Provided as-is, without warranty of any kind. Not legal, coding or billing
advice. The material it monitors is public agency content that can change or
be withdrawn at any time. The live official source always governs; validate
before acting.
