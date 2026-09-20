# EVIDENCE-A3-RECONCILIATION-SRC-002-001

**Date:** 20-09-2026  
**Status:** ACCEPTED  
**Stage:** A3 — RECONCILIATION IMPLEMENTATION / QUERY CONTROL

## 1. Purpose

This evidence records the first QUERY-backed reconciliation control after the read-only boundary adapter was accepted.

The control verifies:

`M06 PASSPORT_RECORDS → RECONCILIATION_INPUT → QUERY → RECONCILIATION`

without modifying DISCOVERY, the OBJECT INDEX, or the source-bound Passport records.

## 2. Boundary

Discovery remains upstream:

`SOURCE → MACHINE-SOURCE-001 → DISCOVERY_RESULT`

Reconciliation starts only after the Discovery boundary:

`DISCOVERY_RESULT → RECONCILIATION_INPUT → RECONCILIATION → CMOC / OBJECT INDEX / QUERY`

No CMOC / OBJECT INDEX / QUERY input is supplied to M01–M08.

## 3. Implementation under test

Read-only adapter:

`05 SUPERAGENT/reconciliation_input_adapter.py`

Commit:

`6a61b3cc11ed8f8a0cff72364f7620931f4242bb`

The adapter maps M06 Passport fields:

- `id` → `record_id`
- `term` → `value`
- source and upstream identifiers → `traceability`

It does not infer `target_object_type`, call QUERY, access CMOC, or modify Discovery.

A3 implementation gate was previously executed and returned PASS for 7 production-derived SRC-002 Passport records.

## 4. Real SRC-002 negative control

Input:

- source_id: `SRC-002`
- input_batch_id: `BATCH-SRC-002-M06-006`
- input_output_type: `PASSPORT_RECORDS`
- query_scope: `TERMS`
- records: 7 production-derived M06 Passport records

Relevant record:

- Passport: `PAS-006`
- term/value: `Fast Response`

Observed result:

- `match_result: NEEDS_REVIEW`
- `cmoc_object_id: null`
- basis: `NO_MATCH from configured query modes; NEW not yet proven`
- status: `PROVISIONAL`

Physical OBJECT INDEX inspection established that the string `Fast Response` occurs inside indexed representations, including GM formulation content, but no record in `records` has `object_name == "Fast Response"`.

Therefore the current EXACT/ALIAS reconciliation path has no indexed TERM object named `Fast Response` to match.

This result does **not** establish NEW. It establishes only that no match was found in the configured query modes.

The same SRC-002 reconciliation control reported:

- `discovery_mutation: NONE`
- `index_mutation: NONE`

## 5. Positive QUERY / Reconciliation control

A separate synthetic control record was used only to verify the positive branch of the existing QUERY/Reconciliation implementation.

Input:

- source_id: `TEST-SRC`
- input_batch_id: `TEST-BATCH`
- input_output_type: `PASSPORT_RECORDS`
- record_id: `TEST-PAS-001`
- value: `Требование`
- query_scope: `TERMS`

The OBJECT INDEX contains:

- object_id: `T-0011`
- object_type: `TERM`
- object_name: `Требование`

Observed result:

- `cmoc_object_id: T-0011`
- `match_result: EXISTING_EQUIVALENT`
- `basis: EXACT match`
- `status: PROVISIONAL`

This verifies that the configured positive branch can resolve an exact object-name match to its indexed object ID and return the current reconciliation result vocabulary.

The synthetic control does not modify the CMOC or source data.

## 6. A3 conclusion

A3 is ACCEPTED for the tested boundary and current implementation.

Confirmed:

1. M06 Passport records can be adapted into the declared RECONCILIATION_INPUT shape without semantic enrichment.
2. QUERY is invoked only after the Discovery boundary.
3. A real SRC-002 Passport with no indexed exact object-name match returns `NEEDS_REVIEW`, not `NEW`.
4. A controlled exact match to an existing TERM returns `EXISTING_EQUIVALENT` with the corresponding CMOC object ID.
5. Discovery records are not modified by Reconciliation.
6. The OBJECT INDEX is not modified by Reconciliation.
7. M07 relation candidates and M08 decision records are not part of this first object-reconciliation interface.

## 7. Limitation

This evidence does not establish:

- semantic equivalence beyond the current exact-match rule;
- NEW classification;
- conflict detection;
- relation reconciliation;
- positive relation-dependent M07/M08 behavior;
- Discovery reproducibility on a new source;
- distributed or process-isolated execution.

## 8. Next stage

Proceed to A4 — Negative Controls.

Required controls:

1. CMOC contains an equivalent object → Discovery result remains unchanged.
2. CMOC contains a similar object → Discovery result remains unchanged.
3. CMOC contains a conflicting object → Discovery result remains unchanged.
4. QUERY unavailable → source-bound Discovery pass remains executable independently.
5. Incomplete or ambiguous Discovery result → Reconciliation does not rewrite Discovery.

Core invariant:

`Сначала добываем. Потом сопоставляем.`
