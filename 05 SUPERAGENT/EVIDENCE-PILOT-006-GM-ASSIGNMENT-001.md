# EVIDENCE — PILOT-006 GM Assignment Action Sheet

**Извещение на изменение:** `0220+280926`  
**Дата:** 28-09-2026  
**Источник:** SRC-002, GM Quality System Basics rev March 2009, PDF p. 96  
**RUN:** `RUN-PILOT-006-SRC-002-ASSIGNMENT`  
**Статус:** живой Discovery/Reconciliation и ручная проверка, без Admission

## Контролируемый вход

`SOURCE-PACKAGE-SRC-002-GM-QSB-P96-ASSIGNMENT.example.json` содержит пересказ правила: поручения, возникшие на ежедневной Verification Station или еженедельной Problem Solving встрече, фиксируются в Assignment Action Sheet и рассматриваются на следующей встрече. Существующий аналитический кандидат — `04 PATCH/GM-042-Assignment-Action-Sheet.md`. Пакет не присваивает тип CMOC и не утверждает NEW.

## Наблюдение в живом RUN

`run_superagent.py` вернул `HUMAN_REVIEW_REQUIRED`. Reconciliation получил два M06 паспорта, оба `NEEDS_REVIEW`, с `query_scope=[TERMS]`, без записи CMOC/OBJECT INDEX и без Admission.

- `PAS-001` / `MAT-PAS-001`: «Assignment Action Sheet issue tracking», `working_class=ACTIVITY`. `FORM-001…003` сохраняют связную последовательность issue → assignment captured in sheet → reviewed at next meeting. Граница M06 остаётся source-bound activity; целевой тип MACHINE или организационная конструкция не установлен.
- `PAS-002` / `MAT-PAS-002`: «Material presentation, delivery, and work-support issue types», `working_class=CONCEPT_MODEL`. `FORM-004…006` превратили примеры возможных вопросов на странице 96 в модель типов; источник не устанавливает самостоятельную классификацию.

Read-only `pilot_001_query_scope_probe.py` проверил десять областей OBJECT INDEX для обоих названий и вернул exact/alias `NO_MATCH`. Это не доказывает NEW и не разрешает отношение к кандидату GM-042, который уже описан в PATCH.

## Решения человека

СГ записал `DEFER` для MAT-PAS-001 (граница, целевой тип и сравнение с GM-042 открыты) и `REJECT` для MAT-PAS-002 (примеры вопросов не самостоятельная модель). Оба CLI-вызова вернули `PERSISTED`, `WAITING_HUMAN_REVIEW`, `projection_valid=true`. Оба JSON решения доступны в `05 SUPERAGENT/human_review_decisions/RUN-PILOT-006-SRC-002-ASSIGNMENT/`.

## Доказанная граница

Живой путь от контролируемого фрагмента до M06, Reconciliation и двух записанных решений человека продемонстрирован. Сохранение последовательности в FORM не равно паспорту машины; `ACTIVITY` не отображается автоматически в целевой тип CMOC. Семантическое тождество с GM-042, NEW, агрегированное завершение RUN, Admission, C1/C2/C3 и запись CMOC/OBJECT INDEX не доказаны. Повторный запуск того же фрагмента не разрешит этот пробел.
