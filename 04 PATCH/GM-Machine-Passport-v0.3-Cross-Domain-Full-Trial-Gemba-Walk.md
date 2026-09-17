# GM-Machine-Passport v0.3 — Cross-Domain Full Trial: Gemba Walk

**Notice:** 0164+170926  
**Date:** 17-09-2026  
**Status:** PASS / WORKING SPECIFICATION SUPPORTED / NON-CANON

## 1. Purpose

Final cross-domain full-passport trial of Machine Passport v0.3 on a Machine substantially different from the GM-096 change/risk-verification family.

Selected realization: **Gemba Walk**.

The trial tests whether v0.3 can describe a Machine whose identity-bearing mode is direct access to the actual place and real work, rather than a change-control, comparison, or material-state transition.

## 2. Boundary proof

### Identity-bearing relation/mode

`DIRECT PRESENCE AT ACTUAL PLACE → DIRECT OBSERVATION OF REAL WORK → UNDERSTANDING / QUESTIONING → TRACEABLE FINDING`

The identity-bearing feature is the mode of access to reality: going to the actual place and directly observing the real work. The subsequent finding/handoff closes the bounded execution.

### Own execution boundary

`SELECT / ENTER ACTUAL PLACE → OBSERVE REAL WORK → UNDERSTAND / QUESTION → IDENTIFY SIGNIFICANT CONDITION / GAP / OPPORTUNITY → RECORD / HANDOFF FINDING`

The Machine does not own the downstream corrective action, problem solving, or process change.

### Local capability

Produce direct, traceable knowledge of actual work and convert significant observed conditions into a finding that can be handed to the responsible downstream mechanism.

### Closure condition

Defined observation scope completed and a traceable finding/handoff produced, or the observation scope explicitly closed with no significant finding.

## 3. Full v0.3 Passport

```yaml
machine_passport:
  identity:
    name: Gemba Walk
    identity_bearing_relation_or_mode: "DIRECT PRESENCE AT ACTUAL PLACE → DIRECT OBSERVATION OF REAL WORK → UNDERSTANDING / QUESTIONING"
    local_capability: "Produce direct, traceable knowledge of actual work and convert significant observed conditions into a finding for downstream action."

  execution:
    trigger: "Scheduled management observation, response to a need for direct knowledge, or defined walk scope."
    inputs_context:
      - defined area / workplace / process
      - purpose or observation scope
      - relevant working context
      - known issue or question, where applicable
    preconditions:
      - access to the actual place
      - defined or discoverable observation scope
      - observer able to directly observe the work
    execution_boundary: "SELECT / ENTER ACTUAL PLACE → OBSERVE REAL WORK → UNDERSTAND / QUESTION → IDENTIFY SIGNIFICANT CONDITION / GAP / OPPORTUNITY → RECORD / HANDOFF FINDING"
    execution_sequence:
      - go to the actual place
      - observe real work directly
      - understand the work and context
      - question / clarify where needed
      - distinguish significant condition, gap, or opportunity
      - create traceable finding
      - record or hand off finding
    evidence:
      - direct observation
      - observed work condition
      - notes / finding record
      - traceable handoff, where applicable
    decision_points_logic:
      - "Is the observed condition significant enough to record?"
      - "Is clarification / questioning required?"
      - "Does the finding require downstream action or handoff?"
    local_outputs:
      - direct knowledge of actual work
      - traceable finding
      - handoff to responsible downstream mechanism, where applicable
    closure_condition:
      type: handoff
      condition: "Defined observation scope completed and finding/handoff completed, or scope explicitly closed with no significant finding."
      evidence: "Observation record / finding / handoff or explicit closure record."
      downstream_continuation: allowed

  realization:
    domain: "Management / production process observation at the actual workplace"
    internal_mechanisms:
      - direct observation
      - questioning / clarification
      - finding capture
      - traceable handoff
    roles:
      - observer / manager
      - process / workplace personnel
      - downstream responsible owner, where action is required
    artifacts:
      - observation notes
      - finding / action record, where used
    domain_specific_conditions:
      - actual place must be accessible
      - real work must be directly observable
    limitations:
      - does not by itself establish root cause
      - does not by itself authorize corrective action or process change
      - does not replace a formal audit where an audit against defined criteria is required
      - does not by itself constitute continuous monitoring
    downstream_ownership: "Corrective action, problem solving, process change, or other downstream mechanisms own consequential action."

  relations:
    pattern: "Response to Abnormality / other Pattern relation is optional and context-dependent; no Pattern canonization implied."
    invokes_uses:
      - observation / recording mechanisms
      - local process information
      - downstream finding/action mechanisms
    feeds:
      - Expected-vs-Actual Control Verification, where an accepted expected state is explicitly introduced
      - Problem Solving, where a problem requires causal investigation
      - corrective action / change mechanisms, where downstream action is authorized

  validation:
    machine_boundary_test:
      identity_bearing_relation_or_mode: PASS
      own_execution_boundary: PASS
      local_capability: PASS
      closure_condition: PASS
      result: PASS

  provenance:
    source: "GM Quality System Basics Overview Supplier Audit — Gemba Walk material"
    evidence_reference: "GM QSB source material; prior CMOC Gemba Walk atomicity/composition and Machine Boundary Triangle tests"
    status: "MACHINE CANDIDATE / DOMAIN MACHINE / NON-CANON"
```

## 4. v0.3 field-by-field result

| Passport layer | Result | Observation |
|---|---|---|
| Identity | PASS | Identity is carried by direct-presence/direct-observation mode, not by a fixed component list. |
| Execution | PASS | Trigger, context, boundary, sequence, evidence, decisions, outputs and closure are representable. |
| Realization | PASS | Domain, mechanisms, roles, artifacts, limitations and downstream ownership remain realization-level properties. |
| Relations | PASS | Pattern and downstream relations remain optional/contextual and do not define identity. |
| Validation | PASS | Boundary proof is separated from the descriptive Passport core. |
| Provenance | PASS | Source and status are retained without substituting source text for the Passport. |

## 5. Adversarial boundary tests

### 5.1 Gemba Walk vs Monitoring

`OBSERVE / MEASURE → STATUS` is insufficient for Gemba Walk.

Gemba requires actual-place/direct-observation mode plus understanding/questioning and traceable finding. Therefore Monitoring does not absorb Gemba Walk.

**Result: PASS.**

### 5.2 Gemba Walk vs Audit

An audit is characterized by evaluation against defined criteria. Gemba Walk may use criteria, but criteria-based conformity evaluation is not required for its identity.

**Result: PASS.**

### 5.3 Gemba Walk vs Expected-vs-Actual Control Verification

Expected-vs-Actual requires an accepted expected state and explicit comparison. Gemba Walk does not require either.

**Result: PASS.**

### 5.4 Gemba Walk vs Problem Solving

Problem Solving requires causal investigation and consequential corrective action with verification. Gemba Walk can feed Problem Solving but does not contain that whole loop.

**Result: PASS.**

### 5.5 Gemba Walk vs Assembly

A sequence such as `GEMBA → VERIFICATION → PROBLEM SOLVING → ACTION → CLOSE` is an Assembly. The bounded Gemba execution itself remains a Machine.

**Result: PASS.**

## 6. Adversarial compression

Removing any of the following changes the identity or boundary materially:

- actual-place/direct-presence mode — identity collapses;
- direct observation of real work — no Gemba-specific access to reality;
- understanding/questioning — observation becomes generic monitoring;
- finding/handoff — local capability and closure become incomplete.

**Result: PASS.**

## 7. Cross-domain conclusion

Machine Passport v0.3 survives a full trial on Gemba Walk, a domain realization whose identity-bearing mode is fundamentally different from the change-control, trial-run, banking, bypass, PFMEA-review and expected-vs-actual family.

The trial confirms that v0.3 does not require:

- material transformation;
- state-transition of a product;
- explicit expected-state comparison;
- authorization as the identity-bearing relation;
- a fixed list of internal mechanisms;
- a particular domain vocabulary.

The schema remains capable of describing a bounded executable unit through:

`identity-bearing relation/mode + local capability + execution boundary + closure condition`

with reproducible execution captured separately.

## 8. Freeze decision

**Machine Passport v0.3 is sufficiently tested to be frozen as the WORKING specification.**

This is a methodological freeze, not ontological canonization. The schema may still be revised by later evidence, but further routine schema redesign is not justified by the present test set.

Working status:

`MACHINE PASSPORT v0.3 = WORKING SPECIFICATION / NON-CANON`

## 9. Scope of freeze

Frozen as working architecture:

```text
MACHINE PASSPORT
├── CORE
├── EXECUTION
├── REALIZATION
├── RELATIONS
├── VALIDATION
└── PROVENANCE
```

Core identity remains:

`identity-bearing relation/mode + local capability`

Execution boundary and closure remain mandatory execution properties.

Validation remains outside the descriptive identity core.

## 10. Catalog / Canon / REG-001 impact

- Catalog: **NO CHANGE**
- Canon: **NO CHANGE**
- REG-001: **NO CHANGE**
- Machine Passport v0.3: **WORKING FREEZE**

## 11. Final methodological status

**PASS.**

`Reverse PFMEA full passport → Gemba Walk cross-domain full passport → v0.3 freeze`

The Passport schema is now sufficiently validated for routine Machine passporting. Future changes should be evidence-driven rather than exploratory schema expansion.
