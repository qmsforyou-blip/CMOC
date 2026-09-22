# P3 — ATTEMPT IDENTITY AND IDEMPOTENCY MODEL

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Parent:** PROD-001  
**Depends on:** P1, P2

## 1. Purpose

P3 defines how the runtime distinguishes repeated execution of the same attempt from a new retry and prevents duplicate authoritative effects.

P3 is an execution concern, not a semantic decision layer.

## 2. Identity distinction

The runtime must distinguish:

- RUN_ID — one logical execution;
- STAGE_ID — one contracted processing stage;
- ATTEMPT_ID — one concrete execution attempt of a stage;
- RESULT_ID — identity of the produced stage result;
- IDEMPOTENCY_KEY — identity used to recognize a repeated invocation where required.

## 3. Core rule

A retry of a failed stage receives a new ATTEMPT_ID.

A repeated invocation of the same attempt must not silently create a second authoritative result.

## 4. Candidate outcomes

Repeated execution may resolve to:

- ALREADY_COMPLETED;
- IN_PROGRESS;
- DUPLICATE_ATTEMPT;
- RETRY_REQUIRED;
- NEW_ATTEMPT_REQUIRED;
- CONFLICTING_ATTEMPT;
- IDEMPOTENCY_KEY_MISMATCH.

These are candidate states and require synthetic closure.

## 5. Completed result protection

If a stage attempt already has an authoritative COMPLETED result, another invocation with the same execution identity must not create a second authoritative result.

The historical result remains unchanged.

## 6. Failed attempt protection

A failed attempt remains failed.

A retry creates:

```text
new ATTEMPT_ID
new execution event sequence
new RESULT_ID where a new result is produced
```

The retry does not overwrite the failed attempt.

## 7. Lost acknowledgement

P3 must cover the case:

stage executes successfully
→ result is persisted
→ acknowledgement is lost
→ caller invokes again.

The runtime must recognize the already-authoritative attempt/result rather than producing a duplicate effect.

## 8. CMOC WRITE implication

P3 must provide an execution-level guard against duplicate CMOC WRITE invocation.

It does not decide semantic equivalence or whether a CMOC object should exist.

Those decisions remain outside P3.

## 9. OBJECT INDEX implication

P3 may prevent duplicate synchronization attempts.

It does not decide the semantic content of the index.

## 10. Cross-run isolation

An ATTEMPT_ID, RESULT_ID or IDEMPOTENCY_KEY bound to one RUN_ID must not be accepted as belonging to another RUN_ID.

## 11. Candidate identity record

```yaml
RUN_ID:
STAGE_ID:
ATTEMPT_ID:
RESULT_ID:
IDEMPOTENCY_KEY:
ATTEMPT_STATUS:
AUTHORITATIVE_RESULT:
```

## 12. Required synthetic test

P3 should prove:

1. first attempt accepted;
2. repeated same attempt recognized;
3. completed result protected;
4. failed attempt preserved;
5. retry receives new ATTEMPT_ID;
6. retry receives new RESULT_ID where applicable;
7. lost acknowledgement does not duplicate authoritative effect;
8. cross-run attempt rejected;
9. conflicting attempt identity rejected;
10. idempotency-key mismatch rejected;
11. no semantic / CMOC / OBJECT INDEX responsibility leakage;
12. input/history remains preserved.

## 13. Non-goals

P3 does not establish:

- distributed locking;
- database-specific unique constraints;
- transaction implementation;
- semantic decision logic;
- semantic comparison;
- canonization;
- CMOC schema changes.

## 14. Candidate conclusion

P3 establishes the execution identity needed to make retries and duplicate invocations distinguishable.

The next artifact is the synthetic P3 attempt/idempotency test.