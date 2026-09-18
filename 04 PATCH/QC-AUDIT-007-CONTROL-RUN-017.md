# QC-AUDIT-007 — CONTROL-RUN-017 — TASK SWAP

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)

## Audit target

`CONTROL-RUN-017-TASK-SWAP-SRC-002-M02.md`

## Checks

| Check | Result |
|---|---|
| Same SOURCE retained | PASS — SRC-002 |
| Same MACHINE retained | PASS — MACHINE-SOURCE-001 |
| TASK explicitly changed | PASS — M02 |
| M02 direct SOURCE_PACKAGE route allowed by contract | PASS |
| New BATCH_ID | PASS |
| Previous M01 output excluded as operational input | PASS |
| Source-grounded M02 execution | PASS |
| Distinction records produced | PASS |
| Traceability retained | PASS |
| Content qualification preserved | PASS |
| Source-specific machine modification absent | PASS |

## Final status

**PASS WITH CONTENT QC NOTE**

The test supports the invariant:

`MACHINE ≠ TASK`

and the operational behavior:

`SAME MACHINE + SAME SOURCE + DIFFERENT TASK → TASK-SPECIFIC OUTPUT`

## Architectural consequence

TASK is confirmed as an explicit production parameter rather than a hidden property of MACHINE for the tested M02 direct-source route.

## Evidence boundary

The result is evidence for the tested M02 route only. It does not establish universal direct-source compatibility or semantic applicability of all TASKs.
