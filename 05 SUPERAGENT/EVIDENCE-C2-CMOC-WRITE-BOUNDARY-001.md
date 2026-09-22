# EVIDENCE-C2-CMOC-WRITE-BOUNDARY-001

**Status:** ACCEPTED  
**Contract:** `05 SUPERAGENT/C2-CMOC-WRITE-BOUNDARY-001.md`  
**Test:** `05 SUPERAGENT/test_c2_cmoc_write_boundary.py`  
**Scope:** synthetic / isolated boundary test; no production persistence engine.

## 1. Test gate

Command executed:

```powershell
py "05 SUPERAGENT\test_c2_cmoc_write_boundary.py"
```

Result:

```json
{
  "gate": "C2-CMOC-WRITE-BOUNDARY",
  "status": "PASS"
}
```

## 2. Accepted write

**C2-01_VALID_READY**

`CANONICALIZATION_READY` was accepted.

Observed:
- status: `CMOC_WRITE_ACCEPTED`
- object_id: `OBJ-C2-001`
- post_write_verified: `true`
- input_unchanged: `true`

This confirms that C2 can persist an already canonically prepared representation without modifying the received input.

## 3. Entry and provenance gates

The following invalid inputs were rejected:

| Case | Result | Basis |
|---|---|---|
| C2-02 non-ready | CMOC_WRITE_REJECTED | entry status is not CANONICALIZATION_READY |
| C2-03 missing provenance | CMOC_WRITE_REJECTED | missing provenance |
| C2-04 missing traceability | CMOC_WRITE_REJECTED | missing traceability |
| C2-05 missing object identity | CMOC_WRITE_REJECTED | missing canonical identity |
| C2-06 integrity failure | CMOC_WRITE_REJECTED | approved candidate integrity hash mismatch |

Therefore C2 does not accept an unprepared, untraceable, or integrity-invalid representation.

## 4. Mutation and relation controls

The following unauthorized operations were rejected:

- C2-07 unauthorized existing-object mutation → `CMOC_WRITE_REJECTED`
- C2-08 unsupported relation creation → `CMOC_WRITE_REJECTED`

Observed global controls:

```json
{
  "semantic_comparison_performed": false,
  "new_decision_performed": false,
  "relations_created_by_writer": false,
  "existing_object_mutation_allowed": false,
  "object_index_rebuilt": false
}
```

This confirms that C2 did not absorb semantic comparison, NEW decision, relation creation, existing-object mutation, or OBJECT INDEX rebuilding.

## 5. Idempotence and identity conflict

**C2-09_IDEMPOTENT_REPEAT**

The same canonical representation was written twice.

First:
- `CMOC_WRITE_ACCEPTED`
- post-write verification: `true`

Second:
- `ALREADY_PERSISTED`
- same object identity
- `idempotent: true`

**C2-10_SAME_ID_DIFFERENT_REPRESENTATION**

A different representation under the same object identity was rejected:

`CMOC_WRITE_REJECTED` with basis `EXISTING_OBJECT_WRITE_CONFLICT`.

C2 therefore does not silently overwrite an existing canonical representation.

## 6. Architectural controls

The test confirms:

- production runtime was not imported;
- persistence used only a synthetic in-memory stub;
- semantic comparison was not performed;
- NEW decision was not performed;
- relations were not created by the writer;
- existing-object mutation was not allowed;
- OBJECT INDEX was not rebuilt;
- input was preserved on write.

## 7. Boundary conclusion

C2 is validated as a **persistence boundary**, not as a semantic decision machine.

The tested architectural chain is:

```
R10 NEW_APPROVED
        ↓
C1 CANONIZATION
        ↓
CANONICALIZATION_READY
        ↓
C2 CMOC WRITE
        ↓
CMOC_WRITE_ACCEPTED
```

The evidence supports the invariant:

> **CMOC WRITE persists an already approved and canonically prepared representation; it does not decide what that representation means.**

C2 remains synthetic/isolated. This evidence does not establish a production CMOC persistence engine or production semantic novelty/canonization behavior.
