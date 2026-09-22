# R5 — SEMANTIC DISTINCTION MODEL

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Date:** 22-09-2026

## 1. Purpose

Define the minimum structure by which a NEW DECISION mechanism can express and preserve a positive semantic distinction between a candidate and relevant accumulated CMOC knowledge.

R5 does not implement semantic comparison, an LLM prompt, embeddings, scoring, or production NEW approval.

## 2. Architectural position

`SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE`

R5 operates at the boundary between Reconciliation evidence and NEW Decision evidence.

It does not move QUERY or CMOC access back into DISCOVERY.

## 3. Core proposition

R4 established:

> NEW requires positive semantic evidence in addition to negative search evidence.

R5 defines the form of that positive evidence.

The basic unit is:

`CANDIDATE DISTINCTION`

A candidate distinction must answer:

> **Что именно в кандидате отличается от релевантного существующего знания, в каком элементе это различие выражено и на каком основании оно установлено?**

## 4. Comparison object

The candidate and the relevant existing object are compared through the CMOC meta-passport dimensions:

- Entity
- Property
- Relation
- Mechanism
- Capability

These dimensions are comparison coordinates, not automatic object types.

A distinction may concern one or several dimensions.

## 5. Minimal semantic distinction record

Proposed structure:

```yaml
semantic_distinction:
  candidate_id:
  existing_object_id:
  comparison_dimension:
  candidate_value:
  existing_value:
  distinction:
  basis:
  source_evidence:
  comparison_status:
  traceability:
```

Where:

- `candidate_id` identifies the discovered candidate;
- `existing_object_id` identifies the relevant accumulated object when one exists;
- `comparison_dimension` identifies Entity / Property / Relation / Mechanism / Capability;
- `candidate_value` states the candidate-side value;
- `existing_value` states the relevant existing-side value;
- `distinction` states the observed semantic difference;
- `basis` states why the distinction is supported;
- `source_evidence` preserves the originating evidence;
- `comparison_status` records the controlled comparison state;
- `traceability` preserves the path to SOURCE and upstream records.

## 6. Comparison status

R5 proposes the following controlled states:

- `DISTINCT`
- `COVERED`
- `UNRESOLVED`
- `NOT_APPLICABLE`

Rules:

### DISTINCT

A supported semantic difference has been established for the compared dimension.

### COVERED

The candidate-side content is covered by the relevant existing knowledge for that dimension.

### UNRESOLVED

Available evidence is insufficient to establish either DISTINCT or COVERED.

UNRESOLVED blocks automatic NEW approval.

### NOT_APPLICABLE

The dimension genuinely does not apply to the comparison and the reason is recorded.

## 7. Positive distinction rule

A positive semantic distinction exists only when:

`comparison_status = DISTINCT`

and the distinction is supported by traceable evidence.

The following are not sufficient by themselves:

- different wording;
- different source;
- different record ID;
- different document location;
- different formatting;
- absence of exact match;
- LLM assertion without preserved basis.

## 8. Existing object requirement

R5 does not require that every candidate be compared to exactly one existing object.

Possible controlled situations:

1. one relevant existing object;
2. several relevant existing objects;
3. no relevant existing object found.

If several existing objects are relevant, the comparison set must be preserved.

If no existing object is found, the positive distinction cannot simply be inferred from absence. A separate evidence form is required to state what semantic coverage was searched and why the candidate distinction remains positive.

This is deliberately left as a future refinement rather than silently assuming that NO_MATCH proves novelty.

## 9. Coverage versus distinction

The comparison must distinguish:

`COVERED`

from:

`DISTINCT`

A candidate may contain additional wording or detail while remaining semantically covered.

Therefore:

> **More text ≠ new knowledge.**

Likewise:

> **Different expression ≠ semantic distinction.**

The distinction must concern the represented engineering content.

## 10. Relation to R4

R4 requires:

`positive_semantic_distinction = TRUE`

R5 proposes that this state can only be supported when at least one controlled comparison yields:

`comparison_status = DISTINCT`

with complete traceability and an explicit basis.

Thus:

`DISTINCT` + evidence → `positive_semantic_distinction = TRUE`

while:

`COVERED`, `UNRESOLVED`, or unsupported assertion → not sufficient.

## 11. Multiple dimensions

A candidate may produce multiple distinction records.

Example:

```yaml
semantic_distinctions:
  - comparison_dimension: Property
    comparison_status: DISTINCT
  - comparison_dimension: Relation
    comparison_status: DISTINCT
```

The NEW decision must preserve all material distinctions rather than collapse them into a single opaque score.

## 12. Evidence discipline

The semantic distinction record must not invent information absent from the candidate or comparison evidence.

The machine must preserve:

`SOURCE → DISCOVERY_RESULT → RECONCILIATION → COMPARISON → DISTINCTION`

If the evidence does not support a distinction, the state must remain `UNRESOLVED` or another applicable non-positive state.

## 13. What R5 does not define

R5 intentionally does not define:

- how the comparison is generated;
- whether comparison is rule-based, LLM-assisted, or hybrid;
- embeddings;
- similarity thresholds;
- ranking;
- weighting;
- scoring;
- semantic distance;
- automatic selection of relevant existing objects;
- final NEW approval policy.

These require separate evidence.

## 14. Required future executable test

Before production implementation, an R5 test should verify at least:

1. Entity distinction → DISTINCT;
2. Property distinction → DISTINCT;
3. Relation distinction → DISTINCT;
4. Mechanism distinction → DISTINCT;
5. Capability distinction → DISTINCT;
6. wording-only difference → not DISTINCT;
7. same meaning with different source → COVERED;
8. unresolved evidence → UNRESOLVED;
9. unsupported LLM assertion → not sufficient;
10. DISTINCT with traceability can support R4 positive semantic evidence;
11. no CMOC or OBJECT INDEX mutation.

## 15. Architectural conclusion

R5 turns the abstract phrase “positive semantic distinction” into a structured comparison object.

The intended chain is:

`RECONCILIATION`
→ identifies relevant accumulated knowledge and search evidence

`SEMANTIC COMPARISON`
→ compares candidate against relevant knowledge

`SEMANTIC DISTINCTION`
→ records explicit differences in Entity / Property / Relation / Mechanism / Capability

`NEW DECISION`
→ determines whether the supported distinctions justify NEW

This keeps the decision explainable and traceable rather than reducing NEW to an opaque similarity score.

## 16. Status

R5 is **DESIGN / ARCHITECTURE CANDIDATE**.

Next controlled step: create an isolated executable R5 test with synthetic comparisons across the five meta-passport dimensions, without changing production Discovery, Reconciliation, QUERY, OBJECT INDEX, or CMOC.
