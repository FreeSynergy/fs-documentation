# Apache Airflow - Tastatur-Shortcuts

## Übersicht

Die Airflow-UI hat **keine dokumentierten Kurzbefehle**; Arbeit passiert in Listen/Dialogen und vor allem in CLI/Code.

> Stand: Airflow 3.x.

## Vorhanden

| Shortcut | Funktion |
|----------|----------|
| `Strg/Cmd+F` | Tabellen-/Log-Suche (Browser) |
| `Enter`/`Tab` | Dialoge (Trigger-Conf) |
| `Esc` | Dialog schließen |

## Zentrale „Kurzbefehle“ = CLI

| Befehl | Wirkung |
|--------|---------|
| `airflow dags list` | DAG-Übersicht |
| `airflow dags test <dag_id> <datum>` | DAG lokal ausführen |
| `airflow tasks test <dag_id> <task_id> <datum>` | Einzelner Task |
| `airflow dags unpause <dag_id>` | Zeitplan aktivieren |
| `airflow users …` | RBAC-Verwaltung |

## Mac

`Cmd` bei Browser-Standards.
