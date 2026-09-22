# EVIDENCE-P5 — TRANSACTION / CONCURRENCY BOUNDARY

**Status:** ACCEPTED  
**Test:** `05 SUPERAGENT/test_p5_transaction_concurrency_boundary.py`  
**Gate result:** PASS

## 1. Scope

P5 establishes the synthetic runtime boundary for concurrent execution and authoritative transaction commit.

The test demonstrates that one authoritative attempt cannot produce two concurrent authoritative effects, that committed results are protected, that rollback does not create authoritative success, and that cross-run execution state remains isolated.

P5 does not establish a particular production database, distributed lock service, or external side-effect transaction protocol.

## 2. Test result

The P5 gate passed all 12 branches.

| Case | Result |
|---|---|
| P5-01 first caller | LOCK_ACQUIRED |
| P5-02 second concurrent caller | IN_PROGRESS |
| P5-03 completed attempt | ALREADY_COMPLETED; effect count remains 1 |
| P5-04 different ATTEMPT_ID | distinct execution boundary |
| P5-05 idempotency reuse | IDEMPOTENCY_CONFLICT |
| P5-06 completed result protection | authoritative result remains WRITE-001 |
| P5-07 commit | COMMITTED |
| P5-08 rollback | TRANSACTION_ROLLBACK; no authoritative success |
| P5-09 crash boundary | UNKNOWN_AFTER_CRASH; not assumed success |
| P5-10 cross-run isolation | separate execution identity |
| P5-11 responsibility isolation | prohibited operations false |
| P5-12 history/input preservation | preserved |

## 3. Evidence points

### 3.1 Concurrent caller protection

The first caller acquires the execution boundary.

A second caller using the same RUN/STAGE/ATTEMPT identity receives:

`IN_PROGRESS`

and does not create a second authoritative effect.

### 3.2 Completed attempt protection

After commit, a repeated invocation resolves to:

`ALREADY_COMPLETED`

with the original result and effect count preserved.

This combines the P5 execution boundary with the P3 idempotency boundary.

### 3.3 Attempt distinction

A retry using a different `ATTEMPT_ID` is a distinct execution identity and may acquire its own execution boundary.

P5 does not interpret this distinction as semantic permission to overwrite another result.

### 3.4 Idempotency conflict

Reusing an idempotency key for a different attempt identity is rejected:

`IDEMPOTENCY_CONFLICT`

### 3.5 Authoritative commit

A successful commit produces:

`COMMITTED`

with exactly one authoritative effect for that attempt.

### 3.6 Rollback

A transaction rolled back before commit produces:

`TRANSACTION_ROLLBACK`

with zero authoritative effects.

No success is reported merely because execution had started.

### 3.7 Crash/uncertainty boundary

A simulated process loss before commit produces:

`UNKNOWN_AFTER_CRASH`

and does not mark the operation as authoritative success.

The subsequent resolution of such uncertainty remains within P4/REC and the production side-effect protocol.

### 3.8 Result protection

When a completed attempt is presented with a different result, the already authoritative result remains unchanged.

P5 does not decide which result is semantically correct.

### 3.9 Cross-run isolation

A foreign RUN_ID receives its own execution identity and does not consume the execution state of the original RUN.

## 4. Responsibility isolation

The test confirms:

`semantic_decision_performed = false`  
`semantic_comparison_performed = false`  
`canonization_performed = false`  
`cmoc_semantic_mutation_performed = false`  
`object_index_semantic_mutation_performed = false`  
`semantic_repair_performed = false`  
`duplicate_authoritative_effect_created = false`

Therefore P5 remains an execution-safety boundary and does not absorb responsibility from R1-R10, C1-C3, RUN, ORCH, REC, or P4.

## 5. Architectural conclusion

P5 closes the minimum synthetic concurrency/transaction question:

**for one authoritative attempt, concurrent callers cannot create duplicate authoritative effects; committed results are protected; rollback does not become success; uncertainty is not silently resolved as success; idempotency remains enforced; and execution identities remain isolated across runs.**

P5 does not yet establish a particular production storage or locking technology, distributed transaction semantics, or external side-effect atomicity.

**Evidence status: ACCEPTED.**
