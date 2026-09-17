# GM Machine Passport v0.1 — Trial on GM-096 Candidates

**Notice:** 0151+170926  
**Source:** GM Quality System Basics Overview Supplier Audit — GM-096 Managing Change  
**Purpose:** контрольный прогон рабочего Machine Passport v0.1 на нескольких реальных кандидатах из одного доменного блока.

---

## 1. Test hypothesis

Passport v0.1 должен позволять описывать разные Machine candidates как воспроизводимые bounded execution units, не превращая паспорт:

- в фиксированный список компонентов;
- в паспорт Assembly;
- в SOP / рабочую инструкцию;
- в описание всего жизненного цикла изменения.

Тестируем четыре кандидата GM-096:

1. Plant Process Change Control (PPCR);
2. Production Trial Run (PTR);
3. Banking Process;
4. Bypass Process Control.

Это не утверждение, что все четыре уже являются Machines. В рамках теста они рассматриваются как **Machine Candidates** и проверяются паспортом.

---

## 2. Passport v0.1 under test

```yaml
identity:
  name:
  identity_bearing_relation_or_mode:
  local_capability:
  closure_condition:

execution:
  trigger:
  inputs:
  preconditions:
  execution_boundary:
  states_actions:
  evidence:
  decision_logic:
  outputs:

realization:
  domain:
  internal_mechanisms:
  roles:
  artifacts:
  downstream_ownership:

relations:
  pattern:
  invokes:
  feeds:

provenance:
  source:
  status:
```

---

# 3. Trial A — Plant Process Change Control

### Working identity

**Candidate:** Plant Process Change Control (PPCR)  
**Class under test:** MACHINE CANDIDATE

### Identity-bearing relation / mode

Управляемое прохождение предлагаемого изменения производственного процесса через оценку, согласование/авторизацию и определение необходимых последующих действий до разрешённого состояния изменения.

### Local capability

Не допустить неуправляемого изменения производственного процесса: определить допустимость изменения, необходимые условия/проверки и ответственное решение о переходе.

### Closure condition

Изменение получило разрешённый статус и определён следующий обязательный путь (trial, implementation, additional verification, rejection/cancel или иной установленный downstream path).

### Execution

**Trigger:** предложение/необходимость изменения процесса.

**Inputs:** описание изменения, затрагиваемый процесс/продукт, причины, риски, требования, необходимые участники и исходные данные.

**Preconditions:** изменение идентифицировано; доступны требуемые данные и ответственные лица.

**Execution boundary:** от идентифицированного предложения изменения до локального управленческого решения о допустимости и маршруте дальнейшего перехода.

**States/actions:** identify → assess impact/risk → determine requirements → review → authorize/reject → define downstream path.

**Evidence:** запись изменения, оценка воздействия/риска, согласования, решение/статус, назначенные последующие действия.

**Decision logic:** change acceptable/authorized? trial required? additional controls/verification required? reject/cancel?

**Outputs:** authorized/rejected change state; defined downstream path; required controls/actions.

### Realization

**Domain:** production process change.  
**Internal mechanisms:** review, risk/impact assessment, authorization, routing.  
**Roles:** change proposer, responsible functions, approver/authority.  
**Artifacts:** change record and associated evaluation/approval records.  
**Downstream ownership:** PTR, implementation, verification and return to normal state are not automatically owned by PPCR.

### Relations

**Pattern:** Managed Transition — likely realization; keep mapping provisional.  
**Invokes:** assessment/review mechanisms.  
**Feeds:** PTR or direct implementation/verification path.

### Passport result

**PASS WITH QUALIFICATION.** Passport captures the candidate cleanly, but a boundary question remains: whether PPCR is itself a Machine or an authorization mechanism inside the broader Managed Transition Assembly. The passport does not force a premature answer.

---

# 4. Trial B — Production Trial Run

### Working identity

**Candidate:** Production Trial Run (PTR)  
**Class under test:** MACHINE CANDIDATE

### Identity-bearing relation / mode

Контролируемое пробное выполнение изменённого/нового процесса с целью получить evidence, достаточное для принятия решения о пригодности и переходе дальше.

### Local capability

Получить проверяемое свидетельство того, что изменённый процесс может быть выполнен в контролируемых условиях и дать основание для решения о дальнейшем переходе.

### Closure condition

Trial completed and evidence evaluated, resulting in accepted/rejected/conditional outcome and explicit downstream disposition.

### Execution

**Trigger:** решение/условие, при котором требуется production trial.

**Inputs:** approved change, trial conditions, product/process requirements, evaluation criteria, resources.

**Preconditions:** trial authorized; conditions defined; responsible personnel/resources available.

**Execution boundary:** от запуска контролируемого trial до получения и оценки trial result.

**States/actions:** prepare → execute trial → observe/measure → collect evidence → evaluate → accept/reject/conditional.

**Evidence:** trial records, measurements, inspection/test results, deviations/findings, evaluation record.

**Decision logic:** result meets criteria? additional trial/action required? accept or reject?

**Outputs:** trial result, evidence package, acceptance/rejection/conditional decision, downstream actions.

### Realization

**Domain:** production process qualification/change implementation.  
**Internal mechanisms:** controlled execution, measurement/observation, evaluation, disposition.  
**Roles:** trial owner, production, quality/engineering/evaluation functions.  
**Artifacts:** trial plan/record and evidence.  
**Downstream ownership:** full change implementation, stabilization and final system closure remain outside the local trial boundary.

### Relations

**Pattern:** Managed Transition — provisional.  
**Invokes:** measurement/verification mechanisms.  
**Feeds:** implementation or return/rework path.

### Passport result

**PASS.** The Passport distinguishes the bounded trial from the broader change Assembly and does not need to enumerate every downstream implementation activity.

---

# 5. Trial C — Banking Process

### Working identity

**Candidate:** Banking Process  
**Class under test:** MACHINE CANDIDATE

### Identity-bearing relation / mode

Выделение и контролируемое удержание материала/продукции, которая не должна продолжать обычный поток, с сохранением идентичности, статуса и условий последующего решения.

### Local capability

Не допустить смешения/непреднамеренного использования материала вне нормального потока и сохранить управляемое состояние до disposition/release/rework/scrap/return.

### Closure condition

Материал получил разрешённое конечное disposition и покинул банковское состояние контролируемым образом.

### Execution

**Trigger:** материал выходит из нормального потока или временно не может быть обработан штатным образом.

**Inputs:** material/product, reason/status, identification, applicable disposition requirements.

**Preconditions:** material identifiable; banking location/status defined; responsible ownership established.

**Execution boundary:** от помещения материала в контролируемое банковское состояние до authorized disposition/release.

**States/actions:** identify → segregate/hold → label/status → protect/control → review/disposition → release/remove from bank.

**Evidence:** identification, location/status record, disposition decision, release record.

**Decision logic:** remain banked? rework? scrap? return? release? additional review?

**Outputs:** controlled banked state; traceable disposition; released/removed material.

### Realization

**Domain:** production material/product control.  
**Internal mechanisms:** segregation, identification, status control, disposition.  
**Roles:** material owner, quality/production, disposition authority.  
**Artifacts:** labels/status records/disposition records.  
**Downstream ownership:** root-cause/problem-solving or process change is downstream.

### Relations

**Pattern:** Managed Transition — provisional; alternative Pattern mapping remains open.  
**Invokes:** nonconforming-product/disposition mechanisms.  
**Feeds:** rework, scrap, return, release or other disposition path.

### Passport result

**PASS.** Strong evidence that Passport can represent a Machine whose identity is a **controlled state transition / containment boundary**, rather than an assessment or signal.

---

# 6. Trial D — Bypass Process Control

### Working identity

**Candidate:** Bypass Process Control  
**Class under test:** MACHINE CANDIDATE

### Identity-bearing relation / mode

Временное разрешённое функционирование при недоступности штатного процесса через специально определённый альтернативный путь с дополнительными ограничениями, контролем и подтверждением возврата к штатному режиму.

### Local capability

Сохранить управляемость результата при временной недоступности штатного процесса, не позволяя временной альтернативе превратиться в неуправляемую норму.

### Closure condition

Штатный процесс восстановлен и возврат к нему подтверждён; bypass закрыт и его состояние/результаты зафиксированы.

### Execution

**Trigger:** штатный процесс/контроль временно недоступен.

**Inputs:** failed/unavailable process, defined alternate method, restrictions, risk assessment, responsible authority.

**Preconditions:** bypass authorized; alternate controls defined; affected material/process identified; additional verification available.

**Execution boundary:** от разрешения временного bypass до подтверждённого возврата к нормальному процессу.

**States/actions:** identify loss of normal control → authorize bypass → define temporary controls → operate under bypass → monitor/review → restore normal process → verify return → close bypass.

**Evidence:** bypass record, authorization, temporary-control records, monitoring/LPA/Fast Response evidence where applicable, return-to-normal verification.

**Decision logic:** bypass permitted? controls adequate? continue? escalate? normal process restored?

**Outputs:** controlled temporary state; evidence of control; verified return to normal.

### Realization

**Domain:** production process continuity/control.  
**Internal mechanisms:** authorization, temporary control, monitoring, escalation, return verification.  
**Roles:** process owner, quality, production, approving authority.  
**Artifacts:** bypass record, temporary-control record, verification/closure record.  
**Downstream ownership:** corrective action to restore/improve the normal process is outside the local bypass boundary.

### Relations

**Pattern:** Managed Transition — strong provisional mapping.  
**Invokes:** abnormality response, monitoring, verification.  
**Feeds:** normal process restoration / corrective action.

### Passport result

**PASS.** Passport captures the candidate as a bounded temporary-state machine without absorbing the broader corrective-action system.

---

# 7. Cross-machine comparison

| Passport field | PPCR | PTR | Banking | Bypass |
|---|---|---|---|---|
| Identity-bearing relation/mode | authorization/routing of change | controlled trial | controlled hold/disposition | controlled temporary alternative |
| Local capability | authorize/manage change path | produce trial evidence | preserve control of held material | preserve control during loss of normal process |
| Closure | authorized disposition/path | evaluated trial result | authorized disposition | verified return to normal |
| Trigger | proposed change | trial required | material leaves normal flow | normal process unavailable |
| Execution boundary | change proposal → route/decision | trial start → evaluated result | bank entry → disposition | bypass activation → verified return |
| Evidence | decision/assessment records | trial evidence | status/disposition evidence | bypass/return evidence |
| Decision logic | authorization/path | accept/reject/conditional | disposition | continue/escalate/return |
| Internal mechanisms | review + assessment + authorization | controlled execution + evaluation | segregation + status + disposition | authorization + temporary control + verification |
| Downstream ownership | implementation/verification | implementation/stabilization | rework/problem solving | restoration/corrective action |
| Passport fit | PASS WITH QUALIFICATION | PASS | PASS | PASS |

---

# 8. What the trial reveals about Passport v0.1

## 8.1 Fields that survived all four candidates

The following appear structurally useful across the sample:

- identity-bearing relation/mode;
- local capability;
- closure condition;
- trigger;
- inputs/context;
- preconditions;
- execution boundary;
- states/actions;
- evidence;
- decision logic;
- outputs;
- domain;
- internal mechanisms;
- roles;
- artifacts;
- downstream ownership;
- provenance/status.

## 8.2 Fields that need qualification

### `pattern`
Can remain `HOLD` without damaging the Passport. This is important: Pattern identification is not a prerequisite for Machine identity.

### `invokes` / `feeds`
Useful for graph integration, but they describe relations around the Machine rather than identity. They should not be required for initial Machine recognition.

### `decision_logic`
Some Machines have explicit gates; others contain more distributed or conditional decisions. The field remains valid, but `N/A` or `distributed` must be allowed.

### `artifacts`
All four use records/records-like artifacts, but the artifact vocabulary differs. Keep the field, allow `N/A`.

### `internal_mechanisms`
Useful and necessary for realization, but the trial confirms that this field must remain **non-identity-bearing**.

---

# 9. Assembly duplication test

Passport does **not** need to reproduce the entire Assembly.

Observed boundary:

- PPCR ends at authorized route/decision;
- PTR ends at evaluated trial result;
- Banking ends at controlled disposition;
- Bypass ends at verified return to normal.

Downstream chains may be larger:

`PPCR → PTR → Implementation → Verification → Normal`

or

`Abnormality → Bypass → Verification → Restoration → Corrective Action`.

These chains are Assembly territory. Passport records the bounded execution unit that participates in the chain.

**Result: PASS.**

---

# 10. SOP duplication test

Passport describes:

- what the Machine is;
- where its boundary lies;
- what triggers it;
- what transformation it performs;
- what evidence and decision logic are intrinsic;
- what local result closes it.

Passport does **not** prescribe:

- exact enterprise work instructions;
- every operator step;
- every form field;
- exact timing/frequency unless identity depends on it;
- local organizational details not required for Machine identity.

**Result: PASS.**

Therefore Passport remains an ontological/architectural description, not an SOP.

---

# 11. N/A test

The trial did not reveal a field that is universally unnecessary.

It did reveal that several fields must explicitly support `N/A` / `HOLD` / `distributed` rather than forcing invented content:

- pattern;
- invokes;
- feeds;
- decision logic in distributed cases;
- artifacts where the Machine can operate without a dedicated artifact.

This is not a defect of the Passport. It is evidence that a universal schema must distinguish **required field** from **required value**.

---

# 12. Architectural finding

The trial strengthens the working rule:

> **Passport describes the invariant identity and bounded execution of a Machine; it does not describe the whole Assembly and does not prescribe the SOP.**

And a second rule becomes visible:

> **A Passport field may be structurally required even when its value for a particular Machine is N/A, HOLD, or distributed.**

This is an important distinction between schema completeness and instance completeness.

---

# 13. Status

- Machine Passport v0.1 trial: **PASS**
- Four GM-096 candidates tested: **PASS / PASS WITH QUALIFICATION**
- Identity core: **STABLE WORKING**
- Execution core: **STABLE WORKING**
- Realization layer: **STABLE WORKING**
- Internal mechanisms as non-identity: **CONFIRMED**
- Pattern as optional/HOLD: **CONFIRMED**
- Downstream ownership as boundary field: **CONFIRMED**
- Assembly duplication: **PASS**
- SOP duplication: **PASS**
- N/A handling: **REQUIRES EXPLICIT SCHEMA SUPPORT**
- Canon: **NON-CANON**

## No changes

No changes to:

- Machine Catalog;
- Canon;
- REG-001.

## Next methodological step

Do **not** canonize Passport v0.1 yet.

Next step: **Passport Schema CrossCheck** — test the schema against Machines from different Patterns/domains, especially Machines whose identity is not a transition of material/change state. The purpose is to determine whether the current field structure is genuinely domain-independent or still biased toward GM-096-style control mechanisms.
