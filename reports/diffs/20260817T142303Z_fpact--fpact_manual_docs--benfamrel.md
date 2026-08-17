# Change: fpact_manual_docs--benfamrel

- Program: fpact
- Source: https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8
- Detected: 2026-08-17T14:23:03+00:00
- Title: Benefits: Family Planning-Related Services (ben fam rel)
- Portal revision date: 2026-08-14T16:22:28

Verify against the live official source before acting.
Machine-extracted text; diffs can contain extraction noise.

## Possible billing codes touched

Heuristic extraction from changed lines only - **verify every row against the live source before acting**. Page numbers come from the extracted-text snapshot and link into the PDF.

| Code | System | Direction | Confidence | Page | Context (excerpt) |
|---|---|---|---|---|---|
| `85651` | CPT | both | high | [p.17](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=17) | ‹‹85651*›› Sedimentation rate, erythrocyte; non-automated |
| `33` | modifier | both | high | [p.4](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=4) | modifier 33 indicates the service was provided in accordance with USPSTF A or B |
| `81000` | CPT | removed | medium | [p.10](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=10) | ‹‹81000∞›› Urinalysis, by dip stick or tablet reagent for |
| `85025` | CPT | removed | medium | [p.17](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=17) | ‹‹85025*›› Blood count; complete (CBC), automated (Hgb, Hct, RBC, WBC and |
| `87491` | CPT | removed | medium | [p.17](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=17) | ‹‹87491*›› Chlamydia trachomatis, amplified probe technique |
| `87624` | CPT | both | medium | [p.6](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=6) | • 87624: Infectious agent detection by nucleic acid (DNA or RNA); Human |
| `B37.31` | ICD-10-CM | both | medium | [p.21](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=21) | ‹‹Vulvovaginal Candidiasis›› B37.31 Acute candidiasis of vulva and vagina |
| `Q0111` | HCPCS | both | low | [p.14](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=14) | ‹‹Q0111∞›› Wet mounts, including preparations of vaginal, cervical or skin specimens |
| `S5000` | HCPCS | both | low | [p.22](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=22) | S5000/S5001 Prescription drugs, generic/brand |
| `S5001` | HCPCS | both | low | [p.22](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=22) | S5000/S5001 Prescription drugs, generic/brand |
| `B37.32` | ICD-10-CM | both | low | [p.21](https://mcweb.apps.prd.cammis.medi-cal.ca.gov/assets/B32916F9-83E4-4C1A-B089-BF8E6C601FA8#page=21) | ‹‹Vulvovaginal Candidiasis›› B37.32 Chronic candidiasis of vulva and |

## Text diff (previous -> current)

```diff
--- previous
+++ current
@@ -55,7 +55,6 @@
 For a list of reimbursable drugs and dispensing guidelines, including restrictions and
 authorization requirements refer to the Family PACT Pharmacy Formulary on the Medi-Cal
-Rx website (https://www.medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+Rx website, as well as the Clinic Formulary section and “Treatment and Dispensing
+Guidelines for Clinicians” in the Benefits Grid section in this manual.
 [[page 3]]
 ben fam rel
@@ -87,5 +86,5 @@
 4
 Family PACT – Benefits: Family Planning-Related Services
-Page updated: January 2026
+Page updated: August 2026
 Family Planning-Related Tests
 Laboratory Tests
@@ -93,19 +92,33 @@
 Cervical Cancer Screening
 Cervical cancer screening is covered when provided as part of a family planning visit. It is
-not a stand-alone service. Family PACT has adopted the U.S. Preventive Services Task
-Force (USPSTF) 2018 Final Recommendation Statement for Cervical Cancer Screening.
-This guideline contains age-based screen strategies and screening intervals. Follow-up
-visits and services related to abnormal results from screening can be found under the
-“Management of Cervical Abnormalities and Pre-invasive Cervical Lesions” heading in this
-section.
-‹‹For cervical cancer screening, the USPSTF recommends screening for cervical cancer
-every three years with cervical cytology alone in women 21 to 29 years of age. For women
-30 to 65 years of age, the USPSTF recommends screening every three years with cervical
-cytology alone, every five years with high-risk human papillomavirus (hrHPV) testing alone
-or every five years with hrHPV testing in combination with cytology (co-testing). Use of
-modifier 33 indicates the service was provided in accordance with USPSTF A or B
-recommendation.››
-The following cervical cancer screening codes are restricted to women ages 21 through 65
+not a stand-alone service.
+‹‹The U.S. Preventive Services Task Force (USPSTF) 2018 Cervical Cancer Screening
+recommendations include:
+• Screening for cervical cancer every three years with cervical cytology alone in women
+21 to 29 years of age.
+• For women 30 to 65 years of age, the USPSTF recommends screening every three
+years with cervical cytology alone, every five years with high-risk human
+papillomavirus (hrHPV) testing alone (primary hrHPV screening), or every five years
+with hrHPV testing in combination with cytology (co-testing).
+Reimbursement for primary hrHPV testing includes self-collected vaginal specimens, which
+is an acceptable option for average-risk individuals age 30 thru 65 according to Health
+Resources and Services Administration, American Cancer Society and the Enduring
+Consensus Cervical Cancer Screening and Management Guidelines. Screening after a
+negative self-collected hrHPV test should be repeated in 3 years.
+Note: Use of modifier 33 indicates the service was provided in accordance with USPSTF A
+or B recommendation.››
+The following cervical cancer screening codes are restricted to women ages 21 thru 65
 regardless of sexual history.
+‹‹The USPSTF recommends against screening for cancer in women who:
+• Are younger than 21 years,
+• Have had a hysterectomy with removal of the cervix and do not have a history of a
+high-grade precancerous lesion or cervical cancer, and
+• Are older than 65 years who have had adequate prior screening and are not otherwise
+at high risk for cervical cancer.››
+[[page 5]]
+ben fam rel
+5
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Reimbursement may be made for services provided to women younger than 21 years or
 over the age of 65 who have, or do not have, a cervix. However, the ordering provider must
@@ -124,14 +137,14 @@
 undetermined significance (ASC-US), low-grade squamous intraepithelial lesion
 (LSIL), or CIN 1 test result
-[[page 5]]
-ben fam rel
-5
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: January 2026
 • Over the age of 65 who did not have adequate negative prior screening. Adequate
 negative prior screening is defined as three consecutive negative cytology results or
 two consecutive negative co-tests within the 10 years before cessation of screening,
 with the most recent test occurring within the past five years.
-Cervical Screening Codes Table
+[[page 6]]
+ben fam rel
+6
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
+‹‹Cervical Cytology Codes Table››
 CPT® Code Description
 88142 Cytopathology, cervical or vaginal (any reporting system), collected in
@@ -159,24 +172,26 @@
 automated system and manual rescreening or review under physician
 supervision
-[[page 6]]
-ben fam rel
-6
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: January 2026
-Primary Cervical Cancer Screening with High Risk Human
+[[page 7]]
+ben fam rel
+7
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
+Primary Cervical Cancer Screening with High-Risk Human
 Papillomavirus (HPV) Testing
-‹‹The following CPT codes are reimbursable for recipients 21 years of age and older:
-• 87624: Infectious agent detection by nucleic acid (DNA or RNA); Human
-Papillomavirus (HPV), high-risk types (eg, 16, 18, 31, 33, 35, 39, 45, 51, 52, 56, 58,
-59, 68), pooled result
-• 87625: Infectious agent detection by nucleic acid (DNA or RNA); Human
-Papillomavirus (HPV), types 16 and 18 only, includes type 45, if performed
-• 87626: Infectious agent detection by nucleic acid (DNA or RNA); Human
-Papillomavirus (HPV), separately reported high-risk types (eg, 16, 18, 31, 45, 51, 52)
-and high-risk pooled result(s)
+The following CPT codes are reimbursable for recipients 21 years of age and older:
+CPT Code Description
+87624 Infectious agent detection by nucleic acid (DNA or RNA); Human
+Papillomavirus (HPV), high-risk types (eg, 16, 18, 31, 33, 35, 39, 45, 51,
+52, 56, 58, 59, 68), pooled result
+87625 Infectious agent detection by nucleic acid (DNA or RNA); Human
+Papillomavirus (HPV), types 16 and 18 only, includes type 45, if
+performed
+87626 Infectious agent detection by nucleic acid (DNA or RNA); Human
+Papillomavirus (HPV), separately reported high-risk types (eg, 16, 18, 31,
+45, 51, 52) and high-risk pooled result(s)
 This service must be billed with the ICD-10-CM diagnosis code that identifies the
 contraceptive method for which the client is being seen. See the Laboratory Services section
 of this manual for additional diagnosis code requirements when testing is performed outside
-of USPSTF screening recommendations.››
+of USPSTF screening recommendations.
 Human Papillomavirus 9-valent Vaccine, Recombinant (9vHPV)
 Coverage for HPV vaccination is restricted to individuals 19 to 45 years of age. The Centers
@@ -199,9 +214,9 @@
 subcutaneous, or intramuscular injections); 1 vaccine (single or
 combination vaccine/toxoid)
-[[page 7]]
-ben fam rel
-7
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 8]]
+ben fam rel
+8
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Management of Sexually Transmitted Infections (STIs)
 Sexually Transmitted Infections (STIs)
@@ -223,9 +238,9 @@
 A56.4 Chlamydial infection of pharynx (M and F)
 N34.2 Other urethritis (M)
-[[page 8]]
-ben fam rel
-8
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 9]]
+ben fam rel
+9
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Presumptive Diagnosis
 Chlamydia Presumptive Diagnosis Codes Table
@@ -255,15 +270,14 @@
 Q0144 Azithromycin dihydrate
 S5000/S5001 Prescription drugs generic/brand (Doxycycline, Levofloxacin)
-[[page 9]]
-ben fam rel
-9
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: December 2025
+[[page 10]]
+ben fam rel
+10
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Pharmacy
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
 Additional Lab Tests
 Chlamydia Additional Lab Test Codes Table
@@ -274,7 +288,11 @@
 Symptomatic males only; not
 payable for Z20.2
-‹‹87491*›› Chlamydia trachomatis, amplified
+87491* Chlamydia trachomatis, amplified
 probe technique
 None
+‹‹87494* Chlamydia trachomatis and
+Neisseria gonorrhoeae, multiplex
+amplified probe technique
+None››
 Epididymitis
 Epididymitis Diagnosis Codes Table
@@ -292,9 +310,9 @@
 Supplies
 None
-[[page 10]]
-ben fam rel
-10
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: December 2025
+[[page 11]]
+ben fam rel
+11
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Drugs
 Epididymitis Drugs Codes Table
@@ -310,5 +328,5 @@
 Epididymitis Additional Lab Tests Codes Table
 CPT Code Description Restrictions
-‹‹81000∞›› Urinalysis, by dip stick or tablet reagent for
+81000∞ Urinalysis, by dip stick or tablet reagent for
 bilirubin, glucose, hemoglobin, ketones,
 leukocytes, nitrite, pH, protein, specific gravity,
@@ -316,18 +334,23 @@
 non-automated, with microscopy
 None
-‹‹81015∞›› Urinalysis; microscopic only None
+81015∞ Urinalysis; microscopic only None
 87205 Smear, primary source with interpretation;
 Gram or Giemsa stain for bacteria, fungi, or cell
 types
 Symptomatic males
-‹‹87491*›› Infectious agent detection by nucleic acid (DNA
+87491* Infectious agent detection by nucleic acid (DNA
 or RNA); Chlamydia trachomatis, amplified
 probe technique
 None
-‹‹87591*›› Infectious agent detection by nucleic acid (DNA
+‹‹87494* Infectious agent detection by nucleic acid (DNA
+or RNA); Chlamydia trachomatis and Neisseria
+gonorrhoeae, multiplex amplified probe
+technique
+None››
+87591* Infectious agent detection by nucleic acid (DNA
 or RNA); Neisseria gonorrhoeae, amplified
 probe technique
 None
-‹‹87563*›› Infectious agent detection by nucleic acid (DNA
+87563* Infectious agent detection by nucleic acid (DNA
 or RNA); Mycoplasma genitalium, amplified
 probe technique
@@ -335,9 +358,9 @@
 not covered when used and
 billed as a screening test.
-[[page 11]]
-ben fam rel
-11
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 12]]
+ben fam rel
+12
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Gonorrhea
 Gonorrhea Diagnosis Codes Table
@@ -371,9 +394,9 @@
 Supplies
 None
-[[page 12]]
-ben fam rel
-12
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: December 2025
+[[page 13]]
+ben fam rel
+13
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Drugs
 Gonorrhea Drug Codes Table
@@ -390,7 +413,6 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
 Additional Laboratory Tests
 Gonorrhea Additional Laboratory Test Codes Table
@@ -401,12 +423,16 @@
 Symptomatic males only; not
 payable for Z20.2
-‹‹87591*›› Neisseria gonorrhoeae,
+‹‹87494* Chlamydia trachomatis and
+Neisseria gonorrhoeae, multiplex
 amplified probe technique
-None
-[[page 13]]
-ben fam rel
-13
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: December 2025
+None››
+87591* Neisseria gonorrhoeae,
+amplified probe technique
+None
+[[page 14]]
+ben fam rel
+14
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Nongonococcal Urethritis (NGU)
 NGU Diagnosis Code Table
@@ -425,43 +451,45 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and TAR requirements, refer to the Family PACT Pharmacy Formulary on the Medi-Cal Rx
-website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section and the
-“Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+website, as well as the Clinic Formulary section and the “Treatment and Dispensing
+Guidelines for Clinicians” in the Benefits Grid section in this manual.
 Additional Laboratory Tests
 NGU Additional Laboratory Test Codes Table
 HCPCS/CPT
 Code Description
-‹‹81000∞›› Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin,
+81000∞ Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin,
 ketones, leukocytes, nitrite, pH, protein, specific gravity, urobilinogen, any
 number of these constituents; non-automated, with microscopy
-‹‹81001∞›› Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin,
+81001∞ Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin,
 ketones, leukocytes, nitrite, pH, protein, specific gravity, urobilinogen, any
 number of these constituents; automated, with microscopy
-‹‹81002*›› Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin,
+81002* Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin,
 ketones, leukocytes, nitrite, pH, protein, specific gravity, urobilinogen, any
 number of these constituents; non-automated, without microscopy
-[[page 14]]
-ben fam rel
-14
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: December 2025
+[[page 15]]
+ben fam rel
+15
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 NGU Additional Laboratory Test Codes Table (continued)
 HCPCS/CPT
 Code
 Description
-‹‹81003*›› Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin,
+81003* Urinalysis, by dip stick or tablet reagent for bilirubin, glucose, hemoglobin,
 ketones, leukocytes, nitrite, pH, protein, specific gravity, urobilinogen, any
 number of these constituents; automated, without microscopy
 81005 Urinalysis; qualitative or semiquantitative, except immunoassays
-‹‹81015∞›› Urinalysis; microscopic only
+81015∞ Urinalysis; microscopic only
 87205 Smear, primary source with interpretation; Gram or Giemsa stain for
 bacteria, fungi, or cell types
 87210 Smear, primary source with interpretation; wet mount for infectious agents
 (eg, saline, India ink, KOH preps)
-‹‹87491*›› Infectious agent detection by nucleic acid (DNA or RNA); Chlamydia
+87491* Infectious agent detection by nucleic acid (DNA or RNA); Chlamydia
 trachomatis, amplified probe technique
-‹‹87591*›› Infectious agent detection by nucleic acid (DNA or RNA); Neisseria
+‹‹87494* Infectious agent detection by nucleic acid (DNA or RNA); Chlamydia
+trachomatis and Neisseria gonorrhoeae, multiplex amplified probe
+technique››
+87591* Infectious agent detection by nucleic acid (DNA or RNA); Neisseria
 gonorrhoeae, amplified probe technique
-‹‹Q0111∞›› Wet mounts, including preparations of vaginal, cervical or skin specimens
+Q0111∞ Wet mounts, including preparations of vaginal, cervical or skin specimens
 Recurrent or Persistent Nongonococcal Urethritis or Cervicitis
 For recurrent or persistent nongonococcal urethritis or cervicitis: either test for Mycoplasma
@@ -481,9 +509,9 @@
 and in some cases of pelvic inflammatory disease (PID). CPT code 87563 is not a covered
 benefit when used and billed as a screening test in asymptomatic persons.
-[[page 15]]
-ben fam rel
-15
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 16]]
+ben fam rel
+16
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Genital Herpes
 Genital Herpes Diagnosis Codes Table
@@ -507,12 +535,11 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
-[[page 16]]
-ben fam rel
-16
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: April 2025
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
+[[page 17]]
+ben fam rel
+17
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Additional Laboratory Tests
 Genital Herpes Additional Laboratory Test Codes Table
@@ -529,5 +556,5 @@
 Limited to: N48.5 (M) and
 N76.6 (F)
-‹‹Benefits are limited to evaluation of ulcers of unconfirmed etiology.››
+Benefits are limited to evaluation of ulcers of unconfirmed etiology.
 Pelvic Inflammatory Disease (PID)
 Limited to outpatient services only; intravenous therapies are not covered.
@@ -542,9 +569,9 @@
 N94.89 Other specified conditions associated with female genital organs and
 menstrual cycle (F)
-[[page 17]]
-ben fam rel
-17
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: December 2025
+[[page 18]]
+ben fam rel
+18
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Supplies
 None
@@ -559,21 +586,20 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
 Additional Laboratory Tests
 PID Additional Laboratory Test Codes Table
 CPT Code Description
-‹‹85025*›› Blood count; complete (CBC), automated (Hgb, Hct, RBC, WBC and
+85025* Blood count; complete (CBC), automated (Hgb, Hct, RBC, WBC and
 platelet count) and automated differential WBC count
-‹‹85651*›› Sedimentation rate, erythrocyte; non-automated
+85651* Sedimentation rate, erythrocyte; non-automated
 85652 Sedimentation rate, erythrocyte; automated
-‹‹87491*›› Chlamydia trachomatis, amplified probe technique
-‹‹87591*›› Neisseria gonorrhoeae, amplified probe technique
-[[page 18]]
-ben fam rel
-18
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+87491* Chlamydia trachomatis, amplified probe technique
+87591* Neisseria gonorrhoeae, amplified probe technique
+[[page 19]]
+ben fam rel
+19
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Procedures
 PID Procedure Codes Table
@@ -599,9 +625,9 @@
 predominantly sexual mode of transmission (M and F)
 Indications: Use for an asymptomatic partner exposed to syphilis
-[[page 19]]
-ben fam rel
-19
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 20]]
+ben fam rel
+20
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Procedures
 Syphilis Procedure Code Table
@@ -624,7 +650,6 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
 Additional Laboratory Tests
 Syphilis Additional Laboratory Test Code Table
@@ -638,9 +663,9 @@
 presumptive diagnosis codes N48.5,
 N76.6 or Z20.2
-[[page 20]]
-ben fam rel
-20
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 21]]
+ben fam rel
+21
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Trichomoniasis
 Trichomoniasis Diagnosis Codes Table
@@ -668,12 +693,11 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
-[[page 21]]
-ben fam rel
-21
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2026
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
+[[page 22]]
+ben fam rel
+22
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Additional Laboratory Tests
 Trichomoniasis Additional Laboratory Test Codes Table
@@ -701,29 +725,27 @@
 Vulvovaginitis Diagnosis Codes Table
 Condition ICD-10-CM Code Description
-‹‹Vulvovaginal Candidiasis›› B37.31 Acute candidiasis of vulva and vagina
-‹‹Vulvovaginal Candidiasis›› B37.32 Chronic candidiasis of vulva and
+Vulvovaginal Candidiasis B37.31 Acute candidiasis of vulva and vagina
+Vulvovaginal Candidiasis B37.32 Chronic candidiasis of vulva and
 vagina
 Bacterial Vaginosis N76.0 Acute vaginitis
-‹‹Male Partner Therapy
+Male Partner Therapy
 Bacterial Vaginosis (BV) Male Partner Therapy Codes Table
 ICD-10-CM Code Description
 Z20.2 Contact with and (suspected) exposure to infections with a
 predominantly sexual mode of transmission.
-Indication: Use for BV-exposed partner (M).››
+Indication: Use for BV-exposed partner (M).
 Procedures
 None
 Supplies
 None
-[[page 22]]
-ben fam rel
-22
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2026
+[[page 23]]
+ben fam rel
+23
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Drugs
 Vulvovaginitis Drug Codes Table
 Condition HCPCS Code Description
-‹‹Vulvovaginal
-Candidiasis››
-S5000/S5001 Prescription drugs, generic/brand
+Vulvovaginal Candidiasis S5000/S5001 Prescription drugs, generic/brand
 (Clotrimazole, Fluconazole,
 Miconazole)
@@ -734,7 +756,6 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
 Additional Laboratory Tests
 Vulvovaginitis Additional Laboratory Test Codes Table
@@ -745,11 +766,11 @@
 agents (eg, saline, India ink, KOH
 preps)
-‹‹Females only for diagnosis
-of BV››
+Females only for diagnosis of
+BV
 Q0111∞ Wet mounts, including preparations of
 vaginal, cervical or skin specimens
 (including urethral specimens)
-‹‹Females only for diagnosis
-of BV.››
+Females only for diagnosis of
+BV.
 Genital Warts
 Genital Warts Diagnosis Codes Table
@@ -758,9 +779,9 @@
 B07.9 Viral warts, unspecified (M and F)
 B08.1 Molluscom contagiosum (M and F)
-[[page 23]]
-ben fam rel
-23
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 24]]
+ben fam rel
+24
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Procedures
 A modifier is required for the following procedures.
@@ -790,9 +811,9 @@
 TCA/BCA, liquid nitrogen and Podophyllin are included in the supply charge for the
 procedure and cannot be billed separately.
-[[page 24]]
-ben fam rel
-24
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 25]]
+ben fam rel
+25
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Drugs
 Genital Warts Drug Codes Table
@@ -802,7 +823,6 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
 Additional Laboratory Tests
 Genital Warts Additional Laboratory Test Codes Table
@@ -828,9 +848,9 @@
 partners, ensuring that all recent partners have been treated is a core aspect of the clinical
 management of patients diagnosed with chlamydia, gonorrhea and/or trichomoniasis.
-[[page 25]]
-ben fam rel
-25
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2026
+[[page 26]]
+ben fam rel
+26
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Family PACT covers medically necessary services for the treatment of STIs. If a Family
 PACT provider diagnoses a Family PACT client with gonorrhea, chlamydia and/or
@@ -846,5 +866,5 @@
 For a list of medically necessary services for the treatment of gonorrhea, chlamydia, and/or
 trichomoniasis, providers may refer to the preceding pages of this manual section.
-‹‹Male Partner Therapy for Bacterial Vaginosis (BV)
+Male Partner Therapy for Bacterial Vaginosis (BV)
 BV is often a recurrent infection and the concurrent treatment of a male sexual partner has
 been shown to reduce the risk of reinfection.
@@ -853,5 +873,5 @@
 regimen, recommended patient populations and additional considerations.
 Male partner therapy for BV is not an EPT benefit. The male partner must be a Family PACT
-client to receive treatment as a Family PACT covered benefit.››
+client to receive treatment as a Family PACT covered benefit.
 Urinary Tract Infection (UTI)
 Urinary Tract Infection (UTI) Females Only
@@ -866,9 +886,9 @@
 R31.0 Gross hematuria
 R35.0 Frequency of micturition
-[[page 26]]
-ben fam rel
-26
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2026
+[[page 27]]
+ben fam rel
+27
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Procedures
 None
@@ -883,7 +903,6 @@
 For a complete list of drugs reimbursed by the Family PACT Program, including restrictions
 and authorization requirements, refer to the Family PACT Pharmacy Formulary on the
-Medi-Cal Rx website (https://medi-calrx.dhcs.ca.gov), as well as the Clinic Formulary section
-and “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section in this
-manual.
+Medi-Cal Rx website, as well as the Clinic Formulary section and “Treatment and
+Dispensing Guidelines for Clinicians” in the Benefits Grid section in this manual.
 Additional Laboratory Tests
 UTI Additional Laboratory Test Codes Table
@@ -898,9 +917,9 @@
 81005 Urinalysis; qualitative or semi-quantitative, except immunoassays
 81015∞ Microscopic only
-[[page 27]]
-ben fam rel
-27
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 28]]
+ben fam rel
+28
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Management of Cervical Abnormalities and Preinvasive Cervical
 Lesions
@@ -911,6 +930,6 @@
 Abnormal Cervical Cancer Screening Tests and Cancer Precursors to guide clinicians in the
 management of abnormal screening and diagnostic tests. Personalized risk-based
-management requires the use of the tool at the ASCCP website (https://www.asccp.org), or
-the 2019 ASCCP Guidelines APP (https://www.asccp.org/mobile-app).
+management requires the use of the tool at the ASCCP website, or the 2019 ASCCP
+Guidelines App.
 The following services and supplies are reimbursable when performed on an outpatient
 basis for the diagnosis and treatment of cervical abnormalities found on cervical cancer
@@ -925,9 +944,9 @@
 services. The facility and loop electrocautery excision procedure (LEEP) provider must be
 participating Medi-Cal providers.
-[[page 28]]
-ben fam rel
-28
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 29]]
+ben fam rel
+29
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Cervical Abnormalities
 Cervical Abnormalities Diagnosis Codes Table
@@ -955,9 +974,9 @@
 endocervical cells, or atypical endometrial cells on cytology.
 R87.810 Cervical high-risk HPV DNA test positive
-[[page 29]]
-ben fam rel
-29
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 30]]
+ben fam rel
+30
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Other Conditions
 Cervical Abnormalities Other Conditions Codes Table
@@ -972,9 +991,9 @@
 ICD-10-CM Code Description
 N88.0 Leukoplakia of cervix uteri
-[[page 30]]
-ben fam rel
-30
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 31]]
+ben fam rel
+31
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Procedures
 A modifier is required for the following procedures.
@@ -1010,9 +1029,9 @@
 CIN 3, or persistent CIN 1 lesions of
 greater than 24 months
-[[page 31]]
-ben fam rel
-31
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 32]]
+ben fam rel
+32
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Cervical Abnormalities Procedure Codes Table (continued)
 CPT Code Description Restrictions
@@ -1050,9 +1069,9 @@
 Drugs
 None
-[[page 32]]
-ben fam rel
-32
-Family PACT – Benefits: Family Planning-Related Services
-Page updated January 2026
+[[page 33]]
+ben fam rel
+33
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Additional Laboratory Tests
 Cervical Abnormalities Additional Laboratory Test Codes Table
@@ -1061,21 +1080,21 @@
 types (e.g., 16, 18, 31, 33, 35, 39, 45,
 51, 52, 56, 58, 59, 68)
-‹‹Additional ICD-10-CM code is
+Additional ICD-10-CM code is
 required when applicable. Refer to
 Laboratory (lab) section of the Family
 PACT Policies, Procedures and
-Billing Instructions (PPBI) Manual.‡››
+Billing Instructions (PPBI) Manual.‡
 87625 Human papillomavirus (HPV), types 16
 and 18 only, includes type 45, if
 performed.
-‹‹Additional ICD-10-CM code is
+Additional ICD-10-CM code is
 required when applicable. Refer to
-Laboratory (lab) section of PPBI.‡››
-‹‹87626 Detection test by nucleic acid for
+Laboratory (lab) section of PPBI.‡
+87626 Detection test by nucleic acid for
 Human Papillomavirus (HPV),
 separately reported high-risk types
 Additional ICD-10-CM code is
 required when applicable. Refer to
-Laboratory (lab) section of PPBI.‡››
+Laboratory (lab) section of PPBI.‡
 88141 Cytopathology, cervical or vaginal
 (any reporting system), requiring
@@ -1110,9 +1129,9 @@
 • As an adjunct to morphologic for biopsy specimens interpreted as less than or equal to
 CIN 1 that are high risk for missed high-grade disease.
-[[page 33]]
-ben fam rel
-33
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 34]]
+ben fam rel
+34
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Complications of Family Planning-Related Services
 Management of Complications for Family Planning-Related Services
@@ -1130,8 +1149,8 @@
 99252 thru 99255 Inpatient consultation, new or established patient
 Pharmacy
-Only drugs listed in the Family PACT Pharmacy Formulary on the Medi-Cal Rx website
-(https://medi-calrx.dhcs.ca.gov) and in the Clinic Formulary section in this manual, which are
-needed for treatment of complications arising from a family planning-related reproductive
-health condition, may be reimbursed.
+Only drugs listed in the Family PACT Pharmacy Formulary on the Medi-Cal Rx website and
+in the Clinic Formulary section in this manual, which are needed for treatment of
+complications arising from a family planning-related reproductive health condition, may be
+reimbursed.
 Additional Complications
 The following additional complications relate to the treatment of cervical abnormalities or
@@ -1143,9 +1162,9 @@
 N99.61 Intraoperative hemorrhage or hematoma of a genitourinary system organ
 or structure complicating a genitourinary system procedure
-[[page 34]]
-ben fam rel
-34
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: May 2023
+[[page 35]]
+ben fam rel
+35
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 The following procedures are reimbursable only for the management of complications from
 treatment of cervical abnormalities and preinvasive lesions:
@@ -1167,11 +1186,11 @@
 Antibiotic regimens are the same as for treatment of uncomplicated PID, as listed in the
 “Treatment and Dispensing Guidelines for Clinicians” in the Benefits Grid section. Providers
-may also refer to the Family PACT Pharmacy Formulary on the Medi-Cal Rx website
-(https://medi-calrx.dhcs.ca.gov) as well as the Clinic Formulary section in this manual.
-[[page 35]]
-ben fam rel
-35
-Family PACT – Benefits: Family Planning-Related Services
-Page updated: January 2026
+may also refer to the Family PACT Pharmacy Formulary on the Medi-Cal Rx website as well
+as the Clinic Formulary section in this manual.
+[[page 36]]
+ben fam rel
+36
+Family PACT – Benefits: Family Planning-Related Services
+Page updated: August 2026
 Legend
 Symbols used in the document above are explained in the following table.
@@ -1183,8 +1202,8 @@
 * Appropriate CLIA certification required. Refer to the Part 2 manual, Pathology:
 An Overview of Enrollment and Proficiency Testing Requirements section.
-‡ ‹‹Coverage for HPV testing and co-testing are based on the 2019 ASCCP
+‡ Coverage for HPV testing and co-testing are based on the 2019 ASCCP
 Risk-Based Management Consensus Guidelines for Abnormal Cervical
 Cancer Screening Test and Cancer Precursors and the USPSTF 2018 Final
-Recommendation Statement for Cervical Cancer Screening.››
+Recommendation Statement for Cervical Cancer Screening.
 ** Per ASCCP, expedited treatment (excisional treatment without prior
 confirmatory biopsy, e.g., “see and treat” LEEP) is preferred for non-pregnant
```
