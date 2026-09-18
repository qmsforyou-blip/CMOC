# TASK-CONTRACT-002 — RECONCILIATION v0.1

## 1. Назначение

TASK-CONTRACT-002 определяет интерфейс второй производственной функции CMOC — RECONCILIATION.

RECONCILIATION сопоставляет накопленный результат DISCOVERY с доступным слоем ядра CMOC.

Она не выполняет повторную добычу источника.

## 2. Инвариант разделения

**DISCOVERY добывает. RECONCILIATION сопоставляет.**

RECONCILIATION не должна менять source-bound результат DISCOVERY.

## 3. Вход

Обязательные параметры:

```
SOURCE_ID
INPUT_BATCH_ID
INPUT_OUTPUT_TYPE
INPUT_RECORDS
TRACEABILITY
CMOC_QUERY_SCOPE
```

INPUT_RECORDS — конкретный результат предыдущего production pass.

CMOC_QUERY_SCOPE определяет, какие области ядра разрешено использовать для сопоставления.

Минимально:

- TERMS / NOMENCLATURE
- DISTINCTIONS
- FORMULATIONS
- CLASSIFICATIONS
- PASSPORTS
- RELATIONS
- CANON

## 4. CMOC как второй вход

RECONCILIATION имеет два источника входных данных:

```
DISCOVERY OUTPUT
      +
CMOC QUERY RESULT
      ↓
RECONCILIATION
```

CMOC QUERY RESULT не является новым source material и не должен подменять INPUT_RECORDS.

## 5. Минимальный запрос к ядру

Запрос должен быть построен вокруг объекта сопоставления.

Примеры:

```
MATCH TERM
MATCH DISTINCTION
MATCH FORMULATION
MATCH RELATION
MATCH PASSPORT
```

Запрос должен возвращать достаточно данных для:

- идентификации кандидата;
- сравнения объектной границы;
- сравнения статуса;
- определения lineage;
- последующей трассировки решения.

## 6. Результаты

Каждый входной кандидат получает один основной результат сопоставления:

### NEW

Эквивалент в доступном слое CMOC не найден.

### EXISTING_EQUIVALENT

В CMOC найден существующий объект с тем же объектным смыслом.

### EXISTING_RELATED

Найден связанный, но не эквивалентный объект.

### CONFLICT

Основания, определения, типы или отношения несовместимы.

### NEEDS_REVIEW

Автоматического основания для классификации недостаточно.

## 7. Output

Выход RECONCILIATION — набор Match/Decision Records.

Минимальный контракт записи:

```
MATCH_ID
SOURCE_ID
INPUT_BATCH_ID
INPUT_RECORD_ID
CMOC_OBJECT_ID / NULL
MATCH_RESULT
BASIS
STATUS
TRACEABILITY
```

CMOC_OBJECT_ID обязателен для EXISTING_EQUIVALENT / EXISTING_RELATED / CONFLICT, если объект найден.

## 8. Что машина может делать автоматически

RECONCILIATION может:

- искать кандидатов;
- сравнивать записи;
- выявлять вероятные дубликаты;
- группировать эквивалентные кандидаты;
- фиксировать RELATED;
- фиксировать CONFLICT;
- направлять неопределённое в NEEDS_REVIEW;
- готовить предложения по индексации.

## 9. Что запрещено без отдельного решения

RECONCILIATION не должна:

- удалять исторические Discovery Records;
- переписывать исходный результат;
- автоматически разрешать CONFLICT;
- автоматически повышать PROVISIONAL → CANONICAL;
- скрывать отсутствие CMOC evidence;
- считать отсутствие найденного объекта доказательством NEW без проверки заданного query scope.

## 10. Batch

Каждый запуск RECONCILIATION получает собственный BATCH_ID.

Повторное сопоставление того же входа после изменения ядра или правил — новый Batch.

## 11. Traceability

Минимальная цепочка:

```
SOURCE_ID
→ DISCOVERY BATCH
→ INPUT_RECORD
→ RECONCILIATION BATCH
→ CMOC QUERY
→ MATCH / DECISION
→ CORE ACTION
```

## 12. Положительный и отрицательный исход

RECONCILIATION может завершиться ACCEPT даже при наличии отдельных NEEDS_REVIEW/CONFLICT записей, если сам production contract выполнен.

Поэтому:

**результат отдельной записи ≠ статус всего production pass.**

## 13. Evidence boundary

TASK-CONTRACT-002 является проектным контрактом второй части архитектуры.

RECONCILIATION runtime, CMOC query interface и контрольные прогоны ещё не подтверждены.
