# AI — Lokaler LLM-Manager

[← Zurück zum Index](../../INDEX.md)

---

## Was die AI-App macht

Startet und verwaltet lokale LLM-Server (Mistral.rs) und verbindet sie mit Editor-Tools (Continue).

## Architektur

| Crate | Zweck |
|---|---|
| `fs-manager-ai` | Backend: `AiEngine` Trait, `LlmEngine` (PID-basiert), `LlmModel` Katalog |
| `fs-ai` | UI: Dioxus Desktop App |

```
LlmModel (catalogue) → LlmEngine (start/stop/status) → ~/.continue/config.json
                                                       → AI-App UI
```

- `AiEngine` Trait — gemeinsame Schnittstelle für alle Engine-Typen
- `LlmEngine` — Mistral.rs Prozess (PID-Datei, `/proc/{pid}` Alive-Check)
- Modelle: Qwen3-4B, Qwen3-8B, Qwen2.5-Coder-7B

## Repo

`git@github.com:FreeSynergy/fs-ai.git`

---

Weiter: [Bot Manager](../botmanager/README.md)
