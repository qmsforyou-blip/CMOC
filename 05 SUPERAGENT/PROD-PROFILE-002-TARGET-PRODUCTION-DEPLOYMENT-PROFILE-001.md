# PROD-PROFILE-002 — TARGET PRODUCTION DEPLOYMENT PROFILE

**Status:** CONFIRMED TARGET PROFILE  
**Date:** 24-09-2026  
**Predecessor:** POST-P10-ARCHITECTURE-REVIEW-001  
**Purpose:** define the first concrete target production profile for CMOC/Superagent before selecting further operational engineering work.

---

## 1. Purpose of this profile

This profile converts the architectural baseline into a concrete first deployment target.

It deliberately defines a **single-host, controlled engineering environment** rather than assuming distributed production infrastructure.

The profile is a target for the next operationalization phase. It is not a claim that all capabilities listed here are already implemented.

The governing rule is:

> **Не проектировать инфраструктуру под гипотетический масштаб. Проектировать её под реальный режим использования, а следующий уровень сложности вводить только тогда, когда появляется конкретное требование.**

---

## 2. Confirmed use profile

The target profile is explicitly fixed as:

| Question | Confirmed decision |
|---|---|
| User | **we ourselves / single expert user** |
| Environment | **Windows + Obsidian + local runtime** |
| CMOC | **Git repository** |
| SOURCE | **manual input; automatically split into packages** |
| Superagent start | **manual** |
| Automation | **the entire contracted pipeline** |
| Human participation | **NEW / conflict / review / publication** |
| Scale | **dozens of sources** |

“Everything is automated” means that the contracted deterministic/operational pipeline executes automatically after a manual start. It does not mean that runtime infrastructure bypasses the established human semantic authority.

Human participation remains at the explicit decision boundaries: NEW, conflict, review and publication.

---

## 3. Intended system

CMOC/Superagent is treated as an engineering knowledge system for:

SOURCE
→ DISCOVERY
→ RECONCILIATION
→ NEW DECISION
→ CANONIZATION
→ CMOC WRITE
→ OBJECT INDEX
→ QUERY / USE

with:

RUN / ORCH / REC

providing execution identity, sequencing, recovery and history.

The semantic authority remains:

R1 → R10 → C1 → C2 → C3

The execution authority remains:

RUN → ORCH → REC

Operational infrastructure must not acquire semantic authority.

---

## 4. Initial deployment profile

### 4.1 Deployment topology

**Target:** single-host controlled deployment.

The initial production-realization target does not require:

- multi-node deployment;
- high availability;
- distributed locking;
- automatic failover;
- network-partition tolerance across nodes.

These remain outside the first profile unless an actual use case makes them necessary.

### 4.2 Host environment

The confirmed host environment is:

- Windows workstation;
- local CMOC working tree;
- Obsidian as the engineering workspace;
- Git/GitHub as versioned repository infrastructure;
- Python runtime invoked through `py`.

The profile should remain portable enough that the runtime can later be moved to a dedicated host without changing semantic contracts.

### 4.3 CMOC persistence

For the first profile:

**Git repository + filesystem representation** is the canonical engineering persistence environment.

CMOC canonical objects are persisted as repository files.

Git provides:

- version history;
- change traceability;
- reproducibility;
- controlled synchronization;
- rollback at repository level.

A separate external database is not required for the first target profile.

### 4.4 OBJECT INDEX

OBJECT INDEX remains a deterministic derived representation.

It is rebuilt from canonical CMOC state using the existing deterministic builder.

It is not an independent semantic store.

The rule remains:

CMOC canonical representation
→ deterministic OBJECT INDEX

not:

CMOC ↔ independently editable index.

---

## 5. Source ingestion

### Target mode

Controlled source ingestion.

A SOURCE_PACKAGE may contain one or multiple files belonging to the same logical source.

The existing SOURCE contract remains authoritative:

SOURCE_ID
→ SOURCE_PACKAGE
→ BATCH_ID
→ PASS
→ OUTPUT

SOURCE is introduced manually. After introduction, the system automatically performs the contracted package handling, including source splitting into SOURCE_PACKAGE/BATCH units.

Automatic discovery of arbitrary external sources is outside this first profile.

---

## 6. Superagent execution

### Initial mode

Superagent is started manually from the Windows engineering environment. After start, the contracted pipeline is intended to execute automatically, subject to the established semantic and human-review boundaries.

The runtime must preserve:

- RUN_ID;
- SOURCE_ID;
- BATCH_ID;
- STAGE_ID;
- ATTEMPT_ID;
- RESULT_ID;
- stage history;
- recovery history.

The execution chain remains:

RUN
→ ORCH
→ REC

The runtime must not silently convert execution failures into semantic results.

---

## 7. Human participation

The first profile assumes **human-supervised engineering knowledge extraction**, with human intervention at explicit decision boundaries.

Human review remains available where the established architecture produces:

- NEEDS_REVIEW;
- ambiguous reconciliation;
- insufficient scope;
- unresolved semantic comparison;
- rejected NEW decision;
- canonization rejection;
- persistence conflict;
- recovery requiring review.

The runtime may automate deterministic execution around these states.

It must not bypass the contracted semantic decision boundary merely to obtain a fully automatic run.

---

## 8. Automation target

The first operationalization target is automation of the **entire contracted pipeline**, not removal of human semantic authority.

Target automation:

- source package handling;
- RUN creation;
- stage execution;
- stage result persistence;
- journal/state persistence;
- retry/resume;
- idempotency;
- CMOC persistence;
- OBJECT INDEX synchronization;
- traceability;
- deterministic verification.

Not automatically delegated to infrastructure:

- semantic NEW decision;
- semantic equivalence;
- semantic conflict;
- semantic comparison;
- semantic repair;
- unsupported relation creation.

---

## 9. Expected scale

The first profile is intentionally **engineering-scale**. The target scale is **dozens of sources**, not high-volume SaaS.

The profile does not yet establish numerical throughput or concurrency targets.

Capacity must be measured after the actual workload is defined.

The following are therefore explicitly OPEN:

- maximum concurrent RUNs;
- source-size limit;
- execution latency target;
- daily/weekly throughput;
- repository growth rate;
- recovery time target.

No high-volume claim is made.

---

## 10. Persistence model

The first profile requires durable local persistence for:

### Canonical knowledge

CMOC repository files.

### Derived knowledge access

OBJECT INDEX.

### Execution history

Runtime journal and persistent RUN/stage/attempt state.

### Recovery identity

ATTEMPT records and recovery state.

The execution history must not be confused with CMOC semantic truth.

---

## 11. Security profile

The first profile is a controlled engineering environment.

Required baseline:

- repository access control;
- protected credentials/secrets;
- no credentials stored in CMOC objects;
- controlled GitHub authentication;
- explicit separation between repository content and runtime secrets.

Full enterprise IAM, SSO, multi-tenant authorization and distributed secret-management infrastructure are outside the first profile unless the deployment use case requires them.

---

## 12. Backup and recovery profile

At the first profile level:

- Git history provides versioned repository recovery;
- canonical CMOC files remain versioned;
- runtime state requires a separately defined backup strategy;
- restore must eventually be tested rather than assumed.

A formal enterprise DR profile is not yet claimed.

The following remain OPEN:

- backup frequency;
- retention;
- off-host backup;
- restore target;
- RPO;
- RTO;
- disaster recovery environment.

---

## 13. Observability

The first profile requires sufficient observability to answer:

1. Which RUN is executing?
2. Which stage is executing?
3. Which ATTEMPT is authoritative?
4. What was the last event?
5. Why did execution stop?
6. Was recovery requested?
7. Was the result persisted?
8. Was OBJECT INDEX synchronization completed?

Minimum operational records:

RUN_ID
→ EVENT_ID / EVENT_SEQ
→ STAGE_ID
→ ATTEMPT_ID
→ RESULT_ID
→ outcome

Advanced SLO dashboards are outside the first profile until actual service behavior is measured.

---

## 14. Failure model

The first profile must explicitly preserve:

- LOCAL_REJECTED;
- LOCAL_FAILED;
- DOWNSTREAM_NOT_REACHED;
- RETRY_REQUIRED;
- RESUME_ALLOWED;
- RESUME_BLOCKED;
- ALREADY_COMPLETED;
- INCONSISTENT_HISTORY;
- RECOVERY_REQUIRES_REVIEW.

A failure must never be represented as successful merely because the process restarted.

A completed authoritative result must not be duplicated by recovery.

---

## 15. Deployment model

Initial deployment is controlled and versioned.

Target sequence:

Git commit
→ controlled pull/deployment
→ runtime verification
→ execution test
→ evidence

Automated CI/CD is not required for the first profile, but the architecture should not prevent adding it later.

---

## 16. Operational acceptance criteria

The first profile becomes operationally meaningful only when evidence exists for:

### A. Runtime durability

RUN, stage and attempt state survive process restart.

### B. Recovery

A failed execution can be retried or resumed according to REC rules.

### C. Idempotency

Repeated execution cannot create duplicate authoritative effects.

### D. Persistence

CMOC WRITE remains protected and traceable.

### E. Index synchronization

OBJECT INDEX is deterministically synchronized with canonical CMOC.

### F. Traceability

A completed execution can be reconstructed from RUN history.

### G. Security baseline

Repository and runtime credentials are controlled.

### H. Backup/restore

A representative CMOC state can be restored and verified.

### I. Observability

An operator can determine execution state and failure cause from durable records.

### J. Capacity baseline

The intended workload has measured, rather than assumed, resource requirements.

---

## 17. Explicit non-goals

The first target profile does not require:

- Kubernetes;
- multi-node orchestration;
- distributed consensus;
- distributed locking;
- active-active HA;
- multi-region deployment;
- SaaS multi-tenancy;
- enterprise SSO;
- automatic arbitrary-source harvesting;
- autonomous semantic decision without contracted evidence;
- high-volume production throughput claims.

These may become requirements later, but they are not justified by the current profile.

---

## 18. Architectural boundary

The following remains immutable unless a new explicit architecture review proves otherwise:

### Semantic authority

R1 → R10

### Canonical / persistence / derivation

C1 → C2 → C3

### Execution authority

RUN → ORCH → REC

### Production realization

P1 → P9

### Readiness assessment

P10

Operational infrastructure surrounds these boundaries.

It does not become semantic authority.

---

## 19. Open decisions before implementation

The following decisions should be resolved against the actual intended workload before building additional infrastructure:

1. runtime process form: CLI, long-running service, or both;
2. exact local state-store technology for the target deployment;
3. runtime journal backup strategy;
4. minimum operator interface;
5. required source-package volume;
6. target concurrent RUN count;
7. target recovery time;
8. backup frequency and retention;
9. authentication boundary if runtime becomes network-accessible;
10. observability format and retention.

These are implementation decisions, not reasons to create new semantic layers.

---

## 20. First operationalization backlog

The next engineering work should be selected from this profile in approximately this order:

1. establish the real runtime entry point;
2. make runtime state/journal durable in the target deployment environment;
3. establish controlled backup/restore;
4. establish minimum operational observability;
5. establish security baseline for the actual deployment;
6. measure representative workload;
7. decide whether external DB, supervision, HA or distributed runtime is actually required.

Each item should be closed by implementation evidence.

---

## 21. Governing rule

> **Сначала добываем. Потом сопоставляем.**
>
> После сопоставления — принимаем решение.
>
> После решения — канонизируем.
>
> После канонизации — сохраняем и индексируем.
>
> И только затем решаем, какая эксплуатационная инфраструктура действительно нужна.

---

## 22. Status

**PROD-PROFILE-002:** DESIGN / TARGET PROFILE

This document defines the first target deployment profile. It does not claim operational readiness.

The profile deliberately chooses a controlled single-host engineering deployment as the next concrete target and leaves distributed production capabilities outside scope until an actual requirement justifies them.
