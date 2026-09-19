# TASK-CONTRACT-001-M06-PASSPORT-SRC-002-v0.1

**Дата:** 19-09-2026  
**Статус:** Candidate — production contract for controlled SRC-002 pass

## INPUT

`CLASSIFICATION_RECORDS`

One Classification Record per nomenclature candidate.

## OPERATION

Form one source-bound Passport Record for each Classification Record.

The Passport records the candidate boundary, working classification, source basis and production lineage.

## OUTPUT

`PASSPORT_RECORDS`

## CARDINALITY

`1 Classification Record → 1 Passport Record`

## REQUIRED INPUT FIELDS

- `id`
- `candidate_id`
- `type`
- `status`
- `uncertainty`
- `source_id`

## REQUIRED OUTPUT FIELDS

- `id`
- `candidate_id`
- `classification_id`
- `source_id`
- `batch_id`
- `task`
- `term`
- `working_class`
- `lifecycle_status`
- `epistemic_status`
- `object_boundary`
- `source_basis`
- `traceability`

## STATUS RULE

For this controlled SRC-002 production pass:

- `lifecycle_status = ЧЕРНОВИК`
- `epistemic_status = PROVISIONAL`

The two statuses are independent and must not be merged.

## TRACE RULE

Minimum lineage:

`SRC-002 → BATCH-SRC-002-M05-001 → CLASSIFICATION_ID → BATCH-SRC-002-M06-001 → PASSPORT_ID`

The passport must retain the source package reference where available.

## OBJECT BOUNDARY

The Passport is a source-bound working record.

It does not establish a canonical CMOC object.

## PROHIBITIONS

M06 must not:

- create relations;
- perform canonization;
- assign `CANONICAL`;
- add unsupported external properties;
- promote a candidate to canonical object;
- infer properties not supported by the supplied classification and source basis.

## COMPLETION CRITERIA

PASS only when:

1. every input classification has exactly one passport;
2. every passport references its input `classification_id`;
3. source and batch traceability are preserved;
4. lifecycle and epistemic statuses are explicit;
5. object boundary is explicit;
6. no relation or canonization fields are produced;
7. unsupported properties are not introduced.

## EXCEPTION

If the basis is insufficient to define the passport boundary, return `NEEDS_EVIDENCE` with a concrete `EVIDENCE_GAP`. Do not silently invent missing properties.