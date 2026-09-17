# GM-096 — Managed Transition: Internal Grammar Cross-Check

**Date:** 17-09-2026  
**Notice:** 0140+170926  
**Status:** CROSS-CHECK COMPLETE / NON-CANON

## 1. Purpose

Проверить внутреннюю грамматику Pattern `Managed Transition` и определить,
какие уже выделенные CMOC Patterns / Mechanisms являются его составными
элементами, а какие не должны включаться в него как обязательные.

Цель — не создать новые сущности, а проверить архитектурную композицию уже
выделенной конструкции.

## 2. Working Pattern

```text
STATE A
  ↓
IDENTIFY
  ↓
ASSESS
  ↓
AUTHORIZE / DECIDE
  ↓
TRANSITION
  ↓
VERIFY
  ↓
ACCEPT / RETURN / ROLLBACK
  ↓
RECORD / CLOSE
```

## 3. Independent cross-check

Независимые материалы по change management и systems engineering воспроизводят
одни и те же функциональные узлы:

- identification / request;
- impact or risk assessment;
- authorization / decision;
- controlled implementation or transition;
- verification / readiness confirmation;
- rollback or return path;
- acceptance / closure and record.

ISO 41014 defines a `decision gate` as an activity that determines whether a
process continues, recycles or stops, and defines management of change as a
process that systematically recognizes and communicates changes that may affect
system integrity.

INCOSE systems engineering material connects decision gates with assessment,
verification/validation, readiness and authorization to proceed.

Current change-management implementations independently show the same gated
sequence: request → assessment → authorization → implementation → verification
→ rollback/close. These sources are treated as supporting evidence for the
functional grammar, not as proof that `Managed Transition` is an established
industry term.

## 4. Grammar decomposition

### 4.1 Decision Gate

**Role:** decision point inside Managed Transition.

Typical questions:

- continue or stop?
- trial required or not?
- return or adopt?
- additional verification required?

Classification:

`MECHANISM / PATTERN`

Existing CMOC candidate. Not a sub-pattern of Managed Transition in the sense
of identity; it is a reusable decision mechanism invoked by the Pattern.

### 4.2 Assessment against Criterion

**Role:** evidence-based comparison before or after a transition.

Typical questions:

- does the proposed state satisfy the applicable criteria?
- is readiness sufficient?
- did the transition produce the required result?

Classification:

`PATTERN`

Existing CMOC pattern. Managed Transition can invoke it before authorization and
again during verification.

### 4.3 Controlled Deviation

**Role:** mechanism for allowing a controlled departure from the normal state
or baseline.

It is not required for every Managed Transition. A transition may move from A
to B without being a deviation from an approved baseline.

Therefore:

`Controlled Deviation` is an optional specialized mechanism invoked by some
Managed Transitions, especially Bypass.

### 4.4 Verification

Verification is a required functional role in the generalized Pattern, but
`Verification` itself should remain a mechanism/family rather than become a
sub-pattern named by Managed Transition.

The verification may be:

- process verification;
- readiness verification;
- result verification;
- parameter/settings verification;
- validation of produced parts/results;
- acceptance evidence.

### 4.5 Response to Abnormality

Not intrinsic to Managed Transition.

It is invoked when the transition is triggered by an abnormal condition or when
verification detects an abnormal state requiring response.

Therefore:

`Response to Abnormality` = optional external/adjacent Pattern.

This preserves the distinction already established with Andon / Fast Response.

### 4.6 Record / Traceability

Recording is a persistent evidence mechanism of Managed Transition, but not the
transition itself.

It provides:

- identity of the change;
- decision history;
- authorization;
- evidence;
- resulting state;
- closure / return status.

## 5. Minimal grammar

The cross-check supports the following minimal form:

```text
MANAGED TRANSITION

1. IDENTIFY
2. ASSESS
3. DECIDE / AUTHORIZE
4. TRANSITION
5. VERIFY
6. ACCEPT / RETURN / ROLLBACK
7. RECORD / CLOSE
```

The following are **not mandatory universal steps**:

- trial;
- deviation;
- abnormality response;
- audit;
- problem solving;
- training;
- customer approval.

They are specialized mechanisms or requirements introduced by a particular
implementation.

## 6. GM-096 mapping

```text
Managed Transition
│
├── Identify / Assess
│      └── PPCR
│
├── Decide / Authorize
│      └── Decision Gate
│
├── Transition / Trial
│      └── PTR
│
├── Special Material State
│      └── Banking
│
├── Special Process State
│      └── Bypass
│             └── Controlled Deviation
│
├── Verify
│      ├── Control Means Verification
│      ├── LPA / Audit
│      └── Assessment against Criterion
│
└── Accept / Return / Close
```

This is an architectural interpretation of the source material, not a claim
that GM QSB presents this exact hierarchy.

## 7. Key boundary

The Pattern is not:

> `Decision Gate + Assessment + Verification + Controlled Deviation`

as a simple sum.

Its identity is the **managed movement between organizational/process states**.
The listed elements are reusable control functions that can be assembled inside
that movement.

Therefore the Pattern is a higher-order organizational construction:

```text
CONTROL FUNCTIONS
      ↓
managed through
      ↓
MANAGED TRANSITION
      ↓
from STATE A to STATE B
```

## 8. Architectural consequence

This explains why the GM-096 candidates remain separate Machines:

- PPCR governs the change-entry/control process;
- PTR specializes controlled trial;
- Banking specializes material state;
- Bypass specializes process state.

They are not four competing definitions of Managed Transition. They are
specialized realizations of the same higher-order transition grammar.

## 9. CMOC classification

`Managed Transition`

- **Kind:** PATTERN
- **Status:** STRONG PATTERN CANDIDATE / NON-CANON
- **Evidence:** MULTI-SOURCE CONFIRMED
- **Identity:** managed movement from one accepted state/baseline to another,
  with decision, authorization, controlled execution, verification and formal
  acceptance/return.
- **Mandatory internal functions:** identify, assess, decide/authorize,
  transition, verify, accept/return/rollback, record/close.
- **Optional specialized functions:** trial, deviation, abnormality response,
  audit, problem solving, training, customer approval.

## 10. Decision

The internal grammar is sufficiently stable to retain `Managed Transition` as
a Pattern candidate.

No new Pattern, Mechanism or Machine is created by this cross-check.

No REG-001 update.
No Canon update.
No Machine Catalog update.

## 11. Next check

If further testing is required, use a completely different class of source or
case and test whether the minimal grammar still reconstructs without GM/QSB
terminology.
