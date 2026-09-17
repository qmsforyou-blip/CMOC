# GM-096 — Plant Process Change Control Cross-Check

**Source:** GM Quality Systems Basics rev. March 2009, Managing Change, pp. 325–335  
**Provenance:** GM SOURCE → SOURCE-FINAL → Distinctions → Mechanisms → Machine Candidates → Catalog Cross-Check  
**Status:** MACHINE-CANDIDATE / NON-CANON  
**Candidate:** Plant Process Change Control (PPCR)

## 1. Source basis

GM defines a system for managing plant process changes, including planned and unplanned/emergency changes. The scope includes changes that may affect the final product, customer-approved machines and systems, and manual or automated plant stations. The process is controlled through a Document Control Process. Responsibility is distributed among Operations, Manufacturing/Engineering, and Quality management.

The Plant Process Change Request (PPCR) is used to document changes, track changes that may negatively affect a process, and ensure that key stakeholders are aware of requirements and participate in controlling out-of-standard conditions.

PPCRs are required for hardware or software changes affecting such areas as final piece cost, machine/system reliability or capability, job instructions, training material, maintenance procedures, calibration procedures, operating instructions, machine setup targets, Process Control Plans, and approved EWO changes.

## 2. Identity

**Candidate type:** controlled change-management machine / process-control machine candidate

**Primary source realization:** Plant Process Change Request (PPCR) process

## 3. Problem

A plant process may change in ways that affect the product, process, equipment, instructions, training, maintenance, or approved controls. Without a controlled change process, stakeholders may not be aware of the change and the organization may create an out-of-standard condition without defined approval, implementation control, or post-implementation closure.

## 4. Input

A proposed plant process change, including its opportunity/problem statement, affected part/process/system, planned or emergency nature, proposed implementation date, and applicable functional or quality requirements.

## 5. Trigger

A planned or emergency change that falls within the organization's PPCR scope.

## 6. Operating sequence

Source flow establishes the following sequence:

`Initiate PPCR → Assign Change Leader → Classify / Route Change → Identify Required Functions → Obtain Approvals → Authorize Implementation → Implement Change → Record Implementation / Breakpoint → Resolve Open Issues → Final Approval → Controlled Record`

The process includes explicit stop/reject branches. If required approvals cannot be obtained, the change process stops. Where the proposed change is routed into the Change Management Process (CMP), the manufacturing focus team guides it through acceptance or rejection before the PPCR process proceeds.

The source's PPCR flow explicitly distinguishes authorization to proceed from implementation and from final approval.

## 7. State transition

A CMOC interpretation of the source flow is:

`PROPOSED CHANGE → UNDER REVIEW → APPROVED TO IMPLEMENT → IMPLEMENTED → OPEN ISSUES / POST-IMPLEMENTATION → FINALLY APPROVED / CLOSED`

Alternative branch:

`PROPOSED CHANGE → REJECTED / STOPPED`

This state model is an architectural interpretation of the documented PPCR flow, not a source-native terminology claim.

## 8. Output

- controlled PPCR record;
- defined responsible Change Leader;
- identified affected functions/departments;
- approval/sign-off evidence;
- implementation date and, where applicable, breakpoint;
- attached applicable worksheets;
- final management approval after open issues are resolved/closed.

## 9. Evidence

Source evidence includes:

- PPCR form;
- PPCR tracking number;
- Document Control Process records;
- functional approval signatures;
- written direction to proceed;
- implementation date;
- breakpoint;
- applicable worksheets;
- final approval signatures.

## 10. Acceptance condition

The change is not treated as complete merely because implementation occurred. The source requires post-implementation recording, resolution/closure of open issues, and final management approval.

## 11. Distinctions implemented

- Change Proposal ≠ Authorized Change
- Approval to Implement ≠ Implementation
- Implementation ≠ Final Approval
- Change Record ≠ Change Effectiveness
- Planned Change ≠ Emergency Change
- PPCR ≠ CMP
- Process Change ≠ Product Validation
- Change Leader ≠ Sole Approver
- Open Issue Closure ≠ Initial Approval

## 12. Boundary

This candidate does **not** by itself establish product validation. The later Production Trial Run (PTR) process is explicitly presented by GM as a separate controlled production tryout for evaluating a change before full-production implementation, and the source states that PTR is not a substitute or extension of product validation.

The PPCR candidate therefore governs the **authorization, coordination, implementation record, and closure of a plant process change**, while PTR is treated as a separate specialized mechanism to be examined independently.

## 13. Relationship to other candidate Machines / mechanisms

### Plant Process Change Control ↔ Production Trial Run

A PPCR may identify a need for a trial run. PTR has its own defined communication, readiness review, quality review, and customer/internal evaluation structure. It should not be collapsed into PPCR at this stage.

### Plant Process Change Control ↔ Control Means Verification

A process change may alter control means. The PPCR provides the change-control route; verification of the effectiveness of the control means remains a distinct mechanism.

### Plant Process Change Control ↔ Bypass Process Control

Emergency or temporary changes can intersect with bypass conditions. GM explicitly treats bypass as a separate section with its own minimum requirements; no merger is made here.

### Plant Process Change Control ↔ Document Control

Document Control is an enabling/control mechanism through which PPCR records are tracked; it is not treated as the same Machine.

## 14. Reusability hypothesis

The candidate appears potentially reusable for controlled organizational changes beyond manufacturing, wherever a change must be proposed, classified, reviewed, authorized, implemented, recorded, and finally closed. This broader reuse is a CMOC hypothesis and requires confirmation from additional sources.

## 15. Canonization assessment

**Candidate strength:** STRONG  
**Independent boundary:** YES  
**Trigger/input:** YES  
**Defined sequence:** YES  
**Approval gates:** YES  
**Implementation record:** YES  
**Closure condition:** YES  
**Evidence:** YES  
**Explicit source realization:** YES (PPCR process)  
**Existing-machine duplication:** no direct duplicate identified in the current cross-check  
**Cross-source confirmation:** NOT YET ESTABLISHED  
**Canon status:** NON-CANON

## 16. Architectural observation

The important CMOC contribution is the separation of three states that are often collapsed:

`AUTHORIZED TO CHANGE → CHANGE IMPLEMENTED → CHANGE ACCEPTED / CLOSED`

The GM form and flow make these transitions visible through separate approval, implementation, post-implementation, breakpoint, open-issue, and final-approval records.

This makes PPCR more than a change form: the candidate is the **controlled transition mechanism for a process from an approved state through an authorized change to a recorded and finally accepted state**.

## 17. Status

**SOURCE-DERIVED / MACHINE-CANDIDATE / NON-CANON**

No REG-001 modification.  
No Canon modification.  
No existing Machine modified.

**Next candidate:** Production Trial Run (PTR).