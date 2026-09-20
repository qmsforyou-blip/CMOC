# EVIDENCE — A4.1 CMOC Equivalent Downstream Isolation

**ID:** EVIDENCE-A4.1-RECONCILIATION-SRC-002-001  
**Дата:** 20-09-2026  
**Статус:** ACCEPTED  
**Область:** WORK-PLAN-DISCOVERY-RECONCILIATION-001 / A4 Negative Controls

## 1. Цель

Проверить, что наличие эквивалентного объекта в CMOC может изменить только результат RECONCILIATION и не изменяет source-bound DISCOVERY RESULT.

Контроль использует production-derived M06 Passport fixture для SRC-002. Реальный OBJECT INDEX не изменяется.

## 2. Контроль

В память загружена копия OBJECT INDEX. В неё добавлен синтетический TERM:

- object_id: `TEST-T-FR-001`
- object_name: `Fast Response`
- representation: OBJECT_FILE
- origin: A4.1 synthetic CMOC

После этого выполняется RECONCILIATION для PAS-006.

Проверяются одновременно:

1. RECONCILIATION распознаёт синтетический объект как `EXISTING_EQUIVALENT`;
2. DISCOVERY/PASSPORT fixture не изменён;
3. исходный OBJECT INDEX не изменён;
4. реальный файл OBJECT INDEX не модифицирован.

## 3. Результат

Команда:

```powershell
py "05 SUPERAGENT/test_a4_1_cmoc_equivalent_downstream.py"
```

Результат:

```text
gate: A4.1-CMOC-EQUIVALENT-DOWNSTREAM-ISOLATION
status: PASS
tested_passport: PAS-006
discovery_value: Fast Response
synthetic_cmoc_object_id: TEST-T-FR-001
reconciliation_result: EXISTING_EQUIVALENT
reconciliation_basis: EXACT match
discovery_unchanged: true
original_index_unchanged: true
real_index_file_modified: NO
```

## 4. Что доказано

Контроль подтверждает правило:

```text
CMOC equivalent
      ↓
RECONCILIATION → EXISTING_EQUIVALENT
      │
      └──→ DISCOVERY RESULT unchanged
```

То есть CMOC находится на downstream-границе и не получает обратного семантического влияния на source-bound Discovery result.

## 5. Ограничение доказательства

Контроль не выполняет новый полный M01–M08 LLM-run.

Он использует production-derived M06 Passport fixture и проверяет изоляцию downstream RECONCILIATION на этом результате.

Следовательно, доказано:

- отсутствие мутации Discovery result со стороны текущего RECONCILIATION;
- отсутствие мутации реального OBJECT INDEX;
- корректность положительной ветки EXISTING_EQUIVALENT.

Не доказано этим тестом отдельно:

- отсутствие CMOC-зависимости внутри нового LLM-run M01–M08;
- поведение при похожем объекте;
- поведение при конфликтующей информации;
- поведение при недоступном QUERY.

Эти случаи остаются отдельными A4 negative controls.

## 6. Gate

**A4.1 — PASS**

Следующий контроль: **A4.2 — CMOC similar object → DISCOVERY RESULT unchanged.**
