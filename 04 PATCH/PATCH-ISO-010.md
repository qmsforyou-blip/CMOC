# PATCH-ISO-010

## Извещение на изменение

**0079+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 4.2 — Understanding the needs and expectations of interested parties

### SOURCE CLAIM

The organization shall determine:

a) the interested parties that are relevant to the quality management system;
b) the relevant requirements of these interested parties;
c) which of these requirements will be addressed through the quality management system.

The organization shall monitor and review information about these interested parties and their relevant requirements. The Note states that relevant interested parties can have requirements related to climate change. fileciteturn37file2

Annex A.4.2 clarifies that relevant requirements of relevant interested parties can affect the organization's ability to provide products and services meeting customer and applicable statutory and regulatory requirements. It also states that not all interested party requirements necessarily become requirements for the organization: they must be applicable or relevant to the organization or its QMS. Requirements may become mandatory through laws, regulations, permits, licences, governmental or court action, or higher-level corporate mandates; other requirements can be adopted voluntarily or through agreement or contract, after which they become requirements for the organization. fileciteturn37file0turn37file18

### TERMS
- interested party
- relevant interested party
- needs
- expectations
- requirement
- relevant requirement
- applicable requirement
- mandatory requirement
- voluntary requirement
- agreement / contract
- quality management system
- monitoring
- review

### DISTINCTIONS

**DIS-001 — INTERESTED PARTY ≠ RELEVANT INTERESTED PARTY**

Clause 4.2 does not require the organization to treat every interested party as relevant to the QMS; it requires determination of the interested parties that are relevant to the QMS.

**STATUS: CANDIDATE / 1 source**

**DIS-002 — INTERESTED PARTY REQUIREMENT ≠ ORGANIZATIONAL REQUIREMENT**

Annex A.4.2 explicitly states that not all interested party requirements necessarily become requirements for the organization. Applicability and relevance determine whether they enter the organization's requirement set. fileciteturn37file18

**STATUS: CANDIDATE / 1 source**

**DIS-003 — REQUIREMENT ≠ REQUIREMENT ADDRESSED THROUGH QMS**

Clause 4.2 requires a separate determination of which relevant interested-party requirements will be addressed through the QMS. Therefore a requirement can be relevant without automatically being assigned to the QMS.

**STATUS: CANDIDATE / 1 source**

**DIS-004 — MANDATORY REQUIREMENT ≠ VOLUNTARILY ADOPTED REQUIREMENT**

The Annex distinguishes requirements imposed through law, regulation, permits, licences, governmental/court action or higher-level corporate mandate from requirements the organization adopts voluntarily or through agreement/contract. fileciteturn37file18

**STATUS: CANDIDATE / 1 source**

**DIS-005 — NEED / EXPECTATION ≠ AUTOMATIC REQUIREMENT**

The clause title refers to needs and expectations, while the normative determination is specifically of interested parties, their relevant requirements, and which requirements will be addressed through the QMS. The Source does not state that every need or expectation automatically becomes a requirement.

**STATUS: CANDIDATE / 1 source**

### GM

**GM-001**

> Не переносить автоматически требования заинтересованных сторон в систему управления: сначала определить релевантность заинтересованной стороны и её требования, затем — какие требования будут адресованы через QMS.

**GM-002**

> Рассматривать требования заинтересованных сторон как изменяемый вход управления: информацию о релевантных заинтересованных сторонах и их требованиях необходимо мониторить и пересматривать.

### REL

**REL-001**

```text
INTERESTED PARTIES
        ↓
RELEVANCE TO QMS
        ↓
RELEVANT INTERESTED PARTIES
```

**STATUS: CANDIDATE / 1 source**

**REL-002**

```text
RELEVANT INTERESTED PARTY
        ↓
RELEVANT REQUIREMENTS
        ↓
DETERMINE
WHICH REQUIREMENTS
ARE ADDRESSED THROUGH QMS
```

**STATUS: CANDIDATE / 1 source**

**REL-003**

```text
INTERESTED-PARTY REQUIREMENT
        ↓
APPLICABILITY / RELEVANCE
        ↓
ORGANIZATIONAL REQUIREMENT
```

Annex A.4.2 states that not all interested-party requirements become requirements for the organization; once voluntarily adopted or agreed through contract/agreement, such requirements become requirements for the organization. fileciteturn37file18

**STATUS: CANDIDATE / 1 source**

**REL-004**

```text
RELEVANT INTERESTED PARTIES
        +
RELEVANT REQUIREMENTS
        ↓
MONITOR + REVIEW
        ↓
AWARENESS OF CHANGES
```

**STATUS: CANDIDATE / 1 source**

### MECHANISM

**M-011 — Determination and filtering of interested-party requirements**

The Source defines a mechanism with three determinations:

```text
INTERESTED PARTIES
        ↓
RELEVANCE
        ↓
RELEVANT REQUIREMENTS
        ↓
QMS-ADDRESSED REQUIREMENTS
```

This is followed by ongoing monitoring and review of information about relevant interested parties and their relevant requirements. fileciteturn37file2

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

Important boundary: no specific reproducible method or organizational implementation is prescribed. Therefore no Machine is created.

### CAPABILITY

**CAP-007 — Ability to determine and maintain awareness of relevant interested parties and their requirements**

CMOC interpretation: the organization needs the ability to identify relevant interested parties, determine their relevant requirements, decide which requirements are addressed through the QMS, and maintain awareness of changes through monitoring and review.

**STATUS: CANDIDATE / 1 source**

### CORE CANDIDATE

**CORE-CANDIDATE-009 — Requirement filtering by relevance and applicability**

An external requirement does not become an organizational/QMS requirement merely because an interested party has it. The system performs a determination of relevance/applicability and separately determines which relevant requirements are addressed through the QMS.

**STATUS: CANDIDATE / 1 source**

**CORE-CANDIDATE-010 — Interested-party requirements as managed inputs**

Relevant interested-party requirements can affect the organization's ability to achieve conformity and customer satisfaction and therefore constitute a managed input that requires monitoring and review.

**STATUS: CANDIDATE / 1 source**

### MACHINE

**NONE**

The clause specifies a management mechanism and required capability, but no concrete reproducible organizational realization.

### CHAIN

**NONE**

The extracted structures contain dependencies and decision points, but Clause 4.2 does not present them as a confirmed execution sequence. Do not promote them to Chain yet.

### ROLE

**NONE**

No sufficiently specified role/action pattern is provided in Clause 4.2 itself.

### PHYSICAL REALIZATION

**NONE**

### CMOC INTERPRETATION

ISO-010 makes an important refinement of ISO-009.

ISO-009 gave us:

```text
CONTEXT / ISSUES
      ↓
RELEVANCE
      ↓
EFFECT ON ABILITY
```

ISO-010 introduces a second filtering layer:

```text
INTERESTED PARTIES
      ↓
RELEVANCE
      ↓
REQUIREMENTS
      ↓
RELEVANCE / APPLICABILITY
      ↓
QMS-ADDRESSED REQUIREMENTS
```

The particularly strong architectural distinction is:

> **Источник требования ≠ требование организации ≠ требование, адресуемое через QMS.**

This is a CMOC interpretation of the Source, not an ISO definition of CMOC.

The Annex also establishes a temporal property: relevant interested parties and their relevant requirements are not a one-time inventory; information about them is monitored and reviewed to maintain awareness of changes. fileciteturn37file0

The climate-change note is treated as an example of a relevant requirement, not as a separate CMOC entity.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **5 CANDIDATES**
- GM: **2**
- REL: **4 CANDIDATES**
- MECHANISM: **M-011 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-007 CANDIDATE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **NONE**
- ROLE: NONE
- PHYSICAL REALIZATION: NONE
- CONFIRMATION: **1 source — ISO/DIS 9001:2025**
