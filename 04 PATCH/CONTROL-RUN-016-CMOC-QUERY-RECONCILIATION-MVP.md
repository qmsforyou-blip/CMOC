# CONTROL-RUN-016 — CMOC QUERY + RECONCILIATION MVP v0.1

## 1. Назначение

Первый контрольный прогон второй части архитектуры:

`DISCOVERY OUTPUT → CMOC QUERY → RECONCILIATION → MATCH/DECISION`

Проверяется не семантическая полнота CMOC, а контрактное поведение read-only QUERY и безопасное сопоставление.

## 2. Вход

SOURCE_ID: `SRC-002`

INPUT_BATCH_ID: `BATCH-SRC-002-M04-001`

INPUT_OUTPUT_TYPE: `NOMENCLATURE`

Discovery candidates из M04, страницы 1–6:

- NOM-001 SOURCE_IDENTITY
- NOM-002 SOURCE_CONTENT
- NOM-003 STRATEGY_SET
- NOM-004 STRATEGY
- NOM-005 AUDIT_RESULT
- NOM-006 WORKSHOP_DECISION
- NOM-007 COMMON_PRINCIPLES
- NOM-008 COMMON_METHODS
- NOM-009 COMMON_PROCESSES
- NOM-010 FAST_RESPONSE
- NOM-011 PROBLEM_SOLVING
- NOM-012 PROBLEM_IDENTIFICATION

CMOC_QUERY_SCOPE: `TERMS`

## 3. Контрольный режим

Для каждого кандидата выполняется:

1. EXACT
2. ALIAS
3. STRUCTURAL

Правило:

`NO_MATCH ≠ NEW`

Если эквивалент не установлен — результат `NEEDS_REVIEW`.

## 4. Результат

Для 12 англоязычных NOM-кандидатов из M04:

- EXACT: `NO_MATCH`
- зарегистрированных ALIAS: нет
- надёжной структурной эквивалентности: не установлено
- RECONCILIATION: `NEEDS_REVIEW`
- автоматическое создание нового объекта: НЕТ

Это ожидаемое безопасное поведение. Отсутствие совпадения в текущем scope не превращается автоматически в NEW.

## 5. Калибровочный положительный тест

Отдельно выполнен синтетический QUERY-кейс:

`Управляемость → T-0001`

Результат:

`EXACT MATCH → EXISTING_EQUIVALENT → T-0001`

Этот кейс не является результатом SRC-002 и используется только для проверки положительной ветви QUERY/RECONCILIATION.

## 6. Проверяемые инварианты

- CMOC QUERY — read-only.
- Discovery Record не изменяется.
- Исторический Batch не изменяется.
- EXISTING_EQUIVALENT требует найденного объекта.
- STRUCTURAL candidate не повышается автоматически до equivalence.
- NO_MATCH не считается NEW.
- Traceability переносится в Match/Decision Record.
- Core action этим прогоном НЕ выполняется.

## 7. Evidence

Исполнимые артефакты:

- `05 SUPERAGENT/cmoc_query.py`
- `05 SUPERAGENT/cmoc_query_index.json`
- `05 SUPERAGENT/reconciliation.py`
- `05 SUPERAGENT/test_cmoc_query.py`
- `05 SUPERAGENT/test_reconciliation.py`

CI: GitHub Actions.

## 8. Граница доказательства

Подтверждено:

- read-only CMOC QUERY MVP;
- EXACT / ALIAS / STRUCTURAL / CANDIDATE interface;
- MATCH / NO_MATCH / CANDIDATE / SCOPE_INSUFFICIENT;
- EXISTING_EQUIVALENT для точного совпадения;
- NEEDS_REVIEW при недостаточности доказательств;
- сохранение traceability.

Не подтверждено:

- семантическое LLM-сопоставление;
- автоматическая эквивалентность по смыслу;
- автоматическое создание/обновление объектов CMOC;
- автоматическое разрешение конфликтов;
- полная индексация всех классов CMOC.

## STATUS

`PASS — MVP QUERY/RECONCILIATION CONTRACT BEHAVIOR`

