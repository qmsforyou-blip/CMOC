# WORK-PLAN — DISCOVERY / RECONCILIATION Boundary

**ID:** WORK-PLAN-DISCOVERY-RECONCILIATION-001  
**Дата:** 20-09-2026  
**Статус:** A6 CLOSED  
**Область:** CMOC / MACHINE-SOURCE-001 / SUPERAGENT  
**Основание:** STD-008 v0.8 + OBJECT INDEX / QUERY / RECONCILIATION architecture

---

## 1. Цель

Формально разделить два режима работы:

`DISCOVERY` — независимая добыча инженерного знания из SOURCE.

`RECONCILIATION` — сопоставление уже добытого результата с накопленным CMOC.

Главный принцип:

> **Сначала добываем. Потом сопоставляем.**

---

## 2. Архитектурная граница

### MODE A — DISCOVERY

```
SOURCE
  ↓
SOURCE_PACKAGE
  ↓
M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
  ↓
DISCOVERY RESULT
```

DISCOVERY отвечает только на вопрос:

> **Что здесь есть?**

DISCOVERY НЕ использует CMOC для изменения результата добычи.

В частности, DISCOVERY не должен:

- обращаться к OBJECT INDEX для изменения добываемого результата;
- выполнять QUERY;
- определять EQUIVALENT относительно CMOC;
- определять RELATED относительно CMOC;
- определять CONFLICT относительно CMOC;
- подменять source evidence накопленным знанием;
- удалять или изменять результат из-за того, что аналог уже существует в CMOC.

### MODE B — RECONCILIATION

```
DISCOVERY RESULT
       ↓
RECONCILIATION
       ↓
CMOC / OBJECT INDEX / QUERY
       ↓
NEW / EQUIVALENT / RELATED / CONFLICT / REVIEW
```

RECONCILIATION отвечает только на вопрос:

> **Что из добытого уже известно в CMOC и как новый результат соотносится с накопленным?**

RECONCILIATION не переписывает исходный DISCOVERY RESULT.

---

## 3. Особое правило M08

M08 относится к DISCOVERY.

```
M07
 ↓
M08
 ↓
source-bound decision
 ↓
DISCOVERY RESULT
```

M08 НЕ является RECONCILIATION.

M08 может принимать решение о степени основания объекта/отношения на основании SOURCE, PASSPORT и предусмотренного source-bound evidence.

M08 не должен использовать:

- CMOC;
- OBJECT INDEX;
- QUERY;
- существующие CMOC objects;
- накопленные ранее результаты как основание для изменения текущего SOURCE-result.

---

## 4. Неизменяемость границы

Результат DISCOVERY является входом RECONCILIATION как отдельный объект результата.

Допустимая схема:

```
SOURCE
  ↓
DISCOVERY
  ↓
RESULT-A
  ↓
RECONCILIATION
  ↓
RESULT-B
```

Недопустимая схема:

```
SOURCE
  ↓
DISCOVERY
  ↓
CMOC lookup
  ↓
изменение RESULT-A
```

RECONCILIATION может добавить собственные поля/решения сопоставления, но не должен молча переписывать source-derived records.

---

## 5. Текущий launcher

`05 SUPERAGENT/run_automated_m01_m08_src002.py`

на текущем этапе трактуется как:

> **контрольный production runner режима DISCOVERY для SRC-002.**

Он не является RECONCILIATION runner.

Его задача:

```
SOURCE_PACKAGE
 → M01
 → M02
 → M03
 → M04
 → M05
 → M06
 → M07
 → M08
 → DISCOVERY RESULT
```

---

## 6. План работ

### Этап A1 — Разбор launcher

Проверить `run_automated_m01_m08_src002.py` по каждому элементу:

- SOURCE;
- SOURCE_PACKAGE;
- initial input;
- M01–M08;
- HANDOFF;
- BATCH;
- wrappers;
- QC;
- post-run control;
- audit output.

Для каждого элемента определить:

`DISCOVERY / RECONCILIATION / SHARED INFRASTRUCTURE`.

**STOP-GATE A1:** ни один элемент DISCOVERY launcher не должен зависеть от CMOC для изменения добываемого результата.

---

### Этап A2 — Формализация интерфейса DISCOVERY

Определить минимальный контракт:

```
SOURCE_PACKAGE
      ↓
MACHINE-SOURCE-001
      ↓
DISCOVERY_RESULT
```

Зафиксировать:

- input;
- output;
- traceability;
- status;
- batch lineage;
- границу ответственности.

**STOP-GATE A2:** результат DISCOVERY самодостаточен для передачи в RECONCILIATION и не требует обратного обращения к CMOC.

---

### Этап A3 — Формализация интерфейса RECONCILIATION

Определить:

```
DISCOVERY_RESULT
       +
CMOC / OBJECT INDEX
       ↓
RECONCILIATION
       ↓
RECONCILIATION_RESULT
```

Проверить существующие:

- OBJECT INDEX;
- QUERY;
- reconciliation.py;
- статусы MATCH / NO_MATCH / CANDIDATE / AMBIGUOUS / SCOPE_INSUFFICIENT;
- переходы к NEW / EQUIVALENT / RELATED / CONFLICT / REVIEW.

**STOP-GATE A3:** RECONCILIATION получает готовый результат и не участвует в его добыче.

---

### Этап A4 — Negative controls

Обязательно проверить:

1. CMOC содержит эквивалентный объект → DISCOVERY RESULT не меняется.
2. CMOC содержит похожий объект → DISCOVERY RESULT не меняется.
3. CMOC содержит конфликтующую информацию → DISCOVERY RESULT не меняется.
4. QUERY недоступен → DISCOVERY всё равно способен завершить source-bound pass.
5. RECONCILIATION получает неполный/неоднозначный результат → не переписывает DISCOVERY.

---

### Этап A5 — Новый SOURCE

Только после закрытия A1–A4.

Новый SOURCE используется для проверки:

```
SOURCE-NEW
   ↓
DISCOVERY
   ↓
DISCOVERY RESULT
   ↓
RECONCILIATION
```

При этом отдельно оцениваются:

- воспроизводимость DISCOVERY;
- независимость от CMOC;
- корректность RECONCILIATION;
- отсутствие обратной семантической утечки.

---

### Этап A6 — Документирование

После прохождения контрольных точек:

1. обновить соответствующий TASK/runner contract;
2. при необходимости внести controlled edit в STD-008;
3. создать evidence;
4. зафиксировать negative controls;
5. только после этого считать границу DISCOVERY / RECONCILIATION доказанной.

---

## 7. Запреты на всём этапе

До закрытия этого Work Plan:

- не подключать CMOC к M01–M08;
- не добавлять QUERY внутрь MACHINE-SOURCE-001;
- не делать RECONCILIATION частью M08;
- не менять source-derived результат из-за найденного эквивалента;
- не считать совпадение термина доказательством эквивалентности;
- не смешивать DISCOVERY evidence и RECONCILIATION evidence;
- не объявлять новую SOURCE проверкой воспроизводимости до формализации интерфейса.

---

## 8. Definition of Done

Work Plan считается закрытым, когда:

- [x] A1 launcher размечен по границе A/B;
- [x] A2 DISCOVERY interface зафиксирован;
- [x] A3 RECONCILIATION interface зафиксирован;
- [x] M08 явно отнесён к DISCOVERY;
- [x] OBJECT INDEX / QUERY остаются за границей DISCOVERY;
- [x] DISCOVERY RESULT определён как отдельный immutable input для RECONCILIATION;
- [x] выполнены negative controls;
- [x] проведён тест на новом SOURCE;
- [x] создано evidence;
- [x] STD-008 и связанные контракты синхронизированы при необходимости.

---

## 9. A4 Closure

A4 закрыт после прохождения всех пяти negative controls и создания сводного evidence:\n\n`05 SUPERAGENT/EVIDENCE-A4-RECONCILIATION-DISCOVERY-ISOLATION-001.md`\n\nРезультаты: A4.1 PASS, A4.2 PASS, A4.3 PASS, A4.4 PASS, A4.5 PASS.\n\nA4 доказывает downstream isolation границы DISCOVERY → RECONCILIATION. A4.3 не доказывает conflict detection/resolution. A4.4 является controlled orchestration test, а не новым LLM production run.\n\n**STOP-GATE A4: CLOSED**\n\n**STOP-GATE A6: CLOSED**

A6 закрыт после controlled update STD-008 v0.9, DISCOVERY-RESULT-CONTRACT-001 и RECONCILIATION-INPUT-CONTRACT-001.\n\n## 10. Рабочее правило проекта

> **Сначала добываем. Потом сопоставляем.**

Или в инженерной форме:

```
SOURCE
  ↓
DISCOVERY
  ↓
RESULT
  ↓
RECONCILIATION
  ↓
CMOC
```

Никакого обратного потока семантики из CMOC в DISCOVERY.


## 11. A6 Closure

A6 закрыт.

Синхронизированы:

- `STD-008 MACHINE-SOURCE-001` → v0.9;
- `DISCOVERY-RESULT-CONTRACT-001` → A6 SYNCHRONIZED;
- `RECONCILIATION-INPUT-CONTRACT-001` → A6 SYNCHRONIZED;
- `EVIDENCE-A5-NEW-SOURCE-001.md` → ACCEPTED.

Статусы контрактов намеренно остаются **CONTRACT CANDIDATE**. A6 не превращает их автоматически в финальные стандарты и не вводит новые правила `NEW`, `CONFLICT`, `RELATED` или `target_object_type mapping`.

**STOP-GATE A6: CLOSED**
