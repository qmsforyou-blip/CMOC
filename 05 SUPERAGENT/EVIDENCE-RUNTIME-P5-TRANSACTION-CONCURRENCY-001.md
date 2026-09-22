# EVIDENCE — RUNTIME P5 TRANSACTION / CONCURRENCY — 001

**Status:** ACCEPTED  
**Date:** 22-09-2026  
**Scope:** first real runtime implementation of P5  
**Implementation:** `05 SUPERAGENT/runtime_transaction_store.py`  
**Test:** `05 SUPERAGENT/test_runtime_transaction_concurrency.py`  
**Persistence:** local SQLite

## 1. Result

User executed:

```
py "05 SUPERAGENT\test_runtime_transaction_concurrency.py"
```

Result:

```
RUNTIME TRANSACTION CONCURRENCY TEST: PASS
```

## 2. Runtime boundary

P5 provides a local single-host transaction/concurrency boundary between P3 attempt identity and authoritative execution effects.

The tested chain is:

```
P3 Attempt Identity
        ↓
P5 Execution Ownership
        ↓
P5 Transaction / Commit
        ↓
Authoritative Result
```

P5 does not perform semantic decisions, canonization, CMOC writes, or OBJECT INDEX writes.

## 3. Proven runtime behavior

The executable test verifies:

1. first caller acquires the execution boundary;
2. second caller for the same attempt is blocked as `IN_PROGRESS`;
3. commit produces exactly one authoritative effect;
4. completed attempt returns `ALREADY_COMPLETED` and does not create another effect;
5. a new `ATTEMPT_ID` is structurally distinct;
6. the same idempotency key cannot create a second attempt;
7. a conflicting result for an active attempt is rejected;
8. rollback does not create authoritative success;
9. authoritative state survives close/reopen of the SQLite store;
10. two concurrent callers using separate SQLite connections cannot both acquire the same fresh attempt;
11. cross-run execution state is isolated;
12. no semantic/canonization/CMOC/index responsibility leaks into P5.

## 4. Concurrency result

The runtime test exercises two concurrent callers against the same SQLite persistence file:

```
OWNER-E ─┐
         ├── ATT-005
OWNER-F ─┘
```

The observed admissible result set is:

```
LOCK_ACQUIRED
IN_PROGRESS
```

Therefore only one caller acquires the execution boundary for the attempt; the other is explicitly prevented from executing a second authoritative effect.

## 5. Atomicity boundary

The implementation uses SQLite `BEGIN IMMEDIATE` transactions for the local single-host runtime.

The tested invariant is:

```
authoritative effect committed
        iff
authoritative execution record committed
```

A rollback leaves:

- `committed = false`;
- `effect_count = 0`;
- no authoritative success.

## 6. Evidence classification

**P5 runtime transaction/concurrency = IMPLEMENTATION PROVEN for the tested single-host local SQLite component.**

This is stronger than the earlier synthetic P5 contract test because the runtime implementation uses actual SQLite persistence and separate connections for the concurrency case.

## 7. Limitations

This evidence does not establish:

- distributed locking;
- multi-node concurrency;
- high availability;
- external database transactionality;
- atomicity of arbitrary external side effects;
- process supervision;
- production workload/capacity;
- universal production readiness.

These remain bounded by PROD-PROFILE-001 and the P10/O9 limitations.

## 8. Conclusion

P5 has crossed from synthetic contract evidence into a working local runtime implementation.

The current runtime foundation is:

```
P1 Journal
   ↓
P2 RUN / Stage State
   ↓
P3 Attempt / Idempotency
   ↓
P4 Restart / Resume
   ↓
P5 Transaction / Concurrency
```

The next runtime boundary is P6: production adapters for the R1→R10→C1→C2→C3 chain.
