# PATCH-ISO-007

## Извещение на изменение

**0076+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 2 — Normative references

### SOURCE CLAIM

The documents listed in Clause 2 are referred to in the text in such a way that some or all of their content constitutes requirements of ISO/DIS 9001:2025.

For dated references, only the edition cited applies.

For undated references, the latest edition of the referenced document, including any amendments, applies.

The listed references are:
- ISO 3534-2:2006, Statistics — Vocabulary and symbols — Part 2: Applied statistics
- ISO 9000:2015, Quality management systems — Fundamentals and vocabulary
- ISO/CD 9000, Quality management systems — Fundamentals and vocabulary
- EN ISO 9001:2015, Quality management systems — Requirements (ISO 9001:2015)

### TERMS
- normative reference
- requirements
- dated reference
- undated reference
- edition
- amendment
- referenced document

### DISTINCTIONS

**DIS-001 — NORMATIVE REFERENCE ≠ INFORMATIVE REFERENCE**

A document is a normative reference when some or all of its content constitutes requirements of this document. Clause 2 therefore establishes a different status from a source cited merely for information or guidance.

**STATUS: CANDIDATE / 1 source**

**DIS-002 — DATED REFERENCE ≠ UNDATED REFERENCE**

The applicable edition rule differs according to whether the reference is dated or undated.

**STATUS: CANDIDATE / 1 source**

**DIS-003 — CITED EDITION ≠ LATEST EDITION**

For dated references, the cited edition governs; for undated references, the latest edition, including amendments, governs.

**STATUS: CANDIDATE / 1 source**

### GM

**GM-001**

> Treat a referenced document as a source of requirements only when the reference is normative; determine the applicable content according to its reference status.

**GM-002**

> Bind a dated normative dependency to its cited edition; resolve an undated normative dependency to the latest applicable edition and amendments.

### REL

**REL-001**

```text
NORMATIVE REFERENCE
        ↓
CONTENT OF REFERENCED DOCUMENT
        ↓
REQUIREMENT OF THIS DOCUMENT
```

**STATUS: CANDIDATE / 1 source**

**REL-002**

```text
DATED REFERENCE
        ↓
CITED EDITION
```

**STATUS: CANDIDATE / 1 source**

**REL-003**

```text
UNDATED REFERENCE
        ↓
LATEST EDITION
        +
APPLICABLE AMENDMENTS
```

**STATUS: CANDIDATE / 1 source**

### MECHANISM

**M-007 — Normative dependency with controlled edition resolution**

The Source establishes a mechanism by which external referenced documents become a source of requirements, with the applicable version resolved differently for dated and undated references.

**CLASS: M**

**STATUS: CANDIDATE / 1 source**

Important boundary: Clause 2 does not specify an organizational implementation for maintaining or applying these references. Therefore this remains M, not MACHINE.

### CAPABILITY

**NONE**

Clause 2 establishes a normative dependency rule, but does not itself state a distinct organizational capability.

### CORE CANDIDATE

**NONE**

The mechanism is potentially relevant to a future CMOC architecture of controlled dependencies, but one source fragment is insufficient to elevate it to a Core candidate.

### MACHINE

**NONE**

### CHAIN

**NONE**

The dated/undated rules are conditional resolution rules, not an execution chain.

### ROLE

**NONE**

### PHYSICAL REALIZATION

**NONE**

### CMOC INTERPRETATION

The significant extraction is a general dependency structure:

```text
REFERENCED SOURCE
      ↓
NORMATIVE DEPENDENCY
      ↓
APPLICABLE VERSION RULE
      ↓
REQUIREMENT SOURCE
```

This is a CMOC interpretation, not a direct ISO definition.

The fragment introduces a potentially reusable architectural pattern: an external knowledge/requirement source can become part of a governing system through an explicit dependency and version-resolution rule. This is deliberately kept as a candidate and is not yet generalized to CMOC Core.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: 3 CANDIDATES
- GM: 2
- REL: 3 CANDIDATES
- MECHANISM: M-007 NEW / SINGLE-SOURCE
- CAPABILITY: NONE
- CORE CANDIDATE: NONE
- MACHINE: NONE
- CHAIN: NONE
- ROLE: NONE
- PHYSICAL REALIZATION: NONE
- CONFIRMATION: 1 source — ISO/DIS 9001:2025
