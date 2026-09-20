# EVIDENCE — A4.2 Similar Object Downstream Isolation

**ID:** EVIDENCE-A4.2-RECONCILIATION-SRC-002-001  
**Дата:** 20-09-2026  
**Статус:** ACCEPTED  
**Область:** WORK-PLAN-DISCOVERY-RECONCILIATION-001 / A4 Negative Controls

## 1. Цель

Проверить, что структурное сходство с объектом CMOC не устанавливает эквивалентность и не изменяет source-bound DISCOVERY RESULT.

Контроль использует production-derived M06 Passport fixture для SRC-002. В копию OBJECT INDEX добавлен синтетический TERM с другим object_name, но с совпадающими явными структурными признаками.

## 2. Контроль

Для PAS-006:

- Discovery value: `Fast Response`
- synthetic CMOC object_id: `TEST-T-FR-SIM-001`
- synthetic CMOC object_name: `Fast Response management`

В RECONCILIATION явно передан structural_query с признаками:

- object_type = TERM;
- representation_kind = OBJECT_FILE;
- fields_present = object_id, object_name, representation.

QUERY возвращает структурного кандидата. RECONCILIATION не преобразует кандидата в эквивалентность.

## 3. Результат

Команда:

```powershell
py "05 SUPERAGENT/test_a4_2_similar_object_downstream.py"
```

Результат:

```text
gate: A4.2-SIMILAR-OBJECT-DOWNSTREAM-ISOLATION
status: PASS
tested_passport: PAS-006
discovery_value: Fast Response
synthetic_cmoc_object_id: TEST-T-FR-SIM-001
reconciliation_result: NEEDS_REVIEW
reconciliation_basis: structural candidate; equivalence not established
discovery_unchanged: true
original_index_unchanged: true
real_index_file_modified: NO
```

## 4. Что доказано

Контроль подтверждает:

```text
STRUCTURAL SIMILARITY
        ↓
CANDIDATE
        ↓
NEEDS_REVIEW
```

и не:

```text
STRUCTURAL SIMILARITY
        ↓
EXISTING_EQUIVALENT
```

DISCOVERY RESULT при этом не изменяется.

## 5. Ограничение доказательства

Контроль не выполняет новый полный M01–M08 LLM-run.

Он использует production-derived M06 Passport fixture и проверяет downstream boundary на результате Discovery.

Не проверены этим тестом:

- конфликтующая информация;
- недоступность QUERY;
- неполный/неоднозначный Discovery Result.

## 6. Gate

**A4.2 — PASS**

Следующий контроль: **A4.3 — CMOC conflicting information → DISCOVERY RESULT unchanged.**