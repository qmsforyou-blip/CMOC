# EVIDENCE-R5 — SEMANTIC DISTINCTION MODEL

**Status:** ACCEPTED  
**Gate:** R5-SEMANTIC-DISTINCTION-MODEL  
**Date:** 22-09-2026

## 1. Purpose

R5 verifies a structured model for expressing positive semantic distinctions between a candidate and relevant accumulated knowledge.

The test uses synthetic fixtures only. It does not implement a production semantic comparison engine.

## 2. Architectural position

`SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → SEMANTIC COMPARISON → SEMANTIC DISTINCTION → NEW DECISION → CANONIZATION → CMOC WRITE`

R5 remains downstream of Reconciliation and does not move CMOC/QUERY access into Discovery.

The governing principle remains:

> **Сначала добываем. Потом сопоставляем. Затем отдельно принимаем решение о NEW.**

## 3. Executable test

Test:

`05 SUPERAGENT/test_r5_semantic_distinction.py`

Local execution:

`py "05 SUPERAGENT\\test_r5_semantic_distinction.py"`

Result:

`PASS`

## 4. Branch results

| Branch | Expected | Actual | Result |
|---|---|---|---|
| ENTITY_DISTINCT | DISTINCT | DISTINCT | PASS |
| PROPERTY_DISTINCT | DISTINCT | DISTINCT | PASS |
| RELATION_DISTINCT | DISTINCT | DISTINCT | PASS |
| MECHANISM_DISTINCT | DISTINCT | DISTINCT | PASS |
| CAPABILITY_DISTINCT | DISTINCT | DISTINCT | PASS |
| WORDING_ONLY | COVERED | COVERED | PASS |
| SAME_MEANING_DIFFERENT_SOURCE | COVERED | COVERED | PASS |
| UNRESOLVED_EVIDENCE | UNRESOLVED | UNRESOLVED | PASS |
| UNKNOWN_EVIDENCE | UNRESOLVED | UNRESOLVED | PASS |
| UNSUPPORTED_LLM_ASSERTION | UNRESOLVED | UNRESOLVED | PASS |
| INVALID_DIMENSION | UNRESOLVED | UNRESOLVED | PASS |

All eleven branch inputs remained unchanged during evaluation.

## 5. Five comparison dimensions

The test confirms that a controlled semantic distinction can be represented across:

- Entity;
- Property;
- Relation;
- Mechanism;
- Capability.

All five synthetic positive fixtures produced `DISTINCT`.

These are comparison dimensions, not automatic object types.

## 6. Negative controls

The test confirms:

### Wording only

Different wording without semantic difference produces:

`COVERED`

Therefore:

> **Разный текст ≠ новое знание.**

### Same meaning, different source

A different source does not establish semantic distinction:

`COVERED`

### Insufficient evidence

No established semantic difference produces:

`UNRESOLVED`

### UNKNOWN

UNKNOWN evidence produces:

`UNRESOLVED`

and is not promoted to `DISTINCT`.

### Unsupported LLM assertion

An unsupported assertion does not constitute semantic evidence:

`UNRESOLVED`

### Invalid comparison dimension

An uncontrolled dimension produces:

`UNRESOLVED`

## 7. Controlled invariants

The executed test confirmed:

- all five dimensions can produce controlled `DISTINCT` in synthetic fixtures;
- wording-only difference is not `DISTINCT`;
- different source with same meaning is not `DISTINCT`;
- UNKNOWN is not `DISTINCT`;
- unsupported assertion is not `DISTINCT`;
- OBJECT INDEX unchanged;
- DISCOVERY RESULT unchanged;
- `cmoc_write = NONE`;
- production runtime not imported;
- production runtime import blocked by test design.

## 8. What R5 proves

R5 proves that the abstract R4 requirement:

`positive_semantic_distinction`

can be represented as an explicit comparison result with:

- candidate identity;
- existing object identity where applicable;
- comparison dimension;
- candidate-side content;
- existing-side content;
- explicit distinction;
- basis;
- source evidence;
- comparison status;
- traceability.

The controlled positive state is:

`comparison_status = DISTINCT`

## 9. What R5 does not prove

R5 does not prove:

- semantic comparison correctness on real CMOC data;
- automatic selection of relevant existing objects;
- semantic novelty on arbitrary sources;
- LLM reliability;
- embedding or similarity correctness;
- scoring;
- production NEW DECISION;
- canonization;
- CMOC mutation.

## 10. Architectural conclusion

R5 turns positive semantic novelty evidence from an opaque assertion into a structured comparison object.

The intended controlled chain is:

`RECONCILIATION`
→ relevant accumulated knowledge / search evidence

`SEMANTIC COMPARISON`
→ controlled comparison

`SEMANTIC DISTINCTION`
→ explicit `DISTINCT / COVERED / UNRESOLVED / NOT_APPLICABLE`

`NEW DECISION`
→ decision based on supported distinctions

This preserves explainability and traceability.

## 11. Status

R5 is **ACCEPTED as evidence of the Semantic Distinction Model boundary**.

The next architectural question is how the relevant existing comparison set is selected and how semantic comparison is generated, while preserving the existing Discovery → Reconciliation separation.
