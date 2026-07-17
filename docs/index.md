# Revenue Integrity Source Watch

Automated monitor for the official billing sources behind the
Revenue Integrity registry. **Alert tool only, not a source of
record.** Verify every flagged item against the live official source
before acting on it.

Each week an automated run fetches every source listed below, compares it against the copy from the previous run, and flags anything that changed, disappeared, or could not be checked. A flag here does not mean the Master sheet is wrong - it means a human should re-read that source and confirm whether anything downstream needs to change. For source definitions, run history, and the full codebase, see the [GitHub repository](https://github.com/mp321/RevInt-SourceWatch).

**Last run:** 2026-07-16T22:04:20+00:00 - **Needs review: 3**

Where to click: [change review page](https://mp321.github.io/RevInt-SourceWatch/changes.html) · [change log (CSV)](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/changes_log.csv) · [reports folder](https://github.com/mp321/RevInt-SourceWatch/tree/main/reports) (diff reports land in `reports/diffs/`) · [latest raw report (JSON)](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/latest_report.json) · [watchlist definition](https://github.com/mp321/RevInt-SourceWatch/blob/main/watchlist.yaml)

Statuses like `CHANGED` or `BLIND_SHELL` are explained in the [status legend](#status-legend) at the bottom of this page.

## Needs review since last run (3)

Work this list top to bottom; every item links straight to the source and, when text changed, to the exact diff.

- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - [fqhc_cms_center](https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center) _(FQHC)_
  - **What happened:** content text hash differs
  - **What to do:** Open the diff to see the exact lines, re-read that part of the live source, then verify the listed Master rows (superbill, tipsheet, Epic review as applicable).
  - **Exact change:** no diff was written this run (no prior text snapshot to compare against) - compare the live source with your last known state.
  - **Master rows to verify:** none mapped in the watchlist; triage by judgment.
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - [mcp_apl_index](https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx) _(Managed Medi-Cal)_
  - **What happened:** content text hash differs
  - **What to do:** Open the diff to see the exact lines, re-read that part of the live source, then verify the listed Master rows (superbill, tipsheet, Epic review as applicable).
  - **Exact change:** no diff was written this run (no prior text snapshot to compare against) - compare the live source with your last known state.
  - **Master rows to verify:** none mapped in the watchlist; triage by judgment.
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - [ncci_medicaid_files](https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files) _(NCCI)_
  - **What happened:** content text hash differs
  - **What to do:** Open the diff to see the exact lines, re-read that part of the live source, then verify the listed Master rows (superbill, tipsheet, Epic review as applicable).
  - **Exact change:** no diff was written this run (no prior text snapshot to compare against) - compare the live source with your last known state.
  - **Master rows to verify:** none mapped in the watchlist; triage by judgment.

### Could not be checked automatically (1)

Monitoring gaps, not confirmed source changes - these sources are effectively unwatched until fixed. (Permanently manual or blind entries - MANUAL_REVIEW, BLIND_SHELL, PROBE_INCONCLUSIVE - are by design and listed in their program sections with the reason in the fine print.)

- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> `CONFIG_TODO` - `fpact_manual_docs` _(Family PACT)_
  - **Why:** manual_list url is empty - paste the portal JSON endpoint (README: one-time DevTools step)
  - **What to do:** Finish the entry in watchlist.yaml; the Why line says what is missing.

## All sources by program

Programs on this page (every watched source, including the quiet ones):

- [Family PACT](#family-pact-fpact) - 5 sources
- [FQHC](#fqhc-fqhc) - 5 sources, 1 needs review
- [Managed Medi-Cal](#managed-medi-cal-managed-medi-cal) - 3 sources, 1 needs review
- [Medi-Cal FFS](#medi-cal-ffs-medi-cal-ffs) - 3 sources
- [NCCI](#ncci-ncci) - 1 source, 1 needs review

Each block: the status line first, then (indented) the source link and a Details fold-out with exactly what is checked and its caveats.

### Family PACT (`fpact`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> fpact_bulletin_probe - `PROBE_INCONCLUSIVE`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/bulletin?community=family-pact&amp;issueNumber={issue}">Open the source</a> - checked 2026-07-16</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> #224:shell(0ch); #225:shell(0ch); #226:shell(0ch) - portal is client-rendered; MCSS email is the reliable detector</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/bulletin?community=family-pact&amp;issueNumber={issue}">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/bulletin?community=family-pact&amp;issueNumber={issue}</a> (template; {issue} is the probed issue number)</li>
<li><b>How:</b> The checker requests the next few issue numbers of the bulletin URL to see whether a new issue returns real content. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> PROBE_INCONCLUSIVE - #224:shell(0ch); #225:shell(0ch); #226:shell(0ch) - portal is client-rendered; MCSS email is the reliable detector</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Best-effort probe; portal is client-rendered so expect PROBE_INCONCLUSIVE - MCSS email is the reliable detector.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> fpact_manual_docs - `CONFIG_TODO`

<p style="margin:.2em 0 .2em 2em">checked 2026-07-16</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> manual_list url is empty - paste the portal JSON endpoint (README: one-time DevTools step)</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> none configured yet.</li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> CONFIG_TODO - manual_list url is empty - paste the portal JSON endpoint (README: one-time DevTools step)</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the page that shows a Revision Date per section). Paste the JSON endpoint the page loads its list from (README, one-time DevTools step). Every PDF found is then watched individually - content hash, portal Revision Date, new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. Until the url is set, this reports CONFIG_TODO and MCSS remains the detector.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_news_archive - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://familypact.org/news-and-updates-archive/">Open the source</a> - checked 2026-07-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://familypact.org/news-and-updates-archive/">https://familypact.org/news-and-updates-archive/</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Program news archive; new post or PDF links = policy updates to read. Pattern excludes feed/json noise.</li>
<li><b>Master rows to verify on change:</b> triage per announcement</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> fpact_ppbi_landing - `MANUAL_REVIEW`

<p style="margin:.2em 0 .2em 2em"><a href="https://familypact.org/providers/policies-procedures-and-billing-instructions/">Open the source</a> - not fetched automatically</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> Redirects off-site to the legacy files.medi-cal.ca.gov manual-query page, which timed out on 2026-07-02; current PPBI sections live on the client-rendered mcweb portal. Detection is MCSS + fpact_news_archive; open the PPBI manually when flagged.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://familypact.org/providers/policies-procedures-and-billing-instructions/">https://familypact.org/providers/policies-procedures-and-billing-instructions/</a></li>
<li><b>How:</b> Not fetched automatically. The weekly run lists it every time as a standing reminder.</li>
<li><b>Why it cannot be auto-checked:</b> Redirects off-site to the legacy files.medi-cal.ca.gov manual-query page, which timed out on 2026-07-02; current PPBI sections live on the client-rendered mcweb portal. Detection is MCSS + fpact_news_archive; open the PPBI manually when flagged.</li>
<li><b>What to do instead:</b> Open it yourself: <a href="https://familypact.org/providers/policies-procedures-and-billing-instructions/">https://familypact.org/providers/policies-procedures-and-billing-instructions/</a>. Follow the cadence in the reason above; if none is stated, re-read it when program news suggests a change.</li>
<li><b>Last checked:</b> never fetched automatically</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> fpact_wic_24005 - `MANUAL_REVIEW`

<p style="margin:.2em 0 .2em 2em"><a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=24005.&amp;lawCode=WIC">Open the source</a> - not fetched automatically</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> leginfo robots.txt disallows automated fetch - review quarterly by hand. Statute changes arrive via bills, so MCSS and program news normally give advance notice.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=24005.&amp;lawCode=WIC">https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=24005.&amp;lawCode=WIC</a></li>
<li><b>How:</b> Not fetched automatically. The weekly run lists it every time as a standing reminder.</li>
<li><b>Why it cannot be auto-checked:</b> leginfo robots.txt disallows automated fetch - review quarterly by hand. Statute changes arrive via bills, so MCSS and program news normally give advance notice.</li>
<li><b>What to do instead:</b> Open it yourself: <a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=24005.&amp;lawCode=WIC">https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=24005.&amp;lawCode=WIC</a>. Follow the cadence in the reason above; if none is stated, re-read it when program news suggests a change.</li>
<li><b>Last checked:</b> never fetched automatically</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Master rows to verify on change:</b> eligibility / payer-of-last-resort denial rows</li>
</ul>
</details>

### FQHC (`fqhc`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> fqhc_cms_center - `CHANGED`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center">Open the source</a> - checked 2026-07-16</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> content text hash differs</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center">https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> CHANGED - content text hash differs</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> 2026-07-16 (CHANGED)</li>
<li><b>Watchlist note:</b> G2025 rate, care-management code set, telehealth expiries.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_dhcs_3097_page - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/">Open the source</a> - checked 2026-07-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/">https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Wrap reconciliation forms and due-date extensions.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> fqhc_ecfr_405_subpart_x - `MANUAL_REVIEW`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-X">Open the source</a> - not fetched automatically</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> eCFR bot wall redirects automated fetches off-host. eCFR publishes an official public API for exactly this use (see ecfr.gov developer documentation) - switching this entry to the API endpoint for Title 42 Part 405 is the planned fix; until then review by hand when CMS guidance changes.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-X">https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-X</a></li>
<li><b>How:</b> Not fetched automatically. The weekly run lists it every time as a standing reminder.</li>
<li><b>Why it cannot be auto-checked:</b> eCFR bot wall redirects automated fetches off-host. eCFR publishes an official public API for exactly this use (see ecfr.gov developer documentation) - switching this entry to the API endpoint for Title 42 Part 405 is the planned fix; until then review by hand when CMS guidance changes.</li>
<li><b>What to do instead:</b> Open it yourself: <a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-X">https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-X</a>. Follow the cadence in the reason above; if none is stated, re-read it when program news suggests a change.</li>
<li><b>Last checked:</b> never fetched automatically</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_manual_page_mcweb - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural">Open the source</a> - checked 2026-07-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Blind spot:</b> This page is client-rendered - the checker sees only the app shell and cannot detect content changes. Detection relies on the MCSS email subscription; open the page yourself when in doubt: <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural</a></li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> fqhc_wic_14132_100 - `MANUAL_REVIEW`

<p style="margin:.2em 0 .2em 2em"><a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14132.100.&amp;lawCode=WIC">Open the source</a> - not fetched automatically</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> leginfo robots.txt disallows automated fetch. ACTION - AB 116 amendment took effect 2026-07-01; manually verify the amended provider list and update the fqhc-billing reference.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14132.100.&amp;lawCode=WIC">https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14132.100.&amp;lawCode=WIC</a></li>
<li><b>How:</b> Not fetched automatically. The weekly run lists it every time as a standing reminder.</li>
<li><b>Why it cannot be auto-checked:</b> leginfo robots.txt disallows automated fetch. ACTION - AB 116 amendment took effect 2026-07-01; manually verify the amended provider list and update the fqhc-billing reference.</li>
<li><b>What to do instead:</b> Open it yourself: <a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14132.100.&amp;lawCode=WIC">https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14132.100.&amp;lawCode=WIC</a>. Follow the cadence in the reason above; if none is stated, re-read it when program news suggests a change.</li>
<li><b>Last checked:</b> never fetched automatically</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Master rows to verify on change:</b> PPS-billable provider list in fqhc-billing reference</li>
</ul>
</details>

### Managed Medi-Cal (`managed_medi_cal`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> mcp_apl_index - `CHANGED`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">Open the source</a> - checked 2026-07-16</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> content text hash differs</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> CHANGED - content text hash differs</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> 2026-07-16 (CHANGED)</li>
<li><b>Watchlist note:</b> First run matched zero links with the APL-specific pattern - broadened to all PDFs; text hash still covers page changes. If the link list stays empty, capture the real APL listing URL from the browser and repoint.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_boilerplate_contract - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf">Open the source</a> - checked 2026-07-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf">https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf</a></li>
<li><b>How:</b> The PDF is downloaded (conditional GET - the server may answer '304 not modified' and skip the download), its text is extracted and hashed, and the hash is compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_tri_faq - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf">Open the source</a> - checked 2026-07-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf">https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf</a></li>
<li><b>How:</b> The PDF is downloaded (conditional GET - the server may answer '304 not modified' and skip the download), its text is extracted and hashed, and the hash is compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

### Medi-Cal FFS (`medi_cal_ffs`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ffs_sb94_fp_fee_schedule - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx">Open the source</a> (clicking downloads an Excel file) - checked 2026-07-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx</a> (clicking downloads an Excel file)</li>
<li><b>How:</b> The raw file bytes are hashed and compared; no text is extracted, so this entry can never produce a text diff. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> SB 94 family-planning augmented fee schedule (supersedes TRI for FP codes with Z30.x). Discovered on the TRI page, first run.</li>
<li><b>Master rows to verify on change:</b> FPACT rows priced on the SB 94 schedule</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ffs_tri_page - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">Open the source</a> - checked 2026-07-16</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> TRI landing; link-set diff catches re-versioned fee schedule filenames and new APL redlines.</li>
<li><b>Master rows to verify on change:</b> reimbursement_basis rows citing TRI / SB 94</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> ffs_wic_14105_201 - `MANUAL_REVIEW`

<p style="margin:.2em 0 .2em 2em"><a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14105.201.&amp;lawCode=WIC">Open the source</a> - not fetched automatically</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> leginfo robots.txt disallows automated fetch - review quarterly by hand.</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14105.201.&amp;lawCode=WIC">https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14105.201.&amp;lawCode=WIC</a></li>
<li><b>How:</b> Not fetched automatically. The weekly run lists it every time as a standing reminder.</li>
<li><b>Why it cannot be auto-checked:</b> leginfo robots.txt disallows automated fetch - review quarterly by hand.</li>
<li><b>What to do instead:</b> Open it yourself: <a href="https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14105.201.&amp;lawCode=WIC">https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14105.201.&amp;lawCode=WIC</a>. Follow the cadence in the reason above; if none is stated, re-read it when program news suggests a change.</li>
<li><b>Last checked:</b> never fetched automatically</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

### NCCI (`ncci`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> ncci_medicaid_files - `CHANGED`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files">Open the source</a> - checked 2026-07-16</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> content text hash differs</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files">https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> CHANGED - content text hash differs</li>
<li><b>Last checked:</b> 2026-07-16</li>
<li><b>Last recorded change:</b> 2026-07-16 (CHANGED)</li>
<li><b>Watchlist note:</b> Quarterly PTP/MUE file drops appear as new links (first run captured the 2026 Q3 set effective 07/01/2026).</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

### Source URLs at a glance

Plain list of every URL this page's data comes from.

```text
fpact_bulletin_probe: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/bulletin?community=family-pact&issueNumber={issue}
fpact_news_archive: https://familypact.org/news-and-updates-archive/
fpact_ppbi_landing: https://familypact.org/providers/policies-procedures-and-billing-instructions/
fpact_wic_24005: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=24005.&lawCode=WIC
fqhc_cms_center: https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center
fqhc_dhcs_3097_page: https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/
fqhc_ecfr_405_subpart_x: https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-B/part-405/subpart-X
fqhc_manual_page_mcweb: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural
fqhc_wic_14132_100: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14132.100.&lawCode=WIC
mcp_apl_index: https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx
mcp_boilerplate_contract: https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf
mcp_tri_faq: https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf
ffs_sb94_fp_fee_schedule: https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx
ffs_tri_page: https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/
ffs_wic_14105_201: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=14105.201.&lawCode=WIC
ncci_medicaid_files: https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files
```

## Status legend

<table style="font-size:.85em;line-height:1.45">
<tr><th>Status</th><th>Code</th><th>What it means, and what to do</th></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>CHANGED</code></td><td>The extracted text of this source differs from the last run. <i>Open the diff to see the exact lines, re-read that part of the live source, then verify the listed Master rows (superbill, tipsheet, Epic review as applicable).</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>NEW</code></td><td>First run for this source; its current state became the baseline. <i>Skim the source once to confirm it is the right document.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>DATE_CHANGED</code></td><td>A revision or &#x27;page updated&#x27; stamp moved but the content text did not. <i>Open the source and confirm nothing substantive changed; usually a republish.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>LINKS_CHANGED</code></td><td>The set of files this page links to changed (often a re-versioned filename, e.g. a new Superbill). <i>Open the page, find the added or removed file named in Why, and if a watched file was re-versioned, point watchlist.yaml at the new URL.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>NEW_ISSUE</code></td><td>A probed bulletin issue number returned real content. <i>Read the new bulletin and triage anything affecting the Master sheet.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>REMOVED</code></td><td>A document disappeared from the portal&#x27;s list. <i>Check the portal: retired, renamed, or moved? Update the Master sheet reference if the section is gone.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>URL_CHANGED_IN_CONFIG</code></td><td>The URL in watchlist.yaml differs from the URL the baseline was built from. <i>Confirm the new URL is intentional; the next run with --update re-baselines it.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>CHANGED_METADATA_ONLY</code></td><td>The portal says this section was revised (new revision date or file id) but the PDF itself could not be downloaded, so there is no text diff. <i>Open the section on the portal, re-read it, and verify the listed Master rows.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span></td><td><code>LIST_TRUNCATED</code></td><td>The portal returned fewer documents than its own count claims. <i>Open the portal list and compare; some sections may be silently unmonitored until this clears.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>UNREACHABLE</code></td><td>The fetch failed this run (HTTP error, network error, robots.txt, or an off-site redirect) - the Why line says which. <i>If it persists more than one run, open the URL in a browser; the page may have moved. Then fix watchlist.yaml. Until then this source is unmonitored.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>MANUAL_REVIEW</code></td><td>This source cannot be fetched automatically, by design (reason in the fine print). <i>Open the link by hand on the cadence given in the fine print; MCSS email is the push detector.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>BLIND_SHELL</code></td><td>The page builds its content with JavaScript, so the checker sees only an empty app shell and cannot detect content changes. <i>Do not rely on this row for detection; MCSS email covers it. Open the page yourself when in doubt.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>PROBE_INCONCLUSIVE</code></td><td>The bulletin probe could not confirm or rule out a new issue (client-rendered portal). <i>Nothing to do; MCSS email is the reliable detector for bulletins.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span></td><td><code>CONFIG_TODO</code></td><td>The watchlist entry is incomplete, so nothing is monitored for it yet. <i>Finish the entry in watchlist.yaml; the Why line says what is missing.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span></td><td><code>unchanged</code></td><td>No change detected. <i>Nothing to do.</i></td></tr>
<tr><td><span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span></td><td><code>metadata_only_unchanged</code></td><td>The PDF is not directly downloadable, but the portal&#x27;s revision metadata is unchanged. <i>Nothing to do.</i></td></tr>
</table>

---

If the last run shown at the top of this page is more than 35 days old, this monitor may not be active or may need an update - notify the maintainer.

This page is regenerated on every run by `write_dashboard` in [source_check.py](https://github.com/mp321/RevInt-SourceWatch/blob/main/source_check.py); edit that, not this file. Alert tool only - verify against the live official source.

Built and maintained by [Michael Phipps](https://github.com/mp321). See the [repository](https://github.com/mp321/RevInt-SourceWatch) for source, history, and license terms.
