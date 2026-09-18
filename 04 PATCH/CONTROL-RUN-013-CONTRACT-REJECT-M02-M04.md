# CONTROL-RUN-013 — Contract Reject M02→M04

## Purpose

Проверить, что суперагент не передаёт результат M02 непосредственно в M04, если тип входа не соответствует контракту M04.

## Route

```
SOURCE_PACKAGE
   ↓
M02
   ↓
DISTINCTION_RECORDS
   ↓
M04
   ↓
CONTRACT CHECK
   ↓
REJECT
```

## Expected contract

- M02 output: `DISTINCTION_RECORDS`
- M04 accepted input: `FORMULATION_RECORDS`

Therefore:

`DISTINCTION_RECORDS → M04 = TYPE_MISMATCH → REJECT`

## Test

The executable MVP runner test `test_contract_reject_before_execution` performs:

1. execute M02 successfully;
2. pass the M02 output to M04;
3. verify `status = REJECT`;
4. verify reason contains `TYPE_MISMATCH`;
5. verify `batch_id = None` for rejected M04;
6. verify no M04 Batch is created in the journal.

## Result

**PASS**

M04 is rejected at the contract gate before production execution.

## Architectural meaning

The test confirms the operational form of INV-002:

**HANDOFF does not mean automatic acceptance.**

It also confirms the negative path:

`CONTRACT MISMATCH → REJECT → STOP`

No silent conversion from Distinction Records to Formulation Records is performed.

## Boundary

This control run proves the tested M02→M04 type mismatch behavior in the deterministic MVP runner. It does not establish universal correctness for every machine contract.

## Related architecture

- INV-001 — MACHINE ≠ SOURCE ≠ TASK ≠ BATCH
- INV-002 — HANDOFF ≠ automatic acceptance
- INV-003 — managed correction after NEEDS_EVIDENCE
- ARCH-002 — orchestration architecture
- ARCH-003 — managed correction cycle
