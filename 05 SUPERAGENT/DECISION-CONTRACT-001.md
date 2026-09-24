# DECISION-CONTRACT-001

## Статус
CONTRACT CANDIDATE — v0.1

## Назначение

Зафиксировать минимальный общий контракт DECISION между RECONCILIATION_RESULT и ADMISSION для текущего MVP.

Контракт не вводит новый тип semantic capability. Он формализует уже принятый MVP-контур:

RECONCILIATION_RESULT
→ HUMAN DECISION
→ ADMISSION
→ CMOC

## 1. Положение в архитектуре

DECISION — отдельный результат принятия решения.

DECISION не является:

- RECONCILIATION_RESULT;
- ADMISSION;
- CMOC object;
- CMOC write operation.

Главная граница:

DECISION
→ разрешает ADMISSION

ADMISSION
→ физически реализует принятое решение.

## 2. Допустимые результаты

Для текущего MVP DECISION может содержать только:

- ADMIT_EXISTING;
- ADMIT_NEW;
- REJECT;
- DEFER.

Новые результаты не вводятся этим контрактом.

## 3. Минимальная структура

```yaml
decision:
  decision_id:
  decision_type: HUMAN | RULE
  decision_result:
    ADMIT_EXISTING | ADMIT_NEW | REJECT | DEFER

  match_id:

  basis:

  source_id:
  traceability:

  decided_by:
  decided_at:

  rule_id: null
  rule_version: null
```

## 4. Идентичность

`decision_id` однозначно идентифицирует конкретное решение.

Decision должен ссылаться на конкретный `match_id`.

Decision не должен заменять upstream identity собственным идентификатором.

Минимальная lineage:

SOURCE
→ DISCOVERY
→ RECONCILIATION_RESULT
→ match_id
→ DECISION
→ ADMISSION

## 5. Decision type

### HUMAN

`decision_type = HUMAN`

Решение принято человеком.

Обязательно сохраняются:

- `decided_by`;
- `decided_at`;
- `basis`;
- `traceability`.

`rule_id` и `rule_version` для HUMAN Decision не требуются.

### RULE

`decision_type = RULE`

Решение сформировано в результате применения конкретного разрешённого RULE.

Обязательно сохраняются:

- `rule_id`;
- `rule_version`;
- `decided_at`;
- `basis`;
- `traceability`.

RULE Decision не должен скрывать semantic inference за отсутствием идентифицированного правила.

## 6. Basis

Каждый DECISION обязан иметь явный `basis`.

Basis объясняет основание принятого решения и не заменяет traceability.

Decision не должен ссылаться только на итоговый result без возможности восстановить основание.

## 7. Traceability

DECISION должен сохранять путь обратно к исходному результату сопоставления.

Минимально:

```yaml
traceability:
  source_id:
  discovery_run:
  reconciliation_id:
  match_id:
```

Дополнительные upstream identifiers сохраняются, если они были предоставлены предыдущими слоями.

## 8. Связь с RECONCILIATION

DECISION принимает результат RECONCILIATION как вход, но не выполняет повторное сопоставление.

DECISION не должен:

- изменять RECONCILIATION_RESULT;
- повторно выполнять QUERY;
- превращать `NO_MATCH` непосредственно в `NEW` без соответствующего отдельного основания;
- изменять source-bound records.

Для `ADMIT_EXISTING` Decision должен опираться на конкретный `cmoc_object_id`, полученный из RECONCILIATION_RESULT.

Для `ADMIT_NEW` Decision должен содержать основание, достаточное для принятого решения о новом объекте. Само отсутствие эквивалента автоматически достаточным основанием не считается.

## 9. Связь с Admission

DECISION не выполняет физическую запись в CMOC.

Цепочка:

DECISION
→ ADMISSION

Admission получает:

- `decision_id`;
- `decision_result`;
- `match_id`;
- `source_id`;
- `traceability`;
- необходимое целевое состояние, определяемое результатом Decision.

Для `ADMIT_EXISTING` Admission использует существующий `cmoc_object_id`.

Для `ADMIT_NEW` Admission запускает отдельный физический pipeline создания объекта.

Для `REJECT` и `DEFER` Admission не создаёт CMOC object.

## 10. Связь с автоматизацией

Текущий MVP не требует RULE automation.

Поэтому:

HUMAN
→ полноценный субъект DECISION.

RULE
→ допустимый тип DECISION при наличии конкретного разрешённого RULE.

MACHINE / LLM без разрешённого RULE
→ recommendation, а не DECISION.

Если используется RULE Decision, он должен сохранять конкретные `rule_id` и `rule_version`.

## 11. CMOC boundary

DECISION не имеет права:

- создавать CMOC object;
- изменять существующий CMOC object;
- изменять OBJECT INDEX;
- выполнять канонизацию;
- создавать relations;
- выполнять Admission.

Первая физическая граница CMOC остаётся ADMISSION.

## 12. Idempotency

Повторная фиксация одного и того же DECISION не должна создавать второй независимый Decision для той же операции.

Механизм идемпотентности физического хранения DECISION остаётся частью последующего runtime-контракта.

## 13. Negative controls

Будущие executable tests должны подтвердить:

1. отсутствует `decision_id` → reject;
2. отсутствует `match_id` → reject;
3. отсутствует `basis` → reject;
4. отсутствует `traceability` → reject;
5. неизвестный `decision_result` → reject;
6. HUMAN без `decided_by` → reject;
7. RULE без `rule_id` → reject;
8. RULE без `rule_version` → reject;
9. ADMIT_EXISTING без `cmoc_object_id` в upstream result → reject;
10. DECISION не изменяет RECONCILIATION_RESULT;
11. DECISION не пишет в CMOC;
12. DECISION не изменяет OBJECT INDEX;
13. DECISION не выполняет Admission.

## 14. Минимальные ветки acceptance

Контракт должен быть проверен минимум на:

```text
EXISTING_EQUIVALENT
        ↓
HUMAN
        ↓
ADMIT_EXISTING

NEEDS_REVIEW / NEW evidence
        ↓
HUMAN
        ↓
ADMIT_NEW

HUMAN
        ↓
REJECT

HUMAN
        ↓
DEFER
```

Отдельно должна сохраняться граница:

```text
DECISION
≠
ADMISSION
```

## 15. Отдельная ветка NEW DECISION

Специализированный NEW DECISION контракт R3/R10 не заменяется этим общим контрактом.

Он определяет условия и evidence для получения:

- NEW_APPROVED;
- NEW_REJECTED.

После получения соответствующего DECISION результат должен входить в общий downstream-контур только в пределах явно определённого mapping.

Этот контракт не расширяет R3/R10 и не превращает их synthetic evidence в production capability.

## 16. Статус

CONTRACT CANDIDATE — v0.1.

Следующий controlled step:

- создать изолированный acceptance test DECISION-CONTRACT-001;
- проверить четыре MVP-ветки;
- подтвердить отсутствие CMOC/OBJECT INDEX/ADMISSION mutation;
- после PASS определить минимальный runtime формат хранения DECISION.