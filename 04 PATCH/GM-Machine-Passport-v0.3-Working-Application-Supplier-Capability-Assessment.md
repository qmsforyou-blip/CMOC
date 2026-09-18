# GM-096 — Machine Passport v0.3 — Working Application: Supplier Capability Assessment

**Notice:** 0167+180926  
**Status:** PASS WITH QUALIFICATION / WORKING SPECIFICATION SUPPORTED / NON-CANON  
**Source:** GM Quality System Basics Overview Supplier Audit, rev. March 2009, §10.3 Tiered Supplier Selection and Evaluation, pp. 306–309

---

## 1. Purpose of the trial

Apply the frozen **Machine Passport v0.3** to the candidate **Supplier Capability Assessment**, using the source's Potential Supplier Assessment (PSA) as the principal realization.

The test asks:

> Does supplier capability assessment possess an independent bounded execution identity, or is it merely an Audit / Assessment artifact inside the wider Supply Chain Management Assembly?

The distinction is important because the source contains both:
- a general requirement to assess suppliers;
- a concrete Potential Supplier Assessment (PSA) example used to weigh the risk of doing business with a new supplier.

No Catalog / Canon / REG-001 changes are made by this trial.

---

# 2. Source evidence

GM QSB §10.2–10.3 states that:
- all new suppliers shall be evaluated prior to placing business;
- the evaluation asks whether the supplier has systems in place meeting customer requirements;
- where new business is placed with an upstream supplier with no performance history, there shall be a method to evaluate supplier capability;
- the organization shall have the ability to weigh the risk of sourcing with that supplier;
- the source presents a Potential Supplier Assessment Audit (PSA) example;
- the PSA contains scored assessment items, risk/rating guidance and comments;
- examples include evaluation of supply-chain protection, process validation understanding, material identification/traceability, Tier 2–3–4 management, layered audits and process flow;
- the stated purpose of the PSA example is to weigh the risk of doing business with a new supplier.

The source also distinguishes ongoing supplier-quality-system measurement and assessment, including QSB, Process Control Plan, Labeling and Special Process Audits. fileciteturn171file0 fileciteturn171file2

---

# 3. Boundary proof

## 3.1 Identity-bearing relation / mode

Working identity-bearing relation:

**SUPPLIER CAPABILITY / REQUIREMENTS / BEST-PRACTICE EXPECTATIONS → STRUCTURED ASSESSMENT EVIDENCE → CAPABILITY / GAP / RISK CHARACTERIZATION → SOURCING DECISION INPUT**

The identity is not simply “audit the supplier”.

It is the bounded transformation of:
1. a supplier candidate;
2. defined requirements / expectations / capability criteria;
3. observed or documented evidence;

into:
- characterized capability;
- identified gaps;
- risk information for sourcing or supplier selection.

The source explicitly connects the assessment to evaluating capability and weighing sourcing risk. fileciteturn171file0

---

## 3.2 Own execution boundary

Working boundary:

> **Define/select supplier assessment scope and criteria → collect/evaluate supplier evidence → score or characterize capability/gaps/risk → complete assessment record → produce sourcing-risk input / assessment disposition.**

The Machine does not own:
- the whole supply-chain management system;
- supplier development as a long-term program;
- ongoing supplier performance monitoring;
- corrective-action management after selection;
- general document control;
- the final commercial sourcing decision as a generic management act.

It owns the **bounded assessment execution and production of capability/risk evidence**.

---

## 3.3 Local capability

> **Characterize a supplier's demonstrated capability against defined requirements/expectations and produce structured evidence about gaps and sourcing risk before or during supplier selection.**

This is narrower than Supply Chain Management.

It is also different from generic Audit:
- Audit can establish conformity/nonconformity against a criterion.
- Supplier Capability Assessment additionally transforms the assessment into a **capability/risk characterization for supplier selection**.

This distinction remains qualified because the source presents PSA explicitly as an audit example.

---

## 3.4 Closure condition

Working closure condition:

> The defined supplier assessment scope is completed; applicable evidence has been evaluated; capability/gaps/risk have been characterized; the assessment record is completed; and the resulting sourcing-risk input or assessment disposition is available to the owning selection process.

Closure is therefore the completion of a bounded **assessment-to-characterization** cycle, not necessarily the final sourcing decision.

---

# 4. Machine Passport v0.3

## CORE

### name

**Supplier Capability Assessment**

### identity_bearing_relation_or_mode

SUPPLIER CAPABILITY / REQUIREMENTS / EXPECTATIONS → STRUCTURED EVIDENCE → CAPABILITY / GAP / RISK CHARACTERIZATION → SOURCING DECISION INPUT

### local_capability

Characterize demonstrated supplier capability and associated gaps/risk against defined requirements and provide structured evidence for supplier selection or evaluation.

---

## EXECUTION

### trigger

Source-defined triggers include:
- new supplier evaluation before placing business;
- new upstream supplier with no performance history;
- supplier selection/evaluation requiring capability and sourcing-risk assessment.

### inputs_context

- supplier candidate / supplier;
- customer requirements;
- applicable GM-specific requirements;
- quality-system expectations;
- assessment criteria/items;
- risk-rating guidance;
- supplier evidence;
- comments and supporting documentation.

### preconditions

- supplier assessment scope is defined;
- applicable requirements/criteria are available;
- an assessment method exists;
- evidence can be obtained from the supplier;
- rating/characterization rules are available where scoring is used.

### execution_boundary

SELECT SUPPLIER / SCOPE → APPLY DEFINED CRITERIA → COLLECT / REVIEW EVIDENCE → EVALUATE CAPABILITY / GAPS → CHARACTERIZE RISK → COMPLETE ASSESSMENT RECORD → HAND OFF SELECTION INPUT / DISPOSITION

### execution_sequence

1. Identify the supplier and reason for assessment.
2. Define the applicable assessment scope and criteria.
3. Review available supplier evidence.
4. Assess capability against the defined requirements/expectations.
5. Record gaps, weaknesses or demonstrated capability.
6. Apply the defined rating/score guidance where applicable.
7. Characterize sourcing risk.
8. Complete comments and assessment records.
9. Produce the assessment output for supplier selection/evaluation.

### evidence

- completed PSA / supplier assessment;
- scored assessment items where applicable;
- supplier documentation/evidence;
- risk-rating guidance and assigned ratings;
- recorded gaps and comments;
- capability evidence;
- assessment disposition / selection input.

### decision_points_logic

- Does the supplier demonstrate the required capability?
- Are customer requirements/system expectations addressed?
- Are material gaps present?
- What sourcing risk is indicated by the assessment?
- Is additional evaluation/evidence required?
- Is the assessment complete enough to hand off to supplier selection/evaluation?

The Machine does not own the commercial decision to source; it produces structured evidence for that decision.

### local_outputs

- completed supplier capability assessment;
- capability characterization;
- identified gaps;
- sourcing-risk characterization;
- documented evidence and comments;
- assessment input to supplier selection/evaluation.

### closure_condition

**type:** mixed

**condition:**

ASSESSMENT SCOPE COMPLETED + EVIDENCE EVALUATED + CAPABILITY/GAPS/RISK CHARACTERIZED + ASSESSMENT RECORD COMPLETED + OUTPUT HANDED OFF TO SELECTION/EVALUATION OWNER

**evidence:**
- completed assessment;
- scoring/ratings where applicable;
- evidence references;
- comments/gaps;
- handoff/disposition.

**downstream_continuation:** allowed

---

# 5. REALIZATION

## domain

Supply chain / supplier selection and supplier quality management.

## internal_mechanisms

- defined assessment criteria;
- evidence review;
- capability evaluation;
- risk-rating/scoring;
- gap identification;
- assessment record;
- handoff to supplier selection/evaluation.

These are realization mechanisms, not separate identity-defining Machines.

## roles

The source establishes the assessment as part of supplier selection/evaluation. Ownership in the broader Supply Chain Management strategy is assigned to the Senior Purchasing Leader, with Supplier Quality Leader as champion. The exact execution role of an individual assessor is not fixed by the cited PSA excerpt and therefore remains **domain-specific / not inferred**. fileciteturn171file6

## artifacts

- Potential Supplier Assessment (PSA);
- assessment/rating sheet;
- supplier evidence;
- comments;
- capability/risk records.

## domain_specific_conditions

- new supplier or supplier without performance history;
- customer and GM-specific requirements;
- sourcing-risk consideration;
- defined assessment/rating criteria;
- supplier evidence must be available for evaluation.

## limitations

Supplier Capability Assessment does not itself:
- select the supplier commercially;
- manage the supplier after selection;
- replace ongoing supplier performance monitoring;
- replace supplier corrective-action/problem-solving mechanisms;
- constitute the entire Supply Chain Management system;
- automatically equal every supplier audit.

## downstream_ownership

The Machine hands off to:
- supplier selection / sourcing decision;
- supplier quality management;
- supplier development;
- additional assessment or audit where gaps/risk require it.

---

# 6. RELATIONS

### pattern

**Assessment against Criterion**

The candidate realizes an assessment pattern in which an object is evaluated against defined criteria and produces a characterized result/finding.

### invokes_uses

- supplier requirements / expectations;
- assessment criteria and rating guidance;
- supplier evidence;
- assessment record.

### feeds

- supplier selection/evaluation;
- supplier quality-management actions;
- supplier development;
- further audits/assessments;
- sourcing-risk management.

---

# 7. VALIDATION

## machine boundary test

### Identity-bearing relation / mode

**PASS WITH QUALIFICATION.**

The PSA contains a recognizable assessment-to-risk characterization relation, but the source also calls it a **Potential Supplier Assessment Audit**. Therefore the distinction from the broader Audit Machine requires preservation of the supplier-selection/risk context.

### Own execution boundary

**PASS.**

A bounded cycle exists from supplier/scope selection through criteria application, evidence evaluation, capability/risk characterization and handoff.

### Local capability

**PASS WITH QUALIFICATION.**

The candidate produces capability/risk characterization for supplier evaluation. However, the source's broader supplier-assessment language does not establish that every supplier assessment has exactly this capability; the present candidate is specifically grounded in the PSA / new-supplier realization.

### Closure condition

**PASS.**

The assessment closes when the defined scope is evaluated and its characterized result is completed and handed off.

### Result

**PASS WITH QUALIFICATION — Supplier Capability Assessment qualifies as a Machine candidate when realized as the bounded Potential Supplier Assessment / supplier-selection assessment.**

The qualification is retained because the source uses audit terminology and because the generalized abstraction must not absorb all supplier audits.

---

# 8. Adversarial boundary tests

| Candidate | Result | Reason |
|---|---|---|
| Generic Audit | FAIL as identical | Audit can evaluate an object against criteria; Supplier Capability Assessment additionally characterizes capability/risk for supplier selection/evaluation. |
| Potential Supplier Assessment Audit (PSA) | PASS as domain realization | This is the principal source realization of the candidate. |
| Layered Process Audit | FAIL as equivalent | LPA verifies compliance in layered manufacturing-system execution; it is not supplier-selection capability characterization. |
| Ongoing Supplier Performance Monitoring | FAIL as equivalent | Monitoring tracks performance over time; the candidate performs a bounded capability/risk assessment. |
| Supplier Development | FAIL as equivalent | Development changes supplier capability over time; assessment characterizes existing demonstrated capability/gaps. |
| Problem Resolution | FAIL as equivalent | Problem Resolution addresses a problem/cause/action/verification loop; supplier assessment characterizes supplier capability/risk. |
| Sourcing Decision | FAIL as Machine-equivalent | The assessment supplies decision input; it does not own the broader sourcing decision. |
| Assessment Checklist / Score Sheet | FAIL as Machine | These are artifacts supporting execution, not the bounded execution itself. |
| Supply Chain Management | FAIL as Machine-equivalent | Supply Chain Management is the larger Assembly/system containing assessment, monitoring, problem resolution, supplier development and other mechanisms. |

---

# 9. Machine vs Assembly boundary

Working composition:

SUPPLY CHAIN MANAGEMENT ASSEMBLY
→ SUPPLIER SELECTION / EVALUATION
→ **SUPPLIER CAPABILITY ASSESSMENT**
→ RISK / CAPABILITY CHARACTERIZATION
→ SOURCING DECISION OR FURTHER SUPPLIER ACTION

The candidate does not absorb:
- supplier performance monitoring;
- supplier problem resolution;
- supplier development;
- ongoing supplier management.

Its bounded identity remains:

SUPPLIER + DEFINED CRITERIA
→ EVIDENCE
→ CAPABILITY / GAP / RISK CHARACTERIZATION
→ SELECTION / EVALUATION INPUT

This is consistent with the Machine definition: a bounded executable unit with identity-bearing relation/mode, own execution boundary, local capability and closure condition.

---

# 10. Audit anti-duplication test

**PASS WITH QUALIFICATION.**

There is substantial structural overlap with Audit:

AUDIT:
OBJECT / CRITERION → EVIDENCE → EVALUATION → FINDING

SUPPLIER CAPABILITY ASSESSMENT:
SUPPLIER / CAPABILITY CRITERIA → EVIDENCE → CAPABILITY / GAP EVALUATION → RISK CHARACTERIZATION → SOURCING INPUT

Therefore:

- At the generic assessment level, Supplier Capability Assessment may be a **domain realization of Assessment against Criterion**.
- At the source-specific PSA level, the supplier-selection/risk characterization provides additional identity-bearing context.
- It must not be promoted as a wholly independent generic Machine without further cross-domain evidence.

This is the reason for the qualification.

---

# 11. Passport adequacy test

All v0.3 sections are usable:

- CORE — PASS WITH QUALIFICATION
- EXECUTION — PASS
- REALIZATION — PASS
- RELATIONS — PASS
- VALIDATION — PASS WITH QUALIFICATION
- PROVENANCE — PASS

No additional Passport field is required.

The test confirms that supplier-selection context belongs in **REALIZATION**, while the identity-bearing relation remains abstract enough to prevent the Passport from becoming a PSA-specific template.

---

# 12. Architectural conclusion

**Supplier Capability Assessment is a MACHINE CANDIDATE WITH QUALIFICATION.**

The strongest source-grounded realization is:

> **Potential Supplier Assessment (PSA) — a bounded assessment that evaluates a new/upstream supplier against defined requirements and capability criteria, characterizes gaps and sourcing risk, and produces structured input for supplier selection/evaluation.**

The qualification matters:

> The source calls the PSA an **audit example**, so we should not yet canonize a separate generic Machine that duplicates the already tested **Audit** candidate.

Boundary proof: **PASS WITH QUALIFICATION**  
Passport v0.3 application: **PASS**  
Machine / Assembly separation: **PASS**  
Audit anti-duplication: **PASS WITH QUALIFICATION**  
Status: **MACHINE CANDIDATE / QUALIFIED / NON-CANON**

No Catalog / Canon / REG-001 changes.

---

## 13. Next methodological step

GM-096 / adjacent Supply Chain candidates now include a qualified Supplier Capability Assessment.

The next useful step is **not another Passport-schema test**.

We should either:
1. continue routine passporting with the next candidate, or
2. perform a focused **Machine Boundary Comparison: Audit ↔ Supplier Capability Assessment ↔ Expected-vs-Actual Control Verification**, because the PSA has exposed a potentially important question about when a domain-specific assessment is a separate Machine versus a realization of a general assessment Machine.
