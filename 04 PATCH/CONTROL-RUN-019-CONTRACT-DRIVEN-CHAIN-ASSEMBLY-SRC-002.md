# CONTROL-RUN-019 — CONTRACT-DRIVEN CHAIN ASSEMBLY

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**SUPERAGENT:** MVP-SUPERAGENT-001  
**MACHINE:** MACHINE-SOURCE-001  
**SOURCE:** SRC-002  
**WORK_SCOPE:** pages 1–5

## 1. Purpose

Проверить следующий слой Superagent: он не просто исполняет заранее заданную цепочку, а собирает следующий переход по контракту INPUT/OUTPUT.

Критерий:

OUTPUT + candidate TASK → CONTRACT CHECK → ACCEPT / REJECT

## 2. Input

SOURCE_ID: SRC-002  
SOURCE_PACKAGE_STATUS: COMPLETE  
MACHINE: MACHINE-SOURCE-001

Initial TASK: M01 EXTRACTION

Previous outputs are not used as initial operational input.

## 3. Orchestration

### Step A — M01

TASK: M01 EXTRACTION  
BATCH_ID: BATCH-SRC-002-M01-003

Direct SOURCE_PACKAGE → M01

Result: Extraction Batch produced.

Contract status: ACCEPT.

### Step B — candidate M04

Current output: Extraction Records.

Candidate next TASK: M04 NOMENCLATURE.

Contract check:

M04 requires Formulation Records.

Current output = Extraction Records.

Result:

REJECT — TYPE_MISMATCH

No M04 Batch is created. No conversion is performed. Chain does not continue through M04.

### Step C — candidate M02

Current output: Extraction Records.

Candidate next TASK: M02 DISTINCTIONS.

Contract check:

M02 accepts Extraction Record.

Result:

ACCEPT

New Batch:

BATCH-SRC-002-M02-004

M02 produces Distinction Records.

### Step D — candidate M04

Current output: Distinction Records.

Candidate next TASK: M04 NOMENCLATURE.

Contract check:

M04 requires Formulation Records.

Result:

REJECT — TYPE_MISMATCH

No M04 Batch/output.

### Step E — candidate M03

Current output: Distinction Records.

Candidate next TASK: M03 FORMULATIONS.

Contract check:

M03 accepts Distinction OR direct SOURCE_PACKAGE when explicitly contracted.

Current handoff is Distinction Records.

Result:

ACCEPT

New Batch:

BATCH-SRC-002-M03-003

M03 produces 15 Formulation Records (3 per distinction).

### Step F — candidate M04

Current output: Formulation Records.

Contract check:

M04 requires Formulation Records.

Result:

ACCEPT

The chain is now contract-compatible for M04. Execution of M04 is not included in this control run; this run tests orchestration and handoff selection.

## 4. Observed orchestration behavior

The Superagent did not treat M01 → M02 → M03 → M04 as an unconditional sequence.

It evaluated candidate transitions against the TASK contract:

M01 OUTPUT → M04 = REJECT

M01 OUTPUT → M02 = ACCEPT

M02 OUTPUT → M04 = REJECT

M02 OUTPUT → M03 = ACCEPT

M03 OUTPUT → M04 = ACCEPT

Thus the executable route emerged from contract compatibility:

M01 → M02 → M03 → M04

rather than from unconditional continuation.

## 5. Result

CONTROL-RUN-019 = PASS

Established behavior:

PLAN/CURRENT OUTPUT → SELECT CANDIDATE TASK → CONTRACT CHECK → ACCEPT/REJECT → EXECUTE NEXT

The contract gate functions as a routing constraint.

## 6. Evidence boundary

Established:
- incompatible candidate TASK is rejected before execution;
- compatible candidate TASK is accepted;
- rejected candidate does not receive a Batch;
- the next compatible TASK can be selected after rejection;
- the chain can therefore be assembled through contract checks.

Not established:
- autonomous optimization of route selection;
- selection among multiple semantically equivalent compatible TASKs;
- universal M01–M08 orchestration;
- autonomous execution outside the current agentic environment.
