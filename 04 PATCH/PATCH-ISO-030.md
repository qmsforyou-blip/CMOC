# PATCH-ISO-030

## Извещение на изменение

**0099+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 8.2 — Requirements for products and services; 8.2.1–8.2.4; Annex A.8.2

### SOURCE CLAIM

Customer communication shall include providing information about products and services; handling enquiries, contracts and orders including changes; obtaining customer feedback including complaints; handling or controlling customer property; and information concerning contingency actions, including relevant disruptions. Customer communication can be direct or indirect and can include meetings, electronic mail, document exchange, websites, publications, social media, FAQs and training. fileciteturn79file0

When determining requirements for products and services offered to customers, the organization shall define applicable statutory and regulatory requirements and requirements it considers necessary, and ensure that it can meet the claims it makes about the products and services. fileciteturn80file10

Before committing to supply products and services, the organization shall ensure it has the ability to meet the requirements and shall review them. The review includes customer-specified requirements (including delivery and post-delivery where applicable), requirements not stated by the customer but necessary for specified or intended use when known, requirements specified by the organization, applicable statutory/regulatory requirements, and contract/order requirements differing from those previously expressed. Differing requirements shall be resolved. If the customer does not provide a documented statement of requirements, the organization shall confirm the customer's requirements before acceptance. Documented information shall be available as applicable as evidence of review results and new or changed requirements. fileciteturn79file0

When requirements change, relevant documented information shall be updated and communicated to relevant interested parties. fileciteturn79file0

Annex A.8.2 explains that adequate customer information through an appropriate communication process supports operational effectiveness and enables outputs to meet requirements. Communication clarifies what products/services are required and customer needs. The organization determines offered requirements, including mandatory requirements and those attributed by the organization, and before offering or committing to provision it must ensure it is capable of delivering what is promised and what is necessary to enhance customer satisfaction. fileciteturn80file0

### TERMS
- customer communication
- enquiry
- contract
- order
- customer feedback
- customer complaint
- customer property
- contingency action
- product/service requirements
- statutory and regulatory requirements
- claims
- specified use
- intended use
- review
- acceptance
- changed requirements
- relevant interested parties
- ability to meet requirements

### DISTINCTIONS

**DIS-001 — CUSTOMER COMMUNICATION ≠ CUSTOMER REQUIREMENT**

Communication is the process through which information is exchanged; customer requirements are one class of content that must be clarified/handled through that communication.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-002 — CUSTOMER-SPECIFIED REQUIREMENT ≠ REQUIREMENT NECESSARY FOR SPECIFIED/INTENDED USE**

The review explicitly treats requirements not stated by the customer but necessary for specified or intended use as a separate category.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-003 — CUSTOMER REQUIREMENT ≠ ORGANIZATION-SPECIFIED REQUIREMENT**

Requirements specified by the organization are separately included in the review.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-004 — CUSTOMER REQUIREMENT ≠ STATUTORY/REGULATORY REQUIREMENT**

Applicable legal requirements form a separate requirement source.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-005 — REQUIREMENT ≠ CLAIM**

The organization must define requirements and ensure it can meet the claims it makes about offered products/services. A claim is therefore not collapsed into the underlying requirement.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-006 — REQUIREMENT DEFINITION ≠ REQUIREMENT REVIEW**

8.2.2 determines/defines requirements; 8.2.3 reviews them before commitment.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-007 — ABILITY TO MEET REQUIREMENTS ≠ REVIEW OF REQUIREMENTS**

Ability is a condition to be ensured; review is a management action performed before commitment.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-008 — REQUIREMENT REVIEW ≠ COMMITMENT TO SUPPLY**

The review occurs before commitment to supply.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-009 — ACCEPTANCE ≠ REQUIREMENT CONFIRMATION**

Where the customer does not provide a documented statement, requirements shall be confirmed before acceptance. Confirmation precedes acceptance in this situation.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-010 — OLD REQUIREMENT ≠ CHANGED REQUIREMENT**

A contract/order requirement differing from previously expressed requirements is explicitly recognized as a distinct case requiring resolution; later changes require update and communication.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-011 — REQUIREMENT CHANGE ≠ DOCUMENT UPDATE ONLY**

When requirements change, relevant documented information must be updated **and** communicated to relevant interested parties.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-012 — CUSTOMER FEEDBACK ≠ CUSTOMER COMPLAINT**

Complaints are included as a type of customer feedback, but the terms are not made synonymous.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### GM

**GM-001**

> До обязательства перед клиентом сначала установи полный набор требований, затем проверь способность организации их выполнить и проведи review.

**GM-002**

> Не считай требованием только то, что клиент сформулировал: учитывай необходимые требования для specified/intended use, требования организации и statutory/regulatory requirements.

**GM-003**

> Не допускай расхождения между новым требованием и ранее согласованным: differing requirements должны быть resolved.

**GM-004**

> Изменение требования должно проходить через две функции: update relevant documented information и communication relevant interested parties.

**GM-005**

> Не обещай клиенту то, что организация не способна выполнить: claims должны соответствовать способности организации.

### REL

**REL-001**

```text
CUSTOMER COMMUNICATION
        ↓
INFORMATION / NEEDS / EXPECTATIONS
        ↓
REQUIREMENTS
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-002**

```text
CUSTOMER REQUIREMENTS
        +
SPECIFIED / INTENDED USE NEEDS
        +
ORGANIZATION REQUIREMENTS
        +
STATUTORY / REGULATORY REQUIREMENTS
        ↓
DEFINED PRODUCT / SERVICE REQUIREMENTS
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-003**

```text
DEFINED REQUIREMENTS
        ↓
ABILITY TO MEET
        ↓
REVIEW
        ↓
COMMITMENT TO SUPPLY
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-004**

```text
REQUIREMENTS DIFFERING FROM PREVIOUSLY EXPRESSED
        ↓
RESOLUTION
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-005**

```text
NO DOCUMENTED CUSTOMER STATEMENT
        ↓
CONFIRM CUSTOMER REQUIREMENTS
        ↓
ACCEPTANCE
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-006**

```text
REVIEW
        ↓
DOCUMENTED INFORMATION
        ↓
EVIDENCE OF REVIEW RESULTS
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-007**

```text
NEW / CHANGED REQUIREMENTS
        ↓
UPDATE DOCUMENTED INFORMATION
        +
COMMUNICATE
        ↓
RELEVANT INTERESTED PARTIES
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-008**

```text
CLAIMS
        ↓
ABILITY TO MEET
        ↓
CUSTOMER EXPECTATION
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MECHANISM

**M-035 — Requirement formation and commitment control**

```text
CUSTOMER COMMUNICATION
        ↓
CAPTURE / CLARIFY NEEDS
        ↓
COMPOSE REQUIREMENTS
        ├── CUSTOMER-SPECIFIED
        ├── SPECIFIED / INTENDED USE
        ├── ORGANIZATION-SPECIFIED
        └── STATUTORY / REGULATORY
        ↓
VERIFY ABILITY TO MEET
        ↓
REVIEW BEFORE COMMITMENT
        ↓
RESOLVE DIFFERENCES
        ↓
COMMIT TO SUPPLY
```

Change branch:

```text
REQUIREMENT CHANGE
        ↓
UPDATE DOCUMENTED INFORMATION
        ↓
COMMUNICATE TO RELEVANT INTERESTED PARTIES
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CAPABILITY

**CAP-030 — Requirement-to-commitment capability**

CMOC interpretation: ability to identify and compose relevant product/service requirements, verify organizational ability to meet them, review them before commitment, resolve differences and propagate subsequent changes.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATES

**CORE-CANDIDATE-067 — Commitment is preceded by ability/review**

The organization must ensure ability to meet requirements and conduct a review before committing to supply.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-068 — Requirement has multiple legitimate sources**

Product/service requirements can arise from customer statements, specified/intended use, organization-defined requirements and statutory/regulatory requirements.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-069 — Requirement change propagates through information and communication**

Changed requirements trigger both update of relevant documented information and communication to relevant interested parties.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-070 — Commitment is a controlled boundary**

CMOC interpretation: the point of commitment to supply is preceded by requirement review and ability verification; it is therefore a potential control boundary between requirement formation and operational execution.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

8.2 defines a reproducible management mechanism, but does not specify a concrete organizational construction sufficient to qualify as a CMOC Machine.

### CHAIN

**CHAIN-CANDIDATE-031 — Requirement-to-commitment**

```text
CUSTOMER COMMUNICATION
 ↓
REQUIREMENT SOURCES
 ↓
DEFINE REQUIREMENTS
 ↓
VERIFY ABILITY
 ↓
REVIEW
 ↓
RESOLVE DIFFERENCES
 ↓
COMMITMENT TO SUPPLY
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-032 — Requirement change propagation**

```text
REQUIREMENT CHANGE
 ↓
UPDATE DOCUMENTED INFORMATION
 ↓
COMMUNICATE
 ↓
RELEVANT INTERESTED PARTIES
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-033 — Customer requirement confirmation**

```text
NO DOCUMENTED CUSTOMER STATEMENT
 ↓
CONFIRM REQUIREMENTS
 ↓
ACCEPTANCE
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

### ROLE

**NONE**

No new concrete CMOC Role is established. The clause specifies organizational obligations rather than introducing a distinct role.

### PHYSICAL REALIZATION

**NONE**

The Source names communication means and channels, but these are not sufficient to identify a specific CMOC physical realization of the mechanism.

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

8.2 provides a particularly important application of the ISO-028 distinction.

Documented information is required as applicable as evidence of:

```text
REVIEW RESULTS
+
NEW / CHANGED REQUIREMENTS
```

The changed requirement must additionally be communicated to relevant interested parties.

This supports the distinction:

```text
REQUIREMENT
        ≠
DOCUMENTED INFORMATION ABOUT REQUIREMENT
        ≠
COMMUNICATION OF REQUIREMENT
```

The documented information evidencing the review is evidentiary in function and may constitute a Record depending on the concrete form/context, but the Source does not require us to classify every such item as Record.

### CMOC INTERPRETATION

8.2 reveals a significant control boundary:

```text
CUSTOMER / ENVIRONMENT
        ↓
COMMUNICATION
        ↓
REQUIREMENT FORMATION
        ↓
ABILITY CHECK
        ↓
REVIEW
        ↓
COMMITMENT
        ↓
OPERATION
```

The most important interpretation is:

> **Обязательство организации перед клиентом не должно быть непосредственной реакцией на запрос; между запросом и обязательством существует управленческий контур формирования, проверки и review требований.**

This is CMOC interpretation, not an ISO definition.

A second interpretation:

> **Requirement в operational architecture — это не только то, что сформулировал клиент. Оно является результатом композиции нескольких источников требований.**

A third:

> **Commitment to supply is a control boundary: after requirements are reviewed and ability to meet them is established, the organization crosses from requirement negotiation/definition into operational obligation.**

This is a CMOC hypothesis requiring confirmation from later clauses and other sources.

### CROSS-CLAUSE OBSERVATION

8.2 composes and operationalizes earlier structures:

```text
ISO-010  NEEDS / EXPECTATIONS OF INTERESTED PARTIES
ISO-013  LEADERSHIP / CUSTOMER FOCUS
ISO-015  RESPONSIBILITIES / AUTHORITIES
ISO-027  COMMUNICATION AS PROCESS
ISO-028  DOCUMENTED INFORMATION
ISO-029  OPERATIONAL PLANNING / CONTROL
        ↓
ISO-030  REQUIREMENT FORMATION → REVIEW → COMMITMENT
```

A particularly strong cross-clause candidate now appears:

```text
INTERESTED PARTY NEED
        ↓
COMMUNICATION
        ↓
REQUIREMENT
        ↓
REVIEW
        ↓
ABILITY
        ↓
COMMITMENT
        ↓
OPERATIONAL PROCESS
```

**MULTI-CONFIRMATION CANDIDATE** — not yet Core/Canon/Chain.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **12**
- GM: **5**
- REL: **8**
- MECHANISM: **M-035 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-030 CANDIDATE**
- CORE CANDIDATES: **4**
- MACHINE: **NONE**
- CHAIN: **3 CANDIDATES**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Document / Documented information / Record: **review evidence and changed requirements explicitly documented; communication is a separate function**
- CROSS-CLAUSE: **strong composition of interested-party needs → communication → requirements → review → ability → commitment → operation**
