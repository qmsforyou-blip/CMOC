# PATCH-ISO-018

## Извещение на изменение

**0087+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 6.3 — Planning of changes

### SOURCE CLAIM

When the organization determines the need for changes to the quality management system, the changes shall be carried out in a planned manner. To ensure changes are implemented effectively to achieve intended results, the organization shall consider: the purpose of the changes and potential consequences; the integrity of the QMS; availability of resources and information; allocation or reallocation of responsibilities and authorities; how effectiveness of changes will be monitored and evaluated; communication of changes; and how to review the results of changes. fileciteturn54file17

### TERMS
- change
- planned change
- purpose
- potential consequence
- QMS integrity
- resource
- information
- responsibility
- authority
- effectiveness
- monitoring
- evaluation
- communication
- result

### DISTINCTIONS

**DIS-001 — NEED FOR CHANGE ≠ IMPLEMENTATION OF CHANGE**

Determining that a change is needed is distinct from carrying out the change in a planned manner.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-002 — CHANGE ≠ PLANNED CHANGE**

The Source distinguishes the determination of need from the requirement that implementation be planned.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-003 — CHANGE PURPOSE ≠ CHANGE CONSEQUENCES**

The purpose of a change and its potential consequences are separate considerations in planning.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-004 — CHANGE EFFECTIVENESS ≠ CHANGE IMPLEMENTATION**

Effective implementation is not established merely by carrying out the change; effectiveness is to be monitored and evaluated, and results reviewed.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-005 — CHANGE ≠ LOCAL MODIFICATION ONLY**

Planning must consider QMS integrity and allocation/reallocation of responsibilities and authorities, indicating that a QMS change can have system-wide organizational consequences beyond the directly modified element.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-006 — COMMUNICATION OF CHANGE ≠ IMPLEMENTATION OF CHANGE**

Communication is a separate consideration in effective implementation of change.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### GM

**GM-001**

> Изменение QMS рассматривай как управляемое воздействие: до реализации нужно учитывать purpose, potential consequences, integrity, resources, responsibilities and authorities, monitoring, communication и review.

**GM-002**

> Не считай изменение завершённым по факту внедрения: его effectiveness должна быть monitored/evaluated, а результаты — reviewed.

### REL

**REL-001**

```text
NEED FOR CHANGE
      ↓
PLANNED CHANGE
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-002**

```text
CHANGE PURPOSE
      +
POTENTIAL CONSEQUENCES
      ↓
CHANGE PLANNING
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-003**

```text
CHANGE
      ↓
QMS INTEGRITY
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-004**

```text
CHANGE
      ↓
RESOURCES + INFORMATION
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-005**

```text
CHANGE
      ↓
RESPONSIBILITY + AUTHORITY
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-006**

```text
CHANGE
      ↓
MONITOR + EVALUATE EFFECTIVENESS
      ↓
REVIEW RESULTS
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-007**

```text
CHANGE
      ↓
COMMUNICATION
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MECHANISM

**M-020 — Planned change management**

```text
NEED FOR CHANGE
      ↓
PLAN CHANGE
      ↓
CONSIDER PURPOSE + CONSEQUENCES
      ↓
PROTECT QMS INTEGRITY
      ↓
PROVIDE RESOURCES + INFORMATION
      ↓
ALLOCATE / REALLOCATE RESPONSIBILITY + AUTHORITY
      ↓
IMPLEMENT
      ↓
COMMUNICATE
      ↓
MONITOR + EVALUATE EFFECTIVENESS
      ↓
REVIEW RESULTS
```

This is a CMOC abstraction of the considerations and actions required by 6.3. The Source does not present this exact sequence as a named mechanism.

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CAPABILITY

**CAP-015 — Planned change capability**

CMOC interpretation: ability to introduce changes to the QMS while considering purpose, consequences, system integrity, resources/information, responsibilities/authorities, communication, effectiveness and results.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATE

**CORE-CANDIDATE-026 — Change requires integrity consideration**

A QMS change is not treated as an isolated modification: planning explicitly considers the integrity of the QMS and potential consequences.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-027 — Change is evaluated after implementation**

Implementation does not close the change loop; effectiveness is monitored/evaluated and results reviewed.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-028 — Change reallocates organizational structure**

Planning a QMS change may require allocation or reallocation of responsibilities and authorities.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

The clause specifies a generic change-management mechanism, not a concrete reusable implementation.

### CHAIN

**CHAIN-CANDIDATE-008 — Planned change**

```text
NEED
 ↓
PLAN
 ↓
IMPLEMENT
 ↓
MONITOR / EVALUATE
 ↓
REVIEW RESULTS
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

The fuller list of planning considerations is not treated as a confirmed execution chain.

### ROLE

**ROLE-CANDIDATE-005 — Change responsibility role**

A relevant role whose responsibility and authority are allocated or reallocated as part of planning and implementing QMS change.

**STATUS: CANDIDATE / CROSS-CLAUSE**

### PHYSICAL REALIZATION

**NONE**

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

Clause 6.3 does not explicitly require documented information for planning changes. Therefore no new Document/Documented information/Record extraction is made.

The important information-related relation is only that resources and information availability are considered when planning change. This is not sufficient to infer a record or document requirement.

The Document / Documented information / Record investigation remains open for Clause 7.5.

### CMOC INTERPRETATION

ISO-018 introduces change as a **system-level managed intervention**:

```text
NEED FOR CHANGE
      ↓
CHANGE DESIGN / PLANNING
      ↓
SYSTEM INTEGRITY
      ↓
RESOURCES + ROLES + INFORMATION
      ↓
IMPLEMENTATION
      ↓
MONITORING / EVALUATION
      ↓
RESULT REVIEW
```

The important CMOC interpretation is:

> **A change is not merely a modification of an element. It is a managed intervention whose purpose, consequences, system integrity, enabling conditions, responsibility, communication and resulting effectiveness must be considered.**

This is CMOC interpretation, not an ISO definition.

A particularly important cross-clause bridge is:

```text
ROLE
 ↓
RESPONSIBILITY + AUTHORITY
 ↓
CHANGE
 ↓
QMS INTEGRITY
```

This directly develops ISO-015's earlier candidate that change requires integrity ownership.

Another strong developing structure is:

```text
CHANGE
 ↓
IMPLEMENT
 ↓
EVALUATE EFFECTIVENESS
 ↓
REVIEW RESULT
```

which strengthens the recurring ISO pattern already observed in ISO-016 and ISO-017.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **6 NEW**
- GM: **2**
- REL: **7 CANDIDATES**
- MECHANISM: **M-020 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-015 CANDIDATE**
- CORE CANDIDATES: **3**
- MACHINE: **NONE**
- CHAIN: **1 CHAIN-CANDIDATE**
- ROLE: **1 ROLE-CANDIDATE**
- PHYSICAL REALIZATION: NONE
- Document / Documented information / Record: **no new extraction**
- CONFIRMATION: **ISO-015 change/integrity responsibility strengthened by ISO-018; ISO-016/017 effectiveness/evaluation pattern further supported**
