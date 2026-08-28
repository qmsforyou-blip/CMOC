# GM-028 — Scrap

**Извещение на изменение:** 0139+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Раздел SOURCE:** 2.5.3 — SCRAP  
**STATUS:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE — ИСТОЧНИК

GM требует от поставщика иметь процедуру, обеспечивающую, что scrap:

- отслеживается (**tracked**);
- предотвращается его повторное введение в процесс или нормальный поток материала (**prevented from being reintroduced to the process or normal material flow**);
- сокращается посредством постоянных усилий команд непрерывного улучшения (**ongoing continuous improvement team efforts**).

Источник не раскрывает в данном фрагменте отдельную технологию физического уничтожения scrap. Поэтому не добавляем её от себя.

---

## 2. LOCATION — РАСПОЛОЖЕНИЕ

**p. 70 — 2.5.3 — SCRAP**, блок **CONTROL OF NONCONFORMING PRODUCT**.

---

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Scrap** | брак / продукция, исключённая из дальнейшего использования |
| **Track** | отслеживать / учитывать движение и состояние |
| **Reintroduce** | повторно вводить |
| **Normal Material Flow** | нормальный поток материала |
| **Procedure** | процедура |
| **Continuous Improvement** | непрерывное улучшение |
| **Continuous Improvement Team** | команда непрерывного улучшения |
| **Effort** | действие / усилие по улучшению |

---

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### DIS-GM-028-01
**Scrap ≠ Nonconforming Product.**

Nonconforming Product — более широкая категория в разделе 2.0. Scrap — один из возможных результатов Disposition.

### DIS-GM-028-02
**Scrap ≠ Segregation.**

Segregation физически отделяет nonconforming/suspect product от нормального потока. Scrap — статус/маршрут продукции после решения о disposition.

### DIS-GM-028-03
**Scrap ≠ просто отсутствие использования.**

GM требует одновременно **tracking** и предотвращения reintroduction в процесс или normal material flow.

### DIS-GM-028-04
**Scrap Control ≠ только предотвращение возврата.**

GM добавляет самостоятельное требование: scrap должен сокращаться через ongoing continuous improvement team efforts.

### DIS-GM-028-05
**Tracking ≠ Disposition.**

Отслеживание scrap не означает, что tracking сам определяет его disposition.

### DIS-GM-028-06
**Continuous Improvement ≠ исправление конкретного scrap.**

В SOURCE improvement относится к снижению самого объёма scrap, а не просто к обработке уже возникшего брака.

---

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

- **“Suppliers shall have a procedure to ensure that scrap:”**
- **“Is tracked and prevented from being reintroduced to the process or normal material flow.”**
- **“Scrap is reduced through on-going continuous improvement team efforts.”**

---

## 6. EXTRACTION — ДОБЫЧА

Источник задаёт для scrap тройную конструкцию:

```text
SCRAP
  ↓
┌─────────────────────────────┐
│ TRACK                       │
│             +               │
│ PREVENT REINTRODUCTION      │
│             +               │
│ REDUCE THROUGH CI           │
└─────────────────────────────┘
```

Это уже не просто конечный статус изделия.

GM требует управлять **дальнейшей судьбой scrap** и одновременно работать на уменьшение его возникновения.

---

## 7. REL — СВЯЗИ

### Связь с GM-025 — Disposition

```text
NONCONFORMING PRODUCT
        ↓
    DISPOSITION
        ↓
      SCRAP
```

### Связь с GM-022 — Segregation

```text
NONCONFORMING PRODUCT
        ↓
    SEGREGATION
        ↓
      SCRAP
        ↓
TRACK + PREVENT REINTRODUCTION
```

### Внутренняя связь GM-028

```text
SCRAP
  ├──→ TRACK
  ├──→ PREVENT REINTRODUCTION
  └──→ REDUCE THROUGH CI
```

Не утверждаем, что эти три операции всегда выполняются как линейная последовательность: SOURCE задаёт их как требования к процедуре.

---

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Scrap Control Mechanism

**Input:** продукция, получившая статус scrap.

**Transformation:** отслеживание scrap + предотвращение его возврата в процесс/normal material flow + работа команд непрерывного улучшения на снижение scrap.

**Output:** контролируемый scrap, исключённый из нормального потока и включённый в контур учёта и улучшения.

**Organizational effect:** предотвращается повторное попадание scrap в поток и создаётся обратная связь для снижения его возникновения.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 9. CAPABILITY — СПОСОБНОСТЬ

**NONE**

Отдельная capability из данного фрагмента SOURCE не извлекается.

---

## 10. CORE CANDIDATE — КАНДИДАТ ЯДРА

> **Scrap Control — воспроизводимый механизм управления продукцией, отнесённой к scrap, посредством её отслеживания, предотвращения повторного введения в процесс или нормальный поток материала и систематического снижения scrap через деятельность команд непрерывного улучшения.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Scrap Control

```text
INPUT
Scrap
  ↓
[ TRACK ]
  +
[ PREVENT REINTRODUCTION ]
  ↓
CONTROLLED SCRAP
  ↓
[ CONTINUOUS IMPROVEMENT ]
  ↓
REDUCED SCRAP
```

Инженерный тест выполняется на уровне совокупного механизма:

- **INPUT:** scrap;
- **OPERATION:** tracking + prevention of reintroduction;
- **OUTPUT:** controlled scrap / no reintroduction;
- **ORGANIZATIONAL EFFECT:** reduction of scrap through continuous improvement.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Важно: SOURCE не даёт достаточных оснований объявлять отдельными Machine конкретные средства tracking или физического уничтожения scrap.

---

## 12. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED

```text
Disposition
    ↓
Scrap
    ↓
Track
    ↓
Prevent Reintroduction
    ↓
Continuous Improvement
    ↓
Reduce Scrap
```

Но в строгом смысле последние три элемента являются **параллельными требованиями к процедуре**, а не обязательно последовательными стадиями.

---

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

---

## 14. CMOC INTERPRETATION — ИНТЕРПРЕТАЦИЯ CMOC

Здесь появляется интересное различение:

> **Scrap — не просто конечная судьба объекта. Он становится входом в контур управления потерями.**

GM связывает два временных горизонта:

```text
СЕЙЧАС
SCRAP
  ↓
TRACK
  ↓
PREVENT REINTRODUCTION

БУДУЩЕЕ
SCRAP
  ↓
CONTINUOUS IMPROVEMENT
  ↓
REDUCE
```

То есть контроль уже возникшего scrap и изменение способности системы производить scrap — разные операции.

Это **CMOC INTERPRETATION**, а не утверждение GM о CMOC.

---

## 15. ВАЖНАЯ ГРАНИЦА С GM-027

```text
GM-027
REINTRODUCE PRODUCT
        ↓
контролируемый возврат
соответствующего продукта
в process stream

GM-028
SCRAP
        ↓
возврат запрещён
в process / normal material flow
```

Это не симметричные операции одного типа:

**Reintroduce** — управляемый возврат в поток.

**Scrap Control** — управляемое исключение из потока.

---

## 16. INTER-SOURCE NOTE

Конструкция потенциально сопоставима с ISO/DIS 9001:2025 в части управления несоответствующими выходами и предотвращения непреднамеренного использования, однако в этом PATCH межисточниковое подтверждение не заявляется.
