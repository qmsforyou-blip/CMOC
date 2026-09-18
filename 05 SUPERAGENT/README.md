# SUPERAGENT MVP

Executable kernel for `MVP-SUPERAGENT-001`.

## Scope

The runner implements the orchestration boundary, not semantic source processing itself:

```
INPUT + TASK + CONTRACT
        ↓
   CONTRACT GATE
        ↓
      BATCH
        ↓
     MACHINE
        ↓
   OUTPUT QC
        ↓
     HANDOFF
```

Machine handlers are injected. The runner therefore does not contain GM-specific knowledge.

## Local run

```bash
python mvp_runner.py < demo_input.json
python -m unittest discover -s . -p "test_*.py" -v
```

The repository CI workflow executes the deterministic control tests on push.

## Evidence boundary

The test fixture uses the already controlled SRC-002 pages 1–6 records from the MVP control work. This proves the executable orchestration kernel and its contract gates. It does **not** claim that this Python runner independently performs semantic LLM extraction from a PDF.

Date: 18-09-2026
