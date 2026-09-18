# CONTROL-RUN-014 — STRUCTURAL CONTRACT REJECT — SRC-002 M03→M04

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**SUPERAGENT:** MVP-SUPERAGENT-001  
**MACHINE:** MACHINE-SOURCE-001  
**SOURCE_ID:** SRC-002  
**Test type:** negative / structural contract violation

## 1. Purpose

Проверить второй уровень контрактной границы: вход имеет правильный тип для следующей машины, но не удовлетворяет обязательному структурному условию — отсутствует обязательная трассировка происхождения.

Проверяем переход:

`M03 FORMULATIONS → M04 NOMENCLATURE`

## 2. Declared handoff

Базовый результат M03 существует в RUN-002:

- Output producer: M03 FORMULATIONS
- Output type: **Formulation Records**
- Source: SRC-002
- Production batch: `BATCH-SRC-002-M03-002`

Для теста создаётся **искажённая копия handoff**, в которой намеренно удалено обязательное поле:

- `TRACEABILITY` = MISSING

Остальные условия типа входа сохраняются.

Это не изменение исторического M03 output и не изменение RUN-002.

## 3. Requested next TASK

**TASK:** M04 NOMENCLATURE

Expected input type:

**Formulation Records**

The test input satisfies the type requirement.

## 4. Structural Contract Gate

Проверка:

- input type = Formulation Records — PASS
- required source traceability = MISSING — FAIL
- provenance of individual formulation records cannot be verified — FAIL

Therefore:

**STRUCTURAL_CONTRACT_MISMATCH**

## 5. Superagent action

Expected and executed action:

**REJECT + REASON**

M04 не запускается.

Не выполняются:
- восстановление TRACEABILITY по памяти;
- обращение к RUN-002 как к скрытому источнику;
- поиск соответствующих source locations;
- генерация Nomenclature Candidates;
- создание полноценного M04 output.

**M04 BATCH_ID не создаётся.**

## 6. Result

**CONTROL-RUN-014 = PASS**

The superagent rejected a type-compatible but structurally invalid handoff.

Проверенная логика:

`OUTPUT + HANDOFF → TYPE CHECK → STRUCTURAL CHECK → REJECT`

а не:

`TYPE MATCH → ACCEPT → downstream execution`

## 7. Evidence boundary

Established:
1. type compatibility alone is insufficient;
2. required traceability is a contract condition;
3. missing traceability blocks downstream execution;
4. the superagent does not silently reconstruct missing provenance;
5. no downstream BATCH is created after rejection.

Not established:
- all possible structural contract violations;
- universal validation of every M04 field.
