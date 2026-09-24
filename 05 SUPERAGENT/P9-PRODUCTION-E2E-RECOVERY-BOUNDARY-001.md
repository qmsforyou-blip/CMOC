# P9 — PRODUCTION END-TO-END RECOVERY BOUNDARY

**Status:** ACCEPTED  
**Layer:** production runtime realization  
**Scope:** RUN + ORCH + REC + R1-R10 + C1 + P7/C2 + P8/C3

## 1. Purpose

P9 is the first production end-to-end gate.

It does not introduce a new semantic machine.

It verifies that the already established execution, semantic, persistence, and synchronization boundaries operate as one traceable production chain.

Candidate chain:

`SOURCE`
→ `DISCOVERY`
→ `RECONCILIATION`
→ `NEW DECISION`
→ `CANONIZATION`
→ `P7 / CMOC WRITE`
→ `P8 / OBJECT INDEX SYNC`
→ `RUN COMPLETION`

Recovery path:

`stage failure`
→ `RECOVERY`
→ `RETRY / RESUME`
→ `ORCH`
→ `downstream continuation`

## 2. Required production boundaries

P9 binds the following previously accepted boundaries:

- R1-R10 semantic decision chain;
- C1 canonization;
- C2/P7 CMOC persistence;
- C3/P8 OBJECT INDEX synchronization;
- RUN execution identity and lineage;
- ORCH execution sequencing;
- REC recovery/retry/resume;
- P1 execution journal;
- P2 persisted operational state;
- P3 attempt identity/idempotency;
- P4 restart/resume;
- P5 transaction/concurrency boundary;
- P6 production adapter boundary.

P9 does not replace any of these contracts.

## 3. Production E2E identity

One production E2E run must preserve:

`RUN_ID`

through every stage.

Minimum lineage:

`RUN_ID`
→ `SOURCE_ID`
→ `DISCOVERY_RESULT_ID`
→ `RECONCILIATION_RESULT_ID`
→ `NEW_DECISION_ID`
→ `CANONIZATION_RESULT_ID`
→ `CMOC_WRITE_ID`
→ `OBJECT_INDEX_SYNC_ID`

Every authoritative downstream result must belong to the same RUN unless an explicit recovery contract creates a controlled child/retry identity.

## 4. Successful path

The successful gate must demonstrate:

1. RUN creation;
2. SOURCE/DISCOVERY result;
3. RECONCILIATION result;
4. NEW decision result;
5. C1 `CANONICALIZATION_READY`;
6. P7 `CMOC_WRITE_ACCEPTED`;
7. P8 `INDEX_SYNCHRONIZED` or explicit idempotent equivalent;
8. final RUN completion;
9. journal contains the complete execution lineage;
10. persisted operational state agrees with journal reduction.

## 5. Failure and recovery path

At least one real persistence-stage failure must be injected after upstream semantic work has completed.

Required sequence:

`stage failure`
→ failure persisted
→ RUN remains non-terminal
→ REC evaluates recovery
→ new ATTEMPT_ID where retry is required
→ ORCH resumes control
→ P7/P8 continuation
→ successful completion.

The failed attempt must remain in history.

The recovery path must not rewrite or erase the failed result.

## 6. Restart path

P9 must also demonstrate at least one restart boundary.

Candidate scenario:

- RUN is interrupted while a stage is operationally active;
- process execution is stopped;
- journal remains available;
- persisted RUN state remains available;
- restart loads journal and persisted state;
- projection is reconstructed;
- interrupted stage is identified;
- REC determines the admissible disposition;
- ORCH continues only after recovery disposition.

The system must not assume an interrupted stage succeeded merely because execution stopped after invocation.

## 7. Idempotency

P9 must prove that repeated execution of the same authoritative attempt does not create duplicate effects.

At minimum:

- repeated P7 invocation is idempotent;
- repeated P8 synchronization is idempotent;
- completed stage is protected;
- retry receives a new ATTEMPT_ID;
- failed attempt remains historical.

## 8. Physical persistence

Unlike the earlier synthetic E2E gate, P9 must use:

- actual local CMOC repository persistence for P7;
- actual deterministic OBJECT INDEX build for P8;
- durable execution journal/state fixtures for RUN/P1/P2;
- explicit attempt identity for P3.

The test must not replace P7/P8 with semantic mocks.

## 9. Semantic boundary

P9 must not alter the established semantic decision chain.

The production E2E gate only consumes semantic results.

It must not:

- make a new semantic decision;
- reinterpret NEEDS_REVIEW;
- convert rejection to approval;
- perform semantic comparison;
- canonize independently of C1;
- resolve semantic conflicts;
- invent object identity.

## 10. Failure isolation

P9 must distinguish:

- semantic rejection;
- execution failure;
- persistence failure;
- synchronization failure;
- recovery rejection;
- lineage failure;
- inconsistent operational state.

One class must not be silently converted into another.

## 11. Post-completion invariants

After successful completion:

- CMOC representation exists and is verified;
- OBJECT INDEX representation is synchronized;
- journal is complete;
- persisted operational state is consistent;
- failed prior attempts remain in history;
- no duplicate authoritative CMOC effect exists;
- no duplicate authoritative index representation exists;
- RUN lineage is complete;
- no semantic responsibility leaked into execution/recovery/persistence layers.

## 12. First production gate

The first P9 gate may use an isolated dedicated test object and dedicated RUN namespace inside the real repository.

It must leave unrelated CMOC objects unchanged.

The gate is not a production deployment benchmark.

It does not establish distributed high availability, network failure semantics, multi-process database guarantees, or production throughput.

## 13. Architectural conclusion sought

P9 should establish:

**the CMOC pipeline can execute from semantic decision through canonicalization, real CMOC persistence, deterministic OBJECT INDEX synchronization, failure recovery, retry/resume, and final RUN completion while preserving identity, history, idempotency, and semantic responsibility boundaries.**

**Status:** DESIGN / ARCHITECTURE CANDIDATE
