# GM QSB — Machine Passport v0.2 Adversarial Test

**Notice:** 0156+170926  
**Status:** TEST PATCH / NON-CANON

## 1. Purpose

Проверить consolidated Machine Passport v0.2 на пограничных объектах, которые особенно легко принять за Machine:

- Audit;
- Problem Solving;
- Knowledge Transfer / Yokoten;
- Visual Control;
- Assembly.

Цель — попытаться сломать схему и проверить нижнюю границу:

```text
MECHANISM ↔ MACHINE ↔ ASSEMBLY
```

## 2. Adversarial rule

Кандидат считается прошедшим как Machine только если Passport позволяет независимо доказать:

```text
identity-bearing relation / mode
        +
own execution boundary
        +
local capability
        +
closure
```

Заполнение всех остальных полей не является доказательством Machine identity.

## 3. Candidate A — Audit

Audit — сильный adversarial case, поскольку имеет:

- trigger / schedule;
- criteria;
- evidence;
- comparison;
- findings;
- report;
- sometimes corrective-action follow-up.

### Identity

`OBJECT / CRITERION → EVIDENCE → EVALUATION → FINDING`

### Boundary

Audit может иметь собственную bounded execution от scope/criteria до evaluated findings/report.

### Local capability

Produce an independent/defined assessment result against specified criteria.

### Closure

`result / assessment report / findings issued`

Corrective action and effectiveness verification могут быть downstream.

### Adversarial conclusion

Audit **проходит как Machine candidate**, если рассматривается как bounded assessment execution, а не как generic document/checklist.

Это важно: предыдущий Boundary Test не говорил, что любой assessment artifact не может быть частью Machine; здесь evidence + evaluation + bounded assessment form own execution relation.

**Result: PASS — Machine candidate.**

## 4. Candidate B — Problem Solving

Problem Solving имеет:

`PROBLEM → CONTAIN → INVESTIGATE → ROOT CAUSE → CORRECTIVE ACTION → VERIFY`

### Identity

`PROBLEM → CAUSE → EFFECTIVE ACTION`

### Boundary

Может быть определена от принятия проблемы до verified result.

### Local capability

Identify and address causal mechanism sufficiently to prevent recurrence within defined scope.

### Closure

`verification / effective result / accepted disposition`

### Adversarial issue

Problem Solving может легко поглотить downstream corrective action, change implementation и lessons learned.

Но Passport требует отделить bounded Problem Solving execution от более крупной Assembly.

### Conclusion

**Result: PASS — Machine candidate, provided boundary is explicitly limited to its own problem-solving execution.**

Не следует автоматически включать в него всю Corrective Action Assembly.

## 5. Candidate C — Knowledge Transfer / Yokoten

Это особенно важный adversarial case, поскольку здесь нет обязательного material/state transition.

### Identity

`VALIDATED KNOWLEDGE → SELECTED RECIPIENT / TARGET → TRANSFER → UNDERSTANDING / AVAILABILITY CONFIRMED`

### Boundary

От выбора transferable knowledge и recipient до подтверждённой передачи.

### Local capability

Make validated knowledge available and transferable to another relevant context/person/process.

### Closure

`transfer result / recipient confirmation / knowledge made available`

### Problem

Если определить Yokoten только как `share information`, получается mechanism.

Если появляется bounded execution с собственной identity, recipient, transfer verification и closure, возникает Machine boundary.

### Conclusion

`Knowledge Transfer` может быть Machine abstraction.

Конкретный Yokoten может быть domain realization.

**Result: PASS WITH QUALIFICATION.**

Условие: простая публикация/запись информации без bounded transfer verification остаётся artifact/mechanism.

## 6. Candidate D — Visual Control

Visual Control:

`RELEVANT STATE / EXPECTATION → VISUAL REPRESENTATION → HUMANLY ACCESSIBLE STATUS`

### Identity

`STATE / EXPECTATION → VISIBILITY`

### Boundary

Потенциальная bounded execution — обеспечить воспроизводимое преобразование relevant state в immediately accessible visual status.

### Local capability

Make relevant condition/status visible for rapid human recognition.

### Closure

Здесь adversarial проблема наиболее сильна.

Если Visual Control означает только static board/sign/label, это artifact.

Если существует bounded mechanism, который:

- получает relevant state;
- обновляет representation;
- обеспечивает актуальность;
- устанавливает condition of valid visibility;

то появляется кандидат на Machine.

### Conclusion

Generic `Visual Control` **не должен автоматически считаться Machine**.

Static visual artifact = `FAIL`.

Bounded visual-status execution with own update/validity boundary = `Machine candidate`.

**Result: PASS AS BOUNDARY-SENSITIVE CANDIDATE.**

## 7. Candidate E — Assembly

Assembly специально используется как adversarial upper-bound test.

Пример:

```text
GEMBA
  ↓
AUDIT / VERIFICATION
  ↓
ANDON
  ↓
PROBLEM SOLVING
  ↓
CORRECTIVE ACTION
  ↓
VERIFY
  ↓
CLOSE
```

### Что произойдёт при попытке заполнить Machine Passport

Все поля можно заполнить.

Есть:

- trigger;
- inputs;
- execution sequence;
- evidence;
- decisions;
- outputs;
- capability;
- closure.

Но возникает критическое противоречие:

`identity-bearing relation` Assembly не совпадает с identity-bearing relation каждой внутренней Machine.

Вместо одной bounded invariant execution relation появляется orchestration/composition нескольких Machines.

### Boundary

Assembly имеет собственную boundary, но она является boundary **composition**, а не bounded execution одной Machine.

### Capability

Assembly может иметь broader capability, не сводимую к local capability одной Machine.

### Closure

Assembly closure может включать закрытие нескольких downstream Machines.

### Conclusion

**Result: FAIL AS MACHINE / PASS AS ASSEMBLY.**

Это ключевой upper-bound test.

## 8. Mechanism ↔ Machine ↔ Assembly triangle

| Object | Own invariant relation/mode | Own bounded execution | Local capability | Closure | Classification |
|---|---|---:|---:|---:|---|
| Checklist | No | No | No | No | Artifact |
| Measurement | Mechanism relation | Local operation | Mechanism-level | Operation completion | Mechanism |
| Audit | Assessment relation | Yes | Assessment result | Result | Machine candidate |
| Problem Solving | Problem→cause→action | Yes | Problem resolution | Verification | Machine candidate |
| Knowledge Transfer | Transfer relation | Yes, if bounded | Transfer capability | Transfer confirmed | Machine candidate / qualified |
| Visual artifact | Representation | No | No | No | Artifact |
| Visual Control realization | State→visibility | Possibly | Visibility | Valid visibility | Machine candidate / boundary-sensitive |
| Assembly | Composition relation | Yes, as composition | Broader capability | Assembly closure | Assembly, not Machine |

## 9. Critical adversarial finding

Adversarial testing не показывает, что граница:

```text
Machine = small
Assembly = large
```

Это неверно.

Правильнее:

```text
Machine
= bounded invariant execution unit

Assembly
= bounded composition / orchestration of Machines and mechanisms
```

Assembly может быть меньше или проще некоторой Machine по количеству действий, но это не меняет ontological distinction.

## 10. New negative test — “well-described process”

Проверка:

> Если любой процесс можно полностью описать Passport, станет ли любой процесс Machine?

**Answer: NO.**

Passport completeness ≠ Machine identity.

Для generic process необходимо сначала установить, что процесс имеет собственную invariant execution relation/mode, local capability и closure.

Если процесс лишь представляет контекст, организационную форму или composition of independent Machines, он не становится Machine автоматически.

## 11. New negative test — “same Passport, different identity”

Два объекта могут иметь одинаковую структуру полей:

```text
trigger
inputs
actions
evidence
output
closure
```

но быть разными ontological classes:

```text
Machine
Assembly
Mechanism
Artifact-supported process
```

Следовательно, Passport — descriptive schema, а не classifier по количеству заполненных полей.

## 12. New positive test — Machine with no material transition

Положительные кандидаты:

- Gemba Walk;
- Audit;
- Knowledge Transfer.

Ни один из них не требует material state transition.

Следовательно:

> Machine ontology не должна быть основана на физическом преобразовании объекта.

Её основа — bounded executable relation/mode + capability + closure.

## 13. Schema stress result

Все ключевые поля v0.2 выдержали adversarial test.

Особенно устойчивыми оказались:

- `identity_bearing_relation_or_mode`;
- `machine_boundary_test`;
- `local_capability`;
- `closure_condition`;
- `execution_boundary`;
- `local_outputs`;
- `downstream_ownership`.

Поле `execution_sequence` не создаёт state-transition bias.

Поле `inputs_context` не требует artifact input.

`closure_condition` не требует return-to-normal.

`pattern` остаётся optional/HOLD.

## 14. Strengthened Machine criterion

После adversarial test рабочая формулировка уточняется:

> **Machine — bounded executable unit, реализующая invariant execution relation или invariant execution mode, обладающая собственной local capability и closure condition. Её identity определяется устойчивой boundary и способом воспроизводимого исполнения, а не перечнем компонентов, размером, количеством шагов, физическим преобразованием или названием практики.**

Assembly:

> **Assembly — bounded composition/orchestration of Machines and/or mechanisms, имеющая собственную broader capability и собственную boundary composition.**

Mechanism:

> **Mechanism — локальный способ действия/преобразования/получения результата, который сам по себе не обязан иметь самостоятельную Machine identity.**

## 15. Important qualification — Machine may be composite

Adversarial test не отменяет ранее установленное:

> Machine может состоять из нескольких mechanisms.

Различие:

```text
mechanisms compose
    ↓
если возникает собственная invariant relation + boundary + capability + closure
    ↓
Machine

Machines/mechanisms compose at larger scope
    ↓
Assembly
```

## 16. Status

- Passport v0.2 Adversarial Test: `PASS`
- Audit: `PASS — Machine candidate`
- Problem Solving: `PASS — Machine candidate`
- Knowledge Transfer / Yokoten: `PASS WITH QUALIFICATION`
- Visual Control: `PASS AS BOUNDARY-SENSITIVE CANDIDATE`
- Assembly: `FAIL AS MACHINE / PASS AS ASSEMBLY`
- Machine ↔ Assembly boundary: `STRENGTHENED`
- Mechanism ↔ Machine boundary: `STRENGTHENED`
- Machine without material transition: `CONFIRMED`
- Passport completeness ≠ Machine identity: `CONFIRMED`
- Passport schema v0.2: `SURVIVED ADVERSARIAL TEST`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

## 17. Next step

Следующий шаг — **Machine Passport v0.2 Field Necessity Test**: после того как schema выдержала позитивные, негативные и adversarial тесты, проверить каждое поле v0.2 на реальную необходимость и попытаться удалить поля по одному, чтобы увидеть, где теряется Machine identity, boundary, reproducibility или provenance.

Только после этого можно обсуждать переход к `v0.3` или к canonicalization.
