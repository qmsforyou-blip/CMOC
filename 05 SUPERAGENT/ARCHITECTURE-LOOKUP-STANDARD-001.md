# ARCHITECTURE LOOKUP STANDARD — 001

**Status:** ACCEPTED  
**Date:** 24-09-2026  
**Layer:** CMOC / Superagent engineering process  
**Purpose:** prevent duplicate architecture work by establishing a mandatory lookup before creating a new boundary, machine, contract, implementation or gate.

---

## 1. Rule

Before creating new architecture, first determine whether the required capability already exists in the repository.

```
ARCHITECTURE LOOKUP
        ↓
CONTRACT
        ↓
IMPLEMENTATION
        ↓
TEST
        ↓
EVIDENCE
        ↓
STATUS
        ↓
ONLY THEN — NEW WORK
```

A new artifact must not be created merely because its name, number or expected phase appears to be missing.

---

## 2. Mandatory lookup questions

For every proposed new architectural step, answer:

1. What already exists?
2. Where does it live?
3. What contract defines it?
4. What implementation realizes it?
5. What test exercises it?
6. What evidence records the result?
7. What is its current status?
8. What scope and limitations apply?
9. Is the required capability already satisfied?
10. If not, what exact gap remains?

The lookup must distinguish absence of a named artifact from absence of the underlying capability.

---

## 3. Required status classification

Every lookup result should be classified as one of:

- **ACCEPTED** — contract/evidence establishes the boundary sufficiently for the declared scope.
- **IMPLEMENTATION PROVEN** — executable implementation is demonstrated, with explicit scope.
- **DESIGN / ARCHITECTURE CANDIDATE** — boundary exists conceptually but is not yet accepted.
- **TESTED / NOT ACCEPTED** — executable test exists but acceptance is incomplete.
- **PARTIAL / LIMITED** — capability exists with declared limitations.
- **MISSING** — no relevant artifact or implementation found.
- **NOT_REQUIRED** — capability is explicitly outside the declared deployment/profile scope.

Do not infer ACCEPTED from a filename, numbering sequence, or existence of code alone.

---

## 4. Evidence chain

Minimum traceability:

```
CONTRACT
  ↓
IMPLEMENTATION
  ↓
TEST
  ↓
EVIDENCE
  ↓
ACCEPTANCE STATUS
```

For runtime/production work:

```
DEPLOYMENT PROFILE
  ↓
REQUIRED CAPABILITY
  ↓
EXISTING CONTRACT
  ↓
EXISTING EVIDENCE
  ↓
ACTUAL GAP
```

This prevents infrastructure limitations from being mistaken for missing CMOC semantics.

---

## 5. Search scope

The lookup covers, at minimum:

### Architecture / contracts
Boundary documents, architecture reviews, standards, profiles, contracts and gates.

### Implementation
Runtime modules, builders, adapters, stores, synchronizers, orchestration and recovery components.

### Verification
Unit, integration, E2E, compatibility and production/runtime tests.

### Evidence
EVIDENCE-* artifacts, accepted reviews and readiness gates.

### Existing operational plans
Before inventing a new operational layer, inspect existing O0-O9 and production-profile material.

---

## 6. Search by capability, not only by proposed name

Search using the underlying capability and observable effects.

For example, for "durable P1-P8 E2E with restart/recovery", search not only that phrase but also:

- RUN_COMPLETED;
- restart;
- recovery;
- retry;
- attempt;
- durable journal;
- runtime state;
- P7;
- P8;
- production E2E;
- P9;
- evidence.

The 24-09-2026 P9 review is the reference case: the requested capability already existed in `test_runtime_p9_production_e2e_recovery.py` with accepted P9 evidence.

---

## 7. Do not duplicate an existing capability

If lookup finds an existing implementation satisfying the requested capability:

1. inspect it;
2. verify its evidence;
3. identify the exact remaining gap, if any;
4. strengthen existing evidence or implementation only where necessary;
5. update status if evidence supports acceptance.

Do not create a second implementation, duplicate test, parallel boundary, or numbering-only artifact.

---

## 8. Distinguish three gaps

### Gap A — missing capability
Nothing adequate exists.

→ New implementation may be required.

### Gap B — existing capability, insufficient evidence
Implementation exists but is not adequately tested/evidenced.

→ Strengthen test/evidence; do not create a duplicate machine.

### Gap C — existing capability, different declared scope
Capability exists but does not cover the required deployment/profile boundary.

→ Extend existing implementation or document the explicit scope gap.

These cases must not be collapsed into "missing architecture".

---

## 9. New boundary decision rule

A new architectural boundary is justified only when:

1. the requested responsibility is materially distinct;
2. existing boundaries cannot express it without responsibility leakage;
3. the deployment/profile requirement is explicit;
4. lookup has been performed;
5. the exact gap is documented;
6. the new boundary does not duplicate an existing capability.

Default:

> **New engineering requirement → implement against existing contract → test → evidence.**

Only when the existing architecture cannot safely contain the responsibility:

> **Documented responsibility gap → new boundary candidate.**

---

## 10. Acceptance rule

The next action depends on lookup status:

| Lookup result | Default action |
|---|---|
| ACCEPTED | Reuse |
| IMPLEMENTATION PROVEN | Reuse / strengthen evidence if needed |
| DESIGN / CANDIDATE | Inspect and continue existing work |
| TESTED / NOT ACCEPTED | Fix/complete existing gate |
| PARTIAL / LIMITED | Identify exact scope gap |
| MISSING | Design new capability |
| NOT_REQUIRED | Do not implement |

---

## 11. Mandatory lookup record

For every substantial new work item, record:

```
PROPOSED CAPABILITY:
WHY NEEDED:

EXISTING CONTRACT:
EXISTING IMPLEMENTATION:
EXISTING TEST:
EXISTING EVIDENCE:
CURRENT STATUS:

EXACT GAP:
SCOPE / LIMITATIONS:

DECISION:
REUSE / EXTEND / NEW
```

For a major architectural decision, persist the lookup as a repository artifact.

---

## 12. Relationship to POST-P10 architecture review

This standard operationalizes the rule established by `POST-P10-ARCHITECTURE-REVIEW-001.md`:

> Do not automatically create another architecture gate. First identify the concrete capability required by the declared deployment profile and determine whether the existing architecture already supports it.

This is a process control for architecture work, not a new CMOC semantic layer.

---

## 13. Non-goals

This standard does not:

- create semantic objects;
- redefine R1-R10;
- redefine C1-C3;
- change RUN/ORCH/REC;
- create operational authority;
- replace existing evidence;
- turn repository search into semantic decision-making.

It controls the engineering process used to extend the existing system.

---

## 14. Canonical short form

Before every substantial CMOC/Superagent engineering step:

```
LOOK FIRST.
FIND CONTRACT.
FIND IMPLEMENTATION.
FIND TEST.
FIND EVIDENCE.
CHECK STATUS.
IDENTIFY THE ACTUAL GAP.
ONLY THEN BUILD.
```

---

## 15. Status

**ARCHITECTURE LOOKUP STANDARD — ACCEPTED**

This standard is part of the engineering process for the CMOC/Superagent repository.
