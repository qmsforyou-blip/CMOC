# GM-026 — Reusable / Rework / Repair

**Извещение на изменение:** 0137+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел источника:** 2.5.1 — Reusable; (rework/repair)  
**Статус:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE — ЧТО ГОВОРИТ GM

GM для reusable product, который проходит rework/repair, требует три вещи:

- **Work Instruction** для выполнения rework;
- метод идентификации scrap и обеспечения **rework product traceability**;
- **Customer Approval** может потребоваться.

В SOURCE это находится внутри раздела **2.5 — DISPOSITION (Reusable or scrap)**.

Важно: этот фрагмент не описывает подробно саму технологию rework/repair. Он задаёт условия, при которых такое действие должно быть управляемым и прослеживаемым.

---

## 2. LOCATION

**Source, p. 69 — 2.5.1 Reusable; (rework/repair).**

---

## 3. TERMS — ТЕРМИНЫ

| English | Русский | Роль в SOURCE |
|---|---|---|
| **Reusable** | пригодный для повторного использования | состояние/маршрут продукта |
| **Rework** | доработка | действие по приведению продукта в соответствие |
| **Repair** | ремонт | действие над продуктом; SOURCE не раскрывает технологию отдельно |
| **Work Instruction** | рабочая инструкция | управляемая инструкция выполнения rework |
| **Scrap** | брак / продукция на списание | отдельный статус/маршрут |
| **Traceability** | прослеживаемость | возможность проследить rework product |
| **Rework Product** | дорабатываемая продукция | объект, для которого требуется traceability |
| **Customer Approval** | одобрение заказчика | условие, которое может потребоваться |
| **Disposition** | решение о дальнейшей судьбе продукции | родительский контур |

---

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### DIS-GM-026-01
**Reusable ≠ Rework/Repair.**

Reusable описывает возможность дальнейшего использования продукта; rework/repair — действия, посредством которых с продуктом работают для достижения допустимого состояния. SOURCE не следует трактовать как определение этих терминов.

### DIS-GM-026-02
**Rework ≠ Work Instruction.**

Rework — действие. Work Instruction — управляемый способ его выполнения.

### DIS-GM-026-03
**Rework ≠ Traceability.**

Выполнение rework не обеспечивает автоматически прослеживаемость. GM отдельно требует метод идентификации scrap и traceability rework product.

### DIS-GM-026-04
**Traceability ≠ Identification.**

Идентификация позволяет распознать объект/статус; traceability позволяет проследить rework product. Не объединять без дополнительного SOURCE.

### DIS-GM-026-05
**Customer Approval ≠ обязательное условие во всех случаях.**

GM формулирует: “Customer approval may be required.” Поэтому нельзя превращать это в безусловное требование.

### DIS-GM-026-06
**Work Instruction ≠ технологический процесс как таковой.**

SOURCE требует наличие инструкции для выполнения rework, но этот фрагмент не раскрывает её содержание и не даёт основания реконструировать полный технологический процесс.

---

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

- **“A work instruction to perform rework.”** — рабочая инструкция для выполнения доработки.
- **“A method to identify scrap and rework product traceability.”** — метод идентификации брака и обеспечения прослеживаемости дорабатываемой продукции.
- **“Customer approval may be required.”** — одобрение заказчика может потребоваться.

---

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

SOURCE задаёт минимальную управляемую конструкцию rework/repair:

```text
NONCONFORMING PRODUCT
        ↓
   REWORK / REPAIR
        ↓
┌──────────────────────────────┐
│ Work Instruction             │
│ Traceability method          │
│ Customer Approval if needed  │
└──────────────────────────────┘
        ↓
 REUSABLE PRODUCT
```

Но SOURCE этого фрагмента **не утверждает**, что каждый rework автоматически приводит к reusable product; слово Reusable является заголовком/контекстом disposition.

---

## 7. REL — СВЯЗИ

Подтверждаемая локальная связь:

```text
Disposition
   ↓
Reusable / Rework / Repair
   ↓
Work Instruction
   +
Traceability Method
   +
Customer Approval (if required)
```

Связь с предыдущими вагонетками:

```text
GM-023 / GM-024
Containment
      ↓
GM-025
Disposition
      ↓
GM-026
Reusable / Rework / Repair
```

Не утверждаем пока переход **Rework → Reintroduce**: он раскрывается в следующей части SOURCE — 2.5.2 Reintroduce Product.

---

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Controlled Rework Mechanism

**Input:** nonconforming product, направленный на rework/repair.

**Transformation:** выполнить rework по Work Instruction с обеспечением идентификации/прослеживаемости; при необходимости получить Customer Approval.

**Output:** управляемо обработанный rework product, статус и история которого могут быть прослежены.

**Организационный эффект:** rework перестаёт быть неформальным исправлением и получает воспроизводимый способ выполнения и контроля прослеживаемости.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 9. CAPABILITY — СПОСОБНОСТЬ

**NONE**

В этом фрагменте SOURCE не даёт достаточно оснований выделять самостоятельную Capability.

---

## 10. CORE CANDIDATE

> **Controlled Rework — воспроизводимая организация доработки несоответствующей продукции посредством установленной рабочей инструкции, метода идентификации и прослеживаемости дорабатываемой продукции и, когда требуется, одобрения заказчика.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Controlled Rework

```text
INPUT
Nonconforming Product
        ↓
[ CONTROLLED REWORK ]
        │
        ├── Work Instruction
        ├── Identification
        ├── Traceability
        └── Customer Approval if required
        ↓
OUTPUT
Controlled Rework Product
        ↓
EFFECT
Rework becomes a defined,
traceable organizational operation
```

### Инженерный тест

**INPUT** — несоответствующая продукция.  
**OPERATION / TRANSFORMATION** — доработка по установленной инструкции с контролем идентификации и traceability.  
**OUTPUT** — продукт после управляемой доработки с возможностью прослеживания.  
**ORGANIZATIONAL EFFECT** — исключение неформальной/непрослеживаемой доработки.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Важно: **Work Instruction сама по себе пока не выделяется как отдельная Machine**. Она является обязательной реализацией/элементом Controlled Rework.

---

## 12. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED

```text
Nonconforming Product
        ↓
Rework / Repair
        ↓
Work Instruction
        ↓
Identification + Traceability
        ↓
Customer Approval if required
```

Не расширять эту цепочку за пределы SOURCE.

---

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не назначается.

---

## 14. CMOC INTERPRETATION — ИНТЕРПРЕТАЦИЯ CMOC

Здесь появляется важное инженерное различение:

> **Исправить продукт и управлять исправлением продукта — не одно и то же.**

GM не ограничивается требованием «сделать rework». Она требует, чтобы существовали:

```text
КАК ДЕЛАТЬ
    ↓
Work Instruction

ЧТО ЭТО ЗА ПРОДУКТ
    ↓
Identification

ЧТО С НИМ ПРОИСХОДИЛО
    ↓
Traceability

НУЖНО ЛИ СОГЛАСОВАНИЕ
    ↓
Customer Approval
```

В результате rework становится не просто действием рабочего, а **управляемым маршрутом объекта**.

Это CMOC INTERPRETATION, а не утверждение, что GM использует термин «организационная машинка».

---

## 15. ВАЖНАЯ ГРАНИЦА ДЛЯ GM-027

Следующий фрагмент **2.5.2 — Reintroduce Product** должен быть рассмотрен отдельно.

Нельзя заранее считать, что:

```text
REWORK
→ REINTRODUCE
```

является полной цепочкой. SOURCE отдельно устанавливает для reintroduced product дополнительные требования: выполнение всех Control Plan inspections/tests, возврат в process stream в определённую точку и идентификацию reintroduced product.

---

## 16. ИНТЕР-СВЯЗЬ С CMOC

Потенциально полезна для будущего межисточникового сравнения с ISO/DIS 9001:2025 по управлению несоответствующими выходами, но подтверждение другим источником в этом PATCH не выполняется.
