# PATCH-ISO-012

## Извещение на изменение

**0081+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 4.4 — Quality management system; 4.4.1–4.4.2

### SOURCE CLAIM

The organization shall establish, implement, maintain and continually improve a quality management system, including the processes needed and their interactions, in accordance with the requirements of the document.

The organization shall determine the processes needed for the QMS and their application throughout the organization, including:

a) inputs required and outputs expected;
b) sequence and interaction of processes;
c) criteria and methods, including monitoring, measurements and related performance indicators, needed for effective operation and control;
d) resources needed and their availability;
e) responsibilities and authorities;
f) risks and opportunities according to 6.1;
g) evaluation of processes and implementation of changes needed to ensure intended results;
h) improvement of processes and the QMS.

Documented information shall be available to the extent necessary to support operation of processes and as evidence that processes are carried out as planned. fileciteturn43file2

Annex A.4.4 states that the process approach incorporates PDCA and risk-based and opportunity-based thinking. Processes interact and interrelate to create an aligned QMS. It is important to determine sequence, interaction and integration of QMS processes with each other and with other business processes; define inputs and intended results; and assign responsibilities and authorities. Process evaluation concerns continuing adequacy and effectiveness. Because contextual factors can change, the organization needs the ability to modify processes and their interactions, partially or totally, in a timely and controlled manner. Documented information can provide evidence that processes are carried out as planned, but is not automatically necessary for every requirement; the organization determines which processes need documented information and its type and degree of detail. fileciteturn42file0

### TERMS
- process
- process interaction
- process sequence
- input
- output
- intended result
- criteria
- method
- monitoring
- measurement
- performance indicator
- resource
- responsibility
- authority
- risk
- opportunity
- evaluation
- change
- documented information
- effective operation
- control
- continual improvement

### DISTINCTIONS

**DIS-001 — PROCESS ≠ ISOLATED ACTIVITY**

The QMS is explicitly established as including needed processes and their interactions. The process is therefore treated as an element within an interacting system, not merely as an isolated activity.

**STATUS: CANDIDATE / 1 source; reinforced by ISO-003**

**DIS-002 — PROCESS ≠ PROCESS SYSTEM**

A process has its own inputs and expected outputs, while the QMS contains multiple processes and their sequence/interactions.

**STATUS: CANDIDATE / 1 source; reinforced by ISO-003**

**DIS-003 — PROCESS SEQUENCE ≠ PROCESS INTERACTION**

Clause 4.4 requires both to be determined separately.

**STATUS: CANDIDATE / 1 source**

**DIS-004 — PROCESS CONTROL ≠ PROCESS EVALUATION**

Criteria/methods are used for effective operation and control; processes are separately evaluated for achievement of intended results and continuing adequacy/effectiveness.

**STATUS: CANDIDATE / 1 source**

**DIS-005 — PROCESS OPERATION ≠ PROCESS IMPROVEMENT**

The clause separately requires support/control of operation and improvement of processes and the QMS.

**STATUS: CANDIDATE / 1 source**

**DIS-006 — DOCUMENTED INFORMATION ≠ MANDATORY DOCUMENTATION OF EVERY PROCESS**

4.4.2 requires documented information only to the extent necessary to support operation and provide evidence that processes are carried out as planned. Annex A.4.4 states the organization determines which processes are supported/accompanied by documented information and its type and detail. fileciteturn42file0

**STATUS: CANDIDATE / 1 source**

**DIS-007 — PROCESS CHANGE ≠ UNCONTROLLED CHANGE**

Annex A.4.4 states that modification of processes and interactions may be needed because context changes, but such modification is to occur in a timely and controlled manner. fileciteturn42file0

**STATUS: CANDIDATE / 1 source**

### GM

**GM-001**

> Описывай управляемый процесс через вход, ожидаемый результат, последовательность и взаимодействия, критерии и методы управления, ресурсы и ответственность.

**GM-002**

> Управляй не только отдельными процессами, но и их взаимодействиями как системой.

**GM-003**

> Оценивай процессы по достижению intended results и поддерживай возможность своевременно и контролируемо изменять процессы и их взаимодействия.

**GM-004**

> Фиксируй процессную информацию только в той степени, в которой она необходима для работы процесса и свидетельства выполнения запланированного.

### REL

**REL-001**

```text
QMS
  ↓
PROCESSES + INTERACTIONS
  ↓
ALIGNED QMS
```

**STATUS: CANDIDATE / 1 source**

**REL-002**

```text
INPUTS
  ↓
PROCESS
  ↓
EXPECTED OUTPUT / INTENDED RESULT
```

**STATUS: CANDIDATE / 1 source; reinforces ISO-003 and ISO-008**

**REL-003**

```text
PROCESS A OUTPUT
       ↓
PROCESS B INPUT
```

This follows the process-system relation already identified in ISO-003 and is consistent with the definition of process in Clause 3. fileciteturn42file10

**STATUS: CONFIRM / UPDATE**

**REL-004**

```text
CRITERIA + METHODS
        ↓
EFFECTIVE OPERATION + CONTROL
```

**STATUS: CANDIDATE / 1 source**

**REL-005**

```text
PROCESS
  ↓
EVALUATION
  ↓
CHANGE AS NEEDED
  ↓
INTENDED RESULTS
```

**STATUS: CANDIDATE / 1 source**

**REL-006**

```text
DOCUMENTED INFORMATION
        ↓
PROCESS OPERATION SUPPORT
        +
EVIDENCE OF PLANNED EXECUTION
```

**STATUS: CANDIDATE / 1 source**

### MECHANISM

**M-013 — Process system establishment and control**

The Source provides a substantially complete management mechanism:

```text
DETERMINE PROCESSES
        ↓
INPUTS + OUTPUTS
        ↓
SEQUENCE + INTERACTIONS
        ↓
CRITERIA + METHODS
        ↓
RESOURCES
        ↓
RESPONSIBILITIES + AUTHORITIES
        ↓
RISKS + OPPORTUNITIES
        ↓
EVALUATE
        ↓
CHANGE AS NEEDED
        ↓
IMPROVE
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

This is stronger than earlier mechanisms because Clause 4.4 explicitly specifies the elements that must be determined and managed. Nevertheless, the Source does not prescribe one concrete organizational implementation, so it remains M rather than Machine.

### CAPABILITY

**CAP-009 — Ability to establish, operate, evaluate and improve an interacting process system**

CMOC interpretation: the organization needs the ability to define the processes required for the QMS, control their interactions, provide resources and responsibilities, evaluate achievement of intended results, and modify/improve the process system when needed.

**STATUS: CANDIDATE / 1 source**

### CORE CANDIDATE

**CORE-CANDIDATE-013 — Process system as an engineered object**

The QMS is not merely a collection of named processes. It is an interacting process system whose inputs, outputs, sequence, interactions, criteria, resources, responsibilities, risks, evaluation and changes are deliberately determined.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-014 — Controlled modifiability of process system**

A process system must be capable of timely and controlled modification when contextual factors change, while preserving achievement of intended results. fileciteturn42file0

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

The clause defines the architecture and management mechanism of the process system, but not a concrete reusable implementation. A procedure, process map or software workflow would be a possible realization only if the Source later provides enough structure to justify a Machine.

### CHAIN

**CHAIN-CANDIDATE-004 — Process control/evaluation loop**

```text
PROCESS
  ↓
CONTROL / OPERATION
  ↓
EVALUATION
  ↓
CHANGE AS NEEDED
  ↓
INTENDED RESULT
  ↓
IMPROVEMENT
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

Do not promote to MACHINE-CHAIN yet. The Source clearly establishes these management requirements, but does not present the above exact sequence as one execution chain.

### ROLE

**NONE**

Responsibilities and authorities are required, but no sufficiently specified role pattern is established in this clause.

### PHYSICAL REALIZATION

**NONE**

### CMOC INTERPRETATION

ISO-012 is a major architectural step. Clauses 4.1–4.3 established:

```text
CONTEXT
  ↓
RELEVANCE
  ↓
REQUIREMENTS
  ↓
SCOPE / BOUNDARY
```

Clause 4.4 now fills that boundary with an engineered process system:

```text
QMS SCOPE
    ↓
PROCESSES
    ↓
INPUTS / OUTPUTS
    ↓
SEQUENCE / INTERACTIONS
    ↓
CRITERIA / METHODS / MEASUREMENT
    ↓
RESOURCES
    ↓
RESPONSIBILITIES / AUTHORITIES
    ↓
RISKS / OPPORTUNITIES
    ↓
EVALUATION
    ↓
CONTROLLED CHANGE
    ↓
IMPROVEMENT
```

The strongest new CMOC hypothesis is therefore:

> **Process can be treated as an engineered object of management, and the process system as an engineered object of management.**

This is CMOC interpretation, not an ISO term.

A second important result is the explicit distinction between **operation and evidence of operation**. Documented information is selected according to what is necessary to support operation and provide evidence; the amount of documentation itself is not the measure of effectiveness. fileciteturn42file0

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **7 CANDIDATES**
- GM: **4**
- REL: **6**
- MECHANISM: **M-013 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-009 CANDIDATE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **1 CHAIN-CANDIDATE**
- ROLE: NONE
- PHYSICAL REALIZATION: NONE
- CONFIRMATION: **SINGLE-SOURCE — ISO/DIS 9001:2025; selected relations reinforce ISO-003/008**
