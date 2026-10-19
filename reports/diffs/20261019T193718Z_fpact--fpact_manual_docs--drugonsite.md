# Change: fpact_manual_docs--drugonsite

- Program: fpact
- Source: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/796C137C-F4E2-44CF-BE51-CCC0D94D7EAC
- Detected: 2026-10-19T19:37:18+00:00
- Title: Drugs: Onsite Dispensing Price Guide (drug onsite)
- Portal revision date: 2026-10-16T16:33:46
- Portal page: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/publications/manual?community=family-pact

Verify against the live official source before acting.
Machine-extracted text; diffs can contain extraction noise.

## Billing codes on the changed lines

Heuristic extraction from changed lines only - **verify every row against the live source before acting**. Page numbers come from the extracted-text snapshot and link into the PDF.

| Code | System | Direction | Confidence | Page | Context (excerpt) |
|---|---|---|---|---|---|
| `A4269` | HCPCS | both | low | p.1 | A4269-U5 ‹‹Contraceptive Vaginal gel›› Box $364.24 |
| `J3490` | HCPCS | both | low | p.1 | J3490-U5 Oral, Ulipristal acetate 30 mg ‹‹$37.11›› |
| `J7294` | HCPCS | both | low | p.1 | ‹‹J7294 Segesterone acetate and ethinyl |
| `J7295` | HCPCS | both | low | p.1 | ‹‹J7295 Ethinyl estradiol and etonogestrel |
| `S4993` | HCPCS | both | low | p.1 | ‹‹S4993 Contraceptive pills for birth control 1 cycle $12.00›› |

## Text diff (previous -> current)

```diff
--- previous
+++ current
@@ -4,5 +4,5 @@
 Family PACT – Drugs: Onsite Dispensing Price Guide
 Drugs: Onsite Dispensing Price Guide
-Page updated: June 2026
+Page updated: October 2026
 This section includes billing instructions and reimbursement rates for drugs covered by the
 Family Planning, Access, Care and Treatment (Family PACT) Program when dispensed
@@ -22,30 +22,30 @@
 A4269-U3 Spermicidal vaginal film Each $0.69
 A4269-U4 Contraceptive sponge Each $2.35
-A4269-U5 ‹‹Contraceptive Vaginal gel›› Box $364.24
+A4269-U5 Contraceptive Vaginal gel Box ‹‹$363.09››
 J3490 Injection, medroxyprogesterone
 acetate
-104mg/0.65
+104 mg/0.65
 ml
 $50.53
-J3490-U5 Oral, Ulipristal acetate 30 mg ‹‹$37.11››
-J3490-U6 Oral, levonorgestrel 1.5 mg ‹‹$6.45››
+J3490-U5 Oral, Ulipristal acetate 30 mg ‹‹$37.09››
+J3490-U6 Oral, levonorgestrel 1.5 mg ‹‹$6.40››
 J3490-U8 Injection, medroxyprogesterone
 acetate
-150 mg/ml ‹‹$33.11››
-‹‹J7294 Segesterone acetate and ethinyl
+150 mg/ml ‹‹$24.90››
+J7294 Segesterone acetate and ethinyl
 estradiol 0.15 mg, 0.013 mg per 24
 hours; yearly vaginal system, each
-Each $2313.05››
-‹‹J7295 Ethinyl estradiol and etonogestrel
+Each $2313.05
+J7295 Ethinyl estradiol and etonogestrel
 0.015 mg, 0.12 mg per 24 hours;
 monthly vaginal ring, each
-Each $135.11››
+Each $135.11
 J7304-U1 Patch, contraceptive, hormone-
 containing
-Each ‹‹$36.82››
+Each ‹‹$37.57››
 J7304-U2 Patch, contraceptive, hormone-
 containing
-Each $67.21
-‹‹S4993 Contraceptive pills for birth control 1 cycle $12.00››
+Each ‹‹$66.80››
+S4993 Contraceptive pills for birth control 1 cycle $12.00
 S5199 Lubricant (non-spermicidal) Gram $0.03
 [[page 2]]
```
