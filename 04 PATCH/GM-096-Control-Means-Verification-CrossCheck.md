# GM-096 — Control Means Verification — Cross-Check

## Извещение на изменение

**0123+300826**

---

## 0. SOURCE

**Источник:** GM Quality System Basics rev. March 2009  
**Basis:** `GM-096-Mechanisms.md` + `GM-096-Machine-Candidates.md` + `GM-096-Measurement-to-Action-CrossCheck.md`.

**Status:** SOURCE-DERIVED / CROSS-CHECK / NON-CANON

---

## 1. OBJECT OF CHECK

**Control Means Verification**

Question:

> Is verification of a control means an independent Machine, or a specialized mechanism instantiated by a broader verification/control architecture?

**Working verdict:** **SPECIALIZED MECHANISM / MACHINE-SUBCANDIDATE — NOT A TOP-LEVEL MACHINE.**

---

## 2. SOURCE-DERIVED LOGIC

GM repeatedly requires that a control means not merely exist but be capable of performing its intended control function.

Compact form:

```text
CONTROL MEANS
      ↓
DEFINED CONTROL FUNCTION
      ↓
VERIFY PRESENCE / CONDITION / FUNCTION
      ↓
RESULT / STATUS
      ↓
REACTION IF FAILED
      ↓
FOLLOW-UP / EFFECTIVENESS
```

Examples include equipment, process controls, error-proofing devices and contamination-control means.

---

## 3. KEY DISTINCTION

> **Control Means ≠ Controlled State**

The existence of a control device or prescribed control activity does not by itself prove that the intended controlled state is being maintained.

A second distinction follows:

> **Control Means Present ≠ Control Means Effective**

This distinction is strongly compatible with the previously identified Measurement-to-Action pattern.

---

## 4. RELATION TO MEASUREMENT-TO-ACTION

Control Means Verification instantiates the generic pattern:

`Observe → Compare → Interpret → Decide → Act → Verify`

Typical realization:

`Verify control means → compare with required condition → determine status → react to failure → verify restoration`.

Therefore Control Means Verification is **not a competing architecture** with Measurement-to-Action. It is one of its specialized applications.

---

## 5. RELATION TO PROCESS VERIFICATION

Process Verification asks whether the process conforms/operates as required.

Control Means Verification focuses on a narrower object:

> **the means intended to maintain or assure the controlled process condition.**

Thus:

`Control Means Verification ⊂ Process/Control Verification family`

but the exact ontological relation must remain open until the CMOC verification hierarchy is canonized.

---

## 6. RELATION TO ERROR-PROOFING VERIFICATION

Error-Proofing Verification is a specialized realization of Control Means Verification when the control means is an error-proofing device or control.

Working hierarchy:

```text
Verification / Control
        ↓
Control Means Verification
        ↓
Error-Proofing Verification
```

This avoids creating separate top-level Machines for every type of control device.

---

## 7. MACHINE TEST

| Test | Result |
|---|---|
| Independent domain object | NO — object varies by control means |
| Generic verification operation | YES |
| Unique trigger | NO — varies by process/control system |
| State/decision relation | YES |
| Reusable sequence | YES |
| Independent evidence model | NO — implementation dependent |
| Independent acceptance condition | NO — tied to control requirements |
| Cross-context reuse | YES |

The candidate therefore has strong mechanism value but insufficient justification for a Top-Level Machine.

---

## 8. CMOC INTERPRETATION

Retain **Control Means Verification** as a reusable mechanism/pattern.

Do not create a Top-Level Machine.

Where a concrete implementation has a sufficiently independent operational boundary, it may later become a specialized Machine or be represented as part of a System Machine.

The source alone does not require such promotion.

---

## 9. IMPORTANT DISTINCTIONS

- Control Means ≠ Controlled State
- Control Means Present ≠ Control Means Effective
- Verification ≠ Correction
- Detection of Control Failure ≠ Restoration of Control
- Restoration ≠ Evidence of Sustained Effectiveness

These distinctions should be retained as candidates for later Canon comparison.

---

## 10. ARCHITECTURAL VALUE

The important contribution of GM-096 is not a new standalone tool but a stronger formulation of the control chain:

```text
INTENDED CONTROL
      ↓
CONTROL MEANS
      ↓
FUNCTIONAL VERIFICATION
      ↓
CONTROL STATUS
      ↓
REACTION
      ↓
RESTORATION
      ↓
EFFECTIVENESS
```

This makes explicit that the organization must control **the controls themselves** when failure of the control means can compromise the process.

---

## 11. FINAL WORKING VERDICT

> **Control Means Verification is a source-derived specialized verification mechanism implementing the generic Measurement-to-Action control pattern; it is not promoted to a Top-Level Machine at this stage. Error-Proofing Verification is treated as a specialization of this mechanism.**

**STATUS: SPECIALIZED MECHANISM / MACHINE-SUBCANDIDATE / NON-CANON**

---

## 12. DECISION RECORD

- No new Top-Level Machine created.
- No existing Machine modified.
- No REG-001 modification.
- No Canon modification.
- Preserve provenance from GM-096.
- Relate Error-Proofing Verification to Control Means Verification rather than creating an automatic duplicate Machine.

**Next step:** resolve `Fast Response` against existing Andon / response architecture.