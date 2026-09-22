# O6 — DEPLOYMENT / UPGRADE BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Parent:** O0 / PROD-PROFILE-001  
**Purpose:** define controlled deployment, versioning, upgrade and rollback for the declared CMOC/Superagent production profile.

## 1. Boundary

O6 governs how the runtime is installed, changed, upgraded and rolled back.

O6 answers:

- what version is being deployed;
- what configuration accompanies it;
- what compatibility conditions must hold;
- how an upgrade is performed;
- how failure is detected;
- how rollback is performed;
- how CMOC and execution history are protected during deployment.

O6 does not:

- decide semantic meaning;
- modify ontology by deployment side effect;
- approve NEW;
- perform canonization;
- directly rewrite canonical CMOC content;
- directly modify OBJECT INDEX;
- silently migrate incompatible semantic data.

## 2. Applicability

For PROD-PROFILE-001:

- versioned deployment: REQUIRED;
- configuration versioning: REQUIRED;
- reproducible deployment: REQUIRED;
- rollback: REQUIRED;
- schema/contract compatibility: REQUIRED;
- automated deployment: UNKNOWN.

## 3. Deployment identity

Every deployment must be identifiable by:

`DEPLOYMENT_ID`
`RELEASE_VERSION`
`PROFILE_ID`
`PROFILE_VERSION`
`CONFIGURATION_VERSION`
`SOURCE_REVISION`

Where applicable:

`CMOC_FORMAT_VERSION`
`JOURNAL_FORMAT_VERSION`
`STATE_FORMAT_VERSION`
`INDEX_FORMAT_VERSION`

Deployment identity is operational identity and must remain distinct from RUN_ID and semantic object identity.

## 4. Versioning

At minimum, the runtime must distinguish:

- application/runtime version;
- contract version;
- configuration version;
- persistence format version;
- OBJECT INDEX format/builder version.

A version change must not be treated as semantically harmless merely because the process starts successfully.

## 5. Compatibility gate

Before activation:

`RELEASE`
→ `PROFILE COMPATIBILITY`
→ `CONFIGURATION COMPATIBILITY`
→ `PERSISTENCE COMPATIBILITY`
→ `CONTRACT COMPATIBILITY`
→ `ACTIVATE`

Candidate outcomes:

`COMPATIBLE`
`INCOMPATIBLE`
`COMPATIBILITY_UNKNOWN`
`DEPLOYMENT_REJECTED`

UNKNOWN compatibility must not be silently treated as compatible.

## 6. Reproducible deployment

A deployment should be reproducible from an explicit release description containing, as applicable:

- source revision;
- dependency versions;
- runtime version;
- configuration version;
- required migrations;
- deployment procedure;
- verification procedure.

A successful deployment must be attributable to a known release identity.

## 7. Configuration boundary

Configuration is separate from canonical CMOC content.

Configuration may contain:

- runtime parameters;
- storage locations;
- service endpoints;
- operational thresholds;
- access configuration;
- deployment-specific settings.

Configuration must not silently encode semantic decisions.

Configuration changes require their own version/traceability.

## 8. Upgrade boundary

Candidate upgrade sequence:

1. identify current release;
2. identify target release;
3. validate compatibility;
4. validate backup/recovery prerequisites;
5. quiesce or otherwise protect active execution according to runtime policy;
6. deploy target release;
7. verify runtime health;
8. verify persistence compatibility;
9. verify RUN/stage state;
10. verify CMOC access;
11. verify OBJECT INDEX derivation;
12. release runtime for normal execution.

If a gate fails, deployment must stop or enter explicit rollback/recovery.

## 9. Active RUN protection

An upgrade must not silently:

- duplicate an active RUN;
- reset RUN_ID;
- overwrite authoritative result;
- erase failed attempt history;
- convert interrupted execution into success.

O1/P1/P2/P3/P4/P5 remain authoritative for execution integrity.

## 10. Rollback boundary

Rollback is an operational action.

Candidate sequence:

`FAILED UPGRADE`
→ `ROLLBACK ELIGIBILITY`
→ `RESTORE PREVIOUS RUNTIME`
→ `VERIFY STATE`
→ `RESUME/RECOVERY`

Rollback must not roll back canonical semantic history merely because a runtime deployment failed.

If persistence-format migration is irreversible, rollback may be blocked and must produce an explicit incompatible-state result.

## 11. Migration boundary

A migration is permitted only when:

- migration is explicitly identified;
- source and target formats are known;
- compatibility is established;
- backup/restore prerequisite is satisfied;
- migration result is verifiable;
- rollback implications are known.

A migration must not invent semantic content.

If migration requires semantic interpretation, it leaves O6 and requires the corresponding semantic contract.

## 12. OBJECT INDEX handling

OBJECT INDEX remains derived.

After deployment/upgrade:

- existing index may be verified;
- index may be deterministically rebuilt when required;
- builder/version compatibility must be checked.

O6 does not manually repair index semantics.

C3/P8 remains the synchronization boundary.

## 13. CMOC handling

O6 may verify access to CMOC and compatibility of its persisted representation.

O6 must not:

- create new canonical objects as a deployment side effect;
- rewrite unrelated CMOC objects;
- resolve semantic conflicts;
- alter provenance or traceability;
- bypass C2/P7.

## 14. Deployment failure classes

Candidate outcomes:

`DEPLOYMENT_ACCEPTED`
`DEPLOYMENT_REJECTED`
`COMPATIBILITY_FAILED`
`CONFIGURATION_FAILED`
`HEALTH_VERIFICATION_FAILED`
`MIGRATION_FAILED`
`ROLLBACK_REQUIRED`
`ROLLBACK_COMPLETED`
`ROLLBACK_BLOCKED`
`POST_DEPLOYMENT_VERIFICATION_FAILED`

These are operational outcomes.

They are not semantic decisions.

## 15. Evidence requirements

An O6 gate should demonstrate at least:

1. explicit deployment identity;
2. version compatibility check;
3. configuration versioning;
4. reproducible release description;
5. successful deployment;
6. post-deployment health verification;
7. persistence compatibility verification;
8. active RUN protection;
9. controlled upgrade;
10. controlled rollback;
11. migration failure handling;
12. OBJECT INDEX remains derived;
13. CMOC remains protected by C2/P7;
14. no semantic responsibility leakage.

## 16. Invariants

**O6-I01 — Release identity**

Every deployment is attributable to a known release.

**O6-I02 — Compatibility honesty**

UNKNOWN compatibility is not silently accepted.

**O6-I03 — Execution protection**

Deployment cannot overwrite authoritative execution history.

**O6-I04 — Rollback separation**

Runtime rollback does not imply semantic rollback.

**O6-I05 — Persistence protection**

Irreversible migration is explicit and rollback implications are known.

**O6-I06 — Derived index**

OBJECT INDEX remains a deterministic derivative.

**O6-I07 — CMOC boundary**

Deployment cannot bypass C2/P7.

**O6-I08 — No semantic leakage**

Deployment/upgrade decisions cannot become semantic decisions.

## 17. Test boundary

The first O6 gate is a synthetic deployment/upgrade harness.

It proves:

- deployment identity;
- compatibility gating;
- configuration/version control;
- upgrade;
- rollback;
- active RUN protection;
- migration failure handling;
- CMOC/INDEX boundary preservation.

It does not establish a particular CI/CD platform, package manager, container platform, OS service manager or production deployment infrastructure.

## 18. Exit condition

O6 can move to ACCEPTED when the test demonstrates:

`identified release + compatibility gate + controlled upgrade + rollback + state protection`

without semantic responsibility leakage.

**Status:** DESIGN / ARCHITECTURE CANDIDATE
