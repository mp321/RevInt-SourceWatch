# Revenue Integrity Source Watch

This page keeps track of the official sources behind Revenue Integrity work - Medi-Cal and Family PACT provider manuals, bulletins, fee schedule pages and policy letters - and shows what has changed on them. A script re-reads each source on a schedule and lists anything that moved since the previous check, so updates can be caught and routed (provider communication, superbill or tipsheet, Epic review) instead of being noticed by accident. **Always review and validate anything here against the live official source before using it or acting on it.**

**Last check:** script ran 2026-08-10 · **items needing review: 2**

**How to read this page**

Start at "Needs review" - that is what a person needs to look at now. After it come lower-priority revision notices, everything that changed in the last 60 days, and then the current status of every watched source under "All sources by program". Status words like `CHANGED` are explained in the [status legend](#status-legend) at the bottom.

More detail: [change review page](https://mp321.github.io/RevInt-SourceWatch/changes.html) (one block per change) · [change history (CSV)](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/changes_log.csv) · [watchlist](https://github.com/mp321/RevInt-SourceWatch/blob/main/watchlist.yaml) · [all reports](https://github.com/mp321/RevInt-SourceWatch/tree/main/reports)

## Needs review (2)

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

Every item links to the source and, when text changed, to the exact before/after diff. If you open a source and cannot find anything that actually changed, that is a normal outcome: agencies re-publish files, re-shuffle links and move pages without changing policy, and the script cannot tell that apart from a real edit. Note it and move on - and if the same item keeps coming back with nothing behind it, its watchlist entry should be tightened or removed rather than re-read every week.

- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - [fqhc_cms_center](https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center) _(FQHC)_
  - **What happened:** The text of this document is not the same as the copy stored at the last check.
  - **What to do:** Open the diff to see the exact lines, re-read that part of the live source, then verify the listed registry rows (superbill, tipsheet, Epic review as applicable).
  - **Seen before:** flagged 2 times in the last 60 days. If the source reads the same as last time, the page most likely re-published or re-shuffled its own files rather than changing policy - note that and move on, and if it keeps repeating, tighten or retire the watchlist entry.
  - **Exact change:** [reports/diffs/20260810T145505Z_fqhc--fqhc_cms_center.md](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260810T145505Z_fqhc--fqhc_cms_center.md)
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - [ncci_medicaid_files](https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files) _(NCCI)_
  - **What happened:** The text of this document is not the same as the copy stored at the last check.
  - **What to do:** Open the diff to see the exact lines, re-read that part of the live source, then verify the listed registry rows (superbill, tipsheet, Epic review as applicable).
  - **Seen before:** flagged 2 times in the last 60 days. If the source reads the same as last time, the page most likely re-published or re-shuffled its own files rather than changing policy - note that and move on, and if it keeps repeating, tighten or retire the watchlist entry.
  - **Exact change:** [reports/diffs/20260810T145521Z_ncci--ncci_medicaid_files.md](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260810T145521Z_ncci--ncci_medicaid_files.md)

<div style="height:1.6em"></div>

## Changed in the last 60 days (5)

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

The recent trail, newest first - use it to confirm what has been communicated downstream. Always verify against the live source before acting.

- 2026-08-10 - [ncci_medicaid_files](https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260810T145521Z_ncci--ncci_medicaid_files.md)
- 2026-08-10 - [fqhc_cms_center](https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260810T145505Z_fqhc--fqhc_cms_center.md)
- 2026-08-03 - [mcp_apl_index](https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx) - `CHANGED` - [what changed](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260803T162103Z_managed_medi_cal--mcp_apl_index.md)
- 2026-07-27 - [ffs_tri_fee_schedule](https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/) - `NEW`
- 2026-07-27 - [fpact_news_archive](https://familypact.org/news-and-updates-archive/) - `LINKS_CHANGED`

<div style="height:1.6em"></div>

## All sources by program

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

Every watched source and its current status, including the items flagged above. Jump to a program:

- [Family PACT](#family-pact-fpact) - 25 sources
- [FQHC](#fqhc-fqhc) - 6 sources, 1 needs review
- [Managed Medi-Cal](#managed-medi-cal-managed_medi_cal) - 3 sources
- [Medi-Cal FFS](#medi-cal-ffs-medi_cal_ffs) - 2 sources
- [NCCI](#ncci-ncci) - 1 source, 1 needs review
- [Manual Revision Notices](#manual-revision-notices-revision_notices) - 3 sources

Each source: status first, then its links, then a Details fold-out with exactly what is checked and the caveats.

### Family PACT (`FPACT`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--00letter - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B">Open the source</a> - revision 2025-05-23T00:02:23 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--0bhwtouse - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A">Open the source</a> - revision 2025-06-16T16:12:25 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--1tocfpact - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71">Open the source</a> - revision 2025-05-23T00:02:48 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--benclinic - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43">Open the source</a> - revision 2025-11-21T18:51:48 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--benfam - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED">Open the source</a> - revision 2026-05-15T16:52:05 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--benfamrel - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8">Open the source</a> - revision 2026-05-15T16:52:25 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--bengrid - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683">Open the source</a> - revision 2026-05-18T17:42:58 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--claimcms - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D">Open the source</a> - revision 2025-10-16T16:11:54 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--claimub - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F">Open the source</a> - revision 2025-10-16T16:12:21 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--clientelig - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A">Open the source</a> - revision 2026-04-16T16:43:52 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--clinic - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10">Open the source</a> - revision 2026-05-15T16:53:48 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--drug - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5">Open the source</a> - revision 2026-03-16T16:27:32 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--drugonsite - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC">Open the source</a> - revision 2026-06-16T15:30:42 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--fam - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528">Open the source</a> - revision 2025-01-16T17:32:57 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--hapid - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326">Open the source</a> - revision 2025-06-16T16:11:43 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--lab - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B">Open the source</a> - revision 2026-01-20T17:54:24 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--office - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F">Open the source</a> - revision 2024-07-16T16:09:38 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--pharm - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00">Open the source</a> - revision 2023-08-06T02:00:31 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--pharmacy - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F">Open the source</a> - revision 2025-10-16T16:12:48 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--progstand - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904">Open the source</a> - revision 2026-07-16T16:28:52 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--provenrollres - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29">Open the source</a> - revision 2026-07-16T16:29:22 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--provrel - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643">Open the source</a> - revision 2025-02-14T17:38:10 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--radif - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0">Open the source</a> - revision 2023-08-06T02:02:15 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--tarf - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705">Open the source</a> - revision 2023-08-21T21:13:15 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for all 24 Family PACT manual sections. Each section is watched individually - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, new sections auto-discovered, removals flagged - and a CHANGED section gets a before/after text diff. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY rather than going blind. The endpoint is undocumented and can change shape or auth without notice, so MCSS email stays the backstop detector. Decision support, not a source of record.</li>
<li><b>Registry rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_news_archive - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-07-27</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://familypact.org/news-and-updates-archive/">Open the source</a> - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://familypact.org/news-and-updates-archive/">https://familypact.org/news-and-updates-archive/</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> 2026-07-27 (LINKS_CHANGED)</li>
<li><b>Watchlist note:</b> Program news archive; new post or PDF links = policy updates to read. Pattern excludes feed/json noise. Also catches re-versioned artifacts (e.g. a new Superbill filename).</li>
<li><b>Registry rows to verify on change:</b> triage per announcement</li>
</ul>
</details>

### FQHC (`FQHC`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> fqhc_cms_center - `CHANGED` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-10</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center">Open the source</a> - checked 2026-08-10 - <a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260810T145505Z_fqhc--fqhc_cms_center.md">text diff</a></p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> The text of this document is not the same as the copy stored at the last check.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center">https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> CHANGED - content text hash differs</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> 2026-08-10 (CHANGED)</li>
<li><b>Watchlist note:</b> G2025 rate, care-management code set, telehealth expiries.</li>
<li><b>Registry rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
<li><b>Latest diff report:</b> <a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260810T145505Z_fqhc--fqhc_cms_center.md">reports/diffs/20260810T145505Z_fqhc--fqhc_cms_center.md</a></li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_dhcs_3097_page - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/">Open the source</a> - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/">https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Wrap reconciliation forms and due-date extensions.</li>
<li><b>Registry rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_rural_manual_docs--rural - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C983B7D9-42B3-4543-BF93-D272AB764BDD">Open the source</a> - revision 2026-07-16T16:54:22 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C983B7D9-42B3-4543-BF93-D272AB764BDD">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C983B7D9-42B3-4543-BF93-D272AB764BDD</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the four RHC/FQHC manual sections (rural, ruralcd billing codes, ruralex billing examples, ruralhosp swing bed) - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change. rural.pdf was revised 2026-07-16, the day before this entry was added. MCSS RHC/FQHC email remains the backstop detector.</li>
<li><b>Registry rows to verify on change:</b> fqhc-billing reference rows; PPS / wrap / per-visit code rows on change</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_rural_manual_docs--ruralcd - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/2D80A3B6-A32B-4131-BE63-12EE7243A849">Open the source</a> - revision 2026-06-16T15:46:44 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/2D80A3B6-A32B-4131-BE63-12EE7243A849">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/2D80A3B6-A32B-4131-BE63-12EE7243A849</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the four RHC/FQHC manual sections (rural, ruralcd billing codes, ruralex billing examples, ruralhosp swing bed) - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change. rural.pdf was revised 2026-07-16, the day before this entry was added. MCSS RHC/FQHC email remains the backstop detector.</li>
<li><b>Registry rows to verify on change:</b> fqhc-billing reference rows; PPS / wrap / per-visit code rows on change</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_rural_manual_docs--ruralex - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/08EC7DD1-AABE-4187-9D9E-F155C3DAF1CA">Open the source</a> - revision 2023-08-06T01:58:46 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/08EC7DD1-AABE-4187-9D9E-F155C3DAF1CA">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/08EC7DD1-AABE-4187-9D9E-F155C3DAF1CA</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the four RHC/FQHC manual sections (rural, ruralcd billing codes, ruralex billing examples, ruralhosp swing bed) - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change. rural.pdf was revised 2026-07-16, the day before this entry was added. MCSS RHC/FQHC email remains the backstop detector.</li>
<li><b>Registry rows to verify on change:</b> fqhc-billing reference rows; PPS / wrap / per-visit code rows on change</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_rural_manual_docs--ruralhosp - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/3E8C0259-6D59-4F20-BFA3-E5AE5754F39D">Open the source</a> - revision 2024-01-16T18:04:36 - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/3E8C0259-6D59-4F20-BFA3-E5AE5754F39D">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/3E8C0259-6D59-4F20-BFA3-E5AE5754F39D</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the four RHC/FQHC manual sections (rural, ruralcd billing codes, ruralex billing examples, ruralhosp swing bed) - full PDF text hash, per-page &quot;Page updated&quot; stamps, portal Revision Date, diffs on change. rural.pdf was revised 2026-07-16, the day before this entry was added. MCSS RHC/FQHC email remains the backstop detector.</li>
<li><b>Registry rows to verify on change:</b> fqhc-billing reference rows; PPS / wrap / per-visit code rows on change</li>
</ul>
</details>

### Managed Medi-Cal (`MANAGED_MEDI_CAL`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_apl_index - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-03</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">Open the source</a> - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> 2026-08-03 (CHANGED)</li>
<li><b>Watchlist note:</b> All Plan Letters index, watched by page text only. APLs are served through /file/&lt;slug&gt;-pdf/ redirects rather than direct .pdf hrefs, so link diffing was removed 2026-07-24. If the text hash proves equally noisy, capture the real APL listing URL from the browser and repoint the entry; MCSS Managed Care is the backstop.</li>
<li><b>Registry rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_boilerplate_contract - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf">Open the source</a> - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf">https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf</a></li>
<li><b>How:</b> The PDF is downloaded (conditional GET - the server may answer '304 not modified' and skip the download), its text is extracted and hashed, and the hash is compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Hard-dated versioned filename (2025/10 upload path) - a revision likely ships under a new URL, which this entry alone cannot see. Treat as a point-in-time watch.</li>
<li><b>Registry rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_tri_faq - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf">Open the source</a> - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf">https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf</a></li>
<li><b>How:</b> The PDF is downloaded (conditional GET - the server may answer '304 not modified' and skip the download), its text is extracted and hashed, and the hash is compared with the copy stored at the previous check. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Hard-dated filename (20250312), so a revision ships under a new URL and this entry goes UNREACHABLE rather than CHANGED. Read a 404 here as &quot;the FAQ was reissued, find it on the TRI landing page&quot;. This URL also intermittently answers 200 with an HTML bot-check page instead of the PDF; that reports UNREACHABLE and keeps the last good baseline.</li>
<li><b>Registry rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

### Medi-Cal FFS (`MEDI_CAL_FFS`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ffs_sb94_fp_fee_schedule - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">Open the source</a> - <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx">watched file</a> (clicking downloads an Excel file) - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx</a> (clicking downloads an Excel file)</li>
<li><b>Where to open it:</b> <a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/</a> - the page this file is published on. The script checks the file itself; a person should start here.</li>
<li><b>How:</b> The raw file bytes are hashed and compared; no text is extracted, so this entry can never produce a text diff. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> SB 94 comprehensive family-planning fee schedule (supersedes TRI for FP codes with Z30.x). Binary watch - a spreadsheet has no extractable text, so this entry reports that the file changed, not which rows changed; open it from the landing page to compare.</li>
<li><b>Registry rows to verify on change:</b> FPACT rows priced on the SB 94 schedule</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ffs_tri_fee_schedule - `unchanged` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-07-27</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">Open the source</a> - <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx">watched file</a> (clicking downloads an Excel file) - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx</a> (clicking downloads an Excel file)</li>
<li><b>Where to open it:</b> <a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/</a> - the page this file is published on. The script checks the file itself; a person should start here.</li>
<li><b>How:</b> The raw file bytes are hashed and compared; no text is extracted, so this entry can never produce a text diff. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> 2026-07-27 (NEW)</li>
<li><b>Watchlist note:</b> CY 2024 Targeted Rate Increase fee schedule - the code list and rates for primary care, obstetric and non-specialty mental health services. Rates stay in effect until further notice (Prop 35), so a content change here is a real rate or code-list change.</li>
<li><b>Registry rows to verify on change:</b> reimbursement_basis rows citing TRI</li>
</ul>
</details>

### NCCI (`NCCI`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> ncci_medicaid_files - `CHANGED` <span style="display:inline-block;padding:.05em .5em;border-radius:1em;font-size:.72em;font-weight:600;background:#fff3cd;color:#6b4e00;white-space:nowrap">changed 2026-08-10</span>

<p style="margin:.2em 0 .2em 2em"><a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files">Open the source</a> - checked 2026-08-10 - <a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260810T145521Z_ncci--ncci_medicaid_files.md">text diff</a></p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> The text of this document is not the same as the copy stored at the last check.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files">https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> CHANGED - content text hash differs</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> 2026-08-10 (CHANGED)</li>
<li><b>Watchlist note:</b> Quarterly PTP/MUE file drops appear as new links (first run captured the 2026 Q3 set effective 07/01/2026). File links are direct downloads (.zip/.xlsx).</li>
<li><b>Registry rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
<li><b>Latest diff report:</b> <a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260810T145521Z_ncci--ncci_medicaid_files.md">reports/diffs/20260810T145521Z_ncci--ncci_medicaid_files.md</a></li>
</ul>
</details>

### Manual Revision Notices (`REVISION_NOTICES`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> rev_clinics_hospitals_manuals - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">Open the source</a> - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals</a></li>
<li><b>How:</b> The portal's manual list for this community is queried for metadata only - no PDFs are downloaded. Each section's Revision Date is compared with the previous check; movement produces a lower-priority revision notice naming the sections. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 246 sections, no revision-date movement</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Clinics and Hospitals manual, ~246 sections (includes the rural* RHC/FQHC sections that fqhc_rural_manual_docs monitors in full - a notice here plus a quiet fqhc row means the movement was outside the rural sections).</li>
<li><b>Registry rows to verify on change:</b> outpatient clinic / hospital billing rows on related section changes</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> rev_general_medicine_manuals - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine">Open the source</a> - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine</a></li>
<li><b>How:</b> The portal's manual list for this community is queried for metadata only - no PDFs are downloaded. Each section's Revision Date is compared with the previous check; movement produces a lower-priority revision notice naming the sections. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 229 sections, no revision-date movement</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> General Medicine manual, ~229 sections - E&amp;M, telehealth, preventive services and other chargemaster-relevant policy.</li>
<li><b>Registry rows to verify on change:</b> professional-services billing rows on related section changes</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> rev_inpatient_manuals - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services">Open the source</a> - checked 2026-08-10</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services</a></li>
<li><b>How:</b> The portal's manual list for this community is queried for metadata only - no PDFs are downloaded. Each section's Revision Date is compared with the previous check; movement produces a lower-priority revision notice naming the sections. Checked by the weekly script run (Mondays 14:00 UTC, GitHub Actions).</li>
<li><b>This run:</b> unchanged - 115 sections, no revision-date movement</li>
<li><b>Last checked:</b> 2026-08-10</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Inpatient Services manual, ~115 sections. Date-only signal for inpatient billing / revenue integrity awareness.</li>
<li><b>Registry rows to verify on change:</b> inpatient billing rows on related section changes</li>
</ul>
</details>

### Source URLs at a glance

One row per watched URL, **colored by website** so sources from the same site are easy to spot together.

<ul style="list-style:none;padding-left:0;font-size:.85em;line-height:1.7">
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--00letter - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--0bhwtouse - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--1tocfpact - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--benclinic - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--benfam - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--benfamrel - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--bengrid - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--claimcms - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--claimub - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--clientelig - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--clinic - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--drug - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--drugonsite - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--fam - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--hapid - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--lab - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--office - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--pharm - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--pharmacy - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--progstand - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--provenrollres - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--provrel - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--radif - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0</a></li>
<li style="color:#5b2d86;font-weight:600">fpact_manual_docs--tarf - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705</a></li>
<li style="color:#14632e;font-weight:600">fpact_news_archive - <a href="https://familypact.org/news-and-updates-archive/" style="color:#14632e">https://familypact.org/news-and-updates-archive/</a></li>
<li style="color:#8b1a1a;font-weight:600">fqhc_cms_center - <a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center" style="color:#8b1a1a">https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center</a></li>
<li style="color:#1f4e79;font-weight:600">fqhc_dhcs_3097_page - <a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/" style="color:#1f4e79">https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/</a></li>
<li style="color:#5b2d86;font-weight:600">fqhc_rural_manual_docs--rural - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C983B7D9-42B3-4543-BF93-D272AB764BDD" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C983B7D9-42B3-4543-BF93-D272AB764BDD</a></li>
<li style="color:#5b2d86;font-weight:600">fqhc_rural_manual_docs--ruralcd - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/2D80A3B6-A32B-4131-BE63-12EE7243A849" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/2D80A3B6-A32B-4131-BE63-12EE7243A849</a></li>
<li style="color:#5b2d86;font-weight:600">fqhc_rural_manual_docs--ruralex - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/08EC7DD1-AABE-4187-9D9E-F155C3DAF1CA" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/08EC7DD1-AABE-4187-9D9E-F155C3DAF1CA</a></li>
<li style="color:#5b2d86;font-weight:600">fqhc_rural_manual_docs--ruralhosp - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/3E8C0259-6D59-4F20-BFA3-E5AE5754F39D" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/3E8C0259-6D59-4F20-BFA3-E5AE5754F39D</a></li>
<li style="color:#1f4e79;font-weight:600">mcp_apl_index - <a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx" style="color:#1f4e79">https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx</a></li>
<li style="color:#1f4e79;font-weight:600">mcp_boilerplate_contract - <a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf" style="color:#1f4e79">https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf</a></li>
<li style="color:#1f4e79;font-weight:600">mcp_tri_faq - <a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf" style="color:#1f4e79">https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf</a></li>
<li style="color:#1f4e79;font-weight:600">ffs_sb94_fp_fee_schedule - <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx" style="color:#1f4e79">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx</a></li>
<li style="color:#1f4e79;font-weight:600">ffs_tri_fee_schedule - <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx" style="color:#1f4e79">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx</a></li>
<li style="color:#8b1a1a;font-weight:600">ncci_medicaid_files - <a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files" style="color:#8b1a1a">https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files</a></li>
<li style="color:#5b2d86;font-weight:600">rev_clinics_hospitals_manuals - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals</a></li>
<li style="color:#5b2d86;font-weight:600">rev_general_medicine_manuals - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine</a></li>
<li style="color:#5b2d86;font-weight:600">rev_inpatient_manuals - <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services" style="color:#5b2d86">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services</a></li>
</ul>

<div style="height:1.6em"></div>

## Status legend

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<table style="font-size:.85em;line-height:1.45">
<tr><th>Status</th><th>Code</th><th>What it means, and what to do</th></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>CHANGED</code></td><td>The extracted text of this source differs from the last run. <i>Open the diff to see the exact lines, re-read that part of the live source, then verify the listed registry rows (superbill, tipsheet, Epic review as applicable).</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>NEW</code></td><td>First run for this source; its current state became the baseline. <i>Skim the source once to confirm it is the right document.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>DATE_CHANGED</code></td><td>A revision or &#x27;page updated&#x27; stamp moved but the content text did not. <i>Open the source and confirm nothing substantive changed; usually a republish.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>LINKS_CHANGED</code></td><td>The set of files this page links to changed (often a re-versioned filename, e.g. a new Superbill). <i>Open the page, check each added or removed file listed with the item, and if a watched file was re-versioned, point watchlist.yaml at the new URL so the script keeps monitoring it.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>NEW_ISSUE</code></td><td>A probed bulletin issue number returned real content. <i>Read the new bulletin and triage anything affecting the registry.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>REMOVED</code></td><td>A document disappeared from the portal&#x27;s list. <i>Check the portal: retired, renamed, or moved? Update the registry reference if the section is gone.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>URL_CHANGED_IN_CONFIG</code></td><td>The URL in watchlist.yaml differs from the URL the baseline was built from. <i>Confirm the new URL is intentional; the next run with --update re-baselines it.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>CHANGED_METADATA_ONLY</code></td><td>The portal says this section was revised (new revision date or file id) but the PDF itself could not be downloaded, so there is no text diff. <i>Open the section on the portal, re-read it, and verify the listed registry rows.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>LIST_TRUNCATED</code></td><td>The portal returned fewer documents than its own count claims. <i>Open the portal list and compare; some sections may be silently unmonitored until this clears.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span></td><td><code>REVISION_NOTICE</code></td><td>The Medi-Cal portal moved the Revision Date on one or more manual sections in this community. Date-only signal - the section text is not monitored here, so there is no diff. <i>When time allows, open the community&#x27;s manual page, skim the sections named in the notice, and route anything touching billing codes or the chargemaster.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>UNREACHABLE</code></td><td>The fetch failed this run (HTTP error, network error, robots.txt, or an off-site redirect) - the Why line says which. <i>If it persists more than one run, open the URL in a browser; the page may have moved. Then fix watchlist.yaml. Until then this source is unmonitored.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>MANUAL_REVIEW</code></td><td>This source cannot be fetched automatically, by design (reason in the fine print). <i>Open the link by hand on the cadence given in the fine print; MCSS email is the push detector.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>BLIND_SHELL</code></td><td>The page builds its content with JavaScript, so the checker sees only an empty app shell and cannot detect content changes. <i>Do not rely on this row for detection; MCSS email covers it. Open the page yourself when in doubt.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>PROBE_INCONCLUSIVE</code></td><td>The bulletin probe could not confirm or rule out a new issue (client-rendered portal). <i>Nothing to do; MCSS email is the reliable detector for bulletins.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>CONFIG_TODO</code></td><td>The watchlist entry is incomplete, so nothing is monitored for it yet. <i>Finish the entry in watchlist.yaml; the Why line says what is missing.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span></td><td><code>unchanged</code></td><td>No change detected. <i>Nothing to do.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span></td><td><code>metadata_only_unchanged</code></td><td>The PDF is not directly downloadable, but the portal&#x27;s revision metadata is unchanged. <i>Nothing to do.</i></td></tr>
</table>

---

**Keeping it working:** if the date of the last check at the top of this page is more than 35 days old, the script may not be running - notify the maintainer. Sources move: when an agency changes a URL, retires a page or reorganizes a portal, the watchlist entry has to be updated before that source is monitored again, so treat a source that has been unreachable for more than one check as unwatched until it is fixed.

This page is rebuilt by each script run (`write_dashboard` in [source_check.py](https://github.com/mp321/RevInt-SourceWatch/blob/main/source_check.py)); edit that, not this file.

Provided as-is, without warranty of any kind, as general decision support. It is not legal, coding or billing advice and is not a source of record - the live official source always governs. Built and maintained by [Michael Phipps](https://github.com/mp321); released under the MIT license ([LICENSE](https://github.com/mp321/RevInt-SourceWatch/blob/main/LICENSE)). If you reuse or adapt it, a credit link back to the [repository](https://github.com/mp321/RevInt-SourceWatch) is appreciated.
