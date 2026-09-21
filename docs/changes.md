# Change review

**TL;DR:** 7 source(s) need review, 3 billing code(s) on the changed lines.

[Back to the dashboard](https://mp321.github.io/RevInt-SourceWatch/) - script last ran 2026-09-21.

Each block below is one flagged source: what happened, any billing codes found on the changed lines (heuristic - **verify each against the linked source before acting**), and a link to the official document.

<div style="height:1.6em"></div>

## fpact_manual_docs--benfam - Family PACT

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - detected 2026-09-21

**What happened:** The text of this document is not the same as the copy stored at the last check.

**Source of truth:** [https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact)

**Watched file:** `https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/BCA0E984-8DF3-4AD4-9499-7DFCA25DCAED` - a portal endpoint readable only by the checker; open the source link above.

**Full before/after diff:** [reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md)

**Follow-up:** ppbi_source_section rows for any changed section

<div style="height:1.6em"></div>

## fpact_manual_docs--drug - Family PACT

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `CHANGED` - detected 2026-09-21

**What happened:** The text of this document is not the same as the copy stored at the last check.

**Source of truth:** [https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact)

**Watched file:** `https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5` - a portal endpoint readable only by the checker; open the source link above.

**Codes on the changed lines** (machine-extracted, verify each):

| Code | System | What | Confidence | Open at |
|---|---|---|---|---|
| `J7299` | HCPCS | both | low | p.7 |
| `J7300` | HCPCS | both | low | p.7 |
| `J7307` | HCPCS | both | low | p.7 |

**Full before/after diff:** [reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md](https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md)

**Follow-up:** ppbi_source_section rows for any changed section

<div style="height:1.6em"></div>

## fpact_news_archive - Family PACT

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#ffebe9;color:#7a271a;white-space:nowrap">Needs review</span> `LINKS_CHANGED` - detected 2026-09-21

**What happened:** The list of files this page links to changed: +1 added, -1 removed. The page's own wording did not have to change for this to flag.

- added: [https://familypact.org/planned-family-pact-portal-production-outage-september-18-20-2026/](https://familypact.org/planned-family-pact-portal-production-outage-september-18-20-2026/)
- removed: [https://familypact.org/fda-approves-updated-nexplanon-label-and-launches-new-rems/](https://familypact.org/fda-approves-updated-nexplanon-label-and-launches-new-rems/)

**Source of truth:** [https://familypact.org/news-and-updates-archive/](https://familypact.org/news-and-updates-archive/)

**Follow-up:** triage per announcement

<div style="height:1.6em"></div>

## rev_clinics_hospitals_manuals - Manual Revision Notices

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> `REVISION_NOTICE` - detected 2026-09-21

**What happened:** 5 of 247 manual sections moved: 'Cell and Gene Therapy (cel gen over)' revised 2026-07-16 -&gt; 2026-09-16; 'List of Contracted Incontinence Creams and Washes' revised 2025-11-14 -&gt; 2026-09-16; 'Non-Physician Medical Practitioners (NMP) (non ph)' revised 2026-03-16 -&gt; 2026-09-16; 'Other Health Coverage (OHC) (oth hlth)' revised 2023-08-06 -&gt; 2026-09-16; 'List of Physician Administered Drugs and HCPCS Codes (physician list)' revised 2026-07-16 -&gt; 2026-09-16

**Source of truth:** [https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals)

**Follow-up:** outpatient clinic / hospital billing rows on related section changes

<div style="height:1.6em"></div>

## rev_general_medicine_manuals - Manual Revision Notices

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> `REVISION_NOTICE` - detected 2026-09-21

**What happened:** 5 of 230 manual sections moved: 'Cell and Gene Therapy (cel gen over)' revised 2026-07-16 -&gt; 2026-09-16; 'List of Contracted Incontinence Creams and Washes' revised 2025-11-14 -&gt; 2026-09-16; 'Non-Physician Medical Practitioners (NMP) (non ph)' revised 2026-03-16 -&gt; 2026-09-16; 'Other Health Coverage (OHC) (oth hlth)' revised 2023-08-06 -&gt; 2026-09-16; 'List of Physician Administered Drugs and HCPCS Codes (physician list)' revised 2026-07-16 -&gt; 2026-09-16

**Source of truth:** [https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=general-medicine)

**Follow-up:** professional-services billing rows on related section changes

<div style="height:1.6em"></div>

## rev_inpatient_manuals - Manual Revision Notices

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> `REVISION_NOTICE` - detected 2026-09-21

**What happened:** 1 of 115 manual sections moved: 'Other Health Coverage (OHC) (oth hlth)' revised 2023-08-06 -&gt; 2026-09-16

**Source of truth:** [https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=inpatient-services)

**Follow-up:** inpatient billing rows on related section changes

<div style="height:1.6em"></div>

## rev_obstetrics_manuals - Manual Revision Notices

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<span style="display:inline-block;padding:.1em .6em;border-radius:1em;font-size:.82em;font-weight:600;background:#e8f1fb;color:#1e4a7a;white-space:nowrap">Revision notice</span> `REVISION_NOTICE` - detected 2026-09-21

**What happened:** 3 of 173 manual sections moved: 'Non-Physician Medical Practitioners (NMP) (non ph)' revised 2026-03-16 -&gt; 2026-09-16; 'Other Health Coverage (OHC) (oth hlth)' revised 2023-08-06 -&gt; 2026-09-16; 'List of Physician Administered Drugs and HCPCS Codes (physician list)' revised 2026-07-16 -&gt; 2026-09-16

**Source of truth:** [https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=obstetrics)

**Follow-up:** obstetric and perinatal billing rows on related section changes

<div style="height:1.6em"></div>

## Change history

<div style="height:3px;background:#1f4e79;border-radius:2px;margin:.15em 0 1.2em"></div>

<details style="margin:.3em 0 1.1em 0">
<summary>Last 20 recorded change event(s) (newest first)</summary>
<table style="font-size:.9em;line-height:1.5">
<tr><th>Date</th><th>Source</th><th>Status</th><th>Diff</th></tr>
<tr><td>2026-09-21</td><td><code>rev_general_medicine_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-09-21</td><td><code>rev_obstetrics_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-09-21</td><td><code>rev_clinics_hospitals_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-09-21</td><td><code>rev_inpatient_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-09-21</td><td><code>fpact_manual_docs--drug</code></td><td><code>CHANGED</code></td><td><a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190205Z_fpact--fpact_manual_docs--drug.md">diff</a></td></tr>
<tr><td>2026-09-21</td><td><code>fpact_manual_docs--benfam</code></td><td><code>CHANGED</code></td><td><a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260921T190149Z_fpact--fpact_manual_docs--benfam.md">diff</a></td></tr>
<tr><td>2026-09-21</td><td><code>fpact_news_archive</code></td><td><code>LINKS_CHANGED</code></td><td></td></tr>
<tr><td>2026-09-14</td><td><code>mcp_apl_index</code></td><td><code>CHANGED</code></td><td><a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260914T190102Z_managed_medi_cal--mcp_apl_index.md">diff</a></td></tr>
<tr><td>2026-09-14</td><td><code>fpact_news_archive</code></td><td><code>LINKS_CHANGED</code></td><td></td></tr>
<tr><td>2026-09-07</td><td><code>fpact_news_archive</code></td><td><code>LINKS_CHANGED</code></td><td></td></tr>
<tr><td>2026-08-31</td><td><code>ncci_medicaid_files</code></td><td><code>LINKS_CHANGED</code></td><td></td></tr>
<tr><td>2026-08-31</td><td><code>rev_general_medicine_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-08-31</td><td><code>rev_obstetrics_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-08-31</td><td><code>rev_clinics_hospitals_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-08-31</td><td><code>fqhc_cms_center</code></td><td><code>CHANGED</code></td><td><a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260831T194936Z_fqhc--fqhc_cms_center.md">diff</a></td></tr>
<tr><td>2026-08-24</td><td><code>mcp_apl_index</code></td><td><code>CHANGED</code></td><td><a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260824T143811Z_managed_medi_cal--mcp_apl_index.md">diff</a></td></tr>
<tr><td>2026-08-17</td><td><code>ncci_medicaid_files</code></td><td><code>CHANGED</code></td><td><a href="https://github.com/mp321/RevInt-SourceWatch/blob/main/reports/diffs/20260817T142415Z_ncci--ncci_medicaid_files.md">diff</a></td></tr>
<tr><td>2026-08-17</td><td><code>rev_general_medicine_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-08-17</td><td><code>rev_obstetrics_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
<tr><td>2026-08-17</td><td><code>rev_clinics_hospitals_manuals</code></td><td><code>REVISION_NOTICE</code></td><td></td></tr>
</table>
</details>

---

Machine-generated review aid, rebuilt each time script is ran. Do not consider an official source of record - validate any item against the live official source before acting. Provided as-is, without warranty. Built and maintained by [Michael Phipps](https://github.com/mp321); released under the MIT license ([LICENSE](https://github.com/mp321/RevInt-SourceWatch/blob/main/LICENSE)), credit appreciated if you reuse it.
