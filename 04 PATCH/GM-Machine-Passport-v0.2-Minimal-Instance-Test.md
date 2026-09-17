# GM Machine Passport v0.2 — Minimal Instance Test

**Notice:** 0160+170926  
**Status:** PASS / NON-CANON  

## 1. Purpose

Проверить, можно ли описать Machine минимальным набором Passport-полей так, чтобы не потерять:

- Machine identity;
- execution boundary;
- local capability;
- closure;
- воспроизводимость исполнения;
- различимость между разными Machines;
- границу Machine / Assembly.

Тест не определяет Canon и не меняет Catalog.

## 2. Working minimal set

Минимальный набор для **Machine Core**:

```yaml
identity:
  name:
  identity_bearing_relation_or_mode:
  local_capability:

execution:
  trigger:
  execution_boundary:
  execution_sequence:
  local_outputs:
  closure_condition:
```

Для практической воспроизводимости дополнительно требуются:

```yaml
execution:
  inputs_context:
  preconditions:
  evidence:
```

Итого:

```text
IDENTITY
+ BOUNDARY
+ CAPABILITY
+ TRIGGER
+ EXECUTION
+ OUTPUT
+ CLOSURE
+ CONTEXT/EVIDENCE
```

## 3. Instance A — Andon

```yaml
name: Andon
identity_bearing_relation_or_mode: abnormality → signal → responsible response
local_capability: make abnormality visible and transfer it into managed response
trigger: abnormality detected
execution_boundary: abnormality detection through response initiation and resolution/escalation
execution_sequence: detect → signal → visibility → response → resolve/escalate
local_outputs: visible abnormality / initiated response
closure_condition: result or accepted escalation
inputs_context: work process / abnormal condition
preconditions: response channel and responsible role available
evidence: signal/event/response record
```

**Result: PASS.** Identity is preserved without internal mechanism list.

## 4. Instance B — Gemba Walk

```yaml
name: Gemba Walk
identity_bearing_relation_or_mode: direct presence at actual place → direct observation → understanding
local_capability: obtain direct knowledge of actual work and produce traceable finding
trigger: planned or condition-driven visit
execution_boundary: arrival at actual place through finding/handoff
execution_sequence: go to place → observe → question/understand → identify finding → record/handoff
local_outputs: traceable finding
closure_condition: handoff or completed finding
inputs_context: actual work / working context
preconditions: access to actual place
 evidence: direct observation / recorded finding
```

**Result: PASS.** Identity is preserved without forcing expected-state comparison.

## 5. Instance C — Expected-vs-Actual Control Verification

```yaml
name: Expected-vs-Actual Control Verification
identity_bearing_relation_or_mode: compare realized state with accepted expected state
local_capability: detect discrepancy and produce verified finding for response
trigger: scheduled/condition-based verification
execution_boundary: expected-state reference through verified comparison result
execution_sequence: establish expected → observe actual → obtain evidence → compare → identify gap → finding → verify result
local_outputs: verified comparison result / finding
closure_condition: verification result confirmed
inputs_context: accepted expected state + realized state
preconditions: accepted reference and access to evidence
 evidence: observation/measurement/test/record
```

**Result: PASS.** Identity depends on comparison relation, not on the particular audit vocabulary.

## 6. Instance D — Production Trial Run

```yaml
name: Production Trial Run
identity_bearing_relation_or_mode: controlled trial execution → evaluated trial result
local_capability: determine whether a changed/new process can produce an acceptable result under trial conditions
trigger: authorized need to trial
execution_boundary: trial authorization/start through evaluated result
execution_sequence: define trial conditions → run → observe/measure → evaluate → result
local_outputs: evaluated trial result
closure_condition: result/decision
inputs_context: proposed process/change + trial conditions
preconditions: authorization and defined trial conditions
 evidence: trial measurements/observations/results
```

**Result: PASS.** Machine remains bounded and is not expanded into the whole change-control Assembly.

## 7. Minimality removal test

| Removed element | Result |
|---|---|
| name | Machine may remain identifiable formally, but Passport loses practical usability; keep as required artifact field |
| identity-bearing relation/mode | FAIL — identity collapses into generic workflow |
| local capability | FAIL — no statement of what bounded execution accomplishes |
| trigger | Reproducibility weakens; execution entry becomes undefined |
| execution boundary | FAIL — Machine cannot be distinguished from surrounding Assembly |
| execution sequence | FAIL for reproducible description; boundary becomes merely declarative |
| local outputs | FAIL/weak — local result and handoff boundary become unclear |
| closure condition | FAIL — cannot determine when bounded execution is complete |
| inputs/context | PASS only as abstraction; required for practical reproducibility |
| preconditions | PASS only as abstraction; required when conditions affect reproducibility |
| evidence | FAIL for verifiable Machines; PASS only for purely descriptive abstraction, therefore keep in Execution Core |
| internal mechanisms | PASS — non-identity field |
| roles | PASS — realization field |
| artifacts | PASS — N/A allowed |
| downstream ownership | PASS for identity itself, but boundary/Assembly distinction weakens; retain |
| pattern | PASS — may be HOLD/unknown |
| invokes/uses | PASS — relational enrichment only |
| feeds | PASS — relational enrichment; not closure |
| provenance.source | PASS for identity, but source traceability is lost |
| provenance.evidence_reference | PASS for identity, but evidence traceability is lost |
| provenance.status | PASS for identity, but CMOC lifecycle status is lost |

## 8. Key result

The true **Machine Core** is smaller than the full Passport:

```text
identity-bearing relation/mode
+ local capability
+ execution boundary
+ trigger
+ execution sequence
+ local outputs
+ closure condition
```

For a **reproducible and auditable Passport instance**, add:

```text
inputs/context
+ preconditions
+ evidence
```

The remaining fields describe realization, relations, validation, provenance, or boundary context.

## 9. Architectural consequence

Passport should distinguish two notions of completeness:

1. **Identity completeness** — enough information to establish what Machine is.
2. **Instance completeness** — enough information to reproduce, verify, contextualize and govern the Machine description.

Therefore a sparse Passport is not automatically an incomplete Machine. It may be a valid abstraction-level Passport instance with N/A/HOLD values in realization fields.

## 10. Machine / Assembly boundary

The four trials demonstrate that minimal Passport does not absorb the surrounding Assembly:

- Andon closes at managed response/resolution/escalation;
- Gemba closes at finding/handoff;
- Expected-vs-Actual closes at verified comparison result;
- PTR closes at evaluated trial result.

Downstream corrective action, process change, PFMEA update, or enterprise-level closure remain outside the Machine unless explicitly demonstrated as part of its own invariant execution boundary.

## 11. Conclusion

**Minimal Instance Test — PASS.**

Confirmed:

- Machine Core can be separated from full Passport;
- identity-bearing relation/mode is indispensable;
- execution boundary and closure are indispensable;
- local capability is indispensable;
- trigger and execution sequence are required for reproducible description;
- outputs are required to define the local result;
- context/preconditions/evidence strengthen reproducibility and verification;
- internal mechanisms do not define Machine identity;
- Pattern remains optional/HOLD;
- relational and provenance fields do not define identity;
- Passport can describe Machines with fundamentally different execution modes.

**No Catalog / Canon / REG-001 changes.**

**Next methodological question:** whether the resulting Passport can be reduced to a stable v0.3 schema without losing any proven capability or boundary information.