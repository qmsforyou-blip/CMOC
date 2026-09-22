# R10 — NEW DECISION RULE

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Date:** 22-09-2026

## 1. Purpose

R10 defines the separate decision rule that consumes an eligible NEW_DECISION_INPUT and produces either NEW_APPROVED or NEW_REJECTED.

R10 does not canonize the candidate and does not write to CMOC.

## 2. Architectural position

SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → QUERY → RELEVANT_COMPARISON_SET → SEMANTIC_COMPARISON → SEMANTIC_DISTINCTION → NEW_DECISION_INPUT → NEW DECISION → CANONIZATION → CMOC WRITE

R10 is the decision boundary between evidence and a NEW decision.

## 3. Core separation

The following are distinct states:

NO_MATCH
NEEDS_REVIEW
SEMANTIC_DISTINCTION
ELIGIBLE_FOR_NEW_DECISION
NEW_APPROVED
NEW_REJECTED
CANONIZED
CMOC_WRITTEN

No earlier state may be silently promoted to a later state.

## 4. Entry condition

R10 accepts only a NEW_DECISION_INPUT that satisfies the evidence gate defined by R2.3/R9.

If the input is not eligible, R10 returns:

`NEW_REJECTED`

with basis:

`candidate is not eligible for NEW DECISION`

R10 must not repair missing evidence itself.

## 5. Decision principle

R10 may approve NEW only when the supplied evidence supports all required decision conditions.

Minimum conditions:

- candidate identity is stable;
- object boundary is stable;
- source provenance is complete;
- query scope is sufficient;
- relevant comparison evidence is preserved;
- no unresolved ambiguity remains;
- semantic distinction is positively evidenced;
- target object type is resolved;
- decision context is explicit.

The exact production rule may later be versioned, but it must remain explicit and testable.

## 6. Positive semantic distinction

R10 may use R8 SEMANTIC_DISTINCTION evidence.

However:

SEMANTIC_DISTINCTION ≠ automatic NEW_APPROVED.

The decision rule must evaluate the complete NEW_DECISION_INPUT.

## 7. Rejection conditions

R10 must return NEW_REJECTED when any mandatory NEW condition is not satisfied.

Examples:

- insufficient query scope;
- UNKNOWN comparison completeness;
- unresolved candidate;
- ambiguity;
- missing source evidence;
- missing traceability;
- unresolved target object type;
- no positive semantic distinction;
- incomplete decision context.

## 8. Multiple distinctions

Multiple valid distinctions may strengthen the evidence package but do not create a separate decision class.

R10 must not use the number of DISTINCT results as an implicit novelty score.

## 9. Partial evidence

PARTIAL evidence must not be silently promoted to COMPLETE.

Unless an explicit future decision rule states otherwise, PARTIAL comparison evidence is insufficient for automatic NEW_APPROVED.

## 10. UNKNOWN

UNKNOWN is not TRUE.

If a mandatory decision condition is UNKNOWN, R10 cannot approve NEW automatically.

## 11. Decision output

Minimum output:

new_decision:
  decision_id:
  candidate_id:
  decision:
    NEW_APPROVED | NEW_REJECTED
  basis:
  evidence_summary:
  rule_version:
  traceability:

The decision record must preserve the evidence used for the decision.

## 12. No object creation

NEW_APPROVED does not create an object ID.

It means only:

> the candidate has passed the current NEW decision rule.

The subsequent CANONIZATION stage is responsible for transforming the approved candidate into a canonical CMOC representation.

## 13. No canonization

R10 must not:

- assign canonical object identity;
- modify object names;
- merge representations;
- create relations;
- update OBJECT INDEX;
- write to CMOC.

## 14. No mutation

R10 is read-only with respect to:

- CMOC;
- OBJECT INDEX;
- DISCOVERY RESULT;
- NEW_DECISION_INPUT.

## 15. Negative controls

The executable R10 test must cover at minimum:

1. complete eligible input → NEW_APPROVED;
2. ineligible input → NEW_REJECTED;
3. no positive semantic distinction → NEW_REJECTED;
4. UNKNOWN mandatory evidence → NEW_REJECTED;
5. unresolved candidate → NEW_REJECTED;
6. ambiguous evidence → NEW_REJECTED;
7. unknown target type → NEW_REJECTED;
8. partial comparison evidence → NEW_REJECTED;
9. multiple positive distinctions → NEW_APPROVED;
10. NEW_APPROVED does not create object ID;
11. NEW_APPROVED does not canonize;
12. NEW_APPROVED does not write CMOC;
13. NEW_REJECTED does not write CMOC.

## 16. Rule versioning

Every R10 decision must identify the rule version used.

A future change in the NEW rule must therefore produce a new rule version and new evidence.

## 17. Boundary with downstream stages

R10 output:

NEW_APPROVED
or
NEW_REJECTED

R10 does not decide:

- canonical representation;
- canonical object ID;
- CMOC insertion;
- relation creation.

Therefore:

NEW_APPROVED → CANONIZATION → CMOC WRITE

and not:

NEW_APPROVED → CMOC WRITE

## 18. Status

R10 is an architecture candidate.

The executable test will establish the decision boundary only. It will not establish production semantic novelty.
