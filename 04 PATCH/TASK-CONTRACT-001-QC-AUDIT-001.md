# TASK-CONTRACT-001 — Audit after Run-004/005

**Date:** 18-09-2026  
**Audit status:** CORRECTION REQUIRED

## Finding 1 — M02 direct SOURCE_PACKAGE

The contract currently marks M02 as having a tested direct SOURCE_PACKAGE input.

The recorded Run-004 M02 artifact was constructed from the 20 observations in the existing M01 extraction artifact. Therefore it demonstrates:

SOURCE_PACKAGE → M01 EXTRACTION → M02 DISTINCTIONS

It does **not** constitute a controlled direct SOURCE_PACKAGE → M02 test.

## Finding 2 — M03 direct SOURCE_PACKAGE

The contract currently marks M03 as having a tested direct SOURCE_PACKAGE input.

The recorded Run-005 artifact uses the 20 source observations taken from the existing M01 extraction artifact. Therefore it demonstrates a TASK-independent route from the already extracted source observations, but it does **not** constitute a clean direct SOURCE_PACKAGE → M03 test.

The statement “Prior M03 formulations are not used” is true but insufficient to prove direct SOURCE_PACKAGE entry.

## Consequence

The earlier architectural conclusion was too strong.

What is established:

- the same SOURCE_PACKAGE can be associated with different TASK values;
- the fixed machine core was not changed;
- M02 and M03 can operate without consuming their own previous outputs;
- the tested runs preserve source traceability.

What is **not yet established**:

- direct SOURCE_PACKAGE → M02;
- direct SOURCE_PACKAGE → M03.

## Required correction

TASK-CONTRACT-001 should therefore be treated as a **candidate contract**, not yet normative.

Until a clean test is performed:

| TASK | Direct SOURCE_PACKAGE | Evidence status |
|---|---|---|
| M01 | YES | TESTED |
| M02 | YES | NOT PROVEN |
| M03 | YES | NOT PROVEN |
| M04 | NO | TESTED via formulations |
| M05 | NO | TESTED via nomenclature |
| M06 | NO | TESTED via classification |
| M07 | NO | TESTED via passports |
| M08 | NO | TESTED via passport/relation evidence |

## Required next experiment

Run M02 and M03 with SOURCE_PACKAGE itself as the declared input and without using the existing M01 extraction artifact as an operational input.

The outputs must retain direct SOURCE traceability.

Only after those tests should direct SOURCE_PACKAGE entry for M02/M03 be promoted from candidate to tested contract.

## Important distinction

“Previous TASK output is not used” ≠ “SOURCE_PACKAGE is the direct operational input”.

This distinction is now recorded as a QC correction.
