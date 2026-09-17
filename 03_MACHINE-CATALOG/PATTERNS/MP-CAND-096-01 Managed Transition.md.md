---
pattern_id: MP-CAND-096-01
name: Managed Transition

source: GM Quality System Basics rev March 2009 — Managing Change; independent MOC sources
source_location: GM-096 pp. 325–344; independent cross-check sources

level: PATTERN
type: ORGANIZATIONAL TRANSITION CONTROL

problem: >
  Организации необходимо перевести объект, процесс или организационное
  состояние из текущего состояния в новое, не теряя управляемости на переходе.
  Простого факта принятия решения об изменении недостаточно: переход требует
  идентификации, оценки, полномочий, контролируемого выполнения, проверки и
  формального завершения либо возврата.

purpose: >
  Обеспечить воспроизводимую управляемость перехода между состояниями системы,
  включая контролируемый вход, выполнение, проверку результата и принятие
  нового состояния либо возврат к исходному.

trigger_mode: managed change / state transition
trigger: >
  Возникает необходимость перевести управляемый объект, процесс или систему
  из State A в State B, включая временный переход с последующим возвратом.

input:
  - исходное состояние
  - требуемое / допустимое целевое состояние
  - описание изменения или причины перехода
  - критерии оценки и принятия
  - полномочия / требования к approval
  - условия возврата или rollback, если применимо

actions:
  - идентифицировать переход
  - определить затронутые элементы и границы перехода
  - оценить последствия / риски / требования
  - определить необходимость разрешения или дополнительных проверок
  - авторизовать переход
  - выполнить переход в контролируемом режиме
  - проверить фактическое состояние и результат
  - принять новое состояние либо выполнить возврат
  - зафиксировать результат и закрытие перехода

output_type: VERIFIED STATE TRANSITION
output: >
  Проверенное принятое состояние B либо документированный возврат к State A.

roles:
  - change owner / transition owner
  - authorized decision maker
  - responsible implementers
  - verification / quality role
  - affected stakeholders

artifacts:
  - change / transition request
  - assessment / impact record
  - approval / authorization record
  - transition plan or procedure
  - verification evidence
  - acceptance / return record
  - close-out record

mechanism: >
  state A → identify → assess → authorize → controlled transition → verify →
  accept / return → record / close

capability: >
  Переводить управляемый объект или процесс между состояниями с сохранением
  прослеживаемости, полномочий, критериев проверки и возможности принятия
  либо возврата.

invokes:
  - Decision Gate
  - Assessment against Criterion
  - Verification
  - Controlled Deviation, where applicable
  - Response to Abnormality, where applicable

feeds:
  - accepted new state
  - verified return state
  - transition evidence / organizational record

checks:
  - transition scope
  - authorization
  - implementation conditions
  - verification criteria
  - target state
  - return / rollback condition, where applicable
  - close-out

improves: []
standardizes:
  - transition entry / decision / verification / closure logic
replicates: []
composes:
  - PPCR
  - PTR
  - Banking
  - Bypass Process Control
  - Management of Change / Temporary Change implementations

conditions:
  - State A is identifiable
  - transition intent and boundary are defined
  - responsible authority is known
  - acceptance / verification criteria exist
  - return is defined when the transition is temporary or reversible

limitations:
  - Managed Transition is a CMOC working name for the recurring construction;
    it is not asserted here as a universal industry-standard term.
  - It is a Pattern, not a Machine and not a replacement for domain-specific
    change-management or validation procedures.
  - The pattern describes the invariant transition grammar; domain-specific
    Machines implement it with additional requirements.
  - A generic State Transition is broader and may describe a state change
    without the governance and verification structure captured here.

cmoc_links:
  - State A → Managed Transition → State B
  - Managed Transition → Decision Gate
  - Managed Transition → Verification
  - Managed Transition → Accept / Return
  - PPCR → Managed Transition
  - PTR → Managed Transition
  - Banking → Managed Transition
  - Bypass → Managed Transition

source_claim: >
  GM-096 establishes a managed change architecture containing plant process
  change control, trial decision and execution, banking of material outside
  normal flow, bypass control, verification and authorized return. Independent
  Management of Change sources reproduce the broader sequence of identifying,
  assessing, authorizing, executing, verifying and closing or returning from a
  change, including temporary changes.

cmoc_interpretation: >
  The recurring engineering distinction is not merely that a change occurs,
  but that the organization controls the transition from one state to another.
  The invariant construction is therefore modeled as a Pattern. PPCR, PTR,
  Banking and Bypass are specialized implementations or assemblies around this
  transition grammar rather than evidence for a universal Change Management
  Machine.

status: STRONG PATTERN CANDIDATE / NON-CANON
evidence: MULTI-SOURCE CONFIRMED
---
# Managed Transition

## 1. Что это

**Managed Transition / Управляемый переход** — паттерн, описывающий
управляемый перевод объекта, процесса или организационной системы из одного
состояния в другое с контролируемым входом, выполнением, проверкой и
формальным принятием либо возвратом.

## 2. Отличительная конструкция

`State A → Identify → Assess → Authorize → Transition → Verify → Accept / Return → Record`

Ключевой признак — не само изменение и не состояние, а **управляемость
перехода между состояниями**.

## 3. Проблема

Изменение может быть формально разрешено, но при отсутствии контролируемого
перехода организация теряет границы, ответственность, критерии проверки и
способность доказать, что новое состояние действительно достигнуто.

## 4. Назначение

Удержать переход в определённых границах и обеспечить доказуемое достижение
нового состояния либо контролируемый возврат.

## 5. Триггер

Необходимость перейти из текущего управляемого состояния в другое состояние,
в том числе временно.

## 6. Вход

Исходное состояние, целевое состояние, описание перехода, затронутые элементы,
критерии оценки, полномочия и условия возврата.

## 7. Действия

1. Идентифицировать переход.
2. Определить границы и затронутые элементы.
3. Оценить последствия / риски / требования.
4. Определить необходимость разрешения и дополнительных проверок.
5. Авторизовать переход.
6. Выполнить переход контролируемым способом.
7. Проверить результат и фактическое состояние.
8. Принять новое состояние либо выполнить возврат.
9. Зафиксировать результат и закрытие.

## 8. Выход

Проверенное принятое состояние B либо документированный возврат к State A.

## 9. Роли

Владелец перехода, уполномоченный принимающий решение, исполнители,
верифицирующая / quality-функция, затронутые стороны.

## 10. Артефакты

Запрос на изменение / переход, оценка воздействия, approval, план / процедура
перехода, доказательства проверки, запись принятия / возврата, close-out.

## 11. Связи с GM-096

- **PPCR** — управляемый вход в изменение.
- **PTR** — контролируемый пробный переход / оценка.
- **Banking** — управляемое специальное состояние материала.
- **Bypass** — управляемое специальное состояние процесса.
- **Verification / Review** — подтверждение состояния.
- **Return / Close** — завершение или возврат.

## 12. Граница с соседними конструкциями

- `State Transition` — более общий факт или модель перехода между состояниями.
- `Controlled Transition` — акцент на контролируемом исполнении перехода.
- `Managed Transition` — акцент на полной организационной конструкции:
  идентификация → оценка → полномочие → переход → проверка → принятие / возврат.
- `Change Management` — более широкая дисциплина и набор методов; Managed
  Transition выделяет повторяющуюся структурную логику внутри неё.

## 13. Условия применения

Должны быть различимы исходное и целевое состояния, границы перехода,
ответственные полномочия и критерии проверки. Для временного / обратимого
перехода должна быть определена точка или условие возврата.

## 14. Ограничения

Паттерн не заменяет отраслевые процедуры изменения, валидации, допуска,
релиза или управления временным отклонением. Его задача — фиксировать
инвариантную организационную логику, которую могут реализовывать разные
специализированные конструкции.

## 15. Статус

**STRONG PATTERN CANDIDATE / MULTI-SOURCE CONFIRMED / NON-CANON**

Следующая проверка: испытать границы паттерна на нескольких независимых
конструкциях и определить, какие из них действительно являются его
специализациями, а какие лишь похожи по последовательности действий.
