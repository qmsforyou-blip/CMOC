# ORCH-POLICY-001 — Политика оркестрации производственных машин v0.1

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**Статус:** Draft / evidence-backed candidate

## 1. Назначение

Определить внешний контракт политики, по которому SUPERAGENT выбирает следующий TASK/MACHINE после получения текущего OUTPUT.

## 2. Принцип

SUPERAGENT не должен самостоятельно выдумывать критерий выбора маршрута.

Оркестрационная политика передаётся явно и является входом оркестратора.

## 3. Минимальный интерфейс

```
CURRENT_OUTPUT
CANDIDATE_TASKS
ORCHESTRATION_POLICY
TASK_CONTRACTS
        ↓
CANDIDATE ORDER
        ↓
CONTRACT CHECK
        ↓
ACCEPT / REJECT
        ↓
SELECT / NEXT / STOP
```

## 4. Минимальная policy v0.1

Для каждого перехода:

1. получить список кандидатов;
2. получить порядок/правило приоритета;
3. проверить кандидатов по контракту;
4. выбрать первый ACCEPTED согласно policy;
5. REJECTED не исполнять;
6. если ACCEPTED отсутствует — STOP;
7. зафиксировать решение и причину.

## 5. Запреты

- нельзя выбирать TASK по скрытой семантической интуиции;
- нельзя обходить CONTRACT CHECK;
- нельзя автоматически конвертировать несовместимый OUTPUT;
- нельзя создавать BATCH до ACCEPT;
- нельзя использовать скрытое состояние;
- нельзя выдавать отсутствие подходящего кандидата как успешное продолжение.

## 6. Формула

`OUTPUT + CANDIDATES + POLICY + CONTRACTS → DECISION → EXECUTE / STOP`

## 7. Evidence

Поддержано CONTROL-RUN-019 и CONTROL-RUN-020:
- contract-driven routing;
- explicit candidate priority;
- reject before execution;
- selection of first contract-compatible candidate.

Ограничение: policy generation и semantic optimization не проверены.
