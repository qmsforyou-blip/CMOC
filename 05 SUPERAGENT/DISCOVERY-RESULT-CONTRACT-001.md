# DISCOVERY-RESULT-CONTRACT-001

**Дата:** 20-09-2026  
**Статус:** CONTRACT CANDIDATE — A6 SYNCHRONIZED  
**Область:** MACHINE-SOURCE-001 / SUPERAGENT  
**Основание:** WORK-PLAN-DISCOVERY-RECONCILIATION-001, A1–A5 + STD-008 v0.9

---

## 1. Назначение

Этот контракт формализует результат режима **DISCOVERY** и границу между:

```
MODE A — DISCOVERY
SOURCE_PACKAGE
      ↓
MACHINE-SOURCE-001
      ↓
M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
      ↓
DISCOVERY_RESULT
```

и:

```
MODE B — RECONCILIATION
DISCOVERY_RESULT
      ↓
RECONCILIATION INPUT
      +
CMOC / OBJECT INDEX / QUERY
      ↓
RECONCILIATION_RESULT
```

Главное правило:

> **Сначала добываем. Потом сопоставляем.**

---

## 2. Определение

**DISCOVERY_RESULT** — отдельный агрегированный результат конкретного прохода MACHINE-SOURCE-001 по конкретному SOURCE_PACKAGE.

DISCOVERY_RESULT не является новым объектом CMOC и не является вторым CMOC.

Он фиксирует:

- идентичность прохода;
- источник и SOURCE_PACKAGE;
- результат исполнения M01–M08;
- batch lineage;
- traceability;
- границу происхождения результата;
- факт, что RECONCILIATION ещё не выполнялась.

---

## 3. Источник происхождения

DISCOVERY_RESULT имеет source-bound происхождение:

```
knowledge_origin = SOURCE_BOUND
```

Все содержательные записи DISCOVERY должны быть трассируемы к SOURCE_PACKAGE через цепочку:

```
SOURCE_ID
  ↓
SOURCE_PACKAGE
  ↓
RUN_ID
  ↓
BATCH_ID
  ↓
MACHINE_ID
  ↓
OUTPUT
```

Накопленное знание CMOC не является источником изменения DISCOVERY_RESULT.

---

## 4. Минимальная структура

Концептуальная форма:

```yaml
discovery_result:
  discovery_id:
  source_id:
  source_package_id:
  run_id:

  status:

  outputs:
    M01:
      ref:
      batch_id:
    M02:
      ref:
      batch_id:
    M03:
      ref:
      batch_id:
    M04:
      ref:
      batch_id:
    M05:
      ref:
      batch_id:
    M06:
      ref:
      batch_id:
    M07:
      ref:
      batch_id:
    M08:
      ref:
      batch_id:

  traceability:
    source_id:
    source_package_id:
    run_id:

  boundary:
    origin: SOURCE_BOUND
    reconciliation: NOT_PERFORMED
```

Конкретная физическая реализация может использовать существующие output-файлы/records M01–M08 вместо их дублирования внутри агрегатора.

---

## 5. Outputs M01–M08

DISCOVERY_RESULT должен позволять адресовать результаты каждой машины:

```
M01 → EXTRACTION_RECORDS
M02 → DISTINCTION_RECORDS
M03 → FORMULATION_RECORDS
M04 → NOMENCLATURE_CANDIDATES
M05 → CLASSIFICATION_RECORDS
M06 → PASSPORT_RECORDS
M07 → RELATION_CANDIDATES
M08 → DECISION_RECORDS
```

DISCOVERY_RESULT не заменяет эти outputs.

Он агрегирует их адресацию и lineage.

---

## 6. Traceability

Для каждого output должна сохраняться возможность установить:

- source_id;
- source_package_id;
- run_id;
- batch_id;
- machine_id;
- upstream reference;
- source location или basis references, если они предусмотрены соответствующей машиной.

Правило:

> Если происхождение записи нельзя проследить до SOURCE_PACKAGE, запись не может считаться полноценно трассируемой частью DISCOVERY_RESULT.

---

## 7. Status

DISCOVERY_RESULT фиксирует статус выполнения Discovery-прохода.

Статус не заменяет:

- SOURCE_PACKAGE status;
- BATCH status;
- HANDOFF status;
- semantic status отдельной записи.

Новые словари статусов без отдельного контракта не вводятся.

---

## 8. Boundary declaration

DISCOVERY_RESULT должен явно фиксировать:

```yaml
boundary:
  origin: SOURCE_BOUND
  reconciliation: NOT_PERFORMED
```

Смысл:

> результат получен из SOURCE_PACKAGE и его внутренних source-supported преобразований; сопоставление с накопленным CMOC ещё не выполнялось.

---

## 9. Immutable boundary

После формирования DISCOVERY_RESULT он передаётся в RECONCILIATION как read-only вход.

Допустимая схема:

```
SOURCE
  ↓
DISCOVERY
  ↓
DISCOVERY_RESULT
  ↓
RECONCILIATION
  ↓
RECONCILIATION_RESULT
```

Недопустимая схема:

```
SOURCE
  ↓
DISCOVERY
  ↓
CMOC lookup
  ↓
изменение DISCOVERY_RESULT
```

RECONCILIATION может создать собственный результат сопоставления, но не должен молча переписывать source-derived records.

---

## 10. Запрет обратного семантического потока

Следующее запрещено:

```
CMOC
  ↓
QUERY
  ↓
изменение
  ↓
DISCOVERY_RESULT
```

CMOC может участвовать в определении результата RECONCILIATION, но не в изменении результата добычи.

---

## 11. RECONCILIATION INPUT

Для передачи в существующий слой RECONCILIATION допускается отдельное представление выбранных Discovery records.

Минимальный интерфейс записи для downstream RECONCILIATION:

```yaml
record_id:
value:
traceability:
```

`target_object_type` не входит в обязательный минимальный интерфейс. Он может присутствовать только при наличии отдельного явно определённого mapping-контракта.

Это представление является **адаптацией адресации**, а не новой добычей или новой семантической интерпретацией.

Адаптер не имеет права добавлять:

- CMOC object id;
- equivalence;
- relation-to-existing-object;
- conflict;
- NEW;
- reconciliation decision.

---

## 12. Граница ответственности

### MACHINE-SOURCE-001

Отвечает за:

- работу с SOURCE_PACKAGE;
- M01–M08;
- source-bound semantic processing;
- source traceability;
- DISCOVERY_RESULT.

Не отвечает за:

- поиск существующих объектов CMOC;
- QUERY;
- OBJECT INDEX;
- equivalence;
- conflict;
- reconciliation decision.

### RECONCILIATION

Получает готовый DISCOVERY_RESULT и сопоставляет его с накопленным знанием через предусмотренные OBJECT INDEX / QUERY механизмы.

RECONCILIATION не участвует в добыче исходного результата.

---

## 13. M08

M08 остаётся частью DISCOVERY.

M08 может принимать source-bound decision на основании:

- SOURCE;
- PASSPORT;
- relation candidates;
- source-supported evidence.

M08 не получает:

- CMOC;
- OBJECT INDEX;
- QUERY;
- existing CMOC objects.

Следовательно:

> M08 decision ≠ RECONCILIATION decision.

---

## 14. Shared infrastructure

Следующие элементы не относятся семантически ни к A, ни к B:

- Contract;
- Batch;
- Handoff;
- Journal;
- QC;
- traceability runtime;
- run_chain;
- machine_id.

Они являются общей инфраструктурой исполнения.

---

## 15. Negative controls

Контракт должен выдерживать следующие проверки:

1. В CMOC существует эквивалент → DISCOVERY_RESULT не изменяется.
2. В CMOC существует похожий объект → DISCOVERY_RESULT не изменяется.
3. В CMOC существует конфликтующая информация → DISCOVERY_RESULT не изменяется.
4. QUERY недоступен → source-bound Discovery не зависит от QUERY.
5. RECONCILIATION получает неполный/неоднозначный Discovery result → исходные Discovery records не переписываются.

---

## 16. Связь с существующими компонентами

```
mvp_runner.py
    = SHARED EXECUTION RUNTIME

MACHINE-SOURCE-001
    = DISCOVERY

DISCOVERY_RESULT
    = A → B INTERFACE

cmoc_object_index.json
    = OBJECT INDEX

cmoc_query.py
    = QUERY

reconciliation.py
    = RECONCILIATION
```

OBJECT INDEX и QUERY находятся за границей Discovery.

---

## 17. Главный инвариант

> **DISCOVERY_RESULT может быть прочитан RECONCILIATION, но не может быть изменён RECONCILIATION.**

И:

> **CMOC может влиять на результат сопоставления, но не может влиять на результат добычи.**

---

## 18. Статус после A5

A2 считается контрактно определённым, если:

- [x] определён DISCOVERY_RESULT;
- [x] определена source-bound природа;
- [x] определена traceability;
- [x] определена batch lineage;
- [x] определены outputs M01–M08;
- [x] определена immutable boundary;
- [x] определён минимальный RECONCILIATION INPUT;
- [x] зафиксировано отсутствие обратного семантического потока;
- [x] M08 явно отнесён к DISCOVERY;
- [x] shared infrastructure отделена от семантических режимов.

A2 подтверждён контрактно.

A5 дополнительно подтвердил контракт на новом SOURCE SRC-003:

- production M01–M08 выполнен;
- DISCOVERY_RESULT сформирован отдельно;
- DISCOVERY_RESULT передан в downstream RECONCILIATION;
- исходный Discovery Result не изменён;
- OBJECT INDEX не изменён;
- CMOC write отсутствует.

Контракт не расширяется результатами A5 за пределы уже определённой границы.

---

## 19. Рабочее правило

```
SOURCE
  ↓
DISCOVERY
  ↓
DISCOVERY_RESULT
  ↓
RECONCILIATION
  ↓
CMOC
```

> **Сначала добываем. Потом сопоставляем.**
