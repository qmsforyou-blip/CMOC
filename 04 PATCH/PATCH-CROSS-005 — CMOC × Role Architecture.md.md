---
patch_id: PATCH-CROSS-005
name: CMOC × Role Architecture

source:
  - Имаи Масааки — «Гемба кайдзен»
source_section:
  - глава 10

status: WORKING
type: CROSS-PATCH
---

# PATCH-CROSS-005 — CMOC × Role Architecture

## 1. Назначение

Сверка материала главы 10 Имаи Масааки
с текущими кандидатами CMOC.

Патч фиксирует результат сверки.
Сам по себе не изменяет канон.

---

## 2. CONFIRM / UPDATE

### DIS

- Role ≠ Responsibility
- Role ≠ Capability

### REL

- Role → Responsibility
- Role → Scope / Object
- Role → Capability
- Role → Performance Assessment
- Training → Capability

---

## 3. NEW CANDIDATES

### DIS

**Role Definition ≠ Role Enablement**

Рабочая интерпретация:

> Формальное определение того, что требуется от роли,
> не тождественно условиям, позволяющим роли реально
> выполнять требуемую функцию.

Status: SINGLE-SOURCE / CANDIDATE

---

### REL

**Management System → supports → Role**

Status: SINGLE-SOURCE / CANDIDATE

**Role → uses → Machine**

Status: SINGLE-SOURCE / CANDIDATE

---

### CAP

**Ability to perform role responsibility**

Status: MULTI-CONFIRMED WITHIN SOURCE

---

## 4. ROLE-CANDIDATE

### ROLE-CANDIDATE-001

Рабочая конструкция роли:

```text
ROLE
+
EXPECTED ACTIONS
+
RESPONSIBILITY
+
SCOPE / OBJECT
+
CAPABILITY
+
SYSTEM SUPPORT
+
PERFORMANCE ASSESSMENT

```
Status:
MULTI-CONFIRMED WITHIN SOURCE
+++

## 5. ROLE-CHAIN

### ROLE-CHAIN-CANDIDATE-001

```
POLICY
↓
GOALS
↓
PROGRESS ANALYSIS
↓
COUNTERMEASURES
↓
RESULTS
```

Тип:

ROLE-CHAIN

Status:

SOURCE-SUPPORTED-CANDIDATE

---

## 6. MACHINE

Новых машинок не выделено.

Подтверждена реализация:

```
ROLE
↓
uses
↓
ANDON
```

---

## 7. SOURCE-SPECIFIC / DROP FROM UNIVERSAL CORE

Следующие элементы не переносятся в универсальное ядро  
как таковые:

- конкретная иерархия ролей TAM;
- конкретные области ответственности TAM;
- конкретная система оценки показателей TAM.

Они сохраняются как материал источника.

---

## 8. M

Новых M не выделено.

---

## 9. CMOC INTERPRETATION

Глава 10 показывает возможную конструкцию:

```
ROLE
↓
RESPONSIBILITY
↓
CAPABILITY
↓
SYSTEM SUPPORT
↓
ACTION
↓
RESULT
↓
ASSESSMENT
```

Это реконструкция CMOC.

Не является утверждением, что Имаи формулирует  
данную схему именно в таком виде.

---

## 10. Решение

PATCH STORED.

CORE NOT MODIFIED.

Кандидаты ожидают дальнейшего подтверждения  
другими источниками.

````

---

# 2. `ROLE-CANDIDATES.md`

В:

```text
02_CANDIDATES/
└── ROLE-CANDIDATES.md
````

Добавляем:

````
# ROLE-CANDIDATES

> Рабочий слой кандидатов архитектуры ролей.
> Не канон CMOC.

---

## ROLE-CANDIDATE-001 — Рабочая конструкция роли

**Status:** MULTI-CONFIRMED WITHIN SOURCE

**Source:** Имаи Масааки, «Гемба кайдзен», глава 10.

### Structure

```text
ROLE
+
EXPECTED ACTIONS
+
RESPONSIBILITY
+
SCOPE / OBJECT
+
CAPABILITY
+
SYSTEM SUPPORT
+
PERFORMANCE ASSESSMENT
````

### Confirmed relations

- Role → Responsibility
- Role → Scope / Object
- Role → Capability
- Role → Performance Assessment
- Training → Capability

### Candidate relations

- Management System → supports → Role
- Role → uses → Machine

### Candidate distinction

```
ROLE DEFINITION
≠
ROLE ENABLEMENT
```

### Status

SINGLE-SOURCE / MULTI-CONFIRMED WITHIN SOURCE

### Next confirmation

Независимый источник.

````

---

# 3. `ROLE-CHAIN-CANDIDATE-001`

Здесь я бы **не смешивал его с Role Candidate**.

Файл:

```text
02_CANDIDATES/
└── ROLE-CHAIN-CANDIDATE-001 — Policy-Goals-Results.md
````

Содержимое:

````
---
chain_id: ROLE-CHAIN-CANDIDATE-001
type: ROLE-CHAIN
status: SOURCE-SUPPORTED-CANDIDATE

source:
  - Имаи Масааки — «Гемба кайдзен», глава 10
---

# ROLE-CHAIN-CANDIDATE-001

## Policy → Goals → Progress → Countermeasures → Results

## Sequence

```text
POLICY
↓
GOALS
↓
PROGRESS ANALYSIS
↓
COUNTERMEASURES
↓
RESULTS
````

## Nature

Последовательность деятельности,  
описываемая Имаи в рамках ответственности  
менеджера участка.

Это не MACHINE-CHAIN.

## Source claim

Источник связывает данные элементы  
с деятельностью менеджера.

## CMOC interpretation

Рабочая гипотеза:

```
REQUIREMENT / POLICY
↓
TARGET / GOAL
↓
OBSERVATION OF PROGRESS
↓
COUNTERMEASURE
↓
RESULT
```

CMOC interpretation ≠ source claim.

## Status

SOURCE-SUPPORTED-CANDIDATE

## Confirmation

Пока SINGLE-SOURCE.

Следующий этап:  
проверка независимым источником.

````

---

# 4. И самое важное — обновляем `MACHINE-CATALOG.md`

**Ничего нового туда не добавляем.**

Только в разделе связей:

```markdown
## Cross-domain relations

### Role → Machine

```text
Role
  ↓ uses
Machine
````

Первый подтверждённый пример:

```
Group Leader
  ↓ uses
Andon
```

Status:

CANDIDATE

````

То есть каталог машинок теперь **знает о существовании роли**, но мы не превращаем Role в Machine.

---

# 5. И ещё одна запись — в `CORE-CANDIDATES.md`

Я бы **не копировал туда весь ROLE-CANDIDATE-001**.

Только то, что потенциально относится к ядру:

```markdown
## CROSS-005 — Role Architecture

### DIS candidates

- Role ≠ Responsibility
- Role ≠ Capability
- Role Definition ≠ Role Enablement

### REL candidates

- Role → Responsibility
- Role → Scope / Object
- Role → Capability
- Role → Performance Assessment
- Management System → supports → Role
- Role → uses → Machine

### CAP candidates

- Ability to perform role responsibility

Source:
Имаи Масааки — «Гемба кайдзен», глава 10

Evidence:
PATCH-CROSS-005
````

Это очень важно:

> **CORE-CANDIDATES остаётся реестром кандидатов ядра, а не копией всех рабочих файлов.**

---

# 6. Получается физическая архитектура

```
CMOC/
│
├── 01_LAB/
│   └── LAB-002 Реестр различений.md
│
├── 02_CANDIDATES/
│   ├── CORE-CANDIDATES.md
│   ├── ROLE-CANDIDATES.md
│   └── ROLE-CHAIN-CANDIDATE-001.md
│
├── 03_MACHINE-CATALOG/
│   ├── MACHINE-CATALOG.md
│   ├── TMP-Machine.md
│   ├── MACHINES/
│   └── CHAINS/
│
└── 04_PATCH/
    └── PATCH-CROSS-005 — CMOC × Role Architecture.md
```

---

## И вот это уже очень хороший результат

Мы физически разделили:

```
LAB
↓
что добыто

CANDIDATES
↓
что может войти в ядро

PATCH
↓
почему мы так решили

MACHINE-CATALOG
↓
как это реализуется

ROLE-CANDIDATES
↓
как организована ответственность

CHAIN
↓
как элементы соединяются
```

А **CORE пока не трогаем**.

