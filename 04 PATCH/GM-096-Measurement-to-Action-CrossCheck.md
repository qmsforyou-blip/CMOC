# GM-096 — Measurement-to-Action Control Loop — Cross-Check

## Извещение на изменение

**0122+300826**

---

## 0. SOURCE

**Источник:** GM Quality System Basics rev. March 2009  
**Basis:** `GM-096-Mechanisms.md` + `GM-096-Machine-Candidates.md` + source-derived extraction of measurement, reaction, contamination, supplier metrics and verification material.

**Status:** SOURCE-DERIVED / CROSS-CHECK / NON-CANON

---

## 1. OBJECT OF CHECK

**Measurement-to-Action Control Loop**

Question:

> Is this a separate Machine, a Mechanism, or a more fundamental CMOC control pattern?

**Working verdict:** **PATTERN / FUNDAMENTAL MECHANISM — NOT A TOP-LEVEL MACHINE.**

---

## 2. SOURCE-DERIVED LOGIC

Across the GM material, measurement becomes operationally significant when it is connected to a criterion/status and a defined reaction.

Compact form:

```text
MEASUREMENT
    ↓
RECORD / RESULT
    ↓
LIMIT / CRITERION / STATUS
    ↓
DECISION / REACTION
    ↓
ACTION
    ↓
VERIFICATION / FOLLOW-UP
```

The source realizes this pattern in different contexts rather than presenting it as one named universal Machine.

---

## 3. EXAMPLES IN GM

### Contamination Control

Measurement of contamination or cleanliness is connected to limits and reaction requirements.

### Supplier Performance

Operational performance is converted into metrics/status and then into review, corrective action or supplier development.

### Process Verification

Verification produces findings which may require reaction and follow-up.

### Error-Proofing / Control Means

Verification of a control condition leads to action when the control is absent or ineffective.

These are different Machines/mechanisms, but they share the same control-loop structure.

---

## 4. WHY IT IS NOT A MACHINE

The pattern does not have one independent operational object or one unique domain boundary.

It is instantiated by many Machines:

- Audit;
- Process Verification;
- Supplier Capability Assessment;
- Nonconforming Product Control;
- Contamination Control mechanisms;
- Error-Proofing Verification;
- other measurement-driven controls.

Turning the pattern itself into a Machine would risk confusing an architectural primitive with its concrete implementations.

---

## 5. IMPORTANT DISTINCTIONS

### Measurement ≠ Control

A measurement is only an observation/result. Control requires a defined relationship between the result and a permitted/required response.

### Detection ≠ Control

Detection identifies a condition. Control establishes what happens because that condition has been detected.

### Record ≠ Action

Recording a result does not by itself change the controlled state.

### Status ≠ Decision

A status represents a condition; the control loop becomes operational when status is connected to a decision/reaction.

### Action ≠ Effectiveness

An action being recorded or completed does not automatically establish that the intended effect was achieved.

---

## 6. CMOC INTERPRETATION

The source supports treating Measurement-to-Action as a **control-loop pattern** connecting observation to controlled response.

It can be represented as:

`Observation → Interpretation → Decision → Action → Verification`

The pattern may be embedded in a Machine, composed into a System Machine, or used as a diagnostic lens.

---

## 7. RELATION TO EXISTING CANDIDATES

### Measurement-to-Action → Audit

Audit may instantiate the pattern when a finding produces a defined response.

### Measurement-to-Action → Nonconforming Product Control

Detection of nonconformance becomes control only through containment/disposition.

### Measurement-to-Action → Supplier Capability Assessment

Supplier evidence becomes capability management only when results are interpreted and connected to development/reassessment.

### Measurement-to-Action → Error-Proofing Verification

Verification results trigger action when error-proofing is absent or ineffective.

### Measurement-to-Action → LPA

LPA adds layering, frequency and risk-based selection to repeated verification; the measurement/action loop remains a lower-level pattern.

---

## 8. MACHINE TEST

| Test | Result |
|---|---|
| Independent domain object | NO |
| Unique trigger | NO — varies by implementation |
| Generic transformation | YES |
| State/decision relation | YES |
| Reusable sequence | YES |
| Independent evidence model | NO — implementation dependent |
| Independent acceptance condition | NO — implementation dependent |
| Cross-context reuse | YES |

The pattern therefore fails the test for a standalone Top-Level Machine while strongly satisfying the test for a reusable CMOC mechanism/pattern.

---

## 9. ARCHITECTURAL VALUE

This may be one of the more important findings of GM-096 because it reveals a recurring control grammar underneath apparently different quality tools.

```text
OBSERVE
   ↓
COMPARE
   ↓
INTERPRET
   ↓
DECIDE
   ↓
ACT
   ↓
VERIFY
```

The same grammar can appear at different scales:

- individual control point;
- process;
- supplier;
- organizational system.

This should be preserved as a reusable CMOC pattern rather than hidden inside a particular Machine passport.

---

## 10. CANONIZATION STATUS

**Decision:** Do not create a Machine.

**Classification:** `PATTERN / FUNDAMENTAL MECHANISM CANDIDATE`

**Status:** NON-CANON.

Before Canonization, compare this pattern with existing CMOC control-loop / feedback / state-transition concepts to avoid introducing duplicate primitives.

---

## 11. PROVENANCE

`GM QSB 2009 → SOURCE-FINAL → GM-096-Distinctions → GM-096-Mechanisms → this Cross-Check`

The page-level source material remains the primary evidence of origin; this file is an architectural interpretation and must not replace source provenance.

---

## 12. DECISION RECORD

- No new Machine created.
- No existing Machine modified.
- No REG-001 modification.
- No Canon modification.
- Preserve as candidate CMOC control-loop pattern.

**Next step:** resolve `Control Means Verification` against this pattern and determine whether it is a specialized mechanism or an independent Machine candidate.