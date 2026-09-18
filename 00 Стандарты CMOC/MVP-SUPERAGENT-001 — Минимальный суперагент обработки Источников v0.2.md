# MVP-SUPERAGENT-001 — Минимальный суперагент обработки Источников

**Версия:** v0.2  
**Дата:** 18-09-2026  
**Статус:** Evidence-backed MVP specification

## 1. Назначение

MVP-SUPERAGENT-001 — минимальный оркестратор производственных машин CMOC для обработки SOURCE_PACKAGE и получения проверяемых промежуточных результатов CMOC.

Он не является экспертом конкретного Источника и не хранит скрытое содержание производственной цепочки.

## 2. Архитектурная формула

SOURCE_PACKAGE + TASK + CONTRACT + ORCHESTRATION_POLICY → BATCH → OUTPUT → HANDOFF

При невозможности корректного перехода:

REJECT / STOP → ESCALATION → EXPLICIT DECISION → CONTRACT CHECK

## 3. Компоненты

### 3.1 MACHINE
MACHINE-SOURCE-001 — фиксированная производственная машина, описанная STD-008.

### 3.2 SOURCE INTERFACE
STD-007 + SPEC-002 — сменный SOURCE_PACKAGE и его идентификация.

### 3.3 WORKING INSTRUCTION
PROMPT-001 — операционное поведение AGENT-SOURCE-001.

### 3.4 TASK CONTRACT
TASK-CONTRACT-001 — допустимые INPUT/OUTPUT для M01–M08.

### 3.5 ORCHESTRATION POLICY
ORCH-POLICY-001 — правило выбора кандидата следующего TASK.

### 3.6 ESCALATION CONTRACT
ESCALATION-CONTRACT-001 — безопасный переход от STOP к внешнему решению.

## 4. Execution loop

RECEIVE INPUT
↓
VALIDATE SOURCE/TASK
↓
SELECT / RECEIVE CANDIDATE TASK
↓
CONTRACT CHECK
↓
ACCEPT → EXECUTE MACHINE → OUTPUT → POST-QC → HANDOFF
REJECT → NEXT CANDIDATE
NO CANDIDATE → STOP → ESCALATION

После внешнего решения:

DECISION → CONTRACT CHECK → EXECUTE / REJECT

## 5. Hard rules

1. MACHINE ≠ SOURCE ≠ TASK ≠ BATCH.
2. Каждый производственный проход получает новый BATCH_ID.
3. Handoff не означает автоматическую приемку.
4. Каждый handoff проходит contract check.
5. REJECT не создаёт downstream Batch.
6. Несовместимый output не конвертируется молча.
7. Previous output не используется без явного handoff.
8. Traceability обязательна.
9. SOURCE_PACKAGE не подменяется внешним знанием.
10. STOP является штатным производственным результатом.
11. ESCALATION не является скрытым продолжением.
12. Внешнее решение после ESCALATION должно быть явным и повторно проверяться контрактом.
13. История append-only; ошибка исправляется новым artifact/pass, а не скрытой правкой старого результата.
14. Канонизация не происходит автоматически.

## 6. Proven capabilities

### Parameterization
- source swap — CONTROL-RUN-016 PASS;
- task swap — CONTROL-RUN-017 PASS;
- combined source + task swap — CONTROL-RUN-018 PASS.

### Contract routing
- contract-driven routing — CONTROL-RUN-019 PASS;
- explicit candidate priority — CONTROL-RUN-020 PASS;
- no compatible candidate → STOP — CONTROL-RUN-021 PASS;
- STOP → ESCALATE → explicit decision → continue — CONTROL-RUN-022 PASS.

### Negative-path controls
- type mismatch reject — CONTROL-RUN-013 PASS;
- structural contract mismatch — CONTROL-RUN-014 PASS;
- repair/retry — CONTROL-RUN-015 PASS.

### Production evidence
- real SRC-002 M01→M02→M03 runs exist;
- direct SOURCE_PACKAGE routes for M01–M03 are evidenced within the tested boundary;
- second-source direct M02/M03 evidence exists for SRC-003;
- M04–M08 direct SOURCE_PACKAGE execution is not established.

## 7. Current evidence boundary

Established for the tested scope:
- fixed machine core can operate with different sources;
- fixed machine core can operate with different tasks;
- source/task can be explicit inputs;
- contract checks can route or reject;
- policy can select among candidates;
- unresolved routing can stop and escalate;
- explicit external decision can resume execution after contract revalidation;
- provenance and Batch identity are retained.

Not established:
- autonomous policy generation;
- semantic route optimization;
- universal compatibility of all SOURCE_PACKAGE × TASK combinations;
- direct-source execution for M04–M08;
- autonomous external software runtime;
- automatic semantic canonization;
- independent validation of semantic completeness of every output.

## 8. MVP Definition of Done

SOURCE/TASK INPUT
↓
CONTRACT GATE
↓
EXECUTE
↓
QC
↓
HANDOFF
↓
CONTRACT ROUTING
↓
ACCEPT / REJECT / STOP
↓
ESCALATE when unresolved
↓
EXPLICIT DECISION
↓
REVALIDATE
↓
CONTINUE

The MVP is an orchestration layer over production machines, not a replacement for the machines themselves.
