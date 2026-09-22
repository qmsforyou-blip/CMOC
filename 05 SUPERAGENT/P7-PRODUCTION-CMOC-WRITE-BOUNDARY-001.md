# P7 — PRODUCTION CMOC WRITE BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE

## 1. Purpose

P7 defines the first production persistence boundary for writing an already approved and canonically prepared representation into the real CMOC repository.

P7 is not a semantic stage.

The semantic decision has already occurred upstream:

`NEW_APPROVED → C1 CANONICALIZATION_READY → P7/C2 CMOC WRITE`

P7 must persist what was approved and canonically prepared. It must not decide what it means.

## 2. Production boundary

The production chain is:

`NEW_APPROVED`
→ `CANONICALIZATION_READY`
→ `P7 PRODUCTION CMOC WRITE`
→ `CMOC_WRITE_ACCEPTED`
→ `P8 OBJECT INDEX SYNCHRONIZATION`

P7 is the concrete production realization of the C2 persistence boundary.

## 3. Required input

Minimum input:

- RUN_ID
- SOURCE_ID
- BATCH_ID
- STAGE_ID
- ATTEMPT_ID
- RESULT_ID
- canonical object_id
- object_type
- canonical_name / canonical representation
- object boundary
- provenance
- traceability
- NEW evidence reference
- approved-candidate integrity anchor
- canonicalization result status = `CANONICALIZATION_READY`

The production writer must reject incomplete input.

## 4. Write rule

Default operation:

`CREATE canonical object`

P7 must not silently update an existing object.

If the same canonical identity already exists:

- identical representation → idempotent `ALREADY_PERSISTED`;
- different representation → `EXISTING_OBJECT_WRITE_CONFLICT`.

P7 does not resolve the conflict semantically.

## 5. Integrity and idempotency

P7 must preserve the approved-candidate integrity anchor established by C1.

The writer must verify that the received canonicalization package has not been changed after approval.

Repeated execution of the same:

`RUN_ID + STAGE_ID + ATTEMPT_ID + IDEMPOTENCY_KEY`

must not create a second authoritative CMOC representation.

P3/P5 remain the execution-safety boundaries.

## 6. Transaction boundary

The production writer must have an explicit commit point.

Before commit:

- no authoritative CMOC write is reported;
- failure remains recoverable;
- partial/incomplete representation must not be reported as accepted.

After commit:

- the representation is authoritative;
- subsequent duplicate invocation returns an idempotent result;
- the original write identity remains traceable.

## 7. Existing object behavior

P7 distinguishes persistence identity from semantic identity.

If an existing object has the same canonical identity and same representation:

`ALREADY_PERSISTED`

If the same identity contains a different representation:

`EXISTING_OBJECT_WRITE_CONFLICT`

P7 must not:

- merge;
- overwrite;
- choose a winner;
- reinterpret the semantic boundary;
- create a hidden NEW decision.

## 8. Physical CMOC representation

P7 must write the canonical representation using the repository's actual CMOC representation format.

The production test must verify:

1. file/object is physically persisted;
2. object identity is preserved;
3. canonical representation is preserved;
4. provenance is preserved;
5. traceability is preserved;
6. integrity anchor is preserved;
7. no unsupported relations are introduced.

## 9. Repository safety

P7 must write only to the contracted CMOC target.

It must not modify:

- unrelated CMOC objects;
- OBJECT INDEX directly;
- semantic evidence;
- source files;
- R1-R10 results.

OBJECT INDEX synchronization remains P8/C3.

## 10. Failure boundary

Candidate production statuses:

- `CMOC_WRITE_ACCEPTED`
- `ALREADY_PERSISTED`
- `CMOC_WRITE_REJECTED`
- `EXISTING_OBJECT_WRITE_CONFLICT`
- `INTEGRITY_FAILURE`
- `POST_WRITE_VERIFICATION_FAILED`
- `CMOC_TARGET_UNAVAILABLE`

No failure status may be converted into semantic approval.

## 11. Post-write verification

A successful physical write is not complete until the persisted representation is read back and verified against the canonicalization package.

Minimum verification:

`written representation == canonical representation`

plus identity, provenance, traceability, and integrity anchor.

If verification fails:

`POST_WRITE_VERIFICATION_FAILED`

The writer must not report `CMOC_WRITE_ACCEPTED`.

## 12. Responsibility boundary

P7 must NOT:

- perform NEW decision;
- perform semantic comparison;
- decide equivalence;
- resolve conflict;
- perform canonization;
- create unsupported relations;
- mutate OBJECT INDEX;
- modify source evidence;
- repair semantic content.

P7 is persistence only.

## 13. First production gate

Unlike P1-P6 synthetic gates, the P7 gate must use the actual local CMOC repository as the persistence target.

The test must use a dedicated isolated test object/fixture and must not modify unrelated production objects.

The first P7 gate therefore establishes:

**real CMOC persistence + integrity + idempotency + read-back verification + repository isolation.**

It does not yet establish full production throughput or distributed deployment.

## 14. Test safety

The P7 test must:

- use a uniquely identified test object;
- avoid overwriting existing CMOC objects;
- preserve the original repository state outside the test target;
- verify cleanup or explicitly document the retained test fixture;
- prove that OBJECT INDEX is not directly mutated by P7.
