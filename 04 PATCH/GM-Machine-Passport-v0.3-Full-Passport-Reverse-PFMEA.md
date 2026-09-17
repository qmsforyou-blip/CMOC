# GM Machine Passport v0.3 — Full Passport Trial: Reverse PFMEA

**Notice:** 0163+170926  
**Status:** PASS WITH QUALIFICATION / NON-CANON  

## 1. Purpose

Провести первый полный практический trial Machine Passport v0.3 на уже разобранной GM Machine Candidate — **Reverse PFMEA** — включая Identity, Execution, Realization, Relations, Validation и Provenance.

Цель — проверить не только форму схемы, но и её способность одновременно:

- зафиксировать Machine identity;
- показать bounded execution;
- сохранить границу с Risk Reduction Assembly;
- отразить конкретную domain realization;
- показать внутреннюю композицию без превращения её в identity;
- обеспечить validation и provenance.

## 2. Boundary proof

Перед заполнением Passport применяем отдельный boundary test.

### Identity-bearing relation

```text
PFMEA / EXPECTED CONTROL STATE
        ↓
ACTUAL STATION STATE
        ↓
OBSERVATION / TEST
        ↓
CONTROL GAP / NEW FAILURE MODE / RATING EVIDENCE
        ↓
FINDING / ACTION HANDOFF
```

### Own execution boundary

От выбора/подготовки станции и проверки Failure Modes до формирования verified findings/action handoff.

### Local capability

> Detect discrepancies between PFMEA-defined failure-mode/control expectations and realized station state, including previously unidentified failure modes, and produce verified findings for risk-model/process update.

### Closure

Machine closes when the bounded review produces the required findings/action handoff and no further Failure Mode within the defined review scope remains unchecked, or when the review is explicitly terminated according to its defined scope.

**Boundary result: PASS.**

## 3. Machine Passport v0.3

```yaml
machine_passport:
  identity:
    name: Reverse PFMEA
    identity_bearing_relation_or_mode: PFMEA/expected control state → actual station state → evidence → discrepancy/new failure mode → finding/action handoff
    local_capability: detect discrepancies between expected PFMEA controls and realized station state and produce verified findings for downstream risk-model/process update

  execution:
    trigger: scheduled station review / risk-reduction review
    inputs_context:
      - current PFMEA
      - known Failure Modes
      - station/process
      - Reverse PFMEA checklist
      - relevant quality/problem history
      - audit criteria
    preconditions:
      - station/process selected
      - audit schedule established
      - cross-functional team available
      - PFMEA and checklist available
      - safe controlled experiment method available where needed
    execution_boundary: station selection/preparation through completion of defined Failure Mode/control review and finding/action handoff
    execution_sequence:
      - select scheduled station
      - assemble cross-functional team
      - obtain PFMEA and checklist
      - enumerate Failure Modes
      - verify control existence
      - verify control effectiveness
      - validate Occurrence/Detection evidence where applicable
      - determine whether additional/new Failure Modes exist
      - conduct controlled station experiment where required
      - record findings and action-plan items
      - hand off downstream action
      - close defined review scope
    evidence:
      - station observation
      - control presence evidence
      - control operation/effectiveness evidence
      - checklist/audit result
      - controlled experiment result
      - rating-validation evidence
      - finding/action record
    decision_points_logic:
      - control present?
      - control working/effective?
      - Occurrence/Detection assessment supported?
      - all defined Failure Modes reviewed?
      - new Failure Mode discovered?
      - additional action required?
    local_outputs:
      - verified review results
      - confirmed control gaps
      - potential new Failure Modes
      - rating-validation observations
      - findings
      - action-plan items
    closure_condition:
      type: handoff + result
      condition: defined review scope completed and findings/action items handed off or explicitly dispositioned
      evidence: completed review/checklist and finding/action record
      downstream_continuation: allowed

  realization:
    domain: production process / station quality risk
    internal_mechanisms:
      - PFMEA Failure Mode review
      - control existence verification
      - control effectiveness verification
      - Occurrence/Detection evidence validation
      - controlled station experiment
      - new Failure Mode discovery
      - finding/action-plan formation
    roles:
      - cross-functional review team
      - station/process representatives
      - maintenance engineer for controlled experiments where required
      - designated action owner/champion downstream
    artifacts:
      - PFMEA
      - Reverse PFMEA checklist
      - audit schedule
      - action plan
      - review/findings record
    domain_specific_conditions:
      - actual production station/process is available
      - current PFMEA reflects the defined review scope
      - controlled experiments are conducted safely
    limitations:
      - does not own enterprise/process authorization to implement changes
      - does not by itself own PFMEA/Control Plan revision
      - does not by itself establish final effectiveness of downstream corrective action
      - does not replace broader Risk Reduction Assembly
    downstream_ownership: PFMEA/Control Plan/process-change owners and wider Risk Reduction Assembly

  relations:
    pattern: Risk Model Feedback Loop (working candidate; non-canon)
    invokes_uses:
      - PFMEA
      - Control Plan where applicable
      - Reverse PFMEA checklist
      - audit schedule
    feeds:
      - Risk Reduction Assembly
      - PFMEA update/reassessment
      - Control Plan/process-control update
      - downstream corrective/process-change mechanisms

  validation:
    machine_boundary_test:
      identity_relation_confirmed: true
      execution_boundary_confirmed: true
      local_capability_confirmed: true
      closure_confirmed: true
    result: PASS WITH QUALIFICATION

  provenance:
    source: GM Quality System Basics Overview Supplier Audit, Strategy 8 — RPN Risk Reduction / Reverse PFMEA
    evidence_reference: GM-8 Risk Reduction extraction and Reverse PFMEA Machine Decomposition / Independence / Composition tests
    status: MACHINE CANDIDATE / DOMAIN MACHINE / NON-CANON
```

## 4. Field-by-field audit

### Identity

The identity-bearing relation distinguishes Reverse PFMEA from generic Audit, Monitoring and Problem Solving.

The local capability is narrower than the wider Risk Reduction Assembly and therefore supports the Machine boundary.

**Identity: PASS.**

### Execution

The sequence is sufficiently concrete to reconstruct the bounded execution while remaining above SOP level.

It does not prescribe exact operator actions, timings or work instructions.

**Execution: PASS.**

### Realization

Internal mechanisms are explicit but remain subordinate to Machine identity.

This is important: if one internal mechanism is replaced, the Machine can remain the same if the invariant execution relation and local capability survive.

**Realization: PASS.**

### Downstream ownership

The Passport explicitly stops before:

- final PFMEA revision;
- Control Plan revision;
- implementation of process changes;
- final effectiveness of downstream corrective action.

This preserves the Machine/Assembly boundary.

**Boundary ownership: PASS.**

### Relations

Pattern remains a working candidate and therefore is not used as an identity requirement.

`feeds` describes downstream relation rather than closure.

**Relations: PASS.**

### Validation

Validation is structurally separate from the Machine description. It confirms the boundary rather than defining it.

**Validation: PASS WITH QUALIFICATION.**

## 5. Assembly anti-duplication test

Wider Risk Reduction architecture:

```text
PFMEA / RISK MODEL
      ↓
REVIEW
      ↓
RISK REDUCTION OPPORTUNITY
      ↓
ACTION / CONTROL / ERROR PROOFING
      ↓
VERIFY EFFECTIVENESS
      ↓
REASSESS RISK
      ↓
UPDATE PFMEA
      ↓
TRACK
```

Reverse PFMEA occupies only the diagnostic-verification portion:

```text
EXPECTED CONTROL MODEL
      ↓
ACTUAL STATION
      ↓
VERIFY / TEST
      ↓
FINDING
      ↓
ACTION HANDOFF
```

It therefore does not duplicate the Assembly.

**PASS.**

## 6. SOP anti-duplication test

Passport does not specify:

- exact operator motions;
- exact timing;
- exact checklist wording;
- detailed safety instructions;
- detailed sampling quantities;
- local work instruction sequence beyond the Machine-level execution architecture.

Therefore Passport remains an architectural description rather than SOP.

**PASS.**

## 7. Pattern realization test

The wider working Pattern is:

```text
REPRESENT → REALIZE → OBSERVE → COMPARE → GAP / NEW INFORMATION → ACT → VERIFY → UPDATE
```

Reverse PFMEA realizes only a bounded portion of this grammar:

```text
EXPECTED CONTROL MODEL
      ↓
REALIZED STATION
      ↓
OBSERVE / TEST
      ↓
COMPARE
      ↓
GAP / NEW FAILURE MODE / RATING EVIDENCE
      ↓
FINDING / ACTION HANDOFF
```

The remaining downstream action, verification and model update belong to the broader Assembly.

**PASS.**

## 8. Full trial result

| Passport layer | Result | Comment |
|---|---|---|
| Identity | PASS | Stable Machine identity established |
| Execution | PASS | Bounded and reproducible above SOP level |
| Realization | PASS | Domain mechanisms separated from identity |
| Relations | PASS | Pattern/feeds do not contaminate identity |
| Validation | PASS WITH QUALIFICATION | Boundary proof remains separate |
| Provenance | PASS | Source and evidence traceability retained |
| Machine/Assembly boundary | PASS | Downstream ownership explicit |
| SOP boundary | PASS | No operator-level prescription |

## 9. Architectural conclusion

The full Reverse PFMEA trial confirms that the reduced v0.3 Passport can serve as an actual Machine description rather than only as a testing abstraction.

The resulting structure is:

```text
BOUNDARY PROOF
      ↓
MACHINE PASSPORT
      ├── IDENTITY
      ├── EXECUTION
      ├── REALIZATION
      ├── RELATIONS
      ├── VALIDATION
      └── PROVENANCE
```

And the larger architecture remains:

```text
PATTERN
   ↓
MACHINE
   ↓
DOMAIN MACHINE
   ↓
ASSEMBLY
   ↓
CAPABILITY
```

## 10. Qualification

One point remains intentionally unresolved: whether **Reverse PFMEA** should eventually be represented as a domain Machine that realizes the generalized **Expected-vs-Actual Control Verification** Machine, or whether it should remain a distinct Machine candidate with a strong structural relation to that abstraction.

The Passport can represent either interpretation without structural change.

This is an ontological classification question, not a Passport schema failure.

## 11. Conclusion

**Full Machine Passport v0.3 Trial — PASS WITH QUALIFICATION.**

The schema is sufficiently stable for working use.

The remaining qualification concerns ontology classification, not field architecture.

**Working status:** Machine Passport v0.3 CANDIDATE / NON-CANON.

**No Catalog / Canon / REG-001 changes.**

**Next methodological question:** determine whether v0.3 can now be frozen as the working Machine Passport specification, or whether one final cross-domain full-passport trial is needed before freezing.