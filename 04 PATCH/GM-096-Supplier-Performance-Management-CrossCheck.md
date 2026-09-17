# GM-096 — Supplier Performance Management Cross-Check

**Source:** GM Quality Systems Basics rev. March 2009, pp. 317–322
**Status:** CROSS-CHECK / ASSEMBLY CANDIDATE / NON-CANON
**Notice:** Извещение на изменение, "GM-096-Supplier-Performance-Management-CrossCheck.md", 0125+170926

## 1. Source extraction

The Supplier Chain Management block requires a comprehensive, documented approach to managing the supply base. The source explicitly names:

- ranking for key suppliers;
- ranking system for key metrics;
- system to address supplier concerns;
- issuance of Corrective Action Requests;
- documented process for supplier improvement;
- control of Pass Through characteristics.

The source also requires updates concerning supplier concerns and responses, unacceptable supplier performance to expectations, and current supplier quality activities. (p.317)

The example on p.318 presents supplier activity through multiple performance measures over time, including quality-related PR/Rs, PPMs, stockouts, plant disruptions and downtimes. (p.318)

Page 320 presents a Supplier Metrics view combining overall supplier status with multiple indicators: rolling PPM, CARs, quality-system status, controlled shipping, supplier audit score and date of last supplier quality visit. The status legend distinguishes below minimum/not initiated, improvement/not complete, meets requirements/complete, and not applicable. (p.320)

Page 321 requires a systematic and disciplined approach to problem solving for all supply-chain tiers, including 5-Why root-cause analysis and Drill Deep and Wide / 3x5 Why to determine why the system failed. (p.321)

Page 322 summarizes the system as a documented systematic approach that assesses compliance and gaps to best practices, monitors supplier performance to established goals, and tracks responses to issues while verifying a systematic and disciplined problem-solving approach. (p.322)

## 2. CMOC distinctions

The source supports the following distinctions:

- Supplier Performance ≠ Supplier Capability
- Metric ≠ Status
- Status ≠ Concern
- Concern ≠ Corrective Action Request
- Corrective Action ≠ Improvement
- Action Completion ≠ Verified Improvement
- Supplier Improvement ≠ Supplier Assessment
- Supplier Management ≠ Single Supplier Event
- Supplier Tier ≠ Isolated Supplier Boundary

These distinctions are used here as CMOC interpretation of the source structure, not as quotations from GM.

## 3. Machine test

### Candidate: Supplier Performance Management

**Trigger:** supplier performance against established goals, supplier concern, unacceptable performance, or need for supplier improvement.

**Input:** supplier performance evidence, metrics, status and identified concerns.

**Possible sequence:**

`Measure → Status → Concern → CAR / Problem Resolution → Improvement → Reassessment`

At first sight this resembles a Machine. However, the source does not present one bounded, self-contained execution sequence with a single defined trigger, owner and acceptance condition. Instead it combines several management activities and explicitly connects them to other assessments, audits and problem-solving methods.

Therefore a new standalone Machine is not justified by pp.317–322.

## 4. Architectural cross-check

The block is better represented as an **Assembly / management loop** composed of existing or already-candidate elements:

`Supplier Capability Assessment`

→ supplies capability evidence and identified gaps;

`Supplier Performance Monitoring / Metrics`

→ observes performance against goals and key metrics;

`Supplier Statusing`

→ makes the current condition visible;

`Supplier Concern / CAR`

→ converts unacceptable performance into a managed issue;

`Systematic Problem Resolution`

→ determines root/system causes;

`Corrective / Development Action`

→ changes the supplier or its management controls;

`Reassessment`

→ checks whether the intended capability/performance condition has been restored or improved.

The source additionally requires this management logic across supply-chain tiers, so the assembly is not confined to the immediate supplier boundary.

## 5. Key architectural observation

The important pattern is not a new supplier-specific Machine but the **transition from observation to managed improvement**:

`Performance Evidence → Status → Concern → Response → Problem Solving → Improvement → Reassessment`

This complements the existing Supplier Capability Assessment candidate, whose passport already contains the assessment/development/reassessment loop.

The supplier-performance block therefore extends the management context around that candidate rather than duplicating it.

## 6. Boundary

This cross-check does not establish:

- a new top-level Machine named Supplier Performance Management;
- a universal supplier ranking formula;
- universal numerical thresholds for supplier status;
- a universal CAR workflow;
- a universal ownership model.

The source provides examples and required management elements, but not one universal implementation specification.

## 7. Relation to existing CMOC candidates

### Supplier Capability Assessment

Direct relationship. Performance evidence can initiate or inform an assessment; assessment can identify capability gaps and development needs. The existing candidate already contains a development/reassessment loop.

### Performance Metrics

Direct relationship. The source explicitly uses key metrics and longitudinal supplier activity measures.

### Systemic Problem Resolution

Direct relationship. The source explicitly requires systematic problem solving and Drill Deep and Wide / 3x5 Why through the supply chain.

### Corrective Action

Supporting element. CARs are explicitly named, but the source block does not redefine corrective action as a new generic mechanism.

## 8. Verdict

**Classification:** ASSEMBLY / MANAGEMENT LOOP / NON-CANON

**New Machine:** NO

**Existing Supplier Capability Assessment:** CONFIRMED, NOT DUPLICATED

**New Canon statement:** NO

**REG-001 modification:** NO

**New reusable mechanism:** NOT ESTABLISHED

The pages strengthen the architecture around supplier capability and performance management but do not justify another standalone Machine.

## 9. Status

**SOURCE-DERIVED / CROSS-CHECKED / NON-CANON**

Next check: continue within GM-096 Supplier Chain Management or proceed to the next source block after 322, maintaining the same Machine-test discipline.
