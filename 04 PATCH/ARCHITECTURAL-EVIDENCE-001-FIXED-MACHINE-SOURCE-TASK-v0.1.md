# ARCHITECTURAL-EVIDENCE-001 — FIXED MACHINE / SOURCE / TASK

**DATE:** 18-09-2026
**STATUS:** EVIDENCE-BACKED DRAFT

## 1. Question

Does the production architecture separate the fixed machine core from the interchangeable source and the production TASK, while preserving Batch identity and traceability?

## 2. Controlled evidence

| Run | Agent | Prompt | Source | Task | Direct source route | Output structure |
|---|---|---|---|---|---|---|
| RUN-007 | AGENT-SOURCE-001 | PROMPT-001 v0.3 | SRC-003 | M03 FORMULATIONS | YES | 20 → 60 → 3/input |
| RUN-008 | AGENT-SOURCE-001 | PROMPT-001 v0.3 | SRC-003 | M03 FORMULATIONS | YES | 20 → 60 → 3/input |
| RUN-009 | AGENT-SOURCE-001 | PROMPT-001 v0.3 | SRC-002 | M03 FORMULATIONS | YES | 20 → 60 → 3/input |

## 3. What is directly established

### 3.1 Fixed machine survives source change

RUN-007/008 and RUN-009 use the same declared AGENT-SOURCE-001 and PROMPT-001 v0.3 while changing SRC-003 to SRC-002. No source-specific modification of the machine or prompt is declared.

**Evidence status: ESTABLISHED for the tested M03 route.**

### 3.2 Same source can be processed repeatedly

RUN-007 and RUN-008 use SRC-003 with the same TASK and the same machine/prompt configuration. Both produce the same structural cardinality: 20 direct observations → 60 formulations → 3 per observation.

**Evidence status: ESTABLISHED structurally for the tested M03 route.**

### 3.3 Source and TASK are separate interface dimensions

The controlled runs demonstrate that source identity and task identity are declared independently in the production interface. Each production pass has its own BATCH_ID.

**Evidence status: ESTABLISHED as an interface rule; direct-source evidence is specific to the tested M03 route and previously tested M01/M02 routes.**

### 3.4 Traceability survives the separation

Each tested formulation set is tied to a source observation, source page/scope, SOURCE_ID and BATCH_ID. The runs explicitly prohibit silent use of previous processing artifacts.

**Evidence status: ESTABLISHED for the tested runs.**

## 4. What is NOT established

The evidence does not establish:

- universal applicability of every TASK to every SOURCE;
- semantic equivalence of formulations between different sources;
- direct SOURCE_PACKAGE execution for M04–M08;
- automatic CMOC canonization;
- universal semantic completeness of the machine;
- that structural reproducibility guarantees identical substantive knowledge output across sources.

## 5. Architectural model supported by evidence

```text
                 FIXED MACHINE CORE
                 AGENT-SOURCE-001
                         │
                         │ fixed
                         ▼
              ┌─────────────────────┐
              │ SOURCE_PACKAGE      │  ← interchangeable source
              └─────────────────────┘
                         │
                         + TASK       ← production instruction
                         │
                         ▼
                     BATCH_ID
                         │
                         ▼
                    OUTPUT
                         │
                         ▼
                    TRACEABILITY
```

The tested architecture therefore supports the following separation:

**MACHINE ≠ SOURCE ≠ TASK ≠ BATCH**

The Batch is the production-pass identity connecting a particular SOURCE/TASK execution to its output and traceability.

## 6. Architectural proposition

> **A source-processing machine can be engineered as a fixed production core with interchangeable SOURCE_PACKAGE and explicit TASK parameters, provided each execution has an explicit Batch identity, traceability contract and defined evidence boundary.**

This is an evidence-backed architectural proposition, not a claim of universal applicability.

## 7. Significance for CMOC

The controlled evidence shifts the unit of analysis from a one-off prompt applied to one document toward a reproducible production machine whose material input can be exchanged without rewriting the machine core.

This supports treating SOURCE_PACKAGE as an interface component rather than embedding source-specific logic inside the machine.

## 8. Next control question

The next useful test is not another M03 repetition. It is whether the same separation remains valid when the TASK changes while the SOURCE remains fixed, using the same explicit interface and a new BATCH_ID, with the direct-source boundary stated honestly.
