# CONTROL-RUN-020 — ORCHESTRATION POLICY — EXPLICIT CANDIDATE PRIORITY

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**SUPERAGENT:** MVP-SUPERAGENT-001  
**MACHINE:** MACHINE-SOURCE-001  
**SOURCE:** SRC-002  
**Initial TASK:** M02 DISTINCTIONS

## 1. Purpose

Проверить, что при наличии нескольких кандидатов следующего TASK Superagent не «угадывает» маршрут, а применяет явно заданную orchestration policy.

## 2. Policy

На каждом переходе используется заранее объявленное правило:

1. рассмотреть кандидатов в заданном порядке;
2. проверить каждого кандидата по TASK CONTRACT;
3. первый ACCEPTED кандидат становится следующим TASK;
4. REJECTED кандидат не исполняется;
5. при отсутствии ACCEPTED кандидата — STOP.

**Candidate priority for this run:**

M04 NOMENCLATURE → M03 FORMULATIONS

## 3. Execution

### Step A — M02

SOURCE_PACKAGE → M02

BATCH_ID: BATCH-SRC-002-M02-005

Result: Distinction Records.

### Step B — candidate M04

Current output: Distinction Records.

M04 requires Formulation Records.

Contract result:

**REJECT — TYPE_MISMATCH**

No M04 Batch is created.

### Step C — candidate M03

Current output: Distinction Records.

M03 accepts Distinction Records.

Contract result:

**ACCEPT**

BATCH_ID: BATCH-SRC-002-M03-004

M03 produces 15 Formulation Records.

The first accepted candidate under the declared priority policy is therefore M03.

## 4. Policy criterion

The result demonstrates:

CANDIDATE SET + EXPLICIT PRIORITY POLICY + CONTRACT CHECK → SELECTED TASK

The selection was not based on semantic guessing or hidden preference.

## 5. Result

**CONTROL-RUN-020 = PASS**

Established:
- multiple candidate TASKs can be presented to the orchestrator;
- candidate order can be explicitly declared as policy;
- contract validation remains mandatory;
- rejected candidate is skipped without execution;
- first contract-compatible candidate under the policy is selected.

Not established:
- which policy is universally optimal;
- autonomous policy generation;
- semantic optimization of routes;
- universal orchestration across M01–M08.
