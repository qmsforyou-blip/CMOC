# GM Machine Passport — Schema CrossCheck v0.1

**Notice:** 0152+170926  
**Status:** TEST PATCH / NON-CANON

## 1. Purpose

Проверить, не является ли Machine Passport v0.1 скрыто заточенным под Machines типа GM-096, где identity часто выражается через управляемый переход состояния.

Тестируем на Machines с другой логикой действия:

- Andon — Response to Abnormality;
- Gemba Walk — direct observation / learning at actual place;
- Visual Control — Visual Control;
- Kamishibai — Assessment against Criterion.

В качестве контрольного объекта оставляем Expected-vs-Actual Control Verification.

---

## 2. Passport under test

```yaml
identity:
  name:
  identity_bearing_relation_or_mode:
  local_capability:
  closure_condition:

execution:
  trigger:
  inputs:
  preconditions:
  execution_boundary:
  states_actions:
  evidence:
  decision_logic:
  outputs:

realization:
  domain:
  internal_mechanisms:
  roles:
  artifacts:
  downstream_ownership:

relations:
  pattern:
  invokes:
  feeds:

provenance:
  source:
  status:
```

---

# 3. CrossCheck A — Andon

**Identity-bearing structure:** abnormality → signal/visibility → responsible response.

Passport fit:

- identity-bearing relation/mode: PASS;
- local capability: PASS;
- closure: PASS, with escalation as alternative branch;
- trigger: PASS;
- inputs/context: PASS;
- preconditions: PASS;
- boundary: PASS;
- states/actions: PASS;
- evidence: PASS;
- decision logic: PASS;
- outputs: PASS;
- internal mechanisms: PASS;
- roles/artifacts: PASS;
- downstream ownership: PASS;
- Pattern: Response to Abnormality.

**Result: PASS.**

Observation: no field presumes change-control or transition management.

---

# 4. CrossCheck B — Gemba Walk

**Identity-bearing structure:** direct presence at actual place → direct observation → understanding/questioning → finding/handoff.

Passport fit:

- identity-bearing relation/mode: PASS;
- local capability: PASS;
- closure: PASS when bounded at traceable finding/handoff;
- trigger: PASS, although trigger can be planned or event-driven;
- inputs/context: PASS;
- preconditions: PASS;
- boundary: PASS;
- states/actions: PASS;
- evidence: PASS;
- decision logic: PASS WITH QUALIFICATION — decision logic is light and may be `distributed`;
- outputs: PASS;
- internal mechanisms: PASS;
- roles/artifacts: PASS;
- downstream ownership: PASS;
- Pattern: HOLD.

**Result: PASS.**

Observation: Passport accommodates a Machine whose identity is an **execution mode** rather than a state-transition relation.

---

# 5. CrossCheck C — Visual Control

**Identity-bearing structure:** make relevant process state immediately visible through a standardized visual representation so that deviation/condition can be recognized by responsible users.

Passport fit:

- identity-bearing relation/mode: PASS;
- local capability: PASS;
- closure: PASS WITH QUALIFICATION — closure is reached when the intended visible state is established/maintained or the visual control hands off a deviation; downstream response is not necessarily part of the Machine;
- trigger: PASS / may be continuous rather than event-triggered;
- inputs/context: PASS;
- preconditions: PASS;
- boundary: PASS;
- states/actions: PASS;
- evidence: PASS — visible state itself is an artifact/evidence channel;
- decision logic: PASS WITH QUALIFICATION — may be external to the Machine;
- outputs: PASS;
- internal mechanisms: PASS;
- roles/artifacts: PASS;
- downstream ownership: PASS;
- Pattern: Visual Control.

**Result: PASS WITH QUALIFICATION.**

Important finding: `trigger` cannot be assumed to mean a discrete event. A Machine may be continuously active or condition-maintaining.

---

# 6. CrossCheck D — Kamishibai

**Identity-bearing structure:** scheduled/defined assessment at the workplace/process against a criterion/check question, producing a visible/traceable result and follow-up path.

Passport fit:

- identity-bearing relation/mode: PASS;
- local capability: PASS;
- closure: PASS at completion of assessment and disposition/handoff of findings;
- trigger: PASS — schedule/defined frequency can be intrinsic to realization;
- inputs/context: PASS;
- preconditions: PASS;
- boundary: PASS;
- states/actions: PASS;
- evidence: PASS;
- decision logic: PASS;
- outputs: PASS;
- internal mechanisms: PASS;
- roles/artifacts: PASS;
- downstream ownership: PASS;
- Pattern: Assessment against Criterion.

**Result: PASS.**

Observation: Passport can represent a Machine whose core is an assessment against a criterion without importing GM-096 change-control semantics.

---

# 7. Control — Expected-vs-Actual Control Verification

Identity remains:

`EXPECTED STATE ↔ REALIZED STATE → EVIDENCE → COMPARE → GAP → RESPONSE → VERIFY`

Passport fit: **PASS**.

This confirms that the schema still handles the previously tested comparison-based Machine while also handling signal-based, observation-mode and criterion-assessment Machines.

---

# 8. CrossCheck matrix

| Field | Andon | Gemba | Visual Control | Kamishibai | Expected-vs-Actual |
|---|---|---|---|---|---|
| Identity-bearing relation/mode | PASS | PASS | PASS | PASS | PASS |
| Local capability | PASS | PASS | PASS | PASS | PASS |
| Closure condition | PASS* | PASS | PASS* | PASS | PASS |
| Trigger | PASS | PASS | PASS* | PASS | PASS |
| Inputs/context | PASS | PASS | PASS | PASS | PASS |
| Preconditions | PASS | PASS | PASS | PASS | PASS |
| Boundary | PASS | PASS | PASS | PASS | PASS |
| States/actions | PASS | PASS | PASS | PASS | PASS |
| Evidence | PASS | PASS | PASS | PASS | PASS |
| Decision logic | PASS | QUAL. | QUAL. | PASS | PASS |
| Outputs | PASS | PASS | PASS | PASS | PASS |
| Domain | PASS | PASS | PASS | PASS | PASS |
| Internal mechanisms | PASS | PASS | PASS | PASS | PASS |
| Roles | PASS | PASS | PASS | PASS | PASS |
| Artifacts | PASS | PASS | PASS | PASS | PASS |
| Downstream ownership | PASS | PASS | PASS | PASS | PASS |
| Pattern | PASS | HOLD | PASS | PASS | PASS |

`*` = closure/trigger semantics may be continuous, branched or external to downstream response.

---

# 9. Schema stress findings

## 9.1 Trigger must not mean only "event"

The field `trigger` survives, but its semantics need widening.

A Machine can enter execution through:

- discrete event;
- scheduled invocation;
- condition becoming true;
- continuous/always-on operation;
- planned routine.

Therefore working meaning should become:

> **Trigger / entry condition — условие или режим, при котором Machine начинает или поддерживает своё execution.**

This is a schema refinement, not a new field.

## 9.2 Decision logic may be internal, distributed or absent

The field remains useful because it exposes the boundary of decisions, but it cannot be required to contain a local decision tree.

Allowed values should include:

- explicit;
- conditional;
- distributed;
- N/A.

## 9.3 Closure is not always "return to normal"

GM-096 strongly emphasizes transition and return to normal. The cross-domain test shows that closure can instead mean:

- signal transferred into response;
- finding handed off;
- visible state established;
- assessment completed and result recorded.

Therefore `closure_condition` is valid, but its value must be Machine-specific.

## 9.4 Outputs are local outputs

The schema continues to work if `outputs` means immediate Machine outputs rather than final enterprise outcomes.

This is essential for avoiding Assembly duplication.

## 9.5 Internal mechanisms remain non-identity

The cross-domain sample strengthens the earlier result: different internal compositions can realize the same Machine identity, and similar components can realize different Machines.

---

# 10. New working rule

The CrossCheck supports the following refinement:

> **Passport fields describe structural roles, not one fixed workflow. Their values must be allowed to vary by Machine.**

This prevents the schema from silently becoming:

`TRIGGER → INPUT → ACTION → DECISION → OUTPUT → CLOSE`

as a mandatory universal workflow.

Instead, Passport describes the invariant architecture of a bounded execution unit.

---

# 11. Does Passport still avoid SOP duplication?

**PASS.**

The cross-domain Machines require different execution modes:

- Andon — signal/response;
- Gemba — direct presence/observation;
- Visual Control — continuous visibility;
- Kamishibai — criterion-based assessment;
- Expected-vs-Actual Verification — comparison/re-verification.

A common Passport exists without imposing a common operating procedure.

---

# 12. Does Passport still avoid Assembly duplication?

**PASS.**

Each Machine has a local closure while downstream effects may continue into other Machines or Assemblies.

Passport therefore remains the description of the bounded unit, not the complete chain.

---

# 13. Architectural result

The schema has now survived two substantially different samples:

### Sample 1 — GM-096 transition/control Machines

PPCR / PTR / Banking / Bypass.

### Sample 2 — different Machine identity structures

Andon / Gemba / Visual Control / Kamishibai / Expected-vs-Actual Verification.

The Passport accommodates at least four identity-bearing forms:

```text
MODE OF ACCESS / EXECUTION
Gemba Walk

RELATION
Expected-vs-Actual Verification

SIGNAL → RESPONSE
Andon

CONTROLLED STATE / TRANSITION
Banking / Bypass / PTR / PPCR

CRITERION-BASED ASSESSMENT
Kamishibai

CONTINUOUS STATE VISIBILITY
Visual Control
```

This is strong evidence that the Passport schema is not merely a GM-096 template.

---

# 14. Status

- Passport Schema CrossCheck: **PASS**
- Cross-domain identity structures: **PASS**
- GM-096 bias detected: **NO MATERIAL BIAS DETECTED**
- Trigger semantics: **REFINEMENT REQUIRED**
- Decision logic semantics: **REFINEMENT REQUIRED**
- Closure semantics: **CONFIRMED AS MACHINE-SPECIFIC**
- Local outputs vs enterprise outcomes: **CONFIRMED**
- SOP duplication: **PASS**
- Assembly duplication: **PASS**
- Passport schema: **WORKING v0.1 → v0.2 CANDIDATE**
- Canon: **NON-CANON**

## No changes

No changes to:

- Machine Catalog;
- Canon;
- REG-001.

## Next step

Do not canonize yet.

The next useful test is a **Passport Boundary Test**: deliberately try to passport things that should *not* be Machines — a simple checklist, a document, a meeting, a KPI/dashboard, a raw monitoring activity, and a single mechanism — and verify that Passport either rejects them or exposes the missing Machine boundary.
