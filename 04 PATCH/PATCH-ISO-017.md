# PATCH-ISO-017

## Извещение на изменение

**0086+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 6.2 — Quality objectives and planning to achieve them; 6.2.1; 6.2.2

### SOURCE CLAIM

The organization shall establish quality objectives at relevant functions, levels and processes needed for the QMS. Objectives shall be consistent with the quality policy; be measurable or verifiable; take into account applicable requirements; be relevant to conformity of products and services and enhancement of customer satisfaction; be monitored; be communicated; and be updated as appropriate. The organization shall maintain documented information on the quality objectives. fileciteturn46file13

When planning how to achieve quality objectives, the organization shall determine what will be done, what resources will be required, who will be responsible, when it will be completed, and how results will be evaluated, including indicators for monitoring progress towards achievement of measurable objectives. fileciteturn46file13

### TERMS
- quality objective
- relevant function
- relevant level
- relevant process
- measurable
- verifiable
- applicable requirement
- conformity
- customer satisfaction
- monitor
- update
- documented information
- action
- resource
- responsibility
- completion
- result
- evaluation
- indicator
- progress

### DISTINCTIONS

**DIS-001 — QUALITY POLICY ≠ QUALITY OBJECTIVE**

Quality policy provides a framework for setting quality objectives; objectives are established at relevant functions, levels and processes.

**STATUS: CONFIRM — ISO-014 + ISO-017**

**DIS-002 — OBJECTIVE ≠ ACTION PLAN**

The objective is established first; planning to achieve it separately determines what will be done, resources, responsibility, timing and evaluation.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-003 — MEASURABLE/VERIFIABLE OBJECTIVE ≠ RESULT**

An objective must be measurable or verifiable, while results are subsequently evaluated. Measurement/verifiability is a property of the objective; result evaluation is a later management operation.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-004 — MONITORING PROGRESS ≠ EVALUATING RESULTS**

6.2.1 requires objectives to be monitored; 6.2.2 requires results to be evaluated and indicators for monitoring progress towards measurable objectives.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-005 — OBJECTIVE ≠ GENERAL INTENTION**

The Source requires objectives to be measurable or verifiable, relevant, monitored, communicated and updated as appropriate. This gives an objective an operational status beyond an unspecified intention.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-006 — RESPONSIBILITY FOR ACHIEVEMENT ≠ RESPONSIBILITY FOR SYSTEM EFFECTIVENESS**

6.2 assigns responsibility for achieving objectives; ISO-013/015 assigns accountability for QMS effectiveness to top management while distributing responsibilities among relevant roles.

**STATUS: CROSS-CLAUSE CANDIDATE / UPDATE**

### GM

**GM-001**

> Не путай цель с планом её достижения: сначала устанавливается objective, затем отдельно определяется способ её достижения — действия, ресурсы, ответственность, срок и оценка.

**GM-002**

> Делай управляемой не только цель, но и движение к ней: monitoring progress должно опираться на indicators, а достигнутые результаты — оцениваться.

### REL

**REL-001**

```text
QUALITY POLICY
        ↓
FRAMEWORK
        ↓
QUALITY OBJECTIVES
```

**STATUS: CONFIRM — ISO-014**

**REL-002**

```text
QUALITY OBJECTIVE
        ↓
WHAT WILL BE DONE
+ RESOURCES
+ RESPONSIBILITY
+ COMPLETION
+ EVALUATION
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-003**

```text
MEASURABLE OBJECTIVE
        ↓
INDICATOR
        ↓
MONITOR PROGRESS
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-004**

```text
ACTION / PLAN
        ↓
RESULT
        ↓
EVALUATION
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-005**

```text
OBJECTIVE
        ↓
RESPONSIBILITY
        ↓
ACHIEVEMENT
```

**STATUS: CANDIDATE / CROSS-CLAUSE**

### MECHANISM

**M-019 — Objective achievement planning and evaluation**

```text
QUALITY OBJECTIVE
        ↓
DEFINE WHAT WILL BE DONE
        ↓
RESOURCES
        ↓
RESPONSIBILITY
        ↓
COMPLETION TIME
        ↓
INDICATORS / MONITORING
        ↓
RESULT
        ↓
EVALUATION
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

This mechanism is distinct from M-018: risk/opportunity actions address uncertainty and potential effects; 6.2 establishes and plans achievement of defined quality objectives.

### CAPABILITY

**CAP-014 — Objective achievement management**

CMOC interpretation: ability to establish relevant, measurable/verifiable objectives, assign the means and responsibility for achieving them, monitor progress and evaluate results.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATE

**CORE-CANDIDATE-024 — Objective requires an achievement architecture**

A quality objective is not complete as a management construct without a defined way of achieving it: what will be done, resources, responsibility, completion and evaluation are determined.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-025 — Progress and result are different control objects**

Monitoring progress towards an objective and evaluating the resulting achievement are distinct management operations.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

No concrete reusable organizational implementation is prescribed.

### CHAIN

**CHAIN-CANDIDATE-007 — Objective achievement**

```text
OBJECTIVE
 ↓
PLAN
 ↓
RESOURCE
 ↓
ASSIGN RESPONSIBILITY
 ↓
EXECUTE
 ↓
MONITOR PROGRESS
 ↓
EVALUATE RESULT
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

The Source does not explicitly present these elements as a single sequential chain, so it remains a candidate.

### ROLE

**ROLE-CANDIDATE-004 — Objective responsible**

A relevant role to which responsibility for achieving the quality objective is assigned.

**STATUS: CANDIDATE / CROSS-CLAUSE**

### PHYSICAL REALIZATION

**NONE**

### DOCUMENT / DOCUMENTED INFORMATION / RECORD — SPECIAL OBSERVATION

This clause contains an important information requirement: the organization shall **maintain documented information on the quality objectives**. fileciteturn46file13

We deliberately do **not** translate this into "create a document" or "create a record". The Source says `documented information`.

This is an important continuation of the distinction tracked since ISO-013/014:

```text
QUALITY OBJECTIVE
        ↓
DOCUMENTED INFORMATION
```

but:

```text
DOCUMENTED INFORMATION
        ≠
OBJECTIVE ACHIEVEMENT
```

The exact Document / Record architecture remains deferred to Clause 7.5.

### CMOC INTERPRETATION

ISO-017 gives us a very useful construction:

```text
POLICY
 ↓
OBJECTIVE
 ↓
ACHIEVEMENT ARCHITECTURE
 ↓
RESULT
 ↓
EVALUATION
```

And inside the achievement architecture:

```text
WHAT
+
RESOURCES
+
RESPONSIBILITY
+
WHEN
+
INDICATORS
        ↓
IMPLEMENTATION
        ↓
PROGRESS
        ↓
RESULT
        ↓
EVALUATION
```

The important CMOC interpretation is:

> **A managed objective is not merely a desired future state; it requires an explicit architecture connecting intention with means, responsibility, timing, progress and evaluation.**

This is CMOC interpretation, not an ISO definition.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **5 NEW + 1 CONFIRM/UPDATE**
- GM: **2**
- REL: **5**
- MECHANISM: **M-019 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-014 CANDIDATE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **1 CHAIN-CANDIDATE**
- ROLE: **1 ROLE-CANDIDATE**
- PHYSICAL REALIZATION: NONE
- Documented information: **explicit requirement; Document/Record distinction remains open**
- CONFIRMATION: **ISO-014 policy → objectives relation confirmed; responsibility line updated from ISO-013/015**
