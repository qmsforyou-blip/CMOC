# STD-009 — Матрица поведения суперагента на контрактном gate v0.1

## Назначение

STD-009 объединяет проверенные режимы поведения суперагента на границе контракта и при последующей проверке результата.

## Матрица

| Ситуация | Gate result | Batch | Execution | Следующее действие |
|---|---|---|---|---|
| Тип входа не допускается TASK | REJECT | НЕ СОЗДАЁТСЯ | НЕ ЗАПУСКАЕТСЯ | STOP |
| Обязательное поле отсутствует | REJECT | НЕ СОЗДАЁТСЯ | НЕ ЗАПУСКАЕТСЯ | STOP |
| Контракт выполнен | ACCEPT | СОЗДАЁТСЯ | ЗАПУСКАЕТСЯ | Output QC → ACCEPT / REJECT |
| Основание результата недостаточно | NEEDS_EVIDENCE | ЗАВИСИТ ОТ ТОЧКИ ОБНАРУЖЕНИЯ | STOP | Explicit operator decision → NEW BATCH → RECHECK |

## 1. TYPE_MISMATCH

```
INPUT
→ CONTRACT CHECK
→ TYPE_MISMATCH
→ REJECT
→ STOP
```

Evidence: `CONTROL-RUN-013-CONTRACT-REJECT-M02-M04.md`

## 2. MISSING_REQUIRED_FIELD

```
INPUT TYPE COMPATIBLE
→ CONTRACT CHECK
→ REQUIRED FIELD ABSENT
→ REJECT
→ STOP
```

Evidence: `CONTROL-RUN-014-MISSING-REQUIRED-FIELD.md`

## 3. CONTRACT PASS

```
INPUT
→ CONTRACT CHECK PASS
→ NEW BATCH
→ MACHINE EXECUTION
→ OUTPUT QC
→ ACCEPT
```

Evidence: `CONTROL-RUN-015-CONTRACT-ACCEPT.md`

## 4. NEEDS_EVIDENCE

```
OUTPUT
→ EVIDENCE / QC CHECK
→ NEEDS_EVIDENCE
→ STOP
→ EXPLICIT OPERATOR DECISION
→ NEW BATCH
→ RECHECK
```

Evidence:

- `CANONIZATION-DECISION-SRC-002-M08-001-CAN-001.md`
- `CANONIZATION-DECISION-SRC-002-M08-002-CAN-001-RECHECK.md`
- `SUPERAGENT-RUN-011-SRC-002-M08-CAN-001-RECHECK.md`

## Общее правило

**Суперагент продолжает производство только при наличии достаточного основания для данного перехода.**

Если контракт не выполнен — `REJECT`.

Если основание недостаточно — `NEEDS_EVIDENCE` и остановка.

Если контракт выполнен — создаётся новый Batch и запускается TASK.

## Связь с архитектурой

```
INVARIANT
   ↓
MACHINE
   ↓
TASK CONTRACT
   ↓
CONTRACT GATE
   ├── REJECT → STOP
   ├── PASS → NEW BATCH → EXECUTE → QC
   └── NEEDS_EVIDENCE → STOP → DECISION → NEW BATCH → RECHECK
```

## Связанные документы

- INV-001 — Инвариант параметризованной производственной машины
- INV-002 — Инвариант контрактной границы
- INV-003 — Инвариант управляемого исправления результата
- ARCH-002 — Архитектура оркестрации производственных машин
- ARCH-003 — Цикл управляемого исправления производственного результата
- ARCH-004 — Режимы безопасной остановки суперагента

## Evidence boundary

Матрица объединяет конкретные проверенные сценарии MVP/SRC-002. Она не утверждает универсальность каждого режима для всех машин и TASK без дополнительных контрольных прогонов.
