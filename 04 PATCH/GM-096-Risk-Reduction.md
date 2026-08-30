# GM-096 — Risk Reduction Process

**Source:** GM Quality Systems Basics rev March 2009, Global Purchasing and Supply Chain, pp. 252–270.

## Scope

Risk Reduction is presented as a managed process built around PFMEA, review, RPN reduction, Reverse PFMEA, error proofing, and management tracking.

## 1. Benefits

The source identifies the following benefits:

- supports continual improvement as expected by TS16949;
- allows leadership to allocate limited resources to critical areas;
- provides a basis for effective error-proofing and problem solving;
- is a core tool for APQP and PPAP requirements;
- provides a Lessons Learned archive;
- promotes cross-functional teamwork;
- meets customer expectations for “living documents”.

## 2. PFMEA overview

PFMEA is defined as an analytical technique applied to each process step to identify:

- ways a process may fail to meet requirements;
- consequences to the internal/external customer (**Severity**);
- frequency with which the failure will/could happen (**Occurrence**);
- effectiveness of current controls — prevention and detection (**Detection**);
- ranking of causes and effects using the **Risk Priority Number (RPN)**.

It is also described as a structured procedure for identifying and eliminating process-related failure modes.

### PFMEA example structure

The example PFMEA evaluates:

`Process step → Potential failure mode → Potential effect → Severity → Potential cause/mechanism → Occurrence → Current controls (prevention/detection) → Detection → RPN → Recommended action → Responsibility/target date → Action results → revised ratings/RPN`

The example demonstrates that a recommended control can materially reduce the resulting RPN.

## 3. PFMEA ratings

Severity, Occurrence and Detection ratings are determined by a cross-functional FMEA team using the AIAG PFMEA manual.

The source provides rating tables for:

- Severity — effect on customer/manufacturing or assembly;
- Occurrence — likelihood/failure rate, including PpK reference values;
- Detection — likelihood that existing controls will detect the failure mode/cause before escape.

## 4. PFMEA ownership and maintenance

PFMEAs shall be developed and maintained by cross-functional teams for manufacturing processes and support functions as required by the AIAG manual.

They shall:

- exist for all product lines / part numbers;
- include support functions such as receiving inspection, material handling, labeling, shipping, repair and rework;
- conform to current AIAG guidelines and customer requirements;
- have accurate Severity/Occurrence/Detection ratings;
- be updated regularly as “living documents”;
- be used for Continuous Improvement per the GP-8 procedure.

## 5. PFMEA review process

Cross-functional teams shall periodically review PFMEAs.

Review frequency and/or number of PFMEA reviews is determined by supplier leadership based on:

- customer expectations (PR/Rs, DDW, launch activities, etc.);
- process capability (FTQ, SPC, etc.);
- changes to the process, including error proofing and Tier 2 changes.

Priority for review includes, among other cases:

- products from an acquisition, tool move, or supplier change;
- PFMEAs developed without adequate cross-functional involvement;
- parts with PR/R, customer complaint, warranty or FTQ history;
- significant changes in Occurrence ratings;
- PFMEAs with the oldest revision dates.

PFMEAs shall be reviewed and updated to verify that:

- all operations/processes are included and accurately represented, including paint, heat treat, material handling, labeling, rework/repair, etc.;
- all process controls are included;
- Detection ratings are accurate;
- Occurrence ratings are analyzed using available data such as SPC, FTQ, Quality Gate, C.A.R.E., scrap and Layered Process Audits;
- customer requirements and expectations are met (AIAG, PPAP, Launch, DDW, etc.).

## 6. Formal RPN reduction process

The source requires a formal and documented RPN reduction process.

Two complementary modes are identified:

### 6.1 Proactive RPN reduction

Purpose: reduce the risk of potential quality failures before they occur.

After PFMEA review:

1. establish and maintain a list of the highest-RPN risk-reduction opportunities;
2. use an action plan or equivalent to track progress in reducing RPN ratings;
3. complete actions and record results;
4. validate the resulting Occurrence and Detection ratings and revised RPN.

The example list ranks opportunities by RPN, identifies responsibility, recommended action, completion date and revised RPN.

## 7. Reverse PFMEA

**Definition:** Reverse PFMEA is an on-station review of all failure modes included in the PFMEA, performed by a cross-functional team, focused on verifying that proper prevention/detection controls exist and are working properly.

**Purpose:** support PFMEA reviews and RPN reduction using actual data from in-station audits of failure modes. The review is intended to:

- discover or create potential failure modes not considered during PFMEA development;
- validate Occurrence and Detection ratings against real data;
- verify that specified controls actually exist and operate properly.

### Reverse PFMEA flow

The source flow is:

`Scheduled station audit by cross-functional team → verify each PFMEA failure mode → proper prevention/detection control? → controls working properly? → verify next failure mode → all failure modes verified? → search for new potential failure modes → if new modes/nonconformances are found, develop an action plan → corrective action / PFMEA update.`

A negative answer at the control-existence or control-functioning decision leads to an action plan for the nonconformance.

### Reverse PFMEA audit schedule

A schedule is used to plan station audits by production line and station number. The example distinguishes:

- stations already audited;
- stations pending but on time;
- delayed audits.

The schedule makes audit coverage and overdue work visible over time.

### Reverse PFMEA checklist

The example checklist verifies, for each station/component, whether:

- a component can be installed improperly;
- improper installation can be detected at the station or downstream;
- a similar but wrong component can be installed and detected;
- a component can fall into/become lodged in the assembly and be detected;
- a damaged component can be installed and detected;
- the relevant detection method is actually performed.

The checklist also contains fields for PFMEA/RPN status and review/approval.

## 8. Reactive RPN reduction

Reactive RPN reduction addresses past quality issues through **error proofing**.

When corrective actions have been implemented, the team shall:

- validate the new Occurrence and Detection rankings and resultant RPN;
- update PFMEAs with all corrective-action measures;
- verify error proofing according to the Error Proofing Verification process.

## 9. Management requirements

Site leadership responsibilities include:

- review the need for PFMEA training at least annually;
- support RPN reduction activities and provide necessary resources;
- monitor and review RPN reduction activities;
- ensure formal cross-functional teams are used in PFMEA preparation and ongoing review.

## 10. Tracking matrix

The source provides an example PFMEA RPN Reduction Summary / Tracking Matrix for the overall plant.

The matrix combines:

- operation-level RPN summaries;
- number of causes;
- counts above selected RPN thresholds;
- highest individual RPN;
- monthly comparison of operation totals;
- a Top Ten RPN Reduction Plan with operation/station, RPN, failure mode, recommended action, completion date and responsibility;
- graphical monitoring of the distribution of causes by RPN range.

The source explicitly notes that the example is for reference and that the latest revision should be checked.

## 11. Summary of the control loop

The Risk Reduction process forms a closed management loop:

`PFMEA → rating of risk → prioritization by RPN → risk-reduction action → implementation → verification using actual process data → revised Occurrence/Detection/RPN → PFMEA update → continued review.`

Reverse PFMEA supplies an on-station verification mechanism; reactive error proofing supplies feedback from past failures; management tracking supplies prioritization, resources and follow-through.

## CMOC extraction note

Primary distinctions exposed by this source include:

- **risk is made actionable through a ranked reduction opportunity**;
- **PFMEA is a living control model, not a static document**;
- **Occurrence and Detection ratings require grounding in actual process data**;
- **Reverse PFMEA tests the correspondence between documented controls and controls actually operating at the station**;
- **risk reduction requires an explicit action-tracking mechanism**;
- **proactive and reactive risk reduction are complementary loops**;
- **cross-functional review is an architectural condition of the PFMEA process**;
- **leadership converts risk priorities into resource allocation and follow-through**.
