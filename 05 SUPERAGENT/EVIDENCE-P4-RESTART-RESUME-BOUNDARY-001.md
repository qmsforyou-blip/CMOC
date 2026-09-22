# EVIDENCE-P4 — RESTART / RESUME BOUNDARY

**Status:** ACCEPTED  
**Test:** `05 SUPERAGENT/test_p4_restart_resume_boundary.py`  
**Gate result:** PASS

## 1. Scope

P4 establishes the synthetic runtime boundary for restarting an interrupted RUN and determining whether execution may resume.

The test verifies that restart disposition is derived from persisted execution history and state, while preserving RUN identity, attempt identity, authoritative results, and prior history.

P4 does not perform semantic decisions, semantic comparison, canonization, CMOC mutation, OBJECT INDEX mutation, or semantic repair.

## 2. Test result

The P4 gate passed all 12 branches.

| Case | Result |
|---|---|
| P4-01 valid restart | RESUME_ALLOWED |
| P4-02 deterministic reconstruction | persisted state reproduced from journal |
| P4-03 completed stage | ALREADY_COMPLETED |
| P4-04 failed stage | RETRY_REQUIRED |
| P4-05 interrupted RUNNING without result | RECOVERY_REQUIRES_REVIEW |
| P4-06 RUNNING with persisted authoritative result | ALREADY_COMPLETED |
| P4-07 predecessor/state boundary violation | INCONSISTENT_HISTORY |
| P4-08 inconsistent history | INCONSISTENT_HISTORY |
| P4-09 cross-run lineage | RUN_REJECTED |
| P4-10 repeated restart | ALREADY_COMPLETED; idempotent |
| P4-11 responsibility isolation | all prohibited operations false |
| P4-12 history/input preservation | preserved |

## 3. Evidence points

### 3.1 Deterministic restart

A valid RUN can be reconstructed from journal history into the persisted operational state.

The test demonstrates:

`JOURNAL_REDUCE(RUN_ID) = PERSISTED_RUN_STATE`

for the valid restart case.

### 3.2 Completed result protection

A completed stage is not re-executed merely because the process restarted.

The disposition is:

`ALREADY_COMPLETED`

The authoritative result remains unchanged.

### 3.3 Failed stage

A failed stage is not silently resumed as if it had succeeded.

The disposition is:

`RETRY_REQUIRED`

The prior `ATTEMPT_ID` remains identifiable. Retry remains subject to the P3 attempt-identity boundary.

### 3.4 Interrupted RUNNING stage

An interrupted RUNNING stage without an authoritative result is not treated as successful.

The disposition is:

`RECOVERY_REQUIRES_REVIEW`

This prevents restart logic from inventing a successful outcome.

### 3.5 Persisted authoritative result

A RUNNING journal state with an already persisted authoritative result resolves to:

`ALREADY_COMPLETED`

This provides the restart-side protection against repeating an already effective operation.

### 3.6 History inconsistency

When journal reduction does not equal persisted state, P4 returns:

`INCONSISTENT_HISTORY`

P4 does not repair the discrepancy semantically.

### 3.7 Cross-run isolation

Foreign lineage is rejected as:

`RUN_REJECTED`

No foreign RUN, stage, result, or attempt is imported.

## 4. Responsibility isolation

The test confirms:

`semantic_decision_performed = false`  
`semantic_comparison_performed = false`  
`canonization_performed = false`  
`cmoc_mutation_performed = false`  
`object_index_mutation_performed = false`  
`semantic_repair_performed = false`  
`cross_run_import_performed = false`

Therefore P4 remains an execution/recovery boundary and does not absorb responsibility from R1-R10, C1-C3, ORCH, or REC.

## 5. Architectural conclusion

P4 closes the minimum synthetic restart/resume question:

**after restart, execution state can be reconstructed deterministically; completed effects remain protected; failed and interrupted stages are not silently treated as successful; inconsistent history is surfaced; and cross-run lineage is rejected.**

P4 does not yet establish OS/process supervision, database transactionality, distributed locking, or durable infrastructure behavior. Those remain later production-engineering concerns.

**Evidence status: ACCEPTED.**
