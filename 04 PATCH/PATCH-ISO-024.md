# PATCH-ISO-024

## Извещение на изменение

**0093+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 7.1.6 — Organizational knowledge; Annex A.7.1.6

### SOURCE CLAIM

The organization shall determine the knowledge necessary for the operation of its processes and to achieve conformity of products and services. This knowledge shall be maintained and made available to the extent necessary. When addressing changing needs and trends, the organization shall consider its current knowledge and determine how to acquire or access any necessary additional knowledge and required updates. fileciteturn57file0

Annex A explains that organizational knowledge is knowledge specific to the organization, generally gained by experience. It is information used and shared to achieve the organization’s objectives. Organizational knowledge can be based on internal sources such as intellectual property, knowledge gained from experience, lessons learned from failures and successful projects, and capture and sharing of undocumented knowledge and experience. External sources can include standards, academia, conferences, customer or external provider knowledge, and other sources. fileciteturn56file4

The Annex also notes that the organization should consider whether current knowledge is sufficient and determine how to acquire or access additional knowledge when changing needs and trends are considered. fileciteturn56file4

### TERMS
- organizational knowledge
- knowledge necessary
- operation of processes
- conformity
- maintain
- make available
- current knowledge
- changing needs and trends
- acquire
- access
- additional knowledge
- required updates
- experience
- lessons learned
- undocumented knowledge
- internal sources
- external sources

### DISTINCTIONS

**DIS-001 — ORGANIZATIONAL KNOWLEDGE ≠ DOCUMENTED INFORMATION**

The Source defines organizational knowledge broadly and explicitly includes knowledge and experience that can be undocumented. The requirement to maintain and make knowledge available does not itself require all knowledge to be converted into documented information.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-002 — KNOWLEDGE NECESSARY ≠ ALL KNOWLEDGE**

The organization determines the knowledge necessary for process operation and conformity; the requirement is purpose-related, not an instruction to collect all possible knowledge.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-003 — MAINTAIN KNOWLEDGE ≠ MAKE KNOWLEDGE AVAILABLE**

The Source states both requirements separately: knowledge is maintained and made available to the extent necessary.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-004 — CURRENT KNOWLEDGE ≠ ADDITIONAL KNOWLEDGE / UPDATES**

Changing needs and trends can create a need to acquire or access additional knowledge and required updates beyond current knowledge.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-005 — INTERNAL KNOWLEDGE SOURCE ≠ EXTERNAL KNOWLEDGE SOURCE**

The Annex distinguishes internal sources (experience, lessons learned, intellectual property, undocumented knowledge) from external sources (standards, academia, conferences, customers, external providers).

**STATUS: NEW / SINGLE-SOURCE**

**DIS-006 — KNOWLEDGE ≠ INFORMATION USED AND SHARED**

Annex A describes organizational knowledge as information used and shared to achieve organizational objectives, while the clause treats knowledge itself as a resource necessary for process operation and conformity. These formulations should not be collapsed into a single identity without further evidence.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-007 — EXPERIENCE ≠ LESSON LEARNED**

Both are identified as sources/bases of organizational knowledge; they are not presented as synonymous.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### GM

**GM-001**

> Определяй необходимое organizational knowledge от потребности процессов и conformity, а не от стремления накопить максимум информации.

**GM-002**

> Управляй knowledge через две разные функции: maintain и make available.

**GM-003**

> При изменении потребностей и трендов сначала оценивай current knowledge, затем определяй, какое additional knowledge или updates необходимо acquire/access.

**GM-004**

> Не ограничивай организационное знание документами: опыт, lessons learned и undocumented knowledge также могут быть его источниками.

### REL

**REL-001**

```text
PROCESS OPERATION / CONFORMITY
        ↓
KNOWLEDGE NECESSARY
        ↓
MAINTAIN + MAKE AVAILABLE
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-002**

```text
CHANGING NEEDS / TRENDS
        ↓
CURRENT KNOWLEDGE
        ↓
DETERMINE GAP / NEED
        ↓
ACQUIRE / ACCESS
        ↓
ADDITIONAL KNOWLEDGE / UPDATES
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-003**

```text
INTERNAL SOURCES
        ↓
ORGANIZATIONAL KNOWLEDGE
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-004**

```text
EXTERNAL SOURCES
        ↓
ORGANIZATIONAL KNOWLEDGE
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-005**

```text
EXPERIENCE / FAILURES / SUCCESSFUL PROJECTS
        ↓
LESSONS LEARNED / CAPTURED KNOWLEDGE
        ↓
ORGANIZATIONAL KNOWLEDGE
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MECHANISM

**M-029 — Organizational knowledge continuity and renewal**

```text
PROCESS / CONFORMITY NEED
        ↓
DETERMINE NECESSARY KNOWLEDGE
        ↓
MAINTAIN
        ↓
MAKE AVAILABLE
        ↓
CHANGING NEEDS / TRENDS
        ↓
ASSESS CURRENT KNOWLEDGE
        ↓
ACQUIRE / ACCESS
        ↓
ADDITIONAL KNOWLEDGE / UPDATES
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CAPABILITY

**CAP-024 — Organizational knowledge continuity capability**

CMOC interpretation: ability to determine, maintain, make available and renew the knowledge necessary for process operation and conformity.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATES

**CORE-CANDIDATE-041 — Knowledge is a managed resource**

Organizational knowledge is explicitly treated as knowledge necessary for process operation and conformity and is subject to determine/maintain/make-available/access controls.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-042 — Organizational knowledge can be undocumented**

The Annex explicitly includes capture and sharing of undocumented knowledge and experience as an internal source.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-043 — Knowledge adequacy is dynamic**

Changing needs and trends require consideration of current knowledge and determination of additional knowledge or updates that need to be acquired or accessed.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

The clause describes a management mechanism for organizational knowledge but does not prescribe a concrete reproducible organizational construction qualifying as a Machine.

### CHAIN

**CHAIN-CANDIDATE-017 — Knowledge continuity**

```text
PROCESS / CONFORMITY NEED
 ↓
DETERMINE KNOWLEDGE
 ↓
MAINTAIN
 ↓
MAKE AVAILABLE
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-018 — Knowledge renewal**

```text
CHANGING NEEDS / TRENDS
 ↓
CURRENT KNOWLEDGE
 ↓
DETERMINE ADDITIONAL NEED
 ↓
ACQUIRE / ACCESS
 ↓
UPDATE
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

### ROLE

**NONE**

### PHYSICAL REALIZATION

**NONE**

The Annex provides examples of internal and external knowledge sources, but no specific CMOC physical realization.

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

No general requirement is stated to document organizational knowledge. The Source explicitly recognizes undocumented knowledge and experience as possible internal sources. This reinforces, but does not by itself finalize, the distinction:

```text
KNOWLEDGE ≠ DOCUMENTED INFORMATION
```

No new Record requirement is created here.

### CMOC INTERPRETATION

ISO-024 significantly strengthens the line already identified in ISO-019:

```text
KNOWLEDGE
 ↓
RETAIN / MAINTAIN
 ↓
APPLY / USE
 ↓
SHARE / MAKE AVAILABLE
```

And adds a renewal loop:

```text
CHANGING NEEDS / TRENDS
        ↓
CURRENT KNOWLEDGE
        ↓
KNOWLEDGE GAP / NEED
        ↓
ACQUIRE / ACCESS
        ↓
ADDITIONAL KNOWLEDGE / UPDATES
        ↺
```

Important CMOC interpretation:

> **Организационное знание — это управляемый ресурс системы, достаточность которого относительна выполняемых функций и процессов и может изменяться вместе с потребностями и средой.**

This is CMOC interpretation, not an ISO definition.

A second important interpretation:

> **Документирование не является условием существования organizational knowledge: часть знания может существовать как undocumented knowledge/experience.**

This interpretation is directly supported by Annex A but should not be extended into a general theory of knowledge without further sources.

### CROSS-CLAUSE OBSERVATION

ISO-019 introduced organizational knowledge among resources. ISO-020 connected workforce adequacy with organizational knowledge. ISO-024 now gives organizational knowledge its own explicit management construction: determine → maintain → make available → reassess against changing needs/trends → acquire/access updates.

This creates a strong multi-source candidate:

```text
PROCESS / FUNCTION NEED
        ↓
KNOWLEDGE RESOURCE
        ↓
MAINTAIN + MAKE AVAILABLE
        ↓
CHANGE
        ↓
REASSESS
        ↓
RENEW
```

It also strengthens the distinction:

```text
KNOWLEDGE
        ≠
DOCUMENTED INFORMATION
```

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **7**
- GM: **4**
- REL: **5**
- MECHANISM: **M-029 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-024 CANDIDATE**
- CORE CANDIDATES: **3**
- MACHINE: **NONE**
- CHAIN: **2 CANDIDATES**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Document / Documented information / Record: **knowledge is not required to be fully documented; no new Record requirement**
- CROSS-CLAUSE: **ISO-019, ISO-020 and ISO-024 strongly reinforce knowledge as a managed resource and knowledge adequacy as dynamic**
