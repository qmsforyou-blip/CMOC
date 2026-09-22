# EVIDENCE-R6 — RELEVANT COMPARISON SET

**Status:** ACCEPTED  
**Gate:** R6-RELEVANT-COMPARISON-SET  
**Date:** 22-09-2026

## 1. Result

The R6 executable synthetic boundary test returned:

`PASS`

All nine defined branches passed.

## 2. Verified branches

- EXACT_MATCH → one comparison object;
- ALIAS_MATCH → one comparison object;
- STRUCTURAL_CANDIDATE → candidate preserved;
- MULTIPLE_CANDIDATES → all candidates preserved;
- EMPTY_COMPLETE_SCOPE → empty set remains COMPLETE;
- EMPTY_UNKNOWN_SCOPE → state remains UNKNOWN;
- TEXTUAL_MENTION_WITHOUT_OBJECT → no comparison object created;
- OBJECT_REPRESENTATION_SEPARATE → representation identities remain separate;
- NO_SEMANTIC_EQUIVALENCE → comparison-set construction does not create equivalence.

## 3. Controlled invariants

The executed test confirmed:

- OBJECT INDEX unchanged;
- DISCOVERY RESULT unchanged;
- semantic equivalence not created;
- NEW decision not created;
- CMOC WRITE = NONE;
- production runtime not imported;
- production runtime import blocked.

## 4. Architectural meaning

R6 establishes the boundary:

SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → QUERY → RELEVANT_COMPARISON_SET → SEMANTIC_COMPARISON → SEMANTIC_DISTINCTION → NEW_DECISION → CANONIZATION → CMOC WRITE

The comparison set is evidence for what should be compared. It is not a semantic judgment.

The following distinctions are therefore preserved:

NO_MATCH ≠ EMPTY_COMPARISON_SET ≠ SEMANTICALLY_NEW

RELEVANT_FOR_COMPARISON ≠ EQUIVALENT ≠ NEW

STRUCTURAL_CANDIDATE ≠ EQUIVALENT

UNKNOWN_SCOPE ≠ COMPLETE_SCOPE

## 5. Evidence boundary

R6 does not establish:

- production relevance selection;
- production semantic comparison;
- semantic novelty;
- NEW_APPROVED;
- canonization;
- CMOC mutation.

The test is synthetic and verifies the architectural boundary only.

## 6. Status

R6 is ACCEPTED as evidence of the Relevant Comparison Set boundary.

The next step is R7: SEMANTIC COMPARISON MODEL.
