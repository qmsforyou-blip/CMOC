# CONTROL-RUN-014 — Missing Required Field

## Purpose

Проверить, что суперагент различает корректный тип входа от полного выполнения контракта и останавливает TASK, если обязательное поле отсутствует.

## Route

```
INPUT TYPE = допустимый
      ↓
CONTRACT CHECK
      ↓
REQUIRED FIELD ABSENT
      ↓
REJECT
      ↓
STOP
```

## Test condition

Для M04 передаётся вход типа `FORMULATION_RECORDS`, то есть тип формально совместим с контрактом M04.

Однако из входа удаляется обязательное поле `traceability`.

Контракт M04 требует:

- `source_id`
- `batch_id`
- `records`
- `traceability`
- `ref`

## Expected result

`MISSING_TRACEABILITY → REJECT`

При этом:

- M04 Batch не создаётся;
- M04 handler не запускается;
- downstream execution не происходит.

## Result

**PASS — contract gate должен отклонить вход до создания Batch.**

## Architectural meaning

Тест отделяет:

`TYPE COMPATIBILITY`

от:

`CONTRACT COMPLETENESS`

То есть совпадение типа входа само по себе не является достаточным условием для запуска машины.

## Related

- INV-002 — HANDOFF ≠ automatic acceptance
- ARCH-004 — Safe Stop Modes
