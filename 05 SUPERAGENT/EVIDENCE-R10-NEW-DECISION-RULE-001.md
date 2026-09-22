# EVIDENCE-R10 — NEW DECISION RULE

**Status:** ACCEPTED  
**Gate:** R10-NEW-DECISION-RULE  
**Date:** 22-09-2026

## 1. Result

The R10 executable synthetic boundary test returned:

`PASS`

All thirteen branches passed.

## 2. Verified decision branches

- COMPLETE_ELIGIBLE → `NEW_APPROVED`
- INELIGIBLE_INPUT → `NEW_REJECTED`
- NO_POSITIVE_DISTINCTION → `NEW_REJECTED`
- UNKNOWN_MANDATORY_EVIDENCE → `NEW_REJECTED`
- UNRESOLVED_CANDIDATE → `NEW_REJECTED`
- AMBIGUOUS_EVIDENCE → `NEW_REJECTED`
- UNKNOWN_TARGET_TYPE → `NEW_REJECTED`
- PARTIAL_COMPARISON → `NEW_REJECTED`
- MULTIPLE_POSITIVE_DISTINCTIONS → `NEW_APPROVED`

Additional controls:

- NEW_APPROVED → no object ID;
- NEW_APPROVED → no canonization;
- NEW_APPROVED → no CMOC WRITE;
- NEW_REJECTED → no CMOC WRITE.

## 3. Decision boundary

R10 establishes:

`ELIGIBLE_FOR_NEW_DECISION + explicit NEW rule → NEW_APPROVED / NEW_REJECTED`

The decision remains separate from:

- canonization;
- object identity creation;
- CMOC insertion;
- relation creation.

## 4. Conservative evidence rule

The tested rule rejects automatic approval when any mandatory condition is absent or unresolved, including:

- positive semantic distinction;
- resolved target object type;
- complete source evidence;
- complete traceability;
- unresolved candidate;
- ambiguity;
- COMPLETE comparison evidence;
- UNKNOWN mandatory evidence.

## 5. Multiple distinctions

Multiple positive distinctions may support NEW_APPROVED when all other mandatory conditions are satisfied.

The number of distinctions is not used as an implicit novelty score.

## 6. Controlled invariants

The executed test confirmed:

- OBJECT INDEX unchanged;
- DISCOVERY RESULT unchanged;
- object ID not created;
- canonization not performed;
- CMOC WRITE = NONE;
- production runtime not imported;
- production runtime import blocked.

## 7. Evidence boundary

R10 is a synthetic decision-boundary test.

It does not establish:

- production semantic novelty;
- correctness of a production NEW engine;
- production NEW_APPROVED;
- production NEW_REJECTED;
- canonization;
- CMOC mutation.

The `NEW_APPROVED` branch is a controlled evidence fixture only.

## 8. Architectural chain

The current controlled chain is:

SOURCE
→ DISCOVERY
→ DISCOVERY_RESULT
→ RECONCILIATION
→ QUERY
→ RELEVANT_COMPARISON_SET
→ SEMANTIC_COMPARISON
→ SEMANTIC_DISTINCTION
→ NEW_DECISION_INPUT
→ NEW_DECISION
→ CANONIZATION
→ CMOC WRITE

## 9. Status

R10 is **ACCEPTED as evidence of the NEW Decision boundary**.

The next architectural task is the CANONIZATION boundary: define how a NEW_APPROVED candidate is transformed into a canonical CMOC representation without silently changing its evidence, identity, relations, or existing knowledge.
