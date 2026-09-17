# GM-096 — Managed Transition: Organizational Handover Blind Test

**Date:** 17-09-2026  
**Change Notice:** 0141+170926  
**Status:** CROSS-CHECK COMPLETE / NON-CANON

## Purpose

Test the working CMOC Pattern **Managed Transition / Управляемый переход** on a non-IT, non-GM/QMS domain: transfer of a function, responsibility, or operational ownership from one organizational unit/person to another.

The test is deliberately performed without using GM/QSB terminology as the construction basis.

## Blind-test hypothesis

Working Pattern grammar:

```text
STATE A
→ IDENTIFY
→ ASSESS
→ DECIDE / AUTHORIZE
→ CONTROLLED TRANSITION
→ VERIFY
→ ACCEPT / RETURN / CORRECT
→ RECORD / CLOSE
```

Question: can this grammar reconstruct a real organizational handover without adding a new Pattern or relying on GM-specific concepts?

## Independent evidence

### 1. UK Health and Safety Executive — organisational change

HSE states that organisational changes such as changes in roles/responsibilities should be systematically managed. The guidance requires:

- identification and assessment of direct and indirect effects of the proposed change;
- planning of the change;
- consultation before, during and after the change;
- identification and successful transfer of key tasks and responsibilities;
- training/support for changed roles;
- review of plans and assessments.

Source: HSE, **Organisational change**.

### 2. UK Health and Safety Executive — shift handover

HSE describes handover between people/teams as a controlled transfer of task responsibility. The construction contains:

- preparation by outgoing personnel;
- handover/exchange of relevant information;
- cross-checking by incoming personnel as they assume responsibility;
- written and verbal information;
- joint responsibility during the handover.

Source: HSE, **Shift handover**.

### 3. UK National Archives — organisational/function transfer

For organisational changes involving transfer of functions, the guidance calls for:

- a joint transition project between transferring and receiving organisations;
- identification and transfer of relevant records and knowledge;
- governance arrangements covering the transition;
- documented decisions and processes;
- continuity until completion.

Source: The National Archives, **Machinery of Government and organisational change**.

### 4. UK Government — Gate 4 Readiness for Service

The Gate 4 model provides an explicit readiness decision before implementation and requires confirmation of:

- risks and unresolved issues;
- resources and readiness;
- organisational controls;
- agreed transition/handover plans;
- training and communications;
- testing against predefined acceptance criteria;
- handover from project responsibility to the operational business owner;
- recording of defects/incomplete work and remediation plans.

Source: GOV.UK, **Gate Review 4: Readiness for Service**.

### 5. UK Government — actual function handover example

A documented NHS transition used Handover Certificates. The receiving organisation's senior manager signed acceptance for safe receipt of the function, explicitly signalling that arrangements were in place for responsibility to continue. A shared tracker showed where responsibility for each function was held.

Source: Sutton and Merton PCT Annual Report and Accounts 2012–13.

### 6. UK Government / TfL — acceptance and transfer of operational responsibility

A London Underground Projects/Operations Acceptance and Handover Certificate contains explicit statements that the receiving Operations function accepts transfer of responsibility and releases the asset for service, with documentation and outstanding work recorded.

Source: London Underground Limited, Projects/Operations Acceptance and Handover Certificate.

## Reconstruction against Managed Transition

| Pattern step | Organizational handover evidence |
|---|---|
| IDENTIFY | Function/task/responsibility to be transferred is identified; boundaries and affected parties are determined. |
| ASSESS | Risks, impacts, resources, readiness, information and capability are assessed. |
| DECIDE / AUTHORIZE | Governance/management determines readiness and authorizes implementation/handover. |
| CONTROLLED TRANSITION | Knowledge, records, tasks and responsibilities are transferred; overlap/shadow operation may be used. |
| VERIFY | Incoming side cross-checks information, readiness and ability to assume responsibility; acceptance criteria/testing may be used. |
| ACCEPT / RETURN / CORRECT | Receiving side accepts responsibility; unresolved items can remain under agreed remediation; failed readiness can delay/return the transition. |
| RECORD / CLOSE | Handover certificates, trackers, decisions, records and outstanding actions document the resulting state. |

## Important observation

The organizational case makes the **STATE** dimension more visible than the IT test.

The object of transition is not merely a process or technology. It can be:

- a function;
- a task;
- an accountability;
- operational ownership;
- associated knowledge and records.

The transition therefore changes the organizational state from:

```text
RESPONSIBILITY HELD BY A
        ↓
RESPONSIBILITY PREPARED FOR TRANSFER
        ↓
RESPONSIBILITY HANDED OVER
        ↓
RESPONSIBILITY ACCEPTED BY B
```

The Handover Certificate is not the transition itself. It is an **Artifact / evidence mechanism** that records the accepted state.

## Boundary test

### Decision Gate

Present as a reusable decision mechanism: readiness/authorization before transfer. It is not the Pattern itself.

### Assessment against Criterion

Present as a reusable assessment function: risks, readiness, capability, acceptance criteria. It remains a reusable Pattern/function rather than becoming the definition of Managed Transition.

### Verification

Present and particularly explicit in handover: incoming party cross-checks information and assumes responsibility only after verification/acceptance.

### Controlled Deviation

Not intrinsic. The organizational handover can occur without any deviation from the normal operating model. If temporary overlap, exception or interim responsibility is required, Controlled Deviation may be invoked separately.

### Response to Abnormality

Not intrinsic. It becomes relevant only when readiness failure, missing information, unresolved risk or another abnormal condition occurs.

## Result

The blind test **passes**.

The same minimal grammar reconstructs a genuine organizational transition/handover without GM/QMS-specific concepts:

```text
STATE A
→ IDENTIFY
→ ASSESS
→ DECIDE / AUTHORIZE
→ CONTROLLED TRANSITION
→ VERIFY
→ ACCEPT / CORRECT / RETURN
→ RECORD / CLOSE
```

Independent organizational sources therefore provide additional evidence for the working Pattern.

## CMOC classification

- **Kind:** PATTERN
- **Name:** Managed Transition / Управляемый переход
- **Status:** STRONG PATTERN CANDIDATE
- **Evidence:** MULTI-SOURCE CONFIRMED
- **Domain coverage tested:**
  - GM manufacturing change
  - IT migration/deployment
  - organizational handover / transfer of responsibility
- **Canon:** NO

## Architectural conclusion

The blind test strengthens the hypothesis that Managed Transition is a higher-order CMOC Pattern describing **controlled movement of an entity/system/organizational responsibility from one accepted state to another**.

Specialized Machines and mechanisms remain domain-specific realizations underneath this Pattern.

No new Machine, Pattern, or Mechanism is created by this test.

No REG-001 change.

No Canon change.

No Machine Catalog update.

## Sources

- HSE — Organisational change
- HSE — Shift handover
- The National Archives — Machinery of Government and organisational change
- GOV.UK — Gate Review 4: Readiness for Service
- Sutton and Merton PCT Annual Report and Accounts 2012–13
- London Underground Limited — Projects/Operations Acceptance and Handover Certificate
