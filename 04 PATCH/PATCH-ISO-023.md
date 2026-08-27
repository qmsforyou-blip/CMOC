# PATCH-ISO-023

## Извещение на изменение

**0092+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 7.1.5 — Monitoring and measuring resources; 7.1.5.1; 7.1.5.2; Annex A.7.1.5

### SOURCE CLAIM

The organization shall determine and provide resources needed to ensure valid and reliable results when monitoring or measuring is used to verify conformity of products and services to specified requirements. The resources shall be suitable for the specific type of monitoring and measurement activities and shall be maintained to ensure continuing fitness for purpose. fileciteturn57file0

Where measurement traceability is a requirement, or is considered essential to provide confidence in the validity of measurement results, measuring equipment shall be calibrated or verified at specified intervals or prior to use, against measurement standards traceable to international or national standards; where no such standards exist, the basis used for calibration or verification shall be retained as documented information. Equipment shall be identified to determine its status, safeguarded from adjustments, damage or deterioration, and fitness for purpose shall be verified when necessary. fileciteturn57file0

Where measuring equipment is found to be unfit for its intended purpose, the organization shall determine whether the validity of previous measurement results has been adversely affected and take appropriate action as necessary. fileciteturn57file0

Annex A clarifies that monitoring is determining status, while measurement is determining a value. The same equipment may be used for indication, monitoring or measurement depending on purpose. It also notes that monitoring and measuring resources may be human or equipment resources, and that the organization determines what monitoring and measurement is necessary and how it is used. fileciteturn56file2

### TERMS
- monitoring
- measurement
- monitoring and measuring resource
- valid result
- reliable result
- suitability
- fitness for purpose
- measurement traceability
- calibration
- verification
- measurement standard
- status
- safeguard
- deterioration
- previous measurement result
- adverse effect
- documented information

### DISTINCTIONS

**DIS-001 — MONITORING ≠ MEASUREMENT**

Monitoring determines status; measurement determines a value. The same equipment may serve different functions depending on purpose.

**STATUS: CONFIRM — ISO-019 + ISO-023**

**DIS-002 — VALID RESULT ≠ RELIABLE RESULT**

The requirement explicitly combines validity and reliability of results.

**STATUS: CONFIRM — ISO-019 + ISO-023**

**DIS-003 — RESOURCE ≠ EQUIPMENT ONLY**

Annex A indicates that monitoring and measuring resources may be human or equipment resources.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-004 — SUITABILITY ≠ CONTINUING FITNESS FOR PURPOSE**

Resources must be suitable for the specific activity and maintained to ensure continuing fitness for purpose.

**STATUS: CONFIRM / UPDATE — ISO-019**

**DIS-005 — CALIBRATION ≠ VERIFICATION**

The Source presents calibration and verification as distinct ways of controlling measuring equipment against applicable measurement standards or specified bases.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-006 — MEASUREMENT TRACEABILITY ≠ CALIBRATION / VERIFICATION**

Traceability is a requirement/condition that may make calibration or verification necessary; it is not identical to either operation.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-007 — EQUIPMENT STATUS ≠ EQUIPMENT FITNESS**

Equipment shall be identified to determine its status, while fitness for purpose is a separate condition to be verified when necessary.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-008 — CURRENT EQUIPMENT FITNESS ≠ VALIDITY OF PREVIOUS RESULTS**

If equipment is found unfit, the organization separately determines whether previous measurement results were adversely affected.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-009 — CALIBRATION / VERIFICATION BASIS ≠ DOCUMENTED INFORMATION ITSELF**

Where no traceable measurement standard exists, the basis used for calibration or verification is retained as documented information; the basis and the information retaining it are distinct.

**STATUS: NEW / SINGLE-SOURCE**

### GM

**GM-001**

> Не путай monitoring с measurement: первое определяет status, второе — value; одно и то же средство может выполнять разные функции в зависимости от purpose.

**GM-002**

> Для измерительного ресурса контролируй не только наличие и калибровку, но его пригодность для конкретной деятельности и continuing fitness for purpose.

**GM-003**

> Если измерительный ресурс оказался непригодным, проверяй не только его текущее состояние, но и validity предыдущих результатов измерений.

**GM-004**

> Traceability, calibration и verification — разные элементы конструкции; не своди их в одно понятие.

### REL

**REL-001**

```text
MONITORING
    ≠
MEASUREMENT
```

**STATUS: CONFIRM — ISO-019 + ISO-023**

**REL-002**

```text
MONITOR / MEASURE
        ↓
RESOURCE
        ↓
VALID + RELIABLE RESULTS
```

**STATUS: CONFIRM / UPDATE — ISO-019**

**REL-003**

```text
RESOURCE
        ↓
SUITABLE FOR SPECIFIC ACTIVITY
        ↓
CONTINUING FITNESS FOR PURPOSE
```

**STATUS: CONFIRM / UPDATE — ISO-019**

**REL-004**

```text
TRACEABILITY REQUIREMENT
        ↓
CALIBRATION / VERIFICATION
        ↓
MEASUREMENT STANDARD
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-005**

```text
NO TRACEABLE STANDARD
        ↓
BASIS FOR CALIBRATION / VERIFICATION
        ↓
RETAIN AS DOCUMENTED INFORMATION
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-006**

```text
EQUIPMENT
        ↓
STATUS IDENTIFICATION
        ↓
SAFEGUARD
        ↓
FITNESS FOR PURPOSE
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-007**

```text
EQUIPMENT UNFIT
        ↓
ASSESS PREVIOUS MEASUREMENT RESULTS
        ↓
ACTION AS NECESSARY
```

**STATUS: NEW / SINGLE-SOURCE**

### MECHANISM

**M-028 — Measurement-result validity assurance**

```text
MONITOR / MEASURE
        ↓
DETERMINE REQUIRED RESOURCE
        ↓
ENSURE SUITABILITY
        ↓
MAINTAIN FITNESS
        ↓
CALIBRATE / VERIFY WHEN REQUIRED
        ↓
SAFEGUARD + IDENTIFY STATUS
        ↓
VALID + RELIABLE RESULT
        ↓
IF UNFIT:
ASSESS PREVIOUS RESULTS
        ↓
ACTION
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

This extends M-022 from ISO-019 but is kept separate because 7.1.5 provides the more explicit control construction for measurement resources.

### CAPABILITY

**CAP-023 — Measurement assurance capability**

CMOC interpretation: ability to determine and maintain monitoring/measuring resources so that required results are valid and reliable, including traceability controls and response to detected unfitness.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATES

**CORE-CANDIDATE-038 — Measurement is a controlled source of evidence**

Where monitoring/measurement is used to verify conformity, the resource is controlled specifically to ensure validity and reliability of the resulting evidence.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-039 — Invalidity can propagate backward to previous results**

Detection of an unfit measuring resource triggers assessment of the validity of previous measurement results.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-040 — Resource status is itself a control object**

Equipment status must be identifiable, while fitness for purpose is separately maintained/verified.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

The clause defines a control mechanism but does not prescribe a complete reproducible organizational implementation qualifying as a Machine.

### CHAIN

**CHAIN-CANDIDATE-015 — Measurement assurance**

```text
REQUIREMENT TO MONITOR / MEASURE
 ↓
RESOURCE
 ↓
SUITABILITY
 ↓
CALIBRATION / VERIFICATION
 ↓
STATUS / SAFEGUARDING
 ↓
MEASUREMENT
 ↓
VALID + RELIABLE RESULT
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-016 — Unfit resource response**

```text
RESOURCE UNFIT
 ↓
ASSESS PREVIOUS RESULTS
 ↓
DETERMINE ADVERSE EFFECT
 ↓
ACTION AS NECESSARY
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

### ROLE

**NONE**

### PHYSICAL REALIZATION

**NONE**

The Source gives equipment and human resources as possible monitoring/measuring resources, but does not prescribe a specific CMOC realization.

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

A precise new observation:

```text
NO TRACEABLE MEASUREMENT STANDARD
        ↓
BASIS FOR CALIBRATION / VERIFICATION
        ↓
RETAIN AS DOCUMENTED INFORMATION
```

This is an explicit requirement for documented information. It is not automatically a "record". The Document / Record architecture remains deferred to Clause 7.5.

### CMOC INTERPRETATION

ISO-023 gives a stronger version of the earlier resource pattern:

```text
PURPOSE
 ↓
REQUIRED MONITOR / MEASURE
 ↓
RESOURCE
 ↓
SUITABILITY
 ↓
FITNESS
 ↓
VALID + RELIABLE RESULT
```

But the most valuable new structure is backward propagation:

```text
RESOURCE STATUS
        ↓
RESULT VALIDITY
```

More precisely:

```text
UNFIT RESOURCE
        ↓
QUESTION THE VALIDITY OF PREVIOUS RESULTS
        ↓
ASSESS
        ↓
ACTION
```

The important CMOC interpretation is:

> **The status of a resource can affect the epistemic status of results already produced by that resource.**

This is CMOC interpretation, not an ISO definition.

This may become a significant CMOC relation between `Resource`, `Evidence/Result`, `Status` and `Decision/Action`, but we do not create those Core entities here without broader confirmation.

### CROSS-CLAUSE OBSERVATION

ISO-019 introduced the resource-suitability relation. ISO-023 makes it operational for monitoring and measurement and adds a new backward relation: resource unfitness can trigger reassessment of previous results.

The earlier pattern is strengthened:

```text
RESOURCE
 ↓
SUITABILITY / FITNESS
 ↓
RESULT
```

and ISO-023 adds:

```text
RESOURCE STATUS
 ↓
VALIDITY OF RESULT
```

This is a **MULTI-CONFIRMATION CANDIDATE** for a more general CMOC principle of result validity depending on the status of the mechanism/resource that produced it.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **9**
- GM: **4**
- REL: **7**
- MECHANISM: **M-028 NEW / SINGLE-SOURCE; extends M-022**
- CAPABILITY: **CAP-023 CANDIDATE**
- CORE CANDIDATES: **3**
- MACHINE: **NONE**
- CHAIN: **2 CANDIDATES**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Documented information: **explicit requirement for calibration/verification basis where no traceable standard exists**
- Document / Record: **distinction remains open for Clause 7.5**
- CROSS-CLAUSE: **ISO-019 strengthened; new Resource status → Result validity relation identified**
