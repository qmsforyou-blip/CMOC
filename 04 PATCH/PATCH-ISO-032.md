# PATCH-ISO-032

## Извещение на изменение

**0101+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 8.4 — Control of externally provided processes, products and services; 8.4.1–8.4.3; Annex A.8.4

### SOURCE CLAIM

The organization shall ensure that externally provided processes, products and services conform to requirements. Controls are required when external provision is incorporated into the organization’s own products/services, provided directly to customers on behalf of the organization, or when a process or part of a process is provided externally as a result of an organizational decision. External providers are evaluated, selected, monitored and re-evaluated against their ability to provide conforming processes, products or services; documented information is evidence of these activities and necessary actions. fileciteturn84file9

Externally provided processes shall remain within the control of the organization’s quality management system. The organization defines controls applied to the external provider and to the resulting output, considers potential impact and effectiveness of provider controls, and determines verification or other activities necessary to ensure requirements are met. fileciteturn84file9

Before communicating requirements to an external provider, the organization shall ensure their adequacy. Requirements communicated can concern the processes/products/services, approval of products/services and methods/processes/equipment, release, competence and qualifications, provider interactions, provider-performance monitoring/control, and verification/validation activities at the provider’s premises. fileciteturn84file4

Annex A.8.4 states that the organization remains responsible for ensuring externally provided processes, products and services conform to requirements. External provision can occur through purchasing from a supplier, an arrangement with an associate company, or externally provided processes. The controls can vary according to the nature of provision; risk-based thinking can determine type and extent of control, while opportunity-based thinking can identify improvements through the supply chain. fileciteturn84file5

### TERMS
- externally provided process
- external provider
- externally provided product/service
- evaluation
- selection
- monitoring of performance
- re-evaluation
- type and extent of control
- resulting output
- provider controls
- verification
- external provider requirements
- approval
- release
- competence / qualification
- interaction
- supply chain

### DISTINCTIONS

**DIS-001 — EXTERNAL PROVISION ≠ LOSS OF QMS CONTROL**

An externally provided process remains within the control of the organization’s quality management system.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-002 — EXTERNAL PROVIDER ≠ EXTERNALIZED RESPONSIBILITY FOR CONFORMITY**

The organization remains responsible for ensuring externally provided processes, products and services conform to requirements.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-003 — PROVIDER CONTROL ≠ OUTPUT CONTROL**

The organization defines both controls applied to the external provider and controls applied to the resulting output.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-004 — PROVIDER ABILITY ≠ PROVIDER EVALUATION**

Ability to provide conforming provision is the basis for evaluation/selection/monitoring/re-evaluation; the evaluation activity is not identical to the ability itself.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-005 — EVALUATION ≠ SELECTION ≠ MONITORING ≠ RE-EVALUATION**

The four activities are explicitly distinguished in 8.4.1.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-006 — REQUIREMENT ADEQUACY ≠ REQUIREMENT COMMUNICATION**

The organization shall ensure adequacy of requirements before communicating them to the external provider.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-007 — TYPE OF CONTROL ≠ EXTENT OF CONTROL**

The controls selected and their extent are determined according to the particular external provision and its impact.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-008 — PROVIDER CONTROL EFFECTIVENESS ≠ ORGANIZATION’S CONTROL**

The organization considers the effectiveness of controls applied by the external provider when determining its own controls.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-009 — EXTERNALLY PROVIDED PROCESS ≠ PURCHASED PRODUCT**

8.4 covers purchasing, associate-company arrangements and processes provided externally; these are different forms of external provision.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-010 — EXTERNAL PROVIDER ≠ EXTERNAL PROCESS**

The provider is the external actor/source; the externally provided process is the process or part of process being provided. They are related but not identical entities.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-011 — VERIFICATION OF EXTERNAL PROVISION ≠ CONTROL OF EXTERNAL PROVISION**

Verification is one activity within the broader control architecture.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-012 — RISK-BASED CONTROL ≠ UNIFORM CONTROL**

The type and extent of controls can vary according to nature, impact and provider-control effectiveness.

**STATUS: NEW / SINGLE-SOURCE**

### GM

**GM-001**

> Передавая процесс наружу, не передавай вместе с ним управленческий контроль: externally provided process остаётся в пределах QMS control.

**GM-002**

> Оценивай external provider не только при выборе: контролируй performance и предусматривай re-evaluation.

**GM-003**

> Разделяй controls над provider и controls над resulting output.

**GM-004**

> Перед передачей требований external provider сначала проверь их adequacy.

**GM-005**

> Type and extent of control определяй с учётом impact, provider-control effectiveness и risk.

### REL

**REL-001**

```text
EXTERNAL PROVISION
        ↓
QMS CONTROL
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-002**

```text
PROVIDER ABILITY
        ↓
EVALUATION
        ↓
SELECTION
        ↓
MONITORING
        ↓
RE-EVALUATION
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-003**

```text
EXTERNAL PROVIDER
        ↓
PROVIDER CONTROLS
        ↓
RESULTING OUTPUT
        ↓
ORGANIZATION CONTROL / VERIFICATION
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-004**

```text
POTENTIAL IMPACT
+
PROVIDER CONTROL EFFECTIVENESS
        ↓
TYPE / EXTENT OF ORGANIZATIONAL CONTROL
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-005**

```text
REQUIREMENTS
        ↓
ADEQUACY CHECK
        ↓
COMMUNICATION TO EXTERNAL PROVIDER
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-006**

```text
EXTERNAL PROVIDER REQUIREMENTS
        ↓
PROCESS / PRODUCT / SERVICE
APPROVAL / RELEASE
COMPETENCE
INTERACTIONS
PERFORMANCE CONTROL
VERIFICATION / VALIDATION
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-007**

```text
RISK-BASED THINKING
        ↓
TYPE / EXTENT OF CONTROL
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-008**

```text
EXTERNAL PROVISION
        ↓
SUPPLY CHAIN
        ↓
OPPORTUNITY FOR IMPROVEMENT
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MECHANISM

**M-037 — External provision control**

```text
EXTERNAL PROVISION IDENTIFIED
        ↓
DETERMINE NEED FOR CONTROL
        ↓
EVALUATE / SELECT PROVIDER
        ↓
DEFINE TYPE / EXTENT OF CONTROL
        ├── PROVIDER
        └── RESULTING OUTPUT
        ↓
COMMUNICATE ADEQUATE REQUIREMENTS
        ↓
MONITOR PROVIDER PERFORMANCE
        ↓
VERIFY / OTHERWISE ENSURE CONFORMITY
        ↓
RE-EVALUATE PROVIDER
```

Control intensity branch:

```text
POTENTIAL IMPACT
+
EFFECTIVENESS OF PROVIDER CONTROLS
+
RISK
        ↓
TYPE / EXTENT OF CONTROL
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CAPABILITY

**CAP-032 — External provision control capability**

CMOC interpretation: ability to retain external provision within organizational control, select and evaluate providers, determine proportionate controls, communicate adequate requirements, verify outputs and monitor/re-evaluate provider performance.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATES

**CORE-CANDIDATE-076 — Externalization does not remove the process from control**

An externally provided process remains within the control of the organization’s QMS.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-077 — Control has two targets: provider and output**

The organization defines controls for both the external provider and resulting output.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-078 — Control intensity is contextual**

Type and extent of control depend on potential impact, provider-control effectiveness and risk.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-079 — Requirement adequacy precedes external communication**

The organization checks adequacy of requirements before communicating them to an external provider.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

8.4 provides a reproducible management mechanism, but does not specify a concrete organizational construction sufficient to qualify as a CMOC Machine.

### CHAIN

**CHAIN-CANDIDATE-037 — External-provider control cycle**

```text
PROVIDER ABILITY
 ↓
EVALUATION
 ↓
SELECTION
 ↓
CONTROL / MONITORING
 ↓
RE-EVALUATION
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-038 — Proportionate control**

```text
POTENTIAL IMPACT
+
PROVIDER CONTROL EFFECTIVENESS
+
RISK
 ↓
TYPE / EXTENT OF CONTROL
 ↓
PROVIDER + OUTPUT CONTROL
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-039 — Requirement communication to external provider**

```text
REQUIREMENT
 ↓
ADEQUACY CHECK
 ↓
COMMUNICATION
 ↓
EXTERNAL PROVIDER
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

### ROLE

**NONE**

The clause assigns organizational obligations but does not establish a distinct CMOC Role.

### PHYSICAL REALIZATION

**NONE**

Purchasing, associate-company arrangements and external processes are forms of external provision, not yet physical realizations of a CMOC Machine.

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

8.4.1 explicitly requires documented information as evidence of evaluation, selection, monitoring of performance and re-evaluation of external providers, including necessary actions. fileciteturn84file9

This reinforces the ISO-028 distinction:

```text
EXTERNAL PROVIDER ACTIVITY
        ↓
EVALUATION / MONITORING / RE-EVALUATION
        ↓
DOCUMENTED INFORMATION
        ↓
EVIDENCE
```

The Source supports evidentiary function, but does not require us to classify every such documented information item as Record automatically.

### CMOC INTERPRETATION

The strongest architectural finding is:

> **Внешний исполнитель не является внешним по отношению к контуру управления, если организация передала ему процесс: процесс остаётся внутри управленческой границы QMS, хотя выполнение происходит за пределами прямой организационной структуры.**

This is CMOC interpretation based directly on 8.4.2(a).

A second important interpretation:

```text
EXTERNAL PROVIDER
        ↓
EXTERNAL ACTIVITY / PROCESS
        ↓
RESULTING OUTPUT
        ↓
ORGANIZATIONAL CONFORMITY
```

The organization retains responsibility for conformity even when execution is external.

A third:

```text
CONTROL
   ≠
CONTROL OF PROVIDER ONLY
```

Control has at least two targets:

```text
PROVIDER
+
RESULTING OUTPUT
```

This is explicitly supported by 8.4.2(b). fileciteturn84file9

A fourth:

> **Граница организации и граница управления — не одно и то же.**

This is a particularly promising CMOC candidate, but remains a CMOC interpretation requiring confirmation by later clauses and independent sources.

### CROSS-CLAUSE OBSERVATION

ISO-029 established operational control inside the organization. ISO-032 now extends the control architecture across an organizational boundary:

```text
ISO-029
PROCESS
 ↓
CRITERIA
 ↓
CONTROL

ISO-032
EXTERNAL PROCESS
 ↓
PROVIDER
 ↓
CONTROL
 ↓
OUTPUT
 ↓
CONFORMITY
```

Combined candidate:

```text
REQUIREMENT
 ↓
PROCESS
 ↓
CONTROL
 ├── INTERNAL EXECUTION
 └── EXTERNAL PROVISION
          ↓
       PROVIDER
          ↓
       OUTPUT
          ↓
      CONFORMITY
```

**MULTI-CONFIRMATION CANDIDATE** — not yet Core/Canon/Chain.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **12**
- GM: **5**
- REL: **8**
- MECHANISM: **M-037 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-032 CANDIDATE**
- CORE CANDIDATES: **4**
- MACHINE: **NONE**
- CHAIN: **3 CANDIDATES**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Document / Documented information / Record: **evaluation/selection/monitoring/re-evaluation evidence explicitly documented; automatic Record classification not made**
- CROSS-CLAUSE: **external provision extends operational control beyond the direct organizational boundary**
