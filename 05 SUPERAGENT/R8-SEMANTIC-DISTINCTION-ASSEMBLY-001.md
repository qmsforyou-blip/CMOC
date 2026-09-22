# R8 — SEMANTIC DISTINCTION ASSEMBLY

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Date:** 22-09-2026

## 1. Purpose

R8 defines how dimension-level R7 comparison records are assembled into a controlled SEMANTIC_DISTINCTION evidence object.

R8 does not decide NEW and does not perform CMOC WRITE.

## 2. Architectural position

SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → QUERY → RELEVANT_COMPARISON_SET → SEMANTIC_COMPARISON → SEMANTIC_DISTINCTION → NEW_DECISION → CANONIZATION → CMOC WRITE

R8 answers:

> When do several dimension-level comparison results constitute a sufficiently explicit semantic distinction record?

## 3. Core rule

A single `DISTINCT` result is evidence of a distinction on one comparison dimension.

It is not automatically:

- semantic novelty of the whole candidate;
- NEW_APPROVED;
- a new CMOC object;
- a canonization decision.

## 4. Input

semantic_distinction_assembly_input:
  candidate:
    record_id:
    value:
    object_boundary:
  comparison_set:
    completeness_state:
  comparisons:
    - candidate_id:
      existing_object_id:
      comparison_dimension:
      candidate_value:
      existing_value:
      comparison_status:
      distinction:
      basis:
      source_evidence:
      traceability:
  traceability:

R8 must not invent missing comparison records or evidence.

## 5. Output

semantic_distinction:
  candidate_id:
  compared_object_ids:
  dimensions:
    Entity:
    Property:
    Relation:
    Mechanism:
    Capability:
  distinction_status:
  positive_distinctions:
  unresolved_dimensions:
  covered_dimensions:
  not_applicable_dimensions:
  evidence_state:
  basis:
  traceability:

## 6. Dimension preservation

R8 must preserve the result for every supplied comparison dimension.

Example:

Entity → COVERED  
Property → DISTINCT  
Relation → COVERED  
Mechanism → UNRESOLVED  
Capability → NOT_APPLICABLE

must not be reduced to a single opaque "different" label.

## 7. Positive distinction

A dimension may contribute to positive semantic distinction only when:

- comparison_status = DISTINCT;
- distinction is explicit;
- basis is present;
- source_evidence is present;
- traceability is present.

Therefore:

DISTINCT + missing evidence ≠ valid positive distinction.

## 8. Aggregation rule

R8 may assemble one or more valid dimension-level DISTINCT results into a SEMANTIC_DISTINCTION evidence object.

It must not require every dimension to be DISTINCT.

It must also not treat COVERED or NOT_APPLICABLE as negative evidence against a distinction established on another dimension.

## 9. UNRESOLVED rule

UNRESOLVED dimensions remain explicitly unresolved.

They are not converted into COVERED, DISTINCT, or NOT_APPLICABLE.

If a distinction is assembled while another dimension remains UNRESOLVED, the unresolved state must remain visible in the output.

## 10. UNKNOWN comparison-set completeness

If comparison_set completeness is UNKNOWN, R8 must not produce a positive semantic-distinction evidence state suitable for automatic NEW approval.

The individual R7 comparison records may still be preserved, but the assembly evidence state must reflect the incomplete comparison area.

## 11. PARTIAL comparison-set completeness

PARTIAL does not automatically invalidate a supported pairwise distinction.

The resulting SEMANTIC_DISTINCTION must preserve the PARTIAL evidence state so that downstream NEW DECISION can account for it.

## 12. No DISTINCT evidence

If all supplied dimensions are:

- COVERED;
- UNRESOLVED;
- NOT_APPLICABLE;

then no positive semantic distinction is assembled.

The output must not manufacture novelty from absence of DISTINCT.

## 13. Multiple DISTINCT dimensions

Multiple valid DISTINCT results may be assembled into one SEMANTIC_DISTINCTION evidence object.

Each distinction remains dimension-specific and traceable.

## 14. Multiple existing objects

Where the candidate was compared with multiple existing objects, R8 preserves the compared object IDs and the corresponding dimension-level evidence.

It must not collapse different comparison targets into an unexplained aggregate.

## 15. Negative controls

The R8 test must cover at minimum:

1. one valid DISTINCT + remaining COVERED;
2. DISTINCT + UNRESOLVED;
3. only COVERED;
4. all UNRESOLVED;
5. multiple DISTINCT dimensions;
6. NOT_APPLICABLE;
7. UNKNOWN comparison-set completeness;
8. DISTINCT without source evidence;
9. DISTINCT without traceability;
10. DISTINCT does not produce NEW_APPROVED;
11. no CMOC write;
12. OBJECT INDEX unchanged;
13. DISCOVERY RESULT unchanged.

## 16. Boundary with R4/R5/R7/R3

R7 produces dimension-level comparison evidence.

R8 assembles those records into explicit SEMANTIC_DISTINCTION evidence.

R5 defines the structure and meaning of positive semantic distinction.

R4 requires positive semantic distinction as part of semantic NEW evidence.

R3 makes the separate NEW decision.

Therefore:

R7 DISTINCT → R8 SEMANTIC_DISTINCTION → R4 NEW evidence → R3 NEW DECISION

and never:

R7 DISTINCT → NEW_APPROVED.

## 17. Status

R8 is an architecture candidate.

No production semantic-distinction assembler, novelty engine, canonization, or CMOC write is established by this document.
