# Revenue Integrity Source Watch

Automated monitor for the official billing sources behind the
Revenue Integrity registry. **Alert tool only, not a source of
record.** Verify every flagged item against the live official source
before acting on it.

Each week an automated run fetches every source listed below, compares it against the copy from the previous run, and flags anything that changed, disappeared, or could not be checked. A flag here does not mean the Master sheet is wrong - it means a human should re-read that source and confirm whether anything downstream needs to change. For source definitions, run history, and the full codebase, see the [GitHub repository](https://github.com/mp321/RevInt-SourceWatch).

**Last run:** 2026-07-17T19:52:00+00:00 - **Needs review: 3**

Where to click: [change review page](https://mp321.github.io/RevInt-SourceWatch/changes.html) · [change log (CSV)](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/changes_log.csv) · [reports folder](https://github.com/mp321/RevInt-SourceWatch/tree/main/reports) (diff reports land in `reports/diffs/`) · [latest raw report (JSON)](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/latest_report.json) · [watchlist definition](https://github.com/mp321/RevInt-SourceWatch/blob/main/watchlist.yaml)

Statuses like `CHANGED` or `BLIND_SHELL` are explained in the [status legend](#status-legend) at the bottom of this page.

## Needs review since last run (3)

Work this list top to bottom; every item links straight to the source and, when text changed, to the exact diff.

- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `LINKS_CHANGED` - [fpact_news_archive](https://familypact.org/news-and-updates-archive/) _(Family PACT)_
  - **What happened:** +1 ['https://familypact.org/family-pact-policy-updates-and-clarifications/'] / -1 ['https://familypact.org/rate-updates-for-select-fpact-hcpcs-codes/']
  - **What to do:** Open the page, find the added or removed file named in Why, and if a watched file was re-versioned, point watchlist.yaml at the new URL.
  - **Master rows to verify:** triage per announcement
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `LINKS_CHANGED` - [mcp_apl_index](https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx) _(Managed Medi-Cal)_
  - **What happened:** +0 [] / -2 ['/wp-content/uploads/2025/10/Web-Accessibility-Cert.pdf', 'https://www.dhcs.ca.gov/wp-content/uploads/2025/10/MOU-FAQs.pdf']
  - **What to do:** Open the page, find the added or removed file named in Why, and if a watched file was re-versioned, point watchlist.yaml at the new URL.
  - **Master rows to verify:** none mapped in the watchlist; triage by judgment.
- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `LINKS_CHANGED` - [ffs_tri_page](https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/) _(Medi-Cal FFS)_
  - **What happened:** +0 [] / -3 ['/wp-content/uploads/2025/10/Web-Accessibility-Cert.pdf', 'https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx', 'https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx']
  - **What to do:** Open the page, find the added or removed file named in Why, and if a watched file was re-versioned, point watchlist.yaml at the new URL.
  - **Master rows to verify:** reimbursement_basis rows citing TRI / SB 94

### Could not be checked automatically (1)

Monitoring gaps, not confirmed source changes - these sources are effectively unwatched until fixed. (Permanently manual or blind entries - MANUAL_REVIEW, BLIND_SHELL, PROBE_INCONCLUSIVE - are by design and listed in their program sections with the reason in the fine print.)

- <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> `UNREACHABLE` - [mcp_tri_faq](https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf) _(Managed Medi-Cal)_
  - **Why:** expected a PDF but the server returned an HTML page - the document may have moved or sit behind a bot check; the previous baseline is kept
  - **What to do:** If it persists more than one run, open the URL in a browser; the page may have moved. Then fix watchlist.yaml. Until then this source is unmonitored.

## All sources by program

Programs on this page (every watched source, including the quiet ones):

- [Family PACT](#family-pact-fpact) - 28 sources, 1 needs review
- [FQHC](#fqhc-fqhc) - 5 sources
- [Managed Medi-Cal](#managed-medi-cal-managed_medi_cal) - 3 sources, 1 needs review
- [Medi-Cal FFS](#medi-cal-ffs-medi_cal_ffs) - 3 sources, 1 needs review
- [NCCI](#ncci-ncci) - 1 source

Each block: the status line first, then (indented) the source link and a Details fold-out with exactly what is checked and its caveats.

### Family PACT (`fpact`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> fpact_bulletin_probe - `PROBE_INCONCLUSIVE`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/bulletin?community=family-pact&amp;issueNumber={issue}">Open the source</a> - checked 2026-07-17</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> #224:shell(0ch); #225:shell(0ch); #226:shell(0ch) - portal is client-rendered; MCSS email is the reliable detector</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/bulletin?community=family-pact&amp;issueNumber={issue}">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/bulletin?community=family-pact&amp;issueNumber={issue}</a> (template; {issue} is the probed issue number)</li>
<li><b>How:</b> The checker requests the next few issue numbers of the bulletin URL to see whether a new issue returns real content. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> PROBE_INCONCLUSIVE - #224:shell(0ch); #225:shell(0ch); #226:shell(0ch) - portal is client-rendered; MCSS email is the reliable detector</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Best-effort probe; portal is client-rendered so expect PROBE_INCONCLUSIVE - MCSS email is the reliable detector.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--00letter - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B">Open the source</a> - revision 2025-05-23T00:02:23 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--0bhwtouse - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A">Open the source</a> - revision 2025-06-16T16:12:25 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--1tocfpact - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71">Open the source</a> - revision 2025-05-23T00:02:48 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--benclinic - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43">Open the source</a> - revision 2025-11-21T18:51:48 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--benfam - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED">Open the source</a> - revision 2026-05-15T16:52:05 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--benfamrel - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8">Open the source</a> - revision 2026-05-15T16:52:25 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--bengrid - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683">Open the source</a> - revision 2026-05-18T17:42:58 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--claimcms - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D">Open the source</a> - revision 2025-10-16T16:11:54 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--claimub - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F">Open the source</a> - revision 2025-10-16T16:12:21 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--clientelig - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A">Open the source</a> - revision 2026-04-16T16:43:52 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--clinic - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10">Open the source</a> - revision 2026-05-15T16:53:48 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--drug - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5">Open the source</a> - revision 2026-03-16T16:27:32 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--drugonsite - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC">Open the source</a> - revision 2026-06-16T15:30:42 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--fam - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528">Open the source</a> - revision 2025-01-16T17:32:57 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--hapid - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326">Open the source</a> - revision 2025-06-16T16:11:43 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--lab - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B">Open the source</a> - revision 2026-01-20T17:54:24 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--office - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F">Open the source</a> - revision 2024-07-16T16:09:38 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--pharm - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00">Open the source</a> - revision 2023-08-06T02:00:31 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--pharmacy - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F">Open the source</a> - revision 2025-10-16T16:12:48 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--progstand - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904">Open the source</a> - revision 2026-07-16T16:28:52 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--provenrollres - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29">Open the source</a> - revision 2026-07-16T16:29:22 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--provrel - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643">Open the source</a> - revision 2025-02-14T17:38:10 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--radif - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0">Open the source</a> - revision 2023-08-06T02:02:15 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fpact_manual_docs--tarf - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705">Open the source</a> - revision 2023-08-21T21:13:15 - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705</a></li>
<li><b>How:</b> The portal's JSON list endpoint is queried; every document it lists is watched individually (PDF text hash plus the portal's revision date). New documents are auto-discovered and removals are flagged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - seed baseline hash established</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Per-document monitor for the entire Family PACT manual list (the portal page that shows a Revision Date per section), all 24 sections. Backed by the undocumented mcweb Directus GraphQL endpoint (POST /graphql, CommunityManuals, communityId 25). Each section is watched individually - full PDF text hash (assets are readable with the same token, verified 2026-07-16), per-page &quot;Page updated&quot; stamps, portal Revision Date (file.modified_on, compared as a raw string), new docs auto-discovered, removals flagged - and CHANGED sections get a before/after text diff in reports/diffs/. If the token ever grants the list but not the assets, the entry degrades to CHANGED_METADATA_ONLY (revision-date + file.id churn, no text diff) instead of going blind. This is an undocumented internal endpoint that can change shape or auth without notice; MCSS email remains the backstop detector and must not be retired on the strength of this integration. Decision support, not a source of record.</li>
<li><b>Master rows to verify on change:</b> ppbi_source_section rows for any changed section</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> fpact_news_archive - `LINKS_CHANGED`

<p style="margin:.2em 0 .2em 2em"><a href="https://familypact.org/news-and-updates-archive/">Open the source</a> - checked 2026-07-17</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> +1 [&#x27;https://familypact.org/family-pact-policy-updates-and-clarifications/&#x27;] / -1 [&#x27;https://familypact.org/rate-updates-for-select-fpact-hcpcs-codes/&#x27;]</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://familypact.org/news-and-updates-archive/">https://familypact.org/news-and-updates-archive/</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> LINKS_CHANGED - +1 [&#x27;https://familypact.org/family-pact-policy-updates-and-clarifications/&#x27;] / -1 [&#x27;https://familypact.org/rate-updates-for-select-fpact-hcpcs-codes/&#x27;]</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> 2026-07-17 (LINKS_CHANGED)</li>
<li><b>Watchlist note:</b> Program news archive; new post or PDF links = policy updates to read. Pattern excludes feed/json noise. Also catches re-versioned artifacts (e.g. a new Superbill filename).</li>
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

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_cms_center - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center">Open the source</a> - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center">https://www.cms.gov/medicare/payment/prospective-payment-systems/federally-qualified-health-centers-fqhc-center</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> 2026-07-16 (CHANGED)</li>
<li><b>Watchlist note:</b> G2025 rate, care-management code set, telehealth expiries.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> fqhc_dhcs_3097_page - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/">Open the source</a> - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/">https://www.dhcs.ca.gov/forms-laws-publications/forms/cost-report-forms-and-documents/</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-07-17</li>
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

<p style="margin:.2em 0 .2em 2em"><a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural">Open the source</a> - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural</a></li>
<li><b>How:</b> The page is downloaded (conditional GET), scripts and styles are stripped, and the visible text is hashed and compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Blind spot:</b> This page is client-rendered - the checker sees only the app shell and cannot detect content changes. Detection relies on the MCSS email subscription; open the page yourself when in doubt: <a href="https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural">https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=rural</a></li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Blind Angular shell today. Planned conversion - a second manual_list GraphQL entry like fpact_manual_docs (community=rural; communityId to capture from DevTools, see notes/CONTEXT-mcweb.md).</li>
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

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> mcp_apl_index - `LINKS_CHANGED`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">Open the source</a> - checked 2026-07-17</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> +0 [] / -2 [&#x27;/wp-content/uploads/2025/10/Web-Accessibility-Cert.pdf&#x27;, &#x27;https://www.dhcs.ca.gov/wp-content/uploads/2025/10/MOU-FAQs.pdf&#x27;]</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> LINKS_CHANGED - +0 [] / -2 [&#x27;/wp-content/uploads/2025/10/Web-Accessibility-Cert.pdf&#x27;, &#x27;https://www.dhcs.ca.gov/wp-content/uploads/2025/10/MOU-FAQs.pdf&#x27;]</li>
<li><b>Blind spot:</b> This page is client-rendered - the checker sees only the app shell and cannot detect content changes. Detection relies on the MCSS email subscription; open the page yourself when in doubt: <a href="https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx">https://www.dhcs.ca.gov/formsandpubs/Pages/AllPlanLetters.aspx</a></li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> 2026-07-17 (LINKS_CHANGED)</li>
<li><b>Watchlist note:</b> Kept provisionally (2026-07-17 review). First run matched zero links with the APL-specific pattern - broadened to all PDFs; text hash still covers page changes. If the link list stays empty, capture the real APL listing URL from the browser and repoint.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> mcp_boilerplate_contract - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf">Open the source</a> - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf">https://www.dhcs.ca.gov/hi/wp-content/uploads/2025/10/2024-Managed-Care-Boilerplate-Contract.pdf</a></li>
<li><b>How:</b> The PDF is downloaded (conditional GET - the server may answer '304 not modified' and skip the download), its text is extracted and hashed, and the hash is compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Hard-dated versioned filename (2025/10 upload path) - a revision likely ships under a new URL, which this entry alone cannot see. Treat as a point-in-time watch.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#fff6e0;color:#7a4a00;white-space:nowrap">Can't verify</span> mcp_tri_faq - `UNREACHABLE`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf">Open the source</a> - checked 2026-07-17</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> expected a PDF but the server returned an HTML page - the document may have moved or sit behind a bot check; the previous baseline is kept</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf">https://www.dhcs.ca.gov/services/Documents/DirectedPymts/CY-2024-TRI-FAQ-20250312.pdf</a></li>
<li><b>How:</b> The PDF is downloaded (conditional GET - the server may answer '304 not modified' and skip the download), its text is extracted and hashed, and the hash is compared with the previous run. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> UNREACHABLE - expected a PDF but the server returned an HTML page - the document may have moved or sit behind a bot check; the previous baseline is kept</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> Hard-dated versioned filename (20250312) - a revision likely ships under a new URL; ffs_tri_page link-set diffing is the catcher for replacements.</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

### Medi-Cal FFS (`medi_cal_ffs`)

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ffs_sb94_fp_fee_schedule - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx">Open the source</a> (clicking downloads an Excel file) - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx">https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx</a> (clicking downloads an Excel file)</li>
<li><b>How:</b> The raw file bytes are hashed and compared; no text is extracted, so this entry can never produce a text diff. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged - 304 not modified</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> none since the change log began</li>
<li><b>Watchlist note:</b> SB 94 family-planning augmented fee schedule (supersedes TRI for FP codes with Z30.x). Versioned filename - a replacement appears via ffs_tri_page. The URL is a direct .xlsx download; prefer opening the TRI landing page and downloading from there.</li>
<li><b>Master rows to verify on change:</b> FPACT rows priced on the SB 94 schedule</li>
</ul>
</details>

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> ffs_tri_page - `LINKS_CHANGED`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">Open the source</a> - checked 2026-07-17</p>

<p style="margin:.2em 0 .2em 2em"><b>Why:</b> +0 [] / -3 [&#x27;/wp-content/uploads/2025/10/Web-Accessibility-Cert.pdf&#x27;, &#x27;https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx&#x27;, &#x27;https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx&#x27;]</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> LINKS_CHANGED - +0 [] / -3 [&#x27;/wp-content/uploads/2025/10/Web-Accessibility-Cert.pdf&#x27;, &#x27;https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx&#x27;, &#x27;https://www.dhcs.ca.gov/wp-content/uploads/2025/10/SB94-Family-Planning-Services-Fee-Schedule.xlsx&#x27;]</li>
<li><b>Blind spot:</b> This page is client-rendered - the checker sees only the app shell and cannot detect content changes. Detection relies on the MCSS email subscription; open the page yourself when in doubt: <a href="https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/">https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/</a></li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> 2026-07-17 (LINKS_CHANGED)</li>
<li><b>Watchlist note:</b> TRI landing; link-set diff catches re-versioned fee schedule filenames and new APL redlines. Heads-up for readers - the fee schedule links on this page are direct .xlsx downloads (clicking one downloads an Excel file rather than opening a page).</li>
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

#### <span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e6f4ea;color:#0f5132;white-space:nowrap">Clear</span> ncci_medicaid_files - `unchanged`

<p style="margin:.2em 0 .2em 2em"><a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files">Open the source</a> - checked 2026-07-17</p>

<details style="margin:.3em 0 1.1em 2em">
<summary>Details: exactly what is checked here, how, and its caveats</summary>
<ul style="line-height:1.6;margin:.5em 0;padding-left:1.4em">
<li><b>URL checked:</b> <a href="https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files">https://www.cms.gov/medicare/coding-billing/ncci-medicaid/medicaid-ncci-edit-files</a></li>
<li><b>How:</b> The page's visible text is hashed AND every file link matching the entry's pattern is collected; a new or removed link is flagged even when the page text is unchanged. Checked by the weekly Monday run (14:00 UTC GitHub Action).</li>
<li><b>This run:</b> unchanged</li>
<li><b>Last checked:</b> 2026-07-17</li>
<li><b>Last recorded change:</b> 2026-07-16 (CHANGED)</li>
<li><b>Watchlist note:</b> Quarterly PTP/MUE file drops appear as new links (first run captured the 2026 Q3 set effective 07/01/2026). File links are direct downloads (.zip/.xlsx).</li>
<li><b>Master rows to verify on change:</b> none mapped in the watchlist; triage by judgment.</li>
</ul>
</details>

### Source URLs at a glance

Plain list of every URL this page's data comes from.

```text
fpact_bulletin_probe: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/bulletin?community=family-pact&issueNumber={issue}
fpact_manual_docs--00letter: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B84C9830-1762-442B-BB11-268B9BB1008B
fpact_manual_docs--0bhwtouse: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/D5B367D8-ED60-4A57-A0F1-71B9626E038A
fpact_manual_docs--1tocfpact: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5416438C-154C-4523-B1C8-8C3888870C71
fpact_manual_docs--benclinic: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/88BE8827-BF04-44FF-86AF-FF16018A7E43
fpact_manual_docs--benfam: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED
fpact_manual_docs--benfamrel: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8
fpact_manual_docs--bengrid: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/59A4DC78-0B85-42B8-90A1-29DF9A757683
fpact_manual_docs--claimcms: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/EBC8AE98-3518-404D-92E3-2FB7CFEB234D
fpact_manual_docs--claimub: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/99A15B51-5AE1-45B4-BEB3-300F9FA3974F
fpact_manual_docs--clientelig: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/907504BF-B611-4569-AA2F-AD19852DC99A
fpact_manual_docs--clinic: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/235F5DF8-9BF2-4851-839C-9C857C757B10
fpact_manual_docs--drug: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5
fpact_manual_docs--drugonsite: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC
fpact_manual_docs--fam: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A3EA3460-4D92-45A3-9F1C-BF9B8A2DC528
fpact_manual_docs--hapid: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/4DD29A09-8E9C-4E33-A06C-4F2EFC196326
fpact_manual_docs--lab: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/C9BE0AAF-EEFB-433A-88AF-43D59741B72B
fpact_manual_docs--office: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7CD4E2BB-3DF5-4FEC-9B68-9D8841D0A55F
fpact_manual_docs--pharm: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B4632038-8414-4115-BE87-3AF4C0B42E00
fpact_manual_docs--pharmacy: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/5D034DCC-2326-4204-A490-63334447067F
fpact_manual_docs--progstand: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AC89DF41-778B-49CD-ACF4-EAF9C4644904
fpact_manual_docs--provenrollres: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/1FC58406-1722-4888-80A5-7B1DBBEB9F29
fpact_manual_docs--provrel: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/AAB9378C-D021-4208-AB7A-B6A7A7549643
fpact_manual_docs--radif: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/A8A04AB0-8C04-4653-9A48-0C765462A3A0
fpact_manual_docs--tarf: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/0CEE81EC-C0E9-4B4A-89FD-AE96C95FA705
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
