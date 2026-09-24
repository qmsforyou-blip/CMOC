# ARCHITECTURE LOOKUP CONTRACT — 001

Status: DESIGN / CONTRACT CANDIDATE
Version: 0.4
Date: 24-09-2026
Layer: CMOC / Superagent engineering process

## 1. Purpose

ARCHITECTURE LOOKUP resolves an already identified subject/capability.

It does not create, mutate, reconcile, canonize or approve CMOC objects.

Operation:
FIND -> RESOLVE -> REPORT

## 2. Input

subject_key
repository_root

subject_key is an existing architectural subject such as P7, P9 or P10. The resolver must not invent a subject key from a missing artifact.

## 3. Output

ARCHITECTURE_LOOKUP_RESULT contains:
subject_key
repository_root
resolved_at
artifacts
implementation_realization
gaps
gap_details
summary

Artifacts are grouped by role:
contract[]
implementation[]
test[]
evidence[]

Each artifact contains:
path
role
status[]
observed_results[]
resolution_basis

## 4. Realization model

Implementation is not assumed to be one file per subject. The resolver reports one of three explicit realization modes:

- DIRECT — a directly identifiable executable implementation exists;
- COMPOSITE — the subject is explicitly realized by composition/integration of existing architectural components;
- GATE — the subject is explicitly a gate/readiness realization rather than a standalone executable capability.

The mode may be inferred only from explicit contract wording. Absence of an implementation file is not sufficient to infer COMPOSITE or GATE.

Only subject-owned contracts contribute to mode resolution. Recognized declarations are an explicit `Realization mode:` field, a readiness-gate title, or subject-led declarations of readiness/audit gate or composition of existing boundaries. A generic occurrence of `integration` or `gate` is insufficient. Consistent multiple contracts are allowed. Conflicting mode declarations return a null mode and AMBIGUOUS_CONTRACT; no contract returns a null mode and SCOPE_INSUFFICIENT. DIRECT remains the default obligation for an owned contract without a recognized non-direct declaration, and does not itself prove that an implementation exists.

## 5. Resolution roles

CONTRACT: boundary, contract, standard, profile, review or gate defining the declared responsibility.

IMPLEMENTATION: executable realization of the capability.

TEST: executable verification artifact.

EVIDENCE: evidence, accepted review or readiness result recording an observed result.

A subject may legitimately have multiple artifacts in any role.

## 6. Status

Status is reported per artifact only from explicit lifecycle status fields such as `Status:` or `Evidence status:`.

Body mentions of status words do not establish artifact status.

Gate/result states such as `READY_WITH_LIMITATIONS` are reported separately as observed results.

The resolver must not invent a status.

Complete field values are preserved in uppercase, with Markdown emphasis and a terminal period removed. In particular, TESTED / NOT ACCEPTED must not also produce ACCEPTED. Distinct lifecycle values within one artifact produce AMBIGUOUS_STATUS and path-specific gap_details; statuses of separate artifacts are not merged. Executable metadata is read only from its module docstring, never from code annotations or string fixtures.

Observed results require a Result, Observed result, Gate result, or Status field whose whole value is a recognized result state. A fenced output block is eligible only in a Result / Gate result / Observed result / Actual result section (optionally numbered). Other fenced examples and unlabelled state lists are ignored. Multiple distinct results in one artifact produce AMBIGUOUS_OBSERVED_RESULT; no chronological winner is inferred.

Canonical lookup status classes:
ACCEPTED
IMPLEMENTATION PROVEN
DESIGN / ARCHITECTURE CANDIDATE
TESTED / NOT ACCEPTED
PARTIAL / LIMITED
MISSING
NOT_REQUIRED

Gate/result states such as READY_WITH_LIMITATIONS are observed results, not replacements for lifecycle status.

## 7. Subject scope

Subject ownership is resolved in this order:

1. filename begins with the exact subject key, optionally after a test/test_runtime or evidence/evidence-runtime role prefix;
2. a Python module docstring's opening subject declaration (or first leading comment when no docstring exists) — allowed for executable artifacts whose filename does not carry the subject key;
3. ordinary body mention — not sufficient for subject ownership.

The resolver must not treat a document as belonging to a subject merely because it mentions that subject somewhere in the body.

Subject matching must also distinguish a subject such as `P9` from a different subject such as `P9.1`.

POST-P10 reviews and PROD-001 boundaries are not owned P10/P7/P9 contracts. Their mentions do not establish ownership. This bounded resolver reports owned artifacts only; it does not claim to enumerate all related documents or follow arbitrary references. It does not pick a primary contract by filename ranking or silently discard other owned contracts.

## 8. Gaps

Only observable lookup gaps are reported:
MISSING_CONTRACT
MISSING_IMPLEMENTATION
MISSING_TEST
MISSING_EVIDENCE
AMBIGUOUS_CONTRACT
AMBIGUOUS_STATUS
AMBIGUOUS_OBSERVED_RESULT
SCOPE_INSUFFICIENT

An empty gap list means no gap under these bounded lookup rules; it does not prove operational readiness or acceptance of the entire capability. Component-level proof of a COMPOSITE realization remains outside this resolver's scope.

The resolver must not convert NO_MATCH into a semantic NEW decision.

## 9. Determinism

For the same repository state and input, lookup must produce the same artifact set and ordering. Artifacts are ordered by normalized repository path.

## 10. Read-only boundary

Architecture Lookup may read repository files and inspect explicit metadata/status text. It must not modify CMOC, OBJECT INDEX or source evidence; create decisions; perform reconciliation; or perform canonization.

## 11. Acceptance

The first implementation is accepted only after an executable test demonstrates deterministic read-only resolution for P7, P9 and P10, including DIRECT, COMPOSITE and GATE realization handling and explicit missing-role reporting.
