# PATCH-ISO-009

## Извещение на изменение

**0078+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 4.1 — Understanding the organization and its context

### SOURCE CLAIM

The organization shall determine external and internal issues that are relevant to its purpose and its strategic direction and that affect its ability to achieve the intended result(s) of its quality management system. The organization shall also determine whether climate change is a relevant issue. fileciteturn32file8

### TERMS
- external issues
- internal issues
- purpose
- strategic direction
- intended result(s)
- quality management system
- relevant issue
- climate change

### DISTINCTIONS

**DIS-001 — EXTERNAL ISSUES ≠ INTERNAL ISSUES**

Clause 4.1 explicitly requires determination of both external and internal issues. The clause does not collapse them into one category.

**STATUS: CANDIDATE / 1 source**

**DIS-002 — ISSUE ≠ RELEVANT ISSUE**

The requirement is not to determine every possible issue, but issues relevant to purpose and strategic direction and affecting the ability to achieve intended QMS results.

**STATUS: CANDIDATE / 1 source**

**DIS-003 — PURPOSE ≠ STRATEGIC DIRECTION**

The clause identifies purpose and strategic direction as separate reference points for determining relevant external and internal issues.

**STATUS: CANDIDATE / 1 source**

**DIS-004 — CONTEXT ≠ STATIC CONDITION**

The clause requires attention to issues affecting the QMS ability; Annex A.4.1 clarifies that external and internal issues are changeable and may change suddenly, with immediate and incisive effects. Therefore context is treated as something whose changes require monitoring and review.

**STATUS: CANDIDATE / 1 source**

### GM

**GM-001**

> Определяй контекст не через полный перечень факторов, а через их релевантность цели, стратегическому направлению и способности системы достигать intended results.

**GM-002**

> Рассматривай контекст как изменяющееся множество внутренних и внешних факторов, изменения которого требуют мониторинга и пересмотра.

### REL

**REL-001**

```text
EXTERNAL / INTERNAL ISSUES
        ↓
RELEVANCE TO PURPOSE + STRATEGIC DIRECTION
        ↓
EFFECT ON ABILITY
        ↓
INTENDED QMS RESULTS
```

**STATUS: CANDIDATE / 1 source**

**REL-002**

```text
EXTERNAL / INTERNAL ISSUES
        ↓
CHANGE
        ↓
MONITOR + REVIEW
```

The changeability and need to monitor/review changes are explicitly clarified in Annex A.4.1. fileciteturn33file0

**STATUS: CANDIDATE / 1 source**

**REL-003**

```text
INTERNAL / EXTERNAL INFORMATION SOURCES
        ↓
DETERMINATION OF RELEVANT ISSUES
```

Annex A.4.1 identifies multiple possible information sources, including internal documented information, meetings, government/statistical publications, professional and technical publications, and meetings with customers and relevant interested parties. fileciteturn33file0

**STATUS: CANDIDATE / 1 source**

### MECHANISM

**M-010 — Context determination and review**

The Source establishes a mechanism in which relevant external and internal issues are determined against purpose, strategic direction and intended QMS results; because such issues can change, changes are monitored and reviewed. Annex A.4.1 further states that the issues should be determined using a rational approach and addressed using risk-based and opportunity-based thinking. fileciteturn33file0

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

Important boundary: the Source does not prescribe a specific named method or tool. Therefore no Machine is created.

### CAPABILITY

**CAP-006 — Context awareness / ability to identify relevant internal and external issues**

CMOC interpretation of the requirement: the organization needs the ability to determine issues relevant to its purpose, strategic direction and intended QMS results, and to remain aware of changes to those issues.

**STATUS: CANDIDATE / 1 source**

### CORE CANDIDATE

**CORE-CANDIDATE-007 — Relevance-filtered context**

The system does not treat context as an undifferentiated list of factors. Relevant issues are selected by their relation to purpose, strategic direction and effect on intended results.

**STATUS: CANDIDATE / 1 source**

**CORE-CANDIDATE-008 — Context change as a management input**

Changes in relevant external and internal issues are something the organization needs to monitor and review because they can affect the ability to achieve intended QMS results.

**STATUS: CANDIDATE / 1 source**

### MACHINE

**NONE**

The clause defines a management mechanism and required capability, but does not specify a concrete reproducible organizational realization.

### CHAIN

**NONE**

The extracted relations form a structural management mechanism, but Clause 4.1 does not explicitly define a formal execution sequence sufficient to promote it to a confirmed Chain.

### ROLE

**NONE**

### PHYSICAL REALIZATION

**NONE**

### CMOC INTERPRETATION

Clause 4.1 introduces a powerful filter: the environment becomes a management input only after relevance is determined in relation to purpose, strategic direction and intended results.

A useful provisional structure is:

```text
CONTEXT
  ↓
ISSUES
  ↓
RELEVANCE
  ↓
EFFECT ON ABILITY
  ↓
INTENDED RESULTS
```

The Annex adds an important temporal dimension:

```text
RELEVANT CONTEXT
      ↓
CHANGES
      ↓
MONITOR / REVIEW
      ↓
UPDATED AWARENESS
```

This is CMOC interpretation. It does not mean that ISO defines “context” as a CMOC object or that the above graph is a canonical CMOC structure.

The climate-change sentence is not treated as a separate CMOC entity or Machine; it is an explicit example of determining relevance within the context requirement. fileciteturn33file0

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **4 CANDIDATES**
- GM: **2**
- REL: **3 CANDIDATES**
- MECHANISM: **M-010 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-006 CANDIDATE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **NONE**
- ROLE: NONE
- PHYSICAL REALIZATION: NONE
- CONFIRMATION: **1 source — ISO/DIS 9001:2025**
