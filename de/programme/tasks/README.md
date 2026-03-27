# Tasks — Automatisierungs-Pipeline-App

[← Zurück zum Index](../../INDEX.md) | [Lenses](../lenses/README.md)

---

## Was die Tasks-App macht

Die Tasks-App ist der visuelle Editor für Automatisierungs-Pipelines.
Konzept: [Tasks](../../konzepte/tasks.md)

## Architektur

| Modul | Zweck |
|---|---|
| `model.rs` | `TaskPipeline`, `DataTrigger`, `FieldTransform`, `DataSource`, `DataTarget` |
| `pipeline_editor.rs` | `PipelineEditor` — visueller Dioxus-Editor für Task-Pipelines |
| `templates.rs` | Vordefinierte Task-Vorlagen (Forgejo→Outline, etc.) |
| `app.rs` | `TasksApp` — Dioxus Root-Komponente |

## Datenfluss

```
TaskTemplate → TaskPipeline (via Editor) → tasks.toml → Bus-Event zur Ausführung
```

- `TasksConfig` lädt/speichert nach `~/.config/fsn/tasks.toml`
- Trigger: `Manual`, `OnEvent(String)`, `Scheduled(cron-String)`
- Feld-Mapping: `Direct` | `Template(String)` | `Fixed(String)`

## Repo

`git@github.com:FreeSynergy/fs-tasks.git`

---

Weiter: [Lenses](../lenses/README.md) | [Konzept: Tasks](../../konzepte/tasks.md)
