# QC-AUDIT-008 — CONTROL-RUN-018 — COMBINED SOURCE + TASK SWAP

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)

## Audit target

`CONTROL-RUN-018-COMBINED-SOURCE-TASK-SWAP-SRC-003-M02.md`

## Checks

| Check | Result |
|---|---|
| MACHINE unchanged | PASS |
| SOURCE explicitly bound | PASS — SRC-003 |
| TASK explicitly bound | PASS — M02 |
| Direct SOURCE_PACKAGE → M02 contract | PASS |
| New BATCH_ID | PASS |
| Hidden previous output excluded | PASS |
| 20 source locations processed | PASS |
| 20 Distinction Records produced | PASS |
| Traceability retained | PASS |
| Machine modification absent | PASS |

## Final status

**PASS**

The combined test supports:

`MACHINE + SOURCE + TASK → BATCH → OUTPUT`

with SOURCE and TASK remaining explicit external parameters of the machine.

## Evidence boundary

This is evidence for the tested M02 direct-source route. It does not establish universal compatibility across all source/task combinations or automatic execution of M04–M08.
