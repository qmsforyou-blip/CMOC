# CONTROL-RUN-013 — CONTRACT REJECT TEST — SRC-002 M02→M04

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**SUPERAGENT:** MVP-SUPERAGENT-001  
**MACHINE:** MACHINE-SOURCE-001  
**SOURCE_ID:** SRC-002  
**Test type:** negative / contract boundary

## 1. Purpose

Проверить реальным переходом, что суперагент не продолжает производственную цепочку, если OUTPUT предыдущей машины не соответствует входному контракту следующей машины.

Проверяем переход:

`M02 DISTINCTIONS → M04 NOMENCLATURE`

## 2. Declared input

Input для перехода взят из результата реального RUN-002:

- Output producer: M02 DISTINCTIONS
- Output type: **Distinction Records**
- Source: SRC-002
- Production batch: `BATCH-SRC-002-M02-002`
- Traceability: retained
- Status: ACCEPT

Важно: это **явный HANDOFF**, а не скрытое использование предыдущего результата.

## 3. Requested next TASK

**TASK:** M04 NOMENCLATURE

По TASK-CONTRACT-001 для M04:

- required input: **Formulation Records**
- output: Nomenclature Candidates

## 4. Contract Gate

Сопоставление:

`ACTUAL INPUT = Distinction Records`

`REQUIRED INPUT = Formulation Records`

Therefore:

**CONTRACT_MISMATCH**

Причина:

`Distinction Records ≠ Formulation Records`

## 5. Superagent action

Expected and executed action:

**REJECT + REASON**

Производство M04 **не запускается**.

Не выполняются:
- преобразование Distinction Records в Formulation Records;
- скрытый вызов M03;
- поиск предыдущего M03 результата без явного HANDOFF;
- генерация Nomenclature Candidates;
- продолжение цепочки.

**M04 BATCH_ID не создаётся**, поскольку M04 не был допущен к исполнению.

## 6. Result

**CONTROL-RUN-013 = PASS**

The contract boundary worked as intended:

`OUTPUT(M02) + HANDOFF → CONTRACT CHECK → REJECT`

rather than:

`OUTPUT(M02) → silent conversion → M04`

## 7. Evidence

This test establishes:

1. the superagent can reject a type-incompatible handoff;
2. rejection occurs before downstream machine execution;
3. rejection contains an explicit reason;
4. no downstream output is fabricated after rejection;
5. no new downstream BATCH is created after contract rejection.

## 8. Boundary

This test establishes the **contract rejection behavior** for the tested M02→M04 transition.

It does not establish rejection behavior for every possible contract violation or every TASK pair.
