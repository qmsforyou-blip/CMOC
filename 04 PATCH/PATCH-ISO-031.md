# PATCH-ISO-031

## Извещение на изменение

**0100+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 8.3 — Design and development of products and services; 8.3.1–8.3.6; Annex A.8.3

### SOURCE CLAIM

The organization shall establish, implement and maintain a design and development process appropriate to ensure subsequent provision of products and services. The process can include cycles of review, verification, validation and feedback, allowing flexibility throughout design and development phases. fileciteturn82file5

Design and development planning shall consider the nature, duration and complexity of activities; process stages and reviews; verification and validation; responsibilities and authorities; internal and external resources; interfaces between persons; involvement of customers and users; requirements for subsequent provision; level of control expected by customers and other interested parties; and documented information needed as evidence. fileciteturn82file6

Design and development inputs shall include requirements essential for the specific types of products and services, considering functional/performance requirements, information from previous similar activities, statutory/regulatory requirements, committed standards/codes, and potential consequences of failure. Inputs shall be complete, unambiguous and adequate; conflicting inputs shall be resolved. Inputs can evolve as design progresses through repeated cycles of development and validation. fileciteturn82file6

Design and development controls shall ensure that results to be achieved are defined; reviews evaluate the ability of design results to meet requirements; verification ensures outputs meet input requirements; validation ensures resulting products/services meet requirements for specified application or intended use; problems found during reviews, verification or validation are addressed; and documented information is available as evidence. Review, verification and validation have distinct purposes and may be conducted separately or in combination as suitable. fileciteturn82file2

Outputs shall meet input requirements, be adequate for subsequent provision processes, include/reference monitoring and measuring requirements and acceptance criteria as appropriate, and specify characteristics essential for intended purpose and safe/proper provision. Changes during or after design and development shall be determined, reviewed and controlled to prevent adverse impact on conformity. Evidence shall be available for changes, review results, authorization of changes and actions taken to prevent adverse impacts. fileciteturn82file2

Annex A.8.3 describes design and development as processes transforming requirements for products and services into specified product/service characteristics. It distinguishes verification as checking that design and development and obtained results meet determined inputs; review as critical evaluation at appropriate stages; and validation as practical ascertainment that design and development outputs meet input requirements. fileciteturn82file8

### TERMS
- design and development process
- design and development planning
- design and development inputs
- design and development controls
- design and development outputs
- design and development changes
- review
- verification
- validation
- feedback
- input requirements
- specified application
- intended use
- subsequent provision
- acceptance criteria
- essential characteristics

### DISTINCTIONS

**DIS-001 — DESIGN AND DEVELOPMENT ≠ RESULTING PRODUCT/SERVICE**

Design and development is a set of processes that transforms requirements into specified product/service characteristics.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-002 — DESIGN REVIEW ≠ VERIFICATION ≠ VALIDATION**

The Source explicitly states that these have distinct purposes.

- Review: critically evaluate what was designed and its ability to meet expected requirements.
- Verification: check design/development outputs against input requirements.
- Validation: ascertain that resulting product/service meets requirements for specified application or intended use.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**DIS-003 — DESIGN INPUT ≠ DESIGN OUTPUT**

Inputs establish requirements for design and development; outputs are required to meet those inputs and satisfy subsequent provision needs.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-004 — DESIGN INPUT ≠ FIXED INPUT**

Inputs are not always fully defined or known initially and can evolve through repeated development and validation cycles.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-005 — REQUIREMENT ≠ DESIGN CHARACTERISTIC**

Annex A describes design and development as transforming requirements into specified product/service characteristics.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-006 — VERIFICATION ≠ VALIDATION**

Verification addresses conformity of design/development outputs with input requirements; validation addresses requirements for specified application or intended use.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**DIS-007 — REVIEW ≠ ACCEPTANCE**

Review evaluates the ability of design results to meet requirements; acceptance criteria are included/referenced in design outputs as appropriate and concern subsequent product/service realization.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-008 — DESIGN CHANGE ≠ DESIGN CHANGE AUTHORIZATION**

Changes, their review, authorization and actions to prevent adverse impacts are separately evidenced.

**STATUS: NEW / SINGLE-SOURCE**

**DIS-009 — DESIGN PROCESS CONTROL ≠ PRODUCT/SERVICE CONTROL**

8.3 controls the design and development process so that its outputs support subsequent provision; it is not identical to control of production/service provision.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-010 — DESIGN OUTPUT ≠ SUBSEQUENT PROVISION PROCESS**

Outputs must be adequate for subsequent processes, but the output and the subsequent process remain distinct.

**STATUS: NEW / SINGLE-SOURCE**

### GM

**GM-001**

> Не смешивай review, verification и validation: они отвечают на разные вопросы.

**GM-002**

> Рассматривай design and development как процесс преобразования requirements в specified characteristics.

**GM-003**

> Не предполагай, что design inputs полностью известны в начале: они могут развиваться через циклы development и validation.

**GM-004**

> Проектируй outputs так, чтобы они были пригодны не только для выполнения input requirements, но и для последующих процессов provision.

**GM-005**

> Изменения design and development должны проходить через review/control, authorization и действия по предотвращению adverse impacts.

### REL

**REL-001**

```text
REQUIREMENTS
        ↓
DESIGN AND DEVELOPMENT
        ↓
SPECIFIED PRODUCT / SERVICE CHARACTERISTICS
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-002**

```text
DESIGN INPUTS
        ↓
DESIGN / DEVELOPMENT
        ↓
DESIGN OUTPUTS
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-003**

```text
DESIGN INPUTS
        ↓
VERIFICATION
        ↓
OUTPUTS MEET INPUT REQUIREMENTS
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-004**

```text
DESIGN RESULTS
        ↓
REVIEW
        ↓
ABILITY TO MEET REQUIREMENTS
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-005**

```text
DESIGN OUTPUTS
        ↓
VALIDATION
        ↓
SPECIFIED APPLICATION / INTENDED USE
        ↓
REQUIREMENTS MET
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-006**

```text
REVIEW / VERIFICATION / VALIDATION
        ↓
PROBLEM IDENTIFIED
        ↓
NECESSARY ACTION
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-007**

```text
DESIGN OUTPUT
        ↓
SUBSEQUENT PROVISION PROCESS
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-008**

```text
DESIGN OUTPUT
        ↓
MONITORING / MEASURING REQUIREMENTS
        +
ACCEPTANCE CRITERIA
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-009**

```text
DESIGN CHANGE
        ↓
REVIEW
        ↓
AUTHORIZATION
        ↓
CONTROL
        ↓
PREVENT ADVERSE IMPACT
```

**STATUS: NEW / SINGLE-SOURCE**

**REL-010**

```text
DEVELOPMENT CYCLE
        ↓
REVIEW / VERIFICATION / VALIDATION
        ↓
FEEDBACK
        ↺
DEVELOPMENT
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MECHANISM

**M-036 — Requirements-to-characteristics design control**

```text
REQUIREMENTS
        ↓
DESIGN INPUTS
        ↓
DESIGN / DEVELOPMENT
        ↓
REVIEW
        ↓
VERIFICATION
        ↓
VALIDATION
        ↓
DESIGN OUTPUTS
        ↓
SUBSEQUENT PROVISION
```

With feedback/evolution loop:

```text
DEVELOPMENT
   ↓
REVIEW / VERIFICATION / VALIDATION
   ↓
FEEDBACK
   ↺
DEVELOPMENT
```

With change-control branch:

```text
DESIGN CHANGE
   ↓
REVIEW
   ↓
AUTHORIZATION
   ↓
CONTROL
   ↓
PREVENT ADVERSE IMPACT
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CAPABILITY

**CAP-031 — Design and development control capability**

CMOC interpretation: ability to transform requirements into specified product/service characteristics through controlled design and development, using appropriate review, verification, validation, feedback and change control.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATES

**CORE-CANDIDATE-071 — Requirement can be transformed into specified characteristics**

Design and development is explicitly described as a process transforming requirements into specified product/service characteristics.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-072 — Review, verification and validation are distinct controls**

The three activities have distinct purposes and should not be collapsed into a generic “check”.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-073 — Design inputs can evolve**

Inputs can evolve during design through repeated cycles of development and validation.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-074 — Output must support the next process**

Design output is not complete merely because it meets input requirements; it must also be adequate for subsequent provision processes.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-075 — Design change requires controlled consequence management**

Design changes require determination, review and control to avoid adverse impact on conformity, with evidence of review, authorization and preventive actions.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**MACHINE-CANDIDATE-001 — Controlled design-and-development cycle**

Potential candidate because the Source defines a reproducible process construction containing defined inputs, transformation, distinct control operations, outputs, feedback and change control.

```text
INPUTS
 ↓
DESIGN / DEVELOPMENT
 ↓
REVIEW
 ↓
VERIFICATION
 ↓
VALIDATION
 ↓
OUTPUT
 ↺ FEEDBACK
```

However, this is still only a **MACHINE-CANDIDATE / SINGLE-SOURCE**. The Source describes the generic process, not a particular organizational implementation. Confirmation from another independent source is required before promotion.

### CHAIN

**CHAIN-CANDIDATE-034 — Design transformation chain**

```text
REQUIREMENTS
 ↓
DESIGN INPUTS
 ↓
DESIGN / DEVELOPMENT
 ↓
SPECIFIED CHARACTERISTICS / OUTPUTS
 ↓
SUBSEQUENT PROVISION
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-035 — Design control cycle**

```text
DESIGN / DEVELOPMENT
 ↓
REVIEW
 ↓
VERIFICATION
 ↓
VALIDATION
 ↓
FEEDBACK
 ↺
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

**CHAIN-CANDIDATE-036 — Design change control**

```text
CHANGE
 ↓
REVIEW
 ↓
AUTHORIZATION
 ↓
CONTROL
 ↓
PREVENT ADVERSE IMPACT
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

### ROLE

**NONE**

Responsibilities and authorities are planning considerations, but no specific CMOC role is defined.

### PHYSICAL REALIZATION

**NONE**

The Source gives process requirements, not a specific organizational or material implementation.

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

8.3 repeatedly requires documented information as evidence of inputs, controls/activities, outputs and changes. In particular, evidence may concern:

```text
INPUTS
REVIEW / VERIFICATION / VALIDATION
OUTPUTS
CHANGES
REVIEW RESULTS
AUTHORIZATION
ACTIONS TO PREVENT ADVERSE IMPACT
```

This strengthens the distinction from ISO-028: documented information can provide evidence at multiple control points of one evolving process. It does not mean that all such information is automatically a single Record or that the design process itself is documented information.

### CMOC INTERPRETATION

The strongest architecture emerging from 8.3 is:

```text
REQUIREMENT
        ↓
INPUT
        ↓
TRANSFORMATION
        ↓
CONTROL
        ├── REVIEW
        ├── VERIFICATION
        └── VALIDATION
        ↓
OUTPUT
        ↓
SUBSEQUENT PROCESS
```

with a feedback loop:

```text
OUTPUT / CONTROL RESULT
        ↓
FEEDBACK
        ↺
DESIGN / DEVELOPMENT
```

and a change-control loop:

```text
CHANGE
 ↓
REVIEW
 ↓
AUTHORIZATION
 ↓
CONTROL
 ↓
CONSEQUENCE PREVENTION
```

The critical CMOC interpretation is:

> **Design and development is a transformation mechanism: requirements are converted into specified characteristics, while review, verification and validation are distinct control functions around that transformation.**

This is CMOC interpretation, not an ISO definition.

A second important interpretation:

> **Verification answers “does the output meet the input requirements?”, while validation addresses “does the resulting product/service meet requirements for the specified application or intended use?”**

This distinction is explicitly supported by Annex A.8.3. fileciteturn82file8

A third:

> **The design process is not necessarily linear. Inputs can evolve and the process can contain repeated cycles of development, review, verification, validation and feedback.**

### CROSS-CLAUSE OBSERVATION

ISO-030 established the boundary:

```text
REQUIREMENT
 ↓
ABILITY / REVIEW
 ↓
COMMITMENT
```

ISO-029 established:

```text
REQUIREMENT
 ↓
PROCESS CRITERIA
 ↓
CONTROLLED EXECUTION
 ↓
CONFORMITY
```

ISO-031 now adds the transformation layer between requirement and operational realization:

```text
REQUIREMENT
 ↓
DESIGN INPUT
 ↓
DESIGN / DEVELOPMENT
 ↓
SPECIFIED CHARACTERISTICS
 ↓
OPERATIONAL PROVISION
```

This gives a major cross-clause candidate:

```text
NEED / REQUIREMENT
 ↓
REVIEW / ABILITY
 ↓
DESIGN / DEVELOPMENT
 ↓
VERIFICATION / VALIDATION
 ↓
SPECIFIED OUTPUT
 ↓
OPERATIONAL PROVISION
```

**MULTI-CONFIRMATION CANDIDATE — not yet Core.**

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **10**
- GM: **5**
- REL: **10**
- MECHANISM: **M-036 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-031 CANDIDATE**
- CORE CANDIDATES: **5**
- MACHINE: **MACHINE-CANDIDATE-001 / SINGLE-SOURCE**
- CHAIN: **3 CANDIDATES**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Document / Documented information / Record: **evidence exists at multiple design-control points; classification as Record remains context-dependent**
- CROSS-CLAUSE: **Requirement → Design → Control → Output → Operation is a major multi-source candidate**
