# GM-087 — Major Steps / Key Points / Reasons

**SOURCE:** GM Quality System Basics Overview Supplier Audit.pdf, pp. 172–174  
**Section:** 4.4.1 — Standardized Work  
**Status:** SOURCE-SUPPORTED extraction; CMOC interpretations remain CANDIDATE.

## 1. SOURCE

### Major Steps — WHAT

SOURCE defines a **Major Step** within an element (Job Element Sheet) as an action necessary for advancing the element to its successful completion.

When writing Major Steps, SOURCE requires the writer to:

- be brief;
- describe a single action;
- avoid abbreviations, acronyms and jargon.

SOURCE examples:

- Place part in fixture.
- Rotate jog switch to the Run position.
- Press Start Cycle button.

### Key Points — HOW

SOURCE states that **Key Points describe how to perform a step**, and that not all steps require Key Points.

SOURCE gives examples of when a Key Point should be written:

- if a team member could get injured by failing to follow a certain method or technique;
- if success or failure depends on performing the work a certain way;
- if an easier way to perform the step has been learned;
- if there is a product quality standard associated with the task.

SOURCE identifies four types of Key Points:

1. **Safety** — points in a job operation which could result in team member injury;
2. **Success** — operational points on which the success or failure of a particular job depends;
3. **Hints** — points which make the job performance easier;
4. **Quality** — points that describe quality requirements for an operation.

### Reasons — WHY

SOURCE asks:

- What happens if the Key Point is ignored?
- Why is it done this way? What is the reason?

SOURCE explicitly states:

**Every Key Point shall have a reason why.**

The examples shown in the visual include consequences such as possible explosion, machine not engaging, wrist injuries, and a customer finding a loose part causing noise.

## 2. TERMS

| English | Русский |
|---|---|
| Major Step | Основной шаг |
| What | Что / действие |
| Key Point | Ключевой момент |
| How | Как |
| Reason | Причина / обоснование |
| Why | Почему |
| Safety | Безопасность |
| Success | Успех / успешное выполнение |
| Hints | Подсказки |
| Quality | Качество |
| Job Element Sheet | Лист элемента работы |
| Single Action | Одно действие |
| Abbreviation | Сокращение |
| Acronym | Акроним / аббревиатура |
| Jargon | Профессиональный жаргон |

## 3. DISTINCTIONS

### Major Step ≠ Work Element

SOURCE places Major Steps **within an Element**. Therefore the structure shown by SOURCE is:

`Element → Major Steps`

**SOURCE-SUPPORTED.**

### Major Step ≠ arbitrary description

A Major Step is to be brief and describe a single action; SOURCE also instructs avoiding abbreviations, acronyms and jargon.

**SOURCE-SUPPORTED.**

### Key Point ≠ mandatory attribute of every step

SOURCE explicitly says that not all steps require Key Points.

**SOURCE-SUPPORTED.**

### Key Point = HOW

SOURCE directly labels Key Points as **HOW** and defines them as describing how to perform a step.

**SOURCE-SUPPORTED.**

### Key Point ≠ Reason

SOURCE separates **HOW** from **WHY**. A Key Point describes how the step is performed; its Reason explains why that Key Point is important.

**SOURCE-SUPPORTED.**

### Every Key Point → Reason

SOURCE explicitly requires every Key Point to have a reason why.

**SOURCE-SUPPORTED.**

## 4. EXTRACTION

The document structure demonstrated by SOURCE is:

```text
ELEMENT
  ↓
MAJOR STEP — WHAT
  ↓
KEY POINT — HOW
  ↓
REASON — WHY
```

The Key Point layer is conditional:

```text
MAJOR STEP
   ↓
Does the step require a Key Point?
   ↓
YES → HOW → WHY
NO  → no Key Point required
```

The SOURCE does not provide a formal decision algorithm for determining whether a Key Point is required; it provides examples/criteria.

## 5. MECHANISM

### SOURCE-supported mechanism

**Major Step specification:**

```text
Element
  ↓
Major Step
  ├─ brief
  ├─ single action
  └─ no abbreviations / acronyms / jargon
```

**Key Point specification:**

```text
Major Step
  ↓
Key Point (when required)
  ├─ Safety
  ├─ Success
  ├─ Hints
  └─ Quality
        ↓
Reason Why
```

The four Key Point types are SOURCE-SUPPORTED.

## 6. CAPABILITY

### SOURCE-SUPPORTED

The SOURCE supports the capability to document a work element at three levels of instruction:

```text
WHAT
→ Major Step

HOW
→ Key Point

WHY
→ Reason
```

This wording is a compact representation of the SOURCE's explicit framing.

### CMOC INTERPRETATION / CANDIDATE

This may be interpreted as a layered representation of executable work knowledge:

`Action → Method → Rationale`

This is **not Canon** and is not presented as a SOURCE term.

## 7. CHAIN

SOURCE-supported chain:

```text
Work Element
    ↓
Major Step (WHAT)
    ↓
Key Point (HOW) [when applicable]
    ↓
Reason (WHY) [for every Key Point]
```

## 8. CMOC INTERPRETATION

### Candidate construction

A **Job Element Sheet** can be viewed as a structured carrier of:

```text
WHAT
  ↓
HOW
  ↓
WHY
```

with the important condition that HOW/Key Point is not required for every Major Step, while every Key Point requires WHY.

**CMOC INTERPRETATION / CANDIDATE.**

Do not promote to CANON from this source fragment alone.

## 9. STATUS

| Construction | Status |
|---|---|
| Major Step is an action within an Element | SOURCE-SUPPORTED |
| Major Step describes a single action | SOURCE-SUPPORTED |
| Major Step should be brief | SOURCE-SUPPORTED |
| Avoid abbreviations, acronyms and jargon | SOURCE-SUPPORTED |
| Key Point describes HOW | SOURCE-SUPPORTED |
| Not all steps require Key Points | SOURCE-SUPPORTED |
| Four Key Point types: Safety / Success / Hints / Quality | SOURCE-SUPPORTED |
| Every Key Point shall have a Reason WHY | SOURCE-SUPPORTED |
| WHAT → HOW → WHY as a compact knowledge structure | CMOC INTERPRETATION / CANDIDATE |
| Canon | NONE |

## 10. SOURCE BOUNDARY

This patch does not infer additional requirements for documentation, approval, revision control, training, or verification beyond what is visible in SOURCE pp. 172–174.

The visual examples are treated as part of SOURCE. No physical parameters or rules from other specifications are transferred here.

## 11. OBSIDIAN

**Извещение на изменение — «GM-087-Major-Steps-Key-Points-Reasons.md» — 0196+300826**

Create/update only the corresponding PATCH record. CORE / Catalogs / LAB are not changed by this patch.
