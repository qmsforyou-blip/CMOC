# AUTOMATED-RUN-001 — M01–M03

Дата: 18-09-2026

## Назначение

Первый автоматизированный контроль MACHINE-SOURCE-001. Проверяется не качество содержания конкретного Источника как такового, а способность агентского контура выполнить фиксированные контракты M01–M03 без ручного конструирования промежуточных результатов.

## Контур

`SOURCE_PACKAGE → M01 → M02 → M03`

### M01

Input: SOURCE_PACKAGE  
Operation: принять, проверить комплектность и зафиксировать Source  
Output: Extraction Batch

### M02

Input: Extraction Record  
Operation: получить source-grounded distinction  
Output: Distinction Record

### M03

Input: Distinction Record  
Operation: сформировать три уровня формулировки  
Output: 3 Formulation Records на каждое различение

## Вход

Использовать тот же логический SOURCE, который был применён в repeatability-контроле GOST ISO 10002-2007, но не передавать агенту результаты Run A/B или результаты M04–M08.

Минимальный интерфейс:

```
SOURCE_ID
SOURCE_NAME
SOURCE_TYPE
SOURCE_VERSION
SOURCE_PACKAGE
PRIMARY_YIELD
BATCH_PREFIX
WORK_SCOPE
TASK
```

TASK для пилота: EXTRACTION.

## Запреты

- не использовать результаты предыдущих Run как вход;
- не переносить готовые Distinction/Formulation Records;
- не канонизировать;
- не выполнять M04–M08;
- не скрывать пропуски;
- не исправлять результат вручную после выполнения агентом.

## QC

### Gate A — Interface

Все обязательные поля SOURCE_PACKAGE присутствуют.

### Gate B — Handoff

M01 Output принимается M02 без ручного преобразования.

M02 Output принимается M03 без ручного преобразования.

### Gate C — Cardinality

M01: 1 SOURCE → 1 Batch.

M02: N Extraction Records → N Distinction Records.

M03: N Distinctions → 3N Formulations.

### Gate D — Trace

Каждая Formulation должна иметь путь:

`FORMULATION → DISTINCTION → EXTRACTION → BATCH → SOURCE`

### Gate E — Semantic boundary

M03 не должен превращать формулировку в CMOC Canon.

## Definition of Done

Пилот считается успешным, если:

- агент выполнил M01–M03;
- промежуточные результаты передавались по контракту;
- кардинальности соблюдены;
- трассировка сохранена;
- отсутствовала ручная реконструкция промежуточных результатов;
- запреты соблюдены;
- ошибки/UNKNOWN/N/A получили явный статус;
- результат пригоден для последующего M04.

## Следующий шаг

После выполнения пилота:

1. QC результатов;
2. при PASS — расширение автоматического контура до M04–M06;
3. затем M07–M08;
4. затем полный AUTOMATED RUN M01–M08.
