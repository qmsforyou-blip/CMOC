# TASK-CONTRACT-001 — M08 CANONIZATION DECISION — SRC-002

**Version:** v0.1
**Date:** 19-09-2026
**Status:** Controlled production contract
**Basis:** TASK-CONTRACT-001 v0.2, M06/M07 production evidence for SRC-002

## 1. Purpose

Define the controlled M08 decision interface for SRC-002.

M08 evaluates source-bound Passport Records and, where applicable, a source-supported Relation Candidate plus its relation evidence. M08 produces a Decision Record. It does not silently promote a provisional passport, relation candidate, or nomenclature candidate to canonical status.

## 2. Input

Required:
- PASSPORT_RECORDS
- source_id
- source_package_status
- upstream M06 batch
- traceability

Optional but required for the relation-dependent branch:
- RELATION_CANDIDATES
- relation evidence

Controlled SRC-002 input:
- 7 Passport Records from BATCH-SRC-002-M06-001
- REL-001 from BATCH-SRC-002-M07-002
- EVID-SRC-002-P2-STRATEGY-SET-001

## 3. Decision sequence

M08 applies this sequence:

1. Source Evidence
2. Object Boundary
3. Type Assignment
4. PROVISIONAL if the controlled gates pass
5. CANONICAL only when a separate CMOC canonicalization criterion is explicitly supplied and passed

For the current SRC-002 controlled run, no separate canonicalization criterion is supplied. Therefore M08 must not produce CANONICAL.

## 4. Output

OUTPUT: DECISION_RECORDS.

Each decision record must explicitly identify:
- id
- source_id
- batch_id
- target_id
- target_kind
- decision
- lifecycle_status
- epistemic_status
- reason
- basis_refs
- traceability

Permitted controlled decisions:
- PROVISIONAL
- CANONICAL
- NEEDS_EVIDENCE
- REJECT

For this SRC-002 run, expected decision for the supported relation candidate is PROVISIONAL.

## 5. Relation-dependent rule

A RELATION_CANDIDATE may be evaluated only when:
- both endpoint passports exist;
- relation candidate status is RELATION_CANDIDATE;
- relation epistemic status is PROVISIONAL;
- basis_refs identify explicit source evidence;
- the referenced evidence supports the declared endpoints and relation type.

A relation candidate does not become a canonical relation automatically.

## 6. Prohibitions

M08 must not:
- use external knowledge;
- invent object properties;
- infer unsupported relations;
- treat a term occurrence as a canonical entity;
- promote PROVISIONAL to CANONICAL without an explicit canonicalization criterion;
- create canonical relation solely because M07 produced a relation candidate;
- silently fill missing evidence.

If evidence is insufficient, return NEEDS_EVIDENCE with a concrete evidence_gap.

## 7. Completion

M08 is complete only when every declared input has an explicit decision, cardinality is checked, traceability is present, decision status is explicit, basis references are preserved, and canonical promotion is controlled by an explicit criterion.

## 8. Evidence boundary

This contract is valid only for the controlled SRC-002 production run and pages 1–6 of the PARTIAL source package. It does not establish universal semantic validity for other sources.
