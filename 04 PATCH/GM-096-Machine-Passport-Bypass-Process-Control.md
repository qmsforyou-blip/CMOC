# GM-096 — Machine Candidate Passport: Bypass Process Control

**Source:** GM Quality Systems Basics rev. March 2009
**Provenance:** GM SOURCE → SOURCE-FINAL → Distinctions → Mechanisms → Machine Candidates → Catalog Cross-Check
**Status:** MACHINE-CANDIDATE / NON-CANON
**Candidate:** Bypass Process Control

## 1. Identity

**Candidate type:** controlled-deviation / alternative-process machine candidate

**Primary source realization:** Managing Change / Bypass Process Control

## 2. Problem

A normal approved process may temporarily be unable to operate as intended. Simply continuing outside the approved process creates an uncontrolled exception. GM instead defines a bypass as a controlled alternative process with explicit boundaries and controls.

## 3. Input

A need and authorization to operate temporarily outside the normal approved process, together with the applicable alternative process controls.

## 4. Trigger

A defined condition requires use of a bypass / backup process.

## 5. Operating sequence

`Normal Process → Authorized Entry → Entry Breakpoint → Controlled Bypass → Inspection / Audit / Control → Exit Breakpoint → Verified Return`

The bypass process is bounded by explicit starting and ending breakpoints.

## 6. Output

Either:

- continued operation within a controlled bypass state; or
- verified return to the normal approved process.

## 7. State transition

`NORMAL → CONTROLLED BYPASS`

followed by:

`CONTROLLED BYPASS → VERIFIED NORMAL`

The candidate therefore manages a temporary state transition rather than merely documenting an exception.

## 8. Control architecture

The source-derived bypass architecture may include:

- approved bypass methods;
- responsible owner;
- applicable PFMEA;
- Control Plan;
- Standardized Work;
- inspection requirements;
- audit requirements;
- communication at the bypass point;
- Backup Worksheet;
- Action Plan;
- trained personnel;
- verification of parameters on return;
- validation of the required quantity/condition before release back to normal;
- management authorization for return where required.

## 9. Evidence

Source-derived evidence includes:

- documented bypass/backup process;
- starting breakpoint;
- ending breakpoint;
- applicable PFMEA / Control Plan / Standardized Work;
- inspection records;
- audit evidence;
- Backup Worksheet;
- Action Plan;
- return verification/validation.

## 10. Acceptance condition

The bypass is closed only when the organization has verified the conditions for returning to the normal approved process and the return boundary has been reached.

The existence of a bypass record alone is not evidence that the normal process has been safely restored.

## 11. Failure / STOP conditions

The source supports stopping or withholding return when required controls or verification conditions are not satisfied. Exact reaction logic for every failure case is not inferred beyond the source-derived control requirements.

## 12. Distinctions implemented

- Temporary Deviation ≠ Uncontrolled Exception
- Bypass ≠ Abandonment of Control
- Normal State ≠ Bypass State
- Entry ≠ Exit
- Return ≠ Verified Return
- Record ≠ Evidence of Effective Control

## 13. Boundary

Bypass Process Control does **not**:

- authorize arbitrary deviation;
- replace the normal approved process permanently;
- eliminate PFMEA, Control Plan, Standardized Work or inspection requirements;
- establish effectiveness merely by entering the bypass;
- treat return to normal as complete without required verification.

Its boundary is:

> **Maintain a controlled alternative process state between explicit entry and exit boundaries and verify the conditions for return to the normal process.**

## 14. Relationship to other candidate Machines

### Decision Gate → Bypass Process Control

Authorization may be required before entering the controlled bypass state.

### Controlled Change Implementation ↔ Bypass Process Control

A bypass is itself a controlled state transition. It may be a specialized implementation pattern or a distinct Machine. This relationship requires later CMOC comparison.

### Production Trial Run ↔ Bypass Process Control

Both are bounded states with verification, but their purposes differ: PTR evaluates a changed process; bypass control maintains production under a temporary alternative process.

### Controlled Deviation

Controlled Deviation may be the generic parent pattern, with Bypass Process Control as a specialized realization. Do not collapse them until CMOC architecture resolves the relationship.

## 15. Reusability hypothesis

The candidate is potentially reusable wherever an organization must temporarily leave an approved process while retaining explicit control, traceability and a verified route back to the normal state.

Broader reuse remains a CMOC hypothesis and requires confirmation from additional sources.

## 16. Canonization assessment

**Candidate strength:** STRONG

**Independent boundary:** YES

**Trigger/input:** YES

**State transition:** YES

**Defined entry/exit:** YES

**Responsible role:** YES

**Repeatable sequence:** YES

**Evidence:** YES

**Return/closure condition:** YES

**Cross-source confirmation:** NOT YET ESTABLISHED

**Existing-machine duplication:** relationship to Controlled Deviation and generic State Transition patterns remains unresolved.

**Canon status:** NON-CANON.

## 17. Architectural observation

The key value of this candidate is that it makes a temporary exception into a **controlled state** rather than an absence of control.

The source therefore demonstrates:

`Deviation → Defined Alternative State → Boundary Control → Evidence → Verified Return`

This is a particularly useful CMOC pattern because many organizational failures occur not in the normal process but in the temporary state created when the normal process cannot be followed.

## 18. Status

**SOURCE-DERIVED / MACHINE-CANDIDATE / NON-CANON**

No REG-001 modification.
No Canon modification.
No existing Machine modified.

**Next candidate:** Supplier Capability Assessment.