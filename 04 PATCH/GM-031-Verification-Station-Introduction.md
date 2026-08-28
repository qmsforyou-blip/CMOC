# GM-031 — Verification Station: Introduction

**Извещение на изменение:** 0142+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Раздел SOURCE:** 3.0 — Introduction, Verification Station  
**Статус:** CANDIDATE / SINGLE-SOURCE

---

## 1. SOURCE

GM определяет **Verification Station (VS)** как систему построения качества непосредственно на рабочем месте через:

- prevention — предотвращение;
- detection — обнаружение;
- containment of abnormalities — локализацию отклонений.

Цель VS сформулирована как проверка того, что процесс выдаёт именно тот результат, который он был спроектирован выдавать.

SOURCE также задаёт назначение VS: улучшение First Time Quality (FTQ) и process capability, обнаружение изменений процесса, понимание того, кого и когда вызывать для помощи, получение необходимой поддержки при возникновении проблем, предотвращение escape дефектов, вовлечение команды в Problem Solving и обеспечение feedback от downstream customers.

Область применения: Manufacturing Operations, Assembly Areas и места, где реализована 100% Inspection или containment. Владение процессом относится к Manufacturing Leadership; поддержка обеспечивается Manufacturing, Engineering, Materials и Quality leadership/staff.

---

## 2. LOCATION

**p. 74–77**, раздел **3.0 — Introduction**, переход к **3.2 — Description, Roles, Responsibility**.

SOURCE также определяет VS на p. 76 как систему building quality in station через prevention, detection и containment.

---

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Verification Station (VS)** | станция верификации / контрольная станция |
| **Build Quality in Station** | встраивать качество непосредственно на рабочем месте |
| **Prevention** | предотвращение |
| **Detection** | обнаружение |
| **Containment** | локализация / удержание отклонения под контролем |
| **Abnormality** | отклонение / аномалия |
| **Process** | процесс |
| **Design Intent** | замысел / заданное предназначение процесса |
| **First Time Quality (FTQ)** | качество с первого прохода |
| **Process Capability** | способность процесса обеспечивать требуемый результат |
| **Escape of Defects** | выход дефектов за пределы контролируемого процесса |
| **Downstream Customer** | следующий / последующий потребитель процесса |
| **Manufacturing Operations** | производственные операции |
| **Assembly Areas** | сборочные зоны |
| **100% Inspection** | стопроцентный контроль |
| **Ownership** | владение / ответственность за процесс |
| **Manufacturing Leadership** | руководство производством |

---

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### DIS-GM-031-01
**Verification Station ≠ просто Inspection Point.**

SOURCE определяет VS как систему, объединяющую prevention, detection и containment, а не только обнаружение дефекта.

### DIS-GM-031-02
**Detection ≠ Prevention ≠ Containment.**

GM называет их тремя различными функциями внутри VS.

### DIS-GM-031-03
**Checking the process output ≠ просто проверка продукта.**

Цель сформулирована через вопрос, выдаёт ли процесс то, что он был спроектирован выдавать. Объектом проверки тем самым выступает связь между фактическим результатом и design intent процесса.

### DIS-GM-031-04
**Verification Station ≠ самостоятельное решение проблемы.**

VS должна вовлекать команду в Problem Solving и обеспечивать поддержку, но SOURCE не определяет саму VS как замену Problem Solving.

### DIS-GM-031-05
**Containment in VS ≠ автоматически Containment из раздела 2.0.**

Термин повторяется, но его тождество с конкретным механизмом Control of Nonconforming Product пока не устанавливаем.

---

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

- “Verification Stations” are the “system of building quality in station through prevention, detection, and containment of abnormalities.”
- “Verification Stations check if your process is giving you what it was designed to give you.”
- VS предназначена, в частности, для улучшения FTQ и process capability, предотвращения escape дефектов и вовлечения Team в Problem Solving.

---

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
PROCESS
   ↓
ACTUAL OUTPUT
   ↓
VERIFICATION STATION
   │
   ├── PREVENTION
   ├── DETECTION
   └── CONTAINMENT OF ABNORMALITIES
   ↓
QUALITY BUILT IN STATION
```

Вторая, целевая конструкция SOURCE:

```text
PROCESS
   ↓
WHAT IT WAS DESIGNED TO GIVE
          ↕
     VERIFICATION
          ↕
ACTUAL PROCESS OUTPUT
```

---

## 7. REL — СВЯЗИ

SOURCE поддерживает:

```text
Verification Station
   ├── Prevention
   ├── Detection
   └── Containment
```

И:

```text
Verification Station
   ↓
Check actual process result
   ↓
Compare with Design Intent
```

Также:

```text
Verification Station
   ↓
Problem Solving
   ↓
Process Improvement
```

Последняя связь здесь фиксируется только на уровне назначения VS; детальная реализация Problem Solving будет разобрана в следующих вагонетках.

---

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Verification-at-Station Mechanism

**Input:** результат процесса на рабочем месте.

**Operation:** обнаружение/предотвращение/локализация отклонений и проверка того, соответствует ли фактический результат тому, что процесс был спроектирован выдавать.

**Output:** обнаруженное и контролируемое отклонение либо подтверждение соответствия ожидаемому результату.

**Organizational effect:** качество проверяется и удерживается непосредственно в месте выполнения процесса; команда получает основание для реакции и Problem Solving.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 9. CAPABILITY — СПОСОБНОСТЬ

**CANDIDATE:**

> **In-Station Quality Verification** — способность процесса/организации своевременно обнаруживать отклонение фактического результата процесса от заданного design intent непосредственно в месте выполнения операции и запускать предусмотренную реакцию.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 10. CORE CANDIDATE

> **Verification Station — организационно-физическая конструкция проверки качества непосредственно в месте выполнения процесса, объединяющая prevention, detection и containment abnormalities и предназначенная для проверки соответствия фактического результата процесса его design intent.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Verification Station

```text
INPUT
Результат процесса
        ↓
[ VERIFICATION AT STATION ]
        │
        ├── prevent
        ├── detect
        └── contain abnormality
        ↓
OUTPUT
Контролируемое состояние процесса
        ↓
EFFECT
Качество удерживается непосредственно
в месте выполнения процесса
```

На уровне этого фрагмента инженерный тест выполняется достаточно для **CANDIDATE**:

- **Input:** фактический результат процесса;
- **Operation:** verification + prevention/detection/containment;
- **Output:** обнаруженное/удержанное отклонение или подтверждённый результат;
- **Effect:** quality built in station.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Не утверждаем пока, что вся последующая архитектура VS является одной машинкой. Детальные alarm, immediate response, leadership support, feedback и performance metrics будут извлекаться отдельно.

---

## 12. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED

```text
Process
   ↓
Verification Station
   ↓
Prevention / Detection / Containment
   ↓
Quality built in station
```

Целевая проверочная связь:

```text
Actual Process Result
        ↕
Design Intent
        ↓
Verification
```

Не добавляем пока конкретный алгоритм принятия решения: SOURCE Introduction его ещё не раскрывает.

---

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не назначается.

---

## 14. CMOC INTERPRETATION — ИНТЕРПРЕТАЦИЯ CMOC

Здесь появляется новая для нашего прохода конструкция:

> **Качество можно проверять не после завершения процесса, а непосредственно в месте его выполнения, одновременно создавая механизм предотвращения, обнаружения и локализации отклонения.**

Особенно важна формула:

```text
DESIGN INTENT
      ↕
ACTUAL RESULT
      ↓
VERIFICATION
      ↓
REACTION / IMPROVEMENT
```

Но последняя строка пока является нашей интерпретацией общей логики SOURCE; конкретная реакция будет добыта в следующих вагонетках.

---

## 15. INTER-SOURCE NOTE

Потенциально интересная точка для последующего сопоставления с ISO/DIS 9001:2025: verification of process output, monitoring/measurement, nonconforming outputs и corrective action. В этом PATCH межисточниковое подтверждение не проводится.

---

## 16. ПЕРЕХОД К СЛЕДУЮЩЕЙ ВАГОНЕТКЕ

Следующий естественный фрагмент SOURCE — **3.1 Benefits**, затем **3.2 Description, Roles, Responsibility**.

Не объединять их с GM-031 задним числом: GM-031 фиксирует именно Introduction и базовую конструкцию Verification Station.
