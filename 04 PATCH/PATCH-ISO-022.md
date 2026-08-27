# PATCH-ISO-022

## Извещение на изменение

**0091+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 7.1.4 — Environment for the operation of processes; Annex A.7.1.4

### SOURCE CLAIM

The organization shall determine, provide and maintain the environment necessary for the operation of its processes and to achieve conformity of products and services. A suitable environment can include a combination of factors that differ depending on the products and services provided. Relevant factors can be social, psychological and physical. Some factors depend on organizational quality culture, including ethical behaviour. fileciteturn61file8

Annex A.7.1.4 clarifies that the environment is a combination of factors related to the conditions in which work is performed. Social factors can include non-discriminatory, calm and non-confrontational conditions; psychological factors can include stress reduction, burnout prevention and emotionally protective conditions; physical factors can include temperature, heat, humidity, light, airflow, hygiene and noise. The working environment can evolve with technologies and can become more complex when it is not under the direct control of the organization. fileciteturn61file2

### TERMS
- environment
- suitable environment
- social factors
- psychological factors
- physical factors
- organizational quality culture
- ethical behaviour
- working environment
- process operation
- conformity

### DISTINCTIONS

**DIS-001 — ENVIRONMENT ≠ INFRASTRUCTURE**

7.1.3 addresses infrastructure necessary for process operation; 7.1.4 separately addresses environment necessary for process operation and conformity.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-002 — ENVIRONMENT ≠ PHYSICAL CONDITIONS ONLY**

The Source explicitly includes social, psychological and physical factors.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-003 — ENVIRONMENT ≠ SINGLE FACTOR**

A suitable environment can be a combination of factors, differing according to products and services.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-004 — SUITABLE ENVIRONMENT ≠ FIXED ENVIRONMENT**

Relevant factors depend on the products and services provided and the working environment can evolve with technologies.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-005 — ENVIRONMENT ≠ FULLY UNDER ORGANIZATIONAL CONTROL**

The Annex notes that management of the working environment can become more complex when it is not under the direct control of the organization.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-006 — ENVIRONMENT ≠ QUALITY CULTURE**

Some environmental factors depend on organizational quality culture, including ethical behaviour; the two concepts are therefore related but not identical.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### GM

**GM-001**

> Определяй environment через условия, необходимые для operation процесса и достижения conformity, а не только через физические параметры рабочего места.

**GM-002**

> Рассматривай suitable environment как комбинацию релевантных факторов, состав которой зависит от продукта, услуги и процесса.

**GM-003**

> При изменении технологий пересматривай условия рабочей среды, особенно если они находятся не под прямым контролем организации.

### REL

**REL-001**

```text
PROCESS OPERATION
        ↓
ENVIRONMENT NEED
        ↓
DETERMINE + PROVIDE + MAINTAIN
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-002**

```text
ENVIRONMENT
        ↓
SOCIAL + PSYCHOLOGICAL + PHYSICAL FACTORS
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-003**

```text
ENVIRONMENT
        ↓
PROCESS OPERATION
        ↓
CONFORMITY
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-004**

```text
TECHNOLOGY CHANGE
        ↓
WORKING ENVIRONMENT EVOLVES
        ↓
MANAGEMENT COMPLEXITY
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-005**

```text
QUALITY CULTURE
        ↓
SOME ENVIRONMENTAL FACTORS
        ↓
ETHICAL BEHAVIOUR
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MECHANISM

**M-027 — Process-environment suitability management**

```text
PROCESS NEED
        ↓
DETERMINE RELEVANT ENVIRONMENTAL FACTORS
        ↓
PROVIDE
        ↓
MAINTAIN
        ↓
PROCESS OPERATION
        ↓
CONFORMITY
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CAPABILITY

**CAP-022 — Operating-environment adequacy capability**

CMOC interpretation: ability to determine, provide and maintain the combination of environmental conditions necessary for effective process operation and conformity.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATE

**CORE-CANDIDATE-036 — Environment is function/process-dependent**

The suitable environment is determined by what is necessary for operation of processes and achievement of conformity; its relevant factors can differ according to products and services.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-037 — Operating environment is multidimensional**

The environment relevant to process operation can combine social, psychological and physical factors.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

The clause defines conditions to be provided and maintained but does not specify a concrete reproducible organizational realization.

### CHAIN

**CHAIN-CANDIDATE-014 — Environment suitability**

```text
PROCESS NEED
 ↓
DETERMINE FACTORS
 ↓
PROVIDE
 ↓
MAINTAIN
 ↓
PROCESS OPERATION
 ↓
CONFORMITY
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

### ROLE

**NONE**

### PHYSICAL REALIZATION

**NONE**

The Source gives examples of environmental factors, not a specific CMOC physical realization.

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

**NONE**

Clause 7.1.4 does not itself require documented information.

### CMOC INTERPRETATION

ISO-022 creates a useful boundary with ISO-021:

```text
INFRASTRUCTURE
        ↓
WHAT ENABLES PROCESS OPERATION

ENVIRONMENT
        ↓
CONDITIONS IN WHICH PROCESS OPERATION OCCURS
```

The Source does not itself formulate this as a CMOC ontology distinction; it is a CMOC interpretation based on the separate requirements of 7.1.3 and 7.1.4.

A broader structure now appears:

```text
FUNCTION / PROCESS NEED
        ↓
REQUIRED RESOURCE / CONDITION
        ↓
REALIZATION
        ↓
PROCESS OPERATION
        ↓
CONFORMITY / RESULT
```

This remains a **MULTI-CONFIRMATION CANDIDATE**.

### CROSS-CLAUSE OBSERVATION

ISO-021 and ISO-022 both use the pattern `determine → provide → maintain`, but they refer to different categories: infrastructure versus environment. This repeated structure strengthens the candidate for a generic resource/condition management mechanism, while the category distinction must be preserved.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **6 NEW**
- GM: **3**
- REL: **5**
- MECHANISM: **M-027 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-022 CANDIDATE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **1 CANDIDATE**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Document / Documented information / Record: **no new requirement**
- CROSS-CLAUSE: **ISO-021 boundary infrastructure ↔ environment; generic determine/provide/maintain pattern strengthened**
