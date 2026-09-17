# GM Machine Passport v0.2 — Field Semantics Test

**Notice:** 0159+170926  
**Status:** PASS / NON-CANON  
**Purpose:** проверить смысловые границы полей Machine Passport v0.2 после Field Necessity Test и Schema Refactor Test.

## 1. Test hypothesis

Поле Passport должно иметь однозначную семантическую роль: описывать identity Machine, её bounded execution, realization, relation, validation или provenance. Поле не должно одновременно выполнять разные онтологические функции и не должно незаметно превращать Passport в Pattern, Assembly, SOP или классификатор.

Критерии:

1. поле отвечает на один основной архитектурный вопрос;
2. его смысл сохраняется для разных Machine;
3. его отсутствие/изменение не подменяет Machine другой сущностью;
4. поле не дублирует другое поле без явной причины;
5. допускается `N/A`, `HOLD` или `distributed`, если это соответствует природе Machine.

---

## 2. Semantic layers

### MACHINE CORE

- `identity.name` — рабочее имя/идентификатор, не доказательство Machine identity;
- `identity.machine_abstraction` — обобщённый класс/абстракция Machine; полезен для связывания Domain Machine с абстрактной Machine, но не обязателен для каждой реализации;
- `identity.identity_bearing_relation_or_mode` — что именно делает Machine узнаваемой как устойчивую bounded execution unit;
- `identity.local_capability` — локальный результат, который Machine способна воспроизводимо обеспечивать.

### EXECUTION CORE

- `trigger` — условие/событие/режим входа в execution;
- `inputs_context` — что Machine получает и в каком контексте;
- `preconditions` — что должно быть истинно до запуска;
- `execution_boundary` — где начинается и заканчивается именно эта Machine;
- `execution_sequence` — воспроизводимая последовательность исполнения;
- `evidence` — что делает execution/decision/result проверяемыми;
- `decision_points_logic` — локальная логика решений, если она intrinsic;
- `local_outputs` — непосредственный результат внутри собственной boundary;
- `closure_condition` — условие завершения именно этой Machine.

### REALIZATION

- `domain` — предметная область конкретной реализации;
- `internal_mechanisms` — из каких mechanisms фактически составлена реализация; не определяет identity;
- `roles` — кто выполняет/поддерживает execution;
- `artifacts` — используемые/создаваемые объекты;
- `domain_specific_conditions` — ограничения и условия конкретной реализации;
- `limitations` — границы применимости;
- `downstream_ownership` — кому принадлежат действия после local boundary.

### RELATIONS

- `pattern` — связь с Pattern; может оставаться `HOLD`;
- `invokes_uses` — используемые/вызываемые Machines или mechanisms;
- `feeds` — downstream Machines/Assemblies, получающие результат.

### VALIDATION

После предыдущего теста `machine_boundary_test` рассматривается как **validation apparatus**, а не как часть Machine identity.

Он проверяет:

```text
identity-bearing relation/mode
        +
own execution boundary
        +
local capability
        +
closure condition
        → Machine boundary PASS/FAIL
```

Значения validation не должны дублировать содержимое Machine Core без необходимости.

### PROVENANCE

- `source` — откуда взято описание;
- `evidence_reference` — где находится подтверждающее свидетельство;
- `status` — epistemic/lifecycle status кандидата.

---

## 3. Critical semantic distinctions

### identity-bearing relation/mode ≠ execution_boundary

`identity-bearing relation/mode` отвечает: **почему это именно эта Machine?**  
`execution_boundary` отвечает: **где начинается и заканчивается её исполнение?**

PASS — поля различимы и оба необходимы.

### local_capability ≠ local_outputs

`local_capability` — устойчивое утверждение о способности Machine.  
`local_outputs` — конкретный результат данного execution.

PASS — capability не сводится к списку outputs.

### closure_condition ≠ downstream_ownership

`closure_condition` — когда Machine локально завершена.  
`downstream_ownership` — кто владеет последующим действием.

PASS — handoff не равен closure, хотя closure может быть handoff-type.

### execution_boundary ≠ closure_condition

Boundary — пространственно/логическая граница execution.  
Closure — условие его завершения.

PASS — различение сохраняется на Gemba, Andon, Verification и PTR.

### internal_mechanisms ≠ Machine identity

Одна и та же Machine может реализовываться различными механизмами. Изменение внутреннего состава не обязательно меняет Machine identity.

PASS.

### feeds ≠ closure

`feeds` описывает relation наружу. Machine может завершиться до downstream execution или иметь downstream continuation как часть Assembly.

PASS.

---

## 4. Four-machine semantic trial

### A. Andon

Identity-bearing relation/mode: abnormality → signal → responsible response.

Boundary: activation of abnormality response through resolution or accepted escalation.

Capability: make abnormality visible and transfer it into managed response.

Closure: resolution / accepted escalation.

Semantic result: PASS.

### B. Gemba Walk

Identity-bearing relation/mode: direct presence at actual place → observation/understanding → finding.

Boundary: access to actual place through traceable finding/handoff.

Capability: obtain direct knowledge of actual work and produce traceable finding.

Closure: finding/handoff.

Semantic result: PASS.

### C. Expected-vs-Actual Control Verification

Identity-bearing relation/mode: accepted expected state ↔ realized state comparison.

Boundary: evidence generation through verified comparison result.

Capability: detect discrepancy and produce verified finding for response/re-verification.

Closure: verification result.

Semantic result: PASS.

### D. Production Trial Run

Identity-bearing relation/mode: controlled trial execution → evaluated trial result.

Boundary: trial start through evaluated result.

Capability: obtain bounded evidence about whether a proposed process/product state can be accepted.

Closure: evaluated result / decision input.

Semantic result: PASS.

---

## 5. Boundary cases

### Pattern

`pattern` cannot substitute for Machine identity. A Pattern is grammar of composition, not a bounded execution instance.

Result: PASS separation.

### Assembly

`feeds` and `downstream_ownership` must not make the Passport describe the entire Assembly. Passport ends at Machine boundary; broader orchestration remains Assembly territory.

Result: PASS.

### SOP

`execution_sequence` describes architecture of reproducible execution, not operator-level instructions, parameters or every procedural detail.

Result: PASS.

### Validation record

Validation evidence can prove Machine boundary, but evidence of validation is not itself Machine identity.

Result: PASS.

---

## 6. Schema implication

Working semantic structure:

```yaml
machine_passport:
  identity:
    name:
    machine_abstraction:
    identity_bearing_relation_or_mode:
    local_capability:

  execution:
    trigger:
    inputs_context:
    preconditions:
    execution_boundary:
    execution_sequence:
    evidence:
    decision_points_logic:
    local_outputs:
    closure_condition:

  realization:
    domain:
    internal_mechanisms:
    roles:
    artifacts:
    domain_specific_conditions:
    limitations:
    downstream_ownership:

  relations:
    pattern:
    invokes_uses:
    feeds:

  validation:
    machine_boundary_test:
    result:

  provenance:
    source:
    evidence_reference:
    status:
```

`machine_boundary_test` здесь является validation data и не должен повторять identity-поля как второй источник истины. В рабочей реализации он может ссылаться на соответствующие поля Passport и фиксировать только применённый тест, evidence и result.

---

## 7. Result

**PASS.**

Семантические границы полей устойчивы на четырёх разных Machine:

- signal-to-response;
- direct-access-to-reality;
- expected-vs-actual comparison;
- bounded trial.

Подтверждено:

- Machine Core не смешивается с Validation;
- identity не смешивается с realization;
- boundary не смешивается с closure;
- capability не смешивается с output;
- local closure не смешивается с downstream ownership;
- internal mechanisms не являются identity;
- relations не превращают Passport в Assembly;
- execution sequence не превращает Passport в SOP.

## 8. Status

- Machine Passport v0.2: **WORKING CANDIDATE**
- Field semantics: **DEFINED / PASS**
- Machine Core: **DEFINED**
- Execution Core: **DEFINED**
- Realization Layer: **DEFINED**
- Relations Layer: **DEFINED**
- Validation Layer: **DEFINED**
- Provenance Layer: **DEFINED**
- Canon: **NON-CANON**
- Machine Catalog: **NO CHANGE**
- Canon: **NO CHANGE**
- REG-001: **NO CHANGE**

## 9. Next methodological step

Провести **Machine Passport v0.2 Minimal Instance Test**: собрать минимально заполненный Passport для нескольких Machine и проверить, сохраняется ли различимость Machine без лишних полей и без скрытого переноса информации из одного поля в другое.
