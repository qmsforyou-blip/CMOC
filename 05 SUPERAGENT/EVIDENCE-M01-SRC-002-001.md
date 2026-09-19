# EVIDENCE-M01-SRC-002-001

**Production M01 evidence**

- **Run ID:** `RUN-SRC-002-M01-001`
- **Source ID:** `SRC-002`
- **Machine ID:** `M01-PRODUCTION`
- **Batch ID:** `BATCH-SRC-002-M01-001`
- **Input:** `SOURCE-002-PACKAGE-001-CONTROLLED-1-6`
- **Input status:** `PARTIAL`
- **Scope:** pages 1–6
- **Output type:** `EXTRACTION_RECORDS`
- **Result:** `ACCEPT`
- **Records:** 7
- **API model returned:** `gpt-5.6-sol`

## Execution chain

```
SOURCE_PACKAGE
→ SOURCE_PACKAGE integrity gate
→ BATCH-SRC-002-M01-001
→ M01-PRODUCTION
→ EXTRACTION_RECORDS
→ output contract QC
→ ACCEPT
```

## Extraction records

### EX-001
- **Location:** p1
- **Observation:** The Quality Systems Basics source is identified as revision March 2009.
- **Evidence:** Quality Systems Basics rev March 2009.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### EX-002
- **Location:** p2
- **Observation:** Quality Systems Basics defines 11 strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; and Managing Change.
- **Evidence:** 11 QSB Strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; Managing Change.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### EX-003
- **Location:** p3
- **Observation:** The supplier is assessed using the latest QSB Audit to identify strategies rated Red that require a workshop.
- **Evidence:** assess supplier per Latest QSB Audit to determine strategies Red and requiring workshop
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### EX-004
- **Location:** p3
- **Observation:** Required strategies are delivered, and an Action Plan is obtained for all Red and Yellow Audit questions.
- **Evidence:** deliver strategies as required and obtain Action Plan for all Red and Yellow Audit questions
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### EX-005
- **Location:** p4
- **Observation:** Quality Systems Basics uses common principles, common methods, and common processes, with a focus on one global language.
- **Evidence:** Common Principles, Common Methods, Common Processes. Focus — ONE LANGUAGE GLOBALLY.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### EX-006
- **Location:** p5
- **Observation:** Fast Response is intended to solve problems faster and earlier upstream through visual management.
- **Evidence:** solving problems faster & earlier upstream through visual management
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### EX-007
- **Location:** p6
- **Observation:** Fast Response separates section 1.2 Fast Response from section 1.3 Problem Solving.
- **Evidence:** Fast Response separates 1.2 Fast Response from 1.3 Problem Solving.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

## Traceability

```
SRC-002
→ SOURCE-002-PACKAGE-001-CONTROLLED-1-6
→ BATCH-SRC-002-M01-001
→ M01-PRODUCTION
→ EX-001 ... EX-007
```

## Evidence boundary

This evidence records the actual production M01 execution against the controlled pages 1–6 package. It does not represent extraction from the complete GM Quality System Basics Overview — Supplier Audit source.

The package was marked `PARTIAL`; therefore this run must not be represented as full-source extraction.

## Technical note

The package's `source_name` displayed in the PowerShell output with a character-encoding artifact (`вЂ”`). The extracted records themselves contain the expected source evidence. This observation is retained rather than silently corrected in the evidence.

## Status

**PRODUCTION M01 EVIDENCE — ACCEPTED**
