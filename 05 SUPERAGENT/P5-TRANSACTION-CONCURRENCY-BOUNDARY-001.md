# P5 — TRANSACTION / CONCURRENCY BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE

## 1. Purpose

P5 defines the production runtime boundary for concurrent execution of the same RUN/STAGE/ATTEMPT and for atomic persistence of authoritative execution effects.

P5 is an execution-safety boundary. It does not add semantic meaning.

## 2. Problem boundary

P3 establishes attempt identity and idempotency.

P4 establishes restart/resume disposition.

P5 establishes that concurrent callers cannot create two authoritative effects for the same attempt or silently overwrite one another.

Candidate identity:

`RUN_ID + STAGE_ID + ATTEMPT_ID`

Idempotency remains a separate guard:

`IDEMPOTENCY_KEY`

## 3. Candidate critical section

For an authoritative stage effect:

`ACQUIRE → CHECK_IDENTITY → CHECK_IDEMPOTENCY → EXECUTE/PERSIST → COMMIT → RELEASE`

Only one owner may hold the authoritative execution lease for a given attempt at a time.

## 4. Candidate outcomes

- `LOCK_ACQUIRED`
- `IN_PROGRESS`
- `ALREADY_COMPLETED`
- `CONCURRENT_ATTEMPT`
- `IDEMPOTENCY_CONFLICT`
- `CONFLICTING_RESULT`
- `TRANSACTION_REJECTED`
- `TRANSACTION_ROLLBACK`
- `COMMITTED`

The exact production persistence mechanism is intentionally not fixed by P5. It may be implemented using database transactions, unique constraints, distributed locks/leases, or another equivalent mechanism.

## 5. Concurrency rules

### Same attempt, first caller

The first admissible caller acquires the execution boundary.

Expected state:

`LOCK_ACQUIRED`

### Same attempt, second concurrent caller

A second caller for the same authoritative attempt must not execute a second authoritative effect.

Expected disposition:

`IN_PROGRESS`

or an equivalent explicit contention state.

The second caller must not silently create a new ATTEMPT_ID.

### Same attempt after commit

If the authoritative result has already committed:

`ALREADY_COMPLETED`

No second effect is executed.

### Different attempt

A legitimate retry has a new `ATTEMPT_ID` and may proceed subject to P3/P4 recovery rules.

P5 must not treat a new ATTEMPT_ID as permission to overwrite an existing authoritative result.

## 6. Atomicity

The authoritative effect and its authoritative result record must have a defined commit boundary.

Candidate invariant:

`EFFECT_COMMITTED iff AUTHORITATIVE_RESULT_PERSISTED`

If the transaction fails before commit:

- no authoritative success is reported;
- partial authoritative state must not be presented as completed;
- the failure remains recoverable through P4/REC.

If commit succeeds:

- the result is authoritative;
- subsequent duplicate invocation resolves through P3 idempotency.

## 7. Crash boundaries

P5 must distinguish:

1. crash before execution;
2. crash during execution;
3. crash after effect but before acknowledgement;
4. crash after authoritative commit.

P5 must not infer success merely from process termination.

Where an external effect cannot participate in the same transaction, the boundary must expose the uncertainty explicitly rather than inventing completion.

## 8. Result conflicts

If two concurrent callers present different results for the same:

`RUN_ID + STAGE_ID + ATTEMPT_ID`

the existing authoritative result must not be overwritten.

Expected outcome:

`CONFLICTING_RESULT`

P5 does not decide which result is semantically correct.

## 9. Retry interaction

Retry is permitted only with a new `ATTEMPT_ID` after the recovery boundary permits it.

P5 must prevent:

- two concurrent executions of the same attempt;
- retry under an already active attempt;
- duplicate authoritative commit;
- overwrite of an existing authoritative result.

## 10. Cross-run isolation

Locks, leases, transactions, and idempotency records are scoped so that RUN-A cannot acquire or consume the authoritative execution state of RUN-B.

Foreign lineage is rejected.

## 11. Responsibility boundary

P5 must NOT:

- make a NEW decision;
- perform semantic equivalence;
- perform semantic comparison;
- resolve semantic conflicts;
- perform canonization;
- alter canonical CMOC meaning;
- mutate OBJECT INDEX semantically;
- repair semantic evidence;
- invent lineage;
- convert failure into success.

P5 may enforce structural persistence and concurrency safety only.

## 12. Synthetic test boundary

The first P5 test is synthetic and isolated.

It must demonstrate at minimum:

1. first caller acquires execution boundary;
2. second concurrent caller is blocked;
3. completed attempt prevents duplicate execution;
4. different ATTEMPT_ID is distinct;
5. same idempotency key cannot create duplicate effect;
6. conflicting result is rejected;
7. commit produces authoritative result;
8. rollback does not produce authoritative success;
9. crash/unknown boundary is not silently treated as success;
10. cross-run isolation;
11. no semantic responsibility leakage;
12. history/input preservation.

P5 does not yet establish a particular database engine, distributed lock implementation, or external side-effect transaction protocol.
