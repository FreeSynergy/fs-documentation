# Bots

[← Zurück zum Index](../INDEX.md) | [Bus](bus.md) | [Desktop](../programme/desktop/README.md)

---

## Drei Orte für Bots

| Ort | Funktion |
|---|---|
| **Store** | Bot finden und installieren |
| **Conductor** | Bot konfigurieren (Tokens, Gruppen, Verbindungen) |
| **Bot Manager** (Desktop) | Bot BENUTZEN (Broadcast senden, Gatekeeper verwalten) |

## Bot-Definition

Ein Bot ist ein Paket im [Store](../programme/store/README.md):
```toml
[package]
id = "broadcast"
name = "Broadcast Bot"
type = "bot"
tags = ["broadcast", "telegram", "matrix", "notification"]
```

## Geplante Bots

**Broadcast Bot:** Nachricht eingeben → an alle konfigurierten Gruppen/Kanäle senden
**Gatekeeper Bot:** Telegram-Gruppen-Join → Verifikation via IAM → Approve/Deny
**Personal Bot:** LLM-gestützt, kann auf Nachrichten im Namen des Users antworten (später)

## Channels (fsn-channel)

Ein Bot spricht über Channels. Ein Channel ist ein Messenger-Adapter:
- Telegram (teloxide)
- Matrix (matrix-sdk)
- Discord (serenity + poise)
- Slack (slack-morphism)
- Email (lettre)
- Weitere hinter Feature-Flags

---

Weiter: [Tasks](tasks.md) | [Bus](bus.md)
