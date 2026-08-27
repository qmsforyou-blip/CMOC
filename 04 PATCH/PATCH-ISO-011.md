# PATCH-ISO-011

## Извещение на изменение

**0080+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 4.3 — Determining the scope of the quality management system

### SOURCE CLAIM

The organization shall determine the boundaries and applicability of the quality management system to establish its scope. When determining the scope, it shall consider: a) the external and internal issues referred to in 4.1; b) the requirements referred to in 4.2; and c) the products and services of the organization. The scope shall state the types of products and services covered and provide justification for any requirement of the document that the organization determines is not applicable. All requirements of the document shall be applied when applicable within the determined scope. The scope shall be available as documented information. Conformity to the document can only be claimed if requirements determined as not applicable do not affect the organization's ability or responsibility to ensure conformity of products and services and enhancement of customer satisfaction. fileciteturn39file2

Annex A.4.3 clarifies that the scope statement communicates which products and services are covered and the boundaries of the QMS. It may define activities, products and services, related sites, and specific scopes. It distinguishes the scope of the document, the scope of the QMS and the scope of certification as different but closely linked concepts. Boundaries define the limits of the QMS; customer requirements can influence them, and organizational boundaries need to be well defined when the organization is part of a larger entity. fileciteturn39file0

### TERMS
- scope
- boundaries
- applicability
- quality management system
- products and services
- requirement
- not applicable
- documented information
- scope of the document
- scope of the QMS
- scope of certification
- organizational boundaries

### DISTINCTIONS

**DIS-001 — SCOPE ≠ BOUNDARIES**

The clause uses boundaries and applicability as the basis for establishing scope. Annex A.4.3 describes boundaries as the limits of the QMS. Scope is therefore the established definition that communicates coverage; boundaries are the limits that delimit it.

**STATUS: CANDIDATE / 1 source**

**DIS-002 — QMS SCOPE ≠ SCOPE OF THE ISO DOCUMENT**

Annex A.4.3 explicitly identifies the scope of the document and the scope of the QMS as different concepts.

**STATUS: CANDIDATE / 1 source**

**DIS-003 — QMS SCOPE ≠ CERTIFICATION SCOPE**

Annex A.4.3 identifies scope of the QMS and scope of certification as different, although closely linked, concepts.

**STATUS: CANDIDATE / 1 source**

**DIS-004 — APPLICABLE REQUIREMENT ≠ NON-APPLICABLE REQUIREMENT**

Within the determined QMS scope, applicable requirements shall be applied. A requirement determined not applicable requires justification.

**STATUS: CANDIDATE / 1 source**

**DIS-005 — NOT APPLICABLE ≠ EXCLUDED WITHOUT CONDITION**

A requirement can be determined not applicable only within the scope logic and with justification; conformity to the document can only be claimed if that non-applicability does not affect the organization's ability or responsibility to ensure conformity and customer satisfaction. fileciteturn39file2

**STATUS: CANDIDATE / 1 source**

### GM

**GM-001**

> Определяй границы QMS на основании контекста, требований и охватываемых продуктов/услуг, а затем фиксируй, что именно входит в систему.

**GM-002**

> Не принимай неприменимость требования как свободное исключение: она требует обоснования и не должна подрывать способность или ответственность организации обеспечивать соответствие и удовлетворённость потребителя.

### REL

**REL-001**

```text
4.1 CONTEXT ISSUES
        +
4.2 REQUIREMENTS
        +
PRODUCTS / SERVICES
        ↓
QMS BOUNDARIES + APPLICABILITY
        ↓
QMS SCOPE
```

**STATUS: CANDIDATE / 1 source**

**REL-002**

```text
QMS SCOPE
        ↓
COVERED PRODUCTS / SERVICES
        +
COVERED ACTIVITIES / SITES
        ↓
DEFINED QMS BOUNDARIES
```

This structure is clarified in Annex A.4.3. fileciteturn39file0

**STATUS: CANDIDATE / 1 source**

**REL-003**

```text
DETERMINED QMS SCOPE
        ↓
APPLICABLE REQUIREMENTS
        ↓
APPLICATION OF REQUIREMENTS
```

**STATUS: CANDIDATE / 1 source**

**REL-004**

```text
NON-APPLICABILITY
        ↓
JUSTIFICATION
        ↓
CHECK EFFECT ON
CONFORMITY + CUSTOMER SATISFACTION
```

**STATUS: CANDIDATE / 1 source**

### MECHANISM

**M-012 — Scope determination by boundary and applicability**

The Source establishes a determination mechanism:

```text
CONTEXT (4.1)
+
REQUIREMENTS (4.2)
+
PRODUCTS / SERVICES
        ↓
BOUNDARIES + APPLICABILITY
        ↓
ESTABLISHED QMS SCOPE
```

A second mechanism governs non-applicability:

```text
REQUIREMENT
   ↓
NOT APPLICABLE
   ↓
JUSTIFICATION
   ↓
NO ADVERSE EFFECT ON
CONFORMITY / CUSTOMER SATISFACTION
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

Important boundary: the Source defines the determination logic and required result, but does not prescribe a specific reproducible organizational implementation. Therefore no Machine is created.

### CAPABILITY

**CAP-008 — Ability to define and maintain QMS boundaries and applicability**

CMOC interpretation: the organization needs the ability to determine what the QMS covers, which requirements apply within that scope, and to justify non-applicability without undermining conformity or customer satisfaction.

**STATUS: CANDIDATE / 1 source**

### CORE CANDIDATE

**CORE-CANDIDATE-011 — Scope as a filtered system boundary**

QMS scope is not an arbitrary declaration: it is established from context, relevant requirements, and products/services, with boundaries and applicability explicitly determined.

**STATUS: CANDIDATE / 1 source**

**CORE-CANDIDATE-012 — Applicability is a controlled determination**

The system distinguishes applicable requirements from requirements determined not applicable; non-applicability requires justification and must not impair conformity or customer satisfaction.

**STATUS: CANDIDATE / 1 source**

### MACHINE

**NONE**

No concrete reproducible organizational realization is specified.

### CHAIN

**NONE**

Although Clause 4.3 gives dependencies among inputs and scope determination, it does not explicitly present them as an execution sequence sufficient to promote them to a confirmed Chain.

### ROLE

**NONE**

### PHYSICAL REALIZATION

**NONE**

### CMOC INTERPRETATION

ISO-011 closes the first Context triad:

```text
4.1 CONTEXT
   ↓
4.2 RELEVANT REQUIREMENTS
   ↓
4.3 QMS SCOPE
```

The important architectural move is that the system does not merely 'have a scope'. It determines a boundary and applicability based on identified context, requirements, and products/services.

This suggests a provisional CMOC structure:

```text
EXTERNAL / INTERNAL REALITY
        ↓
RELEVANT ISSUES
        ↓
RELEVANT REQUIREMENTS
        ↓
PRODUCTS / SERVICES
        ↓
BOUNDARY + APPLICABILITY
        ↓
MANAGED SYSTEM SCOPE
```

This is CMOC interpretation, not a canonical ISO-to-CMOC mapping.

A second important distinction is between three scopes named in Annex A.4.3:

```text
SCOPE OF ISO DOCUMENT
        ≠
SCOPE OF QMS
        ≠
SCOPE OF CERTIFICATION
```

They are closely linked but not identical. fileciteturn39file0

The Annex also makes an important bridge to the next clause: understanding context and relevant interested-party requirements enables the organization to determine the QMS scope and the processes needed to fulfil purpose, follow strategic direction and achieve intended results. fileciteturn38file11

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **5 CANDIDATES**
- GM: **2**
- REL: **4 CANDIDATES**
- MECHANISM: **M-012 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-008 CANDIDATE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **NONE**
- ROLE: NONE
- PHYSICAL REALIZATION: NONE
- CONFIRMATION: **1 source — ISO/DIS 9001:2025**
