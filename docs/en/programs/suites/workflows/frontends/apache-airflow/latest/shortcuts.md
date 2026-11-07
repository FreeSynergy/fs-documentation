# Apache Airflow - Keyboard shortcuts

## Overview

The Airflow UI has **no documented keyboard shortcuts**; work happens in lists/dialogs and mainly in the CLI/code.

> As of: Airflow 3.x.

## Available

| Shortcut | Function |
|----------|----------|
| `Ctrl/Cmd+F` | Table/log search (browser) |
| `Enter`/`Tab` | Dialogs (trigger conf) |
| `Esc` | Close dialog |

## Central "shortcuts" = CLI

| Command | Effect |
|--------|--------|
| `airflow dags list` | DAG overview |
| `airflow dags test <dag_id> <date>` | Run DAG locally |
| `airflow tasks test <dag_id> <task_id> <date>` | Single task |
| `airflow dags unpause <dag_id>` | Activate schedule |
| `airflow users …` | RBAC management |

## Mac

`Cmd` for browser standards.
