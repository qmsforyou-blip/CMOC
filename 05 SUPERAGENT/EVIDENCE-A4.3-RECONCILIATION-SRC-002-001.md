# EVIDENCE — A4.3 Conflicting CMOC Downstream Isolation

**ID:** EVIDENCE-A4.3-RECONCILIATION-SRC-002-001  
**Дата:** 20-09-2026  
**Статус:** ACCEPTED  
**Область:** WORK-PLAN-DISCOVERY-RECONCILIATION-001 / A4 Negative Controls

## 1. Цель

Проверить, что конфликтующая информация в CMOC не изменяет source-bound DISCOVERY RESULT.

Контроль использует production-derived M06 Passport fixture для SRC-002. В копию OBJECT INDEX добавлен синтетический TERM с тем же object_name, что и у PAS-006, и с дополнительным конфликтующим утверждением.

## 2. Контроль

Для PAS-006:

- Discovery value: `Fast Response visual management`
- synthetic CMOC object_id: `TEST-T-FR-CONFLICT-001`
- synthetic CMOC object_name: `Fast Response visual management`
- conflicting claim: `Fast Response is not visual management`

Конфликт помещён в `indexed_attributes` как отдельное поле. Текущий детерминированный RECONCILIATION использует для EXACT только object_id/object_name и не реализует отдельный механизм разрешения конфликтов.

## 3. Результат

Команда:

```powershell
py "05 SUPERAGENT/test_a4_3_conflicting_cmoc_downstream.py"
```

Результат:

```text
gate: A4.3-CONFLICTING-CMOC-DOWNSTREAM-ISOLATION
status: PASS
tested_passport: PAS-006
discovery_value: Fast Response visual management
synthetic_cmoc_object_id: TEST-T-FR-CONFLICT-001
conflicting_claim: Fast Response is not visual management
reconciliation_result: EXISTING_EQUIVALENT
reconciliation_basis: EXACT match
discovery_unchanged: true
original_index_unchanged: true
real_index_file_modified: NO
```

## 4. Что доказано

Контроль подтверждает архитектурную изоляцию:

```text
CMOC conflicting information
          ↓
RECONCILIATION
          ↓
DISCOVERY RESULT unchanged
```

Наличие конфликтующего поля в CMOC не изменяет source-bound Passport result.

## 5. Что НЕ доказано

Этот контроль не доказывает, что текущий RECONCILIATION умеет обнаруживать или разрешать семантический CONFLICT.

Фактически результат:

```text
EXISTING_EQUIVALENT / EXACT match
```

получен потому, что текущий EXACT QUERY проверяет object_name и не анализирует `indexed_attributes.conflicting_claim`.

Следовательно, A4.3 фиксирует только downstream isolation.

Отдельный механизм CONFLICT detection/resolution остаётся будущей задачей и не должен быть приписан текущему MVP.

## 6. Ограничение доказательства

Контроль не выполняет новый полный M01–M08 LLM-run.

Он использует production-derived M06 Passport fixture и проверяет downstream boundary на результате Discovery.

## 7. Gate

**A4.3 — PASS**

Следующий контроль: **A4.4 — QUERY недоступен → DISCOVERY должен оставаться способным завершить source-bound pass.**
