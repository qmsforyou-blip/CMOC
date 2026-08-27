# PATCH-ISO-006

## Извещение на изменение

**0075+250826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 1 — Scope

### SOURCE CLAIM

The document specifies requirements for a quality management system when an organization:

1. needs to demonstrate its ability to consistently provide products and services that meet customer and applicable statutory and regulatory requirements; and
2. aims to enhance customer satisfaction through effective application of the system, including processes for improvement of the system and assurance of conformity to customer and applicable statutory and regulatory requirements.

All requirements are generic. The document is applicable to any organization regardless of type or size, or of the products and services it provides.

The terms “product” and “service” in this document apply only to products and services intended for, or required by, a customer. Statutory and regulatory requirements can be expressed as legal requirements.

### TERMS
- quality management system
- ability
- consistently provide
- customer requirements
- statutory requirements
- regulatory requirements
- customer satisfaction
- effective application
- improvement of the system
- assurance of conformity
- generic requirements
- product
- service

### DISTINCTIONS

**DIS-001 — QMS ability ≠ single successful conformity**

The Source frames the need in terms of an organization's ability to consistently provide conforming products and services, not merely a one-time successful result.

**STATUS: CANDIDATE / 1 source**

**DIS-002 — CONFORMITY ≠ CUSTOMER SATISFACTION**

The Source states both conformity to applicable requirements and enhancement of customer satisfaction as distinct intended purposes of effective application of the QMS.

**STATUS: CANDIDATE / 1 source**

**DIS-003 — SYSTEM IMPROVEMENT ≠ ASSURANCE OF CONFORMITY**

The Source identifies processes for improvement of the system and assurance of conformity as distinct components within effective application of the QMS.

**STATUS: CANDIDATE / 1 source**

**DIS-004 — CUSTOMER REQUIREMENTS ≠ STATUTORY / REGULATORY REQUIREMENTS**

The Source explicitly identifies customer requirements and applicable statutory and regulatory requirements as separate requirement categories.

**STATUS: CANDIDATE / 1 source**

**DIS-005 — PRODUCT / SERVICE ≠ ANY OUTPUT**

Within this document, “product” or “service” applies specifically to products and services intended for, or required by, a customer.

**STATUS: CANDIDATE / 1 source**

### GM

**GM-001**

> Design the quality management system to demonstrate a repeatable ability to provide conforming products and services, not merely to produce an isolated conforming result.

**GM-002**

> Apply the management system so that conformity assurance and system improvement jointly support customer satisfaction.

### REL

**REL-001**

```text
QMS
  ↓
EFFECTIVE APPLICATION
  ↓
CONFORMITY ASSURANCE
  +
SYSTEM IMPROVEMENT
  ↓
CUSTOMER SATISFACTION
```

**STATUS: CANDIDATE / 1 source**

**REL-002**

```text
CUSTOMER REQUIREMENTS
        +
STATUTORY / REGULATORY REQUIREMENTS
        ↓
CONFORMING PRODUCTS / SERVICES
```

**STATUS: CANDIDATE / 1 source**

**REL-003**

```text
QMS
 ↓
ABILITY
 ↓
CONSISTENT PROVISION
 ↓
CONFORMITY
```

**STATUS: CANDIDATE / 1 source**

### MECHANISM

**M-006 — Effective QMS application for conformity assurance and system improvement**

The Scope explicitly connects effective application of the QMS with two internal functions: processes for improvement of the system and assurance of conformity to customer and applicable statutory and regulatory requirements.

**CLASS: M**

**STATUS: CANDIDATE / 1 source**

Important boundary: Clause 1 identifies the required purpose and components of effective application but does not yet specify the concrete operational construction by which they are executed. Therefore this remains M, not MACHINE.

### CAPABILITY

**CAP-004 — Candidate: ability to consistently provide conforming products and services**

This is a direct restatement of the capability required by the Scope and therefore reinforces CAP-001 from ISO-001 rather than creating an independent capability concept.

**STATUS: CONFIRM / 1 source within ISO-003?**

### CORE CANDIDATE

**CORE-CANDIDATE-004 — Repeatable conformity capability**

A quality management system is framed around an organization's ability to consistently provide conforming products and services, rather than around isolated conformity events.

**STATUS: CANDIDATE / 1 source**

### MACHINE

**NONE**

The Scope specifies purpose, required capability and broad components of effective application, but does not provide a concrete reproducible implementation.

### CHAIN

**NONE**

The relations above are extracted structural dependencies, not a confirmed execution sequence stated as a process chain by Clause 1.

### ROLE

**NONE**

### PHYSICAL REALIZATION

**NONE**

### CMOC INTERPRETATION

Clause 1 strengthens the earlier ISO-001 capability. The key extraction is the shift from “having a QMS” to **demonstrable, consistent capability** supported by effective application of the system.

The Source also separates two result directions that should not be collapsed:

```text
CONFORMITY ASSURANCE
        +
SYSTEM IMPROVEMENT
        ↓
EFFECTIVE APPLICATION OF QMS
        ↓
CUSTOMER SATISFACTION
```

This is a CMOC interpretation, not a direct ISO definition.

The Scope does not yet provide enough evidence to create a Machine or Chain.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: 5 CANDIDATES
- GM: 2
- REL: 3 CANDIDATES
- MECHANISM: M-006 NEW / SINGLE-SOURCE
- CAPABILITY: CAP-004 CONFIRM / UPDATE of existing capability
- CORE CANDIDATE: CORE-CANDIDATE-004
- MACHINE: NONE
- CHAIN: NONE
- ROLE: NONE
- PHYSICAL REALIZATION: NONE
- CONFIRMATION: 1 source — ISO/DIS 9001:2025
