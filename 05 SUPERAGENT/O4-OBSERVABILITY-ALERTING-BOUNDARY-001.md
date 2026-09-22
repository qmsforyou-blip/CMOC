# O4 — OBSERVABILITY / ALERTING BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Parent:** O0 / PROD-PROFILE-001  
**Purpose:** define operational observability and alerting for the declared single-host CMOC/Superagent production profile.

## 1. Boundary

O4 observes runtime behavior and exposes operational conditions.

O4 may:

- collect operational events;
- expose runtime health;
- expose RUN/stage/attempt state;
- expose recovery state;
- detect defined operational conditions;
- generate alerts;
- preserve operational evidence.

O4 must not:

- change semantic results;
- repair failed semantic evidence;
- approve NEW;
- perform canonization;
- mutate CMOC;
- mutate OBJECT INDEX;
- silently restart or retry work.

Observation and action remain separate.

## 2. Applicability

For PROD-PROFILE-001:

- runtime health visibility: REQUIRED;
- RUN visibility: REQUIRED;
- stage/attempt visibility: REQUIRED;
- recovery visibility: REQUIRED;
- persistence failure visibility: REQUIRED;
- index synchronization failure visibility: REQUIRED;
- lineage anomaly visibility: REQUIRED;
- operational alerting: REQUIRED;
- alert channel: UNKNOWN;
- observability retention: UNKNOWN;
- formal SLO thresholds: UNKNOWN.

## 3. Observability layers

O4 distinguishes four layers.

### L1 — Runtime

Observe:

- process state;
- health state;
- startup/shutdown;
- unexpected termination;
- restart;
- persistence availability.

### L2 — Execution

Observe:

- RUN_ID;
- current stage;
- ATTEMPT_ID;
- stage status;
- stage duration;
- recovery disposition;
- terminal RUN status.

### L3 — Persistence

Observe:

- journal append failures;
- RUN/state persistence failures;
- CMOC write outcome;
- post-write verification failure;
- idempotency/conflict events.

### L4 — Derived artifacts

Observe:

- OBJECT INDEX synchronization result;
- deterministic rebuild status;
- index verification;
- orphan/missing/conflict states.

These layers are operational views over already defined contracts.

## 4. Identity requirements

Every operational observation should preserve, where applicable:

- RUN_ID;
- STAGE_ID;
- ATTEMPT_ID;
- RESULT_ID;
- EVENT_ID;
- SOURCE_ID;
- BATCH_ID.

O4 must not create semantic identity where none exists.

## 5. Minimum event model

Candidate operational observation:

`OBSERVATION_ID`
`TIMESTAMP`
`RUN_ID`
`STAGE_ID`
`ATTEMPT_ID`
`EVENT_TYPE`
`STATUS`
`SOURCE`
`DETAILS`

Operational observations are distinct from P1 execution journal events.

O4 may derive views from the journal but must not rewrite journal history.

## 6. Health signals

Minimum signals:

`PROCESS_HEALTH`
`PERSISTENCE_HEALTH`
`RUN_HEALTH`
`RECOVERY_HEALTH`
`CMOC_WRITE_HEALTH`
`OBJECT_INDEX_HEALTH`

Candidate states:

`HEALTHY`
`DEGRADED`
`UNHEALTHY`
`UNKNOWN`

UNKNOWN must remain UNKNOWN.

## 7. Alert classes

Candidate alerts:

### A1 — Runtime failure

Examples:

- unexpected process termination;
- failed restart;
- health check failure.

### A2 — Persistence failure

Examples:

- journal append failure;
- RUN/state persistence failure;
- CMOC write failure.

### A3 — Recovery anomaly

Examples:

- inconsistent history;
- blocked resume;
- repeated failed retry;
- unrecoverable interrupted execution.

### A4 — Index synchronization failure

Examples:

- missing object;
- synchronization conflict;
- orphan object;
- deterministic rebuild failure.

### A5 — Security/operational anomaly

Examples:

- repeated authorization failure;
- unexpected privileged operation;
- credential failure.

O4 observes these conditions; O2 remains responsible for authorization.

## 8. Alert severity

Severity must describe operational urgency, not semantic importance.

Candidate levels:

`INFO`
`WARNING`
`CRITICAL`

No severity level may imply:

- NEW;
- EXISTING_EQUIVALENT;
- CONFLICT;
- semantic correctness;
- business importance.

## 9. Alert generation rule

Candidate rule:

`OBSERVED CONDITION + DEFINED THRESHOLD/STATE`
→ `ALERT`

If the threshold is not defined, the condition may be observed but must not be presented as a formally breached SLO.

This is especially important for current UNKNOWN values.

## 10. Alert deduplication

Repeated observations of the same operational condition should not create uncontrolled duplicate alerts.

Candidate alert identity:

`ALERT_KEY = CONDITION + RUN_ID + STAGE_ID + ATTEMPT_ID`

where applicable.

Deduplication must not delete the underlying operational history.

## 11. Recovery interaction

O4 may signal:

`ALERT`
→ operator/runtime recovery workflow.

O4 must not directly reinterpret an alert as:

`RETRY_REQUIRED`
or
`RESUME_ALLOWED`

unless a separate contracted operational action explicitly invokes REC.

Observation is not recovery authority.

## 12. Dashboard boundary

A runtime dashboard may expose:

- active RUNs;
- current stages;
- failed attempts;
- recovery states;
- CMOC persistence status;
- index synchronization status;
- security anomalies;
- recent alerts.

A dashboard is a view, not a semantic authority.

## 13. SLO boundary

Current profile does not yet define numerical SLOs.

Therefore:

- availability SLO = UNKNOWN;
- alert response time = UNKNOWN;
- recovery alert latency = UNKNOWN;
- CMOC write alert latency = UNKNOWN;
- index synchronization alert latency = UNKNOWN.

O4 must not invent these values.

O5/O8/O9 may later establish and validate measurable operational targets.

## 14. Evidence requirements

An O4 gate should demonstrate at least:

1. runtime health observation;
2. RUN/stage/attempt observation;
3. persistence failure observation;
4. recovery anomaly observation;
5. CMOC write failure observation;
6. OBJECT INDEX synchronization failure observation;
7. alert generation;
8. alert severity;
9. alert deduplication;
10. UNKNOWN preservation when thresholds are undefined;
11. operational dashboard/view does not mutate source state;
12. no semantic responsibility leakage.

## 15. Invariants

**O4-I01 — Observation only**

O4 observes; it does not decide semantic meaning.

**O4-I02 — History preservation**

Observability does not rewrite P1 journal history.

**O4-I03 — Identity preservation**

Observations retain execution lineage.

**O4-I04 — UNKNOWN honesty**

Undefined thresholds remain UNKNOWN.

**O4-I05 — Alert/action separation**

An alert does not itself constitute recovery authorization.

**O4-I06 — No persistence mutation**

O4 cannot directly mutate CMOC or OBJECT INDEX.

**O4-I07 — No semantic leakage**

Operational severity and health cannot become semantic judgments.

## 16. Test boundary

The first O4 test is a synthetic observability harness.

It proves observation and alerting boundaries only.

It does not establish a particular monitoring platform, metrics database, log aggregator, notification provider, dashboard framework or production SLO.

## 17. Exit condition

O4 can move to ACCEPTED when the test demonstrates:

`runtime/execution/persistence observation + alert generation + UNKNOWN preservation + no unauthorized action`

without semantic responsibility leakage.

**Status:** DESIGN / ARCHITECTURE CANDIDATE
