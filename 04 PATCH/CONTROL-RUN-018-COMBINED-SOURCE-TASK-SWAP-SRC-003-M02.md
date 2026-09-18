# CONTROL-RUN-018 — COMBINED SOURCE + TASK SWAP

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**SUPERAGENT:** MVP-SUPERAGENT-001  
**MACHINE:** MACHINE-SOURCE-001  
**SOURCE:** SRC-003  
**TASK:** M02 DISTINCTIONS  
**Test type:** combined parameter swap

## 1. Purpose

Проверить, что SOURCE и TASK действительно являются независимыми параметрами MACHINE и могут одновременно изменяться без изменения MACHINE.

`MACHINE ≠ SOURCE ≠ TASK`

## 2. Controlled input

SOURCE_ID: SRC-003  
SOURCE_PACKAGE_STATUS: COMPLETE  
TASK: M02 DISTINCTIONS  
MACHINE: MACHINE-SOURCE-001

Previous SRC-003 outputs are not used as operational input.

New production identity:

**BATCH_ID:** BATCH-SRC-003-M02-001

## 3. Input contract gate

- SOURCE_ID — PASS
- SOURCE_PACKAGE — PASS
- TASK — PASS
- direct SOURCE_PACKAGE → M02 — PASS
- traceability requirement — PASS
- no hidden previous output — PASS

**Gate result: ACCEPT**

## 4. Execution

M02 operates directly on SRC-003 SOURCE_PACKAGE.

Controlled scope: 20 source locations/observations.

Output:
- 20 Distinction Records;
- source traceability retained;
- no external knowledge used;
- no modification of MACHINE;
- no prior SRC-003 M02 output used as operational input.

**Execution result: PASS**

## 5. Combined-swap criterion

Compared with CONTROL-RUN-017:
- MACHINE unchanged;
- SOURCE changed SRC-002 → SRC-003;
- TASK remains M02.

Combined architectural test is interpreted together with CONTROL-RUN-016 (source swap) and CONTROL-RUN-017 (task swap).

The machine accepts the new SOURCE/TASK parameterization without source-specific or task-specific modification to the machine core.

## 6. Result

**CONTROL-RUN-018 = PASS**

Observed behavior:

`MACHINE + SOURCE + TASK → BATCH → OUTPUT`

with SOURCE and TASK supplied as explicit parameters.

## 7. Evidence boundary

Established:
- combined parameterization is operationally valid for the tested M02 direct-source route;
- SOURCE and TASK can vary without modifying MACHINE;
- new BATCH identity is created;
- traceability remains explicit;
- no hidden state is required.

Not established:
- universal compatibility of every SOURCE_PACKAGE with every TASK;
- universal direct-source route for M04–M08;
- semantic completeness of outputs;
- automatic canonization.
