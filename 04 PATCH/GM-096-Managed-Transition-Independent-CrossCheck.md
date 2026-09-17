# GM-096 — Managed Transition: Independent Cross-Check

**Дата:** 17-09-2026  
**Извещение:** 0139+170926  
**Статус:** CROSS-CHECK COMPLETE / NON-CANON

## 1. Цель

Проверить, существует ли за пределами GM-096 воспроизводимая конструкция, соответствующая рабочей гипотезе **Managed Transition**.

Гипотеза была сформирована при разборе GM-096 как обобщение повторяющейся последовательности:

`identify → decide → authorize → controlled transition → verify → accept / return → record`

Задача cross-check — не доказать термин **Managed Transition**, а проверить существование самой конструкции в независимых источниках.

---

## 2. Независимые источники

### 2.1 European Commission JRC — Management of Change

Источник: European Commission / JRC, CIC Management of Change.

Зафиксированы:
- MOC как review and authorization process до реализации изменения;
- применение MOC к постоянным и временным изменениям;
- временное изменение должно иметь определённый срок;
- при завершении временного изменения должна существовать формальная процедура проверки возврата к исходному состоянию либо перехода в новое постоянное состояние;
- перед запуском требуется проверка корректности реализации;
- финальное разрешение даётся после проверки выполнения требований.

Это почти прямое независимое подтверждение конструкции перехода между управляемыми состояниями.

Source: https://minerva.jrc.ec.europa.eu/en/shorturl/technical_working_group_2_seveso_inspections/cic_management_of_change

---

### 2.2 OSHA — Process Safety Management guidance

OSHA указывает, что временные изменения должны иметь установленный и контролируемый срок, подпадать под MOC, а после завершения временного изменения оборудование и процедуры должны быть возвращены к исходному/проектному состоянию. Также предусматриваются документирование, review, approvals/authorization и pre-startup inspection.

Это подтверждает не конкретное название, а тот же общий переход:

`normal state → temporary changed state → controlled return → verified normal/design state`

Source: https://osha.prod.pace.dol.gov/laws-regs/regulations/standardnumber/1910/1910.119AppC

---

### 2.3 Cefic — Guidelines for Managing Change in a Chemicals Supply Chain

Cefic описывает MOC как последовательность:

`identify change → authorization → scope/risk → review and approval → implementation and handover → final completion`

Для временных изменений прямо предусматривается дата review, к которой изменение должно быть отменено.

Это независимо подтверждает наличие управляемого жизненного цикла изменения, а не просто факта изменения.

Source: https://cefic.org/app/uploads/2024/05/Guidelines-for-Managing-Change-in-a-Chemicals-Supply-Chain-2017-GUIDELINES-R-R-S-B-A.pdf

---

### 2.4 WEEC — Management of Change in industrial business

Источник описывает MOC для manufacturing/industrial context через:

`request → classification → baseline/impact → risk/approval → implementation and rollback plan → readiness review → monitor/verify/close`.

Для временного изменения задаются start/end date, scope, extension authority и rollback evidence.

Это особенно близко к нашей гипотезе: переход является управляемым только при наличии точки входа, разрешения, контроля исполнения, проверки и контролируемого выхода.

Source: https://weec.com.tr/en/blog/management-of-change-moc-process/

---

## 3. Cross-source comparison

| Конструкция | JRC | OSHA | Cefic | WEEC |
|---|---:|---:|---:|---:|
| Идентификация изменения | ✓ | ✓ | ✓ | ✓ |
| Оценка / review | ✓ | ✓ | ✓ | ✓ |
| Авторизация | ✓ | ✓ | ✓ | ✓ |
| Ограничение временного состояния | ✓ | ✓ | ✓ | ✓ |
| Контролируемое выполнение | ✓ | ✓ | ✓ | ✓ |
| Проверка реализации | ✓ | ✓ | ✓ | ✓ |
| Формальный выход / возврат | ✓ | ✓ | ✓ | ✓ |
| Документированный close-out | ✓ | ✓ | ✓ | ✓ |

---

## 4. Что подтверждено

Подтверждено независимыми источниками существование устойчивой организационной конструкции:

> **изменение не считается просто событием; оно переводит систему из одного управляемого состояния в другое через идентификацию, оценку, разрешение, контролируемое выполнение, проверку и формальное принятие либо возврат.**

Особенно сильным является повторяющийся мотив временного изменения:

`NORMAL → TEMPORARY CHANGE → VERIFY → RETURN / PERMANENTLY ADOPT → CLOSE`

Следовательно, исходная гипотеза **Managed Transition** имеет независимое межотраслевое подтверждение как **PATTERN**, а не только как обобщение GM-096.

---

## 5. Что НЕ подтверждено

Не подтверждено, что **Managed Transition** является общепринятым названием этой конструкции.

Не следует канонизировать термин только на основании совпадения жизненных циклов.

Также не следует превращать Managed Transition в отдельную Machine: конкретные MOC, Temporary Change, Bypass, PTR и другие конструкции являются реализациями/специализациями разных участков этой общей грамматики.

---

## 6. Отношение к GM-096

GM-096 предоставляет конкретные реализации переходов:

- **PPCR** — управляемый вход в изменение;
- **PTR** — управляемая проба/оценка;
- **Banking** — управляемое состояние материала вне нормального потока;
- **Bypass** — управляемое временное состояние процесса;
- **Verification / Review** — подтверждение состояния;
- **Return / Close** — возврат или завершение.

Независимые источники показывают, что сама логика перехода не является специфической для GM.

---

## 7. CMOC-классификация

**Managed Transition**

- Kind: `PATTERN`
- Status: `STRONG PATTERN CANDIDATE / NON-CANON`
- Evidence: `MULTI-SOURCE CONFIRMED`
- Scope: cross-industry organizational/process change

Рабочая формула:

`STATE A → IDENTIFY → ASSESS → AUTHORIZE → TRANSITION → VERIFY → ACCEPT / RETURN → RECORD`

---

## 8. Architectural consequence

Гипотеза становится сильнее:

```text
PATTERN
Managed Transition
        │
        ├── PPCR
        ├── PTR
        ├── Banking
        ├── Bypass
        ├── Temporary Change / MOC
        └── другие специализированные реализации
```

Таким образом, **Managed Transition не добавляется в Machine Catalog как Machine**.

Он может стать Pattern верхнего уровня, под которым группируются специализированные Machines и Chains.

---

## 9. REG-001 / Canon / Catalog

- REG-001: **без изменений**
- Canon: **без изменений**
- Machine Catalog: **без изменений**
- Existing passports: **без изменения статуса в этом patch**

Следующий шаг — отдельная проверка, достаточно ли уже накопленных независимых источников для создания полноценного **Pattern Passport** для Managed Transition.

**VERDICT: STRONG PATTERN CANDIDATE / MULTI-SOURCE CONFIRMED / NON-CANON**
