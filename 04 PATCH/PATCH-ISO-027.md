# PATCH-ISO-027

## Извещение на изменение

**0096+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 7.4 — Communication; Annex A.7.4

### SOURCE CLAIM

The organization shall determine the internal and external communications relevant to the quality management system, including: what it will communicate; when to communicate; with whom to communicate; how to communicate; and who communicates. fileciteturn71file0

Annex A.7.4 explicitly describes communication as a process involving objectives, inputs, outputs, tools and content, responsibilities and resources, risks and opportunities, and internal and external feedback relevant to the quality management system. Effective communication processes provide the ability to transmit and receive information quickly and act on it, build trust between relevant parties, communicate the importance of customer satisfaction and process performance, and determine opportunities for improvement. Communication can sometimes occur without human intervention when two or more devices interact. fileciteturn71file11turn71file13

### TERMS
- communication
- internal communication
- external communication
- objectives
- inputs
- outputs
- tools
- content
- responsibilities
- resources
- risks
- opportunities
- feedback
- transmit
- receive
- act on information
- relevant party
- human intervention

### DISTINCTIONS

**DIS-001 — COMMUNICATION ≠ TRANSMISSION ONLY**

Annex A describes communication as including transmitting and receiving information and acting on it; communication is not reduced to one-way transmission.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-002 — INTERNAL COMMUNICATION ≠ EXTERNAL COMMUNICATION**

Clause 7.4 explicitly requires determination of both internal and external communications relevant to the QMS.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-003 — WHAT ≠ WHEN ≠ WITH WHOM ≠ HOW ≠ WHO**

The Source identifies five distinct dimensions for determining communication.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-004 — COMMUNICATION ≠ INFORMATION**

Information is what is communicated; communication is the process through which information is transmitted/received and acted upon.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-005 — COMMUNICATION ≠ HUMAN INTERACTION**

Communication can occur without human intervention when devices interact.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-006 — COMMUNICATION ≠ MESSAGE / CONTENT**

Annex A identifies content as one component of a communication process alongside objectives, inputs, outputs, tools, responsibilities, resources, risks, opportunities and feedback.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-007 — COMMUNICATION PROCESS ≠ COMMUNICATION CHANNEL / TOOL**

Tools are components of the communication process, not the process itself.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-008 — FEEDBACK ≠ ONE-WAY COMMUNICATION**

Internal and external feedback relevant to the QMS is explicitly included in the communication process.

**STATUS: NEW / SINGLE-SOURCE**

### GM

**GM-001**

> Проектируй communication как процесс, а не как рассылку сообщений: определяй objective, input, output, content, tools, responsibilities, resources, risks, opportunities и feedback.

**GM-002**

> Для каждой существенной коммуникации явно определяй пять параметров: what, when, with whom, how, who.

**GM-003**

> Проверяй communication по способности не только передавать и получать information, но и обеспечивать действие по ней.

**GM-004**

> Не предполагай наличие человека в каждом communication loop: устройства могут взаимодействовать без human intervention.

### REL

**REL-001**

```text
QMS RELEVANCE
      ↓
INTERNAL / EXTERNAL COMMUNICATION
      ↓
WHAT / WHEN / WITH WHOM / HOW / WHO
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-002**

```text
COMMUNICATION PROCESS
├── OBJECTIVES
├── INPUTS
├── OUTPUTS
├── TOOLS
├── CONTENT
├── RESPONSIBILITIES
├── RESOURCES
├── RISKS / OPPORTUNITIES
└── FEEDBACK
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-003**

```text
TRANSMIT
   ↓
RECEIVE
   ↓
ACT ON INFORMATION
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-004**

```text
COMMUNICATION
      ↓
TRUST BETWEEN RELEVANT PARTIES
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-005**

```text
CUSTOMER SATISFACTION / PROCESS PERFORMANCE
      ↓
COMMUNICATION
      ↓
AWARENESS / UNDERSTANDING
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-006**

```text
COMMUNICATION
      ↓
FEEDBACK
      ↓
OPPORTUNITIES FOR IMPROVEMENT
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-007**

```text
DEVICE
  ↕
DEVICE
```

**STATUS: NEW / SINGLE-SOURCE**

This relation is included because Annex A explicitly recognizes communication without human intervention.

### MECHANISM

**M-032 — Communication-to-action mechanism**

```text
QMS RELEVANCE
      ↓
DEFINE COMMUNICATION
      ↓
WHAT / WHEN / WITH WHOM / HOW / WHO
      ↓
TRANSMIT
      ↓
RECEIVE
      ↓
ACT ON INFORMATION
      ↓
FEEDBACK
      ↓
IMPROVEMENT OPPORTUNITY
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

This is a CMOC abstraction of the Source, not an ISO-named mechanism.

### CAPABILITY

**CAP-027 — Communication-to-action capability**

CMOC interpretation: ability to design and operate relevant internal and external communication so that information is transmitted, received, acted upon and fed back into the QMS where relevant.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATES

**CORE-CANDIDATE-052 — Communication is a process**

Annex A explicitly treats communication as a process with objectives, inputs, outputs, tools, content, responsibilities, resources, risks, opportunities and feedback.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-053 — Communication has a design space**

The Source requires explicit determination of what, when, with whom, how and who communicates.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-054 — Effective communication includes action**

Effective communication provides the ability to transmit and receive information quickly and to act on it.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-055 — Communication can be non-human**

Devices can communicate without human intervention.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-056 — Feedback can connect communication to improvement**

Annex A includes feedback and determining opportunities for improvement among effective communication outcomes.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

Although Annex A gives a process architecture for communication, it does not prescribe a sufficiently concrete reproducible organizational implementation to qualify as a CMOC Machine.

### CHAIN

**CHAIN-CANDIDATE-023 — Communication-to-action**

```text
COMMUNICATION OBJECTIVE
 ↓
TRANSMIT
 ↓
RECEIVE
 ↓
ACT
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-024 — Communication feedback**

```text
COMMUNICATION
 ↓
FEEDBACK
 ↓
OPPORTUNITY FOR IMPROVEMENT
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

The five parameters `what / when / with whom / how / who` are a design specification, not by themselves a Chain.

### ROLE

**NONE**

`who communicates` is a required communication parameter, but the Source does not define a specific CMOC role.

### PHYSICAL REALIZATION

**NONE**

Tools and device-to-device interaction are examples of realization means, but no specific CMOC physical/organizational realization is prescribed.

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

**NONE** as a new explicit requirement in Clause 7.4.

Important boundary: communication may use documented information, but 7.4 does not itself require all communication to be documented. Clause 7.5 remains the dedicated source for documented information management.

### CMOC INTERPRETATION

ISO-027 produces an unusually strong structural statement:

> **Communication is itself a process.**

Not merely a support activity around processes.

Its architecture can be represented as:

```text
OBJECTIVE
   ↓
INPUT
   ↓
COMMUNICATION PROCESS
   ├── CONTENT
   ├── TOOL
   ├── RESPONSIBILITY
   ├── RESOURCE
   └── RISK / OPPORTUNITY
   ↓
OUTPUT
   ↓
RECEIVE / ACT
   ↓
FEEDBACK
```

This is CMOC interpretation based on Annex A.

A second important interpretation:

```text
COMMUNICATION
      ↓
INFORMATION
      ↓
ACTION
```

The Source's notion of effective communication is therefore not exhausted by successful transfer. The transfer has value because it enables action, trust, customer/process awareness and improvement opportunities. fileciteturn71file11

A third important observation for CMOC:

```text
HUMAN ↔ HUMAN
HUMAN ↔ DEVICE
DEVICE ↔ DEVICE
```

The last case is explicitly recognized by the Source. This potentially opens a bridge to digital/automated Machines, but we do **not** create such a Machine from 7.4 alone.

### CROSS-CLAUSE OBSERVATION

ISO-026 Awareness described application of understanding in action. ISO-027 now supplies a process through which relevant information can be transmitted, received and acted upon and through which feedback can expose improvement opportunities.

A candidate composition is:

```text
COMMUNICATION
      ↓
INFORMATION
      ↓
AWARENESS / UNDERSTANDING
      ↓
ACTION
      ↓
FEEDBACK
      ↓
IMPROVEMENT OPPORTUNITY
```

This is **CMOC interpretation**, not a Source-stated Chain. Do not promote it yet.

A second emerging pattern is:

```text
PROCESS NEED
      ↓
DEFINE COMMUNICATION
      ↓
RESOURCE / TOOL / RESPONSIBILITY
      ↓
TRANSMIT ↔ RECEIVE
      ↓
ACTION
      ↓
FEEDBACK
```

This reinforces the general CMOC pattern of a function being realized through a managed process, but remains a candidate.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **8**
- GM: **4**
- REL: **7**
- MECHANISM: **M-032 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-027 CANDIDATE**
- CORE CANDIDATES: **5**
- MACHINE: **NONE**
- CHAIN: **2 CANDIDATES**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Document / Documented information / Record: **no new explicit requirement**
- CROSS-CLAUSE: **ISO-026 strengthened; communication is explicitly a process and can operate without human intervention**
