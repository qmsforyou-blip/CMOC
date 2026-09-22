# EVIDENCE-R4 — SEMANTIC NEW CRITERIA

**Status:** ACCEPTED  
**Gate:** R4-SEMANTIC-NEW-CRITERIA  
**Date:** 22-09-2026

## 1. Purpose

R4 verifies the minimum evidence predicate required before a separate NEW DECISION mechanism may produce `NEW_APPROVED` on semantic-new grounds.

The test uses synthetic fixtures only. It does not implement or claim a production semantic novelty engine.

## 2. Architectural position

`SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE`

The governing distinction is:

`NO_MATCH` ≠ `ELIGIBLE_FOR_NEW_DECISION` ≠ `NEW_APPROVED`

In particular:

> «Я не нашёл» ≠ «этого нет» ≠ «это новое».

R4 adds the positive-evidence requirement to the established boundary.

## 3. Executable test

Test:

`05 SUPERAGENT/test_r4_semantic_new_criteria.py`

Local execution:

`py "05 SUPERAGENT\\test_r4_semantic_new_criteria.py"`

Result:

`PASS`

## 4. Branch results

| Branch | Expected | Actual | Result |
|---|---|---|---|
| COMPLETE_WITH_POSITIVE_DISTINCTION | NEW_APPROVED | NEW_APPROVED | PASS |
| NO_MATCH_WITHOUT_POSITIVE_DISTINCTION | NOT_APPROVABLE | NOT_APPROVABLE | PASS |
| UNKNOWN_SEMANTIC_DISTINCTION | NOT_APPROVABLE | NOT_APPROVABLE | PASS |
| INSUFFICIENT_QUERY_SCOPE | NOT_APPROVABLE | NOT_APPROVABLE | PASS |
| UNRESOLVED_STRUCTURAL_CANDIDATE | NOT_APPROVABLE | NOT_APPROVABLE | PASS |
| AMBIGUOUS_CANDIDATE | NOT_APPROVABLE | NOT_APPROVABLE | PASS |
| UNKNOWN_DECISION_BASIS | NOT_APPROVABLE | NOT_APPROVABLE | PASS |

All seven branch inputs remained unchanged during evaluation.

## 5. R4 semantic evidence predicate

The synthetic `NEW_APPROVED` branch requires all of the following to be TRUE:

- candidate identity;
- stable object boundary;
- sufficient query scope;
- exact search checked;
- alias search checked or not applicable;
- structural search checked or not applicable;
- no ambiguity;
- no unresolved candidate;
- positive semantic distinction;
- complete provenance;
- complete decision basis.

UNKNOWN is not promoted to TRUE.

## 6. Critical positive-evidence control

The test explicitly proves:

`NO_MATCH` without `positive_semantic_distinction` → `NOT_APPROVABLE`

Therefore negative search evidence alone cannot establish semantic NEW.

The test also proves:

`UNKNOWN` semantic distinction → `NOT_APPROVABLE`

## 7. Controlled invariants

The executed test confirmed:

- `cmoc_write = NONE`;
- no object ID created;
- canonization not executed;
- no relations created;
- OBJECT INDEX unchanged;
- DISCOVERY RESULT unchanged;
- production runtime not imported;
- production runtime import blocked by test design;
- approved synthetic result does not write to CMOC;
- non-approvable result does not write to CMOC.

## 8. What R4 proves

R4 proves the contract-level distinction that semantic NEW requires positive evidence in addition to negative search evidence.

The candidate must have a defined and traceable semantic distinction that is not covered by the relevant accumulated knowledge, together with sufficient search and decision evidence.

## 9. What R4 does not prove

R4 does not prove:

- semantic novelty on real CMOC data;
- correctness of any LLM novelty assessment;
- similarity or embedding method;
- scoring or threshold policy;
- production NEW DECISION implementation;
- canonization;
- CMOC mutation.

## 10. Architectural conclusion

R4 establishes:

> **NEW is not the absence of an existing match. NEW requires a positive, traceable semantic distinction that is not covered by the relevant accumulated knowledge.**

This criterion is now executable at the contract level and remains isolated from production Discovery, Reconciliation, QUERY, OBJECT INDEX, and CMOC WRITE.

## 11. Status

R4 is **ACCEPTED as evidence of the semantic NEW criteria boundary**.

The next architectural question is how to establish and compare the positive semantic distinction without weakening the existing DISCOVERY → RECONCILIATION separation.
