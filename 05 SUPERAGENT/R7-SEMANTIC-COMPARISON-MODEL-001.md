# R7 — SEMANTIC COMPARISON MODEL

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Date:** 22-09-2026

## 1. Purpose

R7 defines the minimum controlled structure for comparing a candidate against a Relevant Comparison Set.

R7 does not decide NEW and does not perform CMOC WRITE.

## 2. Architectural position

SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → QUERY → RELEVANT_COMPARISON_SET → SEMANTIC_COMPARISON → SEMANTIC_DISTINCTION → NEW_DECISION → CANONIZATION → CMOC WRITE

R7 answers:

> What exactly is different, covered, unresolved, or not applicable when a candidate is compared with a selected existing object?

## 3. Core rule

A semantic comparison must be expressed as an explicit comparison record.

An LLM statement such as “this is new”, “this is similar”, or “these are equivalent” is not sufficient evidence by itself.

## 4. Minimum input

semantic_comparison_input:
  candidate:
    record_id:
    value:
    object_boundary:
  comparison_set:
    candidate_id:
    completeness_state:
    objects:
  traceability:

R7 must not silently expand the comparison set.

If comparison_set.completeness_state is UNKNOWN, the comparison result must not be promoted to a positive novelty conclusion.

## 5. Comparison coordinates

The controlled comparison dimensions are:

- Entity
- Property
- Relation
- Mechanism
- Capability

These are comparison coordinates, not automatic object types.

## 6. Minimum comparison record

semantic_comparison:
  candidate_id:
  existing_object_id:
  comparison_dimension:
  candidate_value:
  existing_value:
  comparison_status:
  distinction:
  basis:
  source_evidence:
  traceability:

## 7. Allowed comparison statuses

- DISTINCT
- COVERED
- UNRESOLVED
- NOT_APPLICABLE

Definitions:

### DISTINCT

A supported semantic difference is established for the specified comparison dimension.

### COVERED

The candidate content for the dimension is covered by the compared existing knowledge.

### UNRESOLVED

Available evidence is insufficient to establish either DISTINCT or COVERED.

### NOT_APPLICABLE

The dimension genuinely does not apply, with a recorded reason.

## 8. Positive distinction rule

DISTINCT is valid only when the comparison record contains supported evidence for the semantic difference.

The following are not sufficient:

- different wording;
- different source;
- different record ID;
- different file location;
- formatting differences;
- absence of an exact textual match;
- unsupported LLM assertion.

## 9. UNKNOWN rule

UNKNOWN evidence cannot be promoted to DISTINCT.

If evidence needed to establish a semantic difference is UNKNOWN, the result is UNRESOLVED unless another explicit supported basis establishes the distinction.

## 10. Multiple existing objects

One candidate may have multiple relevant existing objects.

R7 must preserve comparisons separately rather than collapsing them into one opaque judgment.

For example:

candidate C1
→ existing A
→ existing B
→ existing C

Each comparison remains independently traceable.

## 11. Dimension-local distinction

A candidate may be covered on one dimension and distinct on another.

Example:

Entity → COVERED  
Property → DISTINCT  
Relation → COVERED  
Mechanism → UNRESOLVED  
Capability → NOT_APPLICABLE

Therefore R7 must not reduce the comparison to a single similarity label.

## 12. LLM boundary

An LLM may assist in generating a proposed comparison, but the machine must preserve:

- which candidate was compared;
- which existing object was compared;
- which dimension was examined;
- candidate-side value;
- existing-side value;
- explicit distinction;
- evidence basis;
- source evidence;
- comparison status;
- traceability.

A bare model conclusion is not sufficient.

## 13. No NEW decision

R7 must not output:

- NEW_APPROVED;
- NEW_REJECTED;
- canonical object;
- new object ID;
- CMOC write.

R7 produces comparison evidence only.

## 14. No mutation

R7 is read-only with respect to:

- OBJECT INDEX;
- DISCOVERY RESULT;
- CMOC.

## 15. Negative controls

The future executable R7 test must cover at minimum:

1. DISTINCT on Entity;
2. DISTINCT on Property;
3. DISTINCT on Relation;
4. DISTINCT on Mechanism;
5. DISTINCT on Capability;
6. wording-only difference;
7. same meaning from a different source;
8. unsupported LLM assertion;
9. UNKNOWN evidence;
10. multiple existing objects;
11. dimension-local mixed results;
12. UNKNOWN comparison-set completeness;
13. no NEW_APPROVED;
14. no CMOC mutation.

## 16. Architectural principle

The intended separation is:

QUERY answers:

> What indexed knowledge is relevant to compare?

R7 answers:

> What semantic comparison can be explicitly evidenced?

R4/R5/R7 together establish:

NO_MATCH is not NEW.

Comparison-set membership is not equivalence.

Semantic distinction is not yet NEW approval.

NEW decision remains a separate controlled stage.

## 17. Status

R7 is an architecture candidate.

No production semantic comparison engine is established by this document.
