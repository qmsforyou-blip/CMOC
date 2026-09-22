# EVIDENCE-R8 — SEMANTIC DISTINCTION ASSEMBLY

**Status:** ACCEPTED  
**Gate:** R8-SEMANTIC-DISTINCTION-ASSEMBLY  
**Date:** 22-09-2026

## 1. Result

The R8 executable synthetic boundary test returned:

`PASS`

All ten branches passed.

## 2. Verified assembly branches

- ONE_DISTINCT_REST_COVERED → `SEMANTIC_DISTINCTION`
- DISTINCT_PLUS_UNRESOLVED → `SEMANTIC_DISTINCTION`
- ONLY_COVERED → `NO_POSITIVE_DISTINCTION`
- ALL_UNRESOLVED → `NO_POSITIVE_DISTINCTION`
- MULTIPLE_DISTINCT → `SEMANTIC_DISTINCTION`
- NOT_APPLICABLE → `SEMANTIC_DISTINCTION`
- UNKNOWN_COMPARISON_SET → `NOT_APPROVABLE`
- DISTINCT_WITHOUT_SOURCE_EVIDENCE → `NOT_APPROVABLE`
- DISTINCT_WITHOUT_TRACEABILITY → `NOT_APPROVABLE`
- DIMENSIONS_PRESERVED → all dimension-level states preserved

## 3. Dimension preservation

The executed test confirmed that aggregation does not collapse dimension-level evidence.

A synthetic result containing:

- 2 DISTINCT;
- 1 COVERED;
- 1 UNRESOLVED;
- 1 NOT_APPLICABLE

remained represented with those four separate evidence groups.

## 4. Positive distinction rule

A valid dimension-level `DISTINCT` may contribute to a `SEMANTIC_DISTINCTION` only when its:

- distinction;
- basis;
- source evidence;
- traceability

are present.

A `DISTINCT` result without source evidence or without traceability is `NOT_APPROVABLE`.

## 5. UNKNOWN comparison-set boundary

When the comparison-set completeness is `UNKNOWN`, the assembly does not produce an approvable positive semantic-distinction state.

This preserves the distinction between:

`positive pairwise difference`

and

`sufficiently complete evidence for downstream novelty decision`.

## 6. Important separation

R8 establishes:

`R7 comparison records → SEMANTIC_DISTINCTION evidence`

It does not establish:

`SEMANTIC_DISTINCTION → NEW_APPROVED`

No NEW decision is created by R8.

## 7. Controlled invariants

The executed test confirmed:

- OBJECT INDEX unchanged;
- DISCOVERY RESULT unchanged;
- NEW_APPROVED = false;
- CMOC WRITE = NONE;
- object ID not created;
- canonization not performed;
- production runtime not imported.

## 8. Evidence boundary

R8 is a synthetic assembly test.

It does not establish:

- production semantic-distinction assembly;
- production semantic novelty;
- correctness of an LLM semantic comparison implementation;
- NEW approval;
- canonization;
- CMOC mutation.

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
→ NEW_DECISION
→ CANONIZATION
→ CMOC WRITE

## 10. Status

R8 is **ACCEPTED as evidence of the Semantic Distinction Assembly boundary**.

The next task is to define the minimum aggregate evidence that R8 must expose to the separate NEW DECISION stage, without converting semantic distinction into automatic approval.
