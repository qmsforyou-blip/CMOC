# PATCH-ISO-029

## Извещение на изменение

**0098+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 8.1 — Operational planning and control; Annex A.8.1

### SOURCE CLAIM

The organization shall plan, implement and control the processes needed to meet requirements for products and services and to implement actions determined in Clause 6. It shall do this by establishing criteria for processes, implementing control in accordance with those criteria, establishing criteria for acceptance of products and services, and determining resources needed to achieve conformity. Documented information shall be available to the extent necessary to have confidence that processes have been carried out as planned and to demonstrate conformity of products and services. The organization shall control planned changes, review consequences of unintended changes, and take action to mitigate adverse effects as necessary. Externally provided processes, products or services relevant to the QMS shall be controlled. fileciteturn77file2

Annex A.8.1 explains that product and service realization is to be carried out under controlled conditions to minimize the possibility of nonconformities or other undesirable situations occurring at each operational stage and being reflected in subsequent stages. These controlled conditions are established by applying risk-based thinking. It further explains that establishing process criteria means determining how the process is to be performed, while implementing control according to criteria means verifying that processes are actually carried out in the intended way. Documenting process criteria/procedures and evidence of conformity may be necessary. fileciteturn77file0

### TERMS
- operational planning and control
- process criteria
- process control
- acceptance criteria
- resources
- planned change
- unintended change
- adverse effect
- externally provided process
- conformity
- controlled conditions
- process realization
- risk-based thinking
- evidence of conformity

### DISTINCTIONS

**DIS-001 — PROCESS CRITERIA ≠ PROCESS CONTROL**

Establishing criteria determines how the process is to be performed; control verifies that the process is actually performed according to those criteria. fileciteturn77file0

**STATUS: NEW / SINGLE-SOURCE**

**DIS-002 — PROCESS CRITERIA ≠ ACCEPTANCE CRITERIA**

Criteria for performing the process and criteria for accepting products/services are separately required.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-003 — PLANNING ≠ IMPLEMENTATION ≠ CONTROL**

8.1 explicitly requires planning, implementation and control of processes.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-004 — PLANNED CHANGE ≠ UNINTENDED CHANGE**

Planned changes are controlled; unintended changes require review of consequences and mitigation of adverse effects.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-005 — PROCESS CONTROL ≠ RESOURCE DETERMINATION**

Control of how a process operates and determination of resources needed to achieve conformity are separate elements of the clause.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-006 — CONFIDENCE THAT PROCESS WAS CARRIED OUT AS PLANNED ≠ DEMONSTRATION OF PRODUCT/SERVICE CONFORMITY**

The clause states two distinct documented-information purposes: confidence that processes were carried out as planned and demonstration of conformity of products/services.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-007 — CONTROLLED CONDITIONS ≠ RISK-BASED THINKING**

Annex A states that controlled conditions are established by applying risk-based thinking; the two concepts are related but not identical.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-008 — EXTERNAL PROVISION ≠ EXTERNAL UNCONTROLLED ACTIVITY**

Externally provided processes/products/services relevant to the QMS remain subject to organizational control.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-009 — CONFORMITY ≠ PROCESS REALIZATION AS PLANNED**

A process can be carried out as planned while conformity is a separately demonstrated outcome; 8.1 requires documented information addressing both purposes.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### GM

**GM-001**

> Сначала определи критерии того, как процесс должен выполняться; затем контролируй фактическое выполнение относительно этих критериев.

**GM-002**

> Не смешивай criteria for process performance и acceptance criteria for product/service.

**GM-003**

> Управляй не только planned changes, но и последствиями unintended changes.

**GM-004**

> Документированная информация в operation может выполнять разные функции: давать уверенность, что процесс выполнен как запланировано, и демонстрировать conformity результата.

### REL

**REL-001**

```text
REQUIREMENTS
        ↓
PROCESS PLANNING
        ↓
PROCESS CRITERIA
        ↓
PROCESS CONTROL
        ↓
PLANNED EXECUTION
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-002**

```text
PRODUCT / SERVICE
        ↓
ACCEPTANCE CRITERIA
        ↓
ACCEPTANCE / CONFORMITY
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-003**

```text
PROCESS REQUIREMENTS
        ↓
RESOURCE NEED
        ↓
RESOURCE DETERMINATION
        ↓
CONFORMITY
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-004**

```text
PLANNED CHANGE
        ↓
CONTROL
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-005**

```text
UNINTENDED CHANGE
        ↓
REVIEW CONSEQUENCES
        ↓
ADVERSE EFFECT
        ↓
MITIGATION ACTION
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-006**

```text
PROCESS EXECUTION
        ↓
DOCUMENTED INFORMATION
        ↓
CONFIDENCE: CARRIED OUT AS PLANNED
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-007**

```text
PRODUCT / SERVICE OUTPUT
        ↓
DOCUMENTED INFORMATION
        ↓
DEMONSTRATE CONFORMITY
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-008**

```text
RISK-BASED THINKING
        ↓
CONTROLLED CONDITIONS
        ↓
MINIMIZE NONCONFORMITY / UNDESIRED SITUATIONS
```

**STATUS: NEW / SINGLE-SOURCE**

### MECHANISM

**M-034 — Operational process control**

```text
REQUIREMENTS
        ↓
PLAN PROCESS
        ↓
ESTABLISH PROCESS CRITERIA
        ↓
DETERMINE RESOURCES
        ↓
IMPLEMENT PROCESS
        ↓
CONTROL AGAINST CRITERIA
        ↓
ACCEPTANCE CRITERIA
        ↓
CONFORMITY
```

With change-control branch:

```text
PLANNED CHANGE → CONTROL

UNINTENDED CHANGE
        ↓
REVIEW CONSEQUENCES
        ↓
MITIGATE ADVERSE EFFECTS
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CAPABILITY

**CAP-029 — Operational control capability**

CMOC interpretation: ability to plan, implement and control operational processes against defined criteria, with adequate resources and acceptance criteria, while managing planned and unintended changes.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATES

**CORE-CANDIDATE-063 — Criteria precede control**

Effective process control presupposes defined criteria for how the process is to be performed; control verifies actual execution against those criteria. fileciteturn77file0

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-064 — Process execution and output conformity are distinct control objects**

8.1 separately requires confidence that processes were carried out as planned and evidence demonstrating conformity of products/services.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-065 — Change control includes unintended change consequences**

Control is not limited to planned change; unintended change triggers consequence review and mitigation.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-066 — Operational control is risk-based**

Annex A explicitly connects controlled conditions with risk-based thinking to minimize nonconformities and undesirable situations across operational stages. fileciteturn77file0

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

8.1 defines a generic operational control mechanism but does not provide a sufficiently concrete reproducible organizational implementation to qualify as a CMOC Machine.

### CHAIN

**CHAIN-CANDIDATE-028 — Operational planning and control**

```text
REQUIREMENTS
 ↓
PROCESS CRITERIA
 ↓
RESOURCE DETERMINATION
 ↓
IMPLEMENT
 ↓
CONTROL AGAINST CRITERIA
 ↓
ACCEPTANCE CRITERIA
 ↓
CONFORMITY
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-029 — Unintended change response**

```text
UNINTENDED CHANGE
 ↓
REVIEW CONSEQUENCES
 ↓
ADVERSE EFFECT
 ↓
MITIGATE
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-030 — Process execution evidence**

```text
PROCESS EXECUTION
 ↓
DOCUMENTED INFORMATION
 ↓
CONFIDENCE PROCESS WAS CARRIED OUT AS PLANNED
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

### ROLE

**NONE**

### PHYSICAL REALIZATION

**NONE**

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

8.1 provides a significant operational distinction in the use of documented information:

```text
PROCESS EXECUTION
        ↓
DOCUMENTED INFORMATION
        ↓
CONFIDENCE PROCESS WAS CARRIED OUT AS PLANNED
```

and:

```text
PRODUCT / SERVICE CONFORMITY
        ↓
DOCUMENTED INFORMATION
        ↓
DEMONSTRATE CONFORMITY
```

This does not make every such item a Record automatically. However, the second function is explicitly evidentiary and connects directly with the Clause 3.10 concept of records as evidence of results achieved. The classification of particular operational information as Record remains context-dependent.

### CMOC INTERPRETATION

8.1 is the first major operational bridge after the resource/documentation block:

```text
REQUIREMENT
        ↓
PROCESS
        ↓
CRITERIA
        ↓
CONTROL
        ↓
EXECUTION
        ↓
OUTPUT
        ↓
ACCEPTANCE / CONFORMITY
```

The critical architectural distinction is:

> **A process is not controlled merely because a procedure exists. Control means comparing/ensuring actual process execution against established criteria.**

This is directly supported by Annex A.8.1. fileciteturn77file0

A second important interpretation:

> **Operational control has two evidentiary directions: evidence that the process was carried out as planned, and evidence that the resulting product/service conforms.**

A third:

> **Change control is asymmetric: planned change is controlled in advance/through implementation, while unintended change requires consequence review and mitigation after or as it is detected.**

These are CMOC interpretations, not ISO definitions.

### CROSS-CLAUSE OBSERVATION

8.1 composes several previously extracted structures:

```text
ISO-003  PROCESS + INTERACTIONS
ISO-004  PDCA / CONTROL
ISO-016  RISKS / OPPORTUNITIES
ISO-021  INFRASTRUCTURE
ISO-022  ENVIRONMENT
ISO-023  MONITORING / MEASUREMENT
ISO-024  KNOWLEDGE
ISO-025  COMPETENCE
ISO-028  DOCUMENTED INFORMATION
        ↓
ISO-029  OPERATIONAL CONTROL
```

The new cross-clause pattern is:

```text
REQUIREMENT
 ↓
PROCESS CRITERIA
 ↓
RESOURCES / CONDITIONS
 ↓
CONTROLLED EXECUTION
 ↓
EVIDENCE
 ↓
ACCEPTANCE / CONFORMITY
```

This is a **MULTI-CONFIRMATION CANDIDATE** for a major CMOC operational architecture, but is not promoted to Core or Machine here.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **9**
- GM: **4**
- REL: **8**
- MECHANISM: **M-034 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-029 CANDIDATE**
- CORE CANDIDATES: **4**
- MACHINE: **NONE**
- CHAIN: **3 CANDIDATES**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Document / Documented information / Record: **two distinct evidentiary functions identified; Record classification remains context-dependent**
- CROSS-CLAUSE: **major operational composition of prior structures**
