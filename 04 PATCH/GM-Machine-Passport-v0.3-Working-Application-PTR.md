# GM Machine Passport v0.3 — Working Application: Production Trial Run (PTR)

**Notice:** 0165+170926  
**Date:** 17-09-2026  
**Status:** PASS / MACHINE CANDIDATE / NON-CANON

## 1. Purpose

First routine application of the frozen-as-working Machine Passport v0.3 to an existing GM-096 Machine Candidate: **Production Trial Run (PTR)**.

The purpose is no longer to test the Passport schema itself, but to demonstrate the working extraction rule:

`BOUNDARY PROOF → MACHINE? → PASSPORT v0.3`

## 2. Boundary proof

### Identity-bearing relation

`PLANNED / REQUIRED CHANGE OR CONDITION → CONTROLLED PRODUCTION TRIAL → OBSERVED TRIAL RESULT → EVALUATION / RELEASE DECISION`

The identity-bearing relation is the controlled execution of a production trial to obtain evidence before normal implementation/release of the tested condition.

### Own execution boundary

`DEFINE TRIAL → PREPARE CONTROLLED CONDITIONS → RUN TRIAL → OBSERVE / MEASURE → EVALUATE RESULT → RELEASE / REJECT / ESCALATE`

The PTR does not own the broader change authorization process or subsequent permanent implementation unless those are explicitly included as downstream mechanisms.

### Local capability

Produce controlled production evidence sufficient to determine whether the tested condition/change is acceptable for the defined trial purpose.

### Closure condition

Defined trial completed and its result evaluated and dispositioned: accepted/released, rejected, or transferred for further action/retrial.

**Boundary result: PASS.**

## 3. Machine Passport v0.3

```yaml
machine_passport:
  identity:
    name: Production Trial Run (PTR)
    identity_bearing_relation_or_mode: "PLANNED / REQUIRED CHANGE OR CONDITION → CONTROLLED PRODUCTION TRIAL → OBSERVED TRIAL RESULT → EVALUATION / RELEASE DECISION"
    local_capability: "Produce controlled production evidence sufficient to determine whether the tested condition/change is acceptable for the defined trial purpose."

  execution:
    trigger: "Defined need to validate a proposed or changed production condition through a controlled production trial."
    inputs_context:
      - trial objective
      - proposed / changed condition
      - relevant process requirements
      - trial parameters / acceptance criteria
      - affected product/process context
    preconditions:
      - trial scope defined
      - responsible personnel assigned
      - controlled trial conditions established
      - acceptance/evaluation criteria available
      - required safety and production controls in place
    execution_boundary: "Trial definition/preparation through controlled run, evaluation and disposition of the trial result."
    execution_sequence:
      - define trial objective and scope
      - establish controlled trial conditions
      - run production trial
      - observe / measure relevant results
      - compare results with defined acceptance criteria
      - evaluate trial outcome
      - release / accept, reject, escalate or require retrial
      - record result and disposition
    evidence:
      - trial plan / defined conditions
      - production trial observations
      - measurements / test results
      - acceptance evaluation
      - trial result / disposition record
    decision_points_logic:
      - "Were defined trial conditions achieved?"
      - "Are required observations / measurements available?"
      - "Does the result meet acceptance criteria?"
      - "Is retrial or downstream action required?"
    local_outputs:
      - controlled trial evidence
      - evaluated trial result
      - release / acceptance decision or rejection/escalation
      - retrial/downstream action requirement where applicable
    closure_condition:
      type: result + disposition
      condition: "Defined trial completed, result evaluated, and disposition established."
      evidence: "Trial result/evaluation and disposition record."
      downstream_continuation: allowed

  realization:
    domain: "Production process / controlled validation of changed or proposed production condition"
    internal_mechanisms:
      - controlled production run
      - observation / measurement
      - acceptance evaluation
      - result disposition
    roles:
      - trial owner / responsible process personnel
      - production personnel
      - quality / engineering representatives as required
      - authorized downstream decision owner where release authority is separate
    artifacts:
      - trial plan / parameters
      - test or measurement records
      - trial result
      - disposition record
    domain_specific_conditions:
      - production conditions must be sufficiently controlled for the trial objective
      - acceptance criteria must be defined or otherwise established for evaluation
    limitations:
      - does not automatically own authorization to introduce permanent process change
      - does not replace broader change control
      - does not by itself constitute long-term effectiveness monitoring
      - does not prescribe operator-level SOP
    downstream_ownership: "Permanent implementation, broader change authorization and longer-term effectiveness remain with their respective downstream mechanisms/owners."

  relations:
    pattern: "Managed Transition (working candidate; non-canon), where PTR functions as the controlled transition/evaluation mechanism."
    invokes_uses:
      - trial criteria / requirements
      - process/product information
      - measurement/test mechanisms
    feeds:
      - change-control decision
      - implementation / release mechanism
      - corrective action or retrial mechanism where result is unacceptable

  validation:
    machine_boundary_test:
      identity_bearing_relation_or_mode: PASS
      own_execution_boundary: PASS
      local_capability: PASS
      closure_condition: PASS
      result: PASS

  provenance:
    source: "GM Quality System Basics Overview Supplier Audit — GM-096 Managing Change / Production Trial Run"
    evidence_reference: "GM-096 extraction and prior PTR Machine Candidate / Passport trial"
    status: "MACHINE CANDIDATE / NON-CANON"
```

## 4. Working application audit

| Layer | Result | Observation |
|---|---|---|
| Boundary proof | PASS | Controlled trial has an autonomous execution boundary and local capability. |
| Identity | PASS | Identity is the controlled trial-to-evaluation relation, not merely testing as an isolated mechanism. |
| Execution | PASS | Trial can be reconstructed above SOP level. |
| Realization | PASS | Production-specific mechanisms and roles remain realization properties. |
| Relations | PASS | PTR can feed change/release decisions without becoming the entire Managed Transition Assembly. |
| Validation | PASS | Boundary proof is retained separately from the descriptive Passport. |
| Provenance | PASS | GM-096 source and prior extraction are traceable. |

## 5. Boundary distinctions

### PTR vs generic testing

A generic test can produce a measurement or result. PTR is a bounded production-trial execution with controlled production conditions and a disposition against a defined trial purpose.

**Result: PASS.**

### PTR vs PPCR / Change Control

PPCR governs whether a process change is authorized/controlled. PTR supplies controlled production evidence for evaluation. The two may be chained but are not identical.

**Result: PASS.**

### PTR vs Managed Transition

Managed Transition is the broader working Pattern/Assembly grammar. PTR is a bounded Machine realization within that broader transition.

**Result: PASS.**

### PTR vs long-term monitoring

Monitoring may continue after the trial. PTR closes when the defined trial result is evaluated and dispositioned.

**Result: PASS.**

## 6. Machine / Assembly boundary

Working composition:

```text
CHANGE / NEED
      ↓
PPCR / DECISION
      ↓
PTR
      ↓
EVALUATION
      ↓
IMPLEMENT / RELEASE
      ↓
VERIFY
      ↓
CLOSE
```

The larger chain is an Assembly. PTR is one bounded Machine within it.

**Result: PASS.**

## 7. SOP anti-duplication

The Passport deliberately does not specify exact trial duration, sample size, operator motions, machine settings or local work-instruction wording.

**Result: PASS.**

## 8. Conclusion

Machine Passport v0.3 is now being used as a routine description instrument rather than as a schema under test.

**PTR Passport application: PASS.**

No schema modification indicated.

**Catalog / Canon / REG-001: NO CHANGE.**

Further work should proceed by passporting the next already-established Machine Candidate, not by redesigning the Passport schema.
