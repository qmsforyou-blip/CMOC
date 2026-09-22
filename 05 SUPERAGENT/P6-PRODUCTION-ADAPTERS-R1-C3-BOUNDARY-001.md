# P6 — PRODUCTION ADAPTERS R1–C3

**Status:** DESIGN / ARCHITECTURE CANDIDATE

## 1. Purpose

P6 defines the boundary for replacing synthetic stage adapters with production adapters for the already established semantic/object chain:

`R1 → R10 → C1 → C2 → C3`

P6 is an integration/adapter boundary, not a new semantic layer.

The production adapters must preserve the contracts already established by R1-R10 and C1-C3.

## 2. Boundary

The production execution chain is:

`SOURCE / DISCOVERY RESULT → RECONCILIATION → NEW DECISION → CANONIZATION → CMOC WRITE → OBJECT INDEX SYNCHRONIZATION`

P6 does not redefine any stage's internal semantics.

It connects production runtime orchestration to existing stage contracts.

## 3. Adapter responsibilities

A production adapter may:

- accept the contracted input schema;
- validate required structural fields;
- invoke the corresponding production implementation;
- preserve RUN_ID and stage lineage;
- preserve ATTEMPT_ID and RESULT_ID;
- persist the contracted stage result;
- return the contracted result status;
- expose structural failure/rejection;
- report execution metadata required by RUN/ORCH/REC/P1-P5.

A production adapter must NOT:

- add semantic meaning;
- infer missing semantic evidence;
- reinterpret a rejection;
- convert NEEDS_REVIEW into NEW_APPROVED;
- perform hidden semantic comparison;
- silently canonize;
- mutate CMOC outside C2;
- mutate OBJECT INDEX outside C3;
- invent relations;
- repair semantic evidence.

## 4. Required production stage mapping

| Stage | Production adapter target | Required boundary |
|---|---|---|
| R1 | QUERY / RECONCILIATION | existing reconciliation contract |
| R2-R4 | NEW criteria / decision evidence | existing NEW decision chain |
| R5-R8 | semantic distinction/comparison/assembly | existing semantic contracts |
| R9-R10 | NEW evidence aggregation/rule | existing NEW decision contract |
| C1 | CANONIZATION | CANONICALIZATION_READY only |
| C2 | CMOC WRITE | CMOC_WRITE_ACCEPTED / REJECTED |
| C3 | OBJECT INDEX SYNC | INDEX synchronization result |

The table is an adapter map, not a new semantic specification.

## 5. Input/output invariants

Every production adapter must preserve:

`RUN_ID`

`SOURCE_ID`

`BATCH_ID`

`STAGE_ID`

`ATTEMPT_ID`

`RESULT_ID`

and the stage-specific traceability required by the upstream contract.

The adapter must not replace an upstream result with a newly inferred result.

## 6. Production result rule

A production adapter result is authoritative only when:

1. the contracted stage executed;
2. its required inputs were accepted;
3. the stage produced a contract-valid result;
4. the result was persisted according to the P1-P5 runtime boundary;
5. lineage remains valid.

Execution success does not imply semantic approval.

## 7. Stage-specific restrictions

### R1–R10

The adapter must preserve the semantic decisions produced by the established R1-R10 contracts.

It must not move semantic responsibility into orchestration, runtime recovery, persistence, or adapter code.

### C1

Input must be `NEW_APPROVED`.

Output must remain `CANONICALIZATION_READY`.

The adapter must preserve the approved-candidate integrity anchor.

### C2

Input must be `CANONICALIZATION_READY`.

C2 remains the only CMOC persistence boundary for this chain.

### C3

Input must be `CMOC_WRITE_ACCEPTED`.

C3 remains the only synchronization boundary for OBJECT INDEX.

## 8. Production readiness checks

P6 must verify at minimum:

- production implementation is actually invoked;
- synthetic stub is not used;
- input contract validation is active;
- output contract validation is active;
- RUN_ID is preserved;
- ATTEMPT_ID is preserved;
- RESULT_ID is preserved;
- stage failure is distinguishable from semantic rejection;
- retry does not overwrite prior attempt;
- duplicate invocation remains idempotent;
- C2 is the only CMOC write boundary;
- C3 is the only OBJECT INDEX synchronization boundary.

## 9. Failure boundary

P6 must expose adapter failures explicitly:

- `ADAPTER_INPUT_REJECTED`
- `ADAPTER_EXECUTION_FAILED`
- `ADAPTER_OUTPUT_INVALID`
- `ADAPTER_LINEAGE_INVALID`
- `SYNTHETIC_ADAPTER_DETECTED`
- `PRODUCTION_ADAPTER_UNAVAILABLE`

No adapter failure may be converted into a semantic result.

## 10. Synthetic-to-production transition

The first P6 gate should NOT pretend that production adapters already exist.

The test must establish the adapter boundary itself and detect whether the implementation under test is synthetic or production.

A passing P6 gate therefore means:

**the runtime can distinguish and structurally validate a production adapter path without changing the established semantic contracts.**

It does not yet mean that every R1-C3 production implementation is fully operational.

## 11. Synthetic test boundary

The first P6 test is a production-adapter harness test.

It must demonstrate at minimum:

1. production adapter accepted;
2. synthetic adapter rejected;
3. input contract preserved;
4. output contract preserved;
5. RUN_ID preserved;
6. ATTEMPT_ID preserved;
7. RESULT_ID preserved;
8. stage failure distinct from semantic rejection;
9. duplicate invocation remains idempotent;
10. C2-only CMOC write boundary;
11. C3-only index synchronization boundary;
12. no semantic responsibility leakage.

P6 deliberately does not invent missing production implementations.
