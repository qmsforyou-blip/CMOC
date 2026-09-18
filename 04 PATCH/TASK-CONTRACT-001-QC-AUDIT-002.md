# TASK-CONTRACT-001 — Audit after Clean Direct Runs 006/007

**Date:** 18-09-2026
**Audit status:** PASS WITH CONTRACT UPDATE REQUIRED
**Basis:** clean direct SOURCE_PACKAGE tests for M02 and M03 on SRC-003.

## 1. M02 direct SOURCE_PACKAGE

Run-006 used SOURCE_PACKAGE itself as the declared operational input.

- BATCH_ID: BATCH-SRC-003-004
- TASK: DISTINCTIONS
- Output: 20 distinctions
- Existing M01/M02 artifacts: not used operationally
- External knowledge: none
- Downstream synthesis: none
- Direct source traceability: PASS

**Evidence status: TESTED.**

## 2. M03 direct SOURCE_PACKAGE

Run-007 used SOURCE_PACKAGE itself as the declared operational input.

- BATCH_ID: BATCH-SRC-003-005
- TASK: FORMULATIONS
- Input: 20 source observations read directly from SOURCE_PACKAGE
- Output: 60 formulations
- Cardinality: 20 × 3 = 60
- Existing M01/M02/M03 artifacts: not used operationally
- External knowledge: none
- Downstream synthesis: none
- Direct source traceability: PASS

**Evidence status: TESTED.**

## 3. Correction of Audit-001

The two previously unproven paths are now experimentally established for SRC-003:

| TASK | Direct SOURCE_PACKAGE | Evidence status |
|---|---|---|
| M01 | YES | TESTED |
| M02 | YES | TESTED — Run-006 |
| M03 | YES | TESTED — Run-007 |
| M04 | NO | TESTED via formulations |
| M05 | NO | TESTED via nomenclature |
| M06 | NO | TESTED via classification |
| M07 | NO | TESTED via passports |
| M08 | NO | TESTED via passport/relation evidence |

## 4. Important scope limitation

These tests establish direct SOURCE_PACKAGE operation for M02 and M03 on SRC-003.

They do **not** establish universal semantic validity for every source type, every source package, or every TASK.

The contract should therefore distinguish:

1. **interface capability tested**;
2. **source/task semantic validity**, which remains subject to source-specific execution and QC.

## 5. Required contract change

TASK-CONTRACT-001 v0.1 can be promoted from the earlier “candidate because M02/M03 were unproven” state to a revised candidate contract v0.2 in which M02 and M03 direct SOURCE_PACKAGE paths are marked TESTED.

The contract remains a candidate pending incorporation into STD-008.

## 6. QC conclusion

**PASS.**

The specific defect identified in Audit-001 has been experimentally closed.

The distinction remains mandatory:

> “Previous TASK output is not used” ≠ “SOURCE_PACKAGE is the direct operational input”.

Run-006 and Run-007 now satisfy the second condition.
