# GM-096 — Focused Machine Boundary Comparison — Nonconforming Product Control / Banking / Bypass / Fast Response

**Notice:** 0170+180926  
**Status:** PASS WITH QUALIFICATION / WORKING SPECIFICATION / NON-CANON  
**Purpose:** отделить четыре близких кандидата, работающих вокруг abnormal / out-of-normal material or process states, чтобы не принять общую тему «контроль отклонения» за одну Machine или, наоборот, не породить лишние Machines из частично совпадающих механизмов.

---

## 1. Starting point

После применения Machine Passport v0.3 к:

- **Nonconforming Product Control**;
- **Banking Process**;
- **Bypass Process Control**;

возникает естественный риск Machine proliferation.

Все четыре конструкции могут встречаться в одном событии:

`ABNORMAL / OUT-OF-NORMAL CONDITION`

и использовать общие механизмы:

- identification;
- status marking;
- segregation / containment;
- authorization;
- verification;
- records;
- escalation;
- handoff.

Но наличие общих механизмов не доказывает общую Machine identity.

Тест поэтому задаёт четыре вопроса:

1. Что именно является identity-bearing relation / mode?
2. Какова собственная execution boundary?
3. Какую local capability поддерживает кандидат?
4. Что означает его closure?

---

# 2. Four candidate structures

## A. Nonconforming Product Control

Working structure:

`NONCONFORMING / SUSPECT PRODUCT → CONTROLLED PRODUCT STATUS → AUTHORIZED DISPOSITION`

Identity-bearing relation:

> **CONTROL THE STATUS AND MOVEMENT OF AFFECTED PRODUCT SO THAT UNINTENDED USE / RELEASE IS PREVENTED UNTIL AUTHORIZED DISPOSITION.**

Local capability:

> Prevent unintended use or release of affected product while preserving identification, status and traceability through disposition.

Closure:

> affected product reaches authorized terminal disposition or controlled downstream handoff with identification, status and traceability preserved.

Primary object:

**affected product / material with actual or suspected nonconformance.**

---

## B. Banking Process

Working structure:

`OUT-OF-NORMAL-FLOW MATERIAL → CONTROLLED BANKING STATE → IDENTIFICATION / SEGREGATION / STATUS CONTROL → AUTHORIZED DISPOSITION / RELEASE`

Identity-bearing mode:

> **CONTROL MATERIAL OUTSIDE THE NORMAL PROCESS FLOW IN A DEFINED BANKING STATE UNTIL AUTHORIZED DISPOSITION / RELEASE.**

Local capability:

> Prevent unintended use or uncontrolled movement of material outside normal flow while preserving identification, status and traceability.

Closure:

> authorized terminal disposition/release, or controlled downstream transfer with status and traceability preserved.

Primary object:

**material deliberately placed outside the normal flow in a controlled banking state.**

---

## C. Bypass Process Control

Working structure:

`NORMAL APPROVED PROCESS UNAVAILABLE / ALTERED → CONTROLLED ALTERNATIVE ROUTE → VERIFIED EXIT → AUTHORIZED RETURN / TERMINAL DISPOSITION`

Identity-bearing mode:

> **CONTROL A TEMPORARY ALTERNATIVE ROUTE WHEN THE APPROVED NORMAL PROCESS CANNOT BE EXECUTED AS DOCUMENTED, WITH VERIFIED EXIT AND AUTHORIZED RETURN.**

Local capability:

> Maintain controlled production during temporary unavailability/alteration of the approved process and provide verified, traceable exit back to the approved process or controlled terminal disposition.

Closure:

> bypass interval ended at recorded exit breakpoint; original process readiness/parameters verified; required output validated; return authorized or terminal disposition established.

Primary object:

**production process temporarily operating outside the approved normal route.**

---

## D. Fast Response

Working source-derived structure:

`ABNORMALITY → SIGNAL / ESCALATION → RAPID RESPONSE → CONTAIN / CORRECT → VERIFY / CLOSE`

Working identity-bearing mode:

> **TRANSFER A DETECTED ABNORMAL CONDITION INTO A RAPID, OWNED RESPONSE LOOP UNTIL THE CONDITION IS CONTAINED / CORRECTED OR ESCALATED.**

Local capability:

> initiate and coordinate rapid response to an abnormal condition, establish containment/cause-investigation/action as required, and move the event toward verified closure.

Closure:

> response has reached its defined local result — containment/correction verified or the case has been formally escalated/handoff completed.

Important qualification:

Fast Response is broader than product-status control. It may **invoke or contain** Nonconforming Product Control, but the two are not identical.

---

# 3. Test A — Same event, different identity

Consider one event:

> A production station produces suspect parts because the normal process is temporarily unavailable.

The same event can instantiate all four structures:

### Nonconforming Product Control

Question:

> What must happen to the affected parts?

Answer:

`IDENTIFY → CONTAIN / STATUS → DISPOSITION → CONTROLLED RELEASE / REWORK / SCRAP`

### Banking

Question:

> Where / in what controlled state does material outside normal flow remain until disposition?

Answer:

`PLACE / MAINTAIN IN BANKING STATE → STATUS / TRACEABILITY → RELEASE / DISPOSITION`

### Bypass

Question:

> How can production continue while the approved normal process cannot be used?

Answer:

`ENTER CONTROLLED ALTERNATIVE ROUTE → EXECUTE → VERIFY EXIT → RETURN`

### Fast Response

Question:

> How is the abnormal event transferred into an immediate managed response?

Answer:

`SIGNAL / ESCALATE → RAPID RESPONSE → CONTAIN / CORRECT → VERIFY`

### Result: PASS — distinct identity dimensions

The same physical event can instantiate several Machines because the Machines control different relations.

This is not duplication.

It is **orthogonal control of different state dimensions**.

---

# 4. Test B — Identity-bearing relation comparison

| Candidate | Identity-bearing relation / mode | What it controls |
|---|---|---|
| Nonconforming Product Control | affected product → controlled status → authorized disposition | **status and movement of affected product** |
| Banking | out-of-normal-flow material → controlled banking state → disposition/release | **controlled holding state outside normal flow** |
| Bypass | approved normal process unavailable → controlled alternative route → verified exit | **temporary alternative process route** |
| Fast Response | abnormality → owned rapid response → containment/correction/escalation | **response state / response tempo to abnormality** |

### Result: PASS

The four candidates do not share one identity-bearing relation.

Their commonality is primarily **context and supporting mechanisms**, not Machine identity.

---

# 5. Test C — Object replacement test

## C1. Replace affected product with an otherwise normal product merely waiting outside normal flow

Result:

- Nonconforming Product Control no longer necessarily applies.
- Banking can still apply.

**PASS — Banking is not reducible to nonconformance.**

## C2. Remove the banking state but keep the product nonconforming

Result:

- Nonconforming Product Control can still operate through containment/segregation and authorized disposition.
- Banking is not required as the identity of the control.

**PASS — Banking is not the generic name for nonconforming-product control.**

## C3. Replace the unavailable process with a different approved alternative route

Result:

- Bypass remains applicable if the normal approved process is temporarily unavailable/altered and the alternative route is controlled.

**PASS — Bypass identity is process-route based, not product-status based.**

## C4. Remove the immediate abnormal-response requirement

Result:

- Product control or Banking may still operate.
- Fast Response no longer necessarily applies.

**PASS — Fast Response is response-loop based, not merely material-status based.**

---

# 6. Test D — Component replacement / mechanism overlap

All four may use:

- labels;
- records;
- status indicators;
- segregation;
- authorization;
- verification;
- escalation;
- handoff.

Therefore:

> **shared mechanisms ≠ shared Machine identity.**

### Example

A hold tag may appear in:

- Nonconforming Product Control;
- Banking;
- Bypass;
- Fast Response.

But the tag is an **artifact / mechanism**.

It does not determine which Machine is executing.

### Result: PASS

The Machine boundary survives removal of the shared implementation mechanisms because the identity-bearing relation remains definable independently.

---

# 7. Test E — Closure comparison

Closure is especially useful because the four candidates stop at different conditions.

| Candidate | Local closure |
|---|---|
| Nonconforming Product Control | affected product reaches authorized disposition or controlled handoff |
| Banking | banked material reaches authorized release/disposition or controlled downstream transfer |
| Bypass | bypass interval ends after exit verification/validation and authorized return or terminal disposition |
| Fast Response | abnormal event reaches defined response result or controlled escalation/handoff |

### Result: PASS

The closure conditions are materially different.

In particular:

> **return to normal process** is central to Bypass but not to Nonconforming Product Control.

And:

> **authorized disposition of affected product** is central to Nonconforming Product Control but not the defining closure of Fast Response.

And:

> **controlled banking state** is central to Banking but is not required by the other three.

---

# 8. Test F — Boundary pair: Nonconforming Product Control ↔ Banking

This is the closest pair.

## Similarity

Both may produce:

`IDENTIFICATION → STATUS CONTROL → SEGREGATION / CONTROLLED LOCATION → DISPOSITION`

## Difference

Nonconforming Product Control is triggered by:

> **actual or suspected nonconformance.**

Banking is triggered by:

> **material being outside the normal process flow and requiring controlled banking.**

Therefore a banked item may be:

- nonconforming;
- awaiting a process decision;
- temporarily outside normal flow for another controlled reason.

### Result: DISTINCT / PASS WITH QUALIFICATION

Banking can be a **realization or supporting state** inside Nonconforming Product Control.

Conversely, Nonconforming Product Control can use Banking as one containment realization.

Neither implication makes the two Machines identical.

---

# 9. Test G — Boundary pair: Banking ↔ Bypass

## Banking

Controls:

`MATERIAL STATE / LOCATION OUTSIDE NORMAL FLOW`

## Bypass

Controls:

`PROCESS ROUTE TEMPORARILY DIFFERENT FROM APPROVED NORMAL ROUTE`

A bypass can generate material that is later banked.

Banking can receive material generated during a bypass.

But:

> Banking controls the material state; Bypass controls the temporary process route.

### Result: DISTINCT / PASS

The two candidates are compositionally compatible rather than redundant.

Possible chain:

`BYPASS → AFFECTED / SUSPECT OUTPUT → BANKING → DISPOSITION`

---

# 10. Test H — Boundary pair: Bypass ↔ Nonconforming Product Control

A bypass does not necessarily mean that product is nonconforming.

The source examples include situations where the approved process is unavailable or altered and production must proceed under controlled alternative conditions.

Conversely, nonconforming product can exist without any bypass.

Therefore:

`BYPASS ≠ NONCONFORMING PRODUCT CONTROL`

A realistic composition may be:

`BYPASS → DETECT / VERIFY PRODUCT CONDITION → NONCONFORMING PRODUCT CONTROL`

### Result: DISTINCT / PASS

The distinction is process-route control versus affected-product status/disposition control.

---

# 11. Test I — Boundary pair: Fast Response ↔ Nonconforming Product Control

Fast Response can react to:

- quality abnormality;
- process abnormality;
- equipment issue;
- safety/operational issue;
- other urgent conditions within the source-defined response architecture.

Nonconforming Product Control is specifically about affected product and its controlled status/disposition.

Therefore:

`FAST RESPONSE → CONTAIN / INITIATE PRODUCT CONTROL`

is a valid composition.

But:

`FAST RESPONSE = PRODUCT CONTROL`

is not supported.

### Result: DISTINCT / PASS

Fast Response is a response-loop mechanism/architecture; Nonconforming Product Control is a product-status/disposition Machine.

---

# 12. Test J — Boundary pair: Fast Response ↔ Banking / Bypass

### Fast Response ↔ Banking

Fast Response may initiate immediate containment and cause affected material to be placed into a controlled state.

Banking owns the controlled material state, not the overall urgency/response loop.

**Result: DISTINCT / PASS**

### Fast Response ↔ Bypass

Fast Response may be triggered because a process has failed and may coordinate the decision to establish a bypass.

Bypass owns the controlled alternative route and verified exit.

**Result: DISTINCT / PASS**

---

# 13. Negative test — “Abnormality Control Machine”

A tempting abstraction is:

`ABNORMALITY → CONTROL → DISPOSITION / RETURN TO NORMAL`

and then to call all four candidates realizations of one Machine.

### Result: FAIL as a Machine identity

The abstraction is too broad.

It collapses four materially different identity-bearing relations:

- product status/disposition;
- material banking state;
- alternative process route;
- rapid response loop.

It is therefore better treated as a **contextual family / Assembly-level framing**, not as evidence that the four candidates are one Machine.

---

# 14. Composition test

The four Machines can legitimately compose.

One possible architecture:

```
ABNORMALITY / PROCESS INTERRUPTION
          ↓
      FAST RESPONSE
          ↓
   ┌──────┴────────┐
   ↓               ↓
BYPASS          AFFECTED PRODUCT
   ↓               ↓
CONTROLLED       NONCONFORMING
ALTERNATIVE      PRODUCT CONTROL
ROUTE                ↓
   ↓              BANKING
   └──────┬─────────┘
          ↓
   VERIFICATION / DISPOSITION
          ↓
     RETURN / CLOSE
```

This diagram is **not** asserted as a universal GM QSB sequence.

It is a composition test showing that the candidates can coexist without absorbing one another.

### Result: PASS WITH QUALIFICATION

The exact order is domain/event dependent.

---

# 15. Machine proliferation rule strengthened

This comparison strengthens a general CMOC rule:

> **Do not create a new Machine merely because an object enters an abnormal state, receives a new status, or is handled by a different department.**

A new Machine requires evidence of a distinct:

`identity-bearing relation / mode + own execution boundary + local capability + closure condition`

The following are insufficient by themselves:

- same abnormal event;
- same product/material;
- same label or record;
- same containment action;
- same authorization;
- same downstream disposition;
- different department;
- different urgency;
- different terminology.

---

# 16. Boundary matrix

| Criterion | Nonconforming Product Control | Banking | Bypass | Fast Response |
|---|---|---|---|---|
| Primary identity | product status/disposition | controlled material state | alternative process route | rapid response loop |
| Requires nonconformance | Yes / suspect condition | No | No | No |
| Requires material outside normal flow | Usually affected material is controlled; not identity itself | Yes | Not necessarily | No |
| Requires alternative process route | No | No | **Yes** | No |
| Requires rapid response | No | No | No | **Yes / defining mode** |
| Owns affected product status | **Yes** | Partially / in banking state | No | No |
| Owns temporary process route | No | No | **Yes** | No |
| Owns response loop | No | No | No | **Yes** |
| Core closure | disposition / handoff | release / disposition / transfer | verified exit / return | response result / escalation |
| Can invoke another | Yes | Yes | Yes | Yes |
| Can be composed with another | Yes | Yes | Yes | Yes |

---

# 17. Architectural result

The focused comparison supports four **distinct candidate identities**:

### Nonconforming Product Control

**MACHINE CANDIDATE — structurally supported**

Identity:

> controlled status and movement of affected nonconforming/suspect product until authorized disposition.

### Banking Process

**MACHINE CANDIDATE — structurally supported, with qualification**

Identity:

> controlled banking state for material outside normal flow until authorized disposition/release.

### Bypass Process Control

**MACHINE CANDIDATE — structurally supported**

Identity:

> controlled temporary alternative process route with verified exit and authorized return/disposition.

### Fast Response

**DISTINCT RESPONSE-LOOP CANDIDATE — structurally distinguishable**

Identity under current working abstraction:

> transfer of abnormality into a rapid owned response loop until containment/correction or escalation.

The present test does **not** establish final Catalog promotion for any of the four.

---

# 18. Consequence for Passport v0.3

**No schema change.**

The test confirms that v0.3 can distinguish Machines whose identity types are very different:

- product-status control;
- controlled state / handling mode;
- alternative process route;
- rapid response mode.

The decisive fields remain:

- identity-bearing relation / mode;
- local capability;
- execution boundary;
- closure condition.

No additional Passport field is required by this comparison.

---

# 19. Consequence for Catalog / Canon / REG-001

- **Catalog:** NO CHANGE
- **Canon:** NO CHANGE
- **REG-001:** NO CHANGE
- **Passport v0.3:** NO CHANGE

The test is methodological and boundary-setting.

It does not justify promotion of candidates to Canon or modification of existing Catalog entries.

---

# 20. Step closure

The focused Boundary Comparison is complete.

**Result: PASS WITH QUALIFICATION.**

The four candidates are sufficiently distinguished at the working Machine-boundary level:

`NONCONFORMING PRODUCT CONTROL ≠ BANKING ≠ BYPASS ≠ FAST RESPONSE`

while remaining compositionally compatible.

The most important finding is:

> **One abnormal event may legitimately activate several different Machines because they control different state dimensions and have different closure conditions.**

**Nothing additional needs to be changed now.**

The next methodological step can return to the GM-096 candidate sequence and apply the frozen Passport v0.3 to the next candidate, without reopening the Passport schema.
