# EVIDENCE-R7 — SEMANTIC COMPARISON MODEL

**Status:** ACCEPTED  
**Gate:** R7.1-SEMANTIC-COMPARISON-COMPLETENESS-GATE  
**Date:** 22-09-2026

## 1. Result

The corrected R7.1 executable synthetic boundary test returned:

`PASS`

All fourteen branches passed.

## 2. Verified semantic dimensions

Controlled semantic comparison produced `DISTINCT` for:

- Entity;
- Property;
- Relation;
- Mechanism;
- Capability.

These are comparison dimensions, not automatic object types.

## 3. Verified negative controls

The test confirmed:

- wording-only difference → `COVERED`;
- same meaning from a different source → `COVERED`;
- unsupported LLM assertion → `UNRESOLVED`;
- UNKNOWN comparison evidence → `UNRESOLVED`;
- NOT_APPLICABLE is preserved explicitly;
- multiple existing objects are compared independently;
- dimension-local mixed results are preserved.

## 4. Comparison-set completeness control

R7.1 corrected the previous test weakness by making `comparison_set_completeness` an actual input to the comparison function.

Verified:

`UNKNOWN` comparison-set completeness → `UNRESOLVED`

Therefore incomplete knowledge of the comparison area cannot be silently promoted into positive semantic evidence.

The test also confirms:

`PARTIAL` comparison-set completeness does not mechanically invalidate a supported pairwise distinction.

The completeness state remains explicit and is not converted into `COMPLETE`.

## 5. Controlled invariants

The executed test confirmed:

- OBJECT INDEX unchanged;
- DISCOVERY RESULT unchanged;
- NEW_APPROVED = false;
- CMOC WRITE = NONE;
- production runtime not imported;
- production runtime import blocked.

## 6. Architectural meaning

R7 establishes the controlled boundary:

`CANDIDATE + RELEVANT_COMPARISON_SET → SEMANTIC_COMPARISON`

The result is dimension-specific comparison evidence:

`DISTINCT / COVERED / UNRESOLVED / NOT_APPLICABLE`

R7 does not decide NEW.

The following separation is preserved:

`QUERY` → selects indexed material relevant for comparison.

`R7 SEMANTIC COMPARISON` → records what the evidence supports for each comparison dimension.

`R5 SEMANTIC DISTINCTION` → structures positive semantic difference evidence.

`R3 NEW DECISION` → makes the separate NEW decision.

## 7. Evidence boundary

R7 does not establish:

- production semantic comparison;
- production semantic novelty;
- NEW_APPROVED;
- NEW_REJECTED;
- canonization;
- CMOC mutation;
- reliability of an LLM semantic-comparison implementation.

The executable test is synthetic and establishes the architectural boundary only.

## 8. Architectural conclusion

The controlled chain is now:

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
→ CMOC_WRITE

A model assertion alone is not semantic evidence.

Semantic comparison must preserve candidate identity, existing-object identity, comparison dimension, values, status, basis, source evidence, and traceability.

## 9. Status

R7 is **ACCEPTED as evidence of the Semantic Comparison Model boundary**.

The next architectural task is to define how a set of dimension-level comparison results is assembled into a single controlled `SEMANTIC_DISTINCTION` evidence object without collapsing unresolved dimensions or allowing a single positive difference to become an automatic NEW decision.
