# mcweb / Directus reference

`mcweb.apps.prd.cammis.medi-cal.ca.gov` is the Medi-Cal provider portal SPA
that fronts publications (manuals, bulletins) and rates. Established by
DevTools capture and curl, 2026-07-02 and 2026-07-16. Read before changing
any `manual_list` or `revision_watch` entry.

## Platform

Backend is Directus. GraphQL at `POST /graphql`, files at
`/assets/<file_uuid>`. The manual page fires operation `CommunityManuals`
with `{"communityId": "<id>"}`.

Portal slugs are slugified community names ("family-pact",
"clinics-and-hospitals"). There is no RHC/FQHC community: that manual is the
`rural*` filename family inside Clinics and Hospitals, watched through a
filename-filtered query. For large communities, filter by filename rather
than watching 200+ documents wholesale.

## Community catalog

Captured 2026-07-17 with the public token; the `communities` collection is
readable, no DevTools needed.

1 Acupuncture, 2 Audiology/Hearing Aids, 3 Chiropractic, 4 DME,
5 Medical Transportation, 6 Orthotics/Prosthetics, 7 Psychological,
8 Therapies, 9 Inpatient Services (115 docs), 10 Medi-Cal Waiver,
11 Clinics and Hospitals (246 docs), 12 Chronic Dialysis, 13 CBAS,
14 Heroin Detox, 15 Home Health/HCBS, 16 Hospice, 17 LEA, 18 MSSP,
19 Rehabilitation Clinics, 20 Long Term Care, 21 General Medicine (229 docs),
22 Obstetrics, 23 Pharmacy, 24 Vision Care, 25 Family PACT (24 docs),
26 Medi-Cal Program & Eligibility.

## Auth

The endpoint requires a Bearer token; anonymous callers see only the
`medical_rates_page*` query fields, and `manuals` / `communities` return a
GraphQL validation error, which in Directus is how a permission denial
presents. `GET /assets/<file_id>` returns 403 anonymously.

The token the SPA carries is static, public and read-only, served in
`/environment.js` as `window.DIRECTUS_TOKEN`. The checker reads it from there
whenever `MCWEB_TOKEN` is unset or has been rotated, so mcweb entries need no
repository secret. Never commit a token or a captured browser cURL.

If a future token grants the list but not `directus_files`, the checker
degrades to metadata-only detection (`CHANGED_METADATA_ONLY`): compare
`file.modified_on` and `file.id` churn, no content hash, no text diff.

## Data model facts

- Always request `manuals_aggregated.count.id` and compare it to the array
  length. A mismatch is the truncation tripwire (`LIST_TRUNCATED`).
- Stable document identity is the filename stem (`benfam`, `progstand`),
  which matches `doc_id = slug(stem)`. `manuals.id` is also stable.
  `file.id` is a per-upload UUID and changes on every revision: never key
  on it.
- `file.modified_on` backs the portal Revision Date column and renders with
  no timezone conversion. Store and compare the raw string; do not parse.
- Publish cadence: batches on the 16th of the month, roughly 15:30 to 16:45,
  observed 2024 through 2026. Expect clustered flags mid-month.
- 2023-08 timestamps (pharm, radif, tarf) are CMS-migration seed dates, not
  real revisions. Valid for forward detection only.

## Working query

```json
{"operationName": "CommunityManuals",
 "variables": {"communityId": "25"},
 "query": "query CommunityManuals($communityId: GraphQLStringOrFloat) { manuals(filter: {community: {communities_id: {id: {_eq: $communityId}}}}, sort: [\"file.filename_download\"], limit: -1) { id title file { id filename_download modified_on } } manuals_aggregated(filter: {community: {communities_id: {id: {_eq: $communityId}}}}) { count { id } } }"}
```

## Cautions

- Undocumented internal endpoint. It can change shape or auth without
  notice. MCSS email is the backstop detector and must not be retired on the
  strength of this integration.
- Keep the UA string, `SLEEP >= 1`, and conditional GETs.
- Untested alternative: the filenames match the legacy
  `files.medi-cal.ca.gov/pubsdoco` naming. If that host still serves them,
  PDFs would need no auth at all. It timed out on 2026-07-02; retest before
  investing in token plumbing.
