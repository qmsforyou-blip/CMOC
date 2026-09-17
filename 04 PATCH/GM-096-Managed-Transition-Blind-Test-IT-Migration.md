# GM-096 — Managed Transition: Blind Test in IT Migration

**Дата:** 17-09-2026  
**Извещение:** `0141+170926`  
**Статус:** `CROSS-CHECK COMPLETE / NON-CANON`

## 1. Цель

Проверить рабочую гипотезу `Managed Transition / Управляемый переход` вне GM/QMS-контекста — на независимом домене IT-системной миграции и cutover.

Тест выполняется без использования GM-терминологии при первичной реконструкции. Задача — установить, воспроизводится ли минимальная грамматика Pattern независимо от исходной предметной области.

## 2. Минимальная грамматика Pattern

```text
STATE A
  ↓
IDENTIFY
  ↓
ASSESS
  ↓
DECIDE / AUTHORIZE
  ↓
TRANSITION
  ↓
VERIFY
  ↓
ACCEPT / RETURN / ROLLBACK
  ↓
RECORD / CLOSE
```

Это рабочая CMOC-конструкция, а не утверждение о наличии такого термина или такой единой схемы в IT-источниках.

## 3. Blind Test — IT migration / cutover

### 3.1 Microsoft 365 change management

Microsoft описывает изменение через документирование причины, области, security impact, приоритетов, зависимостей, deployment plan и ролей; до реализации выполняются review/approval и testing. Для non-code changes фиксируются implementation steps, validation steps и rollback plan. После успешной валидации результат документируется, а при неуспешной реализации запускается rollback.

Источник: Microsoft Learn, *Microsoft 365 change management*.

Получаемая последовательность:

```text
CHANGE IDENTIFICATION / PLANNING
→ REVIEW / APPROVAL
→ IMPLEMENT
→ VALIDATE
→ ACCEPT / RESOLVE
или
→ ROLLBACK
→ RETURN TO PLANNING
→ RECORD
```

Это воспроизводит практически всю минимальную грамматику.

### 3.2 AWS migration / cutover

AWS Migration Lens требует определить окно миграции, оценить его влияние, выполнить dry-run, предусмотреть contingency/rollback и проверить результат после cutover. AWS Prescriptive Guidance для cutover дополнительно задаёт operational readiness review, заранее определённые rollback checkpoints и ответственное лицо, принимающее решение между fix-forward и rollback.

Источники: AWS Well-Architected Migration Lens; AWS Prescriptive Guidance, *Best practices for cutting over network traffic to AWS*.

Получаемая последовательность:

```text
ASSESS / PLAN
→ DRY-RUN / TEST
→ READINESS REVIEW
→ CUTOVER
→ VALIDATE / MONITOR
→ ACCEPT
или
→ ROLLBACK / FAILBACK
```

Здесь особенно явно проявляется переход между двумя состояниями: source environment → target environment.

### 3.3 AWS migration workstream / handover

AWS также описывает после cutover application testing, acceptance decision, а после выполнения критериев handoff/signoff — передачу ответственности операционной команде и завершение migration wave.

Получаемая последовательность:

```text
PREPARE
→ CUTOVER
→ TEST / VALIDATE
→ ACCEPTANCE DECISION
→ HANDOVER / SIGNOFF
→ COMPLETE
```

Таким образом, `ACCEPT / CLOSE` не является искусственно добавленным элементом Pattern: он независимо появляется как acceptance/signoff/handover.

## 4. Сопоставление с минимальной грамматикой

| Элемент Pattern | IT migration evidence | Роль |
|---|---|---|
| IDENTIFY | change description, migration scope, dependencies | фиксация того, что именно меняется |
| ASSESS | impact, risk, downtime, testing, readiness | оценка возможности и условий перехода |
| DECIDE / AUTHORIZE | peer review, approval, CAB/change approval, readiness decision | разрешение перехода |
| TRANSITION | deployment, cutover, migration | фактический переход |
| VERIFY | validation, testing, monitoring, application testing | проверка нового состояния |
| ACCEPT | acceptance decision, handover/signoff | признание нового состояния приемлемым |
| RETURN | rollback/failback | возврат к исходному состоянию |
| RECORD / CLOSE | ticket resolution, runbook/checklist, signoff | фиксация результата и завершение |

## 5. Что произошло с внутренними механизмами

Blind test подтверждает предыдущий вывод о внутренней грамматике:

- `Decision Gate` — присутствует как approval/readiness/acceptance decision;
- `Assessment against Criterion` — присутствует как impact/risk assessment, testing и readiness evaluation;
- `Verification` — присутствует как validation/testing/monitoring;
- `Controlled Deviation` — не является обязательным элементом общего IT-перехода; возникает только при необходимости временного отклонения или специального режима;
- `Response to Abnormality` — также не является обязательным элементом перехода; появляется при failure/alert/rollback decision;
- `Record / Traceability` — присутствует через tickets, runbooks, checklists, signoff и deployment evidence.

То есть результаты blind test согласуются с предыдущей гипотезой: эти конструкции являются переиспользуемыми control functions, а не определением самого Pattern.

## 6. Граница Pattern

Blind test позволяет провести важное различение.

`Managed Transition` — не синоним:

- change management;
- migration;
- deployment;
- cutover;
- rollback;
- validation;
- approval.

Все они могут быть конкретными реализациями или частями управляемого перехода.

Идентичность Pattern определяется не предметным названием операции, а управляемым перемещением системы/процесса/объекта из одного принятого состояния в другое с контролем входа, перехода, проверки и выхода.

Рабочая формула сохраняется:

```text
STATE A
→ IDENTIFY
→ ASSESS
→ AUTHORIZE / DECIDE
→ CONTROLLED TRANSITION
→ VERIFY
→ ACCEPT / RETURN / ROLLBACK
→ RECORD / CLOSE
```

## 7. Вывод

Blind test на IT migration/cutover **пройден**.

Независимые IT-источники воспроизводят ту же управляющую конструкцию без необходимости использовать GM/QMS-терминологию. Особенно сильны подтверждения для:

1. идентификации и оценки изменения;
2. предварительного решения/разрешения;
3. контролируемого перехода;
4. проверки нового состояния;
5. формального acceptance/signoff;
6. rollback/failback как управляемой альтернативы;
7. документированного завершения.

### CMOC classification

- **Entity:** `Managed Transition / Управляемый переход`
- **Kind:** `PATTERN`
- **Status:** `STRONG PATTERN CANDIDATE / NON-CANON`
- **Evidence:** `MULTI-SOURCE CONFIRMED`
- **Cross-domain test:** `PASSED — IT MIGRATION / CUTOVER`
- **Working grammar:** `STATE A → IDENTIFY → ASSESS → AUTHORIZE → TRANSITION → VERIFY → ACCEPT / RETURN / ROLLBACK → RECORD / CLOSE`

## 8. Что НЕ изменяется

- `REG-001` — без изменений;
- `Canon` — без изменений;
- `Machine Catalog` — без изменений;
- существующие Machine Passports — без изменений;
- `Managed Transition` не переводится в CANON;
- новые Machine/Pattern/Mechanism в результате blind test не создаются.

## 9. Следующий архитектурный вопрос

После успешного cross-domain blind test следующий полезный шаг — проверить Pattern не на технологическом переходе, а на **организационном переходе**: передаче ответственности/функции между командами или владельцами.

Если минимальная грамматика и там восстанавливается без искусственной натяжки, гипотеза о более высоком уровне Pattern получает ещё одно независимое подтверждение.

---

### Web evidence

- Microsoft Learn — *Microsoft 365 change management*.
- AWS Well-Architected — *Migration Lens: Assess / Migrate*.
- AWS Prescriptive Guidance — *Best practices for cutting over network traffic to AWS*.
- AWS Prescriptive Guidance — *Large migration workstreams / cutover / handover*.

**Примечание:** ссылки и формулировки источников использованы как evidence для cross-check; названия и формула `Managed Transition / Управляемый переход` остаются рабочей CMOC-номенклатурой и не выдаются за отраслевой стандартный термин.