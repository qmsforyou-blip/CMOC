# GM QSB — Machine Passport v0.2 Schema Consolidation Test

**Notice:** 0155+170926  
**Status:** TEST PATCH / NON-CANON

## 1. Purpose

Собрать результаты:

- Machine Passport Test v0.1;
- Passport Schema CrossCheck;
- Passport Boundary Test;
- Passport Closure Test;

в единую рабочую schema `v0.2` и проверить её на разнородных Machines.

Цель — проверить не отдельные поля, а целостность Passport как инструмента идентификации и описания bounded Machine.

Это не канонизация schema.

## 2. Consolidated principle

Machine Passport описывает:

> **invariant identity + bounded execution + local capability + closure + realization + boundary relations**.

Он не описывает:

- полный Assembly;
- SOP;
- source document;
- организационную форму;
- фиксированный component list.

## 3. Consolidated schema v0.2

```yaml
machine_passport:
  identity:
    name:
    machine_abstraction:
    identity_bearing_relation_or_mode:
    local_capability:
    machine_boundary_test:
      identity_bearing_relation_or_mode:
      own_execution_boundary:
      local_capability:
      closure_condition:
      result:

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

  provenance:
    source:
    evidence_reference:
    status:
```

## 4. Schema rules

### 4.1 Required semantic core

Every candidate claiming Machine status must establish:

```text
identity-bearing relation/mode
        +
own execution boundary
        +
local capability
        +
closure condition
```

If one of these cannot be established, the Passport does not establish Machine identity.

### 4.2 Execution fields

`trigger`, `inputs_context`, `preconditions`, `execution_boundary`, `execution_sequence`, `evidence`, `decision_points_logic`, `local_outputs` describe reproducibility.

They do not independently prove Machine identity.

### 4.3 Closure

`closure_condition` is required.

It must not be interpreted as universal `return_to_normal` or `final_state`.

Working closure types:

```text
result
 decision
 verification
 disposition
 transition
 handoff
 mixed
```

### 4.4 State-transition neutrality

`execution_sequence` replaces the stronger assumption that every Machine must be represented as a state-transition machine.

A Machine may be primarily:

- a mode of access to reality;
- a comparison relation;
- a signal-to-response relation;
- an assessment;
- a knowledge transfer;
- a controlled transition.

States may be explicit, implicit, or N/A.

### 4.5 N/A / HOLD / distributed

Schema must support explicit semantic values:

- `N/A` — field is structurally relevant to schema but not applicable to this Machine;
- `HOLD` — relation/value not yet established;
- `distributed` — responsibility or execution is deliberately distributed across Machines / Assembly.

These values mean different things and must not be collapsed.

## 5. Consolidation trial — Machine 1: Andon

### Identity

`ABNORMALITY → SIGNAL / VISIBILITY → RESPONSIBLE RESPONSE`

### Capability

Make abnormality visible to responsible response and transfer it into managed response until resolution or escalation.

### Closure

`result / escalation / resolution`

### Execution

`trigger → signal → visibility → response → resolved? → resolution / escalation`

### Realization

Internal mechanisms may include trigger, signal, display, audible indication, response initiation and escalation.

### Boundary

Ends at bounded signal-to-response result; broader problem solving may continue downstream.

**Schema result: PASS.**

No field requires artificial material-state framing.

## 6. Consolidation trial — Machine 2: Gemba Walk

### Identity

`DIRECT PRESENCE AT ACTUAL PLACE`

### Capability

Obtain direct knowledge of actual work and produce a traceable finding.

### Closure

`result / handoff`

### Execution

`actual place → observation → understand/question → finding → traceable handoff`

### Realization

Observation, questioning, contextual understanding, recording/handoff.

### Boundary

Does not include downstream corrective action or complete problem closure.

Pattern remains `HOLD` where not established.

**Schema result: PASS.**

`execution_sequence` works where a literal state machine would be misleading.

## 7. Consolidation trial — Machine 3: Expected-vs-Actual Control Verification

### Identity

`EXPECTED STATE ↔ REALIZED STATE → EVIDENCE → COMPARE`

### Capability

Detect discrepancy between accepted expected control state and realized state, initiate response and establish verification result.

### Closure

`verification / result / handoff`, depending on bounded realization.

### Execution

`expected → actual → evidence → compare → gap/new information → finding → action handoff → verify`

### Realization

Monitoring + comparison/audit + finding/handoff + verification.

### Boundary

Does not automatically include complete corrective action or model/requirement update.

**Schema result: PASS.**

## 8. Consolidation trial — Machine 4: Production Trial Run

### Identity

`TRIAL CONDITION → EXECUTE TRIAL → EVALUATE → ACCEPT / REJECT / FURTHER ACTION`

### Capability

Generate bounded trial evidence sufficient to establish an evaluated trial result.

### Closure

`decision / result`

### Execution

Trial setup → execution → evidence collection → evaluation → result.

### Realization

Trial method, roles, measurement/evidence, acceptance criteria, artifacts.

### Boundary

Does not include complete change implementation or entire Managed Transition Assembly.

**Schema result: PASS.**

## 9. Consolidation trial — Machine 5: Banking Process

### Identity

`OUT-OF-NORMAL MATERIAL / STATE → CONTROLLED BANK → DISPOSITION`

### Capability

Keep out-of-normal material/state under controlled status until authorized disposition.

### Closure

`disposition / release / scrap / rework / return`

### Execution

Entry → identification → status control → evaluation/disposition → controlled exit.

### Realization

Bank identification, status marking, segregation, authorization, records.

### Boundary

Downstream rework, release or process correction may remain outside the Machine.

**Schema result: PASS.**

## 10. Consolidation trial — Machine 6: PPCR / Plant Process Change Control

This candidate remains deliberately qualified because previous testing left open whether PPCR is itself a Machine or an authorization mechanism inside Managed Transition Assembly.

### Passport behavior

The schema can describe it without forcing a classification.

Possible identity:

`CHANGE REQUEST → ASSESS → AUTHORIZE / REJECT`

Possible local capability:

Establish a controlled authorization decision for a proposed process change.

Possible closure:

`decision`

Status remains candidate / qualified.

**Schema result: PASS WITH QUALIFICATION.**

This is a useful demonstration that Passport completeness does not equal ontological classification.

## 11. Cross-machine matrix

| Field | Andon | Gemba | Expected-vs-Actual | PTR | Banking | PPCR |
|---|---|---|---|---|---|---|
| identity-bearing relation/mode | PASS | PASS | PASS | PASS | PASS | QUALIFIED |
| machine boundary test | PASS | PASS | PASS | PASS | PASS | QUALIFIED |
| local capability | PASS | PASS | PASS | PASS | PASS | QUALIFIED |
| trigger | PASS | PASS | PASS | PASS | PASS | PASS |
| inputs/context | PASS | PASS | PASS | PASS | PASS | PASS |
| preconditions | PASS | PASS | PASS | PASS | PASS | PASS |
| execution boundary | PASS | PASS | PASS | PASS | PASS | QUALIFIED |
| execution sequence | PASS | PASS | PASS | PASS | PASS | PASS |
| evidence | PASS | PASS | PASS | PASS | PASS | PASS |
| decision logic | PASS | N/A / local | PASS | PASS | PASS | PASS |
| local outputs | PASS | PASS | PASS | PASS | PASS | PASS |
| closure condition | PASS | PASS | PASS | PASS | PASS | QUALIFIED |
| internal mechanisms | PASS | PASS | PASS | PASS | PASS | PASS |
| roles | PASS | PASS | PASS | PASS | PASS | PASS |
| artifacts | PASS | PASS | PASS | PASS | PASS | PASS |
| downstream ownership | PASS | PASS | PASS | PASS | PASS | PASS |
| pattern | HOLD possible | HOLD | HOLD possible | HOLD/known | HOLD/known | HOLD |
| invokes/uses | PASS/optional | PASS/optional | PASS/optional | PASS/optional | PASS/optional | PASS/optional |
| feeds | PASS | PASS | PASS | PASS | PASS | PASS |
| provenance | PASS | PASS | PASS | PASS | PASS | PASS |

## 12. Anti-duplication tests

### 12.1 Pattern duplication

FAIL avoided.

Passport records `pattern` as relation, not as Machine definition.

### 12.2 Assembly duplication

FAIL avoided.

`downstream_ownership` marks boundary without absorbing downstream execution.

### 12.3 SOP duplication

FAIL avoided.

`execution_sequence` describes invariant execution architecture, not enterprise-specific operator instructions.

### 12.4 Source duplication

FAIL avoided.

`provenance` points to source/evidence; Passport does not replace source material.

## 13. Identity test

A critical consolidation result:

```text
Machine identity
    ≠ name
    ≠ component list
    ≠ workflow length
    ≠ number of fields filled
    ≠ source terminology
```

Identity is established by:

```text
invariant execution relation/mode
        +
own bounded execution
        +
local capability
        +
closure
```

## 14. Schema v0.2 — working interpretation

The consolidated Passport has four semantic layers:

```text
A. IDENTITY
   What is this bounded Machine?

B. EXECUTION
   How does its invariant execution occur?

C. REALIZATION
   How is this Machine concretely realized?

D. RELATIONS / PROVENANCE
   Where does it sit in the wider ontology and evidence chain?
```

The layers should not be collapsed.

## 15. Important refinement: `inputs_context`

`inputs` is too narrow for Machines such as Gemba Walk.

Working replacement:

`inputs_context`

This allows the Passport to represent:

- artifacts;
- signals;
- expected state;
- actual place/context;
- prior findings;
- authorization;
- other supplied conditions.

It does not imply that every Machine consumes a discrete artifact.

## 16. Important refinement: `execution_sequence`

`states_actions` is too state-transition-oriented.

Working replacement:

`execution_sequence`

It can represent:

```text
mode → observation → finding
relation → comparison → result
signal → response → escalation
trial → evidence → evaluation → decision
state → control → disposition
```

without imposing a universal state-machine ontology.

## 17. Important refinement: `local_outputs`

The output field should distinguish the Machine's own result from downstream effect.

```text
local_outputs
    ≠
downstream_effects
```

A finding can be the local output even when corrective action happens downstream.

## 18. Important refinement: closure

`closure_condition` remains mandatory but is interpreted relative to Machine boundary.

It can be typed:

```yaml
closure_condition:
  type: result | decision | verification | disposition | transition | handoff | mixed
  condition:
  evidence:
  downstream_continuation: allowed | not_allowed | distributed
```

## 19. Final consolidation result

### PASS

The working v0.2 schema successfully accommodates Machines with different identity modes:

- signal-to-response;
- direct presence/observation;
- comparison relation;
- trial/evaluation;
- controlled disposition;
- qualified authorization decision.

It does not require:

- material transition;
- physical state change;
- identical workflow;
- fixed components;
- immediate return to normal.

### PASS WITH QUALIFICATION

PPCR remains ontologically unresolved as Machine vs authorization mechanism within a larger Assembly, but the Passport schema itself handles this uncertainty correctly.

## 20. Architectural conclusion

The Passport can now be treated as a **working v0.2 schema candidate**, not yet canonical.

Core principle:

> **Passport first establishes whether a bounded Machine exists; then it describes its invariant execution and concrete realization. It does not create Machine identity by filling fields.**

And the broader architecture remains:

```text
PATTERN
  ↓ grammar of composition
MACHINE
  ↓ bounded executable unit
DOMAIN MACHINE
  ↓ concrete realization
ASSEMBLY
  ↓ larger-scope composition
CAPABILITY
```

## 21. Status

- Passport v0.1 consolidation: `PASS`
- Boundary Test incorporated: `PASS`
- Closure Test incorporated: `PASS`
- Schema CrossCheck incorporated: `PASS`
- State-transition neutrality: `CONFIRMED`
- `inputs_context`: `REFINED`
- `execution_sequence`: `REFINED`
- `local_outputs`: `REFINED`
- typed `closure_condition`: `REFINED`
- N/A / HOLD / distributed: `REQUIRED SCHEMA SUPPORT`
- Anti-duplication tests: `PASS`
- Six-machine consolidation trial: `PASS / PASS WITH QUALIFICATION`
- Passport schema: `WORKING v0.2 CANDIDATE`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

## 22. Next step

Не следует сразу канонизировать v0.2.

Следующий тест — **Machine Passport v0.2 Adversarial Test**: попытаться сломать consolidated schema на пограничных случаях, где объект выглядит особенно похожим на Machine: Audit, Problem Solving, Knowledge Transfer/Yokoten, Visual Control и один составной Assembly.

Цель — проверить, не начала ли schema принимать за Machine любой хорошо описанный process/mechanism и не потеряла ли она границу Machine ↔ Assembly.
