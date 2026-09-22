# O2 — SECURITY / ACCESS BOUNDARY

**Status:** DESIGN / ARCHITECTURE CANDIDATE  
**Parent:** O0 / PROD-PROFILE-001  
**Purpose:** define the security and authorization boundary for the declared CMOC/Superagent production profile.

## 1. Boundary

O2 answers:

- who or what is acting;
- how the actor is authenticated;
- what the actor is authorized to do;
- which runtime operation is permitted;
- which persistence boundary may be reached;
- how privileged operations are recorded.

O2 does not decide semantic meaning.

Authentication and authorization are operational controls, not semantic evidence.

## 2. Applicability

For PROD-PROFILE-001:

- operator authentication: REQUIRED;
- service identity: REQUIRED;
- authorization: REQUIRED;
- privileged CMOC write control: REQUIRED;
- secret management: REQUIRED;
- network access policy: UNKNOWN;
- source-data sensitivity classification: UNKNOWN.

## 3. Security actors

Candidate actor classes:

`OPERATOR`
`RUNTIME_SERVICE`
`RECOVERY_SERVICE`
`BUILD_INDEX_SERVICE`
`ADMINISTRATOR`

An actor identity must be distinguishable from:

- RUN_ID;
- STAGE_ID;
- ATTEMPT_ID;
- RESULT_ID;
- OBJECT_ID.

An execution identity is not an authorization identity.

## 4. Authentication boundary

Authentication establishes:

`ACTOR_IDENTITY`

It does not establish:

`PERMISSION`

and it does not establish:

`SEMANTIC_VALIDITY`.

Candidate outcomes:

`AUTHENTICATED`
`AUTHENTICATION_FAILED`
`IDENTITY_UNKNOWN`
`CREDENTIAL_UNAVAILABLE`

Failed authentication must not be converted into an anonymous privileged operation.

## 5. Authorization boundary

Authorization evaluates:

`ACTOR + OPERATION + TARGET`

Candidate operations:

- START_RUN;
- READ_SOURCE;
- READ_RUN_STATE;
- READ_JOURNAL;
- REQUEST_RECOVERY;
- WRITE_CANONICAL_CMOC;
- BUILD_OBJECT_INDEX;
- READ_OBJECT_INDEX;
- DEPLOY_RUNTIME;
- RESTORE_BACKUP;
- CHANGE_CONFIGURATION.

Candidate authorization outcomes:

`AUTHORIZED`
`DENIED`
`TARGET_NOT_ALLOWED`
`OPERATION_NOT_ALLOWED`

Authorization does not evaluate whether a proposed semantic object is correct.

## 6. Minimum privilege boundary

The baseline should use least privilege.

Examples:

- runtime execution does not automatically imply deployment privilege;
- index synchronization does not imply arbitrary CMOC write privilege;
- read access does not imply mutation;
- recovery request does not imply semantic approval;
- operator access does not imply unrestricted filesystem access.

## 7. CMOC write protection

The production CMOC write boundary remains C2/P7.

O2 controls **who may invoke that boundary**.

O2 must not:

- create a canonical object;
- approve NEW;
- canonize;
- resolve semantic conflict;
- alter canonical representation;
- bypass C2/P7.

The authorization decision is:

`MAY_CALL_C2/P7 = TRUE/FALSE`

not:

`OBJECT_IS_VALID = TRUE/FALSE`.

## 8. OBJECT INDEX protection

O2 may authorize invocation of C3/P8.

It must not:

- edit OBJECT INDEX directly;
- create semantic index entries;
- resolve index conflicts;
- turn a missing index object into a new CMOC object.

The existing deterministic derivation boundary remains authoritative.

## 9. Secret management

Required operational controls:

- credentials are not stored in source code;
- credentials are not stored in canonical CMOC representations;
- credentials are not emitted into execution journal records;
- privileged secrets are not exposed through ordinary read operations.

Exact secret-storage technology remains unspecified by O2.

## 10. Audit boundary

Security-sensitive operations should produce an operational audit record containing, as applicable:

- actor identity;
- operation;
- target;
- authorization result;
- timestamp;
- RUN_ID;
- stage/attempt identity where relevant;
- reason/result code.

The audit record must not become a second semantic decision record.

## 11. Failure behavior

Security failure must stop the protected operation.

Examples:

`AUTHENTICATION_FAILED`
→ protected operation does not execute.

`AUTHORIZED = FALSE`
→ protected operation does not execute.

`CREDENTIAL_UNAVAILABLE`
→ operation fails explicitly.

No security failure may be silently interpreted as:

- NEW;
- NEEDS_REVIEW;
- APPROVED;
- RETRY_SUCCESS.

## 12. Recovery interaction

Recovery must preserve security boundaries.

A restart or retry does not grant new privileges.

A recovered RUN must execute under an authenticated/authorized runtime identity.

REC may decide recovery admissibility according to its contract; O2 decides whether the actor/service is authorized to perform the resulting operation.

## 13. Deployment interaction

Deployment privileges remain separate from runtime privileges.

A deployment actor may be authorized to install or upgrade the runtime without being authorized to create semantic CMOC objects.

Conversely, a semantic persistence service may be authorized to write only through the C2/P7 boundary without deployment privileges.

## 14. Evidence requirements

An O2 gate should demonstrate at least:

1. authenticated actor accepted;
2. unauthenticated actor rejected;
3. authorized operation accepted;
4. unauthorized operation rejected;
5. target-specific authorization;
6. read/write separation;
7. CMOC write restricted to C2/P7;
8. OBJECT INDEX mutation restricted to C3/P8;
9. secret material excluded from logs;
10. security failure stops protected operation;
11. recovery does not bypass authorization;
12. no semantic responsibility leakage.

## 15. Invariants

**O2-I01 — Identity separation**

Actor identity is separate from execution identity.

**O2-I02 — Authentication/authorization separation**

Authentication does not imply authorization.

**O2-I03 — Least privilege**

Authorization is operation- and target-specific.

**O2-I04 — Persistence boundary protection**

O2 controls access to C2/P7; it does not replace C2/P7.

**O2-I05 — Index boundary protection**

O2 controls access to C3/P8; it does not replace C3/P8.

**O2-I06 — Security failure honesty**

Denied or unauthenticated operations do not execute as privileged operations.

**O2-I07 — No semantic leakage**

Security decisions cannot become semantic decisions.

## 16. Test boundary

The first O2 test is a synthetic authorization harness.

It proves the security boundary only.

It does not establish a particular identity provider, OS account model, TLS configuration, network firewall, secrets manager or enterprise IAM platform.

Technology selection belongs to the implementation phase after the boundary is accepted.

## 17. Exit condition

O2 can move to ACCEPTED when the test demonstrates:

`actor identity + authentication + operation/target authorization + protected persistence boundaries`

with no semantic responsibility leakage.

**Status:** DESIGN / ARCHITECTURE CANDIDATE
