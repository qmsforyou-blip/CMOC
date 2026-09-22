# PROD-PROFILE-001 — CMOC PRODUCTION DEPLOYMENT PROFILE

**Profile ID:** PROD-PROFILE-001  
**Version:** 0.1  
**Status:** PROFILE_BASELINE  
**Parent:** O0.1 — Production Deployment Profile  
**Scope:** CMOC / Superagent production operationalization baseline

## 1. Purpose

This profile declares the initial operational context for the CMOC/Superagent runtime.

It is intentionally conservative.

Where the current architecture does not provide sufficient evidence for a concrete production parameter, the value is recorded as **UNKNOWN** rather than invented.

This profile is therefore a baseline for O1-O9, not a claim that the complete production environment is already operational.

## 2. Deployment topology

| Parameter | Value | State |
|---|---|---|
| Host topology | Single-host baseline | DECLARED |
| Multi-host deployment | Not required for baseline | NOT_REQUIRED_BY_PROFILE |
| Geographic distribution | Single site baseline | DECLARED |
| Containerization | UNKNOWN | UNKNOWN |
| Shared network storage | UNKNOWN | UNKNOWN |
| External service dependencies | UNKNOWN | UNKNOWN |

### Boundary

The baseline does not require distributed execution.

Therefore O7 distributed coordination/HA is outside the mandatory baseline unless the deployment profile is later revised.

## 3. Process model

| Parameter | Value | State |
|---|---|---|
| Runtime process model | Single-runtime baseline | DECLARED |
| Multiple workers | UNKNOWN | UNKNOWN |
| Process supervision | REQUIRED | REQUIRED |
| Controlled shutdown | REQUIRED | REQUIRED |
| Restart after process failure | REQUIRED | REQUIRED |

The execution architecture remains:

`RUN → ORCH → stage execution → journal/state → recovery`

P1-P5 guarantees remain applicable.

## 4. Persistence model

The baseline distinguishes four persistence concerns:

1. canonical CMOC representation;
2. execution journal;
3. persistent RUN/stage state;
4. deterministic OBJECT INDEX.

| Artifact | Baseline |
|---|---|
| CMOC | Canonical authoritative representation |
| Execution journal | Durable persistence REQUIRED |
| RUN/stage state | Durable persistence REQUIRED |
| OBJECT INDEX | Deterministic derived artifact |
| Temporary execution data | UNKNOWN |

Architectural invariant:

**OBJECT INDEX is not an independent semantic authority.**

## 5. Workload

The current architecture does not yet provide measured production workload data.

Therefore:

| Parameter | Value | State |
|---|---|---|
| Typical source size | UNKNOWN | UNKNOWN |
| Maximum source size | UNKNOWN | UNKNOWN |
| Typical batch size | UNKNOWN | UNKNOWN |
| Maximum batch size | UNKNOWN | UNKNOWN |
| RUNs/day | UNKNOWN | UNKNOWN |
| Concurrent RUNs | UNKNOWN | UNKNOWN |
| Retry frequency | UNKNOWN | UNKNOWN |
| CMOC writes/day | UNKNOWN | UNKNOWN |
| Index rebuild frequency | UNKNOWN | UNKNOWN |

No throughput or capacity claim is made.

These values become the subject of O5.

## 6. Availability

Baseline availability requirement:

**Single-host operational availability.**

| Requirement | State |
|---|---|
| Multi-node HA | NOT_REQUIRED_BY_PROFILE |
| Automatic failover between hosts | NOT_REQUIRED_BY_PROFILE |
| Process restart | REQUIRED |
| Host-loss tolerance | UNKNOWN |
| Planned maintenance | UNKNOWN |
| Availability percentage/SLO | UNKNOWN |

This deliberately separates process recovery from high availability.

## 7. Recovery

The baseline requires:

- deterministic restart/resume behavior;
- preservation of completed results;
- explicit retry for failed attempts;
- preservation of failed history;
- cross-run isolation;
- no semantic repair during recovery.

RPO/RTO values are not yet established:

| Parameter | Value |
|---|---|
| RPO | UNKNOWN |
| RTO | UNKNOWN |
| Host-loss recovery | UNKNOWN |
| Storage-loss recovery | UNKNOWN |

O3/O8 must establish these before O9 can close the corresponding readiness claims.

## 8. Security

The initial profile requires an explicit security boundary but does not yet prescribe technology.

| Control | State |
|---|---|
| Operator authentication | REQUIRED |
| Service identity | REQUIRED |
| Authorization | REQUIRED |
| Privileged CMOC write control | REQUIRED |
| Secret management | REQUIRED |
| Network access policy | UNKNOWN |
| Source-data sensitivity classification | UNKNOWN |

Semantic decisions must remain independent of authentication and authorization mechanisms.

## 9. Backup / restore

Baseline requirement:

**CMOC and execution history must be recoverable.**

Required backup scope:

- canonical CMOC;
- execution journal;
- persistent RUN/stage state;
- configuration required to reconstruct runtime behavior.

OBJECT INDEX does not need to be treated as an independent semantic backup authority because it is deterministically regenerable from canonical CMOC.

Backup destination, frequency, retention and restore targets remain UNKNOWN.

## 10. Observability

The baseline requires operational visibility into:

- process health;
- RUN status;
- current stage;
- attempt identity;
- stage completion/rejection/failure;
- recovery events;
- CMOC persistence failures;
- OBJECT INDEX synchronization failures;
- lineage anomalies.

Alerting channel and SLO thresholds remain UNKNOWN.

## 11. Deployment / upgrade

Baseline:

| Capability | State |
|---|---|
| Versioned deployment | REQUIRED |
| Configuration versioning | REQUIRED |
| Reproducible deployment | REQUIRED |
| Rollback | REQUIRED |
| Schema/contract compatibility | REQUIRED |
| Automated deployment | UNKNOWN |

Deployment must not silently alter canonical CMOC semantics.

## 12. Distributed behavior

`MULTI_NODE = NOT_REQUIRED`

`HIGH_AVAILABILITY = NOT_REQUIRED_BY_PROFILE`

`NETWORK_PARTITION_HANDLING = NOT_REQUIRED_BY_PROFILE`

`DISTRIBUTED_LOCKING = NOT_REQUIRED_BY_PROFILE`

This does not claim that these capabilities are unnecessary in general.

It means only that they are outside the declared baseline production profile.

A future multi-node deployment requires a new profile version.

## 13. Capacity evidence

Capacity is currently:

**UNKNOWN**

No architectural test from P1-P9 is interpreted as a capacity measurement.

O5 must establish:

`DECLARED_LOAD + TEST_CONDITIONS + MEASURED_RESULT + ACCEPTANCE_CRITERIA`

before a production capacity claim is made.

## 14. Operational package applicability

| Package | Baseline applicability |
|---|---|
| O1 Process / Service Supervision | REQUIRED |
| O2 Security / Access | REQUIRED |
| O3 Backup / Restore | REQUIRED |
| O4 Observability / Alerting | REQUIRED |
| O5 Capacity / Load | REQUIRED |
| O6 Deployment / Upgrade | REQUIRED |
| O7 HA / Failure Infrastructure | NOT_REQUIRED_BY_PROFILE |
| O8 Operational E2E | REQUIRED |
| O9 Operational Readiness Gate | REQUIRED |

## 15. Explicit UNKNOWN register

The following remain unresolved:

1. containerization;
2. shared network storage;
3. external service dependencies;
4. worker concurrency;
5. workload bounds;
6. concurrent RUN count;
7. retry frequency;
8. CMOC write frequency;
9. index rebuild frequency;
10. host-loss tolerance;
11. maintenance window;
12. availability SLO;
13. RPO;
14. RTO;
15. network access policy;
16. source-data sensitivity classification;
17. backup destination;
18. backup frequency;
19. backup retention;
20. restore verification frequency;
21. alerting channel;
22. observability retention;
23. automated deployment;
24. configuration migration requirements.

UNKNOWN is intentional and is not treated as proof of absence.

## 16. Profile change rule

A new profile version is required when any of the following changes materially:

- deployment topology;
- process model;
- persistence authority;
- expected workload;
- concurrency;
- availability target;
- recovery target;
- security boundary;
- backup strategy;
- operational ownership.

Example:

`PROD-PROFILE-001 v0.1`
→ single-host baseline

does not automatically cover:

`PROD-PROFILE-002 v0.1`
→ multi-host HA deployment.

## 17. Readiness interpretation

This profile does **not** mean:

- production system fully operational;
- all O1-O9 controls implemented;
- capacity proven;
- security proven;
- backup/restore proven;
- disaster recovery proven.

It means only:

**the initial production deployment boundary has been declared sufficiently to begin operationalization work.**

## 18. Next stage

Proceed to:

**O1 — Process / Service Supervision**

O1 should convert the REQUIRED supervision capabilities above into a concrete contract, test and evidence gate.

**Profile status:** PROFILE_BASELINE
