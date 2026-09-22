# ARCHITECTURE CHAIN REVIEW — R1 → REC-001

**Date:** 22-09-2026  
**Status:** REVIEWED / ARCHITECTURE CANDIDATE  
**Scope:** R1–R10, C1, C2, C3, RUN-001, ORCH-001, REC-001

## 1. Current architecture

### Semantic / object layer

SOURCE → DISCOVERY → QUERY / RECONCILIATION → NEW DECISION EVIDENCE → NEW DECISION → NEW_APPROVED → CANONIZATION → CANONICALIZATION_READY → CMOC WRITE → CMOC_WRITE_ACCEPTED → OBJECT INDEX SYNCHRONIZATION → OBJECT INDEX

### Execution layer

RUN → ORCH → REC

The execution layer carries identity, sequencing, recovery, and history control around the semantic/object boundaries. It does not replace them.

## 2. Responsibility matrix

| Layer | Owns | Does not own |
|---|---|---|
| R1 | QUERY / RECONCILIATION | NEW decision |
| R2–R9 | semantic evidence / eligibility | final NEW approval |
| R10 | NEW decision | canonization / persistence |
| C1 | canonical representation preparation | NEW re-decision |
| C2 | CMOC persistence | semantic interpretation |
| C3 | deterministic OBJECT INDEX synchronization | semantic repair |
| RUN | execution identity, lineage, state | sequence policy / semantic meaning |
| ORCH | execution order, invocation, continue/stop | semantic meaning / recovery policy |
| REC | retry/resume/recovery admissibility, history integrity | semantic meaning / normal stage semantics |

No layer is required to own all responsibilities.

## 3. RUN / ORCH / REC non-overlap

RUN answers: Which execution is this?

ORCH answers: What may execute next?

REC answers: What may safely be resumed, retried, or recovered?

This separation is supported by the individual synthetic tests: RUN-001 PASS, ORCH-001 PASS, REC-001 PASS.

## 4. Critical state distinction

Execution state must remain distinct from semantic/object state.

Execution examples: RUN_COMPLETED, RUN_FAILED, RUN_INCOMPLETE, ORCHESTRATION_REJECTED, RESUME_ALLOWED, RETRY_REQUIRED.

These must not be interpreted as NEW_APPROVED, EXISTING_EQUIVALENT, or CANONICAL_OBJECT.

Likewise, semantic states must not be rewritten as execution states.

## 5. Local result versus execution result

A local boundary returns its own result. The execution layer records and controls what happens next.

NEW_REJECTED remains NEW_REJECTED; ORCH may stop execution but does not change that result.

CMOC_WRITE_FAILED remains CMOC_WRITE_FAILED; REC may return RETRY_REQUIRED but does not turn the local failure into success.

## 6. History versus meaning

CMOC is the canonical persisted object representation.

RUN / ORCH / REC are execution history and control.

Execution history cannot become a second source of semantic truth. CMOC state cannot by itself be treated as the complete execution history. The two domains must remain linked by explicit traceability.

## 7. Traceability

Candidate combined lineage remains:

RUN_ID → SOURCE_ID → DISCOVERY_RESULT_ID → RECONCILIATION_RESULT_ID → NEW_DECISION_ID → CANONIZATION_RESULT_ID → CMOC_WRITE_ID → OBJECT_INDEX_SYNC_ID

REC may add recovery/retry references, but must not replace the original lineage.

## 8. Failure model

The combined architecture distinguishes LOCAL_REJECTED, LOCAL_FAILED, DOWNSTREAM_NOT_REACHED, RETRY_REQUIRED, RESUME_ALLOWED, RESUME_BLOCKED, RECOVERY_REJECTED, and INCONSISTENT_HISTORY.

These are execution outcomes. They do not answer semantic questions.

## 9. Partial execution

Partial execution can remain valid and recoverable. Example: DISCOVERY_COMPLETED → RECONCILIATION_COMPLETED → NEW_DECISION_COMPLETED → CANONIZATION_COMPLETED → CMOC_WRITE_FAILED → OBJECT_INDEX_SYNC NOT_REACHED.

REC determines recovery admissibility; ORCH controls subsequent execution. Neither changes completed semantic results.

## 10. Completed-stage protection

REC-001 demonstrated that a completed stage is not silently executed again: COMPLETED + RETRY → ALREADY_COMPLETED, unless a future explicit retry policy establishes another behavior.

This is an execution integrity rule, not semantic equivalence.

## 11. Cross-run isolation

RUN establishes identity. ORCH and REC reject incompatible results. RUN-A result attached to RUN-B is rejected without semantic reconciliation.

## 12. Recovery does not become orchestration

REC may return RESUME_ALLOWED, RETRY_REQUIRED, RESUME_BLOCKED, ALREADY_COMPLETED, RECOVERY_REJECTED, or INCONSISTENT_HISTORY.

ORCH remains responsible for actual sequence control.

Therefore: REC = recovery admissibility/disposition; ORCH = execution.

REC must not become a second workflow engine.

## 13. No semantic leakage

The execution layer must not perform NEW decision, semantic comparison, equivalence resolution, semantic conflict resolution, canonization, relation creation, semantic repair, CMOC mutation, or OBJECT INDEX semantic mutation.

## 14. Current authority model

SEMANTIC AUTHORITY: R1 → R10 → C1 → C2 → C3

EXECUTION AUTHORITY: RUN → ORCH → REC

DERIVED ACCESS: OBJECT INDEX → QUERY

Execution authority means authority over execution control/history only, not over object meaning.

## 15. What is established

At synthetic / isolated boundary level:

1. R1–R10 separate reconciliation, evidence, and NEW decision.
2. C1 separates canonization from NEW decision.
3. C2 separates persistence from semantic interpretation.
4. C3 separates derived indexing from semantic authority.
5. RUN separates execution identity/lineage from semantic meaning.
6. ORCH separates sequence control from semantic meaning.
7. REC separates recovery admissibility from semantic meaning.
8. Cross-run contamination is rejected.
9. Completed-stage duplication is controlled.
10. Recovery cannot silently overwrite prior result identity.
11. Partial execution remains traceable.
12. Execution-layer tests show no CMOC or OBJECT INDEX mutation.

## 16. What is NOT established

Not established: production end-to-end runtime, production execution journal, retry/attempt identity model, transaction semantics, rollback/compensation, concurrency control, distributed locking, process restart behavior, human approval workflow, production persistence of RUN/ORCH/REC state, and production integration of R1–C3 with RUN/ORCH/REC.

## 17. Architectural closure point

The current candidate architecture has reached a useful closure point:

SEMANTIC / OBJECT: R1 → R10 → C1 → C2 → C3

EXECUTION: RUN → ORCH → REC

No additional semantic boundary is currently indicated by this review.

The next work should move toward integration evidence, not another isolated semantic machine.

## 18. Next architectural question

Can the semantic/object layer and the execution layer be connected in one controlled end-to-end synthetic run while preserving every boundary invariant?

The integration test should demonstrate SOURCE → DISCOVERY → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE → OBJECT INDEX SYNC under RUN + ORCH + REC while preserving local result identity, RUN_ID lineage, stage order, recovery rules, no semantic leakage, no unauthorized mutation, and no cross-run contamination.

Only after such an integration test should productionization questions be addressed.

## 19. Review conclusion

R1–C3 + RUN + ORCH + REC are architecturally coherent as a candidate layered model at synthetic / isolated level.

The clean separation is:

WHAT DOES THE OBJECT MEAN? → R1–R10
HOW IS IT CANONICALLY REPRESENTED? → C1
WHERE IS IT PERSISTED? → C2
HOW IS IT INDEXED? → C3
WHICH EXECUTION IS THIS? → RUN
WHAT EXECUTES NEXT? → ORCH
CAN THIS EXECUTION SAFELY CONTINUE / RETRY / RESUME? → REC

The next boundary should therefore be an end-to-end integration test, not a new semantic layer.

**Current status:** architecture candidate reviewed; synthetic boundary evidence accepted; production runtime not established.
