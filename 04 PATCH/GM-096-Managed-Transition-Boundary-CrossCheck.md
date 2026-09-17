---
patch_id: GM-096-Managed-Transition-Boundary-CrossCheck
notice: 0141+170926
date: 17-09-2026
status: CROSS-CHECK COMPLETE / NON-CANON
---

# GM-096 — Managed Transition: Boundary Cross-Check

## 1. Цель

Проверить границы Pattern `Managed Transition` на независимых конструкциях:
- deployment / release;
- migration / cut-over;
- organizational transition / handover;
- rollback / return.

Задача — проверить, сохраняется ли одна и та же инженерная конструкция за пределами GM/QSB, не превращая все переходы автоматически в один универсальный объект.

## 2. Независимые источники

### Microsoft — transition and handover

Microsoft описывает переход к эксплуатации после implementation/cutover/go-live и отдельно требует учитывать rollback, failover, training, knowledge transfer, readiness и post-go-live reinforcement.

Источник: Microsoft Learn, “Manage changes during transition and handover”.

### Microsoft — cloud modernization

Microsoft описывает deployment strategies через reversible changes, parallel deployment, cutover и rollback procedures. Для крупных изменений предусматриваются проверка и возможность возврата.

Источник: Microsoft Learn, “Plan your cloud modernization — Cloud Adoption Framework”.

### AWS — Change Enablement

AWS рассматривает deployment как часть change process; рекомендует небольшие обратимые изменения, governance, audit trail и rollback для изменений с неблагоприятным результатом.

Источник: AWS Well-Architected, “Change Enablement in the Cloud”.

### Migration / cutover practice

Независимые migration/cutover материалы описывают controlled transition через discovery/readiness → testing → cutover → validation → accept/rollback → stabilization/closure.

Эти источники используются как evidence of recurring construction, а не как нормативные определения CMOC.

## 3. Boundary test

| Область | Наблюдаемая конструкция | Совпадение с Pattern |
|---|---|---|
| Deployment | подготовка → go/no-go → deployment → verification → accept/rollback | высокое |
| Migration | current state → preparation → cutover → validation → accept/rollback | высокое |
| Organizational handover | transition → knowledge transfer → training → support readiness → go-live → reinforcement | высокое |
| Rollback | failed transition → controlled return / alternate change → verification | высокое |

## 4. Что устойчиво

Во всех рассмотренных областях повторяется не конкретная технология, а структура:

`STATE A → IDENTIFY / PREPARE → ASSESS → AUTHORIZE / DECIDE → TRANSITION → VERIFY → ACCEPT / RETURN → RECORD / STABILIZE`

Следовательно, Pattern не ограничивается производственным change control GM.

## 5. Важное ограничение

`Managed Transition` не следует отождествлять с:

- deployment;
- migration;
- cutover;
- rollback;
- change management;
- handover.

Это специализированные реализации или элементы более общей конструкции.

Особенно важно различать:

- **State Transition** — абстрактная модель изменения состояния;
- **Controlled Transition** — характеристика выполнения перехода с контролями;
- **Managed Transition** — организационный паттерн, в котором переход имеет управляемые вход, решение, выполнение, проверку и завершение.

## 6. Роль rollback

Rollback не является обязательным исходом каждого перехода.

Он является одной из ветвей после проверки:

`VERIFY → ACCEPT`

или

`VERIFY → RETURN / ROLLBACK`

Это усиливает границу Pattern: управляемость перехода включает заранее определённую возможность безопасного выхода из неуспешного состояния, когда это применимо.

## 7. Граница Pattern

Pattern `Managed Transition` применим, когда одновременно существуют:

1. различимые исходное и целевое состояния;
2. необходимость перейти между ними;
3. управляемая подготовка / оценка;
4. решение или authorization gate;
5. контролируемое выполнение перехода;
6. проверка достигнутого состояния;
7. формальное принятие, возврат или продолжение управляемого состояния;
8. фиксация результата / закрытие.

Если есть только изменение состояния без организационного управления переходом, это `State Transition`, а не `Managed Transition`.

Если есть только контроль отдельной операции, это механизм контроля, а не Pattern целиком.

## 8. Связь с GM-096

GM-096 предоставляет несколько специализированных реализаций одной более общей конструкции:

- PPCR — управляемый вход в изменение;
- PTR — управляемая проба / evaluation;
- Banking — управление специальным состоянием материала;
- Bypass — управление специальным состоянием процесса;
- verification / review — подтверждение состояния;
- return / close — завершение или возврат.

Таким образом, ранее выделенный Pattern получает независимую boundary evidence.

## 9. Вердикт CMOC

`Managed Transition`

- Kind: `PATTERN`
- Status: `STRONG PATTERN CANDIDATE / NON-CANON`
- Evidence: `MULTI-SOURCE CONFIRMED`
- Scope: cross-domain organizational/process transition

Новая проверка **не требует** превращения Pattern в Machine.

## 10. Воздействие

REG-001: unchanged.

Canon: unchanged.

Machine Catalog: unchanged.

Existing Machine Passports: unchanged.

Pattern Passport: подтверждён как рабочий кандидат; граница расширена до deployment, migration, handover и rollback/return.

## 11. Следующий шаг

Не канонизировать автоматически.

Следующая проверка должна искать возможные конкурирующие паттерны в CMOC: `Controlled Deviation`, `Response to Abnormality`, `Decision Gate`, `Assessment against Criterion`, а также определить, какие из них являются составными механизмами внутри `Managed Transition`.

**VERDICT: BOUNDARY CROSS-CHECK COMPLETE / NON-CANON.**
