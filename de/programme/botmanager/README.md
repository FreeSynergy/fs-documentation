# BotManager — Bot-Steuerung & Messenger-Integration

[← Zurück zum Index](../../INDEX.md) | [Desktop](../desktop/README.md) | [Bots](../../konzepte/bots.md)

---

## Was der BotManager macht

Der BotManager ist das Programm mit dem Bots **benutzt** werden. Er ist **nicht** für Installation oder Konfiguration zuständig — das übernehmen Store und Conductor. Der BotManager ist die Schnittstelle zwischen dem Benutzer und den laufenden Bots.

```
Store       → Findet + installiert Bot-Module (Pakete)
Conductor   → Konfiguriert Bots (Tokens, Gruppen, Verbindungen)
BotManager  → BENUTZT Bots (Broadcasts senden, Gatekeeper verwalten, Status sehen)
```

## Eigenständigkeit

BotManager läuft eigenständig. Desktop nutzt ihn als eingebettete App, aber er kann auch ohne Desktop gestartet werden — als eigenständiges Fenster oder via CLI.

---

## Views

### Bot-Status

Übersicht aller installierten Bots mit Status (online / offline / error):

```
Control Bot (Telegram)    ● online   | 3 Module aktiv
Control Bot (Matrix)      ● online   | 2 Module aktiv
Control Bot (Discord)     ○ offline  | Token fehlt
```

Klick → Detailansicht mit aktiven Modulen, letzter Aktivität, Fehler-Log.

### Broadcast

Nachrichten an Messenger-Gruppen senden ohne in Telegram/Matrix/Discord zu wechseln:

```
Empfänger:  [ Alle Gruppen ▼ ] oder einzelne Gruppen auswählen
Messenger:  [ Alle ▼ ] oder Telegram / Matrix / Discord...
Nachricht:  [___________________________________________]
            [ Markdown ]  [ Datei anhängen ]  [ Senden ]
```

Der BotManager veröffentlicht ein `bot.broadcast` Bus-Event — der Control-Bot empfängt es und sendet in alle abonnierten Gruppen.

### Subscriptions

Verwaltet welche Messenger-Gruppe welche Bus-Events empfängt:

```
Gruppe "Projekt Köln" (Telegram)
  ✅ git.commit          → Commits aus Forgejo
  ✅ wiki.page.created   → Neue Seiten in Outline
  ☐  tasks.assigned     → Aufgaben-Zuweisung
  ☐  calendar.event     → Termine

[ + Subscription hinzufügen ]
```

Intern nutzt das Broadcast-Modul die Bus-Subscription-API. Der BotManager ist nur das UI dafür.

### Gatekeeper

Verwaltung von Beitrittsanfragen zu Messenger-Gruppen:

```
Offene Anfragen:
  @max_muster möchte "Projekt Köln" beitreten
  IAM-Status: ✅ Verifiziert (Kanidm: max.muster@helfa-koeln.de)
  [ Genehmigen ]  [ Ablehnen ]

  @unknown_user möchte "Team Süd" beitreten
  IAM-Status: ❌ Nicht im System
  [ Genehmigen ]  [ Ablehnen ]  [ Blockieren ]
```

Genehmigung löst ein Bus-Event aus (`chat.join_approved`) — das Gatekeeper-Modul führt die eigentliche Aktion im Messenger aus.

### Module

Liste aller installierten Bot-Module je Bot:

```
Control Bot (Telegram)
  📢 Broadcast Module    v1.2.0  ● aktiv
  🚪 Gatekeeper Module   v1.0.3  ● aktiv
  🎫 Tickets Module      v0.8.1  ○ inaktiv (kein Ticket-Service)

[ + Modul aus Store installieren ]
```

Inaktive Module sind solche deren `required_roles` nicht erfüllt sind (kein passender Service installiert).

---

## Rechte

Bot-Aktionen folgen dem [Rechte-System](../../konzepte/rechte.md):

| Aktion | Benötigtes Recht |
|---|---|
| Bot-Status sehen | `read` |
| Broadcasts empfangen (Subscription) | `read` |
| Broadcasts senden | `execute` |
| Subscriptions verwalten (eigene Gruppen) | `write` |
| Gatekeeper: Anfragen sehen | `read` |
| Gatekeeper: Genehmigen/Ablehnen | `execute` |
| Module aktivieren/deaktivieren | `write` |
| Bot-Tokens ändern | `execute` (Admin) |

Wer einen Bot in einer Gruppe verwalten darf, bestimmt das Rechte-System — nicht der Messenger selbst.

---

## Bus-Integration

Der BotManager redet **nie direkt** mit Messengern. Er kommuniziert ausschließlich über den Bus:

```
BotManager → Bus-Event → Control-Bot → fsn-channel → Messenger
```

| Event | Publiziert von | Empfänger |
|---|---|---|
| `bot.broadcast` | BotManager | Control-Bot (Broadcast-Modul) |
| `bot.gatekeeper.approve` | BotManager | Control-Bot (Gatekeeper-Modul) |
| `bot.gatekeeper.deny` | BotManager | Control-Bot (Gatekeeper-Modul) |
| `bot.subscription.add` | BotManager | Control-Bot (Broadcast-Modul) |
| `bot.status.request` | BotManager | Alle laufenden Bots |
| `bot.status.response` | Control-Bot | BotManager |
| `chat.join_request` | Control-Bot | BotManager (Gatekeeper-View) |

---

## fsn-channel — Messenger-Abstraktion

Die eigentliche Messenger-Kommunikation läuft über das `fsn-channel` Crate (in `FreeSynergy.Lib`). BotManager selbst spricht **kein** Telegram/Matrix/Discord — das macht der Control-Bot via `fsn-channel`.

Welche Messenger aktiv sind bestimmt das Inventory:

```rust
// Control-Bot fragt das Inventory:
let channels = inventory.services_with_role("chat").await?;
// → [TelegramChannel, MatrixChannel] wenn beide installiert
// Bot-Code ändert sich nicht wenn ein neuer Messenger hinzukommt
```

Details: [Bots → fsn-channel](../../konzepte/bots.md#fsn-channel)

---

## Interfaces

| Interface | Kürzel | Beschreibung |
|---|---|---|
| Web-based GUI | WGUI | Standalone oder eingebettet in Desktop |
| Command Line | CLI | `fsn bot broadcast`, `fsn bot status` |
| API | REST | `POST /api/bot/broadcast`, `GET /api/bot/status` |

```bash
# CLI-Beispiele
fsn bot status                              # Alle Bots + Status
fsn bot broadcast --groups all "Wartung heute Abend 20:00"
fsn bot gatekeeper list                     # Offene Beitrittsanfragen
fsn bot gatekeeper approve <request-id>
fsn bot subscriptions list --group "Projekt Köln"
fsn bot subscriptions add --group "Projekt Köln" git.commit
```

```
# API-Beispiele
GET  /api/bot/status
GET  /api/bot/modules
POST /api/bot/broadcast       { "groups": ["all"], "message": "..." }
GET  /api/bot/gatekeeper      (offene Anfragen)
POST /api/bot/gatekeeper/:id/approve
POST /api/bot/gatekeeper/:id/deny
GET  /api/bot/subscriptions?group=
POST /api/bot/subscriptions   { "group": "...", "topic": "git.commit" }
DELETE /api/bot/subscriptions/:id
```

---

## Bibliotheken

| Crate | Zweck |
|---|---|
| `dioxus` 0.7.x | UI-Framework |
| `fsn-ui` | Komponenten-Bibliothek |
| `fsn-bus` | Bus-Client (Events publizieren/empfangen) |
| `fsn-inventory` | Welche Bots/Module sind installiert? |
| `fsn-db` | SQLite (fsn-botmanager.db) |
| `reqwest` | Node-API aufrufen |

**Nicht im BotManager:** `grammers`, `matrix-sdk`, `serenity` — diese gehören zum Control-Bot, nicht zum BotManager.

---

## Repo

https://github.com/FreeSynergy/BotManager

Der BotManager ist ein eigenständiges Programm. Desktop nutzt ihn als eingebettete App (`app-botmanager`), aber er kann auch standalone gestartet werden.

---

Weiter: [Bots Konzept](../../konzepte/bots.md) | [Desktop](../desktop/README.md) | [Bus](../../konzepte/bus.md)
