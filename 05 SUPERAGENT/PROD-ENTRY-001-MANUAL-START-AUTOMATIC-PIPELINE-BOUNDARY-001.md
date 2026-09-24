# PROD-ENTRY-001 — MANUAL START / AUTOMATIC PIPELINE ENTRY BOUNDARY

**Status:** DESIGN / IMPLEMENTATION CANDIDATE  
**Date:** 24-09-2026  
**Predecessor:** PROD-PROFILE-002  
**Purpose:** define the real local runtime entry point for the confirmed target profile: Windows + Obsidian + local runtime + Git CMOC.

---

## 1. Boundary

The entry point is the boundary between:

**manual operator action**

and

**automatic contracted runtime execution**.

Target interaction:

`py 05 SUPERAGENT/run_superagent.py --source-package <PATH> [--run-id <RUN_ID>]`

The operator supplies the SOURCE_PACKAGE and explicitly starts the RUN.

After START, the runtime owns deterministic execution control.

---

## 2. Manual responsibility

The operator is responsible for:

- selecting/providing the SOURCE_PACKAGE;
- explicitly starting the RUN;
- responding at established human semantic boundaries;
- publication decisions.

The operator does not manually advance every machine in the pipeline.

---

## 3. Automatic responsibility

After a valid START the runtime is responsible for:

- validating the SOURCE_PACKAGE contract;
- establishing RUN_ID;
- establishing SOURCE_ID and BATCH_ID lineage;
- creating durable RUN state;
- creating execution history;
- splitting the SOURCE_PACKAGE into contracted BATCH units;
- selecting the next contracted stage;
- preserving RUN/STAGE/ATTEMPT/RESULT identity;
- invoking registered production adapters;
- persisting stage outcomes;
- applying retry/resume/idempotency rules;
- routing explicit semantic review states to the human boundary;
- continuing automatically after an accepted human decision;
- completing CMOC WRITE and OBJECT INDEX synchronization only through C2/C3 boundaries.

---

## 4. Source package handling

The entry point accepts the existing SOURCE_PACKAGE contract.

Minimum fields:

- `package_id`;
- `source_id`;
- `source_name`;
- `fragments`;
- `source_package_status`.

The entry point does not interpret source content semantically.

Automatic splitting is structural only.

A fragment becomes a BATCH input unit with preserved:

SOURCE_ID → SOURCE_PACKAGE_ID → BATCH_ID → fragment reference.

No semantic distinction is created by splitting.

---

## 5. Runtime identity

A started execution receives:

- RUN_ID;
- SOURCE_ID;
- SOURCE_PACKAGE_ID;
- BATCH_ID;
- STAGE_ID;
- ATTEMPT_ID;
- RESULT_ID.

The entry point must never reuse an existing RUN_ID.

A caller-supplied RUN_ID is permitted only when it does not already exist.

---

## 6. Production adapter boundary

The entry point must invoke only registered production adapters.

It must not:

- execute synthetic adapters;
- silently substitute a missing adapter;
- interpret semantic results;
- convert NEEDS_REVIEW into approval;
- invent evidence;
- bypass C1/C2/C3 boundaries.

If a required production adapter is unavailable, the RUN stops with an explicit operational failure.

This is an operational failure, not a semantic result.

---

## 7. Human boundary

The runtime may stop with an explicit review state.

Examples:

- NEEDS_REVIEW;
- AMBIGUOUS;
- NEW_REJECTED;
- CANONIZATION_REJECTED;
- EXISTING_OBJECT_WRITE_CONFLICT;
- RECOVERY_REQUIRES_REVIEW.

The runtime must persist the stop state and preserve lineage.

It must not manufacture a semantic answer in order to continue automatically.

---

## 8. Durability

RUN creation and initial state must be durable before downstream execution begins.

The entry point uses the existing local runtime persistence component.

The runtime persistence remains separate from CMOC semantic truth.

---

## 9. Failure states

The entry point distinguishes at minimum:

- START_REJECTED;
- SOURCE_PACKAGE_INVALID;
- RUN_ALREADY_EXISTS;
- PRODUCTION_ADAPTER_UNAVAILABLE;
- STAGE_REJECTED;
- STAGE_FAILED;
- HUMAN_REVIEW_REQUIRED;
- RUN_COMPLETED;
- RUN_INCOMPLETE.

Operational failure is never converted into semantic success.

---

## 10. Non-responsibilities

The entry point is not:

- a new semantic machine;
- a NEW decision engine;
- a semantic comparison engine;
- a canonization engine;
- a CMOC writer;
- an OBJECT INDEX builder;
- an autonomous source discovery engine.

It is an execution entry boundary.

---

## 11. First implementation scope

The first implementation gate proves:

1. manual START is possible through a real Windows/Python CLI;
2. SOURCE_PACKAGE is validated;
3. structural BATCH splitting is automatic;
4. durable RUN state is created;
5. production adapter availability is checked;
6. missing production implementation stops the RUN explicitly;
7. no semantic decision is fabricated;
8. the process exits with a machine-readable result.

This first gate does **not** claim that all R1-R10 semantic production implementations already exist.

---

## 12. Acceptance criterion

The entry point is accepted when a local Windows run demonstrates:

`MANUAL START
→ SOURCE VALIDATION
→ RUN CREATED
→ BATCH SPLIT
→ PRODUCTION PIPELINE CHECK
→ EXPLICIT CONTINUE OR EXPLICIT STOP
`

with durable traceability.

---

## 13. Governing rule

> **После ручного START машина работает сама — но только в пределах уже заключённых контрактов.**

No operational convenience may acquire semantic authority.
