# CONTROL-RUN-015 — Contract ACCEPT

## Purpose

Проверить положительный контрпример: вход соответствует контракту TASK, обязательные поля присутствуют, поэтому машина получает разрешение на запуск и создаёт новый Batch.

## Route

```
INPUT
  ↓
CONTRACT CHECK
  ↓
ALL CONDITIONS PASS
  ↓
NEW BATCH
  ↓
MACHINE EXECUTION
  ↓
OUTPUT QC
  ↓
ACCEPT
```

## Test condition

Для M04 передаётся вход типа `FORMULATION_RECORDS`, который входит в допустимые входы M04.

Присутствуют все обязательные поля:

- `source_id`
- `batch_id`
- `records`
- `traceability`
- `ref`

## Expected result

`CONTRACT PASS → BATCH CREATED → EXECUTION → ACCEPT`

В отличие от CONTROL-RUN-013 и CONTROL-RUN-014:

- контрактный gate не отклоняет вход;
- Batch M04 создаётся;
- handler M04 получает управление;
- output проходит post-execution QC;
- результат получает статус `ACCEPT`.

## Result

**PASS**

Положительный путь подтверждает, что contract gate не является только механизмом блокировки: при выполнении условий он разрешает производственное движение.

## Architectural pair

```
CONTRACT FAIL
  → REJECT → STOP

CONTRACT PASS
  → NEW BATCH → EXECUTE → QC → ACCEPT
```

Таким образом, проверены обе стороны одного gate.

## Related

- INV-001 — MACHINE ≠ SOURCE ≠ TASK ≠ BATCH
- INV-002 — HANDOFF ≠ automatic acceptance
- ARCH-002 — orchestration architecture
- ARCH-004 — safe stop modes
