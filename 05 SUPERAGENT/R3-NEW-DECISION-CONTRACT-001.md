# R3 — NEW DECISION CONTRACT

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Date:** 22-09-2026

## 1. Purpose

Define the boundary and minimal contract for a separate NEW DECISION machine.

R3 does not implement NEW decision logic. It defines what the machine may receive, what it may return, and what it must not do.

## 2. Governing architecture

`SOURCE → DISCOVERY → DISCOVERY_RESULT → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE`

Principle:

> Сначала добываем. Потом сопоставляем. Затем отдельно принимаем решение о NEW.

DISCOVERY and RECONCILIATION remain independent of NEW DECISION.

## 3. Input

The machine receives `NEW_DECISION_INPUT`.

Minimum structure:

```yaml
new_decision_input:
  candidate:
    record_id:
    value:
    object_boundary:

  reconciliation:
    match_result:
    basis:
    cmoc_object_id:

  query_evidence:
    query_scope:
    modes:
      exact:
      alias:
      structural:
    results:

  evidence_state:
    source_bound_candidate:
    traceability_complete:
    query_scope_sufficient:
    exact_checked:
    alias_checked:
    structural_checked_or_NA:
    no_ambiguity:
    no_unresolved_candidate:
    stable_object_boundary:
    target_object_type_resolved:

  target_object_type:
  traceability:
  decision_context:
```

The minimum evidence gate is established by R2.3.

## 4. Entry condition

A candidate may enter the NEW DECISION machine only when:

`ELIGIBLE_FOR_NEW_DECISION`

has been established by the preceding evidence gate.

The NEW DECISION machine must not silently reinterpret:

- `NO_MATCH` as NEW;
- `NEEDS_REVIEW` as NEW;
- `UNKNOWN` as TRUE;
- `CANDIDATE` as equivalence;
- `AMBIGUOUS` as NEW.

## 5. Decision outputs

R3 proposes only two decision results:

`NEW_APPROVED`

or

`NEW_REJECTED`

The machine may additionally return explicit decision evidence and reason fields, but the decision state must remain distinguishable from the evidence-gate state.

`ELIGIBLE_FOR_NEW_DECISION` is not a decision result.

## 6. Decision evidence

A decision output must preserve:

- input record identity;
- source traceability;
- reconciliation result and basis;
- query evidence;
- evidence state;
- target object type;
- decision result;
- decision basis;
- decision traceability.

No decision may discard the path back to SOURCE.

## 7. Separation from Canonization

`NEW_APPROVED` does not mean:

- canonical object already exists;
- canonical object ID has been assigned;
- relations have been created;
- CMOC has been written.

The sequence remains:

`NEW_APPROVED → CANONIZATION → CMOC WRITE`

unless a future explicit contract defines another controlled path.

## 8. Separation from CMOC WRITE

The NEW DECISION machine is read-only with respect to CMOC.

It must not:

- create CMOC objects;
- modify OBJECT INDEX;
- modify DISCOVERY_RESULT;
- modify RECONCILIATION_INPUT;
- perform canonization;
- create relations;
- assign canonical object IDs as a side effect.

## 9. Negative controls

At minimum, future executable tests must prove:

- `NO_MATCH` alone cannot produce `NEW_APPROVED`;
- insufficient query scope cannot produce `NEW_APPROVED`;
- unknown target type cannot produce `NEW_APPROVED`;
- unresolved candidate cannot produce `NEW_APPROVED`;
- ambiguous candidate cannot produce `NEW_APPROVED`;
- `ELIGIBLE_FOR_NEW_DECISION` alone cannot produce `NEW_APPROVED`;
- `NEW_APPROVED` does not write to CMOC;
- rejected candidates do not mutate CMOC;
- source traceability is preserved.

## 10. Current scope

R3 intentionally does not define:

- semantic novelty algorithm;
- similarity threshold;
- scoring or ranking;
- LLM prompt;
- automatic approval policy;
- human approval workflow;
- canonization rules;
- CMOC write contract.

These require separate evidence and contracts.

## 11. Architectural position

The intended separation is:

### DISCOVERY

Answers:

> Что удалось добыть из SOURCE?

### RECONCILIATION

Answers:

> Как добытый результат соотносится с накопленным CMOC?

### NEW DECISION

Answers:

> Достаточно ли оснований, чтобы принять решение, что этот кандидат является новым?

### CANONIZATION

Answers:

> Как оформить утверждённое новое знание в каноническом представлении?

### CMOC WRITE

Performs:

> Контролируемую запись утверждённого результата.

## 12. Status

R3 is a contract candidate only.

It is not evidence that a production NEW DECISION machine exists.

Next controlled step: define and execute an isolated negative/positive decision test before any production integration.
