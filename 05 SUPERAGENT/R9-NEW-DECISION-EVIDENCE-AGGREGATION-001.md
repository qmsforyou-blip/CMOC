# R9 — NEW DECISION EVIDENCE AGGREGATION

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Date:** 22-09-2026

## 1. Purpose

R9 defines the minimum aggregate evidence package that may be passed from Semantic Distinction into the separate NEW DECISION stage.

R9 does not decide NEW.

## 2. Architectural position

SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → QUERY → RELEVANT_COMPARISON_SET → SEMANTIC_COMPARISON → SEMANTIC_DISTINCTION → NEW_DECISION → CANONIZATION → CMOC WRITE

R9 is the controlled bridge:

SEMANTIC_DISTINCTION → NEW_DECISION_INPUT

## 3. Core rule

A semantic distinction is evidence for a NEW decision, not the NEW decision itself.

Therefore:

SEMANTIC_DISTINCTION ≠ NEW_APPROVED

## 4. Minimum NEW_DECISION_INPUT

new_decision_input:
  candidate:
    record_id:
    value:
    object_boundary:
  reconciliation:
    match_result:
    basis:
    cmoc_object_id:
  query_evidence:
    query_scope:
    modes:
      exact:
      alias:
      structural:
    results:
  comparison_set:
    completeness_state:
    object_ids:
  semantic_distinction:
    positive_distinctions:
    unresolved_dimensions:
    covered_dimensions:
    not_applicable_dimensions:
    evidence_state:
  target_object_type:
  traceability:
  decision_context:

R9 must preserve the evidence; it must not invent missing fields.

## 5. Minimum evidence conditions

For an input to be eligible for NEW DECISION, the package must preserve:

- source-bound candidate identity;
- stable object boundary;
- complete traceability;
- sufficient query scope;
- explicit query evidence;
- semantic comparison evidence;
- positive semantic distinction evidence;
- resolved target object type;
- explicit decision context.

The precise eligibility predicate remains the responsibility of the NEW DECISION contract.

## 6. Evidence states

Evidence states remain:

- TRUE
- FALSE
- UNKNOWN
- NOT_APPLICABLE

UNKNOWN must never be silently converted to TRUE.

## 7. Comparison-set completeness

R9 must preserve:

- COMPLETE;
- PARTIAL;
- UNKNOWN.

UNKNOWN comparison-set completeness is not sufficient for automatic NEW approval.

PARTIAL must remain explicit. It must not be rewritten as COMPLETE.

## 8. Semantic distinction aggregation

R9 carries the R8 output forward.

It must preserve:

- every positive distinction;
- every unresolved dimension;
- every covered dimension;
- every not-applicable dimension;
- comparison targets;
- source evidence;
- traceability.

R9 must not collapse these into a single opaque score.

## 9. DISTINCT does not become NEW

The following transformations are prohibited:

DISTINCT → NEW

SEMANTIC_DISTINCTION → NEW_APPROVED

R9 only constructs the evidence package for the separate decision stage.

## 10. Partial evidence

A package with positive distinction but incomplete evidence is not automatically eligible.

Examples:

- missing source evidence;
- missing traceability;
- UNKNOWN target type;
- insufficient query scope;
- unresolved candidate;
- ambiguous comparison set.

Such states must remain visible.

## 11. Target object type

R9 may carry a resolved target object type supplied by an explicit mapping contract.

R9 must not infer target_object_type from working_class, wording, source type, or model intuition.

## 12. Decision context

The package must preserve why the NEW decision is being requested, without embedding the decision itself.

Example:

decision_context:
  requested_decision: NEW
  decision_rule_version:
  decision_run_id:

## 13. No mutation

R9 is read-only with respect to:

- CMOC;
- OBJECT INDEX;
- DISCOVERY RESULT.

It creates no object ID and performs no canonization.

## 14. Negative controls

The R9 test must cover at minimum:

1. complete evidence package;
2. positive distinction with UNKNOWN comparison completeness;
3. positive distinction with PARTIAL completeness;
4. missing source evidence;
5. missing traceability;
6. unknown target object type;
7. insufficient query scope;
8. unresolved candidate;
9. ambiguous comparison set;
10. multiple positive distinctions;
11. semantic distinction without NEW approval;
12. no CMOC write;
13. no object ID creation.

## 15. Boundary with R3

R3 NEW DECISION receives NEW_DECISION_INPUT only when the evidence gate permits it.

R9 does not replace R2.3.

R2.3 checks whether the package is eligible to enter NEW DECISION.

R3 makes the actual NEW_APPROVED / NEW_REJECTED decision.

## 16. Status

R9 is an architecture candidate.

No production NEW decision or CMOC mutation is established by this document.
