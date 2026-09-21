# Change: fpact_manual_docs--drug

- Program: fpact
- Source: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/7C45AD4C-2A15-41B5-98E1-93F2C94370D5
- Detected: 2026-09-21T19:02:05+00:00
- Title: Drugs: Onsite Dispensing Billing Instructions (drug)
- Portal revision date: 2026-09-16T16:17:35
- Portal page: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact

Verify against the live official source before acting.
Machine-extracted text; diffs can contain extraction noise.

## Billing codes on the changed lines

Heuristic extraction from changed lines only - **verify every row against the live source before acting**. Page numbers come from the extracted-text snapshot and link into the PDF.

| Code | System | Direction | Confidence | Page | Context (excerpt) |
|---|---|---|---|---|---|
| `J7299` | HCPCS | both | low | p.7 | ‹‹J7299 Intrauterine copper contraceptive (Miudella) 1 IUC›› |
| `J7300` | HCPCS | both | low | p.7 | J7300 ‹‹Intrauterine copper contraceptive |
| `J7307` | HCPCS | both | low | p.7 | J7307 Etonogestrel contraceptive implant |

## Text diff (previous -> current)

```diff
--- previous
+++ current
@@ -228,12 +228,12 @@
 7
 Family PACT – Drugs: Onsite Dispensing Billing Instructions
-Page updated: March 2026
+Page updated: September 2026
 Table of Onsite Dispensed Contraceptives Billed with NDC (continued)
 HCPCS Code Contraceptives Dosage Size
 J7297 Levonorgestrel IU (Liletta), 52 mg 1 IUC
 J7298 Levonorgestrel IU (Mirena), 52 mg 1 IUC
-‹‹J7299 Intrauterine copper contraceptive (Miudella) 1 IUC››
-J7300 ‹‹Intrauterine copper contraceptive
-(Paragard)››
+J7299 Intrauterine copper contraceptive (Miudella) 1 IUC
+J7300 Intrauterine copper contraceptive
+(Paragard)
 1 IUC
 J7301 Levonorgestrel IU (Skyla), 13.5 mg 1 IUC
@@ -244,7 +244,5 @@
 ethinyl estradiol transdermal system)
 1 patch
-J7307 Etonogestrel contraceptive implant
-(Implanon)
-1 implant
+J7307 ‹‹Etonogestrel contraceptive implant›› 1 implant
 S4993 Oral contraceptives 1 cycle
 Onsite Dispensing Price Guide
```
