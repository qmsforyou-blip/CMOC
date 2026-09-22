# P1 — EXECUTION JOURNAL MODEL

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Parent:** PROD-001  
**Purpose:** define minimum durable append-only execution history for RUN, ORCH and REC.

## 1. Principle

The execution journal records what happened to an execution.

It does not decide what the source means.

The journal is not CMOC.

## 2. Candidate event

Each journal event should contain at minimum:

```yaml
RUN_ID:
EVENT_ID:
EVENT_SEQ:
TIMESTAMP:
STAGE_ID:
EVENT_TYPE:
STAGE_RESULT_ID:
ATTEMPT_ID:
EVENT_STATUS:
TRACEABILITY:
```

Optional fields may be added only by explicit contract.

## 3. Event identity

EVENT_ID is unique.

EVENT_SEQ is monotonic within RUN_ID.

An event is append-only.

Existing events are never rewritten to represent a later attempt.

## 4. Candidate event types

- RUN_CREATED
- STAGE_STARTED
- STAGE_COMPLETED
- STAGE_REJECTED
- STAGE_FAILED
- RECOVERY_REQUESTED
- RETRY_REQUIRED
- RESUME_ALLOWED
- RESUME_BLOCKED
- RUN_COMPLETED
- RUN_REJECTED
- RUN_FAILED
- RUN_INCOMPLETE

The list is a candidate contract and requires test closure before production use.

## 5. Attempt identity

A stage execution may have:

```text
ATTEMPT_ID
```

A retry receives a new ATTEMPT_ID.

The original failed attempt remains in the journal.

A resume of the same execution is not silently converted into a new RUN_ID.

## 6. State derivation

RUN state should be derivable from journal events rather than maintained only as an opaque mutable field.

Candidate rule:

```text
JOURNAL
   ↓ deterministic reduction
RUN STATE
```

The reduction function must be deterministic and must reject impossible event sequences.

## 7. Immutability

The journal must reject:

- duplicate EVENT_ID;
- duplicate EVENT_SEQ within RUN_ID;
- sequence regression;
- foreign RUN_ID;
- stage result attached to another RUN_ID;
- mutation of an existing event;
- retry represented by overwriting the failed event.

## 8. Relationship with ORCH

ORCH may append execution events.

ORCH does not edit historical events.

The journal records orchestration outcomes but does not determine whether the next stage is semantically justified.

## 9. Relationship with REC

REC may append recovery disposition events:

```text
RECOVERY_REQUESTED
RETRY_REQUIRED
RESUME_ALLOWED
RESUME_BLOCKED
ALREADY_COMPLETED
INCONSISTENT_HISTORY
```

REC does not repair historical events.

## 10. Relationship with semantic results

A journal event may reference:

- DISCOVERY_RESULT_ID;
- RECONCILIATION_RESULT_ID;
- NEW_DECISION_ID;
- CANONIZATION_RESULT_ID;
- CMOC_WRITE_ID;
- OBJECT_INDEX_SYNC_ID.

It must not modify those results.

## 11. Crash / restart question

P1 must allow a later runtime instance to reconstruct the last authoritative execution state from durable events.

A missing acknowledgement must not by itself create a new RUN.

A repeated invocation must be distinguishable from a new execution.

## 12. Open transaction question

P1 does not yet define the final transaction mechanism.

It defines the history that the transaction mechanism must preserve.

## 13. Candidate invariants

I-P1-01 — journal is append-only.

I-P1-02 — event identity is unique.

I-P1-03 — event sequence is monotonic per RUN_ID.

I-P1-04 — events cannot cross RUN_ID boundaries.

I-P1-05 — retry creates a new ATTEMPT_ID.

I-P1-06 — historical failed attempts remain preserved.

I-P1-07 — state reduction is deterministic.

I-P1-08 — journal does not perform semantic decisions.

I-P1-09 — journal does not mutate CMOC.

I-P1-10 — journal does not mutate OBJECT INDEX.

## 14. First implementation target

The first test should be synthetic and in-memory.

It should prove:

1. append;
2. ordered sequence;
3. duplicate rejection;
4. cross-run rejection;
5. failed attempt preservation;
6. retry with new ATTEMPT_ID;
7. deterministic state reconstruction;
8. restart reconstruction;
9. impossible transition rejection;
10. no semantic / CMOC / index responsibility leakage.

## 15. Non-goals

P1 does not establish:

- database technology;
- distributed transaction technology;
- locking technology;
- production persistence;
- production recovery;
- semantic decision logic.

## 16. Candidate conclusion

P1 establishes the minimum execution-history abstraction required before durable RUN / ORCH / REC can be engineered.

The next artifact should be the synthetic P1 journal test.
