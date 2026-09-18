# GM-096 — Machine Passport v0.3 — Working Application: Bypass Process Control

**Notice:** 0166+180926  
**Status:** PASS / WORKING SPECIFICATION SUPPORTED / NON-CANON  
**Source:** GM Quality System Basics Overview Supplier Audit, rev. March 2009, §11.5 Bypass Process, pp. 340–343

---

## 1. Purpose of the trial

Apply the frozen **Machine Passport v0.3** to the GM-096 candidate **Bypass Process Control** as a concrete domain realization.

The test asks:

> Does Bypass Process Control possess an independent bounded execution identity that can be described by Machine Passport v0.3, without absorbing the whole Managing Change Assembly, the SOP, the approval mechanism, or the supporting artifacts?

No Catalog / Canon / REG-001 changes are made by this trial.

---

## 2. Source evidence

GM QSB §11.5 defines Bypass Process as a procedure required when a process is altered outside the approved documented Control Plan.

The source requires:
- minimum requirements for bypassing an existing manufacturing process;
- minimum requirements for verification of the original process when exiting the bypass;
- approval of bypass methods/controls by Operations, Engineering and Quality management;
- a maintained list of processes approved for bypass;
- inclusion of the bypass process in PFMEA and Control Plan;
- Standardized Work Instructions for the bypass;
- communication at each active bypass point;
- a Manufacturing Process Bypass Worksheet;
- recording of starting and ending breakpoints;
- trained and certified operators;
- verification of process parameters/settings before return to the original process;
- validation of a pre-established quantity of parts;
- Operations Manager approval of return to the original process.

The source therefore describes not merely an alternative operation, but a **controlled temporary departure from an approved process with controlled entry, operation, exit verification and authorized return**. fileciteturn170file7

---

# 3. Boundary proof

## 3.1 Identity-bearing relation / mode

Working identity-bearing relation:

**NORMAL APPROVED PROCESS UNAVAILABLE / ALTERED → CONTROLLED ALTERNATIVE PROCESS → VERIFIED EXIT → RETURN TO APPROVED PROCESS OR TERMINAL DISPOSITION**

The identity is not simply “doing work another way”.

It is the controlled relationship between:
1. an approved normal process;
2. its temporary unavailability or alteration;
3. an explicitly controlled alternative route;
4. verification before leaving that route;
5. authorized transition back to the approved process.

This relation distinguishes Bypass from ordinary rework, maintenance, storage, monitoring, or generic change control.

---

## 3.2 Own execution boundary

Working boundary:

> **Detection/recognition of the need to bypass an approved process → controlled entry into the bypass → execution under defined bypass controls → recorded exit breakpoint → verification of original-process readiness and defined output → authorized return or terminal disposition.**

The Machine does not own:
- creation of the overall plant change system;
- general document control;
- creation of the PFMEA/Control Plan;
- engineering approval as a generic governance function;
- the whole Managing Change Assembly.

It owns the **bounded execution of the temporary alternative route and its controlled exit**.

---

## 3.3 Local capability

> **Maintain controlled production when the approved process cannot temporarily be used, while preserving defined controls, traceability of the bypass interval, and verified return to the approved process.**

This is narrower than the capability of Managing Change.

Managing Change governs the wider transition/change architecture.

Bypass Process Control governs the temporary alternative route inside that architecture.

---

## 3.4 Closure condition

Working closure condition:

> The bypass interval has ended at the recorded exit breakpoint; the original process parameters/settings have been verified; the required quantity of parts has been validated; and the authorized return to the original process has been approved — or the bypass output has received an explicitly controlled terminal disposition.

Closure is therefore not simply “the alternative operation stopped”.

It is a **verified and authorized exit from the bypass state**.

---

# 4. Machine Passport v0.3

## CORE

### name

**Bypass Process Control**

### identity_bearing_relation_or_mode

NORMAL APPROVED PROCESS UNAVAILABLE / ALTERED → CONTROLLED ALTERNATIVE ROUTE → VERIFIED EXIT → AUTHORIZED RETURN / TERMINAL DISPOSITION

### local_capability

Maintain controlled production during temporary unavailability/alteration of the approved process and provide verified, traceable exit back to the approved process or controlled terminal disposition.

---

## EXECUTION

### trigger

One of the source-defined conditions requiring bypass, including:
- torque gun failure;
- backup operation outside normal process flow;
- error proofing or gaging turned off;
- temporary rework to bring a part back to specification.

More generally:

NORMAL APPROVED PROCESS CANNOT BE EXECUTED AS DOCUMENTED → BYPASS REQUIRED

### inputs_context

- approved manufacturing process / normal process flow;
- defined bypass method and controls;
- applicable PFMEA and Control Plan;
- Standardized Work Instructions;
- active bypass point;
- starting breakpoint;
- tooling / inspection / audit requirements;
- trained and certified operators;
- required authorization.

### preconditions

- bypass method/control is approved by the responsible Operations, Engineering and Quality managers;
- applicable bypass process is defined and controlled;
- required documentation exists;
- operators performing the bypass are trained and certified;
- required tooling, inspection and audit controls are available.

### execution_boundary

ENTER BYPASS → EXECUTE UNDER DEFINED CONTROLS → RECORD / MONITOR ACTIVE BYPASS → DEFINE EXIT BREAKPOINT → VERIFY ORIGINAL PROCESS → VALIDATE REQUIRED PART QUANTITY → AUTHORIZE RETURN / TERMINAL DISPOSITION

### execution_sequence

1. Recognize that the approved process cannot be followed normally.
2. Establish the controlled bypass condition.
3. Record the starting breakpoint.
4. Execute the defined alternative process/method.
5. Maintain required tooling, inspection and audit controls.
6. Maintain the active bypass record/worksheet.
7. Record the ending breakpoint.
8. Verify original-process parameters and settings.
9. Validate the pre-established quantity of parts.
10. Obtain authorized approval for return to the original process, where applicable.
11. Close the bypass interval with traceable status.

### evidence

- Bypass Process Worksheet;
- starting and ending breakpoints;
- approved bypass method/control;
- PFMEA / Control Plan inclusion;
- Standardized Work Instructions;
- communication at active bypass point;
- training/certification evidence;
- verification of original-process parameters/settings;
- validation results for the pre-established quantity;
- authorization of return.

### decision_points_logic

- Is the normal approved process unavailable/altered in a way requiring bypass?
- Is an approved bypass method available?
- Are required controls available and active?
- Has the bypass exit breakpoint been reached?
- Are original-process parameters/settings verified?
- Has the required quantity of parts been validated?
- Is return to the original process authorized?

If return cannot be authorized, the Machine does not invent a new route; the condition remains under controlled disposition/escalation.

### local_outputs

- controlled bypass execution;
- traceable bypass interval;
- verified readiness of the original process;
- validated defined quantity of parts;
- authorized return to normal process, or controlled terminal disposition;
- completed bypass evidence.

### closure_condition

**type:** mixed

**condition:**

EXIT BREAKPOINT RECORDED + ORIGINAL PROCESS VERIFIED + REQUIRED PART QUANTITY VALIDATED + RETURN AUTHORIZED OR TERMINAL DISPOSITION ESTABLISHED

**evidence:**
- completed bypass record;
- verification results;
- validation results;
- authorization/disposition record.

**downstream_continuation:** allowed

---

# 5. REALIZATION

## domain

Manufacturing process control / production operations.

## internal_mechanisms

- approved bypass method/control;
- defined alternative operation;
- breakpoint control;
- process parameter verification;
- part validation;
- communication at active bypass point;
- worksheet / action-plan tracking;
- operator training and certification;
- authorization of return.

These are **realization mechanisms**, not separate identity-defining components of the Machine.

## roles

Source-defined responsible roles include:
- Operations Manager / process owner;
- Engineering Manager;
- Quality Manager;
- trained/certified operators.

## artifacts

- Manufacturing Process Bypass Worksheet;
- approved bypass-process list;
- PFMEA;
- Control Plan;
- Standardized Work Instructions;
- active-bypass communication;
- verification / validation records.

## domain_specific_conditions

- temporary departure from an approved manufacturing process;
- process controls must remain defined during bypass;
- bypass must have identifiable entry and exit breakpoints;
- return to original process requires verification and validation.

## limitations

Bypass Process Control does not itself:
- define the enterprise-wide change-control system;
- replace Plant Process Change Control;
- replace Production Trial Run;
- replace Banking Process;
- replace Problem Solving;
- own the underlying PFMEA/Control Plan as documents;
- constitute the SOP itself.

## downstream_ownership

The Machine hands off to:
- normal approved process;
- Managing Change / change-control governance;
- Quality verification and related controls;
- controlled disposition/escalation where return is not authorized.

---

# 6. RELATIONS

### pattern

Managed Transition

### invokes_uses

- Process Change Control / authorization;
- Standardized Work Instructions;
- PFMEA / Control Plan;
- verification / validation mechanisms;
- Document Control.

### feeds

- verified return to normal process;
- change-control records;
- process/risk-model updates where the bypass reveals new information;
- corrective or improvement mechanisms where required.

---

# 7. VALIDATION

## machine boundary test

### Identity-bearing relation / mode

PASS.

The defining mode is controlled temporary substitution for an unavailable/altered approved process with controlled exit.

### Own execution boundary

PASS.

A coherent bounded interval exists from bypass entry through verified exit.

### Local capability

PASS.

The candidate sustains controlled production during temporary process unavailability and controls the exit.

### Closure condition

PASS.

Closure requires verified readiness/validation and authorized return or controlled terminal disposition.

### Result

**PASS — Bypass Process Control qualifies as a Machine candidate under the frozen v0.3 Passport structure.**

---

# 8. Adversarial boundary tests

| Candidate | Result | Reason |
|---|---|---|
| Storage | FAIL as equivalent | Storage controls a state/location; it does not represent temporary alternative process execution and controlled return. |
| Banking | FAIL as equivalent | Banking controls out-of-normal-flow material; Bypass controls an alternative production route. |
| Rework | FAIL as equivalent | Rework may be an operation within a bypass; it does not by itself define the controlled temporary route and return architecture. |
| Plant Process Change Control | FAIL as equivalent | PPCR governs authorization/control of process changes; Bypass executes a bounded temporary alternative route. |
| Production Trial Run | FAIL as equivalent | PTR produces controlled trial evidence for evaluation; Bypass maintains production under a temporary alternative process. |
| Monitoring | FAIL as equivalent | Monitoring supplies status/evidence; it does not constitute the bounded alternative-route execution. |
| LPA | FAIL as equivalent | LPA verifies compliance; it is not the bypass execution itself. |
| SOP / Work Instruction | FAIL as equivalent | SOP/WI prescribes execution; Bypass is the controlled execution state/route using such instructions. |
| Managing Change Assembly | FAIL as Machine-equivalent | Assembly coordinates broader change-transition mechanisms; Bypass is a bounded Machine within that composition. |

---

# 9. Machine vs Assembly boundary

Working composition:

MANAGING CHANGE ASSEMBLY
→ PLANT PROCESS CHANGE CONTROL
→ **BYPASS PROCESS CONTROL**
→ VERIFICATION / VALIDATION
→ RETURN TO NORMAL PROCESS

The candidate does not absorb the surrounding Assembly.

Its boundary remains:

NORMAL PROCESS UNAVAILABLE / ALTERED
→ CONTROLLED ALTERNATIVE ROUTE
→ VERIFIED EXIT
→ AUTHORIZED RETURN / TERMINAL DISPOSITION

This is consistent with the current Machine definition:

> Machine = bounded executable unit with identity-bearing relation/mode, own execution boundary, local capability and closure condition.

---

# 10. SOP anti-duplication test

**PASS.**

A Standardized Work Instruction can prescribe:
- what operation to perform;
- in what sequence;
- with what tooling;
- with what inspection/control requirements.

The Machine is not the instruction.

The Machine is the **controlled execution mode that temporarily routes production outside the approved normal process and governs entry, active bypass, exit verification and authorized return**.

---

# 11. Passport adequacy test

All v0.3 sections are usable:

- CORE — PASS
- EXECUTION — PASS
- REALIZATION — PASS
- RELATIONS — PASS
- VALIDATION — PASS
- PROVENANCE — PASS

No additional Passport field is required as a result of this trial.

The candidate also confirms that closure_condition must allow a **verified transition/disposition** rather than requiring “return to normal” as a universal Machine closure form.

---

# 12. Architectural conclusion

**Bypass Process Control is a MACHINE CANDIDATE.**

Its identity is not:

> “a backup process”

but:

> **a bounded controlled execution mode for temporarily replacing an approved process, with explicit entry/exit breakpoints, defined controls, verification of the original process, validation of the defined output, and authorized return or terminal disposition.**

Boundary proof: **PASS**  
Passport v0.3 application: **PASS**  
Machine / Assembly separation: **PASS**  
SOP anti-duplication: **PASS**  
Adversarial boundary: **PASS**  
Status: **MACHINE CANDIDATE / NON-CANON**

No Catalog / Canon / REG-001 changes.

---

## 13. Next methodological step

GM-096 now has four practical v0.3 Machine Passport applications:

1. Plant Process Change Control — PASS WITH QUALIFICATION
2. Production Trial Run — PASS
3. Banking Process — PASS WITH QUALIFICATION
4. Bypass Process Control — PASS

The next useful step is **not another Passport-schema test**.

Proceed to the next GM-096 candidate only if we want to continue routine passporting; otherwise the four GM-096 Machines can be used for a **cross-machine boundary comparison** to determine whether any of them collapse into one more general Machine abstraction.
