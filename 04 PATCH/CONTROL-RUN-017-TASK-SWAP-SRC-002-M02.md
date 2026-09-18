# CONTROL-RUN-017 — TASK SWAP — SAME MACHINE + SOURCE

**Дата:** 18-09-2026  
**Время:** 15-12 (мск+2 часа)  
**SUPERAGENT:** MVP-SUPERAGENT-001  
**MACHINE:** MACHINE-SOURCE-001  
**SOURCE:** SRC-002  
**TASK:** M02 DISTINCTIONS  
**Test type:** task interchangeability

## 1. Purpose

Проверить инвариант:

`MACHINE ≠ TASK`

Тот же фиксированный MACHINE-SOURCE-001 и тот же SOURCE_PACKAGE запускаются с другим TASK.

## 2. Source

**SOURCE_ID:** SRC-002  
**SOURCE_NAME:** GM Quality System Basics Overview — Supplier Audit  
**SOURCE_TYPE:** PDF  
**SOURCE_VERSION:** rev March 2009  
**SOURCE_PACKAGE_STATUS:** COMPLETE  
**WORK_SCOPE:** pages 1–5 of 350.

The source package is the same logical source used in the previous SRC-002 production runs.

Previous outputs are not used as operational input.

## 3. Machine and Task

Machine remains:

`MACHINE-SOURCE-001`

Source remains:

`SRC-002`

Task is explicitly:

`M02 DISTINCTIONS`

New production identity:

**BATCH_ID:** BATCH-SRC-002-M02-003

## 4. Input gate

Checks:
- SOURCE_ID present — PASS
- SOURCE_PACKAGE present — PASS
- TASK present — PASS
- scope declared — PASS
- direct SOURCE_PACKAGE route for M02 — contract-supported — PASS
- previous outputs excluded as operational input — PASS
- traceability required — PASS

Result: **ACCEPT**

## 5. M02 execution

M02 operates directly on the declared SOURCE_PACKAGE, without requiring the previous M01 output.

Source-grounded distinctions from pages 1–5:

1. SOURCE IDENTIFICATION ≠ SOURCE CONTENT  
   Engineering distinction; not claimed as GM terminology.

2. QSB STRATEGY SET ≠ SINGLE STRATEGY

3. AUDIT RESULT ≠ WORKSHOP DECISION

4. COMMON PRINCIPLES ≠ COMMON METHODS ≠ COMMON PROCESSES

5. PROBLEM IDENTIFICATION ≠ PROBLEM SOLVING  
   This distinction is retained as a candidate requiring the same scope qualification established previously: pages 1–5 alone do not fully establish the separation later made explicit on p6.

Result: **M02 PASS WITH CONTENT QUALIFICATION**

## 6. Task-swap criterion

Unchanged:
- MACHINE;
- SOURCE;
- source package;
- machine production rules;
- contract framework.

Changed:
- TASK;
- BATCH_ID;
- OUTPUT type/content.

No machine modification is required.

## 7. Result

**CONTROL-RUN-017 = PASS WITH CONTENT QC NOTE**

The architectural behavior is established for the tested route:

`SAME MACHINE + SAME SOURCE + DIFFERENT TASK → VALID TASK-SPECIFIC OUTPUT`

The direct-source M02 route is exercised without silently importing the prior M01 output.

## 8. Evidence boundary

Established:
- TASK can be changed while MACHINE and SOURCE remain fixed;
- M02 accepts direct SOURCE_PACKAGE under the current TASK contract;
- each TASK execution receives a new BATCH_ID;
- previous output is not silently required.

Not established:
- every TASK accepts direct SOURCE_PACKAGE;
- every TASK is semantically valid for every source;
- universal TASK interchangeability across M01–M08.
