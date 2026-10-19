# Change: fqhc_rural_manual_docs--ruralcd

- Program: fqhc
- Source: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/2D80A3B6-A32B-4131-BE63-12EE7243A849
- Detected: 2026-10-19T19:37:55+00:00
- Title: Rural Health Clinics (RHCs) and Federally Qualified Health Centers (FQHCs):  Billing Codes (rural cd)
- Portal revision date: 2026-10-16T16:49:34
- Portal page: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=clinics-and-hospitals

Verify against the live official source before acting.
Machine-extracted text; diffs can contain extraction noise.

## Billing codes on the changed lines

Heuristic extraction from changed lines only - **verify every row against the live source before acting**. Page numbers come from the extracted-text snapshot and link into the PDF.

| Code | System | Direction | Confidence | Page | Context (excerpt) |
|---|---|---|---|---|---|
| `T1015` | HCPCS | both | medium | p.9 | 0521 T1015 SE Dental services that are delivered to members enrolled in |

## Text diff (previous -> current)

```diff
--- previous
+++ current
@@ -119,5 +119,5 @@
 Part 2 – Rural Health Clinics (RHCs) and Federally Qualified Health Centers (FQHCs):
 Billing Codes
-Page updated: June 2026
+Page updated: October 2026
 In addition, providers are required to keep copies of billing records, including supporting
 documents (for example, authorization approvals, lab orders and results, and invoices for
@@ -134,5 +134,5 @@
 When submitting claims directly to DHCS, RHC and FQHC providers should submit the ASC
 X12N 837I standard electronic form through the Computer Media Claims (CMC) system or
-use the CMS Form 1450 (UB-04) paper claim form, unless otherwise instructed.›› For more
+use the CMS Form 1450 (UB-04) paper claim form, unless otherwise instructed. For more
 information on how to complete the forms, refer to the UB-04 Completion: Outpatient
 Services and UB-04 Submission and Timeliness Instructions section of this manual or
@@ -147,18 +147,24 @@
 and to accurately attribute the service to the appropriate location for crossover, Medi-Cal
 MCP, and Medi-Cal fee-for-service claims.
+‹‹ICD-10-CM Code Requirement
+RHC and FQHC providers must include at least one clinically appropriate ICD-10-CM code
+when completing a UB-04 claim form or the 837I electronic form. Providers can include
+ICD-10-CM codes in Box 67 of the UB-04 claim form.
+For UB-04 claim completion instructions, refer to the UB-04 Completion: Outpatient Services
+section of the provider manual.››
+[[page 5]]
+rural cd
+5
+Part 2 – Rural Health Clinics (RHCs) and Federally Qualified Health Centers (FQHCs):
+Billing Codes
+Page updated: October 2026
 Informational Lines
 An informational line is an associated line item(s) listed immediately following the Health
 Insurance Portability and Accountability Act (HIPAA)-compliant RHC or FQHC per-visit
-billing code set used to bill the visit with the Medi-Cal member.›› Informational lines contain
-all CPT-4 Level I or HCPCS Level II code(s) that identify the actual service(s) provided.
+billing code set used to bill the visit with the Medi-Cal member. Informational lines contain all
+CPT-4 Level I or HCPCS Level II code(s) that identify the actual service(s) provided.
 When billing for RHC or FQHC covered services, informational lines should be included in
 addition to the RHC or FQHC per visit billing code sets included in this manual.
 Note: Informational lines are not separately reimbursed.
-[[page 5]]
-rural cd
-5
-Part 2 – Rural Health Clinics (RHCs) and Federally Qualified Health Centers (FQHCs):
-Billing Codes
-Page updated: June 2026
 When submitting informational lines, RHC and FQHC providers should remember the
 following:
@@ -188,14 +194,14 @@
 must obtain prior authorization to act as an OON provider and redirect the member to their
 in-network provider or request reassignment from MCP to their clinic.
+[[page 6]]
+rural cd
+6
+Part 2 – Rural Health Clinics (RHCs) and Federally Qualified Health Centers (FQHCs):
+Billing Codes
+Page updated: October 2026
 Members enrolled in a Medi-Cal MCP or Medi-Cal Dental Managed Care (DMC) plan must
 receive services from in-network MCP providers, except in urgent or other isolated
 circumstances. If the member is not enrolled in a Medi-Cal Dental managed care plan, a
 straight Medi-Cal dental visit may be billed, per-visit code 03.
-[[page 6]]
-rural cd
-6
-Part 2 – Rural Health Clinics (RHCs) and Federally Qualified Health Centers (FQHCs):
-Billing Codes
-Page updated: June 2026
 If an RHC or FQHC delivers an urgent or isolated medical, mental health, or dental service
 to a member not assigned to them, the RHC or FQHC must:
@@ -254,6 +260,6 @@
 Medical or Mental Health Services for Medi-Cal Fee-For-Service
 Members
-Table of Per-Visit Billing Code Set: Medical or Mental Health Services for Fee-
-For-Service Members
+Table of Per-Visit Billing Code Set: Medical or Mental Health Services for
+Fee-For-Service Members
 Revenue
 Code
@@ -343,6 +349,5 @@
 Modifier
 Description
-0521 T1015 SE Dental services that are delivered to members enrolled in
-a Medi-Cal DMC plan
+0521 T1015 SE Dental services that are delivered to members enrolled in a Medi-Cal DMC plan
 RHC and FQHC providers must use this MCP differential rate (wrap) per-visit billing code set
 (revenue and procedure codes with modifier) for dental services rendered to an MCP
@@ -505,10 +510,10 @@
 Contractor (MAC) for processing.
 For members enrolled in a Medicare Advantage non-capitated arrangement, the clinic must
-bill the Medicare Advantage plan first, then the MAC, for the Medicare Advantage Wrap-
-Around Payment (Revenue Code 519) before billing Medi-Cal.
-Note (For UB-04 claim forms): Do not enter Medicare status information in Condition Codes
-(boxes 24-30) fields. The following statement must be included in the Remarks (Box
-80) field of the claim or submit it as an 8 1/2" x 11" attachment: “For a fee-for-service
-Medi-Cal member enrolled in a fee-for-service Medicare Advantage Plan.”
+bill the Medicare Advantage plan first, then the MAC, for the Medicare Advantage
+Wrap-Around Payment (Revenue Code 519) before billing Medi-Cal.
+Note: (For UB-04 claim forms): Do not enter Medicare status information in Condition
+Codes (boxes 24-30) fields. The following statement must be included in the Remarks
+(Box 80) field of the claim or submit it as an 8 1/2" x 11" attachment: “For a fee-for-
+service Medi-Cal member enrolled in a fee-for-service Medicare Advantage Plan.”
 Table of Per Visit Billing Code Sets: Cross Over Claims Payment for Fee-For-Service
 Members Enrolled in Medicare Advantage Plan (Capitated Arrangement)
```
