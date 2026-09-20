# EVIDENCE — A4 Discovery / Reconciliation Negative Controls

**ID:** EVIDENCE-A4-RECONCILIATION-DISCOVERY-ISOLATION-001  
**Дата:** 20-09-2026  
**Статус:** ACCEPTED  
**Область:** WORK-PLAN-DISCOVERY-RECONCILIATION-001 / A4 Negative Controls

## 1. Цель

Зафиксировать результаты полного набора A4 negative controls, проверяющих архитектурную границу между DISCOVERY и RECONCILIATION.

> **Сначала добываем. Потом сопоставляем.**

DISCOVERY формирует source-bound result. RECONCILIATION получает этот результат как вход и может формировать собственный результат сопоставления с CMOC, но не должен молча изменять исходный DISCOVERY RESULT.

Контроли A4 проверяют пять направлений:
1. CMOC содержит эквивалент;
2. CMOC содержит похожий объект;
3. CMOC содержит конфликтующую информацию;
4. QUERY/CMOC недоступны;
5. вход RECONCILIATION неполон или неоднозначен.

## 2. Архитектурная граница

````
SOURCE
  ↓
DISCOVERY
  ↓
DISCOVERY RESULT
  ↓
RECONCILIATION
  ↓
CMOC / OBJECT INDEX / QUERY
  ↓
RECONCILIATION RESULT
````

Недопустим обратный поток:

````
DISCOVERY
  ↓
CMOC lookup
  ↓
изменение DISCOVERY RESULT
````

A4 не проверяет семантическую полноту RECONCILIATION. Его задача — проверить изоляцию границы и отсутствие обратной семантической утечки.

## 3. A4.1 — CMOC equivalent

В копию OBJECT INDEX добавляется синтетический canonical OBJECT_FILE, совпадающий с Discovery value PAS-006.

Результат:
- RECONCILIATION: `EXISTING_EQUIVALENT`;
- basis: `EXACT match`;
- Discovery result: unchanged;
- original OBJECT INDEX: unchanged;
- real index file: not modified.

Команда:
````powershell
py "05 SUPERAGENT/test_a4_1_cmoc_equivalent_downstream.py"
````

Статус: **PASS**

Доказано: наличие эквивалентного объекта в CMOC может изменить RECONCILIATION result, но не source-bound DISCOVERY result.

Ограничение: контроль не является новым полным M01–M08 LLM-run.

## 4. A4.2 — CMOC similar object

В копию OBJECT INDEX добавляется синтетический TERM с другим object_name и явными структурными признаками, заданными через structural_query.

Результат:
- QUERY: structural candidate;
- RECONCILIATION: `NEEDS_REVIEW`;
- basis: `structural candidate; equivalence not established`;
- Discovery result: unchanged;
- original OBJECT INDEX: unchanged;
- real index file: not modified.

Команда:
````powershell
py "05 SUPERAGENT/test_a4_2_similar_object_downstream.py"
````

Статус: **PASS**

Доказано:
````
STRUCTURAL SIMILARITY
        ↓
CANDIDATE
        ↓
NEEDS_REVIEW
````

а не:
````
STRUCTURAL SIMILARITY
        ↓
EXISTING_EQUIVALENT
````

DISCOVERY RESULT при этом не изменяется.

Ограничение: контроль не является новым полным M01–M08 LLM-run.

## 5. A4.3 — CMOC conflicting information

В копию OBJECT INDEX добавляется синтетический TERM с тем же object_name, что у PAS-006, и отдельным conflicting claim.

Результат:
- RECONCILIATION: `EXISTING_EQUIVALENT`;
- basis: `EXACT match`;
- Discovery result: unchanged;
- original OBJECT INDEX: unchanged;
- real index file: not modified.

Команда:
````powershell
py "05 SUPERAGENT/test_a4_3_conflicting_cmoc_downstream.py"
````

Статус: **PASS**

Критическое ограничение:

A4.3 **не доказывает обнаружение или разрешение конфликта**.

Текущий EXACT QUERY проверяет object_id/object_name и не анализирует `indexed_attributes.conflicting_claim`. Поэтому полученный `EXISTING_EQUIVALENT` является следствием текущей реализации QUERY.

Следовательно:
> A4.3 доказывает downstream isolation, но не conflict resolution.

Отдельный механизм CONFLICT detection/resolution остаётся будущей задачей.

## 6. A4.4 — QUERY/CMOC unavailable

Импорты `cmoc_query`, `reconciliation`, `reconciliation_input_adapter` явно блокируются. После этого выполняется контролируемая orchestration-цепочка M01–M08 через тот же SUPERAGENT orchestration kernel с deterministic control handlers.

Результат:
````json
{
  "status": "PASS",
  "discovery_chain_completed": true,
  "tasks_completed": 8,
  "handoffs_accepted": 7,
  "cmoc_access": "BLOCKED",
  "query_access": "BLOCKED"
}
````

Команда:
````powershell
py "05 SUPERAGENT/test_a4_4_query_unavailable_discovery.py"
````

Статус: **PASS**

Доказано:
> DISCOVERY orchestration не требует QUERY/CMOC для завершения source-bound pass.

Ограничение: это controlled orchestration test, а не новый LLM production run. Он не доказывает независимость каждого production LLM adapter от этих импортов; launcher и архитектурная граница проверяются отдельно.

## 7. A4.5 — Incomplete / ambiguous input

Контроль содержит два подслучая.

### 7.1 Incomplete

Минимальный Reconciliation Input содержит только обязательные для этого слоя:
- `record_id`;
- `value`;
- `traceability`.

Результат:
- RECONCILIATION: `NEEDS_REVIEW`;
- `cmoc_object_id = null`;
- input record: unchanged.

### 7.2 Ambiguous

В копию OBJECT INDEX добавляются две неканонические `REGISTRY_RECORD` репрезентации с одинаковым exact `object_name`.

Результат:
- RECONCILIATION: `NEEDS_REVIEW`;
- `cmoc_object_id = null`;
- input record: unchanged;
- original OBJECT INDEX: unchanged;
- real index file: not modified.

Команда:
````powershell
py "05 SUPERAGENT/test_a4_5_incomplete_ambiguous_discovery.py"
````

Статус: **PASS**

Доказано:
> Неполнота или неоднозначность не превращаются автоматически в установленный факт и не вызывают переписывания DISCOVERY.

## 8. Сводная матрица A4

| Gate | Контроль | RECONCILIATION | DISCOVERY mutation | Статус |
|---|---|---|---|---|
| A4.1 | CMOC equivalent | EXISTING_EQUIVALENT | NO | PASS |
| A4.2 | CMOC similar | NEEDS_REVIEW | NO | PASS |
| A4.3 | CMOC conflicting information | EXISTING_EQUIVALENT* | NO | PASS |
| A4.4 | QUERY/CMOC unavailable | DISCOVERY completes | NOT POSSIBLE | PASS |
| A4.5 | incomplete / ambiguous | NEEDS_REVIEW | NO | PASS |

* A4.3 не доказывает conflict resolution; текущий EXACT QUERY не анализирует conflicting claim.

## 9. Общий результат

Все пять предусмотренных A4 negative controls пройдены:

````
A4.1 PASS
A4.2 PASS
A4.3 PASS
A4.4 PASS
A4.5 PASS
````

Следствие для архитектуры:
````
SOURCE
  ↓
DISCOVERY
  ↓
RESULT-A
  │
  │ immutable boundary
  ↓
RECONCILIATION
  ↓
RESULT-B
````

CMOC/OBJECT INDEX/QUERY могут влиять на RESULT-B, но не должны изменять RESULT-A.

## 10. Что A4 НЕ доказывает

A4 не устанавливает:
- semantic completeness DISCOVERY;
- semantic completeness RECONCILIATION;
- automatic CONFLICT detection/resolution;
- automatic NEW decision;
- automatic canonization;
- distributed execution;
- failure recovery;
- correctness of arbitrary positive relation detection;
- reproducibility on a new SOURCE.

Эти свойства относятся к последующим этапам.

## 11. Gate

**A4 — PASS / READY TO CLOSE**

Следующий этап Work Plan: **A5 — Новый SOURCE**, после фиксации данного evidence и закрытия A4 в рабочем плане.