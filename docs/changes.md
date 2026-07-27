# Change review

**TL;DR:** 2 source(s) changed, no billing codes detected in the changes.

[Back to the dashboard](https://mp321.github.io/RevInt-SourceWatch/) - script last ran 2026-07-27T16:15:31+00:00.

Each block below is one flagged source: what happened, which billing codes moved (heuristic - **verify each against the linked source before acting**), and a working link to the exact spot in the official document.

<div style="height:1.6em"></div>

## fpact_news_archive - Family PACT

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `LINKS_CHANGED` - detected 2026-07-27

**What happened:** The list of files this page links to changed: +2 added, -2 removed. The page's own wording did not have to change for this to flag.

- added: [https://familypact.org/medi-cal-news-rems-certification-and-provider-training-required-to-administer-nexplanon/](https://familypact.org/medi-cal-news-rems-certification-and-provider-training-required-to-administer-nexplanon/)
- added: [https://familypact.org/planned-family-pact-portal-production-outage-july-26-27-2026/](https://familypact.org/planned-family-pact-portal-production-outage-july-26-27-2026/)
- removed: [https://familypact.org/dhcs-4475-update/](https://familypact.org/dhcs-4475-update/)
- removed: [https://familypact.org/one-site-certifier-for-multiple-service-locations-update/](https://familypact.org/one-site-certifier-for-multiple-service-locations-update/)

**Source of truth:** [https://familypact.org/news-and-updates-archive/](https://familypact.org/news-and-updates-archive/)

**Registry rows to verify:** triage per announcement

<div style="height:1.6em"></div>

## ffs_tri_fee_schedule - Medi-Cal FFS

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `NEW` - detected 2026-07-27

**What happened:** First time this source was checked - its current state was saved as the starting point.

**Source of truth:** [https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/](https://www.dhcs.ca.gov/medi-cal-targeted-provider-rate-increases-and-investments/)

**Watched file:** [https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx](https://www.dhcs.ca.gov/wp-content/uploads/2025/10/CY-2024-TRI-Fee-Schedule-Feb.xlsx) (clicking downloads an Excel file)

**Registry rows to verify:** reimbursement_basis rows citing TRI

<div style="height:1.6em"></div>

## Change history

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<details style="margin:.3em 0 1.1em 0">
<summary>Last 7 recorded change event(s) (newest first)</summary>
<table style="font-size:.9em;line-height:1.5">
<tr><th>Date</th><th>Source</th><th>Status</th><th>Diff</th></tr>
<tr><td>2026-07-27</td><td><code>ffs_tri_fee_schedule</code></td><td><code>NEW</code></td><td></td></tr>
<tr><td>2026-07-27</td><td><code>fpact_news_archive</code></td><td><code>LINKS_CHANGED</code></td><td></td></tr>
<tr><td>2026-07-20</td><td><code>mcp_apl_index</code></td><td><code>CHANGED</code></td><td></td></tr>
<tr><td>2026-07-17</td><td><code>fpact_news_archive</code></td><td><code>LINKS_CHANGED</code></td><td></td></tr>
<tr><td>2026-07-16</td><td><code>ncci_medicaid_files</code></td><td><code>CHANGED</code></td><td></td></tr>
<tr><td>2026-07-16</td><td><code>fqhc_cms_center</code></td><td><code>CHANGED</code></td><td></td></tr>
<tr><td>2026-07-16</td><td><code>mcp_apl_index</code></td><td><code>CHANGED</code></td><td></td></tr>
</table>
</details>

---

Machine-generated review aid, rebuilt by each script run. Not a source of record and not billing advice - validate every item against the live official source before acting. Provided as-is, without warranty. Built and maintained by [Michael Phipps](https://github.com/mp321); released under the MIT license ([LICENSE](https://github.com/mp321/RevInt-SourceWatch/blob/main/LICENSE)), credit appreciated if you reuse it.
