# GM-080 — S-4: STANDARDIZE / 5S Evaluation

**Извещение на изменение:** 0189+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** S-4: STANDARDIZE  
**SOURCE pages:** 141–142  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE предлагает создать чек-лист:

> **Create a checklist: 5S Evaluation**

Форма содержит:

- Date;
- Name;
- Area;
- Item No.;
- Description;
- 5S Evaluation & Scoring Criteria;
- Rating Scale: **0–5 (Poor = 0, Excellent = 5)**;
- Item Score (0–5);
- Notes for Next Level of Improvement.

Страница 141 содержит 9 критериев оценки.

### 1. Removing Unnecessary Items

**Criterion:** все предметы, не необходимые для выполнения работы, удалены с рабочего места; присутствуют только необходимые инструменты или продукты.

### 2. Storage of Cleaning

**Criterion:** всё cleaning equipment хранится аккуратно; всё легко доступно, когда требуется.

### 3. Floor Cleaning

**Criterion:** все полы чистые и свободны от мусора, масла и грязи; cleaning floors проводится регулярно — как минимум ежедневно.

### 4. Bulletin Boards

**Criterion:** устаревшие, порванные или загрязнённые объявления отсутствуют; все bulletin boards организованы аккуратно и упорядоченно.

### 5. Emergency Access

**Criterion:** fire hoses и emergency equipment не заблокированы и находятся в заметных, легко доступных местах; stop switches и breakers имеют маркировку или цветовую кодировку для visibility.

### 6. Items on Floor

**Criterion:** WIP, tools и другие материалы не оставляются непосредственно на полу; крупные предметы, такие как tote bins, размещаются на glance; линии прямые и расположены под прямыми углами, без chipped или soiled paint.

### 7. Aisleways — Marking

**Criterion:** aisles и walkways чётко обозначены и могут быть идентифицированы с первого взгляда; линии прямые и расположены под прямыми углами, без chipped или soiled paint.

### 8. Aisleways — Maintenance

**Criterion:** aisles всегда свободны от материалов и препятствий; ничего не размещается на линиях; объекты всегда располагаются под прямыми углами к линиям проходов.

### 9. Storage & Arrangement

**Criterion:** хранение boxed, containers и material всегда аккуратно и под прямыми углами; при штабелировании предметы не должны быть перекошены или находиться под угрозой опрокидывания.

## 2. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **5S Evaluation** | оценка 5S |
| **Checklist** | контрольный лист / чек-лист |
| **Evaluation & Scoring Criteria** | критерии оценки и начисления баллов |
| **Rating Scale** | шкала оценки |
| **Item Score** | оценка пункта |
| **Notes for Next Level of Improvement** | замечания для следующего уровня улучшения |
| **Removing Unnecessary Items** | удаление ненужных предметов |
| **Storage of Cleaning** | хранение средств / оборудования для уборки |
| **Floor Cleaning** | уборка пола |
| **Bulletin Board** | информационный стенд |
| **Emergency Access** | доступ к средствам аварийного реагирования |
| **Emergency Equipment** | аварийное оборудование |
| **Items on Floor** | предметы / материалы на полу |
| **Aisleway** | проход |
| **Walkway** | пешеходный проход |
| **Marking** | разметка |
| **Maintenance** | поддержание состояния |
| **Storage & Arrangement** | хранение и размещение |
| **Work-in-Process (WIP)** | незавершённое производство |
| **Straight Lines** | прямые линии |
| **Right Angles** | прямые углы |
| **Chipped Paint** | повреждённая краска |
| **Soiled Paint** | загрязнённая краска |
| **Scoring** | оценивание / начисление баллов |

## 3. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Evaluation ≠ Inspection

SOURCE создаёт **evaluation checklist**, а не отдельную процедуру инспекции.

### Criterion ≠ Score

Критерий определяет, что оценивается. Score фиксирует результат оценки.

### Score ≠ Improvement

Оценка 0–5 показывает текущий результат, а отдельная колонка содержит **Notes for Next Level of Improvement**.

### Standard ≠ Score

Критерии описывают ожидаемое состояние; балл отражает оценку соответствия этому критерию. Это CMOC interpretation, а не прямое определение SOURCE.

### Evaluation ≠ Corrective Action

Чек-лист позволяет оценить и записать следующий уровень улучшения, но сам по себе не задаёт механизм выполнения corrective action.

### Marking ≠ Maintenance

SOURCE отдельно оценивает качество разметки (Item 7) и поддержание проходов свободными/правильно организованными (Item 8).

### Storage ≠ Arrangement

Item 9 объединяет хранение и геометрически организованное размещение; не сводим это к одному понятию «складирование».

## 4. EXTRACTION — ИЗВЛЕЧЕНИЕ

Основная конструкция формы:

```text
AREA
  ↓
5S CRITERIA
  ↓
ITEM SCORE 0–5
  ↓
NOTES FOR NEXT LEVEL OF IMPROVEMENT
```

Шкала:

```text
0 = POOR
5 = EXCELLENT
```

Это не бинарная проверка. SOURCE вводит **градуированную оценку состояния**.

## 5. MECHANISM — МЕХАНИЗМ

### CANDIDATE — 5S Evaluation

**Input:** рабочая зона.

**Transformation:** оценка зоны по 9 заданным критериям с использованием шкалы 0–5.

**Output:** Item Scores + Notes for Next Level of Improvement.

**CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Improvement-Level Feedback

**Input:** Item Score.

**Transformation:** фиксация Notes for Next Level of Improvement.

**Output:** направление следующего улучшения.

**CANDIDATE / SINGLE-SOURCE**

Важно: SOURCE не задаёт здесь алгоритм преобразования score в конкретное действие.

## 6. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Оценивать состояние рабочего места по единым критериям

### CANDIDATE — Представлять качество состояния по градуированной шкале 0–5

### CANDIDATE — Фиксировать следующий уровень улучшения

Последняя способность основана на отдельной колонке формы, но SOURCE не описывает, как формируется её содержание.

## 7. CORE CANDIDATE

> **5S Evaluation — стандартизированная оценка состояния рабочей зоны по набору критериев с градуированной шкалой 0–5 и фиксацией замечаний для следующего уровня улучшения.**

**CANDIDATE / SINGLE-SOURCE**

## 8. MACHINE — МАШИНКА

### CANDIDATE MACHINE — 5S Evaluation

```text
INPUT
Workplace / Area
        ↓
[ APPLY STANDARDIZED CRITERIA ]
        ↓
9 EVALUATION ITEMS
        ↓
[ SCORE 0–5 ]
        ↓
ITEM SCORES
        ↓
[ RECORD NEXT IMPROVEMENT NOTES ]
        ↓
OUTPUT
EVALUATED AREA
+
IMPROVEMENT DIRECTION
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

## 9. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED

```text
Area
→ 5S Evaluation Criteria
→ Item Score 0–5
```

```text
Item Score
→ Notes for Next Level of Improvement
```

Вторая цепочка основана на структуре формы; она не утверждает причинный механизм улучшения.

## 10. CMOC INTERPRETATION

Здесь появляется новый слой после GM-079:

```text
PHYSICAL ORGANIZATION
        ↓
VISIBLE STANDARDIZED STATE
        ↓
STANDARDIZED EVALUATION
        ↓
SCORE
        ↓
NEXT IMPROVEMENT LEVEL
```

Это **CMOC INTERPRETATION / CANDIDATE**.

Особенно важно, что SOURCE не ограничивается вопросом «соответствует / не соответствует». Используется шкала:

```text
0 ───────────── 5
POOR       EXCELLENT
```

Следовательно, состояние может быть представлено как **градуированное значение**.

## 11. 9 КРИТЕРИЕВ КАК ОПТИКА СОСТОЯНИЯ

Критерии вместе покрывают разные аспекты физической организации:

```text
UNNECESSARY ITEMS
CLEANING STORAGE
FLOOR CONDITION
INFORMATION BOARDS
EMERGENCY ACCESS
ITEMS ON FLOOR
AISLE MARKING
AISLE MAINTENANCE
STORAGE / ARRANGEMENT
```

Это не просто перечень хозяйственных требований: форма превращает их в **наблюдаемые точки оценки**.

**CMOC INTERPRETATION / CANDIDATE**

## 12. IMPORTANT BOUNDARY

Страница 142 уже содержит следующую конструкцию:

> **React to Audit Findings**

и форму **5-S Work Place Organization Audit Countermeasure Sheet (Continuous Improvement)**.

Она включает поля:

- Item #;
- Date;
- Location;
- Problem Description;
- Owner;
- Countermeasure;
- Target Date;
- Initials;
- Complete Date.

Эта конструкция **не включена в основную Machine GM-080**. Она является следующим самостоятельным механизмом: **Finding → Countermeasure → Owner → Target Date → Completion**.

## 13. STATUS

**GM-080 — CANDIDATE / SINGLE-SOURCE**

**5S Evaluation Machine — CANDIDATE / SINGLE-SOURCE**

**Improvement-Level Feedback — CANDIDATE / SINGLE-SOURCE**

**CANON — не присваивается.**

## 14. CMOC HYPOTHESIS

> **Стандартизация становится управляемой не только через задание состояния, но и через стандартизированное представление степени достижения этого состояния.**

STATUS: **CMOC INTERPRETATION / CANDIDATE**

Следующий шаг SOURCE — отдельная конструкция **React to Audit Findings**, которую целесообразно выделить в GM-081.
