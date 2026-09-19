# TASK-CONTRACT-001-M07 — RELATIONS — SRC-002

**Version:** v0.1  
**Date:** 19-09-2026  
**Status:** Controlled contract  
**Basis:** STD-008 v0.7, TASK-CONTRACT-001 v0.2, controlled M06 SRC-002 output.

## 1. INPUT

`PASSPORT_RECORDS` from M06.

Controlled input:
- SOURCE_ID: `SRC-002`
- upstream BATCH: `BATCH-SRC-002-M06-001`
- source package: `SOURCE-002-PACKAGE-001-CONTROLLED-1-6`
- cardinality: 7 Passport Records

## 2. OPERATION

Identify only source-supported relation candidates between passport endpoints.

A relation candidate requires:
1. two explicit passport endpoints;
2. source-bound basis for the relation;
3. a relation type;
4. an explicit evidence/basis reference;
5. no reliance on external knowledge.

If the supplied passport input does not contain sufficient relation evidence, M07 returns an explicit `NO_RELATION` result with a concrete reason. It must not infer a relation merely from:
- similar or related terminology;
- working class;
- common source;
- shared formulation basis;
- adjacency in the source;
- presumed hierarchy;
- presumed causality;
- presumed dependency.

## 3. OUTPUT

Output type: `RELATION_CANDIDATES`.

Permitted result states:
- `RELATION_CANDIDATE`
- `NO_RELATION`
- `NEEDS_EVIDENCE`

A relation candidate is provisional and is not an established CMOC relation.

## 4. CARDINALITY

`N → M`.

For the controlled SRC-002 test, the result is not required to contain a candidate for every possible pair. Every evaluated input scope must have an explicit result.

## 5. REQUIRED FIELDS

### Input Passport Record
- `id`
- `candidate_id`
- `source_id`
- `term`
- `working_class`
- `source_basis`

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

For a negative result:

`SRC-002 → BATCH-SRC-002-M06-001 → evaluated passport scope → NO_RELATION`

## 8. PROHIBITIONS

M07 must not:
- establish a canonical relation;
- assign `CANONICAL`;
- create relations from external knowledge;
- infer causal, hierarchical, dependency or justificatory relations without explicit basis;
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

## 10. CONTROLLED SRC-002 EXPECTATION

The current M06 passports contain candidate terms, working classes and upstream formulation references, but do not themselves contain explicit relation evidence.

Therefore M07 must not manufacture relations from these fields.

The controlled test must establish this negative boundary explicitly.