"""SQLite backup/restore for the local CMOC runtime state.

The backup contains execution journal, operational projection, and durable
production-adapter results. It carries no semantic CMOC data.
"""

from __future__ import annotations

import os
import sqlite3
from pathlib import Path


def backup_runtime(source_db: str, backup_db: str) -> None:
    source = sqlite3.connect(source_db)
    try:
        target_path = Path(backup_db)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = target_path.with_suffix(target_path.suffix + ".tmp")
        if temp_path.exists():
            temp_path.unlink()
        target = sqlite3.connect(str(temp_path))
        try:
            source.backup(target)
        finally:
            target.close()
    finally:
        source.close()

    os.replace(temp_path, target_path)


def restore_runtime(backup_db: str, target_db: str) -> None:
    backup = sqlite3.connect(backup_db)
    try:
        target_path = Path(target_db)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = target_path.with_suffix(target_path.suffix + ".restore.tmp")
        if temp_path.exists():
            temp_path.unlink()
        target = sqlite3.connect(str(temp_path))
        try:
            backup.backup(target)
        finally:
            target.close()
    finally:
        backup.close()

    os.replace(temp_path, target_path)
