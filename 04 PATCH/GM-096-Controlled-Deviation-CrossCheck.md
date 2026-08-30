# GM-096 — Controlled Deviation — Cross-Check

## Извещение на изменение

**0124+300826**

---

## 1. OBJECT OF CHECK

**Controlled Deviation** рассматривается в связи с ранее паспортизированной машиной **Bypass Process Control**.

Вопрос:

> является ли Controlled Deviation родительским CMOC-механизмом, отдельной Machine или просто альтернативным названием Bypass?

**Working verdict:** `GENERIC MECHANISM / PATTERN` → `Bypass Process Control` как специализированная реализация.

---

## 2. SOURCE-DERIVED LOGIC

GM-096 показывает ситуацию, когда нормальное состояние/процесс временно не может быть выполнено и требуется управляемое альтернативное состояние.

Минимальная архитектура:

```text
NORMAL REQUIREMENT
        ↓
DEVIATION IDENTIFIED
        ↓
AUTHORIZED ALTERNATIVE
        ↓
CONTROLLED DEVIATION STATE
        ↓
MONITOR / VERIFY
        ↓
RETURN TO NORMAL
```

Критический элемент — **управляемость отклонения**, а не сам факт отклонения.

---

## 3. CROSS-CHECK WITH BYPASS PROCESS CONTROL

Ранее паспортизированный `Bypass Process Control` имеет более конкретную операционную форму:

`Normal → Authorized Entry → Bypass → Controls/Evidence → Exit Breakpoint → Verified Return`.

Это практически точная специализация общего паттерна Controlled Deviation.

Следовательно:

> **Controlled Deviation ≠ новая параллельная Machine рядом с Bypass Process Control.**

Более экономная архитектура:

```text
Controlled Deviation
        ↓
Bypass Process Control
```

где первый уровень описывает общий тип управляемого перехода, а второй — конкретную организационную реализацию.

---

## 4. DISTINCTIONS

### D-01

**Deviation ≠ Uncontrolled Nonconformity**

Отклонение может быть управляемым, если для него определены условия, ответственность, границы и контроль.

### D-02

**Controlled Deviation ≠ Permission to Ignore Requirement**

Разрешение альтернативного состояния не отменяет исходное требование; оно создаёт контролируемое временное состояние.

### D-03

**Entry ≠ Control**

Факт разрешённого входа в deviation state ещё не обеспечивает его управляемость.

### D-04

**Return ≠ Verified Return**

Возврат к нормальному процессу должен быть подтверждён требуемой проверкой.

### D-05

**Deviation Control ≠ Corrective Action**

Управление временным отклонением удерживает текущую ситуацию; устранение причины — другой контур.

---

## 5. RELATION TO NONCONFORMING PRODUCT CONTROL

Не следует смешивать:

`Controlled Deviation`

и

`Nonconforming Product Control`.

Первый управляет **отклонением процесса/состояния относительно требования**.

Второй управляет **продуктом, уже признанным или подозреваемым как несоответствующий**.

Они могут быть связаны:

```text
Process Deviation
      ↓
Potential Product Impact
      ↓
Nonconforming Product Control
```

Но это не одна Machine.

---

## 6. RELATION TO CHANGE CONTROL

Controlled Deviation также не следует автоматически смешивать с Change Control.

`Change` предполагает намеренное изменение состояния/процесса.

`Deviation` предполагает временное или специальное отступление от установленного состояния/требования.

Они могут пересекаться, но имеют разные триггеры и разные логические границы.

---

## 7. MACHINE TEST

| Test | Result |
|---|---|
| Independent generic domain | NO |
| Reusable control logic | YES |
| Unique operational object | NO |
| Generic entry/exit boundary | YES |
| Independent evidence model | NO |
| Independent acceptance condition | NO |
| Specializations exist | YES — Bypass Process Control |

**Result:** insufficient basis for Top-Level Machine; strong basis for generic mechanism/pattern.

---

## 8. CMOC CLASSIFICATION

**Controlled Deviation:** `MECHANISM / PATTERN CANDIDATE`

**Bypass Process Control:** `SPECIALIZED MACHINE CANDIDATE`

This preserves both abstraction levels without duplication.

---

## 9. ARCHITECTURAL VALUE

The important CMOC contribution is a state model:

```text
APPROVED NORMAL STATE
        ↓
CONTROLLED DEVIATION STATE
        ↓
VERIFIED NORMAL STATE
```

This reveals a general rule:

> **An exception becomes manageable when it is represented as an explicit state with entry conditions, controls, evidence and exit conditions.**

This formulation is a candidate for later Canon comparison with the CMOC State Transition architecture.

---

## 10. FINAL WORKING VERDICT

> **Controlled Deviation is retained as a generic mechanism/pattern. Bypass Process Control remains its source-derived specialized Machine candidate. No separate Controlled Deviation Top-Level Machine is created.**

**STATUS:** `PATTERN / MECHANISM / NON-CANON`

---

## 11. DECISION RECORD

- No new Top-Level Machine created.
- `Bypass Process Control` remains unchanged.
- No REG-001 modification.
- No Canon modification.
- Preserve source provenance.
- Compare later with generic CMOC State Transition and Deviation architectures before Canonization.

**Next check:** determine whether remaining GM-096 candidates add genuinely new Machine boundaries or further instantiate the already discovered control grammar.