# GM-101 — Layered Process Audits — Development of High-Risk Items for Auditing

## Source
GM Quality System Basics Overview Supplier Audit.pdf, pp. 234–235, §7.2.2 Development of high risk items for auditing.

## SOURCE extraction

### p.234 — structure of high-risk audit items

1. **High risk items shall be identified and included in the audit.**
2. High-risk items should be organized into three main sections:
   - **Work Station** — a list of checks applicable to all work stations.
   - **Quality Focused** — checks specific to operations and developed by the plant based on quality feedback, process knowledge, and problem solving.
   - **Manufacturing System** — a list of system checks focused on compliance to plant operations.

### p.235 — examples of Work Station issues

The source gives the following examples:

1. Ensuring proper safety practices and PPE are being followed.
2. Ensuring proper tools, gages and materials are available and used.
3. Ensuring standardized work and quality standards are understood and followed.
4. Ensuring the Andon system is functioning properly.
5. Ensuring Workplace Organization and Visual Management standards are maintained, e.g. according to plant WPO standards and Visual Management policy.
6. Ensuring compliance to Material Processes — FIFO / Min.-Max. levels.

These are presented as **Examples of Work Station issues** and therefore are not treated as universal requirements for every plant.

## CMOC interpretation candidates

- **CAND-0554 — High-risk items are an explicit content object of the audit.** Risk identification is translated into specific audit checks rather than remaining only as an abstract risk assessment.
- **CAND-0555 — Audit content can be structured by control scope.** The three sections distinguish universal workstation checks, plant-specific quality-focused checks, and manufacturing-system compliance checks.
- **CAND-0556 — Quality-focused checks can be generated from organizational learning.** The source explicitly connects their development with quality feedback, process knowledge, and problem solving.
- **CAND-0557 — A workstation audit can combine multiple control dimensions.** The examples cover safety, resources, standardized work, abnormal-condition signaling, workplace organization/visual management, and material-flow controls.
- **CAND-0558 — Risk-based audit content can be made operational at the workstation.** The high-risk item becomes an observable check at the place where the operation occurs.

## Architectural significance

The key SOURCE contribution is the conversion of **high risk** into structured audit content:

**HIGH-RISK ITEM → AUDIT CHECK → CONTROL SCOPE**

with three scopes:

**WORK STATION → QUALITY FOCUSED → MANUFACTURING SYSTEM**

The Quality Focused category is particularly important because the source makes it explicitly endogenous to the plant's experience:

**QUALITY FEEDBACK + PROCESS KNOWLEDGE + PROBLEM SOLVING → QUALITY-FOCUSED CHECKS**

This establishes a mechanism by which audit content can evolve from operational experience and detected quality concerns.

## Boundary

Do not infer that the six Work Station examples on p.235 are mandatory checks for every organization. They are explicitly presented as examples. Likewise, do not infer that every organization must use exactly these three section names or an identical checklist structure beyond what the source explicitly states.
