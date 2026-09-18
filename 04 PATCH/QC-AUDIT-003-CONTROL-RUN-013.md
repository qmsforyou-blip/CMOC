# QC-AUDIT-003 — CONTROL-RUN-013 — CONTRACT REJECT

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)

## Audit target

`CONTROL-RUN-013-CONTRACT-REJECT-SRC-002-M02-M04.md`

## Checks

| Check | Result |
|---|---|
| Explicit M02 output supplied as handoff | PASS |
| Actual input type identified | PASS — Distinction Records |
| M04 required input identified | PASS — Formulation Records |
| Type compatibility check performed | PASS |
| CONTRACT_MISMATCH detected | PASS |
| Explicit rejection reason | PASS |
| M04 execution blocked | PASS |
| No silent M03 invocation | PASS |
| No fabricated M04 output | PASS |
| No M04 BATCH created | PASS |
| Traceability preserved | PASS |

## Final status

**PASS**

The negative test confirms the INV-002 rule for the tested transition:

`OUTPUT₁ + HANDOFF → CONTRACT CHECK → ACCEPT / REJECT`

For M02→M04 in this run the result is **REJECT**.

## Evidence boundary

Established for the tested M02→M04 transition only. This is not a universal proof for all possible contract violations.
