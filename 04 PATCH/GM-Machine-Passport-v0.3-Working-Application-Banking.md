# GM Machine Passport v0.3 — Working Application: Banking Process

**Notice:** 0165+170926  
**Date:** 17-09-2026  
**Status:** PASS / WORKING APPLICATION / NON-CANON

## 1. Purpose

Apply the frozen working Machine Passport v0.3 to the GM-096 **Banking Process** without reopening Passport schema design.

The objective is to demonstrate that Banking can be described as a bounded Machine whose identity is a controlled handling mode for material outside the normal flow, while keeping disposition and downstream ownership explicit.

## 2. Boundary proof

### Identity-bearing relation / mode

`OUT-OF-NORMAL-FLOW MATERIAL → CONTROLLED BANKING STATE → IDENTIFICATION / SEGREGATION / STATUS CONTROL → AUTHORIZED DISPOSITION / RELEASE`

The identity-bearing feature is the controlled banking state and its maintained traceability/status until authorized disposition or release.

### Own execution boundary

`IDENTIFY MATERIAL OUTSIDE NORMAL FLOW → PLACE UNDER CONTROL → IDENTIFY / SEGREGATE / STATUS → MAINTAIN CONTROL → AUTHORIZE / EXECUTE DEFINED DISPOSITION OR RELEASE → CLOSE`

### Local capability

Prevent unintended use or uncontrolled movement of material outside the normal process flow while preserving identification, status and traceability until authorized disposition or release.

### Closure condition

The banked material receives an authorized terminal disposition/release, or is explicitly transferred to an owned downstream process with status and traceability preserved.

**Boundary result: PASS.**

## 3. Full v0.3 Passport

```yaml
machine_passport:
  identity:
    name: Banking Process
    identity_bearing_relation_or_mode: "OUT-OF-NORMAL-FLOW MATERIAL → CONTROLLED BANKING STATE → IDENTIFICATION / SEGREGATION / STATUS CONTROL → AUTHORIZED DISPOSITION / RELEASE"
    local_capability: "Prevent unintended use or uncontrolled movement of material outside normal flow while preserving identification, status and traceability until authorized disposition or release."

  execution:
    trigger: "Material is identified as outside normal process flow and requires controlled holding pending disposition or release."
    inputs_context:
      - affected material / product
      - identification and traceability information
      - reason for banking
      - applicable status / disposition information
      - responsible authority / downstream process
    preconditions:
      - material can be identified and traced
      - controlled banking location/state exists
      - status can be made visible and maintained
      - disposition/release authority is defined
    execution_boundary: "IDENTIFY MATERIAL OUTSIDE NORMAL FLOW → PLACE UNDER CONTROL → IDENTIFY / SEGREGATE / STATUS → MAINTAIN CONTROL → AUTHORIZE / EXECUTE DEFINED DISPOSITION OR RELEASE → CLOSE"
    execution_sequence:
      - identify material requiring banking
      - establish controlled banking status
      - identify and segregate material as required
      - maintain traceability and visible status
      - determine authorized disposition or release path
      - execute or transfer the authorized disposition/release
      - confirm terminal status and close banking case
    evidence:
      - material identification
      - banking status / label / visual status
      - segregation or controlled-location evidence
      - traceability record
      - disposition / release authorization
      - terminal disposition or release evidence
    decision_points_logic:
      - material requires banking?
      - identification and traceability sufficient?
      - material remains under controlled status?
      - authorized disposition/release available?
      - downstream transfer required?
      - terminal status confirmed?
    local_outputs:
      - controlled banked material state
      - maintained identification/status
      - authorized disposition/release result
      - traceable handoff where downstream ownership applies
    closure_condition:
      type: disposition + handoff
      condition: "Authorized terminal disposition/release completed, or material transferred to downstream ownership with status and traceability preserved."
      evidence: "Disposition/release record or controlled downstream handoff."
      downstream_continuation: allowed

  realization:
    domain: "Production / quality control of material outside normal process flow"
    internal_mechanisms:
      - identification
      - segregation / controlled location
      - status control
      - traceability maintenance
      - disposition / release control
    roles:
      - responsible process personnel
      - quality / authorized disposition authority
      - downstream owner where material is transferred
    artifacts:
      - material identification / label
      - banking status record
      - traceability record
      - disposition / release record
    domain_specific_conditions:
      - material must remain identifiable
      - banking status must remain controlled and visible
      - unintended use must be prevented
    limitations:
      - does not itself define the enterprise authorization hierarchy
      - does not replace formal nonconforming-product disposition rules where separately applicable
      - does not own downstream rework, repair, change or release processes unless explicitly assigned
    downstream_ownership: "Authorized disposition/release owner and downstream process owner after controlled transfer."

  relations:
    pattern: "Managed Transition / Response to Abnormality relations may apply contextually; no Pattern canonization implied."
    invokes_uses:
      - identification / labeling mechanisms
      - segregation / controlled-location mechanisms
      - disposition / release authority
      - traceability records
    feeds:
      - disposition / rework / repair mechanisms
      - release to normal flow
      - downstream corrective or change mechanisms where applicable

  validation:
    machine_boundary_test:
      identity_bearing_relation_or_mode: PASS
      own_execution_boundary: PASS
      local_capability: PASS
      closure_condition: PASS
      result: PASS

  provenance:
    source: "GM Quality System Basics Overview Supplier Audit — GM-096 Managing Change, Banking Process"
    evidence_reference: "GM-096 extraction and prior Banking Process passport trial"
    status: "MACHINE CANDIDATE / NON-CANON"
```

## 4. Field-by-field result

| Layer | Result | Observation |
|---|---|---|
| Identity | PASS | Banking identity is controlled handling of out-of-normal-flow material, not merely storage. |
| Execution | PASS | Bounded control state, maintenance, disposition/release and closure are representable. |
| Realization | PASS | Identification, segregation, status and traceability remain implementation mechanisms. |
| Relations | PASS | Downstream disposition/release relations do not redefine identity. |
| Validation | PASS | Boundary proof is explicit and separate from descriptive identity. |
| Provenance | PASS | GM-096 source and prior extraction remain traceable. |

## 5. Boundary tests

### 5.1 Banking vs Storage

Generic storage is insufficient: it does not necessarily maintain controlled status, traceability, prevention of unintended use, or authorized disposition/release.

**PASS.**

### 5.2 Banking vs Control of Nonconforming Product

Banking can realize part of nonconforming-product control, but the Machine identity is the controlled banking state for material outside normal flow. Broader nonconforming-product control may include additional containment, communication and disposition architecture.

**PASS WITH QUALIFICATION.**

### 5.3 Banking vs Bypass

Banking holds material outside normal flow; Bypass provides a controlled temporary alternative when the normal process is unavailable. Their identity-bearing modes differ.

**PASS.**

### 5.4 Banking vs Assembly

A wider architecture may chain detection → banking → disposition → verification → release. Banking remains the bounded controlled-state execution within that architecture.

**PASS.**

## 6. SOP anti-duplication

The Passport does not prescribe exact storage locations, label formats, handling motions, approval signatures, timing or local work instructions.

**PASS.**

## 7. Application conclusion

Banking Process is successfully represented by Machine Passport v0.3 without schema modification.

The trial adds a third distinct Machine identity type to the working set:

- Gemba Walk — mode of access to reality;
- PTR — controlled trial/evaluation execution;
- Banking — controlled state/handling mode.

This strengthens the working claim that Machine identity is not tied to one universal process shape.

## 8. Qualification

The relationship between Banking and broader Control of Nonconforming Product remains context-dependent. This is a classification/composition question and does not require a Passport schema change.

## 9. Catalog / Canon / REG-001 impact

- Catalog: **NO CHANGE**
- Canon: **NO CHANGE**
- REG-001: **NO CHANGE**
- Passport v0.3: **NO CHANGE**

## 10. Final result

**PASS WITH QUALIFICATION.**

The qualification concerns the Machine/Assembly or domain-boundary relationship with broader nonconforming-product control, not the Passport schema.

**Step closed.**
