# C3 — OBJECT INDEX SYNCHRONIZATION BOUNDARY

**ID:** C3-OBJECT-INDEX-SYNCHRONIZATION-BOUNDARY-001  
**Date:** 22-09-2026  
**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Scope:** CMOC WRITE → OBJECT INDEX  
**Basis:** C2 CMOC WRITE boundary + SPEC-004 CMOC OBJECT INDEX v0.2

## 1. Purpose

C3 defines the boundary between an already persisted CMOC representation and its deterministic derived representation in OBJECT INDEX.

C3 does not make semantic decisions.

> a confirmed CMOC write can be deterministically reflected in OBJECT INDEX without re-deciding what the object means.

## 2. Architectural position

NEW_APPROVED → C1 CANONIZATION → CANONICALIZATION_READY → C2 CMOC WRITE → CMOC_WRITE_ACCEPTED → C3 INDEX SYNCHRONIZATION → OBJECT INDEX

C3 is downstream of CMOC persistence.

## 3. Core principle

OBJECT INDEX is a derived, deterministic representation of addressable CMOC objects.

C3 must not become a second semantic layer.

## 4. Input

Minimum C3 input:

- status: CMOC_WRITE_ACCEPTED
- object_id
- canonical_representation
- provenance
- traceability
- write_id
- write_verification

The input must identify the persisted canonical object and the successful write operation.

## 5. Entry gate

C3 accepts only status = CMOC_WRITE_ACCEPTED.

The following are not valid entry states:
- CANONICALIZATION_READY;
- NEW_APPROVED;
- CMOC_WRITE_REJECTED;
- ALREADY_PERSISTED without a confirmed persisted representation;
- arbitrary canonicalization output.

C3 does not perform the missing upstream operation.

## 6. Deterministic derivation

C3 may invoke or represent the existing deterministic OBJECT INDEX build process.

It may:
- read persisted CMOC representations;
- enumerate addressable objects;
- derive deterministic index records;
- calculate deterministic counts;
- verify object identity;
- verify representation-to-index traceability;
- verify reproducibility.

It must not:
- infer semantic meaning;
- create semantic equivalence;
- decide NEW;
- perform semantic comparison;
- create unsupported relations;
- alter the canonical CMOC representation.

## 7. OBJECT INDEX is derived state

CMOC = canonical persisted representation.
OBJECT INDEX = derived addressable index.

An OBJECT INDEX record is not an independent semantic authority over the CMOC.

If a discrepancy exists between CMOC and derived index, C3 reports synchronization failure rather than resolving the discrepancy semantically.

## 8. Object identity

The persisted canonical object identity must be preserved.

CMOC.object_id must equal OBJECT_INDEX.object_id.

A mismatch is a synchronization failure.

C3 must not invent a replacement object identity.

## 9. Traceability

C3 must preserve the path:

SOURCE → DISCOVERY → NEW DECISION → CANONIZATION → CMOC WRITE → OBJECT INDEX

At minimum, the derived index record must remain traceable to the persisted CMOC object.

C3 must not manufacture missing provenance.

## 10. Deterministic reproducibility

For the same CMOC state and the same index-build version, repeated builds must produce the same derived result.

C3 must be reproducible. Repeated synchronization of unchanged CMOC state must not create semantic drift.

## 11. Existing index state

If the canonical object is already represented in OBJECT INDEX:

- same deterministic representation → ALREADY_SYNCHRONIZED;
- different derived representation → INDEX_SYNCHRONIZATION_CONFLICT.

C3 must not decide which representation is semantically correct.

## 12. Missing object

If CMOC contains the persisted object but OBJECT INDEX does not:

INDEX_MISSING_OBJECT.

C3 may regenerate the derived index through the deterministic builder.

It must not create a semantic object definition to fill the gap.

## 13. Index-only object

If OBJECT INDEX contains an object identity that cannot be derived from the current CMOC state:

INDEX_ORPHAN_OBJECT.

C3 must report the condition. It must not delete or semantically reinterpret the orphan automatically.

## 14. Counts and integrity

C3 may verify deterministic aggregate properties such as total representations, canonical OBJECT_FILE counts, REGISTRY_RECORD counts, unique object IDs, object-type counts, and deterministic hashes/checksums where defined.

These are integrity checks, not semantic decisions.

## 15. No semantic comparison

C3 must not execute Entity/Property/Relation/Mechanism/Capability semantic comparison, similarity, novelty inference, or conflict resolution.

The index is derived from CMOC; it is not a new semantic comparison set.

## 16. No NEW decision

C3 must not output NEW_APPROVED or NEW_REJECTED.

If a CMOC object has already been approved and persisted, C3 assumes that upstream decision is complete.

## 17. No canonization

C3 must not rename the canonical object, change object boundary, change object type, merge representations, split representations, or create canonical identity.

Any such discrepancy is upstream/canonicalization evidence, not a C3 decision.

## 18. No relation creation

C3 must not create semantic relations.

If a relation is part of the deterministic index representation, C3 may preserve it as derived data only when it already exists in persisted canonical CMOC representation and the index specification requires it.

C3 must not invent a relation.

## 19. No silent CMOC mutation

C3 is downstream of CMOC WRITE.

It must never modify the canonical CMOC representation as a side effect of index synchronization.

## 20. Proposed output

Possible statuses:
- INDEX_SYNCHRONIZED
- ALREADY_SYNCHRONIZED
- INDEX_MISSING_OBJECT
- INDEX_SYNCHRONIZATION_CONFLICT
- INDEX_ORPHAN_OBJECT
- C3_REJECTED

Output should preserve object_id, index_build_version, derived_record_count, traceability, verification, and basis.

## 21. Failure states

C3 may reject or report invalid entry state, missing persisted object identity, missing traceability, unavailable CMOC representation, object identity mismatch, index synchronization conflict, orphan index object, deterministic build failure, or post-build verification failure.

C3 must report the condition rather than repair semantics.

## 22. Relationship to OBJECT INDEX specification

C3 does not replace SPEC-004.

SPEC-004 remains the authority for OBJECT INDEX structure and deterministic construction.

C3 defines the operational boundary: persisted CMOC → deterministic OBJECT INDEX build → verification.

## 23. Relationship to QUERY

QUERY remains read-only over OBJECT INDEX.

C3 does not invoke QUERY to decide whether the persisted object is new or equivalent.

After successful synchronization, OBJECT INDEX → QUERY becomes available to downstream read operations.

## 24. LLM boundary

An LLM may assist with diagnostics or reporting of a synchronization failure, but C3 must not use an LLM to infer missing object identity, decide semantic equivalence, resolve index conflicts, invent relations, or repair canonical representation.

## 25. Synthetic test scope

The first C3 executable test shall be synthetic and isolated.

It should use an in-memory CMOC representation, an in-memory derived OBJECT INDEX, a deterministic builder stub, no production persistence runtime, no semantic engine, and no real CMOC mutation.

The test establishes the boundary contract, not production synchronization infrastructure.

## 26. Minimum test branches

1. valid CMOC_WRITE_ACCEPTED → INDEX_SYNCHRONIZED;
2. non-accepted entry → C3_REJECTED;
3. missing object identity → C3_REJECTED;
4. missing traceability → C3_REJECTED;
5. object absent from index → INDEX_MISSING_OBJECT / deterministic regeneration;
6. same representation already indexed → ALREADY_SYNCHRONIZED;
7. different representation → INDEX_SYNCHRONIZATION_CONFLICT;
8. orphan index object → INDEX_ORPHAN_OBJECT;
9. deterministic rebuild reproducibility;
10. object identity mismatch;
11. no semantic comparison;
12. no NEW decision;
13. no canonization;
14. no CMOC mutation;
15. no relation creation;
16. OBJECT INDEX changes only through deterministic derivation.

## 27. Architectural invariant

> C3 derives and verifies OBJECT INDEX from persisted CMOC state; it does not decide what the persisted object means.

## 28. Current status

DESIGN / ARCHITECTURE CANDIDATE.

This contract does not establish a production synchronization engine.

Next step: implement the isolated synthetic C3 test and verify the boundary before considering production integration.