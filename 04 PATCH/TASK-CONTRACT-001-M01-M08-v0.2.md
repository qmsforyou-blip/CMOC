# TASK-CONTRACT-001 — Formal TASK Contracts M01–M08

**Version:** v0.2
**Date:** 18-09-2026
**Status:** Candidate — evidence-backed, pending incorporation into STD-008
**Basis:** STD-008 v0.6, SPEC-002 v0.3, controlled runs SRC-002 and SRC-003, TASK-CONTRACT-001 QC audits.

## 1. Purpose

Define the minimum production contract for each TASK of MACHINE-SOURCE-001.

A TASK contract determines permitted input, operation, output, cardinality, traceability, status, completion, exception return and prohibitions.

A TASK is not assumed to require the preceding TASK unless its contract says so.

## 2. Contract table

| TASK | Direct SOURCE_PACKAGE input | Previous-output input | Output | Evidence |
|---|---|---|---|---|
| M01 EXTRACTION | YES | NO | Extraction Records | TESTED |
| M02 DISTINCTIONS | YES | YES | Distinction Records | TESTED — SRC-003 Run-006 |
| M03 FORMULATIONS | YES | YES | 3 Formulations / input | TESTED — SRC-003 Run-007 |
| M04 NOMENCLATURE | NO | YES | Nomenclature Candidates | TESTED |
| M05 CLASSIFICATION | NO | YES | Classification Records | TESTED |
| M06 PASSPORT | NO | YES | Passport Records | TESTED |
| M07 RELATIONS | NO | YES | NO_RELATION / Relation Candidates | TESTED |
| M08 CANONIZATION DECISION | NO | YES | Decision | TESTED |

**Scope note:** “TESTED” means the stated interface path has controlled evidence in the recorded runs. It does not mean universal semantic validity for all possible source/task combinations.

## 3. Common contract

Every TASK requires SOURCE_ID, BATCH_ID, TASK, SOURCE_PACKAGE_STATUS, TRACEABILITY and STATUS.

Every TASK must return an explicit result for every processed input or an explicit N/A / UNKNOWN / NEEDS_EVIDENCE / production-stop result with reason.

## 4. M01 EXTRACTION

INPUT: SOURCE_PACKAGE.

OPERATION: source-only extraction of supported observations.

OUTPUT: Extraction Records.

CARDINALITY: source-dependent; tested 40, 100 and 20 records.

PROHIBITIONS: synthesis, downstream classification, passport, relation, canonization.

## 5. M02 DISTINCTIONS

INPUT: Extraction Record OR, when explicitly contracted, SOURCE_PACKAGE.

OPERATION: identify an engineering distinction supported by the input.

OUTPUT: Distinction Record.

CARDINALITY: normally 1→1 in tested paths.

Direct SOURCE_PACKAGE mode was cleanly tested on SRC-003, Run-006: 20 source locations → 20 distinctions. Existing M01/M02 artifacts were not operational inputs.

PROHIBITIONS: invention, formulation, classification, passport, relation, canonization.

## 6. M03 FORMULATIONS

INPUT: Distinction OR, when explicitly contracted, SOURCE_PACKAGE.

OPERATION: produce three formulation levels: intuitive, engineering, canonical-form.

OUTPUT: 3 Formulation Records per input unit.

CARDINALITY: 1→3 in tested paths.

Direct SOURCE_PACKAGE mode was cleanly tested on SRC-003, Run-007: 20 source observations → 60 formulations. Existing M01/M02/M03 artifacts were not operational inputs.

CANONICAL_FORM is a formulation level, not CMOC CANONICAL status.

PROHIBITIONS: classification, passport, relation, canonization.

## 7. M04 NOMENCLATURE

INPUT: Formulation group.

OPERATION: select nomenclature candidate.

OUTPUT: Nomenclature Candidate.

CARDINALITY: tested 3 formulations → 1 candidate.

PROHIBITIONS: classification, passport, relation, canonization.

## 8. M05 CLASSIFICATION

INPUT: Nomenclature Candidate.

OPERATION: source-derived provisional type assignment.

OUTPUT: Classification Record.

CARDINALITY: 1→1 in tested paths.

STATUS: PROVISIONAL unless contract-specific evidence permits another result.

PROHIBITIONS: passport, relation, canonization.

## 9. M06 PASSPORT

INPUT: Classification Record.

OPERATION: assemble source-derived passport.

OUTPUT: Passport Record.

CARDINALITY: 1→1 in tested paths.

Default tested status: LIFE_STATUS=ЧЕРНОВИК, EPISTEMIC_STATUS=PROVISIONAL.

PROHIBITIONS: inventing properties, relations, canonization.

## 10. M07 RELATIONS

INPUT: Passport Records.

OPERATION: identify source-supported relation candidates between two endpoints.

Modes: ISOLATED — one passport → explicit NO_RELATION; MULTI-OBJECT — multiple passports → relation candidates when both endpoints and evidence are present.

CARDINALITY: N→M.

A relation candidate is not an established CMOC relation.

PROHIBITIONS: external knowledge, automatic canonical relation.

## 11. M08 CANONIZATION DECISION

INPUT: Passport and, where applicable, Relation Candidate plus relation evidence.

OPERATION: apply DECISION RULE.

Sequence: Source Evidence → Object Boundary → Type Assignment → PROVISIONAL if all pass → CANONICAL only under separate CMOC criterion.

NEEDS_EVIDENCE requires EVIDENCE_GAP.

A relation candidate does not become a canonical relation automatically.

## 12. Completion rule

TASK is complete only when all declared inputs have an explicit result, cardinality is checked, traceability is present, required statuses are present, prohibited downstream fields are absent, and exceptions are explicitly recorded.

## 13. Architectural conclusion

The machine is specified as:

**fixed core + interchangeable SOURCE_PACKAGE + explicit TASK contract + BATCH.**

The contract, not an assumed linear sequence, determines the valid input path for a TASK.

This v0.2 is evidence-backed but remains a candidate pending incorporation into STD-008.
