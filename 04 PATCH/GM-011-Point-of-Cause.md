# GM-011 — Step 3: Point of Cause

## Извещение на изменение

**0122+280826**

---

## 0. SOURCE

**Источник:** GM Quality System Basics Overview Supplier Audit.pdf  
**Версия:** Quality Systems Basics rev March 2009  
**Раздел:** FAST RESPONSE → 1.3 Problem Solving → Step 3 — Point of Cause  
**Основной фрагмент:** p. 29; продолжение раскрывается в p. 32–33.

---

## 1. LOCATION

p. 29 — **Process 3 Is the Point of Cause! / Go-See; Point of Cause / Where Is the problem happening?**

В фундаментальных принципах Problem Solving GM требует увидеть abnormal occurrence и Point of Cause first hand. fileciteturn112file10

---

## 2. TERMS

- Point of Cause
- Go-See
- Where is the problem happening?
- Process
- Abnormal occurrence
- First hand
- Manufacturing process
- Upstream source
- Statistical Engineering
- Diamonds 1–4
- Process stability
- Design intent
- Special cause

---

## 3. DISTINCTIONS

### DIS-GM-011-01

**Point of Cause ≠ Root Cause.**

В данном месте GM обозначает Point of Cause как место, где проблема происходит. Root Cause — следующий уровень анализа.

### DIS-GM-011-02

**Point of Cause ≠ место обнаружения дефекта.**

GM требует первоначального расследования там, где defect был найден, но если причина находится upstream, расследование проводится также в upstream source. fileciteturn117file0

### DIS-GM-011-03

**Go-See ≠ предположение о месте проблемы.**

GM требует непосредственного наблюдения: увидеть abnormal occurrence и Point of Cause first hand. fileciteturn112file1

### DIS-GM-011-04

**Process stability ≠ отсутствие проблемы.**

Diamonds 1–4 используются для определения, работает ли manufacturing process в соответствии с design intent и для оценки стабильности процесса. fileciteturn117file0

### DIS-GM-011-05

**Out-of-standard / special cause ≠ Statistical Engineering case.**

Если Diamonds 1–4 выявляют out-of-standard condition (special cause), это предотвращает преждевременное применение статистических методов. Если процесс соответствует design intent, а проблема сохраняется, GM переходит к Statistical Engineering. fileciteturn117file13

---

## 4. GM-FORMULATIONS

> “Process 3 Is the Point of Cause!”

> “Go-See; Point of Cause.”

> “Where Is the problem happening?”

> “See abnormal occurrence and Point of Cause first hand.”

> “Initial investigation is done where the defect was found.”

> “If investigation determines the cause of the problem is upstream, then investigation should be conducted at the upstream source as well.” fileciteturn117file0

Все формулировки сохраняются как SOURCE CLAIMS.

---

## 5. EXTRACTION

GM задаёт движение расследования от наблюдаемого дефекта к месту возникновения:

```text
DEFECT / PROBLEM
      ↓
GO-SEE
      ↓
WHERE IS IT HAPPENING?
      ↓
POINT OF CAUSE
      ↓
INITIAL INVESTIGATION
      ↓
IF UPSTREAM → INVESTIGATE UPSTREAM SOURCE
```

Для первичной проверки GM использует Diamonds 1–4: они позволяют быстро определить, есть ли out-of-standard condition / special cause и оценить стабильность процесса. fileciteturn117file0

---

## 6. NOMENCLATURE

Предварительные кандидаты:

- Point of Cause
- Go-See
- Point-of-Cause Investigation
- Diamonds 1–4
- Process Stability
- Design Intent
- Special Cause
- Upstream Source

Не превращаем автоматически термины в Entity или Machine.

---

## 7. CLASSIFICATION

```text
PROBLEM SOLVING
│
├── Step 1 — Define the Problem
├── Step 2 — Contain the Problem
└── Step 3 — Identify the Root Cause
    │
    └── Point of Cause
        ├── Go-See
        ├── Initial Investigation
        ├── Diamonds 1–4
        └── Upstream Investigation if required
```

---

## 8. PASSPORT

### Candidate — Point-of-Cause Investigation

**Type:** CANDIDATE / SINGLE-SOURCE  
**Source role:** непосредственное установление места возникновения проблемы до углублённого анализа причины.

### Candidate — Diamonds 1–4

**Type:** CANDIDATE / SINGLE-SOURCE  
**Source role:** быстрая проверка того, работает ли производственный процесс в соответствии с design intent и присутствует ли out-of-standard / special cause.

---

## 9. RELATIONS

Подтверждённые связи:

```text
Problem
  ↓
Go-See
  ↓
Point of Cause
```

И:

```text
Defect found
  ↓
Initial investigation at finding location
  ↓
Upstream indication
  ↓
Investigation at upstream source
```

И для Diamonds:

```text
Problem identified
  ↓
Diamonds 1–4
  ↓
Process stability / design intent
  ├── out-of-standard / special cause
  └── process meets design intent → Statistical Engineering
```

---

## 10. MECHANISM

### CANDIDATE — Point-of-Cause Investigation

**INPUT:** наблюдаемая проблема / defect.

**OPERATION:** Go-See; непосредственное наблюдение; установление места возникновения; при необходимости движение upstream.

**OUTPUT:** установленный Point of Cause и направление дальнейшего расследования.

**EFFECT:** причинный анализ получает физически/процессно привязанный объект вместо предположительной причины.

### CANDIDATE — Diamonds 1–4 Screening

```text
Problem
 ↓
Diamonds 1–4
 ↓
Is process running to design intent?
 ↓
Special cause / out-of-standard
       OR
Process meets design intent
```

Не объединяем эти два кандидата в одну Machine до дальнейшей проверки.

---

## 11. CAPABILITY

**NONE**

---

## 12. CORE CANDIDATE

> **Point-of-Cause Investigation — воспроизводимая операция непосредственного установления места возникновения проблемы с переходом к upstream source, если расследование у места обнаружения указывает на него.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

Дополнительный кандидат:

> **Diamonds 1–4 — первичная проверка стабильности и соответствия manufacturing process design intent перед применением более глубокого статистического анализа.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 13. MACHINE

### CANDIDATE MACHINE — Point-of-Cause Investigation

```text
INPUT
Observed Problem / Defect
        ↓
GO-SEE
        ↓
Direct observation
        ↓
Locate Point of Cause
        ↓
If upstream indication
→ investigate upstream source
        ↓
OUTPUT
Located Point of Cause
+ defined investigation direction
```

Инженерный эффект: переход от **«где обнаружили»** к **«где возникает»**.

### CANDIDATE MACHINE — Diamonds 1–4

```text
INPUT
Problem
  ↓
PROCESS CHECK
  ↓
Diamonds 1–4
  ↓
OUT-OF-STANDARD / SPECIAL CAUSE
        OR
PROCESS MEETS DESIGN INTENT
  ↓
STATISTICAL ENGINEERING if problem persists
```

Окончательную классификацию оставляем открытой.

---

## 14. CHAIN

### SOURCE-SUPPORTED LOCAL CHAIN

```text
Defect / Problem
 → Go-See
 → Point of Cause
 → Initial Investigation
 → Upstream Investigation if indicated
```

Отдельная локальная цепь:

```text
Problem
 → Diamonds 1–4
 → Process stability / design intent
 → Special Cause OR Statistical Engineering path
```

---

## 15. ASSEMBLY — UPDATE

После GM-009 и GM-010 конструкция Problem Solving теперь выглядит так:

```text
DEFINE THE PROBLEM
        ↓
CONTAIN THE PROBLEM
        ↓
POINT OF CAUSE
        ↓
ROOT CAUSE
```

Важно: **Point of Cause не является Root Cause.** GM-011 находится на переходе от описания/containment к причинному анализу.

---

## 16. STATUS

**CANDIDATE / SINGLE-SOURCE**

### CONFIRM / UPDATE

**UPDATE GM-008:** принцип “See abnormal occurrence and Point of Cause first hand” получает конкретизацию через Go-See и вопрос “Where is the problem happening?”. fileciteturn112file1

**UPDATE GM-010:** после containment расследование привязывается к Point of Cause; при необходимости GM требует движения upstream.

**NO CANON.**

---

## 17. CMOC INTERPRETATION

Главная добыча GM-011:

> **Место обнаружения проблемы не принимается автоматически за место её возникновения. Организация должна пойти к процессу, увидеть abnormal occurrence first hand и установить Point of Cause; если причина уходит upstream, расследование должно двигаться туда.**

Это даёт сильное инженерное различение:

```text
WHERE FOUND
     ≠
WHERE CAUSED
```

А Diamonds 1–4 добавляют второй важный слой:

```text
POINT OF CAUSE
      ↓
IS THE PROCESS RUNNING TO DESIGN INTENT?
      ↓
SPECIAL CAUSE
      OR
PROCESS STABLE → DEEPER STATISTICAL PATH
```

Пока оба элемента остаются **CANDIDATE / SINGLE-SOURCE**.

---

## SOURCE REFERENCE

Источник: `GM Quality System Basics Overview Supplier Audit.pdf`, pp. 26, 29, 32–33.  
Ключевые SOURCE-фрагменты подтверждены поиском File Library. fileciteturn112file1 fileciteturn117file0 fileciteturn117file13
