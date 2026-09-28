# PILOT-003 — review of controlled M07 relations

**Date:** 28-09-2026  
**Status:** HUMAN REVIEW CANDIDATE; no admission  
**Source:** Imai, *Gemba Kaizen*, chapter 13, page 6 of the supplied chapter extract  
**RUN:** `RUN-PILOT-003-SRC-005` (persisted M06 passports)

## Architecture lookup

- M07 already accepts explicit source-bound relation evidence and returns provisional candidates (`m07_llm.py`, accepted controlled SRC-002 evidence).
- M08 already handles provisional decisions and the no-evidence branch. Neither M07 nor M08 authorizes semantic NEW or CMOC write.
- `PATCH-IMA-013-CEO-KAIZEN-v1.md`, §013.3 already describes the whole `Value Stream Performance Review` as a single-source candidate, with no Core or LAB-002 promotion.
- The missing production capability is a stable RUN-bound evidence mapping after M06. Matching on regenerated passport names failed in RUN-004.

## Source check

The supplied page describes six product-family value streams, each assigned a manager. Byrne's team met those managers weekly. In those meetings they reported progress using five groups of indicators and focused on current problems. The controlled public fragment is a paraphrase of that passage.

## Diagnostic M07 output (not persisted as a RUN result)

| Candidate | Source support | Review |
| --- | --- | --- |
| REL-001 PAS-001 → PAS-002, `ROLE_PARTICIPATES_IN_ACTIVITY` | Manager and meeting are linked in the passage. | **Type unresolved:** PAS-001 is `STRUCTURAL_DISTINCTION` (“one manager per stream”), not a role passport. Do not approve this type. |
| REL-002 PAS-003 → PAS-002, `ACTIVITY_OCCURS_WITHIN_ACTIVITY` | Managers report five groups of measures in the meetings. | Provisional source support; confirm the activity boundary in human review. |
| REL-003 PAS-004 → PAS-002, `ACTIVITY_OCCURS_WITHIN_ACTIVITY` | The meetings focus on current tasks/problems. | Provisional source support; confirm the activity boundary in human review. |

The four passports are components of the earlier whole-construction candidate. No M06 passport of that whole was produced. The M07 relations do not create such a passport or prove that it is a NEW CMOC object. Existing four `DEFER` human decisions remain authoritative.

## Controlled continuation

`PILOT-003-SRC-005-RELATION-BINDING.json` pins the source package, evidence package, RUN ID, exact set of passport IDs, working classes, formulation basis refs, and three human-selected evidence endpoint pairs. `pilot_003_relation_probe.py` reads the existing SQLite Discovery result and invokes only M07. It ignores generated passport names when binding evidence, rejects drift in RUN/source/passport lineage, and writes no result to the RUN, CMOC, or index. The full-run CLI rejects packages with relation evidence before any LLM call; those packages require a persisted-RUN continuation.

**Proven:** source-bound M07 can propose three relations on persisted passports; the mapping can be checked without repeating M01–M06.  
**Not proven:** an accepted relation type for all three, M08 on these relations, whole-construction passport, semantic NEW, Admission, C1/C2/C3, or CMOC/index write.
