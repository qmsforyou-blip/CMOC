---
machine_id: MC-CAND-096-02
name: Production Trial Run

source: GM Quality System Basics rev March 2009 — Managing Change
source_location: pp. 333–335

level: MACHINE
type: CHANGE VALIDATION / TRIAL

problem: >
  Изменение производственного процесса может требовать проверки
  в условиях производства до перехода к штатному состоянию.

purpose: >
  Провести контролируемый Production Trial Run с заранее определёнными
  требованиями, решениями, согласованиями и фиксацией результатов.

trigger_mode: decision / controlled trial
trigger: >
  Решение в рамках Change Process о необходимости Production Trial Run.

input:
  - описание изменения
  - PTR request
  - требования к trial run
  - решение о необходимости customer/internal PTR
  - необходимые approvals

actions:
  - инициирование PTR request
  - рассмотрение PTR Core Team
  - принятие решения / получение approval
  - определение customer/internal PTR requirements
  - проведение trial run по установленной процедуре
  - документирование каждого шага в Communication Form
  - фиксация результатов
  - customer evaluation, когда применимо

output_type: TRIAL RESULT / DECISION INPUT
output: >
  Документированный результат производственного trial run,
  пригодный для последующего решения о принятии изменения.

roles:
  - Change Leader
  - PTR Core Team
  - internal approvers
  - customer contacts / customer, when applicable

artifacts:
  - PTR procedure / flowchart
  - PTR Request
  - Communication Form
  - approval / evaluation records

mechanism: >
  PTR request → team decision / approval → requirement decision →
  controlled trial → documented result → evaluation

capability: >
  Способность проверять изменение в производственных условиях
  до его принятия в штатный процесс, сохраняя управляемость решения
  и прослеживаемость результатов.

invokes:
  - Plant Process Change Control
  - evaluation / verification mechanisms

feeds:
  - change implementation decision
  - customer/internal evaluation

checks:
  - requirement for PTR
  - approvals
  - trial steps
  - trial results

improves: []
standardizes:
  - PTR procedure
replicates: []
composes:
  - decision gate
  - controlled trial
  - evaluation
  - documented communication

conditions:
  - written PTR procedure / flowchart exists
  - required approvals are obtained
  - trial requirements are defined
  - results are documented

limitations:
  - PTR is not a substitute for or extension of product validation.
  - PTR is invoked only when the change process determines that a trial is required.
  - The reviewed GM pages establish PTR as a specialized construction within Managing Change; they do not prove it is a universal trial Machine across domains.

cmoc_links:
  - Change → Decision Gate
  - Change → Trial
  - Trial → Evidence
  - Evidence → Evaluation
  - Evaluation → Change Decision
  - Managing Change → Chain

source_claim: >
  GM QSB defines a written PTR procedure / flowchart and a Communication Form
  documenting each step, including PTR request, Core Team decision / approval,
  customer/internal PTR requirement decision, internal review / approval and
  customer evaluation where applicable. GM explicitly states PTR is not a
  substitute for or extension of product validation.

cmoc_interpretation: >
  Specialized, bounded change-validation Machine that is invoked by the
  change-control architecture when a production trial is required. Its
  distinctive identity is the controlled conversion of a proposed process
  change into documented production-trial evidence and an evaluation input.

status: SPECIALIZED-CANDIDATE / NON-CANON
---
# Production Trial Run

## 1. Что это

Воспроизводимая конструкция контролируемого производственного trial run,
который проводится при необходимости проверить изменение до его принятия
в штатное состояние.

## 2. Проблема

Изменение может быть технически реализовано, но требовать проверки поведения
процесса в реальных производственных условиях до окончательного решения.

## 3. Назначение

Получить документированное производственное свидетельство о результате
trial run и обеспечить основу для последующего решения.

## 4. Триггер

Решение Change Process о том, что для изменения требуется PTR.

## 5. Вход

Описание изменения, PTR Request, требования к trial, решения и approvals.

## 6. Действия

1. Инициировать PTR Request.
2. Рассмотреть запрос PTR Core Team.
3. Получить необходимое решение / approval.
4. Определить customer/internal PTR requirements.
5. Провести trial по установленной процедуре.
6. Зафиксировать шаги и результаты в Communication Form.
7. Выполнить evaluation, когда применимо.

## 7. Выход

Документированный результат trial run и evidence для последующего решения
по изменению.

## 8. Роли

Change Leader, PTR Core Team, внутренние согласующие, customer contacts /
customer — когда применимо.

## 9. Артефакты

PTR procedure / flowchart, PTR Request, Communication Form, approvals,
evaluation records.

## 10. Реализуемый механизм

`request → decision/approval → requirement decision → trial → documented result → evaluation`

## 11. Развиваемая способность

Проверять изменение в производственных условиях управляемым и прослеживаемым
способом до его принятия в штатный процесс.

## 12. Связи с другими машинками

- PPCR — источник решения о необходимости PTR и общий change-control context.
- Evaluation / verification — обработка и проверка результатов trial.

## 13. Условия применения

Наличие документированной PTR procedure; определённых требований;
необходимых согласований; документирования результатов.

## 14. Ограничения

PTR не является product validation и не заменяет её. PTR — специализированная
конструкция внутри Managing Change.

## 15. Связи с CMOC

`Change → Decision → Trial → Evidence → Evaluation → Decision`

PTR является специализированной Machine внутри более широкой Chain
управляемого изменения.

## 16. Что утверждает источник

GM QSB описывает written PTR procedure / flowchart и Communication Form,
фиксирующий каждый шаг, включая запрос, решение Core Team, approvals,
определение customer/internal requirements и evaluation.

## 17. Что выделено нами для CMOC

Отличительный признак PTR — не само слово «trial», а bounded construction,
в которой решение о необходимости trial переводится в управляемое испытание
в производственной среде с документированным результатом.

## 18. Статус

**SPECIALIZED-CANDIDATE / NON-CANON**

Следующая проверка: сравнить PTR с PPCR и более общими Trial / Validation
конструкциями по независимым источникам.
