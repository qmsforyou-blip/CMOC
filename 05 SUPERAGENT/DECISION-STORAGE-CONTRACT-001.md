# DECISION-STORAGE-CONTRACT-001

## Статус
CONTRACT CANDIDATE — v0.1

## Назначение

Зафиксировать минимальный физический формат хранения уже принятого DECISION.

Контракт не вводит новый semantic layer и не выполняет Admission.

## 1. Положение

RECONCILIATION_RESULT
→ DECISION
→ DECISION ARTIFACT
→ ADMISSION

DECISION ARTIFACT — физическая сохранённая форма DECISION.

Он не является:

- RECONCILIATION_RESULT;
- ADMISSION;
- CMOC object;
- OBJECT INDEX record;
- runtime journal event.

## 2. Формат

Для MVP используется один UTF-8 JSON artifact на один DECISION.

Рекомендуемая форма:

```json
{
  "type": "DECISION",
  "decision": {
    "decision_id": "DEC-...",
    "decision_type": "HUMAN",
    "decision_result": "ADMIT_EXISTING",
    "match_id": "MAT-...",
    "basis": "...",
    "source_id": "SRC-...",
    "traceability": {
      "source_id": "SRC-...",
      "discovery_run": "RUN-...",
      "reconciliation_id": "RECON-...",
      "match_id": "MAT-..."
    },
    "decided_by": "operator-001",
    "decided_at": "2026-09-24T09:00:00+02:00",
    "rule_id": null,
    "rule_version": null
  },
  "boundary": {
    "origin": "DECISION",
    "reconciliation_mutation": "NONE",
    "cmoc_write": "NONE",
    "object_index_write": "NONE",
    "admission_execution": "NOT_PERFORMED"
  }
}
```

## 3. Identity

`decision_id` является устойчивым идентификатором физического Decision artifact.

Один `decision_id` → один Decision.

Повторная запись того же Decision не должна создавать второй независимый artifact.

Механизм физической дедупликации/идемпотентной записи остаётся runtime responsibility и этим контрактом не реализуется.

## 4. Источник истины

До Admission источником истины для принятого решения является DECISION artifact.

Runtime journal может фиксировать факт создания/обработки Decision, но не заменяет сам Decision artifact.

Runtime state не должен становиться вторым semantic representation Decision.

## 5. Traceability

Минимально сохраняется:

- source_id;
- discovery_run;
- reconciliation_id;
- match_id.

Дополнительная upstream traceability сохраняется без потери.

`match_id` в Decision и `traceability.match_id` должны совпадать.

`source_id` в Decision и `traceability.source_id` должны совпадать.

## 6. Decision type

### HUMAN

Обязательны:

- decided_by;
- decided_at;
- basis;
- traceability.

`rule_id` и `rule_version` могут быть null.

### RULE

Обязательны:

- rule_id;
- rule_version;
- decided_at;
- basis;
- traceability.

## 7. Admission boundary

Сохранение DECISION artifact не означает Admission.

После физического сохранения:

```text
admission_execution = NOT_PERFORMED
cmoc_write = NONE
object_index_write = NONE
```

Следующий шаг выполняется только отдельным Admission контрактом.

## 8. Запрещено

DECISION storage не должен:

- создавать CMOC object;
- изменять CMOC object;
- изменять OBJECT INDEX;
- выполнять канонизацию;
- выполнять Reconciliation;
- выполнять QUERY;
- выполнять Admission;
- превращать recommendation в Decision;
- скрывать semantic inference в runtime storage.

## 9. Relationship с runtime journal

Если runtime фиксирует событие хранения Decision, событие должно ссылаться на `decision_id`.

Runtime journal отвечает за execution history.

DECISION artifact отвечает за содержательную фиксацию принятого решения.

Это разные уровни хранения.

## 10. Минимальный acceptance

PASS требует подтвердить:

1. один Decision → один artifact;
2. artifact содержит `decision_id`;
3. artifact содержит `match_id`;
4. artifact содержит обязательный `basis`;
5. artifact содержит traceability;
6. HUMAN содержит `decided_by` и `decided_at`;
7. RULE содержит `rule_id` и `rule_version`;
8. повторная запись не создаёт второй независимый Decision;
9. storage не пишет CMOC;
10. storage не изменяет OBJECT INDEX;
11. storage не выполняет Admission;
12. runtime journal, если используется, только ссылается на `decision_id`.

## 11. Граница MVP

Этот контракт определяет только физическую форму хранения.

Он не определяет:

- UI принятия решения;
- права и роли пользователей;
- workflow согласования;
- Rule Governance;
- автоматическую генерацию Decision;
- физическую реализацию Admission;
- формат CMOC object.

## Статус

CONTRACT CANDIDATE — v0.1.

Следующий controlled step:

создать минимальный DecisionStore с идемпотентной записью/повторным чтением одного DECISION artifact и acceptance test без CMOC/OBJECT INDEX/ADMISSION mutation.
