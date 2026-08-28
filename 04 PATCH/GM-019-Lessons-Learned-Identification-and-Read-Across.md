# GM-019 — Lessons Learned: Identification and Read Across

**Извещение на изменение:** 0130+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Section:** Fast Response → 1.4 – Lessons Learned  
**Status:** CANDIDATE / SINGLE-SOURCE

---

## SOURCE

GM states that Lessons Learned may be identified by anyone. It gives examples of activities that can identify Lessons Learned, including APQP, Layered Process Audits, Error Proofing Verification Failures, Problem Solving for internal or external issues, Verification Station Findings, Continuous Improvement Teams, Risk Reduction / Reverse PFMEA activity, Suggestion Programs, and management reviews.

GM also explicitly names **GM Drill Wide – Read Across communication and follow up** and **APQP Program reviews of Lessons Learned** as activities within the Lessons Learned approach.

The source states that a disciplined approach to problem prevention using Lessons Learned shall be established.

---

## LOCATION

Source pp. 48–49, Fast Response — 1.4 Lessons Learned.

---

## TERMS

- Lessons Learned
- identify Lessons Learned
- Read Across
- communication
- follow up
- APQP Program reviews
- problem prevention
- activities
- potential users

---

## DISTINCTIONS

### DIS-GM-019-01

**Lesson identification ≠ Lesson storage.**

GM names multiple operational activities as sources through which Lessons Learned are identified. Identification is therefore an upstream activity to the Lessons Learned system.

### DIS-GM-019-02

**Read Across ≠ documentation.**

The source separately identifies GM Drill Wide — Read Across communication and follow up. Read Across is therefore an application/transfer activity, not merely a documentation format.

### DIS-GM-019-03

**Local finding ≠ organizational prevention.**

The purpose of the disciplined Lessons Learned approach is prevention of future problems and improvement of performance. The source therefore connects the identified lesson to subsequent organizational use.

### DIS-GM-019-04

**Identification may be distributed.**

Lessons Learned may be identified by anyone. The source does not restrict identification to Quality or management.

---

## GM-FORMULATIONS

- “Lessons Learned may be identified by anyone.”
- “GM Drill Wide-Read Across communication and follow up.”
- “APQP Program reviews of Lessons Learned.”
- “A disciplined approach to problem prevention using Lessons Learned shall be established.”

---

## EXTRACTION

```text
OPERATIONAL ACTIVITY
        ↓
FINDING / EXPERIENCE
        ↓
LESSON LEARNED IDENTIFIED
        ↓
LESSONS LEARNED SYSTEM
        ↓
READ ACROSS / COMMUNICATION
        ↓
FOLLOW UP
        ↓
PREVENTION / IMPROVEMENT
```

Multiple source activities feed the identification stage:

```text
APQP
LPA
Error Proofing Verification Failures
Problem Solving
Verification Station Findings
Continuous Improvement Teams
Reverse PFMEA / Risk Reduction
Suggestion Programs
Management Reviews
        ↓
LESSON IDENTIFICATION
```

---

## REL

Source-supported relations:

```text
Operational Activity → Lesson Identified
Lesson Identified → Lessons Learned System
Lessons Learned → Read Across Communication
Read Across → Follow Up
Lessons Learned → Problem Prevention / Improvement
```

The source also links Lessons Learned review to APQP program reviews.

---

## MECHANISM

### CANDIDATE — Read Across / Follow-Up Mechanism

**Input:** documented or identified Lesson Learned.

**Transformation:** communicate the lesson beyond its original context, make it relevant to potential users, and perform follow-up.

**Output:** lesson considered/applied in other organizational contexts.

**Organizational effect:** experience from one context can contribute to prevention or improvement elsewhere.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CAPABILITY

**NONE**

---

## CORE CANDIDATE

> **Read Across — an organizational transfer operation that communicates a Lesson Learned beyond its originating context and follows up on its use for prevention or improvement elsewhere.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## MACHINE

### CANDIDATE MACHINE — Read Across

```text
LOCAL LESSON
      ↓
[ READ ACROSS ]
      │
      ├── communicate
      ├── identify potential users / contexts
      └── follow up
      ↓
OTHER CONTEXTS
      ↓
PREVENTION / IMPROVEMENT
```

The candidate passes the machine test at this level because the source explicitly names communication and follow up as part of Read Across. The exact operational implementation is not fully specified in this fragment, so confidence remains limited.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CHAIN

### SOURCE-SUPPORTED CANDIDATE

```text
Activity / Finding
→ Lesson Learned
→ Read Across Communication
→ Follow Up
→ Prevention / Improvement
```

Do not infer that every listed activity automatically produces a Lesson Learned; GM presents them as examples of activities that may identify Lessons Learned.

---

## STATUS

**CANDIDATE / SINGLE-SOURCE**

No CANON status assigned.

---

## CMOC INTERPRETATION

The strongest new distinction is:

> **The organizational value of a Lesson Learned is not exhausted by its capture; it must cross the boundary of the originating case and enter another context where prevention or improvement can occur.**

Thus, in CMOC terms, **Read Across** is a candidate transfer mechanism rather than a storage mechanism.

This is a CMOC interpretation, not a claim that GM uses CMOC terminology.

---

## RELATION TO GM-018

GM-018 established the Lessons Learned system as the organizational capture/documentation/availability context.

GM-019 adds the upstream identification sources and the downstream **Read Across communication + follow up** operation.

The combined candidate flow is therefore:

```text
ACTIVITY / EXPERIENCE
        ↓
IDENTIFY LESSON
        ↓
CAPTURE / DOCUMENT
        ↓
MAKE AVAILABLE
        ↓
READ ACROSS
        ↓
FOLLOW UP
        ↓
PREVENTION / IMPROVEMENT
```

No cross-source confirmation with ISO/DIS 9001:2025 is asserted here.
