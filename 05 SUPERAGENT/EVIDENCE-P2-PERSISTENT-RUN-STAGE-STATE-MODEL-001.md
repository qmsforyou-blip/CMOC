# EVIDENCE-P2 — PERSISTENT RUN / STAGE STATE MODEL

**Status:** ACCEPTED  
**Gate:** P2-PERSISTENT-RUN-STAGE-STATE-MODEL  
**Scope:** synthetic / in-memory

## Result

P2 passed all 12 defined branches.

Verified:

- RUN and stage state projection;
- stage progression;
- completed-stage protection;
- failed-stage state;
- recovery transition;
- retry with a new ATTEMPT_ID;
- deterministic state projection;
- restart reconstruction;
- journal / persisted-state mismatch detection;
- cross-run isolation through projection validation;
- STATE_VERSION handling;
- absence of semantic / CMOC / OBJECT INDEX responsibility leakage.

## Key result

The tested projection contains explicit operational state:

- RUN_ID;
- RUN_STATUS;
- CURRENT_STAGE_ID;
- CURRENT_STAGE_RESULT_ID;
- CURRENT_ATTEMPT_ID;
- LAST_EVENT_SEQ;
- STATE_VERSION.

Retry changes ATTEMPT_ID while preserving the historical failed attempt in the journal.

## Important observation

P2 demonstrates the distinction:

JOURNAL = durable execution history.

RUN / STAGE STATE = operational projection of that history.

A persisted projection that differs from deterministic journal reduction is detected as STATE_MISMATCH rather than silently repaired.

## Controls

- semantic decision performed: false;
- semantic comparison performed: false;
- canonization performed: false;
- CMOC mutation: false;
- OBJECT INDEX mutation: false;
- semantic repair: false;
- synthetic-only: true.

## Limitation

P2 remains synthetic and does not establish database technology, distributed locking, transaction implementation, process supervision, or production persistence.

## Architectural conclusion

P2 closes the minimum state-projection question required after P1.

The next productionization concern is explicit attempt identity and idempotency behavior at the runtime boundary.