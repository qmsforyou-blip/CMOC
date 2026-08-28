# GM-066 — S-3: SHINE / Cleaning — Sources of Dirt & Leaks

**Извещение на изменение:** 0175+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization / S-3: SHINE  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE определяет S-3: SHINE как устранение источника грязи и утечек:

> **Eliminate the source of dirt and leaks (oil, air, water, etc.).**

Далее SOURCE требует:

- clean machines, tools, floors, cabinets;
- develop instructions for cleaning methods and frequency;
- organize for cleaning — correct materials, rags, brooms, etc.;
- find ways to reduce the time required for cleaning.

В результате out-of-standard conditions должны быть легко идентифицируемы и исправляемы. fileciteturn182file0

## 2. LOCATION

**p. 133 — S-3: SHINE.**

Контекст: продолжение 5S Workplace Organization после S-2: SET IN ORDER.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **S-3: SHINE** | S-3: очистка / содержание в чистоте |
| **Shine** | очищать / доводить до чистого состояния |
| **Source of Dirt** | источник загрязнения |
| **Source of Leaks** | источник утечки |
| **Dirt** | загрязнение / грязь |
| **Leak** | утечка |
| **Oil** | масло |
| **Air** | воздух |
| **Water** | вода |
| **Cleaning Method** | метод очистки |
| **Cleaning Frequency** | периодичность очистки |
| **Correct Materials** | необходимые / правильные материалы |
| **Rags** | ветошь |
| **Brooms** | метлы |
| **Out-of-Standard Condition** | состояние вне стандарта |
| **Reduce Cleaning Time** | сокращать время очистки |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Cleaning ≠ Eliminate Source

SOURCE ставит более сильную задачу, чем удаление загрязнения: **устранить источник** грязи и утечки.

### Source ≠ Symptom

Удаление грязи устраняет проявление; устранение источника направлено на причину возникновения загрязнения. Последнее — инженерная интерпретация логики SOURCE, а не отдельная формулировка GM.

### Cleaning Method ≠ Cleaning Frequency

Метод определяет, **как** очищать; frequency — **как часто**.

### Cleaning ≠ Organize for Cleaning

Очистка и организация средств для очистки — разные конструкции.

### Cleaning ≠ Reduced Cleaning Time

SOURCE требует искать способы сокращения времени очистки; это не тождественно самой очистке.

### Out-of-Standard Condition ≠ Dirt / Leak

Dirt/leak могут быть источником или проявлением отклонения, но SOURCE формулирует более широкую категорию **out-of-standard condition**.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **S-3: SHINE - Eliminate the source of dirt and leaks (oil, air, water, etc.).**

> **Clean machines, tools, floors, cabinets.**

> **Develop instructions for cleaning methods and frequency.**

> **Organize for cleaning (correct materials, rags, brooms, etc.).**

> **Find ways to reduce the time required for cleaning.**

> **Out-of-standard conditions can be easily identified and corrected.** fileciteturn182file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

Основная конструкция:

```text
DIRT / LEAK
      ↓
IDENTIFY SOURCE
      ↓
ELIMINATE SOURCE
```

Параллельно:

```text
CLEANING
      ↓
METHOD + FREQUENCY
      ↓
ORGANIZE MATERIALS
      ↓
REDUCE CLEANING TIME
```

И ожидаемый организационный эффект:

```text
STANDARD
      ↓
OUT-OF-STANDARD CONDITION
      ↓
EASY TO IDENTIFY
      ↓
CORRECT
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Dirt / Leak
→ Source
→ Eliminate Source
```

```text
Cleaning
→ Method + Frequency
```

```text
Cleaning
→ Correct Materials
```

```text
Cleaning Process
→ Reduce Required Time
```

```text
Out-of-Standard Condition
→ Identify
→ Correct
```

SOURCE не устанавливает прямую последовательность между всеми перечисленными элементами.

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Source Elimination of Dirt / Leaks

**Input:** источник загрязнения или утечки.

**Transformation:** выявление источника и его устранение.

**Output:** устранённый источник грязи/утечки.

**Организационный эффект:** снижение возникновения загрязнения/утечки.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Оговорка: SOURCE прямо требует eliminate the source, но не раскрывает алгоритм поиска источника. Поэтому алгоритм диагностики не добавляем.

### CANDIDATE — Cleaning Standardization

**Input:** потребность в очистке.

**Transformation:** определение cleaning method и frequency + организация correct materials.

**Output:** организованный способ выполнения очистки.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Cleaning Time Reduction

**Input:** существующая операция очистки.

**Transformation:** поиск способов уменьшения требуемого времени.

**Output:** потенциально сокращённое время очистки.

**STATUS: CANDIDATE / SINGLE-SOURCE — WEAK**

SOURCE требует искать способы, но не раскрывает здесь конкретного преобразования.

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Устранять источники загрязнения и утечек

Способность воздействовать не только на загрязнение как проявление, но на его источник.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Стандартизировать очистку

Способность определять method, frequency и необходимые материалы для очистки.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Сокращать время очистки

Способность искать и реализовывать способы уменьшения требуемого времени очистки.

**STATUS: CANDIDATE / SINGLE-SOURCE — WEAK**

## 10. CORE CANDIDATE

> **Source Elimination of Dirt / Leaks — конструкция устранения источника загрязнений и утечек как часть S-3 SHINE, дополняемая стандартизированным способом и частотой очистки и организацией средств очистки.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Dirt / Leak Source Elimination

```text
INPUT
Dirt / Leak Source
      ↓
[ IDENTIFY SOURCE ]
      ↓
[ ELIMINATE SOURCE ]
      ↓
OUTPUT
Source Eliminated
      ↓
EFFECT
Reduced Recurrence of
Dirt / Leak
```

Инженерный тест проходит частично по SOURCE: input, требуемая операция и output определены. Но способ идентификации источника не раскрыт.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

### CANDIDATE MACHINE — Cleaning Method & Frequency Standardization

```text
INPUT
Cleaning Need
      ↓
[ DEFINE METHOD ]
+
[ DEFINE FREQUENCY ]
+
[ ORGANIZE MATERIALS ]
      ↓
OUTPUT
Defined Cleaning Arrangement
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

### Cleaning Time Reduction

**MACHINE = NONE / WEAK CANDIDATE** по текущему фрагменту: SOURCE задаёт направление поиска, но не показывает воспроизводимую операцию.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Dirt / Leak
→ Source
→ Eliminate Source
```

### SOURCE-SUPPORTED

```text
Cleaning
→ Method + Frequency
→ Correct Materials
```

### SOURCE-SUPPORTED

```text
Out-of-Standard Condition
→ Easy Identification
→ Correction
```

Не добавляем причинно-следственную цепь «cleaning → source identification» как прямое утверждение SOURCE: это следует из конструкции S-3, но отдельным алгоритмом здесь не задано.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Source Elimination Machine — **CANDIDATE / SINGLE-SOURCE**.

Cleaning Standardization Machine — **CANDIDATE / SINGLE-SOURCE**.

Cleaning Time Reduction — **WEAK CANDIDATE**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-061 показала:

```text
CLEANING
→ CHECKING
→ EQUIPMENT PROBLEM
```

GM-066 усиливает эту конструкцию:

```text
DIRT / LEAK
→ SOURCE
→ ELIMINATE SOURCE
```

То есть появляется переход от работы с **проявлением** к работе с **источником его возникновения**.

CMOC-гипотеза:

> **Устойчивая организация состояния требует отличать устранение наблюдаемого проявления от устранения источника его повторного возникновения.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

Вторая гипотеза:

> **Стандартизация операции включает не только содержание действия, но как минимум способ, периодичность и обеспеченность необходимыми средствами.**

Она основана на связке SOURCE: method + frequency + correct materials.

## 15. СВЯЗЬ С GM-061

```text
GM-061
CLEAN
→ CHECK
→ IDENTIFY EQUIPMENT PROBLEM
→ CORRECT
```

```text
GM-066
DIRT / LEAK
→ IDENTIFY SOURCE
→ ELIMINATE SOURCE
```

Пока не объединяем их в одну SOURCE Chain. Это две соседние конструкции, которые потенциально могут быть связаны в CMOC.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
