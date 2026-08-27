# PATCH-ISO-008

## Извещение на изменение

**0077+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 3 — Terms and definitions

### SOURCE CLAIM

Clause 3 states that, for this document, the terms and definitions given in ISO/CD 9000 apply, including the terms defined in Clause 3 of ISO/DIS 9001. The clause defines organization, interested party, top management, management system, quality management system, policy, quality policy, objective, quality objective, risk, process, competence, documented information, performance, continual improvement, effectiveness, requirement, conformity, nonconformity, corrective action and audit. fileciteturn24file11turn25file15

### TERMS

Core terminology extracted for CMOC consideration:
- organization
- interested party / stakeholder
- top management
- management system
- quality management system
- policy
- quality policy
- objective / quality objective
- risk
- process
- competence
- documented information
- performance
- continual improvement
- effectiveness
- requirement
- conformity
- nonconformity
- corrective action
- audit

### DISTINCTIONS

**DIS-001 — ORGANIZATION ≠ MANAGEMENT SYSTEM**

The organization is the person or group with functions, responsibilities, authorities and relationships to achieve objectives; the management system is a set of interrelated or interacting elements of the organization established to set policies/objectives and processes to achieve objectives. fileciteturn24file11

**STATUS: CANDIDATE / 1 source**

**DIS-002 — MANAGEMENT SYSTEM ≠ QUALITY MANAGEMENT SYSTEM**

The quality management system is defined as a part of the management system related to quality. fileciteturn24file11

**STATUS: CANDIDATE / 1 source**

**DIS-003 — OBJECTIVE ≠ QUALITY OBJECTIVE**

An objective is a result to be achieved; a quality objective is an objective related to quality. Quality objectives are generally specified for relevant functions, levels and processes. fileciteturn25file15

**STATUS: CANDIDATE / 1 source**

**DIS-004 — RISK ≠ ONLY NEGATIVE CONSEQUENCE**

Risk is defined as the effect of uncertainty; the effect may be positive or negative. fileciteturn25file15

**STATUS: CANDIDATE / 1 source**

**DIS-005 — PROCESS ≠ ACTIVITY**

A process is a set of interrelated or interacting activities that uses or transforms inputs to deliver a result. fileciteturn25file15

**STATUS: CANDIDATE / 1 source**

**DIS-006 — DOCUMENTED INFORMATION ≠ DOCUMENT ONLY**

Documented information includes both information required to be controlled and maintained and the medium on which it is contained; it can refer to documentation and records as distinct uses. fileciteturn21file15

**STATUS: CANDIDATE / 1 source**

**DIS-007 — PERFORMANCE ≠ EFFECTIVENESS**

Performance is a measurable result; effectiveness is the extent to which planned activities are realized and planned results are achieved. fileciteturn21file15

**STATUS: CANDIDATE / 1 source**

**DIS-008 — CONFORMITY ≠ NONCONFORMITY**

Conformity is fulfilment of a requirement; nonconformity is non-fulfilment of a requirement. fileciteturn21file15

**STATUS: CANDIDATE / 1 source**

**DIS-009 — CORRECTIVE ACTION ≠ CORRECTION**

Corrective action is defined as action to eliminate cause(s) of a nonconformity and prevent recurrence. The definition distinguishes its purpose from merely dealing with the existing nonconforming condition. fileciteturn21file15

**STATUS: CANDIDATE / 1 source**

**DIS-010 — COMPETENCE ≠ KNOWLEDGE / SKILLS**

Competence is the ability to apply knowledge and skills to achieve intended results. fileciteturn25file15

**STATUS: CANDIDATE / 1 source**

### GM

**GM-001**

> Рассматривай организацию как объект, а management system — как организованное множество взаимосвязанных элементов этой организации, предназначенное для достижения целей.

**GM-002**

> Рассматривай requirement как основание для последующей проверки conformity / nonconformity.

**GM-003**

> Разделяй результат, выполнение запланированного и соответствие требованию: performance, effectiveness и conformity — разные понятия.

**GM-004**

> Рассматривай competence как способность применять knowledge и skills для достижения intended results, а не как наличие знаний само по себе.

### REL

**REL-001**

```text
ORGANIZATION
    ↓
MANAGEMENT SYSTEM
    ↓
POLICIES + OBJECTIVES + PROCESSES
    ↓
OBJECTIVES ACHIEVEMENT
```

**STATUS: CANDIDATE / 1 source**

**REL-002**

```text
MANAGEMENT SYSTEM
    ↓
QUALITY MANAGEMENT SYSTEM
```

QMS — part of management system related to quality. fileciteturn24file11

**STATUS: CANDIDATE / 1 source**

**REL-003**

```text
INPUTS
  ↓
PROCESS
  ↓
RESULT
```

Process uses or transforms inputs to deliver a result; inputs are generally outputs of other processes and outputs generally inputs to other processes. fileciteturn25file15

**STATUS: CANDIDATE / 1 source**

**REL-004**

```text
REQUIREMENT
   ↓
CONFORMITY / NONCONFORMITY
```

Conformity and nonconformity are defined respectively as fulfilment and non-fulfilment of a requirement. fileciteturn21file15

**STATUS: CANDIDATE / 1 source**

**REL-005**

```text
NONCONFORMITY
   ↓
CAUSE(S)
   ↓
CORRECTIVE ACTION
   ↓
PREVENT RECURRENCE
```

This is directly encoded in the definition of corrective action. fileciteturn21file15

**STATUS: CANDIDATE / 1 source**

**REL-006**

```text
KNOWLEDGE + SKILLS
        ↓
COMPETENCE
        ↓
INTENDED RESULTS
```

**STATUS: CANDIDATE / 1 source**

### MECHANISM

**M-008 — Corrective action as a causal prevention mechanism**

The definition itself contains an action mechanism: identify/eliminate the cause(s) of a nonconformity and prevent recurrence. fileciteturn21file15

**CLASS: M**

**STATUS: CANDIDATE / 1 source**

Boundary: this is a mechanism definition, not yet a Machine. The definition does not specify a complete reproducible organizational implementation.

**M-009 — Audit as evidence acquisition and objective evaluation mechanism**

An audit is defined as a systematic and independent process for obtaining evidence and evaluating it objectively to determine the extent to which audit criteria are fulfilled. fileciteturn21file15

**CLASS: M**

**STATUS: CANDIDATE / 1 source**

### CAPABILITY

**CAP-005 — Competence**

Ability to apply knowledge and skills to achieve intended results. fileciteturn25file15

**STATUS: CANDIDATE / 1 source**

Note: this is a direct Source definition; no broader CMOC capability is inferred beyond it.

### CORE CANDIDATE

**CORE-CANDIDATE-005 — Requirement as basis of conformity judgement**

The Source defines conformity as fulfilment of a requirement and nonconformity as non-fulfilment of a requirement. This gives a compact structural basis for the relation:

```text
REQUIREMENT
    ↓
FULFILMENT / NON-FULFILMENT
    ↓
CONFORMITY / NONCONFORMITY
```

**STATUS: CANDIDATE / 1 source**

**CORE-CANDIDATE-006 — Management system as interrelated organizational elements**

A management system is not identified with a document set or a single process; it is defined as interrelated/interacting organizational elements used to establish policies/objectives and processes to achieve objectives. fileciteturn24file11

**STATUS: CANDIDATE / 1 source**

### MACHINE

**NONE**

Definitions of corrective action and audit expose mechanisms, but Clause 3 does not provide enough evidence of concrete reproducible organizational realizations to create Machines.

### CHAIN

**CHAIN-CANDIDATE-003**

```text
INPUT → PROCESS → RESULT
```

The Source explicitly defines process through use/transformation of inputs to deliver a result and states that process outputs generally become inputs to other processes. fileciteturn25file15

**STATUS: CANDIDATE / SINGLE-SOURCE**

The other relations are not promoted to Chains because the definitions do not necessarily assert execution sequences.

### ROLE

**NONE**

Top management is defined, but Clause 3 alone does not provide a role pattern/action structure sufficient for a ROLE candidate beyond the Entity/Role term itself.

### PHYSICAL REALIZATION

**NONE**

### CMOC INTERPRETATION

Clause 3 is not merely a glossary. It provides a compact ontology of the objects and relations on which the normative body operates.

The strongest extraction is a structural triad:

```text
REQUIREMENT
    ↓
CONFORMITY / NONCONFORMITY
```

and:

```text
INPUT
    ↓
PROCESS
    ↓
RESULT
```

plus the system-level construction:

```text
ORGANIZATION
    ↓
INTERRELATED ELEMENTS
    ↓
MANAGEMENT SYSTEM
    ↓
OBJECTIVES
```

This is CMOC interpretation, not a claim that ISO uses the CMOC ontology.

A particularly important candidate is the distinction between **performance** (measurable result) and **effectiveness** (degree of realization of planned activities and planned results). fileciteturn21file15

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **10 CANDIDATES**
- GM: **4**
- REL: **6 CANDIDATES**
- MECHANISM: **M-008, M-009 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-005 NEW / SINGLE-SOURCE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **CHAIN-CANDIDATE-003**
- ROLE: NONE
- PHYSICAL REALIZATION: NONE
- CONFIRMATION: **1 source — ISO/DIS 9001:2025**
