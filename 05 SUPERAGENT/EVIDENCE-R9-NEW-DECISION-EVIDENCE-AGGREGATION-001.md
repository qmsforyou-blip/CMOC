# EVIDENCE-R9 — NEW DECISION EVIDENCE AGGREGATION

**Status:** ACCEPTED  
**Gate:** R9-NEW-DECISION-EVIDENCE-AGGREGATION  
**Date:** 22-09-2026

## 1. Result

The R9 executable synthetic boundary test returned:

`PASS`

All eleven branches passed.

## 2. Verified branches

- COMPLETE_EVIDENCE → `ELIGIBLE_FOR_NEW_DECISION`
- UNKNOWN_COMPARISON_COMPLETENESS → `NOT_ELIGIBLE`
- PARTIAL_COMPARISON_COMPLETENESS → `NOT_ELIGIBLE`
- MISSING_SOURCE_EVIDENCE → `NOT_ELIGIBLE`
- MISSING_TRACEABILITY → `NOT_ELIGIBLE`
- UNKNOWN_TARGET_TYPE → `NOT_ELIGIBLE`
- INSUFFICIENT_QUERY_SCOPE → `NOT_ELIGIBLE`
- UNRESOLVED_CANDIDATE → `NOT_ELIGIBLE`
- AMBIGUOUS_COMPARISON_SET → `NOT_ELIGIBLE`
- MULTIPLE_POSITIVE_DISTINCTIONS → `ELIGIBLE_FOR_NEW_DECISION`
- ELIGIBLE_IS_NOT_NEW_APPROVED → confirmed

## 3. Architectural boundary

R9 establishes the controlled bridge:

`SEMANTIC_DISTINCTION → NEW_DECISION_INPUT`

It does not make the NEW decision.

The following separation is preserved:

`ELIGIBLE_FOR_NEW_DECISION ≠ NEW_APPROVED`

## 4. Evidence requirements preserved

The tested aggregation requires, at minimum:

- source-bound candidate;
- stable object boundary;
- complete traceability;
- sufficient query scope;
- semantic distinction evidence;
- resolved target object type;
- source evidence;
- no unresolved candidate;
- no ambiguity;
- sufficient comparison-set evidence.

UNKNOWN and missing evidence remain explicit failures of eligibility.

## 5. Completeness boundary

The test confirms:

- COMPLETE comparison evidence may produce `ELIGIBLE_FOR_NEW_DECISION`;
- UNKNOWN comparison completeness produces `NOT_ELIGIBLE`;
- PARTIAL comparison completeness produces `NOT_ELIGIBLE`.

The R9 test therefore preserves the conservative boundary that the current evidence package must be complete enough before entering the separate NEW DECISION stage.

## 6. Multiple distinctions

Multiple positive semantic distinctions do not create a different decision class.

They remain evidence inside the same `NEW_DECISION_INPUT`.

## 7. Controlled invariants

The executed test confirmed:

- OBJECT INDEX unchanged;
- DISCOVERY RESULT unchanged;
- CMOC WRITE = NONE;
- object ID not created;
- canonization not performed;
- NEW_APPROVED = false;
- production runtime not imported;
- production runtime import blocked.

## 8. Evidence boundary

R9 is a synthetic evidence-aggregation test.

It does not establish:

- production NEW decision;
- semantic novelty in production;
- NEW_APPROVED;
- NEW_REJECTED;
- canonization;
- CMOC mutation;
- correctness of an LLM implementation.

## 9. Architectural chain

The current controlled chain is:

SOURCE
→ DISCOVERY
→ DISCOVERY_RESULT
→ RECONCILIATION
→ QUERY
→ RELEVANT_COMPARISON_SET
→ SEMANTIC_COMPARISON
→ SEMANTIC_DISTINCTION
→ NEW_DECISION_INPUT
→ NEW_DECISION
→ CANONIZATION
→ CMOC WRITE

## 10. Status

R9 is **ACCEPTED as evidence of the NEW DECISION evidence-aggregation boundary**.

The next task is the separate NEW DECISION rule itself: define what evidence is sufficient for `NEW_APPROVED` versus `NEW_REJECTED`, while preserving the prohibition on automatic CMOC mutation.
