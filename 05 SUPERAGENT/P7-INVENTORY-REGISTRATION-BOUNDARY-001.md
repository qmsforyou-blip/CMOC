# P7 → INVENTORY REGISTRATION BOUNDARY

**ID:** P7-INVENTORY-REGISTRATION-BOUNDARY-001  
**Date:** 24-09-2026  
**Status:** CONTRACT CANDIDATE — v0.1  
**Scope:** CMOC_WRITE_ACCEPTED → REGISTERED INVENTORY REPRESENTATION  
**Basis:** P7-CMOC-OBJECT-REGISTRATION-BOUNDARY-001 + C3-OBJECT-INDEX-SYNCHRONIZATION-BOUNDARY-001 + CMOC-INVENTORY-001 + build_cmoc_object_index.py

## 1. Purpose

Define the boundary between physical registration of a new CMOC object and the structural inventory from which OBJECT INDEX may subsequently be derived.

This boundary does not create semantic meaning.

## 2. Architectural position

NEW_APPROVED → C1 CANONIZATION → CANONICALIZATION_READY → P7 CMOC OBJECT REGISTRATION → CMOC_WRITE_ACCEPTED → INVENTORY REGISTRATION → C3/P8 OBJECT INDEX SYNCHRONIZATION → OBJECT INDEX

## 3. Governing distinction

Three different representations must remain separate:

1. **CMOC object** — canonical persisted object representation.
2. **CMOC Inventory** — structural inventory/snapshot of addressable repository representations.
3. **OBJECT INDEX** — deterministic derived read-only index used by QUERY.

Therefore:

P7 ≠ Inventory Registration  
Inventory ≠ OBJECT INDEX  
Inventory Registration ≠ C3/P8

## 4. Entry

The boundary accepts only a successful P7 result:

- status = CMOC_WRITE_ACCEPTED;
- object_id present and stable;
- persisted representation verified;
- provenance and traceability preserved.

No NEW decision, semantic comparison, reconciliation, canonization, relation creation, or QUERY operation is performed here.

## 5. Registration obligation

Inventory Registration must establish that the persisted CMOC object is represented in the structural inventory mechanism used by the subsequent deterministic index build.

At minimum the registration representation must preserve:

- object_id;
- object_type;
- addressable CMOC representation/path;
- provenance;
- traceability;
- registration/write identity;
- source state required to reproduce the inventory entry.

## 6. Snapshot versus registration

The existing CMOC-INVENTORY-001 is explicitly a structural inventory snapshot with generated_at, repository, branch, source_commit and records.

This contract therefore does **not** assume that the existing JSON snapshot itself is the operational registration database.

The physical mechanism for maintaining the current inventory source remains an implementation question.

The mechanism must not silently rewrite a historical snapshot merely to make C3 pass.

## 7. Authority

Inventory Registration may record structural existence.

It must not:

- decide whether an object is NEW;
- determine equivalence;
- alter Decision;
- alter Reconciliation;
- infer semantic properties;
- create relations;
- change object_id;
- canonize content;
- mutate OBJECT INDEX directly.

## 8. Idempotency

Repeated registration of the same unchanged object identity and representation must be idempotent.

A registration for an occupied object_id with a different structural representation must produce an explicit conflict.

## 9. Relationship to C3/P8

C3/P8 consumes the resulting persisted structural state and derives/verifies OBJECT INDEX deterministically.

Inventory Registration does not build OBJECT INDEX.

C3/P8 must be able to distinguish:

- object registered and index synchronized;
- object registered but index missing;
- conflicting index representation;
- orphan index representation.

## 10. Current open implementation question

The repository currently contains CMOC-INVENTORY-001 as a snapshot and build_cmoc_object_index.py as a deterministic index builder.

A separate operational mechanism for updating the inventory source from a newly registered P7 object has not yet been established.

This contract therefore defines the boundary without inventing that mechanism.

## 11. Acceptance test scope

The first executable test shall verify:

1. valid CMOC_WRITE_ACCEPTED enters Inventory Registration;
2. object_id is preserved;
3. structural representation is recorded;
4. provenance/traceability are preserved;
5. repeated identical registration is idempotent;
6. changed representation produces conflict;
7. invalid P7 entry is rejected;
8. OBJECT INDEX is not directly mutated;
9. no semantic operation occurs;
10. the inventory representation is sufficient as input to a later deterministic C3/P8 step.

The test must use an isolated temporary inventory representation and must not modify the committed CMOC-INVENTORY-001 snapshot.

## 12. Non-goals

This contract does not define:

- the final physical inventory storage format;
- repository-wide inventory regeneration;
- OBJECT INDEX generation;
- QUERY;
- semantic reconciliation;
- Decision;
- CMOC canonization;
- production orchestration.

## 13. Status

CONTRACT CANDIDATE — v0.1.

The contract closes the architectural distinction between P7 object persistence and C3/P8 index synchronization while leaving the physical inventory-maintenance mechanism explicitly open.
