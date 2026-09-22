# P2 — PERSISTENT RUN / STAGE STATE MODEL

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Parent:** PROD-001  
**Depends on:** P1 — EXECUTION JOURNAL MODEL

## 1. Purpose

P2 defines the execution state that may be reconstructed from the durable journal and persisted as a controlled runtime representation.

P2 does not replace the journal.

The journal remains the historical source of execution events.

## 2. Core distinction

Historical truth:

JOURNAL = what events were recorded.

Operational state:

RUN / STAGE STATE = what the execution currently permits.

Therefore:

JOURNAL
→ deterministic state reduction
→ RUN STATE

A persisted state is a projection, not a rewritten history.

## 3. Candidate RUN state

A RUN state may contain:

```yaml
RUN_ID:
SOURCE_ID:
BATCH_ID:
RUN_STATUS:
CURRENT_STAGE_ID:
CURRENT_STAGE_RESULT_ID:
CURRENT_ATTEMPT_ID:
LAST_EVENT_SEQ:
STATE_VERSION:
TRACEABILITY:
```

The final schema is a subsequent implementation decision.

## 4. Candidate stage state

Each contracted stage may have one derived operational state:

```text
NOT_REACHED
READY
RUNNING
COMPLETED
REJECTED
FAILED
RECOVERABLE
BLOCKED
```

The state is derived from a defined transition model.

## 5. State transition authority

A stage state may change only through a valid journal event.

No component may directly rewrite the semantic result in order to obtain a desired execution state.

## 6. Candidate transitions

### RUN

```text
RUN_CREATED → ACTIVE
ACTIVE → RUN_COMPLETED
ACTIVE → RUN_REJECTED
ACTIVE → RUN_FAILED
ACTIVE → RUN_INCOMPLETE
```

### STAGE

```text
NOT_REACHED → READY
READY → RUNNING
RUNNING → COMPLETED
RUNNING → REJECTED
RUNNING → FAILED
FAILED → RECOVERABLE
RECOVERABLE → READY
```

These transitions are candidate semantics and require synthetic test closure.

## 7. Completed-stage protection

Once a stage has an authoritative COMPLETED result, the runtime must not execute it again merely because the process was restarted.

A duplicate invocation must resolve to an explicit idempotency outcome.

Historical completion remains preserved in the journal.

## 8. Failed-stage handling

A FAILED stage must not automatically become successful.

It may become RECOVERABLE only through an explicit RECOVERY event/disposition.

A retry produces a new ATTEMPT_ID.

## 9. Restart

After process restart:

1. load journal;
2. validate event history;
3. deterministically reduce state;
4. compare with persisted projection where applicable;
5. reject or rebuild inconsistent state only according to an explicit integrity rule.

No semantic result is repaired during restart.

## 10. State version

A persisted state should carry:

```text
STATE_VERSION
```

The version identifies the runtime state representation, not the semantic version of CMOC objects.

## 11. State / journal consistency

Candidate invariant:

```text
JOURNAL_REDUCE(RUN_ID) = PERSISTED_RUN_STATE
```

If they differ, the runtime must enter a controlled inconsistency state.

It must not silently overwrite the journal or alter semantic results.

## 12. Cross-run isolation

A persisted RUN state must reject:

- foreign SOURCE_ID;
- foreign BATCH_ID where binding is required;
- foreign STAGE_RESULT_ID;
- foreign ATTEMPT_ID;
- reuse of RUN_ID with incompatible execution identity.

## 13. Separation from CMOC

RUN / stage state is execution infrastructure.

It must not be stored as a CMOC object merely because it has an identifier.

Any future CMOC representation requires a separate CMOC decision.

## 14. Idempotency boundary

P2 defines the state needed to answer:

> Has this contracted execution already produced an authoritative result?

It does not define the full implementation of idempotency keys or distributed locks.

Those remain production engineering concerns.

## 15. Required synthetic test

P2 test should prove:

1. RUN_CREATED → active state;
2. stage progression;
3. completed stage protection;
4. failed stage state;
5. recovery transition;
6. retry with new ATTEMPT_ID;
7. deterministic state projection;
8. restart reconstruction;
9. journal / state mismatch detection;
10. cross-run isolation;
11. state version handling;
12. no semantic / CMOC / OBJECT INDEX leakage.

## 16. Non-goals

P2 does not establish:

- database technology;
- distributed locking;
- transaction implementation;
- production process supervision;
- semantic decision logic;
- CMOC schema changes.

## 17. Candidate conclusion

P2 converts P1's execution history into an explicit operational state model.

The architectural distinction is:

**Journal = durable history.**

**RUN / stage state = controlled operational projection of that history.**

The next artifact is the synthetic P2 state-model test.