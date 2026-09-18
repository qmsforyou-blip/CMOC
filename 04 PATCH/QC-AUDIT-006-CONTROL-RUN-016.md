# QC-AUDIT-006 — CONTROL-RUN-016 — SOURCE SWAP

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)

## Audit target

`CONTROL-RUN-016-SOURCE-SWAP-SRC-003-M01.md`

## Checks

| Check | Result |
|---|---|
| Different SOURCE_ID declared | PASS — SRC-003 |
| SOURCE_PACKAGE declared | PASS |
| Same MACHINE retained | PASS — MACHINE-SOURCE-001 |
| Same TASK retained | PASS — M01 |
| New BATCH_ID | PASS |
| Previous SRC-003 outputs excluded as operational input | PASS |
| Source-grounded extraction performed | PASS |
| 20 source locations processed | PASS |
| 20 Extraction Records produced | PASS |
| Traceability retained | PASS |
| Source-specific machine modification absent | PASS |

## Final status

**PASS**

The test supports the invariant:

`MACHINE ≠ SOURCE`

and the operational behavior:

`SAME MACHINE + SAME TASK + DIFFERENT SOURCE → NEW OUTPUT`

## Architectural consequence

SOURCE is confirmed as a replaceable input parameter rather than a hidden component of MACHINE for the tested M01 route.

## Evidence boundary

The result is evidence for the tested M01 route only. It does not establish universal interchangeability across all TASKs or all SOURCE_PACKAGE types.
