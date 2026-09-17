# GM-Machine-Passport-v0.2-Schema-Refactor-Test

**Notice:** 0158+170926  
**Date:** 17-09-2026  
**Status:** PASS / WORKING NON-CANON  

## 1. Purpose

Проверить предложенную рефакторизацию Machine Passport v0.2 после Field Necessity Test и установить, действительно ли разделение на:

- MACHINE CORE;
- EXECUTION CORE;
- REALIZATION;
- RELATIONS;
- PROVENANCE;
- VALIDATION

позволяет описывать разные типы Machines без скрытого требования одного типа исполнения, без дублирования identity и validation и без превращения Passport в Assembly или SOP.

## 2. Refactored working schema under test

```yaml
machine_passport:
  identity:
    name:
    machine_abstraction:
    identity_bearing_relation_or_mode:
    local_capability:

  execution:
    trigger:
    inputs_context:
    preconditions:
    execution_boundary:
    execution_sequence:
    evidence:
    decision_points_logic:
    local_outputs:
    closure_condition:

  realization:
    domain:
    internal_mechanisms:
    roles:
    artifacts:
    domain_specific_conditions:
    limitations:
    downstream_ownership:

  relations:
    pattern:
    invokes_uses:
    feeds:

  validation:
    machine_boundary_test:
      identity_bearing_relation_or_mode:
      own_execution_boundary:
      local_capability:
      closure_condition:
      result:

  provenance:
    source:
    evidence_reference:
    status:
```

Рабочее изменение относительно v0.2: `machine_boundary_test` вынесен из `identity` в `validation`. Значения, описывающие Machine, больше не должны дублироваться как будто это одновременно identity и результат проверки.

## 3. Test set

Проверены четыре Machines с разными identity-bearing structures:

1. Andon — signal-to-response relation.
2. Gemba Walk — direct-presence / actual-place execution mode.
3. Expected-vs-Actual Control Verification — comparison relation.
4. Production Trial Run (PTR) — bounded trial / evaluated-result transition.

Дополнительно проведён отрицательный тест на Assembly.

---

# 4. Trial A — Andon

## Identity

```yaml
identity:
  name: Andon
  machine_abstraction: Signal-to-Response Machine
  identity_bearing_relation_or_mode: abnormality -> visible signal -> responsible response
  local_capability: make an abnormality visible and transfer it into managed response
```

**Result:** PASS.

Identity не требует material/state transformation. Устойчивая identity задаётся отношением `abnormality -> signal/visibility -> response`.

## Execution

```yaml
execution:
  trigger: abnormality detected / response trigger
  inputs_context: abnormality and responsible response context
  preconditions: signal/visibility channel and responsible response path available
  execution_boundary: abnormality recognition through response initiation and resolution/escalation indication
  execution_sequence: abnormality -> signal -> visibility -> response -> resolved/escalated
  evidence: signal state, response initiation, resolution/escalation indication
  decision_points_logic: resolved? -> close : escalate/continue
  local_outputs: visible abnormality and initiated/accepted response
  closure_condition: resolution or accepted escalation
```

**Result:** PASS.

Schema does not force Andon into audit, verification or state-transition machinery.

## Realization

```yaml
realization:
  domain: production
  internal_mechanisms: detection/trigger, signal activation, visual/audible indication, response initiation, escalation
  roles: responsible responder / escalation role
  artifacts: Andon signal / board / indication channel
  domain_specific_conditions: production abnormality context
  limitations: does not own broader problem-solving closure
  downstream_ownership: problem solving / corrective action where required
```

**Result:** PASS.

Internal mechanisms remain realization, not identity.

## Validation

```yaml
validation:
  machine_boundary_test:
    identity_bearing_relation_or_mode: abnormality -> signal/visibility -> response
    own_execution_boundary: yes
    local_capability: yes
    closure_condition: resolution or accepted escalation
    result: PASS
```

**Result:** PASS.

Validation now records the test without pretending that the test itself defines the Machine.

---

# 5. Trial B — Gemba Walk

## Identity

```yaml
identity:
  name: Gemba Walk
  machine_abstraction: Direct-Reality Observation Machine
  identity_bearing_relation_or_mode: direct presence at actual place -> observe real work -> understand -> finding
  local_capability: obtain direct knowledge of actual work and turn significant observation into traceable finding
```

**Result:** PASS.

Identity-bearing element is mode of access to reality, not comparison against a formal criterion.

## Execution

```yaml
execution:
  trigger: scheduled/initiated visit or need for direct observation
  inputs_context: actual work area and working context
  preconditions: access to actual place
  execution_boundary: go to actual place through finding formation and record/handoff
  execution_sequence: actual place -> direct observation -> understand/question -> significant condition -> finding -> record/handoff
  evidence: direct observation and recorded finding
  decision_points_logic: significant finding/opportunity? -> record/handoff : continue observation
  local_outputs: traceable finding / direct knowledge
  closure_condition: finding recorded/handoff or observation scope completed
```

**Result:** PASS.

`trigger` допускает schedule, event или initiated mode. `closure_condition` не требует return-to-normal.

## Realization

```yaml
realization:
  domain: production/operations
  internal_mechanisms: physical presence, direct observation, questioning, finding formation
  roles: person conducting Gemba and responsible recipient
  artifacts: observation/finding record where used
  domain_specific_conditions: actual work must be accessible for direct observation
  limitations: does not own full corrective-action closure
  downstream_ownership: verification/problem solving/action mechanisms
```

**Result:** PASS.

## Validation

Validation independently confirms the boundary. It does not become part of the execution sequence.

**Result:** PASS.

---

# 6. Trial C — Expected-vs-Actual Control Verification

## Identity

```yaml
identity:
  name: Expected-vs-Actual Control Verification
  machine_abstraction: Expected-vs-Actual Control Verification
  identity_bearing_relation_or_mode: accepted expected state <-> realized state comparison
  local_capability: detect discrepancy/new information, initiate response and confirm result within bounded verification
```

**Result:** PASS.

The abstraction remains domain-neutral.

## Execution

```yaml
execution:
  trigger: scheduled verification / defined verification need
  inputs_context: accepted expected state, realized state, verification context
  preconditions: expected representation and access to realized state/evidence
  execution_boundary: expected state through evidence, comparison, finding, response handoff and re-verification
  execution_sequence: expected -> actual -> evidence -> compare -> gap/new information -> finding -> action/handoff -> verify
  evidence: observations, measurements, tests, records
  decision_points_logic: discrepancy? control effective? result confirmed?
  local_outputs: verified result, finding, action handoff
  closure_condition: verification result confirmed or bounded re-test/disposition completed
```

**Result:** PASS.

The schema preserves the defining comparison relation and does not confuse the Machine with the broader Risk Model Feedback Loop Assembly.

## Realization

```yaml
realization:
  domain: domain-independent / realized in production, maintenance, quality, etc.
  internal_mechanisms: observation, measurement, comparison, finding, action handoff, re-verification
  roles: verifier and responsible action owner
  artifacts: expected-state representation, checklist/record where used
  domain_specific_conditions: supplied by realization
  limitations: does not automatically own model/process update beyond its bounded boundary
  downstream_ownership: broader feedback / risk / process-management Assembly
```

**Result:** PASS.

## Validation

**Result:** PASS.

This is the strongest test of the refactor because the Machine abstraction itself is not tied to a named GM practice.

---

# 7. Trial D — Production Trial Run (PTR)

## Identity

```yaml
identity:
  name: Production Trial Run
  machine_abstraction: Controlled Trial Machine
  identity_bearing_relation_or_mode: controlled trial of production under defined conditions -> evaluated result
  local_capability: obtain bounded evidence about production readiness/effect under trial conditions
```

**Result:** PASS.

PTR identity is a bounded trial relation, not merely a list of test steps.

## Execution

```yaml
execution:
  trigger: authorized need to test a production change/process condition
  inputs_context: defined trial condition, product/process context, evaluation criteria
  preconditions: authorization, defined trial conditions and evaluation basis
  execution_boundary: trial initiation through evidence collection and evaluated result
  execution_sequence: define trial -> run -> collect evidence -> evaluate -> result
  evidence: trial records, measurements, observations, product/process results
  decision_points_logic: result acceptable? -> accept / further action
  local_outputs: evaluated trial result and evidence
  closure_condition: evaluated trial result recorded
```

**Result:** PASS.

PTR can be represented without embedding the whole Managed Transition Assembly.

## Realization

```yaml
realization:
  domain: production/process change
  internal_mechanisms: controlled run, evidence collection, evaluation
  roles: trial owner, production/quality participants
  artifacts: trial plan/record where used
  domain_specific_conditions: defined production trial conditions
  limitations: does not by itself own full change authorization and implementation closure
  downstream_ownership: change implementation / broader transition Assembly
```

**Result:** PASS.

## Validation

**Result:** PASS.

---

# 8. Negative test — Assembly

Candidate:

`GEMBA -> AUDIT/VERIFICATION -> ANDON -> PROBLEM SOLVING -> CORRECTIVE ACTION -> VERIFY -> CLOSE`

Attempted Passport classification:

- identity-bearing relation: no single invariant relation survives the entire composition;
- execution boundary: yes, but at broader orchestration level;
- local capability: broader managed improvement/closure capability;
- closure: Assembly closure rather than one bounded Machine closure.

**Result:** FAIL AS MACHINE / PASS AS ASSEMBLY.

The refactored Passport therefore does not classify an Assembly as a Machine merely because all fields can technically be filled.

---

# 9. Refactor-specific tests

## 9.1 Identity duplication test

Before refactor, `identity.machine_boundary_test.*` repeated identity facts.

After refactor:

`identity` = what the Machine is.

`validation.machine_boundary_test` = evidence that the classification test was passed.

**Result: PASS.**

## 9.2 Validation/execution separation test

Validation does not appear in `execution_sequence` and does not become an operational step of the Machine.

**Result: PASS.**

## 9.3 Assembly duplication test

Passport remains bounded to the Machine. Downstream continuation is represented through `downstream_ownership` and `feeds`, without importing the whole Assembly.

**Result: PASS.**

## 9.4 SOP duplication test

`execution_sequence` describes reproducible execution architecture, but not operator-level instructions, timings, tolerances or complete work instruction text.

**Result: PASS.**

## 9.5 Pattern duplication test

`relations.pattern` remains optional/HOLD. Pattern grammar is referenced, not redefined inside the Passport.

**Result: PASS.**

## 9.6 Domain forcing test

Gemba, Andon, Expected-vs-Actual and PTR retain different identity-bearing structures under one schema.

**Result: PASS.**

## 9.7 N/A / HOLD / distributed test

The schema still supports values such as `N/A`, `HOLD`, and `distributed` for fields that are structurally present but not applicable or not yet established for a particular Machine.

**Result: PASS.**

---

# 10. Resulting Passport architecture

The test supports the following working architecture:

```text
MACHINE CORE
  identity
    name
    machine_abstraction
    identity_bearing_relation_or_mode
    local_capability

EXECUTION CORE
  trigger
  inputs_context
  preconditions
  execution_boundary
  execution_sequence
  evidence
  decision_points_logic
  local_outputs
  closure_condition

REALIZATION
  domain
  internal_mechanisms
  roles
  artifacts
  domain_specific_conditions
  limitations
  downstream_ownership

RELATIONS
  pattern
  invokes_uses
  feeds

VALIDATION
  machine_boundary_test

PROVENANCE
  source
  evidence_reference
  status
```

## 11. Architectural conclusion

Рефакторизация проходит проверку.

Ключевое разделение:

> **Passport описывает Machine; Validation доказывает, что объект удовлетворяет критерию Machine.**

Отсюда:

```text
PATTERN
  ↓ realization
MACHINE
  ↓ domain realization
DOMAIN MACHINE
  ↓ composition/orchestration
ASSEMBLY
  ↓ broader capability
CAPABILITY
```

И отдельно:

```text
MACHINE PASSPORT
      ↓ describes
MACHINE

VALIDATION
      ↓ tests
MACHINE BOUNDARY
```

Это снимает обнаруженное ранее дублирование `machine_boundary_test` с Machine identity и сохраняет возможность описывать Machines, чья identity задаётся разными способами: режимом доступа к реальности, отношением сравнения, отношением signal-to-response или bounded trial.

## 12. Status

- Machine Passport v0.2 Schema Refactor Test: **PASS**
- MACHINE CORE: **STABLE WORKING**
- EXECUTION CORE: **STABLE WORKING**
- REALIZATION: **STABLE WORKING**
- RELATIONS: **STABLE WORKING**
- VALIDATION: **DEFINED / WORKING**
- PROVENANCE: **STABLE WORKING**
- Four-machine trial: **PASS**
- Assembly negative test: **PASS**
- Identity/validation duplication: **REMOVED**
- Canon: **NON-CANON**
- Machine Catalog: **NO CHANGE**
- REG-001: **NO CHANGE**

## 13. Next methodological step

Следующий тест: **Machine Passport v0.2 Field Semantics Test** — проверить не просто наличие полей, а однозначность их смысла: где заканчивается `identity`, где `execution_boundary`, чем `local_outputs` отличаются от `closure_condition`, а `downstream_ownership` — от `feeds`.

На этом шаге дополнительных изменений в Catalog / Canon / REG-001 не требуется.
