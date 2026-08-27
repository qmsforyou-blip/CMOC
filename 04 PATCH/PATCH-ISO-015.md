# PATCH-ISO-015

## Извещение на изменение

**0084+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 5.3 — Roles, responsibilities and authorities

### SOURCE CLAIM

Top management shall ensure that responsibilities and authorities for relevant roles are assigned, communicated and understood within the organization. Top management shall assign responsibility and authority for: ensuring that the QMS conforms to the requirements of the document; reporting QMS performance to top management; ensuring processes deliver intended outputs; ensuring promotion of customer focus throughout the organization; reporting opportunities for improvement to top management; and ensuring QMS integrity is maintained, including when QMS changes are planned and implemented. fileciteturn50file16

Annex A.5.3 clarifies that the document does not require one person to be responsible for the QMS. Rather, responsibilities and authorities for relevant roles are to be assigned so that the QMS achieves its objectives. This applies to all people involved in quality management processes, so that the QMS is not regarded as the responsibility of only a few. It also requires assignment of responsibility and authority to report to top management information about the degree to which the QMS is operating, enabling top management to act as needed to ensure QMS integrity during changes. Responsibility should be assigned to prevent changes to QMS elements from causing unintended consequences or inconsistencies. For organizations using emerging technologies in QMS management, traceability of QMS decisions, the responsibility of decision-makers and their accountability needs to be ensured. fileciteturn50file9

### TERMS
- role
- responsibility
- authority
- top management
- relevant role
- QMS performance
- intended output
- QMS integrity
- change
- decision
- accountability
- traceability

### DISTINCTIONS

**DIS-001 — ROLE ≠ RESPONSIBILITY ≠ AUTHORITY**

The Source assigns responsibilities and authorities to relevant roles, treating these as distinct elements rather than interchangeable terms.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-002 — RESPONSIBILITY FOR ACTIVITY ≠ ACCOUNTABILITY FOR RESULT**

This confirms the distinction extracted in ISO-013: responsibility can be distributed among roles, while accountability for QMS effectiveness remains with top management. The terminology guidance states that responsibility can be delegated but accountability for results cannot. fileciteturn46file18

**STATUS: CONFIRM / UPDATE**

**DIS-003 — QMS RESPONSIBILITY ≠ RESPONSIBILITY OF ONE PERSON**

The Source explicitly states that there is no requirement for one person to be responsible for the QMS. Responsibilities and authorities are distributed among relevant roles. fileciteturn50file9

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-004 — ASSIGNED ≠ COMMUNICATED ≠ UNDERSTOOD**

5.3 requires responsibilities and authorities to be assigned, communicated and understood. These are distinct organizational states.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-005 — RESPONSIBILITY FOR PROCESS ≠ RESPONSIBILITY FOR SYSTEM INTEGRITY**

The clause assigns responsibility both for process outputs and for maintaining QMS integrity, including during changes. These are related but distinct responsibility domains.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### GM

**GM-001**

> Распределяй responsibilities и authorities по relevant roles; не своди QMS к ответственности одного человека.

**GM-002**

> Для управляемости недостаточно назначить ответственность: она должна быть communicated и understood.

**GM-003**

> Связывай ответственность с конкретным управленческим результатом: соответствие QMS, performance, intended outputs, customer focus, improvement и integrity при изменениях.

### REL

**REL-001**

```text
RELEVANT ROLE
      ↓
RESPONSIBILITY + AUTHORITY
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-002**

```text
RESPONSIBILITY + AUTHORITY
      ↓
ASSIGNED
      ↓
COMMUNICATED
      ↓
UNDERSTOOD
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-003**

```text
RESPONSIBILITY / AUTHORITY
      ↓
QMS PERFORMANCE INFORMATION
      ↓
TOP MANAGEMENT
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-004**

```text
ROLE RESPONSIBILITY
      ↓
PROCESS INTENDED OUTPUT
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-005**

```text
QMS CHANGE
      ↓
RESPONSIBILITY FOR INTEGRITY
      ↓
PREVENT UNINTENDED CONSEQUENCES /
INCONSISTENCIES
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-006**

```text
QMS DECISION
      ↓
DECISION-MAKER
      ↓
RESPONSIBILITY + ACCOUNTABILITY
      ↓
TRACEABILITY
```

This last relation is specifically highlighted for organizations using emerging technologies. fileciteturn50file9

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MECHANISM

**M-017 — Role-based allocation and feedback of management responsibility**

```text
RELEVANT ROLES
      ↓
ASSIGN RESPONSIBILITY + AUTHORITY
      ↓
COMMUNICATE
      ↓
UNDERSTAND
      ↓
PERFORM / REPORT
      ↓
TOP MANAGEMENT
```

A parallel integrity mechanism applies to changes:

```text
QMS CHANGE
      ↓
ASSIGNED RESPONSIBILITY
      ↓
CHECK / PROTECT QMS INTEGRITY
      ↓
PREVENT UNINTENDED CONSEQUENCES /
INCONSISTENCIES
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

No Machine is created because the Source specifies allocation logic but no concrete reusable organizational implementation.

### CAPABILITY

**CAP-012 — Ability to distribute and operate responsibilities and authorities across relevant roles**

CMOC interpretation: the organization can allocate responsibility and authority, communicate and establish understanding of them, obtain QMS performance information through assigned roles, and preserve system integrity during change.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATE

**CORE-CANDIDATE-019 — Role-based distribution of management responsibility**

The QMS does not need a single "quality person". Its responsibilities and authorities are distributed across relevant roles according to what the system requires.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-020 — Responsibility requires organizational legibility**

Assignment alone is insufficient: responsibility and authority must be communicated and understood within the organization.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-021 — Change requires integrity ownership**

When QMS elements are changed, responsibility must exist for preventing unintended consequences and inconsistencies in the system.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

### CHAIN

**NONE**

The Source defines role assignments and reporting responsibilities, but does not provide a single confirmed execution sequence. The allocation/reporting loop remains a mechanism.

### ROLE

**ROLE-CANDIDATE-002 — Relevant QMS role**

The Source establishes that relevant roles form the carrier structure for QMS responsibilities and authorities. It does not prescribe a fixed universal list of roles.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**ROLE-CANDIDATE-003 — QMS performance reporter**

A role with assigned responsibility and authority to report information on QMS performance to top management.

**STATUS: CANDIDATE / SINGLE-SOURCE**

These are role patterns, not named organizational positions.

### PHYSICAL REALIZATION

**NONE**

### DOCUMENT / DOCUMENTED INFORMATION / RECORD — SPECIAL OBSERVATION

Clause 5.3 does not prescribe documented information for role assignments. Therefore no new document/record distinction is extracted here.

However, the clause strengthens a different information architecture line: QMS performance information must travel from assigned roles to top management, and for emerging-technology contexts QMS decisions, their decision-makers, responsibility and accountability require traceability. fileciteturn50file9

This is not yet a claim that a specific "record" is required. We defer the document/record architecture to Clause 7.5 and retain the distinction as a cross-clause investigation.

### CMOC INTERPRETATION

ISO-015 completes an important transition begun in ISO-013:

```text
TOP MANAGEMENT
      ↓
ACCOUNTABILITY FOR QMS EFFECTIVENESS
      ↓
DISTRIBUTED RESPONSIBILITIES + AUTHORITIES
      ↓
RELEVANT ROLES
      ↓
PROCESS / SYSTEM RESULTS
      ↓
INFORMATION TO TOP MANAGEMENT
```

The architecture is therefore not:

```text
QMS → ONE QUALITY MANAGER
```

but:

```text
QMS
 ↓
REQUIRED FUNCTIONS
 ↓
RELEVANT ROLES
 ↓
RESPONSIBILITIES + AUTHORITIES
 ↓
ACTIONS / REPORTING
 ↓
SYSTEM RESULTS
```

This is a significant CMOC interpretation because it makes **role distribution a structural property of the management system**, not an administrative afterthought.

The change-related part is even more interesting:

```text
SYSTEM ELEMENT
      ↓
CHANGE
      ↓
ASSIGNED RESPONSIBILITY
      ↓
INTEGRITY PROTECTION
      ↓
NO UNINTENDED CONSEQUENCES /
NO INCONSISTENCIES
```

This creates a direct bridge from ROLE architecture to the future CMOC concept of controlled change.

Finally, the emerging-technology note introduces a potentially important future distinction:

```text
DECISION
 ≠
DECISION-MAKER
 ≠
RESPONSIBILITY
 ≠
ACCOUNTABILITY
```

and requires traceability among them in the specified context. This is retained as a candidate, not canonized.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **5** — including **1 CONFIRM/UPDATE** from ISO-013
- GM: **3**
- REL: **6 CANDIDATES**
- MECHANISM: **M-017 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-012 CANDIDATE**
- CORE CANDIDATES: **3**
- MACHINE: **NONE**
- CHAIN: **NONE**
- ROLE: **2 ROLE-CANDIDATES**
- PHYSICAL REALIZATION: NONE
- DOCUMENT / DOCUMENTED INFORMATION / RECORD: **no new extraction; cross-clause line retained**
- CONFIRMATION: **ISO/DIS 9001:2025; responsibility/accountability distinction CONFIRM/UPDATE from ISO-013**
