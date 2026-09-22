# R6 — RELEVANT COMPARISON SET

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Date:** 22-09-2026

## 1. Purpose
R6 defines the boundary for constructing the set of accumulated CMOC objects that may be used as the comparison set for downstream semantic comparison.
R6 does not decide NEW and does not establish semantic distinction.

## 2. Architectural position
SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → QUERY → RELEVANT_COMPARISON_SET → SEMANTIC_COMPARISON → SEMANTIC_DISTINCTION → NEW_DECISION → CANONIZATION → CMOC WRITE

> Reconciliation identifies the evidence state; the comparison-set stage selects relevant existing indexed representations. Semantic Comparison determines whether a positive semantic distinction exists.

## 3. Core problem
The candidate must not be compared blindly against the entire CMOC. The comparison set must be derived from indexed evidence, reproducible, traceable, bounded by explicit query scope, and independent from Discovery.

## 4. Minimum input
comparison_set_input:
  candidate: record_id, value, object_boundary
  reconciliation: match_result, basis, cmoc_object_id
  query_evidence: query_scope, modes, results
  traceability:

R6 consumes evidence already produced by Reconciliation/QUERY. It must not silently infer missing search evidence.

## 5. Minimum output
relevant_comparison_set:
  candidate_id:
  selection_basis:
  query_scope:
  objects: cmoc_object_id, representation_ids, relevance_basis, traceability
  completeness_state:
  traceability:

Completeness states: COMPLETE, PARTIAL, UNKNOWN. UNKNOWN is never COMPLETE.

## 6. Selection rules
An object may enter the comparison set only when its inclusion has an explicit basis: exact match evidence, explicit alias evidence, structural candidate evidence, or another explicitly contracted query result.

A textual occurrence alone does not establish relevance.

## 7. Boundary
R6 must not perform semantic equivalence and must not conclude EXISTING_EQUIVALENT, NEW, RELATED, CONFLICT, DISTINCT, or COVERED.

## 8. Empty comparison set
EMPTY_SET + COMPLETE_SCOPE may be useful evidence for subsequent NEW analysis.
EMPTY_SET + UNKNOWN_SCOPE does not establish absence.

## 9. Ambiguity
If query evidence returns multiple unresolved candidates, R6 preserves them and marks completeness accordingly. It must not arbitrarily select one.

## 10. Structural candidates
A structural QUERY result with status CANDIDATE may enter the comparison set as a candidate representation. Its presence means relevant for comparison, not equivalent.

## 11. Identity
R6 preserves object identity and representation identity separately. A canonical OBJECT_FILE and additional registry representations remain distinct physical representations.

## 12. No semantic enrichment
R6 must not invent aliases, object types, relations, semantic similarity, equivalence, conflicts, ontology properties, or relevance based only on model intuition.

## 13. Traceability
Every comparison-set member remains traceable through SOURCE_ID → INPUT_BATCH_ID → DISCOVERY_RECORD → RECONCILIATION → QUERY_RESULT → COMPARISON_SET.

## 14. Relationship to NEW
NO_MATCH is evidence about the search result, not itself evidence of semantic novelty.
The intended chain is: NO_MATCH → sufficient search evidence → comparison set → semantic comparison → positive semantic distinction → NEW DECISION.

## 15. Negative controls
R6 must reject or preserve as incomplete: insufficient query scope, UNKNOWN query evidence, ambiguous unresolved results, unsupported relevance assertions, invented target object types, semantic equivalence assertions, and arbitrary candidate selection.

## 16. Future executable test
At minimum test: exact match; alias result; structural candidate; multiple candidates; empty set with complete scope; empty set with unknown scope; textual mention without indexed object identity; object/representation identity separation; no semantic equivalence; unchanged OBJECT INDEX and DISCOVERY RESULT.

## 17. Status
R6 is an architecture candidate only. No production implementation or semantic novelty claim is established by this document.