# REC-001 — EXECUTION RECOVERY / RETRY / RESUME BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Scope:** synthetic / isolated investigation  
**Depends on:** RUN-001, ORCH-001, R1-C3 architecture chain

## 1. Purpose

REC-001 investigates whether interruption, failure, retry, resume, and recovery require a separate execution boundary above RUN and ORCH.

The architectural question is:

> How can an interrupted or failed execution be resumed or retried without changing the semantic responsibility of R1–C3 and without silently duplicating or corrupting execution results?

REC-001 is not a semantic machine and is not a production recovery specification.

## 2. Why REC is considered

RUN-001 establishes execution identity and lineage.

ORCH-001 establishes execution sequence and continuation control.

Neither contract yet defines what happens when execution is interrupted or when a stage fails after a partial execution.

Relevant cases include:

- LOCAL_FAILED;
- ORCHESTRATION_FAILED;
- interrupted RUN;
- retry of a failed stage;
- resume after an interruption;
- repeated invocation of an already completed stage;
- partial persistence;
- duplicate downstream invocation;
- human intervention.

These cases should not be silently absorbed into ORCH because that would turn sequence control into recovery semantics.

## 3. Architectural responsibility

REC-001 may:

- identify a recoverable execution state;
- determine whether a retry/resume request is structurally admissible;
- preserve the original RUN_ID and lineage when resuming the same execution;
- create an explicitly related retry/child execution identity when the contract requires it;
- prevent duplicate execution where an existing completed result is already authoritative;
- record recovery disposition;
- hand control back to ORCH after a valid recovery decision;
- stop recovery when required evidence of prior execution is missing or inconsistent.

REC-001 must not:

- decide NEW;
- perform semantic comparison;
- resolve semantic conflict;
- canonize;
- mutate CMOC;
- mutate OBJECT INDEX directly;
- rewrite local semantic results;
- invent missing lineage;
- silently convert a failed result into a successful result;
- silently merge two RUNs;
- decide that two executions are semantically equivalent.

## 4. RUN / ORCH / REC distinction

    RUN
    = Which execution is this?
      identity + lineage + state

    ORCH
    = What may execute next?
      sequence + continuation control

    REC
    = What may safely be retried or resumed?
      recovery admissibility + recovery disposition

REC must return execution control to ORCH rather than becoming a second orchestration engine.

## 5. Recovery disposition

Candidate recovery outcomes:

- RECOVERY_ACCEPTED;
- RECOVERY_REJECTED;
- RETRY_REQUIRED;
- RESUME_ALLOWED;
- RESUME_BLOCKED;
- ALREADY_COMPLETED;
- INCONSISTENT_HISTORY;
- RECOVERY_REQUIRES_REVIEW.

These are execution states/dispositions, not semantic object states.

## 6. Same RUN versus new RUN

REC-001 must distinguish at least:

### Resume

Continuation of the same execution.

    original RUN_ID preserved
    lineage preserved
    missing downstream stages may continue

### Retry

Repeated attempt to execute a failed stage.

The retry must retain explicit relationship to the original execution and must not silently overwrite the original result.

### New RUN

A separate execution, even if it processes the same SOURCE_ID.

New RUN identity must not be inferred to be a continuation of the old RUN.

These three cases must remain distinguishable.

## 7. Completed-stage protection

If a stage has already produced an authoritative completed result, REC must not silently request a second execution as though the first result did not exist.

Candidate outcomes:

    completed result + same requested continuation
        → ALREADY_COMPLETED

    completed result + explicit retry policy
        → RETRY_ALLOWED only if explicitly contracted

    completed result + conflicting replacement
        → RECOVERY_REQUIRES_REVIEW or INCONSISTENT_HISTORY

REC does not decide which semantic result is correct.

## 8. Partial execution

REC must preserve the distinction between:

    stage completed
    stage failed
    stage not reached
    stage result missing
    execution history inconsistent

Example:

    DISCOVERY_COMPLETED
    RECONCILIATION_COMPLETED
    NEW_DECISION_COMPLETED
    CANONIZATION_COMPLETED
    CMOC_WRITE_FAILED
    INDEX_SYNC not reached

Recovery must not reinterpret the semantic outputs already produced.

## 9. Idempotency boundary

REC-001 must investigate, not assume, idempotency.

At minimum distinguish:

- repeated request with identical completed input;
- retry after explicit failure;
- duplicate request with incompatible payload;
- same RUN_ID with changed lineage;
- new RUN_ID with same source.

Idempotency is an execution property. It must not be established through semantic equivalence.

## 10. History integrity

Recovery must reject or require review when execution history cannot be trusted.

Examples:

- missing required predecessor result;
- conflicting result IDs for the same stage;
- result belongs to another RUN_ID;
- same RUN_ID reused with incompatible SOURCE_ID;
- completed state without corresponding result;
- downstream completion recorded while predecessor is absent.

REC must not repair such history by inference.

## 11. Human intervention

A future production system may require explicit human intervention.

REC may record:

    RECOVERY_REQUIRES_REVIEW

but must not turn a human-review state into automatic approval.

Human intervention semantics remain an open production question.

## 12. LLM boundary

LLM assistance is not required for recovery identity or execution history validation.

LLM must not:

- infer missing execution lineage;
- invent prior results;
- merge RUN histories;
- decide that a failed stage actually succeeded;
- determine semantic equivalence of retry outputs;
- silently repair history.

## 13. Synthetic-first-test boundary

The first REC-001 test should be synthetic and isolated.

It should demonstrate at minimum:

1. valid resume after an interrupted RUN;
2. valid retry after local failure;
3. same RUN remains distinguishable from new RUN;
4. completed stage is protected from silent duplicate execution;
5. missing predecessor blocks recovery;
6. cross-run result blocks recovery;
7. incompatible RUN_ID reuse is rejected;
8. conflicting stage history is rejected or requires review;
9. partial execution remains traceable;
10. no semantic decision;
11. no canonization;
12. no CMOC mutation;
13. no OBJECT INDEX mutation;
14. no semantic repair.

## 14. Open architectural questions

The synthetic boundary does not settle:

- whether retries receive child RUN_IDs or attempt IDs;
- whether recovery history is append-only;
- whether a recovery journal is part of RUN or separate;
- transaction/rollback semantics;
- compensation semantics;
- concurrent recovery attempts;
- distributed locks;
- operator approval workflow;
- retention and audit policy;
- recovery across production process restarts.

These require separate evidence.

## 15. Architectural invariant

> Recovery may decide whether an execution can safely continue, retry, or resume; it must not decide what the processed object means.

Therefore:

    RECOVERY_ACCEPTED ≠ NEW_APPROVED
    RETRY_ALLOWED ≠ SEMANTIC_EQUIVALENT
    RESUME_ALLOWED ≠ CANONICAL_OBJECT

## 16. Candidate architecture

    RUN
      │
      ▼
    ORCH
      │
      ├── normal execution
      │
      ▼
    R1 → R10 → C1 → C2 → C3
      ▲
      │
    REC
      │
      └── retry / resume / recovery

REC is a candidate recovery boundary around execution, not around semantic meaning.

## 17. Current status

**DESIGN / ARCHITECTURE CANDIDATE**

REC-001 is a hypothesis. It must first pass an isolated synthetic boundary test before being promoted.