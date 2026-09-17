# GM QSB — Reverse PFMEA — Pattern → Machine Decomposition Test

**Notice:** 0144+170926

## 1. Purpose

Проверить, как общий Pattern `Risk Model Feedback Loop` реализуется в специализированной Machine `Reverse PFMEA`, и провести границу между:

- тем, что принадлежит самой Machine;
- тем, что предоставляется окружающей Assembly;
- тем, что является downstream effect / последующим изменением.

Это decomposition test, не канонизация.

Рабочая Pattern:

`INTENDED / EXPECTED STATE → REALIZED STATE → EVIDENCE → GAP / NEW INFORMATION → ACTION → VERIFY → UPDATE`

Reverse PFMEA в GM QSB описан как on-station review failure modes из PFMEA cross-functional team с проверкой наличия и работоспособности prevention/detection controls; после проверки существующих failure modes выполняется попытка обнаружить новые failure modes, а findings документируются в action plan. citeturn0search0turn0search1

## 2. Machine candidate

**Working name:** Reverse PFMEA / Обратная PFMEA

**Class:** MACHINE

**Domain:** process risk / production station

**Working capability:**

> Detect discrepancies between PFMEA-defined failure-mode/control expectations and the realized station state, including previously unidentified failure modes, and produce verified findings for risk-model/process update.

Это capability-формулировка decomposition test, не каноническое определение.

## 3. Machine boundary

### 3.1 What the Machine receives

**Inputs / supplied context:**

- existing PFMEA;
- Control Plan;
- Reverse PFMEA checklist;
- claims / scrap / past quality issues;
- error-proofing verification results;
- station audit information;
- scheduled station and audit criteria.

GM-derived and cross-checked Reverse PFMEA materials explicitly list PFMEA, Control Plan, checklist and quality/problem evidence as inputs. citeturn0search0turn0search4

These are **not created by the Machine**. They belong to the surrounding risk-management / quality-system Assembly.

### 3.2 Preconditions

The Machine requires:

1. a station/process step selected for review;
2. a defined audit schedule;
3. a cross-functional team;
4. PFMEA and applicable checklist available at the station;
5. a safe way to perform any controlled station experiment.

GM material specifies cross-functional teams and a review schedule; experiments are supervised by maintenance to avoid damage to the station. citeturn0search0turn0search5

### 3.3 Roles inside the Machine

Core execution role:

- cross-functional review team: Quality / Production / Engineering / Maintenance etc.

Additional role:

- external auditor / “fresh eyes”, where used.

Safety/technical boundary role:

- maintenance engineer supervises station experiments.

The roles are execution resources of the Machine, while organizational appointment/authorization of those roles belongs outside the Machine.

## 4. Machine state sequence

The Machine can be decomposed into these operational states:

`S0 READY`
→ scheduled station and inputs available

`S1 REVIEWING FAILURE MODE`
→ one PFMEA failure mode is under examination

`S2 CONTROL EXISTENCE CHECK`
→ prevention/detection controls checked for presence / appropriateness

`S3 CONTROL EFFECTIVENESS CHECK`
→ actual control operation checked

`S4 RATING VALIDATION`
→ Occurrence / Detection values checked against actual evidence where applicable

`S5 NEXT FAILURE MODE`
→ continue through PFMEA failure modes

`S6 NEW FAILURE MODE DISCOVERY`
→ controlled attempt to create/find potential failure modes not represented in PFMEA

`S7 FINDINGS / ACTION PLAN`
→ findings and required tasks documented with responsibility and timing

`S8 HANDOFF / CLOSE`
→ results passed to downstream PFMEA / process-improvement / control-document update mechanisms.

The GM flow explicitly checks each failure mode, control existence, control effectiveness, rating accuracy/consistency, then searches for new potential failure modes and documents findings/tasks. citeturn0search0turn0search4

## 5. Core actions of the Machine

### A1 — Select / enter scheduled station

Input: scheduled station + PFMEA + checklist.

Output: active review context.

### A2 — Enumerate PFMEA failure modes

Input: PFMEA.

Output: ordered set of failure modes to review.

### A3 — Verify control existence

Question:

`Does the failure mode have proper prevention/detection controls?`

Output:

- control confirmed;
- control gap / finding.

### A4 — Verify control effectiveness

Question:

`Are the controls working properly?`

Output:

- effectiveness confirmed;
- effectiveness gap / finding.

### A5 — Validate Occurrence / Detection

Where applicable, compare ratings with actual station evidence/data.

Output:

- rating supported;
- rating requires reassessment.

The GM material explicitly describes validation of Occurrence and Detection ratings based on real data. citeturn0search0turn0search5

### A6 — Discover new failure modes

After existing PFMEA failure modes are verified, conduct controlled station experiments to attempt to reveal potential failure modes not included in the PFMEA.

Examples in GM material include mixing similar components or assembling parts inverted. citeturn0search1turn0search4

Output:

- no new potential FM found;
- new potential FM candidate(s).

### A7 — Record findings / action plan

Findings are converted into documented tasks, with champion/owner and timing.

Output:

- finding record;
- action plan;
- responsibility;
- due date.

GM explicitly requires findings to be documented in an action plan after the audit. citeturn0search1

## 6. Evidence generated by the Machine

The Machine produces evidence at several levels:

| Evidence | What it establishes |
|---|---|
| station observation | actual process state |
| control presence check | whether expected control exists |
| control operation check | whether control works |
| audit/checklist result | structured finding |
| experiment result | whether a potential new FM can be induced/observed |
| rating evidence | support for Occurrence / Detection assessment |
| finding/action record | traceable output for follow-up |

Important boundary: **the Machine produces evidence and findings; it does not by itself guarantee that all downstream corrective actions are implemented.**

## 7. Decision points

The Machine contains local decisions:

1. proper controls present?
2. controls working?
3. Occurrence / Detection values accurate and consistent?
4. all PFMEA failure modes verified?
5. new potential failure modes found?

These decisions determine the next state and output of the Machine.

The Machine does **not** own the broader organizational decision of whether a resulting PFMEA/process change is authorized. That belongs to the surrounding Assembly / change-management mechanism.

## 8. Outputs

### Direct outputs owned by the Machine

- verified review results;
- findings;
- identified control gaps;
- identified potential new failure modes;
- rating-validation observations;
- action-plan items with owner/champion and timing.

### Downstream outputs, not owned by the Machine

Potential subsequent changes to:

- Process Flow;
- PFMEA;
- Control Plan;
- Work Instructions;
- process controls;
- risk ratings.

GM supplier-audit material explicitly expects Reverse PFMEA findings to be driven back into Process Flow, PFMEA, Control Plan and Work Instructions as applicable. citeturn0search19turn0search22

This is a crucial boundary: **Reverse PFMEA discovers and structures the evidence; the surrounding risk-management Assembly performs and controls the resulting updates.**

## 9. Machine vs surrounding Assembly

| Element | Reverse PFMEA Machine | Surrounding Assembly |
|---|---|---|
| PFMEA | consumes | owns/maintains |
| Control Plan | consumes | owns/maintains |
| Audit schedule | executes scheduled review | establishes/prioritizes schedule |
| Cross-functional team | uses | appoints/organizes |
| Station observation | **performs** | — |
| Control existence verification | **performs** | — |
| Control effectiveness verification | **performs** | — |
| Rating validation | **performs / supplies evidence** | decides/updates risk model |
| New FM experiment | **performs under safe conditions** | — |
| Findings | **produces** | receives |
| Action plan | **creates/records findings and tasks** | owns completion / escalation |
| PFMEA update | supplies evidence/trigger | **performs/authorizes update** |
| Control Plan update | supplies evidence/trigger | **performs/authorizes update** |
| Work Instruction update | supplies evidence/trigger | **performs/authorizes update** |
| Effectiveness of resulting change | supplies later evidence when re-run | owns broader closure loop |

## 10. Pattern mapping

The Reverse PFMEA Machine realizes the broader Pattern as:

`PFMEA / EXPECTED CONTROLS`
→ `ACTUAL STATION`
→ `OBSERVATION / TEST`
→ `CONTROL GAP / NEW FM / RATING EVIDENCE`
→ `FINDING / ACTION PLAN`
→ `DOWNSTREAM ACTION`
→ `RE-VERIFICATION`
→ `PFMEA / CONTROL MODEL UPDATE`

But the Machine boundary ends before full organizational closure.

Therefore:

> **Reverse PFMEA is not the whole Risk Model Feedback Loop. It is a specialized diagnostic-verification Machine that supplies the evidence and findings needed to drive the wider feedback Assembly.**

This boundary is consistent with the GM flow: Reverse PFMEA reviews and finds gaps/new failure modes; findings are then driven back into the relevant process/risk documents. citeturn0search19turn0search22

## 11. Machine Passport implications

The decomposition suggests that a CMOC Machine Passport should distinguish at least:

1. **Supplied Context** — what the Machine consumes but does not own;
2. **Preconditions** — what must exist before execution;
3. **Execution Roles** — who performs the Machine;
4. **State Machine** — operational states and transitions;
5. **Core Actions** — actions owned by the Machine;
6. **Evidence** — what the Machine produces as proof/observation;
7. **Decision Points** — local decisions inside the Machine;
8. **Direct Outputs** — outputs owned by the Machine;
9. **Downstream Effects** — what another Machine/Assembly must perform;
10. **Boundary / Non-ownership** — what the Machine explicitly does not own;
11. **Pattern Realization** — which Pattern grammar it instantiates;
12. **Closure Condition** — what counts as completion of the Machine itself.

This is a proposed passport refinement, not yet a change to the canonical Machine Passport schema.

## 12. Decomposition result

**Pattern → Machine decomposition: PASS.**

The Pattern remains broader than Reverse PFMEA.

Reverse PFMEA has a recognizable autonomous execution boundary:

`SCHEDULE → STATION → REVIEW → VERIFY CONTROLS → TEST / DISCOVER → RECORD FINDINGS → HANDOFF`

The downstream risk-model update is external to the Machine.

Therefore the current architectural interpretation is:

`PATTERN`

`Risk Model Feedback Loop`

↓

`MACHINE`

`Reverse PFMEA`

↓

`ASSEMBLY`

`Risk Reduction / PFMEA Management`

where the Assembly closes the larger loop by applying, verifying and incorporating the resulting changes.

## 13. Status

- Pattern: `STRONG PATTERN CANDIDATE`
- Reverse PFMEA: `MACHINE CANDIDATE`
- Decomposition: `PASS`
- Machine boundary: `DEFINED`
- Passport implication: `PROPOSED`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

## 14. Next verification

Следующий тест: **Machine Independence Test**.

Нужно проверить, сохраняет ли Reverse PFMEA свою Machine identity, если убрать PFMEA/RPN терминологию и заменить её на другой domain representation:

`EXPECTED FAILURE/CONTROL STATE → ACTUAL STATION → EVIDENCE → GAP → FINDING → ACTION → VERIFY`

Если структура сохраняется, это усилит Machine abstraction. Если нет — граница Machine окажется domain-bound и это тоже будет полезным результатом.
