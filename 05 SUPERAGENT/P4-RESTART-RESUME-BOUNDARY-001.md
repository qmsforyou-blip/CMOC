# P4 — RESTART / RESUME BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE

## 1. Purpose

P4 defines the production runtime boundary for restarting an interrupted RUN and determining whether execution may resume.

P4 operates on execution state and lineage. It does not reinterpret semantic results.

## 2. Inputs

Minimum input:

- RUN_ID
- persisted RUN/stage state from P2
- append-only execution journal from P1
- ATTEMPT identity from P3
- stage/result lineage
- recovery disposition from REC-001 where applicable

## 3. Restart sequence

Candidate deterministic sequence:

`LOAD JOURNAL → VALIDATE HISTORY → REDUCE JOURNAL → LOAD PERSISTED STATE → COMPARE PROJECTION → IDENTIFY INTERRUPTED STAGE → CHECK ATTEMPT STATE → DETERMINE RESUME DISPOSITION`

The sequence must preserve RUN_ID and existing lineage.

## 4. Resume admissibility

Resume may be considered only when:

1. RUN_ID is valid and consistent;
2. journal history is structurally valid;
3. persisted projection agrees with the journal reduction;
4. predecessor stages required by the contract are completed;
5. the interrupted stage is identifiable;
6. the existing ATTEMPT_ID is either safely resumable or a new retry attempt is explicitly required;
7. no authoritative completed result is replaced;
8. no cross-run result is imported.

## 5. Candidate outcomes

- `RESUME_ALLOWED`
- `RESUME_BLOCKED`
- `RETRY_REQUIRED`
- `ALREADY_COMPLETED`
- `INCONSISTENT_HISTORY`
- `RUN_REJECTED`
- `RECOVERY_REQUIRES_REVIEW`

P4 must not silently convert a blocked resume into a retry.

## 6. Attempt handling

### Completed stage

A completed authoritative stage is not re-executed merely because the process restarted.

Expected disposition:

`ALREADY_COMPLETED`

### Failed stage

A failed stage may be resumed/retried only through an explicit recovery path.

Retry requires a new ATTEMPT_ID under P3.

### Interrupted RUNNING stage

An interrupted RUNNING stage must not automatically be treated as successful.

P4 must distinguish:

- authoritative completed result already persisted;
- attempt still recoverable;
- attempt outcome unknown;
- retry required.

Where outcome is unknown, P4 must not invent success or semantic meaning.

## 7. Restart idempotency

A restart must not create a second authoritative effect when the original result was already persisted.

The P3 idempotency boundary remains authoritative for repeated attempt identity.

## 8. State consistency

Required invariant:

`JOURNAL_REDUCE(RUN_ID) = PERSISTED_RUN_STATE`

If the invariant fails, P4 returns `INCONSISTENT_HISTORY` or `RUN_REJECTED`; it does not repair history semantically.

## 9. Cross-run isolation

A restart of RUN-A may consume only lineage belonging to RUN-A.

Foreign RUN_ID, SOURCE_ID, stage result, ATTEMPT_ID, or persisted state is rejected.

## 10. Responsibility boundary

P4 must NOT:

- make a NEW decision;
- perform semantic equivalence;
- resolve conflicts;
- perform semantic comparison;
- perform canonization;
- mutate CMOC;
- mutate OBJECT INDEX;
- rewrite semantic evidence;
- invent missing lineage;
- silently replace a failed stage;
- convert rejection into approval.

P4 may invoke ORCH and REC after producing a structurally valid recovery disposition.

## 11. Failure states

- `P4_REJECTED`
- `INCONSISTENT_HISTORY`
- `RESUME_BLOCKED`
- `RECOVERY_REQUIRES_REVIEW`

All failure/rejection history remains preserved.

## 12. Synthetic test boundary

The first P4 test is synthetic and isolated.

It must demonstrate at minimum:

1. restart of a valid RUN;
2. deterministic state reconstruction;
3. completed stage protected;
4. failed stage requires explicit recovery;
5. interrupted RUNNING stage is not assumed successful;
6. valid resume when predecessor and state conditions permit;
7. resume blocked when predecessor is incomplete;
8. inconsistent journal/state detected;
9. cross-run contamination rejected;
10. idempotent restart after persisted result;
11. no semantic responsibility leakage;
12. input/history preservation.

P4 does not yet establish OS/process supervision, database transactions, distributed locks, or durable infrastructure behavior.
