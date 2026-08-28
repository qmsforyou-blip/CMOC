# GM-036 — Defects Entering Verification Station

**Извещение на изменение:** 0147+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.3 — Defects Entering the Station  
**Статус:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE

На странице 84 SOURCE определяет эту конструкцию предельно кратко:

> **Defects Entering VS Station — Checking the part for defects and raising Alarms.**

То есть входящий в Verification Station объект проверяется на дефекты, после чего при обнаружении дефекта поднимается Alarm.

Следующая страница SOURCE уже отдельно раскрывает **Alarm and Escalation**: пределы Alarm устанавливаются в зависимости от типа и количества обнаруженных дефектов. Поэтому подробные правила Alarm Limits не смешиваем с GM-036 и добываем отдельной вагонеткой.

---

## 2. LOCATION

**p. 84 — 3.3 Defects Entering the Station / Verification Station.**

---

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Defects Entering the Station** | дефекты, входящие на станцию |
| **Verification Station (VS)** | станция верификации |
| **Checking the Part** | проверка детали |
| **Defect** | дефект |
| **Raising an Alarm** | подача / инициирование сигнала тревоги |
| **Alarm** | сигнал тревоги / сигнал отклонения |
| **Inspection** | контроль / проверка |
| **Part** | деталь / изделие |

---

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### DIS-GM-036-01 — Checking ≠ Alarm

Проверка детали и поднятие Alarm — разные операции.

```text
CHECK
  ↓
DEFECT FOUND
  ↓
ALARM
```

### DIS-GM-036-02 — Defect ≠ Alarm

Дефект — обнаруженное состояние объекта.
Alarm — механизм сообщения / сигнализации об этом состоянии.

Не смешиваем объект контроля и сигнал.

### DIS-GM-036-03 — Detection ≠ Escalation

В GM-036 SOURCE говорит только о **checking** и **raising Alarms**.
Правила уровней Alarm и дальнейшей эскалации находятся в следующем фрагменте SOURCE.

### DIS-GM-036-04 — Inspection ≠ Problem Solving

На этом фрагменте нет утверждения, что сама проверка решает проблему. Problem Solving появляется дальше как отдельная конструкция.

---

## 5. GM-FORMULATIONS

> **Defects Entering VS Station**

> **Checking the part for defects and raising Alarms**

Это две основные SOURCE-формулировки GM-036.

---

## 6. EXTRACTION

```text
PART ENTERS VS
      ↓
CHECK PART FOR DEFECTS
      ↓
DEFECT?
   ↓       ↓
 NO       YES
 ↓          ↓
CONTINUE   RAISE ALARM
```

Последний шаг фиксируем как SOURCE-supported, но не расширяем пока до конкретного механизма эскалации.

---

## 7. REL

Подтверждённая связь:

```text
Part
 ↓
Checking
 ↓
Defect Detection
 ↓
Alarm
```

Следующая связь:

```text
Alarm
 ↓
Alarm Limits / Escalation
```

относится уже к следующей вагонетке SOURCE.

---

## 8. MECHANISM

### CANDIDATE — Defect Detection and Alarm Mechanism

**Input:** деталь / изделие, поступающее на Verification Station.

**Operation:** проверка детали на наличие дефектов.

**Output:** обнаруженный дефект получает связанный с ним Alarm.

**Организационный эффект:** наличие дефекта становится сигналом, на который может реагировать система VS.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Оговорка: SOURCE данного фрагмента не раскрывает ещё конкретный способ проверки, тип сигнала или правила порогов. Поэтому их сюда не добавляем.

---

## 9. CAPABILITY

### CANDIDATE — In-Station Defect Detection

> Способность организации обнаруживать дефекты непосредственно при прохождении детали через Verification Station и инициировать сигнал о таком обнаружении.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 10. CORE CANDIDATE

> **Defect Detection and Alarm — воспроизводимая конструкция Verification Station, связывающая проверку детали на наличие дефекта с инициированием Alarm при его обнаружении.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 11. MACHINE

### CANDIDATE MACHINE — Defect Detection & Alarm

```text
INPUT
Part
  ↓
[ CHECK FOR DEFECTS ]
  ↓
OUTPUT
Defect detected
  ↓
[ RAISE ALARM ]
  ↓
EFFECT
Defect becomes a
recognized signal for action
```

Инженерный тест:

- **INPUT:** Part;
- **OPERATION:** Checking;
- **OUTPUT:** Defect detection + Alarm;
- **ORGANIZATIONAL EFFECT:** возможность дальнейшей реакции системы.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

При этом конкретные Alarm Levels, escalation и immediate response здесь сознательно не включены.

---

## 12. CHAIN

SOURCE поддерживает только короткую цепочку:

```text
Part
 ↓
Check
 ↓
Defect
 ↓
Alarm
```

Не достраиваем её до escalation, containment или problem solving — это следующие фрагменты SOURCE.

---

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

---

## 14. CMOC INTERPRETATION

Здесь появляется очень чистое различение:

> **Обнаружение дефекта ещё не является управлением дефектом.**

GM-036 фиксирует только первый переход:

```text
СОСТОЯНИЕ ОБЪЕКТА
      ↓
ОБНАРУЖЕНИЕ
      ↓
СИГНАЛ
```

Следующий вопрос системы — **что она делает с этим сигналом**. SOURCE отвечает на него уже в конструкции Alarm and Escalation.

Поэтому GM-036 сама по себе не должна поглощать GM-037 и последующие механизмы.

---

## 15. ГРАНИЦА С GM-031—035

GM-031 — назначение Verification Station.

GM-032 — ожидаемые Benefits.

GM-033 — работа VS и распределение ролей.

GM-034 — Information Board.

GM-035 — Template / управленческая карта VS.

GM-036 — **первичная операция внутри VS: проверить деталь и при обнаружении дефекта поднять Alarm.**

Таким образом, GM-036 переводит нас от архитектуры VS к её операционному контуру.

---

## 16. INTER-SOURCE NOTE

Конструкция потенциально сопоставима с CMOC-различением **обнаружение → сигнал → реакция**, но межисточниковое подтверждение здесь не заявляется.

---

## 17. FIXATION

PATCH создан непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
