# Bots

[← Zurück zum Index](../INDEX.md) | [Bus](bus.md) | [Desktop](../programme/desktop/README.md)

---

## Drei Orte für Bots

| Ort | Funktion |
|---|---|
| **Store** | Bot-Module finden und installieren |
| **Conductor** | Bot konfigurieren (Tokens, Gruppen, Verbindungen) |
| **Bot Manager** (Desktop) | Bot BENUTZEN (Broadcast senden, Gatekeeper verwalten) |

---

## Architektur: Ein Control-Bot mit Plugin-Modulen

Nicht viele separate Bots pro Gruppe, sondern **ein Control-Bot** der Module nachlädt:

```
Control-Bot (immer installiert, Admin-Rechte)
  ├── /broadcast Modul    ← Bus-Events → Messenger-Nachrichten
  ├── /gatekeeper Modul   ← Gruppen-Beitritt verifizieren
  ├── /tickets Modul      ← Ticket-System
  ├── /calendar Modul     ← Termine anzeigen
  └── weitere Module aus dem Store
```

Ein Bot in der Gruppe statt fünf. Jedes Modul ist ein Paket im Store das nachgeladen werden kann.

---

## Control-Bot

Der Control-Bot ist der erste Bot der installiert wird. Nur Admins können ihn steuern.

**Funktionen:**
- Räume/Gruppen erstellen und verwalten
- Mitglieder einladen / entfernen
- Module nachladen (aus dem Store)
- Befehle von Admins empfangen
- Andere spezialisierte Bots einladen wenn nötig

### Control-Bot je Messenger

| Messenger | Bot-Typ | Crate | Volle Kontrolle? |
|---|---|---|---|
| Telegram | UserBot (MTProto) | `grammers` | Ja (Räume erstellen, Mitglieder verwalten) |
| Matrix | Normaler User mit Admin | `matrix-sdk` | Ja |
| Discord | Bot mit Admin-Permission | `serenity` + `poise` | Ja |
| Rocket.Chat | Admin-Integration (REST + WebSocket) | `reqwest` | Ja |
| Slack | App mit allen Scopes | `slack-morphism` | Fast alles |
| XMPP | Account + MUC-Admin | `xmpp-rs` | Ja |
| Mattermost | Admin-Integration | `reqwest` | Ja |

**Hinweis zu Telegram:** Für den Control-Bot wird ein **UserBot** benötigt, kein normaler Bot. UserBots laufen über MTProto mit einem echten Account und haben volle Kontrolle. Normale Bots (Bot-API via `teloxide`) sind für Gruppen-Verwaltung eingeschränkt.

---

## Channels (fsn-channel) — Messenger-Unabhängigkeit

Der Bot schreibt **einmal**, `fsn-channel` übersetzt für jeden Messenger:

```rust
// Bot-Code (messenger-unabhängig):
control_bot.create_room("projekt-koeln").await?;
control_bot.invite("projekt-koeln", user_id).await?;
control_bot.send("projekt-koeln", "Willkommen!").await?;

// fsn-channel übersetzt intern:
// Telegram:    grammers  → CreateChat + InviteToChat + SendMessage
// Matrix:      matrix-sdk → create_room + invite_user + send_message
// Discord:     serenity  → create_channel + add_member + send_message
// Rocket.Chat: reqwest   → POST /api/v1/channels.create + invite + sendMessage
```

**Welcher Messenger aktiv ist, bestimmt das [Inventory](inventory.md):** Der Bot fragt nicht "Habe ich Telegram?" — er fragt das Inventory: "Welche Services haben die Rolle `chat`?" Wenn Telegram installiert ist, ist der Telegram-Channel aktiv. Wenn Matrix dazukommt, wird der Matrix-Channel ebenfalls aktiv. Der Bot-Code ändert sich nicht.

---

## Wichtiges Prinzip: Bots reden NIE direkt mit Services

Der Control-Bot redet **nicht** direkt mit Kanidm, Outline, Forgejo. Er geht **immer** über den Bus und die Bridges:

```
FALSCH:
  Bot → HTTP-Request → Outline API → Seite erstellen

RICHTIG:
  Bot → Bus-Event publizieren (Rolle: wiki, Topic: page.create)
    → Bus → Bridge (outline-wiki-bridge) → Outline API → Seite erstellen
```

Das ist das Grundprinzip: Rollen-basiert, nie direkt. Wenn Outline durch ein anderes Wiki ersetzt wird, funktioniert der Bot weiterhin ohne Änderung.

---

## Kanal-Abonnements (Broadcast-Modul)

Das Broadcast-Modul verbindet den Message Bus mit Messenger-Gruppen:

```
User in Telegram-Gruppe schreibt: /subscribe git.commit
  → Control-Bot registriert Subscription im Bus:
      Rolle: git, Topic: git.commit → Ziel: Gruppe "projekt-koeln"
  → Ab jetzt: Jeder Commit erzeugt ein Bus-Event → Bot postet in die Gruppe

User schreibt: /subscribe wiki.page.created
  → Neue Wiki-Seiten werden in die Gruppe gepostet

User schreibt: /unsubscribe git.commit
  → Subscription entfernt
```

Jede Gruppe kann verschiedene Topics abonnieren. Benutzer konfigurieren das für ihre eigenen Gruppen (wenn sie die Rechte haben).

---

## Bot-Module als Store-Pakete

Bot-Module sind Pakete im Store mit `type = "bot"`:

```toml
[package]
id = "bot-broadcast"
name = "Broadcast Module"
type = "bot"
tags = ["bot", "broadcast", "notification", "subscribe"]
description = "Subscribe to Bus-Events and receive notifications in Messenger groups"

[bot]
parent = "control-bot"
commands = [
    { name = "/subscribe",     params = ["topic"],     description = "Subscribe to events" },
    { name = "/unsubscribe",   params = ["topic"],     description = "Unsubscribe" },
    { name = "/subscriptions", description = "List active subscriptions" },
]
required_roles = []
triggers = ["*"]              # Kann auf alle Bus-Events reagieren
```

```toml
[package]
id = "bot-gatekeeper"
name = "Gatekeeper Module"
type = "bot"
tags = ["bot", "gatekeeper", "iam", "verification"]

[bot]
parent = "control-bot"
commands = [
    { name = "/verify", params = ["user_id"], description = "Verify a user via IAM" },
    { name = "/approve", params = ["request_id"] },
    { name = "/deny",    params = ["request_id"] },
]
required_roles = [{ roles = ["iam"], mode = "ANY" }]
triggers = ["chat.join_request"]
```

Jeder kann Bot-Module schreiben und in den Store stellen. Andere installieren sie und laden sie in ihren Control-Bot.

---

Weiter: [Tasks](tasks.md) | [Bus](bus.md) | [Inventory](inventory.md)
