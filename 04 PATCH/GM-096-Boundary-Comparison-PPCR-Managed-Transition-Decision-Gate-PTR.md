# GM-096 — Focused Boundary Comparison — PPCR / Managed Transition / Decision Gate / PTR

**Notice:** 0172+180926  
**Status:** PASS WITH QUALIFICATION / WORKING SPECIFICATION / NON-CANON

## 1. Purpose

Проверить границу между четырьмя конструкциями: Plant Process Change Control (PPCR), Managed Transition, Decision Gate и Production Trial Run (PTR).

Главный вопрос: где находится bounded Machine PPCR, а где начинается более крупная transition architecture и отдельные механизмы принятия решения / испытания?

No Catalog / Canon / REG-001 changes are made by this test.

## 2. Starting structures

### Managed Transition
Working Pattern: STATE A → IDENTIFY → ASSESS → AUTHORIZE → CONTROLLED TRANSITION → VERIFY → ACCEPT / RETURN → RECORD / CLOSE.
Managed Transition — Pattern, not Machine.

### PPCR
Working Machine candidate: PROPOSED CHANGE → CONTROLLED CHANGE CASE → REVIEW / AUTHORIZATION → IMPLEMENTATION TRACEABILITY → FINAL ACCEPTANCE.
PPCR controls a specific plant process change through authorization, implementation traceability and closure.

### Decision Gate
Working mechanism: INPUT / EVIDENCE → DECISION → AUTHORIZE / REJECT.
Decision Gate does not by itself own the whole change case, transition or trial.

### PTR
Working Machine candidate: CHANGE REQUIRING TRIAL → CONTROLLED PRODUCTION TRYOUT → RESULT / REVIEW.
PTR performs a limited, controlled and contained production tryout to evaluate a change before full implementation.

## 3. Test A — Level of abstraction

| Construction | Working class | Primary question |
|---|---|---|
| Managed Transition | PATTERN | How is a transition between states structurally managed? |
| PPCR | MACHINE CANDIDATE | How is a specific plant process change controlled through authorization and closure? |
| Decision Gate | MECHANISM | What decision is made at a defined gate? |
| PTR | MACHINE CANDIDATE | Does the proposed change work in a controlled production tryout? |

**Result: PASS.** The apparent overlap is largely caused by different abstraction levels.

## 4. Test B — Can Managed Transition be reduced to PPCR?

Apply the Managed Transition grammar to software deployment, organizational handover, temporary operating state or migration. The grammar remains meaningful; PPCR does not.

**Result: PASS.** PPCR is a domain-specific bounded realization inside a broader transition architecture, while Managed Transition remains domain-neutral.

## 5. Test C — Can PPCR be reduced to Decision Gate?

Remove initiation, change characterization, stakeholder identification, implementation, breakpoint, open-issue closure and final approval. What remains is approximately INPUT / EVIDENCE → DECISION → PROCEED / STOP.

That is Decision Gate.

**Result: PASS.** Decision Gate is a mechanism used by PPCR; PPCR is not merely Decision Gate.

## 6. Test D — Can PPCR be reduced to PTR?

PPCR may determine whether a PTR is required. PTR then performs the controlled production tryout and review. PPCR remains responsible for the broader change case.

**Result: PASS.** PPCR → PTR is a valid composition; PPCR = PTR is not supported.

## 7. Test E — Can PTR be reduced to Decision Gate?

PTR contains decisions and approvals, but the GM source explicitly defines PTR as a limited, controlled and contained production tryout used to evaluate a change before full production implementation.

**Result: PASS.** Decision Gate can authorize PTR; it does not constitute PTR.

## 8. Test F — Can PTR be reduced to Managed Transition?

PTR does not itself manage the complete transition from State A to State B. It provides evidence about a proposed change in the normal production environment.

**Result: PASS.** PTR is a specialized Machine participating in a broader transition Assembly.

## 9. Test G — PPCR boundary inside Managed Transition

Working composition:

MANAGED TRANSITION → IDENTIFY / ASSESS → PPCR → DECISION / AUTHORIZATION → PTR if required OR DIRECT IMPLEMENTATION → VERIFY / ACCEPT → RETURN / CLOSE.

**Result: PASS WITH QUALIFICATION.** PPCR has a bounded execution identity, but it is naturally embedded in Managed Transition.

The qualification is not “PPCR is not a Machine”. Rather: PPCR may be a Machine at one abstraction level while simultaneously functioning as a specialized component of the Managed Transition Assembly.

## 10. Test H — Closure conditions

| Construction | Local closure |
|---|---|
| Managed Transition | transition accepted, returned, rolled back or otherwise closed |
| PPCR | implementation recorded, open issues closed, final approval obtained |
| Decision Gate | decision made and gate exited |
| PTR | controlled trial and required review/evaluation completed |

**Result: PASS.** The four closure conditions are not interchangeable.

## 11. Test I — Identity-bearing relation

| Construction | Identity-bearing relation |
|---|---|
| Managed Transition | manage transition between accepted states |
| PPCR | control a specific plant process change through authorization, implementation traceability and closure |
| Decision Gate | make a bounded decision at a defined gate |
| PTR | produce controlled production evidence about a proposed change |

**Result: PASS.** Each relation is independently expressible.

## 12. Negative test — “Change Management Machine”

Tempting abstraction: CHANGE → REVIEW → APPROVE → IMPLEMENT → VERIFY → CLOSE.

Calling this one Machine would absorb PPCR, PTR, Bypass, Banking, Decision Gate and verification.

**Result: FAIL as Machine identity.** This is better treated as higher-level transition/change architecture, with Managed Transition as the current working Pattern.

## 13. Negative test — “Approval Machine”

REQUEST → SIGNATURE → PROCEED / STOP is a Decision Gate / authorization mechanism.

**Result: FAIL as PPCR identity.** It does not contain PPCR's complete change-case boundary.

## 14. Composition test

CHANGE NEED → MANAGED TRANSITION → PPCR → DECISION GATE → PTR? → EVALUATION → IMPLEMENTATION / RETURN / FURTHER ACTION → VERIFICATION → ACCEPT / CLOSE.

This is a CMOC composition test, not a claim that every GM change follows exactly this path.

**Result: PASS.** The structures compose without requiring one to absorb another.

## 15. Critical architectural finding

PPCR is not the whole Managed Transition, a Decision Gate, PTR, a form, implementation alone or final verification alone.

At the working Machine level it can be treated as a bounded change-control Machine for a plant process change.

At the Assembly level it is naturally a specialized change-control component inside Managed Transition.

These statements are compatible because Machine and Assembly describe different architectural levels.

## 16. Consequence for Machine Passport v0.3

**No schema change.**

The comparison confirms that the Passport separation of identity, execution boundary, local capability, closure, realization, relations and validation is sufficient.

## 17. Consequence for Catalog / Canon / REG-001

- Catalog: NO CHANGE
- Canon: NO CHANGE
- REG-001: NO CHANGE
- Passport v0.3: NO CHANGE

PPCR remains MACHINE CANDIDATE WITH QUALIFICATION / NON-CANON.
PTR remains SPECIALIZED MACHINE CANDIDATE / NON-CANON.
Decision Gate remains MECHANISM / HOLD.
Managed Transition remains STRONG PATTERN CANDIDATE / MULTI-SOURCE CONFIRMED / NON-CANON.

## 18. Step closure

The focused boundary comparison is complete.

**Result: PASS WITH QUALIFICATION.**

Key distinction: PATTERN Managed Transition → transition architecture → PPCR / PTR / other specialized Machines and Decision Gate mechanisms.

PPCR does not need to be downgraded merely because it sits inside Managed Transition. At the same time, it must not be promoted to a universal Change Management Machine.

**Nothing additional needs to be changed now.**

Next we can return to the GM-096 candidate sequence and proceed with the remaining candidate architecture, keeping this Pattern / Machine / Mechanism boundary fixed.