# O3 — BACKUP / RESTORE BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Parent:** O0 / PROD-PROFILE-001  
**Purpose:** define backup and restore boundaries for canonical CMOC and execution state.

## 1. Boundary

O3 governs durability outside normal execution.

It answers:

- what must be backed up;
- what is authoritative;
- what can be regenerated;
- how restore is verified;
- how restored state is prevented from silently becoming a new semantic state.

O3 does not make semantic decisions.

## 2. Applicability

For PROD-PROFILE-001:

- canonical CMOC recovery: REQUIRED;
- execution journal recovery: REQUIRED;
- persistent RUN/stage state recovery: REQUIRED;
- OBJECT INDEX independent semantic backup: NOT_REQUIRED;
- restore verification: REQUIRED;
- backup destination/frequency/retention: UNKNOWN.

## 3. Authority hierarchy

The baseline authority is:

`CANONICAL CMOC`
→ deterministic derivation
→ `OBJECT INDEX`

Execution history is separately represented by:

`EXECUTION JOURNAL + PERSISTED RUN/STAGE STATE`

Therefore:

**OBJECT INDEX is not an independent semantic backup authority.**

## 4. Backup domains

Minimum backup domains:

### B1 — Canonical CMOC

Must preserve:

- canonical object representation;
- object identity;
- object boundary;
- provenance;
- traceability;
- approved canonical content.

### B2 — Execution journal

Must preserve:

- RUN_ID;
- EVENT_ID;
- EVENT_SEQ;
- stage/event information;
- ATTEMPT_ID where present;
- result references;
- recovery events;
- terminal state events.

### B3 — Persistent RUN/stage state

Must preserve:

- RUN_ID;
- SOURCE_ID;
- BATCH_ID;
- RUN_STATUS;
- CURRENT_STAGE_ID;
- CURRENT_STAGE_RESULT_ID;
- CURRENT_ATTEMPT_ID;
- LAST_EVENT_SEQ;
- STATE_VERSION;
- TRACEABILITY.

### B4 — Runtime configuration

The minimum configuration required to reconstruct the declared runtime environment must be identified.

Exact configuration contents remain implementation-specific.

## 5. Derived artifacts

OBJECT INDEX is treated as:

`DERIVED_ARTIFACT`

not:

`CANONICAL_AUTHORITY`.

After restoring canonical CMOC, the preferred recovery path is:

`RESTORE CMOC`
→ `VERIFY CMOC`
→ `DETERMINISTIC OBJECT INDEX BUILD`
→ `VERIFY INDEX`

An index backup may exist operationally, but it must not override canonical CMOC.

## 6. Restore boundary

Restore consists of distinct phases:

1. identify backup;
2. verify backup integrity;
3. restore required authoritative data;
4. verify canonical CMOC;
5. restore execution history/state where required;
6. validate lineage;
7. regenerate derived OBJECT INDEX;
8. verify deterministic reproducibility;
9. expose recovered system to runtime.

Restore must not silently execute semantic reconciliation.

## 7. Backup integrity

Candidate backup integrity checks:

- backup identity;
- creation timestamp;
- version/profile compatibility;
- content integrity;
- completeness;
- storage readability;
- traceability;
- cryptographic/checksum verification where implemented.

A failed integrity check produces an explicit restore failure.

It must not produce a guessed successful restore.

## 8. Restore consistency

After restore:

`JOURNAL_REDUCE(RUN_ID)`

must remain consistent with the restored persistent RUN/stage state where both are restored.

For CMOC:

- object identity must remain stable;
- canonical representation must remain unchanged;
- provenance must remain present;
- traceability must remain present.

For OBJECT INDEX:

- deterministic rebuild must reproduce the expected derived representation.

## 9. Recovery scenarios

Candidate scenarios:

### R1 — CMOC loss

Restore canonical CMOC, verify it, then rebuild OBJECT INDEX.

### R2 — Journal/state loss

If CMOC remains intact, semantic objects are not recreated from memory or assumptions.

Operational recovery must explicitly identify missing execution history.

### R3 — OBJECT INDEX loss

Rebuild from canonical CMOC.

No semantic reconstruction is required.

### R4 — Full local environment loss

Restore:

- CMOC;
- execution history/state as required;
- runtime configuration.

Then rebuild derived artifacts and verify runtime readiness.

## 10. Backup and execution interaction

O3 must coordinate with P1/P2 but must not replace them.

A backup taken during active execution must have an explicitly defined consistency boundary.

If consistency cannot be guaranteed, the backup must be marked accordingly rather than presented as a complete authoritative snapshot.

## 11. Restore and completed effects

Restore must not duplicate already completed authoritative effects.

After restore, P3/P4/P5 controls remain applicable:

- completed attempt protection;
- idempotency;
- retry identity;
- concurrency protection;
- recovery disposition.

Restoring state does not grant permission to repeat an effect.

## 12. Security interaction

Backup and restore are privileged operations.

O2 authorization applies.

Therefore:

`O3 restore`
requires appropriate:

`ACTOR + AUTHENTICATION + AUTHORIZATION`.

O3 must not bypass O2.

## 13. Evidence requirements

An O3 gate should demonstrate at least:

1. backup of canonical CMOC;
2. backup of execution journal;
3. backup of persistent RUN/stage state;
4. backup integrity verification;
5. successful restore;
6. canonical CMOC identity preservation;
7. provenance/traceability preservation;
8. journal/state consistency;
9. OBJECT INDEX deterministic regeneration;
10. deterministic rebuild reproducibility;
11. OBJECT INDEX does not override CMOC;
12. completed-effect/idempotency protection after restore;
13. restore failure is explicit;
14. no semantic responsibility leakage.

## 14. Candidate outcomes

`BACKUP_ACCEPTED`
`BACKUP_REJECTED`
`RESTORE_ACCEPTED`
`RESTORE_REJECTED`
`BACKUP_INTEGRITY_FAILED`
`RESTORE_INTEGRITY_FAILED`
`RESTORE_INCOMPLETE`
`STATE_INCONSISTENCY`
`INDEX_REBUILD_REQUIRED`
`INDEX_REBUILD_VERIFIED`

## 15. Invariants

**O3-I01 — CMOC authority**

Canonical CMOC remains authoritative after restore.

**O3-I02 — Index derivation**

OBJECT INDEX is regenerated deterministically from canonical CMOC when required.

**O3-I03 — History preservation**

Restoration does not rewrite execution history.

**O3-I04 — Effect protection**

Restoration does not authorize duplicate authoritative effects.

**O3-I05 — Integrity honesty**

Failed integrity verification cannot become successful restore.

**O3-I06 — Security boundary**

Restore requires O2 authorization.

**O3-I07 — No semantic leakage**

Backup/restore cannot decide NEW, equivalence, conflict, canonization or semantic meaning.

## 16. Test boundary

The first O3 gate is a local isolated backup/restore harness.

It should use a dedicated test fixture and demonstrate the full authority chain:

`CMOC backup`
→ `restore`
→ `verify`
→ `OBJECT INDEX rebuild`
→ `verify reproducibility`.

It does not establish enterprise backup infrastructure, off-site replication, immutable storage, disaster recovery or a specific backup product.

## 17. Exit condition

O3 can move to ACCEPTED when the test demonstrates:

`authoritative backup + verified restore + deterministic index regeneration + execution-state integrity`

without semantic responsibility leakage.

**Status:** DESIGN / ARCHITECTURE CANDIDATE
