# INVENTORY-BUILDER-001 — CMOC Inventory Snapshot Builder

**ID:** INVENTORY-BUILDER-001  
**Date:** 24-09-2026  
**Status:** CONTRACT CANDIDATE — v0.1  
**Scope:** CMOC repository state → CMOC-INVENTORY snapshot  
**Basis:** P7-INVENTORY-REGISTRATION-BOUNDARY-001 + CMOC-INVENTORY-001 + build_cmoc_object_index.py

## 1. Purpose

Define the deterministic structural mechanism that observes the physical CMOC repository and produces a reproducible CMOC Inventory Snapshot.

The Inventory Builder does not register objects by semantic decision. It observes persisted repository representations and records their structural existence.

## 2. Architectural position

P7 CMOC OBJECT REGISTRATION  
→ CMOC repository state  
→ INVENTORY-BUILDER-001  
→ CMOC-INVENTORY SNAPSHOT  
→ C3/P8 OBJECT INDEX SYNCHRONIZATION  
→ OBJECT INDEX  
→ QUERY

## 3. Governing distinction

The following remain separate:

- CMOC object — canonical persisted representation;
- Inventory Builder — structural observation mechanism;
- CMOC Inventory — snapshot produced by the builder;
- OBJECT INDEX — deterministic derived read-only index;
- QUERY — consumer of OBJECT INDEX.

The Inventory Builder does not become an operational registration database.

## 4. Input

The Builder observes an explicitly selected CMOC repository root/state.

The input state must be identifiable by:

- repository;
- branch or equivalent state identifier;
- source commit or equivalent immutable state identifier;
- generation timestamp;
- builder version.

The Builder must not discover arbitrary external sources.

## 5. Structural discovery

The Builder may:

- enumerate repository files within the configured CMOC scope;
- classify representations structurally;
- identify addressable object representations;
- extract explicit object identifiers from permitted structural locations;
- record path/container;
- record file metadata required by the Inventory contract;
- preserve repository provenance.

The Builder must not:

- infer semantic equivalence;
- decide whether an object is NEW;
- perform reconciliation;
- query OBJECT INDEX for semantic decisions;
- create relations;
- alter CMOC objects;
- alter Decision or Admission;
- modify the repository state it is observing.

## 6. Addressability

An addressable object representation must have an explicit stable object identifier according to the applicable CMOC object standard or registered structural rule.

An unresolved object identity must not silently become an invented identifier.

The Builder must report an explicit structural error or non-addressable classification according to the Inventory contract.

## 7. Snapshot semantics

The output is a snapshot of the observed repository state.

It must contain sufficient provenance to reproduce or audit the snapshot:

- schema/version;
- generated_at;
- repository;
- branch/state;
- source_commit;
- builder version;
- structural records;
- structural counts.

A historical snapshot is immutable evidence of the observed state. A new repository state produces a new snapshot; it does not silently rewrite an older snapshot.

## 8. Determinism

For the same repository state, builder version, configured scope and configuration, the structural result must be reproducible.

Ordering of records must be deterministic.

The builder must not depend on:

- LLM output;
- semantic model judgment;
- wall-clock time for object content;
- network state;
- QUERY results.

The generation timestamp is provenance metadata and must not alter the structural record set.

## 9. Relationship to P7

P7 establishes the persisted CMOC object.

The Inventory Builder subsequently observes it.

P7 does not call the Builder to decide admission.

The Builder does not decide whether P7 was semantically correct.

## 10. Relationship to C3/P8

C3/P8 consumes the resulting structural state to derive or verify OBJECT INDEX.

The Builder does not directly write OBJECT INDEX.

The Builder does not bypass Inventory.

## 11. Failure and conflict conditions

The Builder must distinguish at least:

- valid addressable object;
- non-addressable repository representation;
- unresolved object identity;
- structurally conflicting duplicate addressable representation;
- invalid/unreadable representation.

No semantic resolution is permitted inside these states.

## 12. Acceptance test scope

The first executable test shall use an isolated temporary CMOC repository fixture and verify:

1. one valid CMOC object is discovered;
2. object_id is preserved;
3. object type/path are recorded;
4. provenance is recorded;
5. repeated build over identical repository state produces identical structural records;
6. a second valid object is discovered;
7. missing object_id is reported structurally and is not invented;
8. duplicate addressable representations are reported as a structural conflict;
9. non-object repository files can be excluded/classified without becoming CMOC objects;
10. the builder does not mutate the observed repository;
11. no OBJECT INDEX is written;
12. no semantic operation is performed.

The test must not use the committed CMOC-INVENTORY-001 as a mutable fixture.

## 13. Non-goals

This contract does not define:

- semantic object classification beyond explicit structural rules;
- reconciliation;
- Decision;
- Admission;
- canonization;
- CMOC writing;
- OBJECT INDEX generation;
- QUERY;
- production orchestration;
- repository synchronization or Git commit operations.

## 14. Open implementation points

The following remain deliberately open:

- exact configured CMOC scope;
- complete structural classification rules;
- physical Inventory Snapshot storage path;
- whether snapshots are committed automatically or manually;
- migration from the current historical CMOC-INVENTORY-001 format;
- integration of the Builder with C3/P8.

These must be resolved before production deployment, not invented by the acceptance test.

## 15. Status

CONTRACT CANDIDATE — v0.1.

This contract establishes the missing physical distinction:

**CMOC repository state → Inventory Snapshot**

without turning Inventory into a second semantic or operational CMOC.
