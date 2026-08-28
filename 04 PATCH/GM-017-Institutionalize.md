# GM-017 — Step 6: Institutionalize

**Извещение на изменение:** 0128+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Section:** Fast Response → 1.3 Problem Solving → Step 6 — Institutionalize  
**Status:** CANDIDATE / SINGLE-SOURCE

---

## SOURCE

GM defines Step 6 — Institutionalize through three linked actions:

1. Identify similar products and processes which potentially have or may produce the same failure mode.
2. Send a copy of the Problem Solving Report to other Departments/Plants with the potential of experiencing the problem.
3. Implement the solution across the organization.
4. Update necessary documentation:
   - PFMEA
   - Control Plan
   - Error Proofing Verification
   - Standardized Work
   - Operator Instructions
   - Lessons Learned

The source therefore treats institutionalization as extending the validated solution beyond the original case and changing the organizational system/documentation so the learning is retained.

---

## LOCATION

**p. 44 — Step 6: Institutionalize**

---

## TERMS

- Institutionalize
- similar products
- similar processes
- same failure mode
- Problem Solving Report
- Departments / Plants
- implement the solution across the organization
- PFMEA
- Control Plan
- Error Proofing Verification
- Standardized Work
- Operator Instructions
- Lessons Learned

---

## DISTINCTIONS

### DIS-GM-017-01

**Local solution ≠ institutionalized solution.**

Implementing the solution where the original problem occurred is not the end of Step 6. GM requires implementation across the organization.

### DIS-GM-017-02

**Original problem ≠ only relevant problem.**

GM requires identification of similar products and processes that may have or produce the same failure mode.

### DIS-GM-017-03

**Problem Solving Report ≠ Lessons Learned.**

GM uses the Problem Solving Report as an information-transfer vehicle to other Departments/Plants, while Lessons Learned is one of the organizational documents to be updated.

### DIS-GM-017-04

**Implementation ≠ institutionalization.**

Step 4 implements corrective action. Step 6 extends the solution across the organization and updates the relevant system artifacts.

### DIS-GM-017-05

**Documentation update ≠ clerical update.**

The listed documents are operational system elements: PFMEA, Control Plan, Error Proofing Verification, Standardized Work, Operator Instructions and Lessons Learned. Updating them embeds the learning into the way work is planned, controlled, performed and remembered.

---

## GM-FORMULATIONS

- “Identify similar products and processes which potentially have or may produce the same failure mode.”
- “Send a copy of this Problem Solving Report to other Departments/Plants with the potential of experiencing this problem.”
- “Implement the solution across the organization.”
- “Update the necessary documentation.”

---

## EXTRACTION

```text
VERIFIED / EFFECTIVE SOLUTION
          ↓
IDENTIFY SIMILAR PRODUCTS / PROCESSES
          ↓
IDENTIFY POTENTIAL SAME FAILURE MODE
          ↓
TRANSFER PROBLEM SOLVING REPORT
TO OTHER DEPARTMENTS / PLANTS
          ↓
IMPLEMENT SOLUTION ACROSS ORGANIZATION
          ↓
UPDATE SYSTEM DOCUMENTATION
  ├── PFMEA
  ├── Control Plan
  ├── Error Proofing Verification
  ├── Standardized Work
  ├── Operator Instructions
  └── Lessons Learned
          ↓
INSTITUTIONALIZED LEARNING
```

---

## REL

Source-supported relations:

```text
Problem Solving
      ↓
Solution
      ↓
Verify Effectiveness
      ↓
Institutionalize
      ├── similar products / processes
      ├── other Departments / Plants
      ├── organization-wide implementation
      └── documentation update
```

The six-step Problem Solving sequence is preserved:

```text
1 Define the Problem
2 Contain the Problem
3 Find the Point of Cause
4 Implement Corrective Action
5 Verify Effectiveness of Actions
6 Institutionalize
```

---

## MECHANISM

### CANDIDATE — Institutionalization / Learning Propagation Mechanism

**Input:** verified effective solution / completed problem-solving result.

**Transformation:** identify analogous exposure, transfer the Problem Solving Report, deploy the solution across the organization, and update the specified system artifacts.

**Output:** solution and learning embedded beyond the original problem location.

**Organizational effect:** the response is converted from a local fix into an organization-level change and retained in operational knowledge/control artifacts.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CAPABILITY

**CANDIDATE — Organizational Learning Propagation**

GM explicitly requires transfer of the Problem Solving Report to other potentially affected Departments/Plants and updating Lessons Learned. However, capability classification remains candidate because this is a single-source extraction.

---

## CORE CANDIDATE

> **Institutionalization — a reproducible operation that extends a verified solution to analogous products/processes and organizational locations and embeds the resulting learning in specified operational documents and methods.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## MACHINE

### CANDIDATE MACHINE — Institutionalization

```text
VERIFIED EFFECTIVE SOLUTION
          ↓
[ INSTITUTIONALIZE ]
          │
          ├── find similar exposure
          ├── transfer Problem Solving Report
          ├── deploy solution organization-wide
          └── update system artifacts
          ↓
ORGANIZATIONAL EMBEDDED SOLUTION
          ↓
REDUCED RISK OF REPEATING / REPRODUCING SAME FAILURE MODE
```

Engineering test:

- **Input:** verified effective solution;
- **Transformation:** propagation + system embedding;
- **Output:** solution incorporated beyond original location;
- **Organizational effect:** learning becomes part of the organization rather than remaining local to the original case.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CHAIN

### SOURCE-SUPPORTED

```text
Verify Effectiveness
      ↓
Identify Similar Products / Processes
      ↓
Transfer Problem Solving Report
      ↓
Implement Solution Across Organization
      ↓
Update PFMEA / Control Plan / EPV /
Standardized Work / Operator Instructions /
Lessons Learned
```

Do not collapse this chain into Step 5 verification.

---

## STATUS

**CANDIDATE / SINGLE-SOURCE**

No CANON status assigned.

---

## CMOC INTERPRETATION

The key distinction is:

> **A problem can be solved locally without the organization learning from it.**

GM makes institutionalization a separate operation after effectiveness has been verified:

```text
LOCAL PROBLEM
   ↓
SOLUTION
   ↓
VERIFY EFFECTIVENESS
   ↓
FIND ANALOGOUS EXPOSURE
   ↓
PROPAGATE
   ↓
EMBED IN SYSTEM ARTIFACTS
```

The important CMOC interpretation is that organizational learning requires more than storing a conclusion. It requires changing the relevant structures through which future work is planned, controlled, performed and instructed.

This interpretation is not presented as a GM definition of CMOC.

---

## INTER-SOURCE NOTE

Potentially relevant to later comparison with ISO/DIS 9001:2025 concepts concerning organizational knowledge, documented information, improvement and corrective action. No cross-source confirmation is asserted in this PATCH.
