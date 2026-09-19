# MVP-SUPERAGENT-001-RUNNER v0.1

**Дата:** 18-09-2026  
**Статус:** RUNNER SPEC / MVP  
**Цель:** первый исполняемый сценарий суперагента для SRC-002 по цепочке M01→M02→M03.

## 1. Input

SOURCE_ID: SRC-002  
SOURCE: GM Quality System Basics Overview Supplier Audit  
SOURCE_PACKAGE_STATUS: COMPLETE  
TASK_SEQUENCE: M01 → M02 → M03

## 2. Execution protocol

Для каждого TASK:

1. создать новый BATCH_ID;
2. проверить входной контракт;
3. выполнить только текущий TASK;
4. сохранить OUTPUT как именованный артефакт;
5. выполнить post-output QC;
6. при ACCEPT сформировать explicit HANDOFF;
7. проверить контракт следующего TASK;
8. при REJECT остановить цепочку.

## 3. Chain

SOURCE_PACKAGE
→ M01 / EXTRACTION
→ BATCH-001
→ EXTRACTION OUTPUT
→ HANDOFF
→ M02 / DISTINCTIONS
→ BATCH-002
→ DISTINCTION OUTPUT
→ HANDOFF
→ M03 / FORMULATIONS
→ BATCH-003
→ FORMULATION OUTPUT

## 4. Input contracts

M01 accepts SOURCE_PACKAGE.

M02 accepts:
- Extraction Record; or
- SOURCE_PACKAGE only when direct M02 is explicitly contracted.

For this sequential run M02 receives the explicit M01 OUTPUT.

M03 accepts:
- Distinction; or
- SOURCE_PACKAGE only when direct M03 is explicitly contracted.

For this sequential run M03 receives the explicit M02 OUTPUT.

## 5. Gate model

Before each machine:

INPUT → CONTRACT CHECK

After each machine:

OUTPUT → OUTPUT QC

Before next machine:

OUTPUT → HANDOFF-ID → HANDOFF CONTRACT CHECK → INPUT → NEXT BATCH → MACHINE

A HANDOFF is an explicit transfer artifact between the OUTPUT of one TASK and the INPUT of the next TASK.

Minimum HANDOFF fields:

- HANDOFF_ID
- RUN_ID
- SOURCE_ID
- FROM_TASK
- TO_TASK
- OUTPUT_REF
- INPUT_TYPE
- TRACEABILITY
- STATUS
- REASON

HANDOFF status controls downstream execution:

- ACCEPT → downstream BATCH may be created and execution may continue;
- REJECT → downstream BATCH must not be created; chain stops with REASON.

Any failed gate:

REJECT + REASON + CHAIN STOP.

## 6. Required journal

Each task records:

RUN_ID  
SOURCE_ID  
TASK  
MACHINE_ID  
BATCH_ID  
INPUT_REFERENCE  
OUTPUT_REFERENCE  
STATUS  
QC_RESULT  
HANDOFF_RESULT  
REASON

The journal must preserve the HANDOFF identity and its relation to the corresponding task boundary.

## 7. Acceptance tests

### A — Sequential
M01→M02→M03 completes with three distinct Batch IDs.

### B — Handoff
M02 input explicitly references M01 output; M03 input explicitly references M02 output.

### C — No hidden state
No task may rely on an earlier result unless it is explicitly named as INPUT.

### D — Trace
M03 output can be traced to M03 Batch, M02 output, M01 output and SRC-002.

### E — Reject
A deliberately incompatible M02→M04 handoff must return CONTRACT_MISMATCH and produce no M04 output.

### F — Missing field
An otherwise type-compatible input with a required field removed must be rejected.

### G — Handoff identity
Each accepted or rejected HANDOFF has a deterministic HANDOFF_ID within the RUN and is preserved in the journal.

### H — Downstream linkage
An accepted HANDOFF is explicitly linked to the downstream BATCH that receives it.

### I — Reject stops downstream creation
A rejected HANDOFF preserves its REASON and produces no downstream BATCH.

## 8. MVP completion condition

The MVP is not considered operational merely because the chain can be described.

It is operational only after a runner produces the journal and artifacts for A–I without manually constructing hidden intermediate state.

## 9. Current implementation boundary

This file defines the runner contract. The present CMOC repository does not yet contain a separate executable agent runtime that can invoke M01/M02/M03 as independent processes.

The current MVP runner implements orchestration and explicit HANDOFF control inside one runner process. It must not be reported as an AUTOMATED RUN of independent production machines.

The next implementation step is to bind this runner contract to an actual execution mechanism while keeping MACHINE, TASK CONTRACT, SOURCE PACKAGE, BATCH, OUTPUT and HANDOFF separate.

## 10. Architectural rule

The runner may orchestrate.

It may not silently become the MACHINE.

SUPERAGENT = ORCHESTRATION  
MACHINE = PRODUCTION
