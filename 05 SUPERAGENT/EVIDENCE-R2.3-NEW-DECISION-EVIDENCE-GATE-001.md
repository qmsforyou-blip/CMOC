# EVIDENCE-R2.3 — NEW DECISION EVIDENCE GATE

**Status:** ACCEPTED  
**Gate:** R2.3-NEW-DECISION-EVIDENCE-GATE  
**Date:** 22-09-2026

## 1. Purpose

R2.3 verifies the evidence gate defined for a separate NEW DECISION stage.

The test does **not** decide that a candidate is NEW. It verifies whether a candidate has sufficient evidence to be passed to a separate NEW DECISION mechanism.

The tested distinction is:

`ELIGIBLE_FOR_NEW_DECISION` ≠ `NEW_APPROVED`

## 2. Architectural boundary

The tested sequence is:

`SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE`

The R2.3 test is isolated from production DISCOVERY and RECONCILIATION runtime.

It does not import or execute production `reconciliation.py` or `cmoc_query.py`.

## 3. Test

Executable test:

`05 SUPERAGENT/test_r2_3_new_decision_evidence_gate.py`

Local execution:

`py "05 SUPERAGENT\\test_r2_3_new_decision_evidence_gate.py"`

Result:

`PASS`

## 4. Branch results

| Branch | Expected | Actual | Result |
|---|---|---|---|
| COMPLETE | ELIGIBLE_FOR_NEW_DECISION | ELIGIBLE_FOR_NEW_DECISION | PASS |
| INSUFFICIENT_SCOPE | NOT_ELIGIBLE | NOT_ELIGIBLE | PASS |
| UNKNOWN_TARGET_TYPE | NOT_ELIGIBLE | NOT_ELIGIBLE | PASS |
| UNRESOLVED_CANDIDATE | NOT_ELIGIBLE | NOT_ELIGIBLE | PASS |
| AMBIGUOUS | NOT_ELIGIBLE | NOT_ELIGIBLE | PASS |

All five branch inputs remained unchanged during evaluation.

## 5. Controlled invariants

The executed test confirmed:

- `cmoc_write = NONE`
- no `object_id` created
- `NEW_APPROVED = false`
- `NEW_REJECTED = false`
- canonization not executed
- production Reconciliation not imported
- OBJECT INDEX unchanged
- DISCOVERY RESULT unchanged
- UNKNOWN was not promoted to TRUE
- `ELIGIBLE_FOR_NEW_DECISION` was not treated as `NEW_APPROVED`

## 6. Evidence gate

The tested eligibility condition is:

`source_bound_candidate`
AND `traceability_complete`
AND `query_scope_sufficient`
AND `exact_checked`
AND `alias_checked`
AND `structural_checked_or_NA`
AND `no_ambiguity`
AND `no_unresolved_candidate`
AND `stable_object_boundary`
AND `target_object_type_resolved`

Any failed condition prevents eligibility.

`UNKNOWN` is not promoted to `TRUE`.

## 7. What R2.3 proves

R2.3 proves that a separate NEW DECISION stage can have an explicit evidence gate with deterministic negative branches.

It establishes a controlled architectural boundary between:

- reconciliation result;
- evidence sufficiency for NEW decision;
- actual NEW approval/rejection;
- canonization;
- CMOC write.

## 8. What R2.3 does not prove

R2.3 does **not** prove:

- automatic `NEW_APPROVED`;
- automatic `NEW_REJECTED`;
- semantic novelty;
- canonization;
- CMOC mutation;
- production integration of a NEW DECISION machine;
- correctness of NEW decisions on arbitrary real sources.

These remain separate future work.

## 9. Architectural conclusion

The current architecture preserves the governing principle:

> **Сначала добываем. Потом сопоставляем.**

More precisely:

> **DISCOVERY independently extracts engineering knowledge from SOURCE. RECONCILIATION compares the already extracted result with accumulated CMOC. NEW DECISION is a separate decision boundary and must not be silently embedded into either stage.**

R2.3 is therefore accepted as evidence for the NEW DECISION boundary, not as implementation of NEW itself.
