# ARCHITECTURE CHAIN REVIEW — R1 → ORCH-001

**Date:** 22-09-2026  
**Status:** REVIEWED / ARCHITECTURE CANDIDATE  
**Scope:** R1–R10, C1, C2, C3, RUN-001, ORCH-001  
**Purpose:** проверить целостность semantic → persistence → index → execution layers and identify the next architectural boundary without introducing hidden responsibility.

## 1. Current architecture

The current candidate architecture separates two dimensions.

### A. Object / meaning pipeline

    SOURCE
      ↓
    DISCOVERY
      ↓
    QUERY / RECONCILIATION
      ↓
    NEW DECISION EVIDENCE
      ↓
    NEW DECISION
      ↓
    NEW_APPROVED
      ↓
    CANONIZATION
      ↓
    CANONICALIZATION_READY
      ↓
    CMOC WRITE
      ↓
    CMOC_WRITE_ACCEPTED
      ↓
    OBJECT INDEX SYNCHRONIZATION
      ↓
    OBJECT INDEX

### B. Execution pipeline

    RUN
      ↓
    ORCH
      ↓
    invocation of the established boundaries

RUN and ORCH do not replace the object/meaning boundaries.

## 2. Responsibility map

| Layer | Primary responsibility | Must not assume |
|---|---|---|
| R1 | QUERY / RECONCILIATION | NEW decision |
| R2–R9 | evidence and eligibility | final NEW approval |
| R10 | NEW decision | canonization / persistence |
| C1 | canonical representation | NEW re-decision |
| C2 | CMOC persistence | semantic interpretation |
| C3 | deterministic derived index synchronization | semantic repair |
| RUN | execution identity, lineage, state | semantic meaning |
| ORCH | execution sequence and continuation control | semantic meaning |

The boundaries remain conceptually distinct.

## 3. RUN versus ORCH

The distinction is useful and non-overlapping:

    RUN
    = Which execution is this?
      identity + lineage + execution state

    ORCH
    = What may execute next?
      sequence + stage invocation + continue/stop

RUN establishes execution context.

ORCH consumes that context to control progression.

ORCH should not become a second RUN state authority. RUN should not become a hidden workflow engine.

## 4. Local result versus orchestration state

A critical invariant is:

    LOCAL RESULT
          ↓
    ORCH interprets only execution eligibility
          ↓
    ORCH STATE

ORCH may determine continue, stop, reject orchestration step, or downstream not reached.

It must not rewrite the local semantic result.

Examples:

    NEW_REJECTED ≠ ORCHESTRATION_REJECTED
    NEW_APPROVED ≠ ORCHESTRATION_APPROVED
    CMOC_WRITE_ACCEPTED ≠ ORCHESTRATION_DECISION

The first value belongs to the local boundary; the second belongs to execution control.

## 5. Cross-run isolation

RUN and ORCH jointly establish a useful invariant:

> A stage result must not be attached to an incompatible RUN_ID.

RUN provides the execution identity.

ORCH checks that the result belongs to the active execution before continuing.

Neither layer attempts semantic reconciliation of foreign results.

## 6. Failure model

The architecture now distinguishes:

    LOCAL_REJECTED
    LOCAL_FAILED
          ↓
    ORCH records / stops
          ↓
    DOWNSTREAM_NOT_REACHED

This is preferable to turning execution failure into semantic inference.

A future recovery layer may be required, but it must not be silently inserted into ORCH.

## 7. No hidden semantic machine

Across R1–C3 + RUN + ORCH, responsibilities remain separated:

    R1–R10  → semantic/reconciliation decision
    C1      → canonization
    C2      → persistence
    C3      → derived index
    RUN     → execution identity/lineage
    ORCH    → execution control

This is the central architectural result of the review.

No current boundary is required to own all of these responsibilities.

## 8. The execution layer does not change object authority

The current authority model remains:

    CMOC
    = canonical persisted representation

    OBJECT INDEX
    = deterministic derived address/index layer

    QUERY
    = read-only access to OBJECT INDEX

RUN and ORCH add execution traceability/control around these authorities. They do not become a new semantic authority.

## 9. Important unresolved boundary: recovery

The review identifies a new question, but not yet a new machine:

> What happens after LOCAL_FAILED, ORCHESTRATION_FAILED, or an interrupted RUN?

Open cases include retry, resume, compensation, rollback, partial persistence, duplicate invocation, idempotency across boundaries, human intervention, and execution journal recovery.

These are deliberately outside RUN-001 and ORCH-001.

They should not be added to ORCH implicitly, because doing so would turn sequence control into recovery semantics.

## 10. Important unresolved boundary: execution persistence

Another open question is where execution history lives:

    RUN state
    ORCH state
    execution journal
    external runtime

RUN-001 explicitly left this unresolved.

ORCH-001 also leaves persistent orchestration journal unresolved.

Therefore production execution persistence is not yet established.

## 11. End-to-end chain

The current candidate architecture can now be represented as:

                         RUN
                          │
                         ORCH
                          │
SOURCE → DISCOVERY → RECONCILIATION
                          ↓
                    NEW DECISION
                          ↓
                      CANONIZATION
                          ↓
                     CMOC WRITE
                          ↓
                 OBJECT INDEX SYNC
                          ↓
                    OBJECT INDEX

RUN traces the vertical execution.

ORCH controls progression.

The horizontal machines retain their own contracts and decision authority.

## 12. What is established

At synthetic / isolated boundary level:

1. R1 does not turn NO_MATCH into NEW.
2. R2–R9 establish evidence/eligibility rather than hidden NEW decisions.
3. R10 owns the NEW decision.
4. C1 owns canonical representation preparation.
5. C2 owns persistence.
6. C3 owns deterministic derived-index synchronization.
7. RUN binds end-to-end lineage and execution identity.
8. ORCH controls stage order and continuation.
9. Cross-run contamination is rejected.
10. Local rejection/failure is not semantically reinterpreted by execution layers.
11. Execution layers do not mutate CMOC or OBJECT INDEX directly.
12. The boundaries remain individually testable.

## 13. What is NOT established

The review does not establish production runtime, production orchestration, production recovery, transaction semantics, concurrency semantics, persistent execution journal, retry/resume semantics, compensation/rollback, human intervention protocol, or production end-to-end integration.

These are implementation/architecture questions for a subsequent layer.

## 14. Architectural conclusion

The review supports the following model:

    SEMANTIC / OBJECT LAYER
    R1 → R10 → C1 → C2 → C3

    EXECUTION LAYER
    RUN → ORCH

This is a clean separation.

The next architectural question should therefore not be another semantic boundary.

> How does the execution layer safely handle interruption, retry, resume, idempotency, and recovery without taking over semantic responsibility from R1–C3?

That question should be investigated as a separate candidate boundary only after its contract is formulated.

For now, do not name it C4.

## 15. Review status

**R1–C3:** reviewed  
**RUN-001:** PASS / evidence accepted  
**ORCH-001:** PASS / evidence accepted  
**Current architecture:** coherent candidate, synthetic/isolated only  
**Next candidate area:** execution recovery / retry / resume boundary