# R1 — QUERY → RECONCILIATION semantic control

**ID:** R1-QUERY-RECONCILIATION-SEMANTICS-001  
**Дата:** 20-09-2026  
**Статус:** TEST CANDIDATE  
**Область:** RECONCILIATION / QUERY  
**Основание:** A6 CLOSED

## 1. Цель

Проверить четыре управляемые ветви перехода от результата QUERY к текущему RECONCILIATION:

```
MATCH
NO_MATCH
CANDIDATE
AMBIGUOUS
```

Контроль выполняется без изменения DISCOVERY_RESULT и без записи в CMOC.

## 2. Контролируемые правила

| QUERY result | Current RECONCILIATION result |
|---|---|
| MATCH | EXISTING_EQUIVALENT |
| NO_MATCH | NEEDS_REVIEW |
| CANDIDATE | NEEDS_REVIEW |
| AMBIGUOUS | NEEDS_REVIEW |

Дополнительное правило:

`NO_MATCH ≠ NEW`.

`CANDIDATE ≠ EXISTING_EQUIVALENT`.

`AMBIGUOUS ≠ EXISTING_EQUIVALENT`.

## 3. Test fixture

Используется изолированный in-memory OBJECT INDEX fixture, содержащий:

- один canonical OBJECT_FILE для EXACT MATCH;
- отсутствие записи для NO_MATCH;
- один structural candidate;
- две non-canonical representations с одинаковым object_name для AMBIGUOUS.

Fixture не является изменением нормативного OBJECT INDEX.

## 4. Invariants

R1 не должен:

- изменять DISCOVERY_RESULT;
- изменять OBJECT INDEX;
- писать в CMOC;
- выводить NEW из NO_MATCH;
- выводить equivalence из CANDIDATE;
- выводить equivalence из AMBIGUOUS.

## 5. Expected result

```
MATCH      → EXISTING_EQUIVALENT
NO_MATCH   → NEEDS_REVIEW
CANDIDATE  → NEEDS_REVIEW
AMBIGUOUS  → NEEDS_REVIEW
```

Для CANDIDATE допускается сохранение `cmoc_object_id` как адреса candidate, но это не означает equivalence.

Для AMBIGUOUS `cmoc_object_id` должен отсутствовать.

## 6. Boundary

R1 проверяет только текущую семантику существующего `reconciliation.py`.

R1 НЕ вводит правила:

- NEW;
- RELATED;
- CONFLICT;
- target_object_type mapping;
- semantic similarity.

Следующий вопрос после R1: требуется ли отдельный контракт для перехода `NO_MATCH → NEW`, либо `NEEDS_REVIEW` остаётся конечным состоянием текущего reconciliation MVP.
