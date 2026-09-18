# QC-AUDIT-005 — CONTROL-RUN-015 — REJECT → REPAIR → RETRY

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)

## Audit target

`CONTROL-RUN-015-REJECT-REPAIR-RETRY-SRC-002-M03-M04.md`

## Checks

| Check | Result |
|---|---|
| Original rejection preserved | PASS |
| Original rejected handoff not rewritten | PASS |
| Repair represented as new artifact | PASS |
| Source identity retained | PASS |
| Provenance restored explicitly | PASS |
| New handoff declared | PASS |
| Type check after repair | PASS |
| Structural contract check after repair | PASS |
| M04 execution only after ACCEPT | PASS |
| New M04 BATCH_ID created | PASS |
| Retry output separately identified | PASS |
| No historical mutation | PASS |

## Final status

**PASS**

The test establishes that a rejected handoff can re-enter production through an explicit repair artifact and a new downstream BATCH.

The repair itself is **not automatic**. It is an explicit production input.

## Architectural consequence

The production lifecycle now includes a controlled recovery path:

`EXECUTE → REJECT → REPAIR → NEW HANDOFF → CONTRACT CHECK → ACCEPT → RETRY`

This preserves append-only history while allowing production to continue.

## Evidence boundary

Established for the tested M03→M04 structural defect.

Not established:
- automatic defect diagnosis;
- automatic repair generation;
- recovery from arbitrary defect classes.
