# MVP-SUPERAGENT-001 — Runner

Минимальный локальный runner для проверки контрактной оркестрации CMOC.

## Что он реально делает

- принимает SOURCE_PACKAGE;
- получает последовательность TASK;
- создаёт отдельный BATCH для каждого TASK;
- проверяет входной контракт;
- вызывает зарегистрированную MACHINE;
- проверяет OUTPUT;
- фиксирует ACCEPT/REJECT;
- формирует явный handoff;
- пишет журнал RUN в JSON.

## Важное ограничение

Runner не содержит семантику добычи инженерного знания. В текущем MVP функции M01/M02/M03 являются заглушками, демонстрирующими границу MACHINE.

Поэтому запуск runner сам по себе ещё не является доказательством качества M01/M02/M03. Следующий шаг — заменить заглушки реальными исполнителями машин, сохранив интерфейс runner.

## Запуск

Создать минимальный package:

```json
{"files":[],"scope":"test"}
```

Запустить:

```powershell
python MVP-SUPERAGENT-001-RUNNER.py --source-id SRC-002 --source-json source.json --tasks M01 M02 M03
```

Результат появится в каталоге `runs/`.

## Архитектурный принцип

SUPERAGENT = ORCHESTRATION  
MACHINE = PRODUCTION  
CONTRACT = GATE  
BATCH = EXECUTION IDENTITY  
OUTPUT = ARTIFACT  
HANDOFF = EXPLICIT TRANSFER
