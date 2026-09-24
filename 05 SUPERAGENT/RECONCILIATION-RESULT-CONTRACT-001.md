# RECONCILIATION-RESULT-CONTRACT-001 — Контракт результата сопоставления

**Версия:** 0.1  
**Дата:** 24-09-2026  
**Статус:** CONTRACT CANDIDATE  
**Область:** RECONCILIATION → downstream review / decision  
**Основание:** RECONCILIATION-INPUT-CONTRACT-001 + A5 SRC-003 downstream validation

---

## 1. Назначение

Контракт формализует самостоятельный результат слоя RECONCILIATION.

```
RECONCILIATION_INPUT
        ↓
      QUERY
        ↓
RECONCILIATION_RESULT
```

RECONCILIATION_RESULT фиксирует только то, что установлено сопоставлением source-bound записи с уже существующим CMOC.

Он **не является решением о включении знания в CMOC**.

---

## 2. Разрешённые результаты v0.1

На уровне одной записи:

- `EXISTING_EQUIVALENT`
- `NEEDS_REVIEW`

Другие решения в этот контракт v0.1 не вводятся.

В частности, v0.1 не вводит:

- `NEW`
- `CONFLICT`
- `RELATED`
- `REJECT`
- автоматическое admission в CMOC.

---

## 3. Основная структура

```yaml
reconciliation_result:
  reconciliation_id:
  source_id:
  discovery_run:
  input_batch_id:
  input_output_type: PASSPORT_RECORDS
  query_scope:

  records:
    - match_id:
      source_id:
      input_batch_id:
      input_record_id:
      cmoc_object_id:
      match_result:
      basis:
      status: PROVISIONAL
      traceability:

  summary:
    total:
    existing_equivalent:
    needs_review:

  boundary:
    origin: RECONCILIATION
    discovery_mutation: NONE
    cmoc_write: NONE
    object_index_write: NONE
    admission_decision: NOT_PERFORMED
```

---

## 4. Идентичность результата

`reconciliation_id` идентифицирует конкретный результат сопоставления конкретной входной партии.

Минимальная lineage:

```
source_id
  ↓
discovery_run
  ↓
input_batch_id
  ↓
RECONCILIATION_RESULT
```

Идентичность должна быть детерминированной для одного и того же `source_id + discovery_run + input_batch_id`.

---

## 5. Запись результата

Минимальная запись:

```yaml
match_id:
source_id:
input_batch_id:
input_record_id:
cmoc_object_id:
match_result:
basis:
status: PROVISIONAL
traceability:
```

### Правила

**EXISTING_EQUIVALENT**

- `cmoc_object_id` должен быть указан;
- `basis` должен объяснять основание соответствия;
- `status = PROVISIONAL`.

**NEEDS_REVIEW**

- `cmoc_object_id` может быть `null`;
- если существует структурный кандидат, его идентификатор может сохраняться как кандидат;
- `basis` должен объяснять причину review;
- `status = PROVISIONAL`.

---

## 6. Ключевое ограничение NEW

```
NO_MATCH
   ≠
NEW
```

Если configured query modes не доказали существующий эквивалент:

```
match_result = NEEDS_REVIEW
```

Решение `NEW` требует отдельного правила и отдельного downstream-контракта.

---

## 7. Ключевое ограничение admission

```
EXISTING_EQUIVALENT
   ≠
CMOC ADMITTED
```

RECONCILIATION только устанавливает отношение source-bound записи к уже существующему CMOC.

Само наличие `EXISTING_EQUIVALENT` не разрешает запись, изменение или канонизацию объекта в CMOC.

---

## 8. Traceability

Traceability из RECONCILIATION_INPUT передаётся без потери lineage.

Минимальный путь:

```
SOURCE
  ↓
SOURCE_PACKAGE
  ↓
DISCOVERY RUN
  ↓
M06 BATCH
  ↓
PASSPORT
  ↓
RECONCILIATION_INPUT
  ↓
RECONCILIATION_RESULT
```

RECONCILIATION_RESULT не должен заменять upstream identifiers собственными идентификаторами.

---

## 9. Boundary

Контракт фиксирует:

```yaml
boundary:
  origin: RECONCILIATION
  discovery_mutation: NONE
  cmoc_write: NONE
  object_index_write: NONE
  admission_decision: NOT_PERFORMED
```

Это не описание будущего CMOC admission. Это явная фиксация границы текущего результата.

---

## 10. Aggregate summary

Для партии результат содержит только агрегаты, которые непосредственно следуют из record-level results:

```yaml
summary:
  total:
  existing_equivalent:
  needs_review:
```

Никаких новых semantic categories aggregate summary не создаёт.

---

## 11. Negative controls

Результат считается корректным только при соблюдении:

1. Discovery records не изменяются.
2. M06 PASSPORT_RECORDS не изменяются.
3. OBJECT INDEX не изменяется.
4. QUERY остаётся read-only.
5. `NO_MATCH` не преобразуется в `NEW`.
6. `NEEDS_REVIEW` не преобразуется в admission decision.
7. `EXISTING_EQUIVALENT` не выполняет CMOC write.
8. M07/M08 не включаются в object reconciliation result.

---

## 12. Что находится после RECONCILIATION_RESULT

Следующая цепочка намеренно остаётся за пределами v0.1:

```
RECONCILIATION_RESULT
        ↓
HUMAN REVIEW / отдельное DECISION
        ↓
NEW / EXISTING / REJECT / ...
        ↓
CMOC admission
```

Не следует вводить эти состояния в текущий контракт до отдельного архитектурного решения.

---

## 13. Production basis

Контракт опирается на уже выполненный A5.3 SRC-003 downstream run:

- 16 входных записей;
- 16 результатов `NEEDS_REVIEW`;
- `NO_MATCH` не превращён в `NEW`;
- Discovery и OBJECT INDEX остались неизменными;
- QUERY использован downstream от Discovery.

Таким образом, контракт не создаёт новую semantic capability, а фиксирует уже наблюдаемый результат существующего Reconciliation слоя.

---

## 14. Статус

**CONTRACT CANDIDATE — v0.1**

Следующий отдельный вопрос — что делать с `NEEDS_REVIEW`.

Этот контракт сам на него не отвечает.
