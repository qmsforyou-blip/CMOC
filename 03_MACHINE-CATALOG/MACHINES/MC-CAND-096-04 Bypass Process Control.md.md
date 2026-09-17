---
machine_id: MC-CAND-096-04
name: Bypass Process Control

source: GM Quality System Basics rev March 2009 — Managing Change
source_location: pp. 340–343

level: MACHINE
type: CHANGE IMPLEMENTATION / BYPASS CONTROL

problem: >
  Штатный производственный процесс может временно оказаться недоступным
  или быть изменён так, что выполнение выходит за пределы утверждённого
  документированного Control Plan.

purpose: >
  Обеспечить управляемое выполнение производства в состоянии bypass,
  определить минимальные требования к входу и выходу из bypass и обеспечить
  проверку возврата к исходному процессу.

trigger_mode: controlled exception
trigger: >
  Необходимость изменить процесс вне утверждённого документированного
  Control Plan.

input:
  - описание bypass / отклонения
  - исходный утверждённый процесс
  - требования к tooling / inspection / audit
  - точки входа и выхода
  - необходимые approvals

actions:
  - определить breakpoint для входа в bypass
  - определить минимальные требования bypass
  - зафиксировать tooling / inspection / audit requirements
  - обеспечить обучение / сертификацию операторов
  - включить bypass в ежедневный Fast Response review
  - выполнить LPA для каждого bypass
  - перед возвратом проверить параметры и настройки
  - валидировать parts перед возвратом
  - получить Operations Manager approval на возврат
  - зафиксировать выход из bypass

output_type: CONTROLLED RETURN / VERIFIED PROCESS STATE
output: >
  Документированный и проверенный возврат к исходному процессу
  либо управляемое продолжение производства в установленном bypass-состоянии.

roles:
  - Operations Manager
  - responsible production personnel
  - operators
  - quality personnel

artifacts:
  - Manufacturing Process Backup Worksheet
  - documented Control Plan / original process
  - bypass action plan
  - training / certification records
  - LPA records
  - verification / validation records

mechanism: >
  bypass identification → breakpoint control → minimum requirements →
  monitoring / audit → operator qualification → parameter verification →
  part validation → authorized return

capability: >
  Управлять временным или альтернативным состоянием производственного процесса
  без потери требований к контролю, прослеживаемости и проверке возврата.

invokes:
  - Controlled Deviation
  - Response to Abnormality
  - Audit / LPA
  - Verification mechanisms

feeds:
  - verified process state
  - return-to-normal decision

checks:
  - bypass requirements
  - operator qualification
  - tooling / inspection / audit requirements
  - active bypass status
  - parameters / settings before return
  - parts before return

improves: []
standardizes:
  - bypass entry / exit requirements
replicates: []
composes:
  - controlled deviation
  - response to abnormality
  - audit / LPA
  - verification
  - authorization

conditions:
  - original process / Control Plan is defined
  - bypass is explicitly identified
  - entry / exit breakpoints are defined
  - operators are trained / certified
  - verification is performed before return

limitations:
  - The reviewed GM pages establish Bypass Process Control as a specialized construction within Managing Change; they do not prove a universal Bypass Machine across domains.
  - Bypass is specifically associated with process execution outside the approved documented Control Plan.
  - Bypass does not replace the underlying change-control architecture.

cmoc_links:
  - Normal Process → Bypass State
  - Bypass State → Controlled Deviation
  - Controlled Deviation → Verification
  - Verification → Return to Normal State
  - Managing Change → Chain

source_claim: >
  GM QSB defines Bypass Process Control for cases where the process is altered
  outside the approved documented Control Plan. The Manufacturing Process Backup
  Worksheet records entering / exiting breakpoints and requirements for tooling,
  inspection and audit. Active bypasses are reviewed in daily Fast Response;
  each bypass receives LPA; operators are trained / certified; before return,
  parameters and settings are verified, parts are validated, and Operations
  Manager approves the return.

cmoc_interpretation: >
  Specialized, bounded construction for controlling production while the normal
  process is unavailable or deliberately bypassed. Its distinctive identity is
  not deviation itself, but the complete managed bypass lifecycle: controlled
  entry, defined safeguards, active monitoring, operator qualification,
  verification and authorized return.

status: SPECIALIZED-CANDIDATE / NON-CANON
---
# Bypass Process Control

## 1. Что это

Воспроизводимая конструкция управления производством в состоянии bypass,
когда выполнение выходит за пределы утверждённого документированного процесса.

## 2. Проблема

Производство может временно работать не по штатному процессу. Само наличие
отклонения ещё не обеспечивает управляемость перехода, работы в bypass и
возврата к нормальному состоянию.

## 3. Назначение

Удержать bypass в определённых границах и обеспечить проверенный возврат
к исходному процессу.

## 4. Триггер

Необходимость изменить процесс вне утверждённого документированного
Control Plan.

## 5. Вход

Описание bypass, исходный процесс, требования к tooling / inspection / audit,
breakpoints и необходимые согласования.

## 6. Действия

1. Определить breakpoint входа.
2. Определить минимальные требования bypass.
3. Зафиксировать требования к tooling, inspection и audit.
4. Обучить / сертифицировать операторов.
5. Включить активный bypass в Fast Response review.
6. Провести LPA для каждого bypass.
7. Перед возвратом проверить параметры и настройки.
8. Валидировать parts.
9. Получить approval Operations Manager.
10. Зафиксировать выход из bypass.

## 7. Выход

Проверенное состояние процесса и авторизованный возврат к исходному
процессу.

## 8. Роли

Operations Manager, производственный персонал, операторы, quality personnel.

## 9. Артефакты

Manufacturing Process Backup Worksheet, исходный Control Plan, bypass action
plan, records обучения / сертификации, LPA records, verification / validation
records.

## 10. Реализуемый механизм

`entry → safeguards → monitoring → qualification → verification → validation → authorized return`

## 11. Развиваемая способность

Управлять временным отклонением производственного процесса так, чтобы
отклонение оставалось контролируемым и имело проверяемую точку возврата.

## 12. Связи с другими машинками

- Controlled Deviation — более общий механизм / паттерн.
- Fast Response / Andon — реакция и обзор активного abnormal state.
- LPA / Audit — периодическая проверка.
- Verification — проверка условий возврата.

## 13. Условия применения

Должны быть определены исходный процесс, bypass, breakpoints и минимальные
требования; операторы должны быть обучены / сертифицированы.

## 14. Ограничения

Bypass Process Control — специализированная конструкция GM QSB. Рассматривать
её как универсальную Machine для любого вида управляемого отклонения пока
нельзя.

## 15. Связи с CMOC

`Normal State → Bypass → Verification → Return to Normal State`

При этом `Controlled Deviation` является более общей абстракцией, а Bypass
содержит собственную замкнутую процедуру управления состоянием процесса.

## 16. Что утверждает источник

GM QSB устанавливает требования к входу и выходу из bypass, breakpoint,
tooling / inspection / audit requirements, обучению операторов, Fast Response,
LPA, проверке параметров и settings, validation parts и approval Operations
Manager перед возвратом.

## 17. Что выделено нами для CMOC

Ключевой кандидатный признак — **управляемый жизненный цикл исключительного
состояния процесса**, а не просто факт отклонения.

Поэтому Bypass можно пока сохранить как специализированную Machine-кандидата,
но его независимость от общего `Controlled Deviation` требует дальнейшего
cross-check по независимым источникам.

## 18. Статус

**SPECIALIZED-CANDIDATE / NON-CANON**

Следующая проверка: сравнить Bypass Process Control с общей конструкцией
Controlled Deviation и с независимыми практиками contingency / alternate
process control.
