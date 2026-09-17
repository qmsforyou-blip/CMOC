---
machine_id: MC-CAND-096-01
name: Plant Process Change Control

source: GM Quality System Basics rev March 2009 — Managing Change
source_location: pp. 327–331, 344

level: MACHINE
type: CHANGE CONTROL / GOVERNANCE

problem: >
  Изменения производственного процесса, включая planned и emergency
  changes, могут быть выполнены без единого управляемого порядка,
  без согласования затронутых сторон и без прослеживаемой записи.

purpose: >
  Обеспечить управляемое внесение изменений в производственный процесс
  через регистрацию, рассмотрение, согласование, выполнение и фиксацию
  результата.

trigger_mode: event / planned / emergency
trigger: изменение производственного процесса

input:
  - предложение об изменении
  - описание требуемого изменения
  - сведения о затронутых процессах / системах
  - требования заинтересованных сторон

actions:
  - регистрация изменения
  - документирование изменения в Plant Process Change form
  - определение затронутых сторон
  - получение их input / review
  - согласование изменения
  - выполнение изменения по установленному порядку
  - фиксация результата и статуса

output_type: CONTROLLED CHANGE / RECORD
output: >
  Изменение выполнено в управляемом состоянии, имеет запись,
  согласование и прослеживаемый статус.

roles:
  - change owner / responsible person
  - affected stakeholders
  - approvers
  - Document Control

artifacts:
  - Plant Process Change procedure
  - Plant Process Change form / PPCR
  - controlled records

mechanism: >
  change registration → stakeholder review → approval → controlled
  implementation → recorded result

capability: >
  Способность организации управляемо проводить planned и emergency
  изменения производственного процесса с сохранением прослеживаемости,
  согласования и информированности затронутых сторон.

invokes:
  - Production Trial Run (when trial is required)
  - Bypass Process Control (when approved process cannot be maintained)
  - verification / review mechanisms

feeds:
  - Production Trial Run
  - Banking Process
  - Bypass Process Control

checks:
  - completeness of change record
  - required stakeholder input / approval
  - implementation status

improves: []
standardizes:
  - plant process change procedure
replicates: []
composes:
  - change registration
  - decision gate
  - controlled change implementation
  - verification

conditions:
  - procedure exists and is controlled
  - change is registered before / as required by the plant process change procedure
  - affected stakeholders are identified and involved
  - approvals are obtained before execution where required

limitations:
  - PPCR does not by itself constitute product validation.
  - PPCR does not replace the specialized PTR construction when a trial run is required.
  - PPCR does not replace Bypass Process Control for temporary departure from an approved process.
  - The reviewed GM pages do not by themselves establish a universal CMOC-level change-control Machine beyond this plant-process context.

cmoc_links:
  - Change → Registration
  - Change → Decision Gate
  - Change → Controlled Implementation
  - Change → Record
  - Change → Verification
  - Managing Change → Chain

source_claim: >
  GM requires suppliers to have a Plant Process Changes procedure covering
  planned and emergency changes, to document changes using a plant process
  change form, and to maintain a record of changes impacting final product
  while ensuring affected stakeholders are aware and can provide input.

cmoc_interpretation: >
  Bounded, reproducible governance Machine for controlling a plant process
  change from registration through review, approval, implementation and
  recorded result. Within GM-096 it functions as the entry and governing
  Machine for the broader change-control grammar.

status: STRONG-CANDIDATE / NON-CANON
---
# Plant Process Change Control

## 1. Что это

Воспроизводимая конструкция управления изменением производственного процесса:
изменение регистрируется, рассматривается затронутыми сторонами, согласуется,
выполняется по установленному порядку и оставляет управляемую запись.

## 2. Проблема

Без отдельного процесса planned или emergency change может стать разовым
решением без согласования, прослеживаемости и контроля последствий.

## 3. Назначение

Перевести изменение из состояния «предложение / необходимость» в состояние
«управляемо реализованное изменение».

## 4. Триггер

Необходимость изменения производственного процесса — плановая или аварийная.

## 5. Вход

Описание изменения, затронутые процессы и системы, требования и input
заинтересованных сторон.

## 6. Действия

1. Зарегистрировать изменение.
2. Оформить Plant Process Change form.
3. Определить затронутые стороны.
4. Получить их input / review.
5. Получить необходимые согласования.
6. Выполнить изменение по установленной процедуре.
7. Зафиксировать результат и статус.

## 7. Выход

Контролируемое изменение и запись, позволяющая проследить его содержание,
согласование и результат.

## 8. Роли

Ответственный за изменение, затронутые стороны, согласующие лица,
Document Control.

## 9. Артефакты

Plant Process Change procedure, Plant Process Change form / PPCR,
управляемые записи.

## 10. Реализуемый механизм

`change registration → stakeholder review → approval → controlled implementation → recorded result`

## 11. Развиваемая способность

Проводить изменения производственного процесса без потери управляемости,
согласования и прослеживаемости.

## 12. Связи с другими машинками

- PTR — вызывается, если для изменения требуется Production Trial Run.
- Banking — управляет специальным состоянием материала после изменения / при длительном хранении.
- Bypass — используется для временного отклонения от approved process.
- Audit / verification — может проверять соблюдение и результат процесса.

## 13. Условия применения

Наличие документированной Plant Process Change procedure; определение
затронутых сторон; управление формами и записями; выполнение необходимых
согласований.

## 14. Ограничения

PPCR не является заменой product validation и не поглощает PTR, Banking или
Bypass как специализированные конструкции.

## 15. Связи с CMOC

`Change → Registration → Decision → Approval → Implementation → Record → Verification`

PPCR является кандидатом на самостоятельную Machine, встроенную в более
широкую Chain / grammar of managed change.

## 16. Что утверждает источник

GM QSB требует Plant Process Changes procedure для planned и emergency changes,
documentation через plant process change form и ведение записи изменений,
затрагивающих final product, с участием заинтересованных сторон.

## 17. Что выделено нами для CMOC

Ключевой признак самостоятельной Machine — не название PPCR, а bounded
reproducible construction с собственным trigger, input, набором действий,
ролями, артефактами и выходом. Она отвечает на вопрос:

> «Как провести изменение производственного процесса так, чтобы оно осталось управляемым?»

## 18. Статус

**STRONG-CANDIDATE / NON-CANON**

Следующая проверка: сравнить PPCR с более общими Change Control mechanisms и
с другими источниками, чтобы определить, является ли конструкция
MULTI-SOURCE CONFIRMED.
