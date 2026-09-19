# EVIDENCE-M02-SRC-002-001

**Production M02 evidence**

- **Run ID:** `RUN-SRC-002-M02-001`
- **Source ID:** `SRC-002`
- **Machine ID:** `M02-PRODUCTION`
- **Batch ID:** `BATCH-SRC-002-M02-001`
- **Input:** `EXTRACTION_RECORDS` from `BATCH-SRC-002-M01-001`
- **Input records:** 7
- **Output type:** `DISTINCTION_RECORDS`
- **Result:** `ACCEPT`
- **Semantic QC:** `PASS`

## Execution chain

```
M01-PRODUCTION
→ EXTRACTION_RECORDS
→ M02-PRODUCTION
→ DISTINCTION_RECORDS
→ output contract QC
→ ACCEPT
→ semantic QC PASS
```

## Distinction records

### DIS-001
- **Extraction:** EX-001
- **Distinction:** Identifies the Quality Systems Basics source as the March 2009 revision.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### DIS-002
- **Extraction:** EX-002
- **Distinction:** Defines 11 QSB strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; and Managing Change.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### DIS-003
- **Extraction:** EX-003
- **Distinction:** Requires assessment of the supplier using the latest QSB Audit to identify Red-rated strategies requiring a workshop.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### DIS-004
- **Extraction:** EX-004
- **Distinction:** Requires delivery of applicable strategies and an Action Plan for every Red and Yellow Audit question.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### DIS-005
- **Extraction:** EX-005
- **Distinction:** Defines QSB as using common principles, methods, and processes with a focus on one global language.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### DIS-006
- **Extraction:** EX-006
- **Distinction:** Defines Fast Response as solving problems faster and earlier upstream through visual management.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

### DIS-007
- **Extraction:** EX-007
- **Distinction:** Separates section 1.2 Fast Response from section 1.3 Problem Solving.
- **Uncertainty:** CLEAR
- **Source:** SRC-002

## Semantic QC

All seven `EX → DIS` mappings were checked against the corresponding extraction records.

- Cardinality: 7 → 7
- Order and extraction IDs: preserved
- Source grounding: preserved
- External knowledge: not added
- Cross-record synthesis: not detected
- Inferred causal/logical/justificatory links: not detected
- `DIS-005`: no unsupported “basis for” relationship retained

## Traceability

```
SRC-002
→ SOURCE-002-PACKAGE-001-CONTROLLED-1-6
→ BATCH-SRC-002-M01-001
→ EXTRACTION_RECORDS
→ BATCH-SRC-002-M02-001
→ M02-PRODUCTION
→ DIS-001 ... DIS-007
```

## Evidence boundary

This evidence records M02 processing of the seven extraction records produced from the controlled pages 1–6 package. It does not represent processing of the complete GM Quality System Basics Overview — Supplier Audit source.

The upstream package was marked `PARTIAL`; therefore this run must not be represented as full-source processing.

## Re-run note

The M02 run was repeated after tightening the M02 semantic prompt to prohibit inferred relationships between source statements. The runner retained the same explicit `RUN-ID` and `BATCH-ID`; this evidence therefore records the accepted result of that controlled re-run rather than inventing a new batch identifier.

## Status

**PRODUCTION M02 EVIDENCE — ACCEPTED**
