# PATCH — AUTOMATED RUN M01→M08 — SRC-002 — NO_RELATION control

**Target:** `05 SUPERAGENT/mvp_runner.py` + production M01–M08 adapters  
**Run launcher:** `05 SUPERAGENT/run_automated_m01_m08_src002.py`  
**Date:** 19-09-2026  
**Status:** CANDIDATE — awaiting execution evidence

## Purpose

Move from the previously proven FULL SEQUENTIAL HANDOFF TEST to an executable production AUTOMATED RUN controlled by the SUPERAGENT runner.

The run must:

- invoke M01–M08 production handlers;
- pass the actual output of each TASK through HANDOFF to the next TASK;
- create BATCH records through the runner;
- preserve SOURCE_ID and traceability;
- avoid manual construction of semantic intermediate records;
- exercise the M07 negative branch without supplied relation evidence;
- pass the actual M07 output to production M08;
- ensure M08 does not fabricate a decision from `NO_RELATION`.

## Implementation

Added:

`05 SUPERAGENT/run_automated_m01_m08_src002.py`

The launcher injects the existing production adapters:

`M01-PRODUCTION ... M08-PRODUCTION`

No intermediate extraction, distinction, formulation, nomenclature, classification, passport or relation records are manually constructed by the launcher.

M07 receives an empty relation-evidence list deliberately.

## M08 boundary change

Production `m08_llm.decide()` now treats an explicit M07 `NO_RELATION` result as a terminal negative branch:

`NO_RELATION → M08 → DECISION_RECORDS with zero records`

The semantic model is not asked to reinterpret the negative result as a decision target.

Mixed `NO_RELATION` and relation records remain rejected pending explicit branch handling.

## Evidence condition

This PATCH is not closed until the launcher produces an ACCEPT result with:

- 8 production batches;
- 7 ACCEPT handoffs;
- M07 = `NO_RELATION`;
- M08 = zero decision records;
- complete traceability.

## Limitation

This control establishes an automated one-process runner execution. It does not establish independent distributed process execution.

It also does not test the positive relation-evidence branch; that branch is covered by separate controlled relation-dependent evidence.
