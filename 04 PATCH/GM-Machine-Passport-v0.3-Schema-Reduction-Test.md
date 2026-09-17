# GM Machine Passport v0.3 — Schema Reduction Test

**Notice:** 0161+170926  
**Status:** PASS WITH REFINEMENT / NON-CANON  

## 1. Purpose

Проверить, можно ли сократить Machine Passport v0.2 до стабильной компактной схемы без потери доказанных свойств:

- identity;
- execution boundary;
- local capability;
- trigger;
- reproducible execution;
- local result;
- closure;
- realization context;
- downstream boundary;
- provenance;
- validation.

## 2. Reduction principle

Сокращаем не по количеству полей, а по функции поля.

Поле сохраняется, если его удаление приводит к одному из эффектов:

1. теряется Machine identity;
2. теряется граница Machine;
3. теряется воспроизводимость исполнения;
4. теряется возможность проверить результат;
5. теряется различение Machine и Assembly;
6. теряется необходимая трассируемость описания.

## 3. Proposed v0.3 structure

```yaml
machine_passport:
  identity:
    name:
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
    result:

  provenance:
    source:
    evidence_reference:
    status:
```

## 4. Reduction decisions

### 4.1 `machine_abstraction`

**REMOVE as mandatory field.**

Reason: abstraction can be expressed by the Machine identity/name and identity-bearing relation. It is useful as a relation to a generalized Machine class, but the previous tests did not establish it as universally necessary.

If later required for ontology navigation, it can be represented as a relation rather than a core Passport field.

**Result: REMOVE FROM CORE.**

### 4.2 `machine_boundary_test`

**RETAIN, but move to `validation`.**

It is not Machine identity. It is evidence that the candidate satisfies the Machine boundary.

The validation object may reference rather than duplicate Passport values:

```yaml
validation:
  machine_boundary_test:
    identity_relation_confirmed:
    execution_boundary_confirmed:
    local_capability_confirmed:
    closure_confirmed:
  result: PASS | PASS_WITH_QUALIFICATION | FAIL
```

This prevents two competing descriptions of the same Machine property.

### 4.3 `decision_points_logic`

**RETAIN, but N/A/distributed allowed.**

A Machine may have intrinsic decisions, distributed decisions, or no meaningful decision point. Removing the field entirely would hide this distinction.

### 4.4 `domain`

**RETAIN in realization.**

Necessary to distinguish an abstraction-level Machine from its domain realization. May be N/A for a domain-neutral abstraction.

### 4.5 `internal_mechanisms`

**RETAIN in realization, not identity.**

It explains how the Machine is realized without defining what the Machine is.

### 4.6 `roles`

**RETAIN in realization.**

Roles are not identity-bearing but can be necessary for reproducing the realization.

### 4.7 `artifacts`

**RETAIN with N/A allowed.**

Some Machines have artifacts; some do not. The schema should not force artificial artifacts.

### 4.8 `domain_specific_conditions`

**RETAIN with N/A allowed.**

Captures realization constraints that materially affect execution without contaminating Machine identity.

### 4.9 `limitations`

**RETAIN with N/A allowed.**

Useful for boundary and applicability. Not identity-bearing.

### 4.10 `downstream_ownership`

**RETAIN.**

This field is not part of identity, but it is important for preventing Passport from silently absorbing Assembly-level work.

### 4.11 `pattern`

**RETAIN as optional/HOLD.**

Pattern mapping is a higher-level ontological relation and may legitimately remain unresolved.

### 4.12 `invokes_uses`

**RETAIN as optional relation.**

Useful for composition mapping; not identity-bearing.

### 4.13 `feeds`

**RETAIN as optional relation.**

Useful for Machine-to-Assembly / downstream mapping; not closure.

### 4.14 provenance

**RETAIN.**

`source`, `evidence_reference`, and `status` do not define Machine identity, but they are necessary for CMOC traceability and lifecycle control.

## 5. Cross-machine reduction trial

### Andon

```text
identity = abnormality → signal → response
capability = transfer abnormality into managed response
boundary = detection through response/resolution/escalation
closure = resolution or accepted escalation
```

All retained core fields remain meaningful.

**PASS.**

### Gemba Walk

```text
identity = direct presence → observation → understanding
capability = direct knowledge → traceable finding
boundary = actual-place access through finding/handoff
closure = finding/handoff
```

No expected-state comparison is forced.

**PASS.**

### Expected-vs-Actual Control Verification

```text
identity = expected ↔ actual comparison
capability = verified discrepancy/finding for response
boundary = expected-state reference through verified result
closure = verification result
```

The reduced structure preserves the comparison relation.

**PASS.**

### Production Trial Run

```text
identity = controlled trial → evaluated result
capability = determine acceptability under trial conditions
boundary = trial start through evaluated result
closure = result/decision
```

The reduced structure does not absorb the surrounding change-control Assembly.

**PASS.**

## 6. Assembly anti-absorption test

Assembly example:

```text
GEMBA → AUDIT/VERIFICATION → ANDON → PROBLEM SOLVING → CORRECTIVE ACTION → VERIFY → CLOSE
```

Attempting to represent this as one v0.3 Machine Passport causes the following failure:

- multiple identity-bearing relations;
- multiple local capabilities;
- multiple closure conditions;
- multiple downstream ownership boundaries;
- no single invariant execution relation.

Therefore the reduced Passport still acts as a classifier boundary between Machine and Assembly.

**PASS.**

## 7. Minimal stable core

The tests support the following compact Machine Core:

```yaml
identity:
  name:
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
```

This is the smallest tested structure that preserves both identity and reproducible execution.

## 8. Full Passport architecture

```text
MACHINE PASSPORT
│
├── IDENTITY
│   ├── name
│   ├── identity-bearing relation/mode
│   └── local capability
│
├── EXECUTION
│   ├── trigger
│   ├── inputs/context
│   ├── preconditions
│   ├── boundary
│   ├── sequence
│   ├── evidence
│   ├── decision logic
│   ├── local outputs
│   └── closure
│
├── REALIZATION
│   ├── domain
│   ├── mechanisms
│   ├── roles
│   ├── artifacts
│   ├── conditions
│   ├── limitations
│   └── downstream ownership
│
├── RELATIONS
│   ├── pattern
│   ├── invokes/uses
│   └── feeds
│
├── VALIDATION
│   └── machine boundary test
│
└── PROVENANCE
    ├── source
    ├── evidence reference
    └── status
```

## 9. Architectural result

The reduction test confirms that Passport v0.3 can be smaller than v0.2 without becoming a different artifact.

The central distinction is now explicit:

```text
CORE = what makes this a Machine
EXECUTION = how it is reproducibly executed
REALIZATION = how it is concretely embodied
RELATIONS = how it connects to other ontology objects
VALIDATION = why its Machine status is justified
PROVENANCE = where the description came from and what status it has
```

The Passport therefore remains descriptive rather than classificatory by field count.

## 10. Conclusion

**Schema Reduction Test — PASS WITH REFINEMENT.**

Confirmed:

- `machine_abstraction` can leave the mandatory schema;
- `machine_boundary_test` belongs under Validation, not Identity;
- Machine Core remains stable;
- Execution Core remains stable;
- Realization remains separate from identity;
- Relations remain optional;
- Provenance remains separate from ontology identity;
- N/A/HOLD/distributed remain necessary instance values;
- the reduced schema distinguishes Machines from Assemblies;
- four heterogeneous Machine types remain representable.

**Working status:** Machine Passport v0.3 CANDIDATE / NON-CANON.

**No Catalog / Canon / REG-001 changes.**

**Next methodological question:** run a `v0.3 Adversarial Compression Test` against borderline objects (Checklist, Record, Meeting, Monitoring, Static Visual Control) to ensure the reduced schema does not start classifying generic objects as Machines.