# mcweb / Directus findings

Discovery record for `mcweb.apps.prd.cammis.medi-cal.ca.gov`, the Medi-Cal
provider portal SPA fronting publications (manuals, bulletins) and rates.
Established by DevTools capture and curl on 2026-07-02 and 2026-07-16.
Suggested location in repo: `notes/CONTEXT-mcweb.md`. New Claude Code
sessions should read this file plus README.md before touching code.

## Platform

- Backend is Directus (headless CMS). GraphQL at `POST /graphql`; REST would
  be `/items/<collection>`; file downloads at `/assets/<file_uuid>`.
  Telltales: `__typename: directus_files`, `_eq` filter syntax,
  `GraphQLStringOrFloat` scalar, `filename_download`, `modified_on`.
- The manual page fires operation `CommunityManuals` with variables
  `{"communityId": "25"}`. communityId 25 = Family PACT (group
  `group_part_identifier: "Specialty Program"`). The FQHC manual page
  (`?community=rural`) will use a different numeric id, not yet captured.

## Auth: the decisive finding

- Anonymous schema (bare curl introspection) exposes ONLY four query fields:
  `medical_rates_page`, `medical_rates_page_by_id`,
  `medical_rates_page_aggregated`, `medical_rates_page_by_version`.
- `manuals` and `communities` from curl return
  `Cannot query field "manuals" on type "Query"` (GRAPHQL_VALIDATION).
  Directus strips collections the caller cannot read from the schema, so a
  validation error here IS a permission denial.
- `GET /assets/<file_id>` from curl returns 403:
  `You don't have permission to perform "read" for collection
  "directus_files" or it does not exist.`
- The browser succeeds at all of the above, so the SPA carries a credential.
- CONFIRMED 2026-07-16: DevTools "Copy as cURL" of the CommunityManuals
  request, replayed from a terminal, returns the full response including the
  anon-blocked `communities` field. So the credential travels in the request
  headers of that command and is replayable outside the browser. The
  credential is captured in `notes/mcweb_browser_curl.txt` (gitignored).
- STILL UNKNOWN: which header carries it, and whether it is durable. Three
  branches, best to worst:
  1. Neither `authorization` nor a `-b` cookie is present, meaning access is
     gated on `origin`/`referer`. Fix is two static headers in config. No
     secret, no expiry. Plausible, since the failing curl sent no headers.
  2. `authorization` present. Determine whether the token is static in the
     JS bundle (fetch the SPA index, grep the main.*.js bundles for the
     token value or for Bearer / access_token / static_token) and therefore
     reusable in CI, or minted at runtime by an early auth/config XHR.
  3. Only a session cookie. It will expire; do not put it in CI. Use the
     metadata-only degrade path and document the limitation honestly.
- Header names can be listed without exposing values:
  `grep -oiE "\-H '[A-Za-z0-9-]+:" notes/mcweb_browser_curl.txt | sort -u`

## Consequences for the watcher

- `fpact_manual_docs` cannot run anonymously at all; the list itself is
  blocked, not just the PDFs. It needs the browser's credential or it stays
  CONFIG_TODO with honest fine print.
- `medical_rates_page` IS readable anonymously today, so
  `ffs_rates_page_mcweb` can become a real detector with no auth work.
- If a token grants the list but not `directus_files`, degrade to
  metadata-only detection: compare `file.modified_on` and `file.id` churn
  per document. No content hash, no text diff; verdict should say so
  (CHANGED_METADATA_ONLY) and link the portal page for manual reading.

## Data model facts (2026-07-16 capture; seed in data/seeds/)

- 24 documents for communityId 25. `manuals_aggregated.count.id` = 24.
  Always request the aggregate and compare to array length as a truncation
  tripwire.
- Stable document identity: the filename stem (`benfam`, `progstand`, ...),
  which matches the runner's existing `doc_id = slug(stem)` convention.
  `manuals.id` is also stable. `file.id` is a per-upload UUID; EXPECT it to
  change on every revision. Never key on `file.id`.
- `file.modified_on` backs the portal "Revision Date" column and is rendered
  with no timezone conversion (2025-05-23T00:02:23 renders as May 23, 2025).
  Store and compare the raw string; do not parse to a datetime.
- Publish cadence: batches on the 16th of the month, roughly 15:30 to 16:45,
  observed across 2024-2026 stamps. Expect clustered flags mid-month.
- 2023-08 timestamps (pharm.pdf, radif.pdf, tarf.pdf) are CMS-migration seed
  dates, not true revision dates. Valid for forward detection only.
- Changed on 2026-07-16 around 16:28-16:29 (flagged for immediate human
  review): progstand.pdf (Program Standards, manuals.id 424) and
  provenrollres.pdf (Provider Enrollment and Responsibilities,
  manuals.id 594). Provider enrollment maps to the master rows under the
  fpact_enrollment entry.

## Working query (trimmed)

Keep the aggregate; drop `__typename`, `community`, and `communities` (the
last is anon-blocked anyway and not needed once ids are known).

```json
{"operationName": "CommunityManuals",
 "variables": {"communityId": "25"},
 "query": "query CommunityManuals($communityId: GraphQLStringOrFloat) { manuals(filter: {community: {communities_id: {id: {_eq: $communityId}}}}, sort: [\"file.filename_download\"], limit: -1) { id title file { id filename_download modified_on } } manuals_aggregated(filter: {community: {communities_id: {id: {_eq: $communityId}}}}) { count { id } } }"}
```

## Legacy host hypothesis (untested, try before token plumbing)

The filenames match the old files.medi-cal.ca.gov pubsdoco naming
(benfam.pdf, tarf.pdf; trailing "f" as in radif = Family PACT variants of
shared sections). If the legacy static host still serves them, PDFs need no
auth at all:

```
curl -sI https://files.medi-cal.ca.gov/pubsdoco/publications/masters-other/fpact/benfam.pdf
```

That host timed out on 2026-07-02 per watchlist notes; retest before ruling
it out, and also try masters-mtp paths.

## Cautions

- Undocumented internal endpoint. It can change shape or auth without
  notice. MCSS email remains the backstop detector; never retire it on the
  strength of this integration.
- Keep the UA string, SLEEP >= 1s, conditional GETs. 24 docs weekly is
  polite; keep it that way.
- Never commit tokens or the captured browser cURL. Gitignore
  `notes/mcweb_browser_curl.txt` and any `.env`.
