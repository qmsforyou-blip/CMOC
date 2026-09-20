# EVIDENCE-R1-QUERY-RECONCILIATION-SEMANTICS-001

**Дата:** 20-09-2026  
**Статус:** ACCEPTED  
**Gate:** `R1-QUERY-RECONCILIATION-SEMANTICS`

## 1. Цель

Зафиксировать контроль семантики перехода от четырёх результатов QUERY к текущим результатам RECONCILIATION:

- MATCH
- NO_MATCH
- CANDIDATE
- AMBIGUOUS

Тест выполнен без изменения нормативного OBJECT INDEX и без записи в CMOC.

## 2. Тест

Файл:

`05 SUPERAGENT/test_r1_query_reconciliation_semantics.py`

Локальный запуск:

`py ".\05 SUPERAGENT\test_r1_query_reconciliation_semantics.py"`

Результат:

`status = PASS`

## 3. Подтверждённая семантика

| QUERY result | RECONCILIATION result | Basis |
|---|---|---|
| MATCH | EXISTING_EQUIVALENT | EXACT match |
| NO_MATCH | NEEDS_REVIEW | NO_MATCH from configured query modes; NEW not yet proven |
| CANDIDATE | NEEDS_REVIEW | structural candidate; equivalence not established |
| AMBIGUOUS | NEEDS_REVIEW | exact object_name |

Для CANDIDATE сохранён адрес найденного кандидата `T-R1-CAND`, но результат не преобразован в equivalence.

Для AMBIGUOUS `cmoc_object_id = null`.

## 4. Контрольные инварианты

Подтверждено:

- OBJECT INDEX memory mutation = false;
- CMOC write = NONE;
- NO_MATCH → NEW = false;
- CANDIDATE → EXISTING_EQUIVALENT = false;
- AMBIGUOUS → EXISTING_EQUIVALENT = false.

Таким образом, текущая реализация не делает неявного перехода от отсутствия совпадения к NEW и не превращает кандидата или неоднозначное совпадение в установленную эквивалентность.

## 5. Граница доказательства

R1 подтверждает только текущую семантику `reconciliation.py` на изолированном тестовом fixture.

R1 не доказывает:

- NEW;
- RELATED;
- CONFLICT;
- semantic similarity;
- target_object_type mapping;
- полноту QUERY;
- семантическую полноту OBJECT INDEX;
- запись результата в CMOC.

## 6. Архитектурный вывод

Текущая граница Reconciliation MVP подтверждена экспериментально:

```
QUERY
  ├─ MATCH      → EXISTING_EQUIVALENT
  ├─ NO_MATCH   → NEEDS_REVIEW
  ├─ CANDIDATE  → NEEDS_REVIEW
  └─ AMBIGUOUS  → NEEDS_REVIEW
```

`NEEDS_REVIEW` является текущим безопасным результатом там, где эквивалентность не установлена.

Вопрос о правилах `NO_MATCH → NEW` выносится в отдельный следующий архитектурный слой и не считается реализованным данным тестом.

## 7. Связанные артефакты

- `05 SUPERAGENT/R1-QUERY-RECONCILIATION-SEMANTICS-001.md`
- `05 SUPERAGENT/test_r1_query_reconciliation_semantics.py`
- `05 SUPERAGENT/reconciliation.py`
- `05 SUPERAGENT/cmoc_query.py`
- `00 Стандарты CMOC/SPEC-004 CMOC OBJECT INDEX v0.2.md`
- `00 Стандарты CMOC/SPEC-005 CMOC QUERY v0.3.md`
