# C2 — CMOC WRITE BOUNDARY

**ID:** C2-CMOC-WRITE-BOUNDARY-001  
**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Stage:** C2  
**Predecessor:** C1-CANONIZATION-BOUNDARY-001  
**Input:** `CANONICALIZATION_READY`  
**Output:** `CMOC_WRITE_ACCEPTED` / `CMOC_WRITE_REJECTED`

---

## 1. Purpose

C2 defines the boundary between a prepared canonical representation and persistence into CMOC.

The controlled transition is:

```
R10
NEW_APPROVED
    ↓
C1
CANONIZATION
    ↓
CANONICALIZATION_READY
    ↓
C2
CMOC WRITE
    ↓
CMOC PERSISTED
```

C2 is a persistence boundary.

It does **not** become a new semantic decision stage.

---

## 2. Fundamental Separation

The following boundaries remain distinct:

```
NEW DECISION
    ≠
CANONIZATION
    ≠
CMOC WRITE
```

Therefore C2 MUST NOT:

- re-decide NEW;
- perform semantic comparison;
- decide semantic equivalence;
- decide conflict;
- discover or infer relations;
- change the approved semantic boundary;
- enrich the representation with hidden meaning;
- silently merge with an existing object;
- canonize a rejected or unapproved candidate.

C2 persists what C1 has prepared and accepted for persistence.

---

## 3. Entry Condition

The only normal entry state is:

```
status = CANONICALIZATION_READY
```

The incoming record MUST carry the canonicalization result produced by C1.

At minimum the write package MUST preserve:

- canonical object identity;
- canonical object type;
- canonical name / representation;
- object boundary;
- provenance;
- traceability;
- NEW decision evidence reference;
- approved-candidate integrity anchor;
- canonicalization result status.

C2 MUST NOT infer missing semantic fields.

Missing required data is a write rejection, not an invitation to enrich.

---

## 4. Pre-Write Gate

Before persistence C2 MUST verify:

### C2-P01 — Status

```
CANONICALIZATION_READY
```

Anything else:

```
CMOC_WRITE_REJECTED
```

### C2-P02 — Provenance

Provenance is present and traceable.

Missing provenance:

```
CMOC_WRITE_REJECTED
```

### C2-P03 — Traceability

The canonical representation retains traceability to its source and approved candidate.

Missing traceability:

```
CMOC_WRITE_REJECTED
```

### C2-P04 — Object Identity

A canonical object identity is present.

C2 MUST NOT manufacture a new identity as a substitute for a missing C1 result.

### C2-P05 — Integrity

The approved-candidate integrity anchor is present and remains consistent with the canonicalization input contract.

Integrity failure:

```
CMOC_WRITE_REJECTED
```

The integrity check is an identity/control check.

It is not a semantic comparison.

### C2-P06 — No Hidden Mutation

The write package MUST NOT contain an instruction to modify an existing CMOC object unless such mutation is explicitly part of a separate authorized contract.

Default C2 behavior:

```
NEW CANONICAL OBJECT WRITE
```

not:

```
UPDATE EXISTING OBJECT
```

### C2-P07 — No Unsupported Relations

C2 MUST NOT create relations merely because a relation would appear useful.

Relations require their own controlled evidence/contract.

---

## 5. Write Semantics

C2 performs one operation:

```
PERSIST(CANONICALIZATION_READY)
```

The persistence operation MUST preserve the approved representation.

C2 MUST NOT transform the semantic content while writing.

Allowed technical transformations are limited to serialization/storage requirements and MUST NOT change the represented object.

---

## 6. Existing Object Protection

If the target canonical identity already exists, C2 MUST NOT silently overwrite it.

The default result is:

```
CMOC_WRITE_REJECTED
basis = EXISTING_OBJECT_WRITE_CONFLICT
```

Any merge, replacement, or update requires a separate explicit contract.

This prevents CMOC WRITE from becoming an implicit reconciliation or conflict-resolution machine.

---

## 7. Idempotency

A repeated write of the same canonicalization result MUST be distinguishable from a different representation.

C2 SHOULD use the canonical object identity together with the approved/incoming representation integrity anchor to detect an already-persisted identical result.

Expected states:

```
same identity + same approved representation
    → ALREADY_PERSISTED / idempotent success
```

versus:

```
same identity + different representation
    → CMOC_WRITE_REJECTED
```

C2 MUST NOT resolve the difference semantically.

The exact persistence mechanism for this check is implementation-specific and is not established by this contract.

---

## 8. Post-Write Verification

A successful persistence operation MUST have a verification step.

Minimum verification:

1. target object exists;
2. canonical identity is preserved;
3. canonical representation is preserved;
4. provenance is preserved;
5. traceability is preserved;
6. integrity anchor is preserved;
7. no unauthorized relation was created;
8. no unrelated existing object was mutated.

If verification fails:

```
CMOC_WRITE_REJECTED
basis = POST_WRITE_VERIFICATION_FAILED
```

The contract does not prescribe rollback mechanics yet.

---

## 9. Object Index Boundary

CMOC WRITE and OBJECT INDEX construction remain separate operations.

```
CMOC WRITE
    ↓
CMOC state changed
    ↓
OBJECT INDEX BUILD
```

C2 MUST NOT silently perform QUERY or semantic indexing as part of the write decision.

Whether index rebuilding is triggered automatically after a successful write is a separate orchestration question and is NOT decided by this C2 contract.

---

## 10. Failure States

At minimum C2 recognizes:

- `NOT_ELIGIBLE`
- `CMOC_WRITE_REJECTED`
- `EXISTING_OBJECT_WRITE_CONFLICT`
- `INTEGRITY_FAILURE`
- `POST_WRITE_VERIFICATION_FAILED`

No failure state may be converted automatically into:

```
NEW
```

or:

```
EXISTING_EQUIVALENT
```

or:

```
CONFLICT_RESOLVED
```

Those decisions belong to other controlled boundaries.

---

## 11. LLM Boundary

LLM assistance MAY be used for representation formatting only if the resulting representation remains controlled by the canonicalization contract and integrity verification.

LLM MUST NOT:

- decide whether the object is new;
- decide semantic equivalence;
- invent missing provenance;
- invent traceability;
- invent relations;
- modify an existing object without explicit authorization;
- bypass the pre-write gate.

C2 is therefore not an LLM semantic decision boundary.

---

## 12. Synthetic MVP Scope

The first C2 test MUST be synthetic and isolated.

It MUST NOT:

- mutate production CMOC;
- depend on production semantic novelty;
- modify existing CMOC objects;
- require automatic object-index rebuild;
- assume a production persistence engine that has not yet been specified.

The first test establishes the **boundary contract**, not production persistence.

---

## 13. Definition of Done — Candidate

C2 is ready for test when the following are explicitly testable:

- [ ] CANONICALIZATION_READY accepted as entry state.
- [ ] non-ready state rejected.
- [ ] missing provenance rejected.
- [ ] missing traceability rejected.
- [ ] missing object identity rejected.
- [ ] integrity failure rejected.
- [ ] unauthorized existing-object mutation rejected.
- [ ] unsupported relation creation absent.
- [ ] same approved representation handled idempotently.
- [ ] different representation for same identity rejected without semantic re-decision.
- [ ] successful persistence preserves canonical representation.
- [ ] post-write verification is enforced.
- [ ] no NEW decision performed.
- [ ] no semantic comparison performed.
- [ ] no CMOC write performed by the isolated boundary test itself unless an explicit synthetic persistence stub is used.
- [ ] no production runtime dependency.

---

## 14. Architectural Invariant

The core invariant is:

> **CMOC WRITE persists an already approved and canonically prepared representation; it does not decide what that representation means.**

Therefore:

```
R10
NEW_APPROVED
    ↓
C1
CANONICALIZATION_READY
    ↓
C2
CMOC_WRITE
```

is a controlled one-way architectural chain.

**C2 remains a persistence boundary, not a hidden semantic decision machine.**
