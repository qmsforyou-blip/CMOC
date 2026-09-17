# GM QSB — Machine Passport Test v0.1

**Notice:** 0150+170926  
**Status:** TEST PATCH / NON-CANON

## 1. Purpose

Проверить, какие поля Machine Passport действительно необходимы, чтобы зафиксировать:

- Machine identity;
- execution boundary;
- local capability;
- closure condition;
- internal composition;
- domain realization;
- downstream ownership;

не превращая Passport в фиксированный component list.

Тест опирается на результаты предыдущих проверок:

- Reverse PFMEA — Machine Independence;
- Reverse PFMEA — Machine Composition;
- Andon — Machine Atomicity / Composition;
- Gemba Walk — Machine Atomicity / Composition;
- Machine Boundary Triangle: Gemba / Expected-vs-Actual Verification / Andon.

Это не канонизация schema.

## 2. Test hypothesis

Machine Passport должен описывать не перечень компонентов, а воспроизводимую bounded execution.

Рабочее различение:

```text
IDENTITY
    ↓
BOUNDARY
    ↓
EXECUTION
    ↓
CAPABILITY
    ↓
REALIZATION
```

Ключевой принцип:

> Internal mechanisms describe how a Machine is realized; they do not by themselves define what the Machine is.

## 3. Candidate Passport layers

### Layer A — Identity

Минимальный набор:

- Machine ID / Name;
- Machine abstraction, если она выявлена;
- Domain realization;
- identity-bearing execution relation or execution mode;
- local capability;
- closure condition.

### Layer B — Execution

- trigger / entry condition;
- inputs / supplied context;
- preconditions;
- execution boundary;
- states / actions;
- evidence;
- decision logic;
- outputs.

### Layer C — Realization

- internal mechanisms / composition;
- roles;
- artifacts;
- downstream ownership;
- domain-specific conditions and limitations.

### Layer D — Ontological relations

- Pattern realized, if established;
- invokes / uses other mechanisms or Machines;
- feeds downstream Assembly;
- status / evidence / source.

## 4. Field-removal test

### 4.1 Machine identity / name

Удаление делает объект неидентифицируемым.

**Result: REQUIRED.**

### 4.2 Identity-bearing relation / mode

Без этого невозможно отличить соседние Machines при совпадении компонентов.

Examples:

- Gemba Walk — direct presence at actual place;
- Expected-vs-Actual Verification — comparison of realized state with accepted expected state;
- Andon — signal / visibility → responsible response.

**Result: REQUIRED.**

### 4.3 Local capability

Без capability непонятно, какой результат делает bounded execution самостоятельной.

**Result: REQUIRED.**

### 4.4 Execution boundary

Без boundary Machine растворяется в более крупной Assembly или процессе.

**Result: REQUIRED.**

### 4.5 Closure condition

Без closure невозможно определить, где bounded execution заканчивается.

**Result: REQUIRED.**

### 4.6 Trigger / entry condition

Без trigger теряется условие запуска и применимость Machine.

**Result: REQUIRED for a reproducible Passport.**

### 4.7 Inputs / supplied context

Без входной рамки execution нельзя воспроизвести или проверить применимость.

**Result: REQUIRED.**

### 4.8 States / actions

Без execution sequence остаётся только декларативное название capability.

**Result: REQUIRED.**

### 4.9 Evidence

Без evidence невозможно описать, на чём основано execution и decision.

**Result: REQUIRED.**

### 4.10 Decision logic

Без decision logic не видна управленческая граница Machine.

**Result: REQUIRED where decisions are intrinsic to the Machine; field may be explicit or marked N/A.**

### 4.11 Outputs

Без output невозможно установить непосредственный результат bounded execution.

**Result: REQUIRED.**

### 4.12 Internal mechanisms / composition

Удаление не разрушает Machine identity.

Andon остаётся Andon без перечисления display, signal, escalation mechanisms; Gemba Walk остаётся Gemba Walk без конкретного checklist/questioning format; Expected-vs-Actual Verification остаётся той же abstraction независимо от конкретного monitoring/audit/verification implementation.

**Result: REQUIRED as realization description, NOT an identity field.**

### 4.13 Roles

Удаление не разрушает Machine identity, но снижает воспроизводимость конкретной реализации.

**Result: REQUIRED for realization, NOT identity.**

### 4.14 Artifacts

Удаление не разрушает Machine identity, но ослабляет traceability.

**Result: REQUIRED for realization where artifacts are used; may be N/A.**

### 4.15 Downstream ownership

Удаление не разрушает identity, но стирает границу Machine ↔ downstream Assembly.

**Result: REQUIRED for boundary/ownership description.**

### 4.16 Pattern

Удаление не разрушает Machine identity.

Gemba Walk может иметь Pattern mapping `HOLD`, не переставая быть Machine candidate.

**Result: OPTIONAL / may be HOLD.**

### 4.17 Domain realization

Для domain-specific Machine отсутствие domain делает конкретную реализацию неясной; для abstraction-level Machine поле может быть multiple / N/A.

**Result: REQUIRED for domain realization; not universal identity requirement.**

## 5. Resulting minimum Passport core

Тест позволяет выделить минимальное ядро:

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

Это **working v0.1**, а не canonical schema.

## 6. Four-machine trial

### A. Reverse PFMEA

Identity-bearing relation:

`EXPECTED CONTROL → ACTUAL STATION → EVIDENCE → GAP / FINDING`

Domain realization:

PFMEA / production risk.

Internal composition:

station review, control existence check, effectiveness check, rating validation, controlled failure-mode discovery, finding/action handoff.

Downstream ownership:

PFMEA / Control Plan / Process Flow / Work Instruction updates и последующие изменения.

Passport core is fillable.

**Result: PASS.**

### B. Expected-vs-Actual Control Verification

Identity-bearing relation:

`ACCEPTED EXPECTED STATE ↔ REALIZED STATE → EVIDENCE → COMPARE → GAP → VERIFY`

Internal composition:

Monitoring + comparison/Audit + finding/handoff + verification.

Domain may be maintenance, production control, quality control or another domain.

**Result: PASS.**

### C. Andon

Identity-bearing relation:

`ABNORMALITY → SIGNAL / VISIBILITY → RESPONSIBLE RESPONSE → RESOLUTION / ESCALATION`

Internal composition:

trigger, signal, visual/audible indication, response initiation, optional escalation, resolution indication.

**Result: PASS.**

### D. Gemba Walk

Identity-bearing mode:

`DIRECT PRESENCE AT ACTUAL PLACE`

Execution:

`ACTUAL PLACE → DIRECT OBSERVATION → UNDERSTAND → FINDING → TRACEABLE HANDOFF`

Internal composition:

observation, questioning, contextual understanding, finding formation, recording/handoff, optional follow-up.

Pattern mapping remains `HOLD`.

**Result: PASS.**

## 7. Cross-machine result

The same Passport core accommodates Machines with different identity-bearing structures:

```text
Gemba Walk
identity = mode of access to reality

Expected-vs-Actual Verification
identity = comparison relation

Andon
identity = signal-to-response relation

Reverse PFMEA
identity = domain realization of expected-vs-actual control verification
```

Следовательно, Passport не должен требовать единственного типа identity definition.

## 8. What Passport must NOT become

Passport не должен превращаться в:

- fixed component checklist;
- обязательный одинаковый workflow для всех Machines;
- описание полного downstream Assembly;
- замену source evidence;
- Pattern definition;
- полный SOP конкретного предприятия.

Его функция — сохранить **онтологическую границу Machine** и достаточную информацию для воспроизведения/проверки её execution.

## 9. Architectural conclusion

### PASS

Passport Test подтверждает рабочее разделение:

```text
MACHINE PASSPORT

IDENTITY
  ├─ identity-bearing relation / mode
  ├─ local capability
  └─ closure

EXECUTION
  ├─ trigger
  ├─ input/context
  ├─ boundary
  ├─ states/actions
  ├─ evidence
  ├─ decisions
  └─ outputs

REALIZATION
  ├─ domain
  ├─ internal mechanisms
  ├─ roles
  ├─ artifacts
  └─ downstream ownership

RELATIONS / PROVENANCE
  ├─ pattern
  ├─ invokes / feeds
  ├─ source
  └─ status
```

Главный результат:

> **Machine Passport фиксирует identity и bounded execution; Internal Composition фиксирует способ реализации, но не определяет identity.**

И ещё одно важное следствие:

> **Pattern может быть неизвестен, а Machine Passport уже может быть полноценным.**

## 10. Status

- Passport Test: `PASS`
- Identity Core: `DEFINED`
- Execution Core: `DEFINED`
- Realization Layer: `DEFINED`
- Internal Composition as non-identity field: `CONFIRMED`
- Pattern as optional/HOLD: `CONFIRMED`
- Downstream Ownership as boundary field: `CONFIRMED`
- Four-machine trial: `PASS`
- Passport schema: `WORKING v0.1`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

## 11. Next step

Следующий шаг — не канонизация schema, а применение `Machine Passport v0.1` к нескольким реальным Machine candidates из GM QSB и проверка, какие поля систематически оказываются `N/A`, какие требуют уточнения и где Passport начинает дублировать Assembly или SOP.

Только после этого имеет смысл рассматривать отдельный `Passport Schema CrossCheck`.
