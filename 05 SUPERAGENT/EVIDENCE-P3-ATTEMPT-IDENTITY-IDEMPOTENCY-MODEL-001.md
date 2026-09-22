# EVIDENCE-P3 — ATTEMPT IDENTITY / IDEMPOTENCY MODEL

**Status:** ACCEPTED  
**Test:** `05 SUPERAGENT/test_p3_attempt_identity_idempotency.py`  
**Gate result:** PASS

## 1. Scope

P3 establishes the productionization boundary for attempt identity and idempotency. It distinguishes:

`RUN_ID + STAGE_ID + ATTEMPT_ID`

from the independent `IDEMPOTENCY_KEY`, while preserving the authoritative `RESULT_ID`.

The test is synthetic and isolated. It does not perform production CMOC persistence, OBJECT INDEX mutation, semantic comparison, NEW decision, or canonization.

## 2. Test result

The P3 gate passed all 12 branches.

| Case | Result |
|---|---|
| P3-01 first attempt | ACCEPTED |
| P3-02 repeated completed attempt | ALREADY_COMPLETED |
| P3-03 completed result replacement | CONFLICTING_ATTEMPT |
| P3-04 failed attempt | ACCEPTED and preserved |
| P3-05 repeat failed attempt | DUPLICATE_ATTEMPT |
| P3-06 retry | NEW ATTEMPT_ID + NEW RESULT_ID accepted |
| P3-07 lost acknowledgement | ALREADY_COMPLETED; no duplicate authoritative effect |
| P3-08 cross-run idempotency | IDEMPOTENCY_KEY_CONFLICT |
| P3-09 conflicting result for same attempt | CONFLICTING_ATTEMPT |
| P3-10 idempotency-key mismatch | IDEMPOTENCY_KEY_MISMATCH |
| P3-11 repeated RUNNING attempt | IN_PROGRESS |
| P3-12 history/input preservation | preserved |

## 3. Evidence points

### 3.1 Completed attempt protection

A repeated request for an already completed attempt returns `ALREADY_COMPLETED` and retains the original authoritative `RESULT_ID`.

A second result for the same attempt is rejected as `CONFLICTING_ATTEMPT`. The existing result is not replaced.

### 3.2 Failed attempt and retry

A failed attempt remains recorded. Replaying the same failed attempt returns `DUPLICATE_ATTEMPT`.

A retry requires a new `ATTEMPT_ID` and receives a new `RESULT_ID`. The previous failed result remains preserved.

### 3.3 Lost acknowledgement

The synthetic test models the case where the authoritative result exists but the caller may repeat the request. The repeated request resolves to `ALREADY_COMPLETED`, demonstrating the intended idempotent boundary and prevention of a duplicate authoritative effect.

### 3.4 Idempotency-key boundary

The idempotency key is checked separately from attempt identity.

The test rejects:
- use of the same attempt identity under a different idempotency key: `IDEMPOTENCY_KEY_MISMATCH`;
- reuse of an idempotency key across different run identity: `IDEMPOTENCY_KEY_CONFLICT`.

### 3.5 In-progress protection

A repeated invocation of an already `RUNNING` attempt returns `IN_PROGRESS` rather than creating another attempt.

## 4. Responsibility isolation

The following remained false throughout the test:

`semantic_decision_performed`  
`semantic_comparison_performed`  
`canonization_performed`  
`cmoc_mutation_performed`  
`object_index_mutation_performed`  
`semantic_repair_performed`  
`duplicate_authoritative_effect_created`  
`failed_attempt_overwritten`

Therefore P3 does not absorb responsibility from the semantic layer R1-R10 or persistence/synchronization boundaries C1-C3.

## 5. Architectural conclusion

P3 closes the minimum attempt identity/idempotency question for the synthetic runtime model:

**same attempt is repeatable without duplicate authoritative effect; retry is a new attempt; failed history is preserved; idempotency is checked independently; cross-run reuse is isolated.**

P3 does not yet establish database transactionality, distributed locking, durable production storage, or concurrency guarantees. Those remain production-engineering concerns for later stages.

**Evidence status: ACCEPTED.**
