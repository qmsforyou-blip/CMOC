# EVIDENCE — A5 NEW SOURCE

**ID:** EVIDENCE-A5-NEW-SOURCE-001  
**Дата:** 20-09-2026  
**Статус:** ACCEPTED  
**Область:** CMOC / MACHINE-SOURCE-001 / SUPERAGENT  
**Основание:** WORK-PLAN-A5-NEW-SOURCE-001 / A4 CLOSED

---

## 1. Цель

Зафиксировать контролируемый проход нового SOURCE через:

```
SOURCE
  ↓
SOURCE_PACKAGE
  ↓
M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
  ↓
DISCOVERY_RESULT
  ↓
RECONCILIATION_INPUT
  ↓
RECONCILIATION
  ↓
CMOC / OBJECT INDEX / QUERY
```

Основное проверяемое правило:

> **Сначала добываем. Потом сопоставляем.**

---

## 2. SOURCE identity

- **SOURCE_ID:** SRC-003
- **SOURCE_NAME:** ISO/DIS 9001:2025 — Quality management systems — Requirements
- **SOURCE_TYPE:** PDF
- **SOURCE_VERSION:** ISO/DIS 9001:2025(en), sixth edition, draft
- **SOURCE_PACKAGE_ID:** SOURCE-003-PACKAGE-001-CONTROLLED-5-6
- **SOURCE_PACKAGE_STATUS:** PARTIAL
- **WORK_SCOPE:** pages 5-6 of 50

SOURCE_PACKAGE содержит только контролируемый scope p5-p6. Предыдущие результаты ISO-добычи не использовались как вход нового Discovery pass.

---

## 3. Discovery production run

- **RUN_ID:** RUN-SRC-003-AUTOMATED-M01-M08-001
- **TASK SEQUENCE:** M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
- **HANDOFFS:** 7/7 ACCEPT
- **DISCOVERY MODE:** production
- **CMOC ACCESS:** NONE
- **QUERY ACCESS:** NONE

### Record counts

| Machine | Output | Records |
|---|---|---:|
| M01 | EXTRACTION_RECORDS | 16 |
| M02 | DISTINCTION_RECORDS | 16 |
| M03 | FORMULATION_RECORDS | 48 |
| M04 | NOMENCLATURE_CANDIDATES | 16 |
| M05 | CLASSIFICATION_RECORDS | 16 |
| M06 | PASSPORT_RECORDS | 16 |
| M07 | RELATION_CANDIDATES | 1 |
| M08 | DECISION_RECORDS | 0 |

M07 прошёл контролируемую ветку **NO_RELATION** при отсутствии relation evidence. M08 не создал DECISION_RECORDS.

---

## 4. Discovery Result

Фиксированный результат:

- **DISCOVERY_RESULT:** DISCOVERY-RESULT-SRC-003-M06-001.json
- **M06 BATCH:** BATCH-SRC-003-M06-006
- **PASSPORT_RECORDS:** 16

Все паспорта являются source-bound и сохраняют source basis и traceability.

Discovery Result рассматривается как отдельный вход следующего режима и не переписывается Reconciliation.

---

## 5. A5.3 downstream Reconciliation

Вход:

- SOURCE_ID: SRC-003
- DISCOVERY RUN: RUN-SRC-003-AUTOMATED-M01-M08-001
- M06 BATCH: BATCH-SRC-003-M06-006
- INPUT RECORDS: 16
- QUERY_SCOPE: TERMS
- TARGET_OBJECT_TYPE INFERENCE: NONE

Результат:

```
EXISTING_EQUIVALENT = 0
NEEDS_REVIEW        = 16
NEW                 = 0
```

Все 16 записей получили:

```
NO_MATCH from configured query modes; NEW not yet proven
```

Это не означает, что объекты доказанно NEW. Текущая реализация сохраняет NO_MATCH как NEEDS_REVIEW.

---

## 6. Boundary controls

A5.3 runner подтвердил:

- DISCOVERY_RESULT memory mutation: NONE
- DISCOVERY_RESULT file mutation: NONE
- OBJECT INDEX file mutation: NONE
- CMOC write: NONE
- QUERY downstream only: TRUE
- NO_MATCH → NEW: FALSE
- working_class → target_object_type mapping: NOT PERFORMED

Хэши DISCOVERY_RESULT и OBJECT INDEX до/после Reconciliation совпали.

---

## 7. Traceability

Контролируемая цепочка:

```
SRC-003
  ↓
SOURCE-003-PACKAGE-001-CONTROLLED-5-6
  ↓
RUN-SRC-003-AUTOMATED-M01-M08-001
  ↓
BATCH-SRC-003-M06-006
  ↓
PAS-001 … PAS-016
  ↓
MAT-PAS-001 … MAT-PAS-016
```

Traceability сохраняется в Reconciliation result.

---

## 8. Architectural conclusion

A5 подтвердил на новом SOURCE разделение:

```
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
CMOC / OBJECT INDEX / QUERY
```

CMOC/QUERY не использовались для изменения Discovery.

Reconciliation не изменяет source-derived Discovery Result.

M08 остаётся частью DISCOVERY и не является Reconciliation.

---

## 9. Limitations

Эксперимент не доказывает:

- семантическую полноту Discovery;
- автоматическое определение NEW;
- автоматическое разрешение CONFLICT;
- автоматическое установление RELATED;
- полноту CMOC QUERY;
- distributed execution;
- failure recovery;
- автоматическую канонизацию;
- воспроизводимость на полном тексте ISO/DIS 9001:2025.

Scope SOURCE_PACKAGE ограничен страницами 5-6 из 50.

---

## 10. A5 status

### A5.1 — SOURCE isolation
**PASS**

### A5.2 — full M01-M08 production pass
**PASS**

### A5.3 — downstream Reconciliation
**PASS**

### A5.4 — Evidence
**PASS**

### Overall A5
**READY FOR WORK-PLAN CLOSURE**

---

## 11. Working rule

> **Сначала добываем. Потом сопоставляем.**

```
DISCOVERY производит source-bound результат.
RECONCILIATION устанавливает его отношение к накопленному CMOC.
```
