# CONTROL-RUN-016 — SOURCE SWAP — SAME MACHINE + TASK

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**SUPERAGENT:** MVP-SUPERAGENT-001  
**MACHINE:** MACHINE-SOURCE-001  
**TASK:** M01 EXTRACTION  
**Test type:** source interchangeability

## 1. Purpose

Проверить инвариант:

`MACHINE ≠ SOURCE`

Тот же фиксированный MACHINE-SOURCE-001 и тот же TASK M01 запускаются на другом SOURCE_PACKAGE. Изменение источника не должно требовать изменения машины.

## 2. Source

Используется другой проверенный источник из ранее выполненных работ:

**SOURCE_ID:** SRC-003

Для теста используется контролируемый фрагмент SOURCE-003, ранее применявшийся в direct-source контрольных прогонах.

**WORK_SCOPE:** 20 source observations/locations from the declared SRC-003 package.

Предыдущие результаты SRC-003 не используются как operational input.

## 3. Machine and Task

Machine remains exactly:

`MACHINE-SOURCE-001`

Task remains exactly:

`M01 EXTRACTION`

No source-specific modification is introduced.

New production identity:

**BATCH_ID:** BATCH-SRC-003-M01-001

## 4. Input gate

Checks:
- SOURCE_ID present — PASS
- SOURCE_PACKAGE present — PASS
- TASK present — PASS
- source scope declared — PASS
- traceability required — PASS
- no previous SRC-003 output used as operational input — PASS

Result: **ACCEPT**

## 5. M01 execution

M01 extracts source-grounded observations from the declared SRC-003 package.

Result:
- 20 source locations processed;
- 20 Extraction Records produced;
- every record retains source traceability;
- no external knowledge introduced.

**M01 result: PASS**

## 6. Source-swap criterion

The following remain unchanged:
- MACHINE;
- TASK;
- production logic;
- contract logic;
- traceability requirement.

The following changes:
- SOURCE_ID;
- SOURCE_PACKAGE;
- BATCH_ID;
- resulting OUTPUT content.

No machine modification is required.

## 7. Result

**CONTROL-RUN-016 = PASS**

The tested evidence supports:

`SAME MACHINE + SAME TASK + DIFFERENT SOURCE → VALID NEW OUTPUT`

## 8. Evidence boundary

Established:
- source substitution works for the tested M01 route;
- the fixed machine core does not require source-specific modification;
- a new source receives a new BATCH_ID;
- previous source outputs are not silently reused.

Not established:
- source interchangeability for every TASK M01–M08;
- semantic equivalence of outputs across different sources;
- universal source-package compatibility.
