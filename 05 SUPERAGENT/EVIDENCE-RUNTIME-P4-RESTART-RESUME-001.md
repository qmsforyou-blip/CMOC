# EVIDENCE — RUNTIME P4 RESTART / RESUME — 001

**Status:** ACCEPTED  
**Date:** 22-09-2026  
**Scope:** first real runtime implementation of P4  
**Implementation:** `05 SUPERAGENT/runtime_restart_resume.py`  
**Dependencies:** P1/P2 runtime state store + P3 attempt store  
**Test:** `05 SUPERAGENT/test_runtime_restart_resume.py`

## 1. Result

User executed:

```
py "05 SUPERAGENT\test_runtime_restart_resume.py"
```

Result:

```
RUNTIME RESTART RESUME TEST: PASS
```

## 2. Runtime boundary

P4 consumes durable execution state from P1/P2 and attempt identity from P3:

```
P1 Journal
   ↓
P2 RUN / Stage State
   ↓
P3 Attempt / Idempotency
   ↓
P4 Restart / Resume
```

P4 determines a structural recovery disposition after restart. It does not reinterpret semantic results.

## 3. Proven runtime behavior

The executable test verifies:

1. interrupted RUNNING attempt → RESUME_ALLOWED;
2. failed stage paired with explicit P3 attempt failure → RETRY_REQUIRED;
3. authoritative attempt result → ALREADY_COMPLETED;
4. terminal RUN remains protected after restart;
5. unknown RUN → RUN_REJECTED;
6. missing attempt identity → RECOVERY_REQUIRES_REVIEW;
7. failed attempt remains preserved and retry uses a distinct ATTEMPT_ID;
8. cross-run/source identity is rejected;
9. P2 journal/state projection remains deterministic;
10. no semantic/canonization/CMOC/index responsibility leakage;
11. decisions survive closing and reopening the SQLite stores;
12. journal remains the execution-history source.

## 4. Important boundary finding

During initial integration testing, P4 correctly returned a non-retry disposition when P2 contained `STAGE_FAILED` but P3 still recorded the attempt as `IN_PROGRESS`.

The implementation was corrected by adding an explicit P3 transition:

```
AttemptStore.mark_failed()
```

The final test therefore verifies the intended cross-layer protocol:

```
P2: STAGE_FAILED
        ↓
P3: ATTEMPT FAILED
        ↓
P4: RETRY_REQUIRED
```

This is a runtime integration correction, not a semantic reinterpretation.

## 5. Evidence classification

**P4 runtime restart/resume = IMPLEMENTATION PROVEN for the tested single-host local SQLite component.**

The result demonstrates that restart disposition is based on durable execution state and explicit attempt identity.

## 6. Limitations

This evidence does not establish:

- distributed restart/resume;
- multi-node execution;
- distributed locking;
- external database transactionality;
- high availability;
- OS/container process supervision;
- production capacity;
- universal production readiness.

Those remain bounded by PROD-PROFILE-001 and the existing operational limitations.

## 7. Conclusion

P4 has crossed from synthetic contract evidence into a working local runtime implementation.

The proven runtime foundation is now:

```
P1 Journal
   ↓
P2 RUN / Stage State
   ↓
P3 Attempt / Idempotency
   ↓
P4 Restart / Resume
```

The next engineering boundary should continue from this runtime foundation rather than introduce a new architectural layer without an actual implementation need.
