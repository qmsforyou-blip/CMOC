# R4 — SEMANTIC NEW CRITERIA

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Date:** 22-09-2026

## 1. Purpose

Define the minimum evidence required before a separate NEW DECISION mechanism may produce `NEW_APPROVED` on the grounds of semantic novelty.

R4 does not implement a novelty algorithm, LLM prompt, score, threshold, or production decision engine.

## 2. Governing distinctions

The following statements are distinct:

`NO_MATCH`

> В проверенном QUERY scope не найдено индексированного совпадения.

`ELIGIBLE_FOR_NEW_DECISION`

> Доказательств достаточно, чтобы передать кандидата в отдельный NEW DECISION.

`NEW_APPROVED`

> На основании установленного набора доказательств принято решение считать кандидат новым.

Therefore:

> **«Я не нашёл» ≠ «этого нет» ≠ «это новое».**

## 3. Architectural position

`SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE`

R4 concerns only the evidence entering NEW DECISION.

It must not weaken the already established boundary:

> **Сначала добываем. Потом сопоставляем. Затем отдельно принимаем решение о NEW.**

## 4. Minimum semantic NEW evidence

A candidate should not be approved as NEW unless the following evidence dimensions are resolved.

### R4.1 Candidate identity

The candidate has a stable identity within the current decision context.

Required:

- candidate record identity;
- candidate value;
- source traceability;
- explicit object boundary.

### R4.2 Object boundary

The candidate has an explicit boundary sufficient to answer:

> Что именно предлагается считать новым объектом?

A vague topic, phrase, fragment, or observation is insufficient by itself.

### R4.3 Search completeness

The relevant CMOC search scope is sufficient for the claimed object type.

The decision must record:

- query scope;
- query modes executed;
- scope limitations;
- unresolved search limitations.

Insufficient scope blocks automatic NEW approval.

### R4.4 Exact absence

The configured exact search does not identify an existing equivalent object.

This is necessary but not sufficient.

### R4.5 Alias absence

The configured explicit alias search does not identify an existing equivalent object.

This is necessary where aliases are applicable.

### R4.6 Structural non-equivalence

Where structural search is applicable, available structural candidates have been considered.

A structural candidate is not automatically equivalent.

If a candidate remains unresolved after structural comparison, NEW approval is blocked.

### R4.7 No unresolved ambiguity

The candidate does not have unresolved ambiguity caused by:

- multiple non-canonical representations;
- unresolved object identity;
- insufficient boundary;
- conflicting evidence;
- insufficient query scope.

Ambiguity blocks automatic NEW approval.

### R4.8 Positive semantic distinction

This is the critical R4 criterion.

A NEW decision requires positive evidence of what distinguishes the candidate from existing CMOC knowledge.

The decision must be able to state, in a traceable form:

> **Какое различение / свойство / отношение / механизм / capability присутствует у кандидата и почему существующее знание не покрывает его?**

Absence of a match is not positive semantic novelty evidence.

### R4.9 Provenance

The positive distinction must remain traceable to the originating SOURCE and upstream Discovery result.

The path must not be broken by Reconciliation or NEW Decision.

### R4.10 Decision basis

The resulting NEW decision must preserve:

- candidate identity;
- evidence used;
- existing candidates considered;
- positive semantic distinction;
- limitations;
- decision result;
- traceability.

## 5. Evidence states

R4 retains the existing evidence-state discipline:

- TRUE
- FALSE
- UNKNOWN
- NOT_APPLICABLE

Rules:

- UNKNOWN is not TRUE.
- UNKNOWN in a mandatory criterion blocks automatic NEW approval.
- NOT_APPLICABLE is permitted only when the criterion genuinely does not apply and the basis is recorded.
- FALSE blocks NEW approval.

## 6. Proposed minimum decision predicate

Conceptually:

`NEW_APPROVED` requires:

`candidate_identity`
AND `stable_object_boundary`
AND `query_scope_sufficient`
AND `exact_checked`
AND `alias_checked_or_NA`
AND `structural_checked_or_NA`
AND `no_ambiguity`
AND `no_unresolved_candidate`
AND `positive_semantic_distinction`
AND `provenance_complete`
AND `decision_basis_complete`

This predicate is a contract candidate, not yet an executable implementation.

## 7. Positive novelty versus negative search

R4 explicitly separates:

### Negative evidence

> Existing object was not found under configured search modes.

from:

### Positive evidence

> Candidate contains a defined semantic distinction not covered by the relevant existing object(s).

The second is required for semantic NEW.

## 8. What R4 does not define

R4 intentionally does not define:

- how semantic distinction is generated;
- how semantic distinction is compared;
- similarity metrics;
- embeddings;
- LLM prompts;
- scoring;
- confidence thresholds;
- human approval policy;
- automatic versus manual approval boundary;
- canonization rules.

These are separate design questions.

## 9. Required future executable test

Before production implementation, an R4 test should verify at least:

1. full evidence including positive semantic distinction → eligible for NEW decision;
2. NO_MATCH without positive semantic distinction → not approvable;
3. UNKNOWN semantic distinction → not approvable;
4. unresolved structural candidate → not approvable;
5. insufficient query scope → not approvable;
6. ambiguous candidate → not approvable;
7. complete negative search plus positive distinction → decision boundary can produce NEW_APPROVED in a synthetic fixture;
8. NEW_APPROVED does not perform canonization or CMOC WRITE.

## 10. Architectural conclusion

R4 establishes the key conceptual boundary:

> **NEW is not the absence of an existing match. NEW is a positive claim that the candidate contains a defined, traceable semantic distinction not covered by the relevant accumulated knowledge.**

This criterion must be evidenced before a production NEW DECISION mechanism is allowed to approve a candidate as NEW.

## 11. Status

R4 is **DESIGN / ARCHITECTURE CANDIDATE**.

Next controlled step: create an isolated executable R4 evidence test using synthetic fixtures, without changing production Discovery, Reconciliation, QUERY, OBJECT INDEX, or CMOC.
