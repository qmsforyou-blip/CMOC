# ORCH-001 — EXECUTION ORCHESTRATION BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Scope:** synthetic / isolated investigation  
**Depends on:** RUN-001, R1-C3 architecture chain

## 1. Purpose

ORCH-001 investigates whether a separate execution orchestration boundary is required to move a RUN through already established boundaries:

SOURCE → DISCOVERY → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE → OBJECT INDEX SYNCHRONIZATION.

RUN-001 establishes lineage and execution state. ORCH-001 asks a different question:

> Who is responsible for invoking the next already-defined boundary, checking its result, and stopping or continuing the run?

ORCH-001 is therefore an execution-control boundary, not a semantic decision layer.

## 2. Architectural responsibility

ORCH-001 may:

- select the next contracted machine/boundary from the established execution sequence;
- pass the output of one boundary as the input of the next;
- preserve RUN_ID and lineage;
- verify that the returned result is attached to the same RUN;
- stop execution when a local boundary rejects or fails;
- record the execution state;
- prevent execution of a downstream stage when its required predecessor result is absent;
- distinguish local result status from orchestration status.

ORCH-001 must not:

- decide NEW;
- decide semantic equivalence;
- decide conflict;
- perform semantic comparison;
- canonize;
- mutate CMOC;
- mutate OBJECT INDEX directly;
- create unsupported relations;
- repair semantic evidence;
- infer missing lineage;
- silently replace a failed stage with another stage;
- reinterpret a local rejection as approval.

## 3. RUN versus ORCH

The distinction is:

**RUN**
- identifies and traces the execution;
- binds lineage;
- records state.

**ORCH**
- controls the sequence of execution;
- invokes the next contracted boundary;
- accepts/rejects the returned execution result at the orchestration level;
- stops or continues the RUN.

Neither layer owns semantic meaning.

## 4. Candidate execution model

```
RUN_CREATED
   ↓
ORCH → DISCOVERY
   ↓
ORCH → RECONCILIATION
   ↓
ORCH → NEW DECISION
   ↓
ORCH → CANONIZATION
   ↓
ORCH → CMOC WRITE
   ↓
ORCH → OBJECT INDEX SYNCHRONIZATION
   ↓
RUN_COMPLETED
```

The orchestration layer does not implement these machines. It invokes their existing contracts.

## 5. Result handling

For each stage ORCH receives a result with at least:

```yaml
RUN_ID:
STAGE_ID:
STAGE_STATUS:
RESULT_ID:
TRACEABILITY:
```

The orchestration decision is limited to execution control:

- accepted/complete result → continue;
- local rejection → stop or follow explicitly contracted rejection path;
- local failure → stop or follow explicitly contracted recovery path;
- missing/foreign result → reject orchestration step;
- invalid stage transition → reject orchestration step.

A local semantic result must not be rewritten by ORCH.

## 6. Boundary invariant

```
ORCH decides:
    whether execution may proceed.

ORCH does not decide:
    what the processed object means.
```

In particular:

```
ORCH_ACCEPTED ≠ NEW_APPROVED
ORCH_COMPLETED ≠ SEMANTIC_EQUIVALENT
ORCH_COMPLETED ≠ CANONICAL_OBJECT
```

## 7. Cross-run isolation

ORCH must reject a stage result when its RUN_ID differs from the active RUN_ID.

ORCH must not infer that two different RUN_ID values represent the same execution.

## 8. Failure isolation

A failure in one boundary remains a failure of that boundary.

ORCH may record:

```
LOCAL_REJECTED
LOCAL_FAILED
DOWNSTREAM_NOT_REACHED
ORCHESTRATION_REJECTED
ORCHESTRATION_FAILED
```

but may not transform these into semantic conclusions.

## 9. LLM boundary

LLM assistance is not required for orchestration identity or state transition.

If LLM assistance is later used for formatting, diagnostics, or operator-facing explanation, it must not:

- infer lineage;
- choose a different stage because the contracted stage failed;
- repair missing evidence;
- approve semantic decisions;
- merge runs.

## 10. Synthetic-first-test boundary

The first ORCH-001 test should be synthetic and isolated.

It should demonstrate at minimum:

1. valid sequential execution;
2. correct stage invocation order;
3. downstream blocked when predecessor is absent;
4. local rejection stops execution;
5. local failure stops execution;
6. cross-run result rejected;
7. invalid stage transition rejected;
8. completed chain reaches RUN_COMPLETED;
9. ORCH does not perform semantic decision;
10. ORCH does not perform canonization;
11. ORCH does not mutate CMOC;
12. ORCH does not mutate OBJECT INDEX.

## 11. Open architectural questions

The synthetic test does not settle:

- whether ORCH is a standalone machine or part of a future runtime;
- whether execution is synchronous/asynchronous;
- retry semantics;
- transaction boundaries;
- concurrency;
- compensation/rollback;
- persistent orchestration journal;
- whether failed runs can be resumed under the same RUN_ID;
- how human intervention enters the execution chain.

These questions remain outside ORCH-001 until evidence requires them.

## 12. Candidate conclusion

ORCH-001 should be promoted only if the isolated test demonstrates that execution sequencing can be separated cleanly from semantic responsibility.

The intended architecture is:

```
RUN = lineage + execution identity
ORCH = sequence control
R1-C3 = semantic / persistence boundaries
```

No production orchestration is established by this document alone.
