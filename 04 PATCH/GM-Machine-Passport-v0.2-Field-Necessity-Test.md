# GM Machine Passport v0.2 — Field Necessity Test

**Notice:** 0157+170926  
**Date:** 17-09-2026  
**Status:** WORKING / NON-CANON

## 1. Purpose

Проверить необходимость каждого поля рабочего `Machine Passport v0.2` и отделить:

1. поля, необходимые для **Machine identity**;
2. поля, необходимые для **bounded execution / reproducibility**;
3. поля, необходимые для **realization / boundary description**;
4. поля, необходимые для **provenance / lifecycle**;
5. поля, которые полезны, но не должны быть обязательными для каждого Machine.

Тест должен также проверить, не содержит ли схема дублирования между описанием Machine и аппаратом проверки того, что объект действительно является Machine.

---

## 2. Working schema under test

```yaml
machine_passport:
  identity:
    name:
    machine_abstraction:
    identity_bearing_relation_or_mode:
    local_capability:
    machine_boundary_test:
      identity_bearing_relation_or_mode:
      own_execution_boundary:
      local_capability:
      closure_condition:
      result:

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
    feeds

  provenance:
    source:
    evidence_reference:
    status:
```

---

## 3. Test rule

Для каждого поля задаётся вопрос:

> Если удалить это поле из Passport, что ломается — identity, boundary, reproducibility, realization, provenance — или ничего существенного?

Важно различать **структурную необходимость поля** и **обязательность конкретного значения**.

`N/A`, `HOLD` и `distributed` остаются допустимыми значениями там, где поле структурно необходимо, но не имеет единственного значения для конкретного Machine.

---

# 4. Identity layer

## 4.1 `identity.name`

**Удаление:** Machine identity как онтологическое различение не исчезает, если сохранены identity-bearing relation/mode, boundary, capability и closure.

**Результат:** НЕ identity-core.

Но Passport без имени практически теряет удобную адресуемость и читаемость.

**Класс необходимости:** `PRACTICAL / ADDRESSABILITY`.

**Вывод:** поле сохраняется, но не считается доказательством Machine identity.

---

## 4.2 `identity.machine_abstraction`

**Удаление:** конкретный Domain Machine может быть описан без отдельного уровня абстракции; доменная реализация сама может быть однозначно различима.

Пример: `Reverse PFMEA` может быть описан как domain realization без обязательного отдельного generic Machine abstraction.

**Результат:** НЕ универсально необходимо.

**Класс необходимости:** `OPTIONAL / ABSTRACTION SUPPORT`.

**Вывод:** сохраняется как полезное поле, допускает `N/A`.

---

## 4.3 `identity.identity_bearing_relation_or_mode`

**Удаление:** исчезает основание различить Machine от произвольного набора действий/механизмов.

**Результат:** CRITICAL.

Это одно из основных условий Machine identity.

**Класс необходимости:** `IDENTITY-CORE`.

---

## 4.4 `identity.local_capability`

**Удаление:** невозможно определить, какой локальный результат должен устойчиво воспроизводить bounded execution.

**Результат:** CRITICAL.

**Класс необходимости:** `IDENTITY-CORE`.

---

## 4.5 `identity.machine_boundary_test`

На первый взгляд этот блок содержит необходимые элементы проверки:

- identity-bearing relation/mode;
- own execution boundary;
- local capability;
- closure condition;
- result.

Однако первые четыре значения уже описываются в самом Passport, а `result` относится не к Machine identity, а к **результату валидации классификации**.

**Результат:** в текущем расположении блок создаёт DUPLICATION.

### Вывод

`machine_boundary_test` не должен дублировать паспортные поля внутри `identity`.

Он является **validation apparatus**, а не частью самой Machine identity.

Рабочая гипотеза:

```yaml
validation:
  machine_boundary_test:
    identity_relation_check:
    own_execution_boundary_check:
    local_capability_check:
    closure_condition_check:
    result:
```

При этом значения самих характеристик берутся из Passport, а validation фиксирует факт их проверки.

**Класс необходимости:** `VALIDATION / NOT IDENTITY`.

---

# 5. Execution layer

## 5.1 `execution.trigger`

**Удаление:** можно знать, что делает Machine, но нельзя воспроизводимо определить, когда/при каком условии запускается bounded execution.

Для некоторых Machines trigger может быть:

- событием;
- условием;
- расписанием;
- непрерывным режимом.

**Результат:** необходим для воспроизводимости, но не является identity-core.

**Класс:** `EXECUTION-CORE`.

---

## 5.2 `execution.inputs_context`

**Удаление:** теряется информация, на каком исходном состоянии/контексте запускается Machine.

Это ослабляет воспроизводимость и делает boundary менее определённой.

**Результат:** REQUIRED FOR REPRODUCIBILITY.

**Класс:** `EXECUTION-CORE`.

---

## 5.3 `execution.preconditions`

**Удаление:** в простых Machines может быть возможно исполнение без отдельного перечня preconditions; часть условий может быть очевидна из inputs/context.

**Результат:** не универсальный identity/execution core.

**Класс:** `CONDITIONAL / MAY BE N/A`.

---

## 5.4 `execution.execution_boundary`

**Удаление:** исчезает собственная граница bounded execution.

Невозможно уверенно отличить Machine от Assembly, downstream continuation или произвольного набора механизмов.

**Результат:** CRITICAL.

**Класс:** `IDENTITY + BOUNDARY CORE`.

---

## 5.5 `execution.execution_sequence`

**Удаление:** локальная capability может быть заявлена, но воспроизводимость execution становится недостаточной.

Паспорт превращается из описания исполняемой единицы в декларацию.

**Результат:** REQUIRED FOR REPRODUCIBILITY.

Важно: sequence не обязана быть фиксированным SOP и не обязана быть одной и той же для всех реализаций.

**Класс:** `EXECUTION-CORE`.

---

## 5.6 `execution.evidence`

**Удаление:** невозможно понять, на каких наблюдаемых основаниях Machine принимает локальные решения или подтверждает результат.

Для некоторых Machines evidence может быть минимальным, но bounded execution без любого наблюдаемого результата теряет проверяемость.

**Результат:** REQUIRED FOR VERIFIABILITY.

**Класс:** `EXECUTION-CORE / VERIFICATION`.

---

## 5.7 `execution.decision_points_logic`

**Удаление:** допустимо для Machines, где нет intrinsic decision point или логика распределена во внешнем механизме.

**Результат:** не универсально обязательно.

**Класс:** `CONDITIONAL / N/A / DISTRIBUTED`.

---

## 5.8 `execution.local_outputs`

**Удаление:** исчезает локальный результат, через который Machine отделяется от downstream Assembly.

**Результат:** CRITICAL FOR BOUNDARY.

**Класс:** `BOUNDARY-CORE`.

---

## 5.9 `execution.closure_condition`

**Удаление:** невозможно определить, когда bounded execution завершено относительно собственной capability.

Closure не означает обязательно `return to normal`; это может быть:

- result;
- decision;
- verification;
- disposition;
- transition;
- handoff;
- mixed.

**Результат:** CRITICAL.

**Класс:** `IDENTITY + BOUNDARY CORE`.

---

# 6. Realization layer

## 6.1 `realization.domain`

**Удаление:** abstraction-level Machine может существовать без конкретного domain; Domain Machine — нет.

**Результат:** REQUIRED FOR DOMAIN REALIZATION, OPTIONAL FOR GENERIC MACHINE.

**Класс:** `REALIZATION / CONDITIONAL`.

---

## 6.2 `realization.internal_mechanisms`

**Удаление:** Machine identity не исчезает.

Это поле описывает, **как реализована** bounded execution, но не определяет identity через список компонентов.

**Результат:** НЕ identity-core.

**Класс:** `REALIZATION-CORE / NON-IDENTITY`.

Это подтверждает ранее установленное правило:

> Machine identity ≠ component list.

---

## 6.3 `realization.roles`

**Удаление:** Machine может быть онтологически определена, но конкретная организационная реализация становится менее воспроизводимой.

**Результат:** не identity-core.

**Класс:** `REALIZATION / REPRODUCIBILITY SUPPORT`.

---

## 6.4 `realization.artifacts`

**Удаление:** некоторые Machines вообще могут не иметь отдельного артефакта.

**Результат:** `OPTIONAL / MAY BE N/A`.

---

## 6.5 `realization.domain_specific_conditions`

**Удаление:** generic Machine identity сохраняется.

**Результат:** `OPTIONAL / DOMAIN SUPPORT`.

---

## 6.6 `realization.limitations`

**Удаление:** identity и execution boundary сохраняются, но теряется важная информация о пределах применимости.

**Результат:** `OPTIONAL BUT RECOMMENDED`.

Это поле особенно полезно для предотвращения ложного переноса Machine из одного domain в другой.

---

## 6.7 `realization.downstream_ownership`

**Удаление:** Machine ещё можно описать, но становится сложнее провести границу между локальным результатом Machine и последующим Assembly.

**Результат:** не identity-core, но важно для boundary/ownership.

**Класс:** `BOUNDARY SUPPORT`.

---

# 7. Relations layer

## 7.1 `relations.pattern`

**Удаление:** Machine остаётся определённой, даже если Pattern ещё находится в `HOLD`.

**Результат:** OPTIONAL.

Это сохраняет ранее установленный принцип:

> Pattern mapping не является предварительным условием полного Machine Passport.

---

## 7.2 `relations.invokes_uses`

**Удаление:** Machine identity не меняется.

Связь полезна для Assembly и архитектурной карты, но не определяет Machine.

**Результат:** OPTIONAL RELATION.

---

## 7.3 `relations.feeds`

**Удаление:** Machine identity не меняется.

Downstream relation может быть неизвестна или распределена.

**Результат:** OPTIONAL RELATION.

---

# 8. Provenance layer

## 8.1 `provenance.source`

**Удаление:** Machine как онтологический объект не исчезает, но исчезает traceability к источнику.

Для CMOC это существенно, поскольку текущая методология требует source-based evidence.

**Результат:** REQUIRED FOR CMOC PROVENANCE, NOT MACHINE IDENTITY.

---

## 8.2 `provenance.evidence_reference`

**Удаление:** становится невозможно быстро проверить основание классификации/извлечения.

**Результат:** REQUIRED FOR EVIDENCE TRACEABILITY.

Не является Machine identity.

---

## 8.3 `provenance.status`

**Удаление:** теряется управление жизненным циклом кандидата/подтверждённого объекта.

Для CMOC это важно, поскольку Machine может быть `CANDIDATE`, `STRONG CANDIDATE`, `MULTI-SOURCE CONFIRMED`, `CORE-RELEVANT`, `CANON` и т.д.

**Результат:** REQUIRED FOR CMOC LIFECYCLE, NOT MACHINE IDENTITY.

---

# 9. Consolidated field necessity matrix

| Field | Identity | Boundary | Reproducibility | Realization | Provenance | Necessity |
|---|---|---|---|---|---|---|
| name | — | — | — | — | — | Practical |
| machine_abstraction | — | — | — | + | — | Optional |
| identity_bearing_relation_or_mode | **+** | + | + | — | — | **Critical** |
| local_capability | **+** | + | + | — | — | **Critical** |
| machine_boundary_test | — | validation | — | — | — | Move to validation |
| trigger | — | + | **+** | — | — | Required for reproducibility |
| inputs_context | — | + | **+** | — | — | Required |
| preconditions | — | + | + | — | — | Conditional |
| execution_boundary | **+** | **+** | + | — | — | **Critical** |
| execution_sequence | — | + | **+** | — | — | Required |
| evidence | — | + | **+** | — | + | Required for verifiability |
| decision_points_logic | — | + | + | — | — | Conditional |
| local_outputs | — | **+** | **+** | — | — | Critical for boundary |
| closure_condition | **+** | **+** | + | — | — | **Critical** |
| domain | — | — | — | **+** | — | Conditional |
| internal_mechanisms | — | — | + | **+** | — | Realization only |
| roles | — | — | + | **+** | — | Realization support |
| artifacts | — | — | + | + | — | Optional |
| domain_specific_conditions | — | — | + | + | — | Optional |
| limitations | — | — | — | + | — | Optional/recommended |
| downstream_ownership | — | **+** | + | + | — | Boundary support |
| pattern | — | — | — | + | — | Optional/HOLD |
| invokes_uses | — | — | — | + | — | Optional |
| feeds | — | **+** | + | + | — | Optional |
| source | — | — | — | — | **+** | CMOC-required |
| evidence_reference | — | — | — | — | **+** | CMOC-required |
| status | — | — | — | — | **+** | CMOC lifecycle-required |

---

# 10. Key result: two different kinds of “core”

Тест выявил необходимость не смешивать два понятия.

### A. Machine Core

Минимум, необходимый для определения bounded executable unit:

```yaml
identity:
  identity_bearing_relation_or_mode:
  local_capability:

execution:
  execution_boundary:
  execution_sequence:
  local_outputs:
  closure_condition:
```

Для воспроизводимого исполнения дополнительно необходимы:

```yaml
execution:
  trigger:
  inputs_context:
  evidence:
```

`preconditions` и `decision_points_logic` могут быть `N/A`/`distributed`.

### B. CMOC Passport Core

Для объекта CMOC нужны также:

```yaml
provenance:
  source:
  evidence_reference:
  status:
```

Это не свойства Machine как таковой; это свойства **зафиксированного в CMOC объекта знания**.

---

# 11. Important schema correction

Текущий v0.2 содержит:

```yaml
identity:
  machine_boundary_test:
    identity_bearing_relation_or_mode:
    own_execution_boundary:
    local_capability:
    closure_condition:
    result:
```

Тест показывает, что это смешивает:

- характеристики Machine;
- проверку классификации.

Рабочая корректировка:

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

  provenance:
    source:
    evidence_reference:
    status:

  validation:
    machine_boundary_test:
      result:
      checked_against:
```

`checked_against` может ссылаться на уже заполненные Passport fields вместо повторного хранения их значений.

---

# 12. Architectural conclusion

Тест подтверждает разделение:

`PATTERN → MACHINE → DOMAIN MACHINE → ASSEMBLY → CAPABILITY`

и уточняет роль Passport:

> **Machine Passport описывает Machine; Validation проверяет, действительно ли описанный объект удовлетворяет Machine boundary.**

Passport не должен одновременно быть и описанием объекта, и протоколом его классификационного теста.

Также подтверждено:

> **Machine identity определяется не количеством заполненных полей, а identity-bearing relation/mode + own execution boundary + local capability + closure condition.**

При этом для воспроизводимого CMOC-описания bounded execution нужны trigger, inputs/context, sequence и evidence.

---

# 13. Status

- Machine Passport v0.2 Field Necessity Test: **PASS**
- Machine Identity Core: **DEFINED**
- Execution/Reproducibility Core: **DEFINED**
- Realization Layer: **DEFINED**
- Provenance Layer: **DEFINED**
- `machine_boundary_test` as identity content: **REJECTED / MOVE TO VALIDATION**
- Pattern as optional/HOLD: **CONFIRMED**
- Internal mechanisms as non-identity: **CONFIRMED**
- N/A / HOLD / distributed support: **CONFIRMED**
- Canon: **NON-CANON**
- Machine Catalog: **NO CHANGE**
- Canon: **NO CHANGE**
- REG-001: **NO CHANGE**

## Next methodological step

**Machine Passport v0.2 Schema Refactor Test** — проверить предложенное разделение `machine_passport` и `validation`, затем прогнать его минимум через Andon, Gemba Walk, Expected-vs-Actual Control Verification и один GM-096 Machine Candidate, чтобы убедиться, что удаление дублирования не потеряло ни identity, ни boundary, ни provenance.
