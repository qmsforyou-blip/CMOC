# O1 — PROCESS / SERVICE SUPERVISION BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Parent:** O0 / PROD-PROFILE-001  
**Purpose:** define the runtime supervision boundary for the declared single-host CMOC/Superagent production profile.

## 1. Boundary

O1 governs the operational lifecycle of the runtime process/service.

O1 answers:

- is the runtime started;
- is it healthy enough to execute;
- what happens when it stops unexpectedly;
- how is restart initiated;
- how is controlled shutdown performed;
- how is RUN/stage state preserved across process restart.

O1 does not execute semantic decisions.

## 2. Declared profile applicability

For PROD-PROFILE-001:

- single-host baseline;
- single-runtime baseline;
- process supervision REQUIRED;
- controlled shutdown REQUIRED;
- restart after process failure REQUIRED;
- multi-node HA outside profile.

Therefore O1 is REQUIRED.

## 3. Responsibility

O1 may:

- start a contracted runtime;
- stop a contracted runtime;
- observe process/service health;
- detect process termination;
- apply an explicit restart policy;
- preserve or recover runtime identity;
- expose health state;
- record operational events;
- hand recovery to REC/ORCH according to existing contracts.

O1 must not:

- reinterpret semantic results;
- convert rejection to success;
- invent missing results;
- alter NEW decisions;
- alter canonization;
- mutate CMOC directly;
- mutate OBJECT INDEX directly;
- rewrite execution history.

## 4. Lifecycle states

Candidate service states:

`STOPPED`
`STARTING`
`RUNNING`
`DEGRADED`
`STOPPING`
`FAILED`
`RESTARTING`

Candidate transitions:

`STOPPED → STARTING → RUNNING`

`RUNNING → DEGRADED`

`RUNNING → STOPPING → STOPPED`

`RUNNING → FAILED → RESTARTING → STARTING`

An operational state must not be confused with a semantic stage result.

## 5. Health model

Minimum health dimensions:

- process existence;
- process responsiveness;
- ability to access required local persistence;
- ability to append execution journal events;
- ability to load persistent RUN/stage state.

Candidate health:

`HEALTHY`
`DEGRADED`
`UNHEALTHY`
`UNKNOWN`

Health observation does not authorize semantic repair.

## 6. Restart policy

A restart may be initiated when:

- the runtime terminates unexpectedly;
- a declared health check fails;
- an operator explicitly requests restart.

Before restarting an interrupted RUN, O1 must not assume the interrupted stage succeeded.

The restart path is:

`O1 detects failure`
→ `persist operational event`
→ `P4 restart/resume`
→ `REC disposition`
→ `ORCH`

O1 does not replace P4 or REC.

## 7. Controlled shutdown

A controlled shutdown must:

1. stop accepting new work according to runtime policy;
2. allow active stage handling to reach a defined boundary;
3. persist required operational state;
4. record shutdown event;
5. terminate the runtime.

A forced termination must remain distinguishable from controlled shutdown.

## 8. RUN preservation

O1 must preserve:

- RUN_ID;
- SOURCE_ID;
- current stage;
- current ATTEMPT_ID;
- persisted result references;
- execution journal;
- persistent RUN/stage state.

O1 must not create a new RUN merely because the process restarted.

A new RUN requires an explicit new execution identity.

## 9. Duplicate execution protection

O1 must not bypass P3/P5.

After restart:

- completed attempts remain protected;
- authoritative results remain authoritative;
- failed attempts remain history;
- interrupted execution is evaluated by P4/REC;
- duplicate effects are prevented by existing idempotency/concurrency boundaries.

## 10. Failure classes

Candidate O1 operational outcomes:

`START_FAILED`
`HEALTH_CHECK_FAILED`
`UNEXPECTED_TERMINATION`
`RESTART_ACCEPTED`
`RESTART_BLOCKED`
`CONTROLLED_SHUTDOWN`
`FORCED_SHUTDOWN`
`PERSISTENCE_UNAVAILABLE`
`SUPERVISION_UNAVAILABLE`

These are operational states/events, not semantic decisions.

## 11. Persistence dependency

O1 depends on durable P1/P2 persistence.

If journal or persistent RUN/stage state is unavailable, O1 must not claim that an interrupted RUN is safely recoverable.

The correct result is an explicit operational failure or recovery-required state.

## 12. Single-host boundary

O1 v0.1 does not cover:

- host failover;
- multi-node orchestration;
- distributed locks;
- split-brain;
- network partition consensus;
- cross-host service discovery.

Those remain outside PROD-PROFILE-001.

## 13. Evidence requirements

An O1 gate should demonstrate at least:

1. clean start;
2. health detection;
3. controlled shutdown;
4. unexpected termination detection;
5. restart;
6. RUN identity preservation;
7. journal/state preservation;
8. completed-result protection;
9. interrupted-stage non-success assumption;
10. handoff to P4/REC;
11. persistence-unavailable behavior;
12. no semantic responsibility leakage.

## 14. Invariants

**O1-I01 — Runtime/semantic separation**

Process supervision cannot decide semantic meaning.

**O1-I02 — RUN identity preservation**

Process restart does not create a new RUN.

**O1-I03 — Completed-effect protection**

Restart cannot replace an authoritative completed result.

**O1-I04 — Interrupted-state honesty**

RUNNING without an authoritative result is not treated as successful.

**O1-I05 — Recovery delegation**

Restart recovery is delegated to P4/REC/ORCH.

**O1-I06 — No direct semantic mutation**

O1 cannot mutate NEW decisions, canonization, CMOC semantics or OBJECT INDEX semantics.

**O1-I07 — Persistence honesty**

Unavailable persistence prevents a claim of safe recovery.

## 15. Test boundary

The first O1 test is a synthetic supervision harness.

It must prove the O1 boundary and integration with the already established P1/P2/P4/REC contracts.

It does not prove a particular operating system service manager, container orchestrator or HA platform.

## 16. Exit condition

O1 can move from DESIGN to ACCEPTED only when its test demonstrates:

`runtime lifecycle + failure detection + restart + identity preservation + recovery handoff`

without semantic responsibility leakage.

**Status:** DESIGN / ARCHITECTURE CANDIDATE
