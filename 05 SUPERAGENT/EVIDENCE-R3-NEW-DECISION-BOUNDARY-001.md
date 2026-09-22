# EVIDENCE-R3 — NEW DECISION BOUNDARY

**Status:** ACCEPTED  
**Gate:** R3-NEW-DECISION-BOUNDARY  
**Date:** 22-09-2026

## 1. Purpose

R3 verifies the contract boundary for a separate NEW DECISION stage after Reconciliation.

The test does not claim that production semantic novelty detection exists. It verifies the controlled transition from an evidence-eligible candidate to a synthetic NEW decision result, while preserving the boundary to Canonization and CMOC WRITE.

## 2. Architectural sequence

`SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE`

The governing principle remains:

> **Сначала добываем. Потом сопоставляем. Затем отдельно принимаем решение о NEW.**

DISCOVERY remains independent of CMOC/QUERY.

RECONCILIATION consumes already extracted knowledge and compares it with accumulated CMOC through the configured query boundary.

NEW DECISION is a separate decision boundary.

## 3. Executable test

Test:

`05 SUPERAGENT/test_r3_new_decision.py`

Local execution:

`py "05 SUPERAGENT\\test_r3_new_decision.py"`

Result:

`PASS`

## 4. Branch results

| Branch | Expected | Actual | Result |
|---|---|---|---|
| COMPLETE_ELIGIBLE | NEW_APPROVED | NEW_APPROVED | PASS |
| INSUFFICIENT_SCOPE | NEW_REJECTED | NEW_REJECTED | PASS |
| UNKNOWN_TARGET_TYPE | NEW_REJECTED | NEW_REJECTED | PASS |
| UNRESOLVED_CANDIDATE | NEW_REJECTED | NEW_REJECTED | PASS |
| AMBIGUOUS | NEW_REJECTED | NEW_REJECTED | PASS |
| ELIGIBLE_BUT_UNKNOWN_EVIDENCE | NEW_REJECTED | NEW_REJECTED | PASS |

All six branch inputs remained unchanged during evaluation.

## 5. Controlled invariants

The executed test confirmed:

- `cmoc_write = NONE`
- no `object_id` created;
- canonization not executed;
- no relations created;
- OBJECT INDEX unchanged;
- DISCOVERY RESULT unchanged;
- production runtime not imported;
- production runtime import is explicitly blocked by test design;
- an approved synthetic result does not write to CMOC;
- a rejected synthetic result does not write to CMOC.

## 6. Decision boundary

The R3 test establishes the following controlled distinction:

`ELIGIBLE_FOR_NEW_DECISION` → decision stage

does not mean:

`ELIGIBLE_FOR_NEW_DECISION` → automatic CMOC write.

The tested decision outputs are:

- `NEW_APPROVED`
- `NEW_REJECTED`

They remain separate from:

- `CANONIZATION`
- `CMOC WRITE`

## 7. Important evidence limitation

The `NEW_APPROVED` branch uses a fully evidenced synthetic fixture.

Therefore R3 proves the **decision boundary and control behavior**, not semantic novelty in production.

R3 does not prove:

- that a candidate is semantically novel;
- that an LLM can reliably determine novelty;
- a production novelty algorithm;
- a scoring threshold;
- automatic approval policy;
- canonization;
- CMOC mutation.

## 8. Architectural conclusion

R3 confirms that the architecture can preserve the separation:

### DISCOVERY
What engineering knowledge was extracted from SOURCE?

### RECONCILIATION
How does the extracted result relate to accumulated CMOC?

### NEW DECISION
Are the available grounds sufficient to make a separate NEW decision?

### CANONIZATION
How is approved new knowledge represented canonically?

### CMOC WRITE
How is the approved canonical result written into accumulated knowledge?

The boundaries are explicit and tested.

## 9. Status

R3 is **ACCEPTED as evidence of the NEW DECISION boundary**.

It is not evidence that a production NEW DECISION machine has been implemented.

Next architectural step: define the evidence and decision criteria for genuine semantic NEW, without weakening the established DISCOVERY → RECONCILIATION boundary.
