# GM-016 — Step 5: Verify Effectiveness of Actions

**Извещение на изменение:** 0127+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Section:** Fast Response → 1.3 Problem Solving → Step 5 — Verify Effectiveness of Actions  
**Status:** CANDIDATE / SINGLE-SOURCE

---

## SOURCE

GM defines Step 5 as **Follow Up and Check**. The source requires:

- implement Layered Process Audits (LPA) to verify that changes to the system are being performed consistently and working as intended;
- verify effectiveness through measurement and data;
- establish a verification period (duration/date);
- determine who will follow up;
- create a standardized process or method;
- remove excess work from containment.

---

## LOCATION

Source pp. 43–44, Step 5 — Verify Effectiveness of Actions.

---

## TERMS

- Follow Up and Check
- Layered Process Audits (LPA)
- measurement
- data
- verification period
- duration/date
- follow-up owner
- standardized process or method
- containment
- effectiveness

---

## DISTINCTIONS

### DIS-GM-016-01

**Implementation ≠ effectiveness.**

The fact that an action has been implemented does not establish that it is effective. GM creates a separate Step 5 for verification.

### DIS-GM-016-02

**Verification of implementation ≠ verification of effectiveness.**

LPA is used to verify that the system change is being performed consistently and working as intended; measurement and data are also required to verify effectiveness.

### DIS-GM-016-03

**Verification ≠ indefinite observation.**

GM requires an explicit verification period with duration/date.

### DIS-GM-016-04

**Action ≠ standardized process or method.**

After effectiveness is verified, GM requires creation of a standardized process or method. This anticipates the separate Step 6 — Institutionalize.

### DIS-GM-016-05

**Containment ≠ permanent solution.**

GM explicitly calls for removing excess work from containment after the effectiveness of the action has been verified.

---

## GM-FORMULATIONS

- “Implement Layered Process Audits to verify changes to the system are being performed consistently and working as intended.”
- “Verify effectiveness through measurement and data.”
- “Establish a verification period (duration/date).”
- “Determine who will follow up.”
- “Create a standardized process or method.”
- “Remove excess work from containment.”

---

## EXTRACTION

The source describes a controlled verification loop:

```text
IMPLEMENTED CHANGE
        ↓
FOLLOW UP / CHECK
        ↓
┌───────────────────────────────┐
│ LPA — performed consistently? │
│ Measurement / Data            │
│ Working as intended?          │
└───────────────────────────────┘
        ↓
VERIFICATION PERIOD
        ↓
FOLLOW-UP OWNER
        ↓
EFFECTIVENESS VERIFIED
        ↓
STANDARDIZED PROCESS / METHOD
        ↓
REMOVE EXCESS CONTAINMENT
```

---

## REL

Confirmed local relations from the source:

```text
Corrective Action Implementation
        ↓
Follow Up and Check
        ↓
LPA + Measurement / Data
        ↓
Verification Period
        ↓
Effectiveness
        ↓
Standardized Process / Method
        ↓
Reduced / Removed Excess Containment
```

The source also preserves the larger sequence:

```text
Step 4 — Implement Corrective Action
        ↓
Step 5 — Verify Effectiveness of Actions
        ↓
Step 6 — Institutionalize
```

---

## MECHANISM

### CANDIDATE — Effectiveness Verification Mechanism

**Input:** implemented corrective action.

**Transformation:** subject the changed system to defined follow-up, LPA, measurement/data and a defined verification period.

**Output:** evidence-based determination of whether the change is working as intended.

**Organizational effect:** the organization does not treat implementation itself as proof of effectiveness; it creates a bounded verification cycle before institutionalization and removal of excess containment.

---

## CAPABILITY

**NONE**

No separate capability is extracted from this single source fragment.

---

## CORE CANDIDATE

> **Effectiveness Verification — a reproducible operation that subjects an implemented change to defined follow-up, layered audit, measurement/data and a verification period in order to establish whether the change is working as intended.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## MACHINE

### CANDIDATE MACHINE — Effectiveness Verification

```text
IMPLEMENTED CHANGE
        ↓
[ VERIFICATION ]
        │
        ├── LPA
        ├── measurement / data
        ├── verification period
        └── follow-up owner
        ↓
EFFECTIVENESS DETERMINATION
        ↓
STANDARDIZE / REMOVE EXCESS CONTAINMENT
```

The machine test is satisfied at candidate level:

- **Input:** implemented change;
- **Transformation:** bounded verification using audits and evidence;
- **Output:** effectiveness determination;
- **Effect:** provides the basis for standardization and withdrawal of unnecessary containment.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CHAIN

### SOURCE-SUPPORTED

```text
Implement Corrective Action
        ↓
LPA / Measurement / Data
        ↓
Verification Period
        ↓
Follow Up
        ↓
Effectiveness
        ↓
Standardized Process / Method
        ↓
Remove Excess Containment
```

Do not collapse this into the Step 4 implementation chain or Step 6 institutionalization chain.

---

## STATUS

**CANDIDATE / SINGLE-SOURCE**

No CANON status assigned.

---

## CMOC INTERPRETATION

The important engineering distinction is:

> **A changed system is not yet a proven effective system.**

GM inserts a distinct verification operation between implementation and institutionalization:

```text
SOLUTION
   ↓
IMPLEMENT
   ↓
VERIFY
   ↓
INSTITUTIONALIZE
```

Within Verify, GM combines **process-conformance observation (LPA)** with **measurement/data** and a **defined verification period**. This creates a bounded evidence-producing step rather than an assertion that the action worked.

This is a CMOC interpretation, not a GM claim about CMOC.

---

## INTER-SOURCE NOTE

Potentially relevant to later cross-source comparison with ISO/DIS 9001:2025, but no cross-source confirmation is asserted in this PATCH.
