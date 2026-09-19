# TASK-CONTRACT-001-M07 — RELATIONS — SRC-002

**Version:** v0.2  
**Date:** 19-09-2026  
**Status:** Controlled contract  
**Basis:** STD-008 v0.7, TASK-CONTRACT-001 v0.2, controlled M06 SRC-002 output, M07-001 negative test.

## 1. INPUT

Primary input: `PASSPORT_RECORDS` from M06.

Optional controlled evidence context may accompany the passports when the purpose is to test the MULTI-OBJECT relation branch. Such context must contain only source-bound evidence explicitly available in the controlled SOURCE_PACKAGE.

Controlled SRC-002 input:
- SOURCE_ID: `SRC-002`
- upstream BATCH: `BATCH-SRC-002-M06-001`
- source package: `SOURCE-002-PACKAGE-001-CONTROLLED-1-6`
- Passport cardinality: 7

## 2. OPERATION

Identify only source-supported relation candidates between passport endpoints.

A relation candidate requires:
1. two explicit passport endpoints;
2. source-bound basis for the relation;
3. a relation type;
4. explicit evidence/basis reference;
5. no reliance on external knowledge.

For MULTI-OBJECT testing, relation evidence may be supplied separately from the passport fields, but it must be traceable to the controlled SOURCE_PACKAGE.

## 3. OUTPUT

Output type: `RELATION_CANDIDATES`.

Permitted result states:
- `RELATION_CANDIDATE`
- `NO_RELATION`
- `NEEDS_EVIDENCE`

A relation candidate is provisional and is not an established CMOC relation.

## 4. CARDINALITY

`N → M`.

The result is not required to contain a candidate for every possible pair. Every evaluated scope must have an explicit result.

## 5. REQUIRED FIELDS

### Input Passport Record
- `id`
- `candidate_id`
- `source_id`
- `term`
- `working_class`
- `source_basis`

### Controlled relation evidence
- `evidence_id`
- `locations`
- `text`
- `supports`

### Relation Candidate
- `id`
- `source_id`
- `from_passport_id`
- `to_passport_id`
- `relation_type`
- `status`
- `epistemic_status`
- `basis_refs`
- `evidence_gap`

## 6. STATUS RULE

Default relation candidate status:
- lifecycle: `ЧЕРНОВИК`
- epistemic: `PROVISIONAL`

`NO_RELATION` is an explicit negative result, not an absence of processing.

`NEEDS_EVIDENCE` requires a concrete `EVIDENCE_GAP`.

## 7. TRACEABILITY

Minimum lineage:

`SRC-002 → BATCH-SRC-002-M06-001 → PASSPORT_ID → RELATION_ID`

When separate evidence context is used, the relation candidate additionally retains `basis_refs` to that evidence.

## 8. PROHIBITIONS

M07 must not:
- establish a canonical relation;
- assign `CANONICAL`;
- create relations from external knowledge;
- infer causal, hierarchical, dependency or justificatory relations without explicit source basis;
- treat `SAME SOURCE` as a relation;
- treat `SAME TERM` as identity or relation;
- use absence of evidence as evidence;
- silently discard an evaluated input.

## 9. COMPLETION CRITERIA

M07 is complete when:
- all declared input scope is explicitly processed;
- endpoints are bound to existing passports;
- every relation candidate has basis references;
- relation candidates remain provisional;
- no canonical relation is created;
- insufficient evidence is explicitly returned;
- traceability is complete.

## 10. CONTROLLED SRC-002 TESTS

### M07-001 — negative boundary

Passports only, without relation evidence.

Expected result: `NO_RELATION`.

### M07-002 — MULTI-OBJECT positive branch

Use explicit source evidence from the controlled pages 1–6 package.

The test must demonstrate that M07 can create a relation candidate when both endpoints and source evidence are explicitly present.

The test must not use external knowledge or a relation inferred merely from the existence of both terms in the same source.
