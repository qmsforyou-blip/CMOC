# ESCALATION-CONTRACT-001 — Контракт эскалации при остановке v0.1

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**Статус:** Draft / evidence-backed candidate

## 1. Назначение

Определить штатный переход Superagent от STOP к внешнему решению без самостоятельного обхода контрактной границы.

## 2. Rule

Если для текущего OUTPUT отсутствует ACCEPTED candidate TASK:

`STOP → ESCALATE → DECISION REQUIRED`

Superagent обязан:
- сохранить текущий OUTPUT и traceability;
- зафиксировать отклонённые кандидаты и причины;
- сформировать объект эскалации;
- остановить производственное продолжение;
- ожидать явного решения.

## 3. Запрет

До DECISION нельзя:
- самостоятельно менять TASK;
- самостоятельно менять policy;
- конвертировать OUTPUT;
- восстанавливать скрытый предыдущий результат;
- создавать следующий BATCH.

## 4. Decision outcomes

Минимально:

`CONTINUE_WITH_TASK`
`CHANGE_POLICY`
`STOP_FINAL`

Решение является новым явным входом оркестратора.

## 5. Formula

`NO ACCEPTED CANDIDATE → STOP → ESCALATION → EXPLICIT DECISION → CONTINUE / CHANGE / FINAL STOP`

## 6. Evidence

Контракт проверен контрольным прогоном CONTROL-RUN-022.
