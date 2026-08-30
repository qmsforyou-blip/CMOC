# GM-096 — Managing Change

**Source:** GM Quality Systems Basics rev March 2009, Global Purchasing and Supply Chain, pp. 323–350.

## Scope

The source presents Managing Change as one of eleven key strategies supporting world-class quality. The section describes a controlled change process with defined roles, approval gates, implementation records, trial-run evaluation where applicable, final approval, and a workshop mechanism for translating requirements and gaps into organizational action.

## 1. PPCR process architecture

The PPCR (process change) flow establishes a sequence from initiation to controlled implementation:

`Initiator → Change Leader → PPCR tracking → CMP/PPCR decision → review → approval/rejection → required departmental approvals → management direction → implementation → record → final approval`

The source distinguishes the change initiator from the Change Leader and requires the initiator to complete the initial PPCR information and obtain a tracking number.

## 2. Approval and rejection gates

The proposed change is assessed for whether it proceeds through the Change Management Process (CMP) or remains in the PPCR system. Where CMP is required, the PPCR is reviewed with the manufacturing focus team / PDT-CIT.

The change is explicitly subject to an approval/rejection decision. A rejection stops the change process.

The Change Leader determines the persons/departments required to implement the change and obtains approval signatures from each designated department. If any required signature cannot be obtained, the change process stops and the contacted departments are notified of the rejection.

## 3. Approval is distinct from authorization to proceed

After departmental approvals, the Change Leader reviews the pending process change with the General Supervisor or Superintendent.

The Change Leader must obtain written direction to proceed, together with the required signature. If direction is not to proceed, the change stops and all concerned parties are notified with the reason for rejection.

This establishes a distinct sequence:

`review / approval → written authorization to proceed → implementation`

Approval of the change and authorization to execute the change are therefore separate control events in the source process.

## 4. Implementation and records

Once authorization to proceed is obtained, the Change Leader and the designated parties implement the process change.

The date on which the process change was actually implemented is recorded on the PPCR form and on the PPCR log sheet.

The completed PPCR, together with applicable worksheets, is then forwarded for final approval. The original final-approved PPCR is retained by Manufacturing Engineering.

The source therefore distinguishes the decision to implement from the recorded fact of implementation and from final approval of the completed change record.

## 5. Production Trial Run

The Production Trial Run Form provides a controlled path for trial evaluation of a change where a PTR is required.

The form addresses:

- identification of the change and Change Leader;
- decision whether an internal Production Trial Run is required;
- decision whether Customer PTR is required;
- PTR readiness;
- internal PTR value review and successful completion;
- Customer Plant PTR Evaluation where applicable.

The trial run therefore provides an intermediate verification stage between authorization/implementation and acceptance of the changed process or product.

`Change → authorization → trial readiness → trial → evaluation → acceptance`

The source demonstrates that authorization to make a change is not itself evidence that the changed process has demonstrated acceptable performance.

## 6. Manufacturing Process Backup Worksheet

The Manufacturing Process Backup Worksheet is presented as a record documenting breakpoints for entering and exiting a bypass process and identifying tooling, inspection and audit requirements.

This represents a controlled temporary or alternative process rather than an informal deviation. The bypass has defined entry and exit points and associated control requirements.

`Normal process → controlled entry → backup / bypass process → controlled exit → normal process`

## 7. Workshop mechanism

The later pages of the Managing Change section describe how the QSB strategies are assigned to workshop teams and converted into actionable work.

The source recommends teams of three to five people where possible. Strategies are paired with personnel from the functions capable of changing or controlling the relevant process. Examples include Manufacturing Engineering, Maintenance, Operators, Supervisors, Auditors/Quality, Training/HR and Quality Engineering, with management and operators assigned to Layered Process Audits, Verification Stations and Fast Response.

The architectural implication is important:

> **A strategy is assigned not to an isolated function, but to a cross-functional team capable of changing the corresponding process.**

The workshop is expected to examine whether the applicable requirements are actually being fulfilled and to identify what is required to make them operational.

The source directs teams to consider such elements as forms, tracking, analysis, management review, communication to employees, inclusion in procedures, and To-Do / Action Lists.

Results are presented to Top Management. Items that cannot be completed by the closing meeting are transferred to the QSB Action Plan rather than being left unresolved.

This establishes a transition:

`Requirement / strategy → team examination → current status / gap → required mechanism → action → Top Management → Action Plan`

## 8. Workshop architectural distinction

The strongest distinction from the workshop material is:

> **Workshop is a mechanism for translating a requirement and an identified gap into a governed organizational action.**

A diagnostic result does not become an implemented change merely because the gap has been identified. The source requires the team to determine the supporting mechanisms for execution and follow-up: forms, tracking, analysis, management review, communication and action ownership.

A second distinction is:

> **An action that cannot be completed at the workshop boundary must acquire a subsequent control state rather than disappear.**

The QSB Action Plan provides that continuation state.

## 9. CMOC architectural extraction

The strongest architectural distinction from the complete section is:

> **A change is governed not only by the decision to change, but by controlled transition between states.**

The source controls the transition through identifiable gates:

`Change proposal → classification/review → approval/rejection → required approvals → authorization → implementation → evidence/record → trial/evaluation where required → final approval`

The workshop layer adds:

`Requirement / strategy → team → current status → gap → mechanism → action → management → action plan`

The process also demonstrates that different kinds of decision and evidence must not be collapsed into one event:

- approval is distinct from authorization to proceed;
- authorization is distinct from implementation;
- implementation is distinct from the record of implementation;
- implementation is distinct from trial/evaluation;
- completion is distinct from final approval;
- identification of a gap is distinct from implementation of corrective action;
- workshop completion is distinct from closure of unfinished actions.

## 10. CMOC candidate mechanisms

**MC-15** — Required departmental approval is a condition for continuing a change; failure to obtain a required approval stops the process.

**MC-16** — Approval of a change and written authorization to proceed are distinct control events.

**MC-17** — Rejection at a change-control gate produces a STOP state and requires notification of concerned parties.

**MC-18** — The fact of implementation is recorded separately from the decision to implement.

**MC-19** — Final approval follows implementation and completion of the change record; implementation does not by itself close the change process.

**MC-20** — A bypass/backup process has explicitly defined entry and exit points, with those boundaries recorded.

**MC-21** — A bypass/backup process has defined tooling, inspection and audit requirements.

**MC-22** — A temporary deviation from the normal process can be treated as a controlled process state with defined boundaries and records.

**MC-23** — Where required, a production trial run is a separate verification stage for evaluating the result of a change.

**MC-24** — Readiness for a production trial run is a separate condition to be verified before the trial.

**MC-25** — The result of a change is evaluated separately from the decision to implement it; customer evaluation may form part of acceptance where applicable.

**MC-26** — A cross-functional workshop team is assigned a strategy according to its ability to change or control the relevant process.

**MC-27** — A workshop converts an identified requirement/gap into defined mechanisms and actions rather than treating diagnosis as completion.

**MC-28** — Workshop results are escalated to Top Management for consideration and direction.

**MC-29** — Unfinished workshop actions are transferred into an Action Plan, preserving their continuation and follow-up state.

**MC-30** — Forms, tracking, analysis, management review and communication can function as explicit mechanisms for converting requirements into controlled organizational action.

## 11. CMOC significance

Managing Change in this source is not merely a document-control activity. It is an operational control architecture for moving a process from one accepted state to another while preserving responsibility, authorization, evidence, traceability and acceptance.

The workshop material extends the architecture upstream: before a change is implemented, the organization must be able to translate requirements and identified gaps into mechanisms, actions and management follow-up.

The combined architecture is therefore:

`Requirement → assessment → status/gap → mechanism → authorized change → implementation → verification/evaluation → record → management follow-up → closure`

This provides a concrete industrial example of the CMOC principle that **a system becomes governable when states, transitions, responsibilities, evidence and continuation paths are made explicit**.

The final strategy page places Managing Change alongside Fast Response, Control of Non-Conforming Product, Verification Station, Standardized Operations, Standardized Operator Training, Error Proofing Verification, Layered Process Audits, Risk Reduction, Contamination Control and Supply Chain Management. Together these strategies are presented as contributing to no major disruptions, no PRRs and zero PPM quality performance.

**Status:** source extraction / architectural confirmation. No new REG-001 distinction added by this patch.