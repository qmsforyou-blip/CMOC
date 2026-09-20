# RECONCILIATION-INPUT-CONTRACT-001 — Интерфейс входа из DISCOVERY в RECONCILIATION

**Версия:** 0.1  
**Дата:** 20-09-2026  
**Статус:** CONTRACT CANDIDATE  
**Область:** MACHINE-SOURCE-001 → RECONCILIATION  
**Основание:** A2 DISCOVERY RESULT contract + A3-GATE по production M06 SRC-002

---

## 1. Назначение

Этот контракт формализует границу между:

**MODE A — DISCOVERY**

~~~
SOURCE
  ↓
SOURCE_PACKAGE
  ↓
M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
  ↓
DISCOVERY_RESULT
~~~

и

**MODE B — RECONCILIATION**

~~~
DISCOVERY_RESULT
  ↓
RECONCILIATION_INPUT
  ↓
RECONCILIATION
  ↓
CMOC / OBJECT INDEX / QUERY
  ↓
RECONCILIATION_RESULT
~~~

Главное правило:

> **Сначала добываем. Потом сопоставляем.**

RECONCILIATION-INPUT является адаптированным входом для сопоставления уже добытых source-bound кандидатов с существующим CMOC.

---

## 2. Что является входом

Первичная партия для object reconciliation формируется из:

~~~
M06 PASSPORT_RECORDS
~~~

M06 является первой точкой, где результат Discovery оформлен как source-bound паспорт кандидата объекта.

M01–M05 не передаются как самостоятельные объекты сопоставления в первом варианте интерфейса. Их идентификаторы и ссылки на доказательную цепочку сохраняются в traceability.

M07 RELATION_CANDIDATES и M08 DECISION_RECORDS не входят в этот интерфейс.

Для отношений предусматривается отдельный будущий интерфейс.

---

## 3. Минимальная структура RECONCILIATION_INPUT

~~~yaml
reconciliation_input:
  source_id:
  input_batch_id:
  input_output_type: PASSPORT_RECORDS

  records:
    - record_id:
      value:
      traceability:

  query_scope:
~~~

### Обязательные поля верхнего уровня

- source_id
- input_batch_id
- input_output_type
- records
- query_scope

### Обязательные поля записи

- record_id
- value
- traceability

---

## 4. Отображение PASSPORT → RECONCILIATION_INPUT

Production M06 SRC-002 подтвердил следующую адресацию.

| PASSPORT field | RECONCILIATION field | Правило |
|---|---|---|
| id | record_id | Прямая передача |
| term | value | Прямая передача |
| source_id | верхний source_id / traceability | Прямая передача |
| M06 batch_id | input_batch_id | Идентификатор партии M06 |
| source_basis | traceability | Сохраняется как upstream basis |
| candidate_id | traceability | Сохраняется как upstream reference |
| classification_id | traceability | Сохраняется как upstream reference |
| object_boundary | traceability | Сохраняется как source-bound boundary |
| working_class | target_object_type | **НЕ отображается автоматически** |
| lifecycle_status | — | Не используется как query semantic |
| epistemic_status | — | Не используется как query semantic |
| evidence_gap | — | Не преобразуется автоматически в query instruction |

---

## 5. Правило для value

value берётся только из:

~~~
PASSPORT.term
~~~

Не допускается автоматически строить value из:

- object_boundary;
- source_basis;
- working_class;
- formulation;
- distinction;
- classification description;
- внешнего знания.

Таким образом:

~~~
PAS-006.term
"Fast Response"
      ↓
RECONCILIATION.value
"Fast Response"
~~~

---

## 6. Правило target_object_type

target_object_type **не является обязательным полем записи первого варианта интерфейса**.

Критическое ограничение:

> **working_class из M05/M06 не является автоматически target_object_type CMOC.**

Например:

~~~
working_class = STRATEGY
        ≠
автоматически CMOC object_type
~~~

Причина: M05/M06 классифицируют source-bound результат Discovery, а OBJECT INDEX использует собственную систему типов адресуемых объектов.

Любое отображение:

~~~
working_class → CMOC object_type
~~~

может быть введено только отдельным явно определённым mapping-контрактом.

До появления такого контракта target_object_type отсутствует.

---

## 7. Query scope

query_scope задаётся на стороне RECONCILIATION.

DISCOVERY и адаптер не имеют права выводить query_scope из:

- working_class;
- term;
- object_boundary;
- сходства с существующими CMOC объектами.

query_scope является параметром запроса и не является результатом Discovery.

Если необходимый scope не покрыт OBJECT INDEX / QUERY, результатом Reconciliation может быть:

~~~
SCOPE_INSUFFICIENT
~~~

а затем:

~~~
NEEDS_REVIEW
~~~

---

## 8. Traceability

Каждая запись RECONCILIATION_INPUT должна сохранять путь:

~~~
SOURCE_ID
   ↓
SOURCE_PACKAGE
   ↓
DISCOVERY RUN
   ↓
M06 BATCH
   ↓
PASSPORT
   ↓
RECONCILIATION_INPUT RECORD
~~~

Минимальный пример:

~~~yaml
traceability:
  source_id: SRC-002
  source_package: SOURCE-002-PACKAGE-001-CONTROLLED-1-6
  discovery_run: RUN-SRC-002-AUTOMATED-M01-M08-001
  batch_id: BATCH-SRC-002-M06-006
  passport_id: PAS-006
  candidate_id: NOM-006
  classification_id: CLS-006
  source_basis:
    - FORM-016
    - FORM-017
    - FORM-018
  object_boundary: "source-bound ..."
~~~

Traceability является адресной информацией.

Она не должна использоваться как скрытый механизм семантического вывода.

---

## 9. Неизменяемость Discovery

После формирования RECONCILIATION_INPUT:

~~~
DISCOVERY_RESULT
      ↓
RECONCILIATION_INPUT
      ↓
RECONCILIATION
~~~

RECONCILIATION не имеет права изменять:

- M01–M08 outputs;
- M06 PASSPORT_RECORD;
- DISCOVERY_RESULT;
- source evidence;
- source-bound object boundary.

Если обнаружено соответствие с CMOC, это создаёт результат Reconciliation, а не переписывает Discovery.

---

## 10. Что Reconciliation может установить

QUERY возвращает только предусмотренные его контрактом результаты:

- MATCH
- NO_MATCH
- CANDIDATE
- AMBIGUOUS
- SCOPE_INSUFFICIENT

На их основании текущий слой Reconciliation формирует, в частности:

- EXISTING_EQUIVALENT
- NEEDS_REVIEW

### Важное ограничение

NO_MATCH **не означает автоматически NEW**.

Текущая реализация Reconciliation сохраняет отсутствие доказанного соответствия как NEEDS_REVIEW.

Решение о NEW требует отдельного правила и отдельного контракта.

---

## 11. Что запрещено

RECONCILIATION-INPUT adapter не имеет права:

1. обращаться к CMOC для формирования Discovery результата;
2. обращаться к OBJECT INDEX для изменения паспорта;
3. обращаться к QUERY до формирования входа;
4. выводить эквивалентность;
5. выводить отношение;
6. выводить конфликт;
7. объявлять объект NEW;
8. превращать совпадение терма в эквивалентность;
9. выводить target_object_type из working_class;
10. изменять source-bound object_boundary;
11. объединять M07/M08 с object reconciliation.

---

## 12. M07 и M08

Этот контракт **не принимает**:

~~~
RELATION_CANDIDATES
DECISION_RECORDS
~~~

Причина:

~~~
M06 PASSPORTS
   ↓
M07 RELATIONS
   ↓
M08 DECISION
~~~

является отдельной source-bound ветвью Discovery.

Для последующего сопоставления отношений с CMOC должен быть разработан отдельный контракт.

---

## 13. Production example — SRC-002

Для production M06 SRC-002 подтверждена партия:

~~~
BATCH-SRC-002-M06-006
type = PASSPORT_RECORDS
records = 7
~~~

В ней присутствуют PAS-001 … PAS-007.

Пример:

~~~yaml
record_id: PAS-006
value: "Fast Response"

traceability:
  source_id: SRC-002
  source_package: SOURCE-002-PACKAGE-001-CONTROLLED-1-6
  discovery_run: RUN-SRC-002-AUTOMATED-M01-M08-001
  batch_id: BATCH-SRC-002-M06-006
  passport_id: PAS-006
  candidate_id: NOM-006
  classification_id: CLS-006
  source_basis:
    - FORM-016
    - FORM-017
    - FORM-018
~~~

При этом:

~~~
working_class = STRATEGY
~~~

не преобразуется автоматически в target_object_type.

---

## 14. Ответственность компонентов

### MACHINE-SOURCE-001

Отвечает за:

~~~
SOURCE → DISCOVERY_RESULT
~~~

и производит source-bound PASSPORT_RECORDS.

### RECONCILIATION INPUT ADAPTER

Отвечает только за:

~~~
PASSPORT_RECORDS
      ↓
RECONCILIATION_INPUT
~~~

Без семантического обогащения.

### RECONCILIATION

Отвечает за:

~~~
RECONCILIATION_INPUT
      ↓
QUERY
      ↓
RECONCILIATION_RESULT
~~~

### CMOC / OBJECT INDEX / QUERY

Отвечают за сопоставление с уже накопленным CMOC.

---

## 15. Negative controls

Контракт должен сохранять следующие проверки.

### NC-01 — существующий эквивалент

Если CMOC содержит соответствующий объект:

~~~
DISCOVERY_RESULT
~~~

не изменяется.

Меняется только:

~~~
RECONCILIATION_RESULT
~~~

### NC-02 — похожий объект

Структурный/кандидатный результат QUERY не превращается автоматически в эквивалентность.

### NC-03 — отсутствие QUERY

Если QUERY недоступен:

~~~
DISCOVERY
~~~

всё равно считается независимым от Reconciliation.

### NC-04 — неоднозначность

~~~
AMBIGUOUS
~~~

не изменяет паспорт и приводит к review.

### NC-05 — scope insufficient

~~~
SCOPE_INSUFFICIENT
~~~

не изменяет Discovery и не превращается в NEW.

### NC-06 — missing target type

Отсутствие target_object_type не считается ошибкой Discovery.

Это нормальное состояние первого варианта интерфейса.

---

## 16. Boundary invariant

Основной инвариант:

~~~
SOURCE
  ↓
DISCOVERY
  ↓
DISCOVERY_RESULT
  ↓
RECONCILIATION_INPUT
  ↓
RECONCILIATION
  ↓
CMOC
~~~

Обратный семантический поток запрещён:

~~~
CMOC
  X
  ↓
DISCOVERY
~~~

CMOC может влиять только на результат Reconciliation.

---

## 17. Статус контракта

**CONTRACT CANDIDATE**

A3-GATE завершён на production данных SRC-002.

Следующий шаг:

**A3-IMPLEMENTATION GATE** — реализовать минимальный read-only adapter и проверить его на 7 production PASSPORT_RECORDS без запуска QUERY.

До прохождения этого gate:

- M01–M08 не изменять;
- OBJECT INDEX не изменять;
- QUERY не изменять;
- reconciliation.py не изменять;
- новую семантику target_object_type не вводить.

---

## 18. Рабочее правило

> **Сначала добываем. Потом сопоставляем.**

> **Discovery производит source-bound кандидата. Reconciliation устанавливает его отношение к уже существующему CMOC.**
