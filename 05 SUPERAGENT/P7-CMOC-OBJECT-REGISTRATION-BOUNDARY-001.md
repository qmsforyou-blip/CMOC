# P7 — CMOC OBJECT REGISTRATION BOUNDARY

**ID:** P7-CMOC-OBJECT-REGISTRATION-BOUNDARY-001  
**Date:** 24-09-2026  
**Status:** CONTRACT CANDIDATE — v0.1  
**Scope:** CANONICALIZATION_READY → REGISTERED CMOC OBJECT → CMOC_WRITE_ACCEPTED  
**Basis:** STD-0001 Universal CMOC Object + current ProductionCmocWriter + C3 OBJECT INDEX boundary

## 1. Purpose

Define the physical boundary at which an already canonicalized representation becomes a registered, addressable CMOC object.

P7 does not make semantic decisions.

## 2. Architectural position

C1 CANONIZATION → CANONICALIZATION_READY → P7 CMOC OBJECT REGISTRATION / WRITE → CMOC_WRITE_ACCEPTED → C3 / P8 OBJECT INDEX SYNCHRONIZATION → OBJECT INDEX

## 3. Governing principle

STD-0001 establishes:
- every CMOC object has a unique identifier;
- every CMOC object must be registered;
- every CMOC object has a passport;
- the passport is at the beginning of the file;
- the object is primary; the file is a storage representation.

P7 therefore must not treat an arbitrary persisted file as sufficient evidence of a CMOC object.

## 4. Entry

P7 accepts only status = CANONICALIZATION_READY.

The input must contain the canonical object identity and the representation required for persistence.

P7 does not perform:
- NEW decision;
- semantic comparison;
- reconciliation;
- canonization;
- relation creation;
- OBJECT INDEX construction.

## 5. Registration obligations

Before returning CMOC_WRITE_ACCEPTED, P7 must establish, within the selected CMOC target:
1. object_id is present and stable;
2. object type is present;
3. object name/title is present;
4. lifecycle status is present;
5. source/provenance is preserved;
6. creation/registration information is preserved;
7. tags/metadata required by the applicable CMOC object standard are preserved;
8. the representation is addressable as a CMOC object;
9. the persisted representation can be read back and verified.

The exact physical YAML/file format is governed by the applicable CMOC object standard and is not redefined by this boundary contract.

## 6. Identity

P7 must preserve the object_id supplied by C1.

P7 must not invent a replacement object identity.

Repeated write of the same unchanged object must be idempotent.

A different representation under an already occupied object_id is a write conflict.

## 7. Registration vs inventory

P7 registration is not the same thing as CMOC-INVENTORY-001.

CMOC-INVENTORY-001 is a structural inventory snapshot.

P7 establishes the existence of the persisted CMOC representation.

The inventory/index layer may subsequently discover and index that representation through its deterministic mechanism.

P7 must not silently edit an inventory snapshot merely to make C3 pass.

## 8. Output

Successful output: CMOC_WRITE_ACCEPTED.

The output must preserve:
- object_id;
- run/source/batch lineage;
- write identity;
- provenance;
- traceability;
- verification of persisted representation.

Possible non-success states include:
- CMOC_WRITE_REJECTED;
- EXISTING_OBJECT_WRITE_CONFLICT;
- POST_WRITE_VERIFICATION_FAILED;
- ALREADY_PERSISTED.

## 9. Boundary invariants

P7 must not:
- change DECISION;
- change RECONCILIATION_RESULT;
- repeat semantic comparison;
- decide NEW;
- alter canonical object identity;
- invent relations;
- mutate OBJECT INDEX;
- use QUERY to determine admission;
- use LLM to repair missing semantic content.

## 10. Relationship to C3/P8

C3 starts only after CMOC_WRITE_ACCEPTED.

C3 derives OBJECT INDEX from persisted CMOC state.

P7 does not require C3 to validate the existence of the object.

C3 may report INDEX_MISSING_OBJECT if the deterministic index source does not yet represent the persisted object.

This is a synchronization condition, not a reason for P7 to mutate the index.

## 11. Acceptance test scope

The first executable test shall verify:
1. valid CANONICALIZATION_READY is persisted;
2. object identity is preserved;
3. required registration fields are present;
4. persisted representation is readable;
5. repeat write is ALREADY_PERSISTED;
6. changed representation is EXISTING_OBJECT_WRITE_CONFLICT;
7. invalid entry is rejected;
8. no OBJECT INDEX mutation occurs;
9. no semantic operation occurs.

The test is a P7 registration boundary test. It does not establish P8 synchronization.

## 12. Current status

CONTRACT CANDIDATE — v0.1.

This contract closes the distinction between CMOC object persistence and CMOC-INVENTORY / OBJECT INDEX derivation.

The next controlled step is an isolated P7 registration acceptance test against the existing ProductionCmocWriter.