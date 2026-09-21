# Revenue Integrity Source Watch

This page tracks changes in the official sources used by Revenue Integrity, mainly medical payer programs such as Medi-Cal and associated programs. A script runs on a scheduled cadence and checks each source, highlighting anything changed since the previous review, helping catch updates relevant to billing and revenue integrity (ICD-10 changes, coverage rules etc). **Always review and validate any listed change against the live official source before use.**

**Last check:** script ran 2026-09-21 · **items needing review: 3** · revision notices: 4

**How to read this page**

- **Needs review** - start here; this is what needs looking at now.
- **Manual revision notices** - lower priority, date-only.
- **Sources changed in the last 60 days** - the recent trail.
- **All sources by program** - current status of every watched source.

Status words are explained at the bottom in [status legend](#status-legend).

More detail: [change review page](https://mp321.github.io/RevInt-SourceWatch/changes.html) (one block per change) · [change history (CSV)](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/changes_log.csv) · [watchlist](https://github.com/mp321/RevInt-SourceWatch/blob/main/watchlist.yaml) · [all reports](https://github.com/mp321/RevInt-SourceWatch/tree/main/reports)

## Needs review (3)

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

Every item links to the source and, when text changed, to the exact before/after diff. Finding nothing behind a flag is a normal outcome: agencies re-publish files, re-shuffle links and move pages without changing policy, and the script cannot tell that apart from a real edit. Note it and move on; if the same item keeps coming back with nothing behind it, tighten or retire its watchlist entry.

- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - [fpact_manual_docs--benfam](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact) _(Family PACT)_
  - **What happened:** The text of this document is not the same as the copy stored at the last check.
  - **Watched file:** `https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED` - a portal endpoint readable only by the checker; the link above opens the portal list it belongs to.
  - **What to do:** Open the diff to see the exact lines, re-read that part of the live source, then update whatever it feeds downstream (superbill, tipsheet, Epic review as applicable).
  - **Exact change:** [reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md)
  - **Revision stamp:** 2026-09-16T16:17:12
  - **Follow-up:** ppbi_source_section rows for any changed section
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - [fpact_manual_docs--drug](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact) _(Family PACT)_
  - **What happened:** The text of this document is not the same as the copy stored at the last check.
  - **Watched file:** `https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5` - a portal endpoint readable only by the checker; the link above opens the portal list it belongs to.
  - **What to do:** Open the diff to see the exact lines, re-read that part of the live source, then update whatever it feeds downstream (superbill, tipsheet, Epic review as applicable).
  - **Exact change:** [reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md)
  - **Codes on the changed lines (heuristic, verify each):** `J7299` (HCPCS, both, low conf.) p.7; `J7300` (HCPCS, both, low conf.) p.7; `J7307` (HCPCS, both, low conf.) p.7
  - **Revision stamp:** 2026-09-16T16:17:35
  - **Follow-up:** ppbi_source_section rows for any changed section
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `LINKS_CHANGED` - [fpact_news_archive](https://familypact.org/news-and-updates-archive/) _(Family PACT)_
  - **What happened:** The list of files this page links to changed: +1 added, -1 removed. The page's own wording did not have to change for this to flag.
    - added: [https://familypact.org/planned-family-pact-portal-production-outage-september-18-20-2026/](https://familypact.org/planned-family-pact-portal-production-outage-september-18-20-2026/)
    - removed: [https://familypact.org/fda-approves-updated-nexplanon-label-and-launches-new-rems/](https://familypact.org/fda-approves-updated-nexplanon-label-and-launches-new-rems/)
  - **What to do:** Open the page, check each added or removed file listed with the item, and if a watched file was re-versioned, point watchlist.yaml at the new URL so the script keeps monitoring it.
  - **Seen before:** flagged 4 times in the last 60 days. If it keeps repeating with nothing behind it, tighten or retire the watchlist entry.
  - **Follow-up:** triage per announcement

### Manual revision notices - lower priority (4)

The Medi-Cal portal moved the Revision Date on manual sections in these communities. Date-only signal, no text diff - when time allows, skim the named sections on the portal and route anything touching billing codes or the chargemaster.

- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> [rev_clinics_hospitals_manuals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals) - 5 of 247 manual sections moved: 'Cell and Gene Therapy (cel gen over)' revised 2026-07-16 -&gt; 2026-09-16; 'List of Contracted Incontinence Creams and Washes' revised 2025-11-14 -&gt; 2026-09-16; 'Non-Physician Medical Practitioners (NMP) (non ph)' revised 2026-03-16 -&gt; 2026-09-16; 'Other Health Coverage (OHC) (oth hlth)' revised 2023-08-06 -&gt; 2026-09-16; 'List of Physician Administered Drugs and HCPCS Codes (physician list)' revised 2026-07-16 -&gt; 2026-09-16
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> [rev_general_medicine_manuals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine) - 5 of 230 manual sections moved: 'Cell and Gene Therapy (cel gen over)' revised 2026-07-16 -&gt; 2026-09-16; 'List of Contracted Incontinence Creams and Washes' revised 2025-11-14 -&gt; 2026-09-16; 'Non-Physician Medical Practitioners (NMP) (non ph)' revised 2026-03-16 -&gt; 2026-09-16; 'Other Health Coverage (OHC) (oth hlth)' revised 2023-08-06 -&gt; 2026-09-16; 'List of Physician Administered Drugs and HCPCS Codes (physician list)' revised 2026-07-16 -&gt; 2026-09-16
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> [rev_inpatient_manuals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services) - 1 of 115 manual sections moved: 'Other Health Coverage (OHC) (oth hlth)' revised 2023-08-06 -&gt; 2026-09-16
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> [rev_obstetrics_manuals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics) - 3 of 173 manual sections moved: 'Non-Physician Medical Practitioners (NMP) (non ph)' revised 2026-03-16 -&gt; 2026-09-16; 'Other Health Coverage (OHC) (oth hlth)' revised 2023-08-06 -&gt; 2026-09-16; 'List of Physician Administered Drugs and HCPCS Codes (physician list)' revised 2026-07-16 -&gt; 2026-09-16

<div style="height:1.6em"></div>

## Sources changed in the last 60 days (15)

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

The most recent change-log event per source, newest first. Use it to confirm what has been communicated downstream; every individual event is in the [change history (CSV)](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/changes_log.csv). Always verify against the live source before acting.

- 2026-09-21 - [rev_obstetrics_manuals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics) - `REVISION_NOTICE`
- 2026-09-21 - [rev_inpatient_manuals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services) - `REVISION_NOTICE`
- 2026-09-21 - [rev_general_medicine_manuals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine) - `REVISION_NOTICE`
- 2026-09-21 - [rev_clinics_hospitals_manuals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals) - `REVISION_NOTICE`
- 2026-09-21 - [fpact_news_archive](https://familypact.org/news-and-updates-archive/) - `LINKS_CHANGED`
- 2026-09-21 - [fpact_manual_docs--drug](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md)
- 2026-09-21 - [fpact_manual_docs--benfam](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md)
- 2026-09-14 - [mcp_apl_index](https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260914T190102Z_managed_medi_cal--mcp_apl_index.md)
- 2026-08-31 - [ncci_medicaid_files](https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files) - `LINKS_CHANGED`
- 2026-08-31 - [fqhc_cms_center](https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260831T194936Z_fqhc--fqhc_cms_center.md)
- 2026-08-17 - [fpact_manual_docs--lab](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260817T142327Z_fpact--fpact_manual_docs--lab.md)
- 2026-08-17 - [fpact_manual_docs--clinic](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260817T142316Z_fpact--fpact_manual_docs--clinic.md)
- 2026-08-17 - [fpact_manual_docs--bengrid](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260817T142306Z_fpact--fpact_manual_docs--bengrid.md)
- 2026-08-17 - [fpact_manual_docs--benfamrel](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260817T142303Z_fpact--fpact_manual_docs--benfamrel.md)
- 2026-07-27 - [ffs_tri_fee_schedule](https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/) - `NEW`

<div style="height:1.6em"></div>

## All sources by program

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

Every watched source and its current status, including the items flagged above. Jump to a program:

- [Family PACT](#family-pact-fpact) - 25 sources, 3 need review
- [FQHC](#fqhc-fqhc) - 6 sources
- [Managed Medi-Cal](#managed-medi-cal-managed_medi_cal) - 3 sources
- [Medi-Cal FFS](#medi-cal-ffs-medi_cal_ffs) - 2 sources
- [NCCI](#ncci-ncci) - 1 source
- [Obstetrics](#obstetrics-obstetrics) - 3 sources
- [Manual Revision Notices](#manual-revision-notices-revision_notices) - 4 sources, 4 revision notices

Each source: status first, then its links, then a Details fold-out with exactly what is checked and the caveats.

### Family PACT (`FPACT`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--00letter - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-05-23T00:02:23 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--0bhwtouse - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-06-16T16:12:25 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--1tocfpact - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-05-23T00:02:48 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--benclinic - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-11-21T18:51:48 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> fpact_manual_docs--benfam - `CHANGED` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-09-21</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-09-16T16:17:12 - checked 2026-09-21 - <a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md">text diff</a></p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> The text of this document is not the same as the copy stored at the last check.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> CHANGED - content text hash differs</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-09-21 (CHANGED)</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
<li><b>Latest diff report:</b> <a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md">reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md</a></li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--benfamrel - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-17</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-08-14T16:22:28 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-08-17 (CHANGED)</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--bengrid - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-17</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-08-14T16:22:54 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-08-17 (CHANGED)</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--claimcms - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-10-16T16:11:54 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--claimub - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-10-16T16:12:21 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--clientelig - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-04-16T16:43:52 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--clinic - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-17</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-08-14T16:23:28 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-08-17 (CHANGED)</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> fpact_manual_docs--drug - `CHANGED` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-09-21</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-09-16T16:17:35 - checked 2026-09-21 - <a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md">text diff</a></p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> The text of this document is not the same as the copy stored at the last check.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> CHANGED - content text hash differs</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-09-21 (CHANGED)</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
<li><b>Latest diff report:</b> <a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md">reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md</a></li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--drugonsite - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-06-16T15:30:42 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--fam - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-01-16T17:32:57 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--hapid - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-06-16T16:11:43 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--lab - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-17</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-08-14T16:23:59 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-08-17 (CHANGED)</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--office - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2024-07-16T16:09:38 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--pharm - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2023-08-06T02:00:31 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--pharmacy - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-10-16T16:12:48 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--progstand - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-07-16T16:28:52 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--provenrollres - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2026-07-16T16:29:22 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--provrel - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2025-02-14T17:38:10 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--radif - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2023-08-06T02:02:15 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--tarf - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">Open the portal list</a> - revision 2023-08-21T21:13:15 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Follow-up when this changes:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> fpact_news_archive - `LINKS_CHANGED` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-09-21</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://familypact.org/news-and-updates-archive/">Open the source</a> - checked 2026-09-21</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> The list of files this page links to changed: +1 added, -1 removed. The page&#x27;s own wording did not have to change for this to flag.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://familypact.org/news-and-updates-archive/">https://familypact.org/news-and-updates-archive/</a></li>
<li><b>How:</b> The page's visible text is hashed, and every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> LINKS_CHANGED - +1 link(s) added, -1 removed | added: https://familypact.org/planned-family-pact-portal-production-outage-september-18-20-2026/ | removed: https://familypact.org/fda-approves-updated-nexplanon-label-and-launches-new-rems/</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-09-21 (LINKS_CHANGED)</li>
<li><b>Watchlist note:</b> Program news archive; new post or PDF links = policy updates to read. Pattern excludes feed/json noise. Also catches re-versioned artifacts (e.g. a new Superbill filename).</li>
<li><b>Follow-up when this changes:</b> triage per announcement</li>
</ul>
</details>

### FQHC (`FQHC`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_cms_center - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-31</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center">Open the source</a> - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center">https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-08-31 (CHANGED)</li>
<li><b>Watchlist note:</b> G2025 rate, care-management code set, telehealth expiries.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_dhcs_3097_page - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/">Open the source</a> - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/">https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Wrap reconciliation forms and due-date extensions.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_rural_manual_docs--rural - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">Open the portal list</a> - revision 2026-07-16T16:54:22 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C983B7D9-42B3-4543-BF93-D272AB764BDD</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the four RHC/FQHC manual sections (rural, ruralcd billing codes, ruralex billing examples, ruralhosp swing bed) - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change. rural.pdf was revised 2026-07-16, the day before this entry was added. MCSS RHC/FQHC email remains the backstop detector.</li>
<li><b>Follow-up when this changes:</b> fqhc-billing reference rows; PPS / wrap / per-visit code rows on change</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_rural_manual_docs--ruralcd - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">Open the portal list</a> - revision 2026-06-16T15:46:44 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/2D80A3B6-A32B-4131-BE63-12EE7243A849</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the four RHC/FQHC manual sections (rural, ruralcd billing codes, ruralex billing examples, ruralhosp swing bed) - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change. rural.pdf was revised 2026-07-16, the day before this entry was added. MCSS RHC/FQHC email remains the backstop detector.</li>
<li><b>Follow-up when this changes:</b> fqhc-billing reference rows; PPS / wrap / per-visit code rows on change</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_rural_manual_docs--ruralex - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">Open the portal list</a> - revision 2023-08-06T01:58:46 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/08EC7DD1-AABE-4187-9D9E-F155C3DAF1CA</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the four RHC/FQHC manual sections (rural, ruralcd billing codes, ruralex billing examples, ruralhosp swing bed) - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change. rural.pdf was revised 2026-07-16, the day before this entry was added. MCSS RHC/FQHC email remains the backstop detector.</li>
<li><b>Follow-up when this changes:</b> fqhc-billing reference rows; PPS / wrap / per-visit code rows on change</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_rural_manual_docs--ruralhosp - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">Open the portal list</a> - revision 2024-01-16T18:04:36 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/3E8C0259-6D59-4F20-BFA3-E5AE5754F39D</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the four RHC/FQHC manual sections (rural, ruralcd billing codes, ruralex billing examples, ruralhosp swing bed) - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change. rural.pdf was revised 2026-07-16, the day before this entry was added. MCSS RHC/FQHC email remains the backstop detector.</li>
<li><b>Follow-up when this changes:</b> fqhc-billing reference rows; PPS / wrap / per-visit code rows on change</li>
</ul>
</details>

### Managed Medi-Cal (`MANAGED_MEDI_CAL`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_apl_index - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-09-14</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">Open the source</a> - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-09-14 (CHANGED)</li>
<li><b>Watchlist note:</b> All Plan Letters index, watched by page text only. APLs are served through /file/&lt;slug&gt;-pdf/ redirects rather than direct .pdf hrefs, so link diffing was removed 2026-07-24. If the text hash proves equally noisy, capture the real APL listing URL from the browser and repoint the entry; MCSS Managed Care is the backstop.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_boilerplate_contract - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf">Open the source</a> - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf">https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf</a></li>
<li><b>How:</b> The PDF is downloaded (conditional GET - the server may answer '304 not modified' and skip the download), its text is extracted and hashed, and the hash is compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Hard-dated versioned filename (2025/10 upload path) - a revision likely ships under a new URL, which this entry alone cannot see. Treat as a point-in-time watch.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_tri_faq - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf">Open the source</a> - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf">https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf</a></li>
<li><b>How:</b> The PDF is downloaded (conditional GET - the server may answer '304 not modified' and skip the download), its text is extracted and hashed, and the hash is compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Hard-dated filename (20250312), so a revision ships under a new URL and this entry goes UNREACHABLE rather than CHANGED. Read a 404 here as &quot;the FAQ was reissued, find it on the TRI landing page&quot;. This URL also intermittently answers 200 with an HTML bot-check page instead of the PDF; that reports UNREACHABLE and keeps the last good baseline.</li>
</ul>
</details>

### Medi-Cal FFS (`MEDI_CAL_FFS`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ffs_sb94_fp_fee_schedule - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">Open the source</a> - <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx">watched file</a> (clicking downloads an Excel file) - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx</a> (clicking downloads an Excel file)</li>
<li><b>Where to open it:</b> <a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/</a> - the page this file is published on. The script checks the file itself; a person should start here.</li>
<li><b>How:</b> The raw file bytes are hashed and compared; no text is extracted, so this entry can never produce a text diff. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> SB 94 comprehensive family-planning fee schedule (supersedes TRI for FP codes with Z30.x). Binary watch - a spreadsheet has no extractable text, so this entry reports that the file changed, not which rows changed; open it from the landing page to compare.</li>
<li><b>Follow-up when this changes:</b> FPACT rows priced on the SB 94 schedule</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ffs_tri_fee_schedule - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-07-27</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">Open the source</a> - <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx">watched file</a> (clicking downloads an Excel file) - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx</a> (clicking downloads an Excel file)</li>
<li><b>Where to open it:</b> <a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/</a> - the page this file is published on. The script checks the file itself; a person should start here.</li>
<li><b>How:</b> The raw file bytes are hashed and compared; no text is extracted, so this entry can never produce a text diff. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-07-27 (NEW)</li>
<li><b>Watchlist note:</b> CY 2024 Targeted Rate Increase fee schedule - the code list and rates for primary care, obstetric and non-specialty mental health services. Rates stay in effect until further notice (Prop 35), so a content change here is a real rate or code-list change.</li>
<li><b>Follow-up when this changes:</b> reimbursement_basis rows citing TRI</li>
</ul>
</details>

### NCCI (`NCCI`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ncci_medicaid_files - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-31</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files">Open the source</a> - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files">https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files</a></li>
<li><b>How:</b> The page's visible text is hashed, and every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-08-31 (LINKS_CHANGED)</li>
<li><b>Watchlist note:</b> Quarterly PTP/MUE file drops appear as new links (first run captured the 2026 Q3 set effective 07/01/2026). File links are direct downloads (.zip/.xlsx).</li>
</ul>
</details>

### Obstetrics (`OBSTETRICS`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ob_cpsp_manual_docs--pregcom - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics">Open the portal list</a> - revision 2025-07-16T16:25:15 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7E3FF663-2682-4A45-82A5-688A7D42FD46</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the three Comprehensive Perinatal Services Program (CPSP) sections of the Obstetrics manual - the policy section (preg com), the CMS-1500 billing examples (preg com exc) and the list of billing codes. Each is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change - so a CPSP code or rate change is reported with the changed lines, not just the date. All three were last revised 2025-07-16. The rest of the Obstetrics manual is covered date-only by rev_obstetrics_manuals. MCSS Obstetrics email remains the backstop detector.</li>
<li><b>Follow-up when this changes:</b> CPSP per-visit and support-service billing rows on change</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ob_cpsp_manual_docs--pregcomexc - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics">Open the portal list</a> - revision 2025-07-16T16:25:32 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/21AA9E49-37BD-473D-BBF6-0756C8ED95C6</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the three Comprehensive Perinatal Services Program (CPSP) sections of the Obstetrics manual - the policy section (preg com), the CMS-1500 billing examples (preg com exc) and the list of billing codes. Each is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change - so a CPSP code or rate change is reported with the changed lines, not just the date. All three were last revised 2025-07-16. The rest of the Obstetrics manual is covered date-only by rev_obstetrics_manuals. MCSS Obstetrics email remains the backstop detector.</li>
<li><b>Follow-up when this changes:</b> CPSP per-visit and support-service billing rows on change</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ob_cpsp_manual_docs--pregcomlis - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics">Open the portal list</a> - revision 2025-07-16T16:25:54 - checked 2026-09-21</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B49DC7A8-9C98-475A-AFF8-F3702FE0AB0F</code> - a portal endpoint that returns the document only to the checker's token, so it does not open in a browser</li>
<li><b>Where to open it:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics</a> - the portal list this section is published in; open it there.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the three Comprehensive Perinatal Services Program (CPSP) sections of the Obstetrics manual - the policy section (preg com), the CMS-1500 billing examples (preg com exc) and the list of billing codes. Each is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change - so a CPSP code or rate change is reported with the changed lines, not just the date. All three were last revised 2025-07-16. The rest of the Obstetrics manual is covered date-only by rev_obstetrics_manuals. MCSS Obstetrics email remains the backstop detector.</li>
<li><b>Follow-up when this changes:</b> CPSP per-visit and support-service billing rows on change</li>
</ul>
</details>

### Manual Revision Notices (`REVISION_NOTICES`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> rev_clinics_hospitals_manuals - `REVISION_NOTICE` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-09-21</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">Open the source</a> - checked 2026-09-21</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> 5 of 247 manual sections moved: &#x27;Cell and Gene Therapy (cel gen over)&#x27; revised 2026-07-16 -&gt; 2026-09-16; &#x27;List of Contracted Incontinence Creams and Washes&#x27; revised 2025-11-14 -&gt; 2026-09-16; &#x27;Non-Physician Medical Practitioners (NMP) (non ph)&#x27; revised 2026-03-16 -&gt; 2026-09-16; &#x27;Other Health Coverage (OHC) (oth hlth)&#x27; revised 2023-08-06 -&gt; 2026-09-16; &#x27;List of Physician Administered Drugs and HCPCS Codes (physician list)&#x27; revised 2026-07-16 -&gt; 2026-09-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals</a></li>
<li><b>How:</b> The portal's manual list for this community is queried for metadata only - no PDFs are downloaded. Each section's Revision Date is compared with the previous check; movement produces a lower-priority revision notice naming the sections. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> REVISION_NOTICE - 5 of 247 manual sections moved: &#x27;Cell and Gene Therapy (cel gen over)&#x27; revised 2026-07-16 -&gt; 2026-09-16; &#x27;List of Contracted Incontinence Creams and Washes&#x27; revised 2025-11-14 -&gt; 2026-09-16; &#x27;Non-Physician Medical Practitioners (NMP) (non ph)&#x27; revised 2026-03-16 -&gt; 2026-09-16; &#x27;Other Health Coverage (OHC) (oth hlth)&#x27; revised 2023-08-06 -&gt; 2026-09-16; &#x27;List of Physician Administered Drugs and HCPCS Codes (physician list)&#x27; revised 2026-07-16 -&gt; 2026-09-16</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-09-21 (REVISION_NOTICE)</li>
<li><b>Watchlist note:</b> Clinics and Hospitals manual, ~246 sections (includes the rural* RHC/FQHC sections that fqhc_rural_manual_docs monitors in full - a notice here plus a quiet fqhc row means the movement was outside the rural sections).</li>
<li><b>Follow-up when this changes:</b> outpatient clinic / hospital billing rows on related section changes</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> rev_general_medicine_manuals - `REVISION_NOTICE` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-09-21</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine">Open the source</a> - checked 2026-09-21</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> 5 of 230 manual sections moved: &#x27;Cell and Gene Therapy (cel gen over)&#x27; revised 2026-07-16 -&gt; 2026-09-16; &#x27;List of Contracted Incontinence Creams and Washes&#x27; revised 2025-11-14 -&gt; 2026-09-16; &#x27;Non-Physician Medical Practitioners (NMP) (non ph)&#x27; revised 2026-03-16 -&gt; 2026-09-16; &#x27;Other Health Coverage (OHC) (oth hlth)&#x27; revised 2023-08-06 -&gt; 2026-09-16; &#x27;List of Physician Administered Drugs and HCPCS Codes (physician list)&#x27; revised 2026-07-16 -&gt; 2026-09-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine</a></li>
<li><b>How:</b> The portal's manual list for this community is queried for metadata only - no PDFs are downloaded. Each section's Revision Date is compared with the previous check; movement produces a lower-priority revision notice naming the sections. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> REVISION_NOTICE - 5 of 230 manual sections moved: &#x27;Cell and Gene Therapy (cel gen over)&#x27; revised 2026-07-16 -&gt; 2026-09-16; &#x27;List of Contracted Incontinence Creams and Washes&#x27; revised 2025-11-14 -&gt; 2026-09-16; &#x27;Non-Physician Medical Practitioners (NMP) (non ph)&#x27; revised 2026-03-16 -&gt; 2026-09-16; &#x27;Other Health Coverage (OHC) (oth hlth)&#x27; revised 2023-08-06 -&gt; 2026-09-16; &#x27;List of Physician Administered Drugs and HCPCS Codes (physician list)&#x27; revised 2026-07-16 -&gt; 2026-09-16</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-09-21 (REVISION_NOTICE)</li>
<li><b>Watchlist note:</b> General Medicine manual, ~229 sections - E&amp;M, telehealth, preventive services and other chargemaster-relevant policy.</li>
<li><b>Follow-up when this changes:</b> professional-services billing rows on related section changes</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> rev_inpatient_manuals - `REVISION_NOTICE` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-09-21</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services">Open the source</a> - checked 2026-09-21</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> 1 of 115 manual sections moved: &#x27;Other Health Coverage (OHC) (oth hlth)&#x27; revised 2023-08-06 -&gt; 2026-09-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services</a></li>
<li><b>How:</b> The portal's manual list for this community is queried for metadata only - no PDFs are downloaded. Each section's Revision Date is compared with the previous check; movement produces a lower-priority revision notice naming the sections. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> REVISION_NOTICE - 1 of 115 manual sections moved: &#x27;Other Health Coverage (OHC) (oth hlth)&#x27; revised 2023-08-06 -&gt; 2026-09-16</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-09-21 (REVISION_NOTICE)</li>
<li><b>Watchlist note:</b> Inpatient Services manual, ~115 sections. Date-only signal for inpatient billing / revenue integrity awareness.</li>
<li><b>Follow-up when this changes:</b> inpatient billing rows on related section changes</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> rev_obstetrics_manuals - `REVISION_NOTICE` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-09-21</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics">Open the source</a> - checked 2026-09-21</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> 3 of 173 manual sections moved: &#x27;Non-Physician Medical Practitioners (NMP) (non ph)&#x27; revised 2026-03-16 -&gt; 2026-09-16; &#x27;Other Health Coverage (OHC) (oth hlth)&#x27; revised 2023-08-06 -&gt; 2026-09-16; &#x27;List of Physician Administered Drugs and HCPCS Codes (physician list)&#x27; revised 2026-07-16 -&gt; 2026-09-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics</a></li>
<li><b>How:</b> The portal's manual list for this community is queried for metadata only - no PDFs are downloaded. Each section's Revision Date is compared with the previous check; movement produces a lower-priority revision notice naming the sections. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> REVISION_NOTICE - 3 of 173 manual sections moved: &#x27;Non-Physician Medical Practitioners (NMP) (non ph)&#x27; revised 2026-03-16 -&gt; 2026-09-16; &#x27;Other Health Coverage (OHC) (oth hlth)&#x27; revised 2023-08-06 -&gt; 2026-09-16; &#x27;List of Physician Administered Drugs and HCPCS Codes (physician list)&#x27; revised 2026-07-16 -&gt; 2026-09-16</li>
<li><b>Last checked:</b> 2026-09-21</li>
<li><b>Last recorded change:</b> 2026-09-21 (REVISION_NOTICE)</li>
<li><b>Watchlist note:</b> Obstetrics manual, 172 sections - the whole community page, including pregnancy global and per-visit billing, CPSP, doula services, presumptive eligibility and the CCS sections. Date-only signal - it names the sections whose Revision Date moved and reports sections added or removed, with no PDF download and no text diff. The three CPSP sections inside it are monitored in full text by ob_cpsp_manual_docs, so a notice here with quiet ob_cpsp_manual_docs rows means the movement was outside CPSP.</li>
<li><b>Follow-up when this changes:</b> obstetric and perinatal billing rows on related section changes</li>
</ul>
</details>

### Source URLs at a glance

One row per watched URL, grouped and **colored by website**. Portal endpoints are shown as plain text: they return their document only to the checker's token, so the link to open is the portal page on that source's row above.

<ul style="list-style:none;padding-left:0;font-size:.85em;line-height:1.7">
<li style="color:#14632e;font-weight:600">fpact_news_archive - <a href="https://familypact.org/news-and-updates-archive/" style="color:#14632e">https://familypact.org/news-and-updates-archive/</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--00letter - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--0bhwtouse - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--1tocfpact - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--benclinic - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--benfam - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--benfamrel - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--bengrid - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--claimcms - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--claimub - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--clientelig - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--clinic - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--drug - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--drugonsite - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--fam - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--hapid - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--lab - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--office - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--pharm - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--pharmacy - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--progstand - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--provenrollres - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--provrel - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--radif - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0</code></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--tarf - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705</code></li>
<li style="color:#5b2d86;font-weight:600">fqhc_rural_manual_docs--rural - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C983B7D9-42B3-4543-BF93-D272AB764BDD</code></li>
<li style="color:#5b2d86;font-weight:600">fqhc_rural_manual_docs--ruralcd - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/2D80A3B6-A32B-4131-BE63-12EE7243A849</code></li>
<li style="color:#5b2d86;font-weight:600">fqhc_rural_manual_docs--ruralex - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/08EC7DD1-AABE-4187-9D9E-F155C3DAF1CA</code></li>
<li style="color:#5b2d86;font-weight:600">fqhc_rural_manual_docs--ruralhosp - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/3E8C0259-6D59-4F20-BFA3-E5AE5754F39D</code></li>
<li style="color:#5b2d86;font-weight:600">ob_cpsp_manual_docs--pregcom - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7E3FF663-2682-4A45-82A5-688A7D42FD46</code></li>
<li style="color:#5b2d86;font-weight:600">ob_cpsp_manual_docs--pregcomexc - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/21AA9E49-37BD-473D-BBF6-0756C8ED95C6</code></li>
<li style="color:#5b2d86;font-weight:600">ob_cpsp_manual_docs--pregcomlis - <code>https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B49DC7A8-9C98-475A-AFF8-F3702FE0AB0F</code></li>
<li style="color:#5b2d86;font-weight:600">rev_clinics_hospitals_manuals - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals</a></li>
<li style="color:#5b2d86;font-weight:600">rev_general_medicine_manuals - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine</a></li>
<li style="color:#5b2d86;font-weight:600">rev_inpatient_manuals - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services</a></li>
<li style="color:#5b2d86;font-weight:600">rev_obstetrics_manuals - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics</a></li>
<li style="color:#8b1a1a;font-weight:600">fqhc_cms_center - <a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center" style="color:#8b1a1a">https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center</a></li>
<li style="color:#8b1a1a;font-weight:600">ncci_medicaid_files - <a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files" style="color:#8b1a1a">https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files</a></li>
<li style="color:#1f4e79;font-weight:600">ffs_sb94_fp_fee_schedule - <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx" style="color:#1f4e79">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx</a></li>
<li style="color:#1f4e79;font-weight:600">ffs_tri_fee_schedule - <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx" style="color:#1f4e79">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx</a></li>
<li style="color:#1f4e79;font-weight:600">fqhc_dhcs_3097_page - <a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/" style="color:#1f4e79">https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/</a></li>
<li style="color:#1f4e79;font-weight:600">mcp_apl_index - <a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx" style="color:#1f4e79">https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx</a></li>
<li style="color:#1f4e79;font-weight:600">mcp_boilerplate_contract - <a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf" style="color:#1f4e79">https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf</a></li>
<li style="color:#1f4e79;font-weight:600">mcp_tri_faq - <a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf" style="color:#1f4e79">https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf</a></li>
</ul>

<div style="height:1.6em"></div>

## Status legend

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<table style="font-size:.85em;line-height:1.45">
<tr><th>Status</th><th>Code</th><th>What it means, and what to do</th></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>CHANGED</code></td><td>The extracted text of this source differs from the last run. <i>Open the diff to see the exact lines, re-read that part of the live source, then update whatever it feeds downstream (superbill, tipsheet, Epic review as applicable).</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>NEW</code></td><td>First run for this source; its current state became the baseline. <i>Skim the source once to confirm it is the right document.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>DATE_CHANGED</code></td><td>A revision or &#x27;page updated&#x27; stamp moved but the content text did not. <i>Open the source and confirm nothing substantive changed; usually a republish.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>LINKS_CHANGED</code></td><td>The set of files this page links to changed (often a re-versioned filename, e.g. a new Superbill). <i>Open the page, check each added or removed file listed with the item, and if a watched file was re-versioned, point watchlist.yaml at the new URL so the script keeps monitoring it.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>NEW_ISSUE</code></td><td>A probed bulletin issue number returned real content. <i>Read the new bulletin and triage anything that affects billing.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>REMOVED</code></td><td>A document disappeared from the portal&#x27;s list. <i>Check the portal: retired, renamed, or moved? If the section is gone, repoint anything that cites it.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>URL_CHANGED_IN_CONFIG</code></td><td>The URL in watchlist.yaml differs from the URL the baseline was built from. <i>Confirm the new URL is intentional; the next run with --update re-baselines it.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>CHANGED_METADATA_ONLY</code></td><td>The portal says this section was revised (new revision date or file id) but the PDF itself could not be downloaded, so there is no text diff. <i>Open the section on the portal and re-read it by hand.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>LIST_TRUNCATED</code></td><td>The portal returned fewer documents than its own count claims. <i>Open the portal list and compare; some sections may be silently unmonitored until this clears.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span></td><td><code>REVISION_NOTICE</code></td><td>The Medi-Cal portal moved the Revision Date on one or more manual sections in this community. Date-only signal - the section text is not monitored here, so there is no diff. <i>When time allows, open the community&#x27;s manual page, skim the sections named in the notice, and route anything touching billing codes or the chargemaster.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>UNREACHABLE</code></td><td>The fetch failed this run (HTTP error, network error, robots.txt, or an off-site redirect) - the Why line says which. <i>If it persists more than one run, open the URL in a browser - the page may have moved - and repoint watchlist.yaml. Until then this source is unmonitored.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>MANUAL_REVIEW</code></td><td>This source cannot be fetched automatically, by design (reason in the fine print). <i>Open the link by hand on the cadence given in the fine print; MCSS email is the push detector.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>BLIND_SHELL</code></td><td>The page builds its content with JavaScript, so the checker sees only an empty app shell and cannot detect content changes. <i>Do not rely on this row for detection; MCSS email covers it. Open the page yourself when in doubt.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>PROBE_INCONCLUSIVE</code></td><td>The bulletin probe could not confirm or rule out a new issue (client-rendered portal). <i>Nothing to do; MCSS email is the reliable detector for bulletins.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>CONFIG_TODO</code></td><td>The watchlist entry is incomplete, so nothing is monitored for it yet. <i>Finish the entry in watchlist.yaml; the Why line says what is missing.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#eef1f5;color:#3f4c5a;white-space:nowrap">Not yet checked</span></td><td><code>not_yet_checked</code></td><td>The entry is in watchlist.yaml but the last run did not cover it, normally because it was added after that run. <i>Nothing to do; the next scheduled run reports it.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span></td><td><code>unchanged</code></td><td>No change detected. <i>Nothing to do.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span></td><td><code>metadata_only_unchanged</code></td><td>The PDF is not directly downloadable, but the portal&#x27;s revision metadata is unchanged. <i>Nothing to do.</i></td></tr>
</table>

---

**Keeping it working:** if the date of the last check at the top of this page is more than 35 days old, the script may not be running - notify the maintainer. Sources can change, so update watchlist as needed.

This page is rebuilt each time script runs (`write_dashboard` method in [source_check.py](https://github.com/mp321/RevInt-SourceWatch/blob/main/source_check.py)); edit that to update this page.

Provided as-is, without warranty of any kind, as general decision support. It is not legal, coding or billing advice - always refer to the live official source. Built and maintained by [Michael Phipps](https://github.com/mp321); released under the MIT license ([LICENSE](https://github.com/mp321/RevInt-SourceWatch/blob/main/LICENSE)). If you reuse or adapt it, a credit link back to the [repository](https://github.com/mp321/RevInt-SourceWatch) is appreciated.
