# CONTROL-RUN-015 — REJECT → REPAIR → RETRY — SRC-002 M03→M04

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**SUPERAGENT:** MVP-SUPERAGENT-001  
**MACHINE:** MACHINE-SOURCE-001  
**SOURCE_ID:** SRC-002  
**Test type:** recovery / retry after contract rejection

## 1. Purpose

Проверить, что после REJECT суперагент способен принять исправленный вход и выполнить новый производственный проход, не переписывая исходный отклонённый проход.

## 2. Initial rejected handoff

Основание: CONTROL-RUN-014.

- producer: M03 FORMULATIONS
- output type: Formulation Records
- source: SRC-002
- original production batch: BATCH-SRC-002-M03-002
- defect: TRACEABILITY = MISSING
- result: STRUCTURAL_CONTRACT_MISMATCH
- downstream M04: not executed
- M04 batch: not created

CONTROL-RUN-014 remains unchanged.

## 3. Repair

Исправляется не исторический M03 output, а создаётся новый handoff package:

**REPAIR_ID:** REPAIR-SRC-002-001

Repair action:
- restore explicit source traceability for the handed-off formulation records;
- retain source identity SRC-002;
- retain provenance to the source locations used in RUN-002;
- retain producer identity M03;
- retain original M03 batch as provenance.

The rejected handoff is preserved as evidence of the defect.

## 4. Retry

New downstream TASK:

**M04 NOMENCLATURE**

New production identity:

**BATCH_ID:** BATCH-SRC-002-M04-001

### Contract Gate

- input type = Formulation Records — PASS
- required traceability present — PASS
- source identity present — PASS
- provenance retained — PASS
- handoff explicit — PASS

Result:

**ACCEPT**

### M04 execution

M04 is executed against the repaired handoff.

Output:

**Nomenclature Candidates**

The output is explicitly marked as the result of the retry and is not presented as the result of CONTROL-RUN-014.

## 5. Retry result

**CONTROL-RUN-015 = PASS**

The tested lifecycle is:

`VALID OUTPUT → REJECTED HANDOFF → REPAIR → NEW HANDOFF → CONTRACT CHECK → ACCEPT → NEW BATCH → NEW OUTPUT`

No historical record is rewritten.

## 6. What this proves

1. REJECT does not terminate the whole production system permanently.
2. A rejected handoff can be repaired through an explicit new artifact.
3. Retry receives a new BATCH_ID.
4. The original defective handoff remains traceable.
5. Downstream execution occurs only after the repaired handoff passes the contract gate.
6. The retry output has its own production identity.

## 7. Boundary

This test establishes recovery behavior for the specific structural defect tested in CONTROL-RUN-014.

It does not establish automatic repair: the repair package is an explicit input to the retry.
