# GM-013 — Step 3: 5-Why / Root Cause

**Извещение на изменение:** 0124+280826
**Source:** GM Quality System Basics Overview Supplier Audit.pdf
**Status:** CANDIDATE / SINGLE-SOURCE

## SOURCE

Fast Response → 1.3 Problem Solving → Step 3 — Identify the Root Cause, p. 39.

GM presents the **FIVE WHY PROBLEM SOLVING TOOL** as a Cause Investigation example. For each NO response in Diamonds 1–4, a 5-Why analysis is performed; when a cause is found, WHY is asked until the real root cause is found.

## EXTRACTION

Example chain:

Robot stopped
→ fuse blown
→ circuits overloaded
→ bearings locked up
→ insufficient lubrication
→ oil pump not circulating sufficient oil
→ pump intake clogged with metal shavings
→ no filter on pump intake
→ pump was not designed with a filter

The example therefore moves from an observed failure through successive causal explanations toward a design-level condition.

## DISTINCTIONS

- Cause ≠ Root Cause
- observed failure ≠ causal explanation
- immediate cause ≠ underlying cause
- 5-Why is a Cause Investigation tool, not merely a list of questions
- 5-Why follows a NO response in Diamonds 1–4; it is not presented here as the universal first step

## GM-FORMULATIONS

- “FIVE WHY PROBLEM SOLVING TOOL”
- “When a cause is found, ask why until you find the real root cause (5 Why’s)”

## REL

```text
Observed failure
→ immediate cause
→ next causal condition
→ deeper causal condition
→ ...
→ real root cause
```

## MECHANISM

**CANDIDATE — Causal Deepening Mechanism**

Input: identified cause.
Operation: repeatedly test the causal explanation with WHY.
Output: progressively deeper causal explanation, terminating at the real root cause as determined by the investigation.

## CAPABILITY

NONE.

## CORE CANDIDATE

**5-Why causal investigation** — a repeatable method for deepening from an identified cause toward a real root cause by successive WHY questions.

## MACHINE

**CANDIDATE MACHINE — 5-Why Causal Deepening**

```text
CAUSE
  ↓
WHY?
  ↓
DEEPER CAUSE
  ↓
WHY?
  ↓
...
  ↓
REAL ROOT CAUSE
```

The source supports the transformation logic through the worked example. It does not establish a universal numeric stopping rule beyond reaching the real root cause.

## CHAIN

**SOURCE-SUPPORTED:**

```text
Cause
→ Why
→ deeper cause
→ Why
→ deeper cause
→ ...
→ real root cause
```

## CMOC INTERPRETATION

The useful CMOC abstraction is not “ask Why five times.” It is:

> **Do not stop at the first plausible cause; repeatedly test the causal explanation until the investigation reaches the condition treated as the real root cause.**

The worked GM example is especially important because its final condition is not a person’s mistake but a design condition: the pump was not designed with a filter.

This is a source-supported distinction, but no broader CMOC canon is asserted here.
