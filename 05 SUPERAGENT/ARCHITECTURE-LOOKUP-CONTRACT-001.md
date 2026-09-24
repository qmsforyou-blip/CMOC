# ARCHITECTURE LOOKUP CONTRACT — 001

Status: DESIGN / CONTRACT CANDIDATE
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
status_observations
gaps
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
resolution_basis

## 4. Resolution roles

CONTRACT: boundary, contract, standard, profile, review or gate defining the declared responsibility.

IMPLEMENTATION: executable realization of the capability.

TEST: executable verification artifact.

EVIDENCE: evidence, accepted review or readiness result recording an observed result.

A subject may legitimately have multiple artifacts in any role.

## 5. Status

Status is reported per artifact from explicit repository content where available.

The resolver must not invent a status.

Canonical lookup status classes:
ACCEPTED
IMPLEMENTATION PROVEN
DESIGN / ARCHITECTURE CANDIDATE
TESTED / NOT ACCEPTED
PARTIAL / LIMITED
MISSING
NOT_REQUIRED

Gate/result states such as READY_WITH_LIMITATIONS are observed results, not replacements for lifecycle status.

## 6. Gaps

Only observable lookup gaps are reported:
MISSING_CONTRACT
MISSING_IMPLEMENTATION
MISSING_TEST
MISSING_EVIDENCE
AMBIGUOUS_CONTRACT

The resolver must not convert NO_MATCH into a semantic NEW decision.

## 7. Determinism

For the same repository state and input, lookup must produce the same artifact set and ordering. Artifacts are ordered by normalized repository path.

## 8. Read-only boundary

Architecture Lookup may read repository files and inspect explicit metadata/status text. It must not modify CMOC, OBJECT INDEX or source evidence; create decisions; perform reconciliation; or perform canonization.

## 9. Acceptance

The first implementation is accepted only after an executable test demonstrates deterministic read-only resolution for P7, P9 and P10, including positive resolution and explicit missing-role reporting.
