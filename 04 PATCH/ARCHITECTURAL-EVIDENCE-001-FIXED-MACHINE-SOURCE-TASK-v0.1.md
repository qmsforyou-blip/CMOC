# ARCHITECTURAL-EVIDENCE-001 — FIXED MACHINE / SOURCE / TASK

**DATE:** 18-09-2026  
**STATUS:** EVIDENCE-BACKED v0.2

## 1. Question

Does the production architecture separate the fixed machine core from the interchangeable SOURCE and TASK while preserving Batch identity and traceability?

## 2. Controlled evidence

| Run | Agent | Prompt | Source | Task | Direct source route | Output structure |
|---|---|---|---|---|---|---|
| RUN-007 | AGENT-SOURCE-001 | PROMPT-001 v0.3 | SRC-003 | M03 FORMULATIONS | YES | 20 → 60 → 3/input |
| RUN-008 | AGENT-SOURCE-001 | PROMPT-001 v0.3 | SRC-003 | M03 FORMULATIONS | YES | 20 → 60 → 3/input |
| RUN-009 | AGENT-SOURCE-001 | PROMPT-001 v0.3 | SRC-002 | M03 FORMULATIONS | YES | 20 → 60 → 3/input |
| RUN-010 | AGENT-SOURCE-001 | PROMPT-001 v0.3 | SRC-002 | M02 DISTINCTIONS | YES | 20 → 20 |

## 3. What is directly established

### 3.1 Fixed machine survives SOURCE change

RUN-007/008 and RUN-009 use the same declared AGENT-SOURCE-001 and PROMPT-001 v0.3 while changing SRC-003 to SRC-002. No source-specific modification of the machine or prompt is declared.

**Evidence status: ESTABLISHED for the tested M03 route.**

### 3.2 Same SOURCE can be processed repeatedly

RUN-007 and RUN-008 use SRC-003 with the same TASK and the same machine/prompt configuration. Both produce the same structural cardinality: 20 direct observations → 60 formulations → 3 per observation.

**Evidence status: ESTABLISHED structurally for the tested M03 route.**

### 3.3 Same SOURCE can accept different TASKs

RUN-009 and RUN-010 use the same SRC-002 SOURCE_PACKAGE with the same AGENT-SOURCE-001 and PROMPT-001 v0.3, while changing TASK from M03 FORMULATIONS to M02 DISTINCTIONS. A new BATCH_ID is assigned and the previous M03 output is not used as operational input.

**Evidence status: ESTABLISHED for the tested M02/M03 pair on SRC-002.**

### 3.4 SOURCE and TASK are separate interface dimensions

The controlled runs demonstrate that SOURCE identity and TASK identity are declared independently in the production interface. Each production pass has its own BATCH_ID.

**Evidence status: ESTABLISHED as an interface rule, with direct-source evidence for the tested M01/M02/M03 routes.**

### 3.5 Traceability survives the separation

Each tested output is tied to SOURCE_ID, BATCH_ID and a defined source scope/observation boundary. The runs explicitly prohibit silent use of previous processing artifacts.

**Evidence status: ESTABLISHED for the tested runs.**

## 4. Architectural invariant supported by evidence

> **MACHINE ≠ SOURCE ≠ TASK ≠ BATCH**

This is an evidence-backed architectural invariant for the tested production routes.

- **MACHINE** — fixed production core.
- **SOURCE** — material/input package.
- **TASK** — declared production operation.
- **BATCH** — identity of one concrete SOURCE/TASK execution.

## 5. Architectural model

```
                 FIXED MACHINE CORE
                 AGENT-SOURCE-001
                         │
                         │ fixed
                         ▼
              ┌─────────────────────┐
              │ SOURCE_PACKAGE      │
              │ interchangeable     │
              └─────────────────────┘
                         │
                         + TASK
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

The machine therefore does not contain the source and does not define the particular task instance. SOURCE and TASK are supplied through an explicit interface; BATCH identifies the concrete production pass.

## 6. Architectural proposition

> **A source-processing machine can be engineered as a fixed production core with interchangeable SOURCE_PACKAGE and explicit TASK parameters, provided each execution has an explicit Batch identity, traceability contract and defined evidence boundary.**

This proposition is supported by RUN-007 through RUN-010 for the tested routes. It is not a claim of universal applicability.

## 7. Significance for CMOC

The controlled evidence shifts the production unit from a one-off prompt applied to one document toward a parameterized production machine.

The practical consequence is:

**source-specific material belongs in SOURCE_PACKAGE; production intent belongs in TASK; execution identity belongs in BATCH; reusable production rules belong in the MACHINE.**

This supports treating SOURCE_PACKAGE as an interface component rather than embedding source-specific logic inside the machine.

## 8. Evidence boundary — not established

The evidence does not establish:

- universal applicability of every TASK to every SOURCE;
- semantic equivalence of outputs between different sources;
- direct SOURCE_PACKAGE execution for M04–M08;
- automatic CMOC canonization;
- universal semantic completeness of the machine;
- that structural reproducibility guarantees identical substantive knowledge output across sources.

## 9. Next architectural question

The next question is no longer whether SOURCE and TASK can be varied independently in the tested cases. That has been demonstrated.

The next useful control is to test whether the **same explicit interface and Batch discipline remain stable across a longer TASK chain**, without turning intermediate outputs into hidden state.

