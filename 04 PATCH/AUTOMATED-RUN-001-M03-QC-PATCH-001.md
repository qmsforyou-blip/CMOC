# AUTOMATED-RUN-001 — QC PATCH after M03

**18-09-2026**

## Finding

M03 artifact contains `CLASSIFICATION_HINT` fields. This is a stage-boundary violation.

M03 contract requires:
- input: Distinction Records;
- output: three Formulation Records per distinction;
- no conversion of formulation into CMOC classification;
- no hidden preparation of M04/M05 results.

Although the field is labelled as a hint and does not alter the 40→120 cardinality, it introduces information belonging to the later classification stage into the M03 output.

## Decision

The previously recorded M03 PASS is **withdrawn as a semantic-boundary PASS**.

This is not a failure of the source extraction. It is a defect in the automated pilot artifact generation.

Per CMOC principle: do not repair the test result; repair the technology that produced the ambiguity/leakage.

## Required correction

Re-run M03 from the existing M02 output with:
- exactly 3 formulations per distinction;
- no CLASSIFICATION_HINT;
- no classification, passport, relation or canon fields;
- full trace Formulation → Distinction → Extraction → Batch → Source.

M01 and M02 remain unchanged and immutable.

## Status

- M01: PASS
- M02: PASS
- M03: RE-RUN REQUIRED
- M04–M06: NOT STARTED

