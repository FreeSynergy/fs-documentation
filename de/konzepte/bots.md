# Bots

[← Zurück zum Index](../INDEX.md) | [Bus](bus.md) | [Pakete](pakete.md) | [Rechte](rechte.md)

---

## Grundprinzip

Jeder Bot ist ein **eigenständiges Programm** — mit eigenem Icon, eigenem Namen, eigener Beschreibung.
Bots können allein arbeiten oder von einem Control Bot koordiniert werden. Beides ist gleichwertig.

```
Standalone-Bot:
  Broadcast Bot allein  → leitet Bus-Events in Gruppen weiter
  Gatekeeper Bot allein → verifiziert Join-Requests
  Calendar Bot allein   → postet Termine

Control Bot:
  Verwaltet und koordiniert andere Bots
  Gibt Zugangsdaten und Gruppen-Mitgliedschaften weiter (Vererbung)
  Ist selbst auch ein Bot — kann alles was andere auch können
```

Der Control Bot ist **optional**. Kein Bot braucht ihn um zu funktionieren.
Wer ihn trotzdem nutzt, spart Konfigurationsaufwand und hat eine zentrale Steuerung.

---

## Bot-Typen aus dem Store

Jeder Bot-Typ ist ein eigenes `bot`-Paket im Store. Nach der Installation erscheint er
im Desktop als eigenes Programm (Icon, Name, optionales Widget).

| Bot-Paket | Funktion | Standalone? |
|---|---|---|
| `bot-control` | Koordiniert andere Bots, erbt Einstellungen weiter | Ja |
| `bot-broadcast` | Bus-Events → Messenger-Gruppen | Ja |
| `bot-gatekeeper` | Gruppen-Beitritte via IAM verifizieren | Ja |
| `bot-calendar` | Termine aus Desktop anzeigen + Erinnerungen | Ja |
| `bot-tickets` | Ticket-System in Gruppen | Ja |
| `bot-tasks` | Aufgaben-Verwaltung in Gruppen | Ja |
| `bot-room-sync` | Räume/Gruppen synchronisieren | Ja |
| `bundle-bots-all` | Alle oben zusammen | — |

Jedes Paket kann einzeln installiert werden. `bundle-bots-all` installiert alles auf einmal.

---

## Bot als Programm

Eine Bot-Instanz im Desktop:

```
Desktop-Launcher:
  [Icon] Community Bot      ← eigene Instanz, eigener Name
  [Icon] Projekt Bot        ← eigene Instanz
  [Icon] Mein Privater Bot  ← eigene Instanz
  [Icon] Bot Manager        ← zentrale Übersicht aller Instanzen

Optionales Widget auf dem Desktop:
  ┌─────────────────────────┐
  │  Community Bot          │
  │  ● Online               │
  │  47 Gruppen · 3 offen   │
  │  [Broadcast] [Status]   │
  └─────────────────────────┘
```

Klick auf eine Bot-Instanz → öffnet diesen Bot direkt, ohne Umweg über den Manager.
Der Bot Manager ist nur für die Gesamtübersicht und für die Erstellung neuer Instanzen.

### Tabs in jedem Bot

Jede Bot-Instanz hat dieselbe Tab-Struktur:

| Tab | Inhalt |
|---|---|
| **Info** | Wo ist der Bot aktiv? Gruppen, Messenger, Status, letzte Aktivität |
| **Einstellungen** | Name, Icon, Beschreibung, Tags, Sichtbarkeit, Messenger-Konten |
| **Steuerung** | Wer darf was — auf drei Ebenen (siehe unten) |
| **Aktionen** | Bot-spezifische Funktionen (Broadcast, Module, Sync, ...) |
| **Log** | Audit-Log: jede Aktion, Zeitstempel, auslösender User |

---

## Instanz erstellen — Meta

Beim Erstellen einer Bot-Instanz werden dieselben Felder wie bei allen anderen Ressourcen verwendet:

```toml
[meta]
name        = "Community Bot"
description = "Verwaltet die Köln-Community auf Telegram und Matrix"
icon        = "bot-community"         # aus dem Icon Manager
tags        = ["community", "köln", "broadcast", "moderation"]
visibility  = "group"                 # private | group | public
```

**Name und Icon** sind das, was Benutzer im Messenger sehen.
**Tags** ermöglichen das Finden im Manager und Store.
Die technische Umsetzung (welcher Messenger, welche Token) ist Implementierungsdetail —
der Name sagt was der Bot tut, nicht wie er es tut.

---

## Messenger verbinden

Pro Bot-Instanz können beliebig viele Messenger-Konten hinzugefügt werden:

```
Bot-Instanz "Community Bot"
  + Telegram hinzufügen   → Bot-Token eingeben (+ optional: UserBot-Session)
  + Telegram hinzufügen   → zweiter Telegram-Account
  + Matrix hinzufügen     → Homeserver-URL + Access Token
  + Discord hinzufügen    → Bot-Token
  + Rocket.Chat hinzufügen → Server-URL + Credentials
```

Jeder Messenger-Account ist in Wirklichkeit ein eigenständiger Bot bei der jeweiligen Plattform.
In FreeSynergy erscheinen alle als eine einzige Bot-Instanz.
`fsn-channel` übersetzt Aktionen intern für jeden Messenger.

**Zugangsdaten** werden nie im Klartext gespeichert — sie landen im Secrets-Store
(dieselbe Schicht wie bei Containers). Bot-Instanzen kriegen nur Referenzen.

---

## Unterstützte Messenger und Chats

### Erste Priorität — Self-hosted / Open Source

| Plattform | Rust-Crate | Adapter-Paket | Bemerkungen |
|---|---|---|---|
| **Matrix** | `matrix-sdk` | `adapter-matrix` | Federated, selbst-hostbar, Goldstandard |
| **Rocket.Chat** | `reqwest` (REST + WS) | `adapter-rocketchat` | Selbst-hostbar |
| **Mattermost** | `reqwest` (REST + WS) | `adapter-mattermost` | Selbst-hostbar, Open Source |
| **XMPP** | `xmpp-rs` | `adapter-xmpp` | Offenes Protokoll, viele Clients |
| **Zulip** | `reqwest` | `adapter-zulip` | Selbst-hostbar, gut für Communities |
| **Revolt** | `revolt-rs` | `adapter-revolt` | Open-Source Discord-Alternative |
| **Nextcloud Talk** | `reqwest` | `adapter-nextcloud-talk` | Automatisch aktiv wenn Nextcloud installiert |
| **IRC** | `irc` | `adapter-irc` | Legacy, aber noch genutzt |

### Zweite Priorität — Mainstream

| Plattform | Rust-Crate | Adapter-Paket | Bemerkungen |
|---|---|---|---|
| **Telegram** | `grammers` (UserBot) + `teloxide` (Bot) | `adapter-telegram` | UserBot für volle Kontrolle |
| **Discord** | `serenity` + `poise` | `adapter-discord` | Sehr beliebt in Communities |
| **Slack** | `slack-morphism` | `adapter-slack` | Business-Umfeld |
| **Microsoft Teams** | `reqwest` (Bot Framework) | `adapter-teams` | Corporate |
| **Viber** | `reqwest` | `adapter-viber` | Regional stark (Osteuropa) |
| **Line** | `reqwest` | `adapter-line` | Regional stark (Asien) |

### Dritte Priorität — Eingeschränkt

| Plattform | Adapter-Paket | Einschränkung |
|---|---|---|
| **WhatsApp** | `adapter-whatsapp` | Nur Meta Business API; stark eingeschränkt; Kosten |
| **Signal** | `adapter-signal` | Kein offizieller Bot-API; `signal-cli` (inoffiziell, fragil) |
| **Threema** | `adapter-threema` | Gateway-API vorhanden; Kosten pro Nachricht |
| **Wire** | `adapter-wire` | Wire Bot SDK; Business-Fokus |

### Foren

| Plattform | Adapter-Paket | Bemerkungen |
|---|---|---|
| **Discourse** | `adapter-discourse` | Sehr verbreitet, gute API |
| **Lemmy** | `adapter-lemmy` | Fediverse, selbst-hostbar, ActivityPub |
| **Mastodon** | `adapter-mastodon` | Für Ankündigungen / öffentliche Bots |

### Adapter-Pakete

Jeder Messenger-Support ist ein eigenes Store-Paket (`type = "messenger-adapter"`).
Nur installierte Adapter stehen bei der Bot-Konfiguration zur Verfügung.
Inventory fragt: "Welche Adapter sind aktiv?" — nicht der Bot.

```
Store/
└── messenger-adapters/
    ├── adapter-telegram/
    ├── adapter-matrix/
    ├── adapter-discord/
    └── ...
```

---

## Hinweis zu Telegram

Für volle Kontrolle (Räume erstellen, Mitglieder verwalten) wird ein **UserBot** benötigt,
kein normaler Bot. UserBots laufen über MTProto mit einem echten Account (`grammers` Crate).
Normale Bots (Bot-API via `teloxide`) sind für Gruppen-Verwaltung eingeschränkt.

Ein Telegram-Account kann bis zu **500 Gruppen** haben. Verwaltung über Filterung (siehe unten).

---

## Steuerung — drei Ebenen

Wer einen Bot steuern darf, wird auf drei unabhängigen Ebenen konfiguriert:

### Ebene 1: FSN-Ebene

| Wert | Bedeutung |
|---|---|
| `private` | Nur der Owner (der FSN-User der den Bot erstellt hat) |
| `group` | Alle Mitglieder einer bestimmten FSN-Gruppe |
| `public` | Alle — auch ohne FSN-Account |

### Ebene 2: Messenger-Ebene

| Wert | Bedeutung |
|---|---|
| `everyone` | Jeder in der Gruppe kann Befehle senden |
| `admins` | Nur Messenger-Admins der Gruppe |
| `nobody` | Kein Messenger-User kann direkt steuern |

### Ebene 3: Control Bot

| Wert | Bedeutung |
|---|---|
| `control-bot: <instanz-id>` | Nur dieser Control Bot darf steuern |
| (nicht gesetzt) | Kein Control Bot involviert |

**Wichtig:** Messenger-Admin-Status hat in FreeSynergy keinerlei Bedeutung.
Ein Telegram-Admin kann den Bot nicht steuern wenn er kein FSN-Recht hat.
Der Bot prüft immer FSN-Rechte — nie den Messenger-Status.

```
Telegram-Admin Alice führt /delete_room aus:
  → Bot prüft NICHT: Ist Alice Telegram-Admin?
  → Bot prüft: Hat Alice execute-Recht in FSN für bot.room.delete?
  → Nein → Abgelehnt. Egal was Telegram sagt.
```

Dasselbe gilt für Discord-Owner, Matrix-Admins, etc.

### Rechte pro Funktion pro Gruppe

Im Bot können für jede verbundene Gruppe die Rechte je Funktion gesetzt werden:

```
Gruppe "Projekt Köln" (Telegram):
  /broadcast        → FSN: member,  Messenger: everyone
  /delete_member    → FSN: admin,   Messenger: admins
  /sync_rooms       → FSN: admin,   Messenger: nobody
  /subscribe        → FSN: member,  Messenger: everyone
  /status           → FSN: —,       Messenger: everyone  (kein FSN-Account nötig)
```

---

## Control Bot — Vererbung

Wenn der Control Bot Kind-Bots erstellt, erben diese:

| Was | Geerbt | Überschreibbar? |
|---|---|---|
| Messenger-Accounts | Ja — Control Bot stellt sie bereit | Nein (Kind-Bot hat keine eigenen Tokens) |
| Gruppen-Mitgliedschaften | Ja — Kind-Bot wird automatisch eingeladen | Ja — kann Gruppen entfernen |
| Steuerungs-Einstellungen | Ja — als Startpunkt | Ja — kann pro Kind-Bot überschrieben werden |
| Rechte pro Funktion | Ja — als Startpunkt | Ja |

Kind-Bots kommunizieren nach außen **über den Control Bot**.
Der Control Bot ist der einzige der echte Messenger-Tokens hält.
Wenn der Control Bot offline ist: Kind-Bots arbeiten intern weiter (Bus-Events sammeln),
senden nach außen sobald er wieder da ist.

**Standalone-Bots** konfigurieren alle Zugangsdaten selbst.

---

## Gruppen verwalten (bis 500)

Es werden **keine automatischen Gruppen/Sets** erstellt.
Stattdessen: Filterung + manuelle Collections.

### Filter

| Filter | Beispiel |
|---|---|
| Mitglieder-Anzahl | > 100, < 50 |
| Letzte Aktivität | Aktiv in den letzten 7 Tagen |
| Gruppenname | enthält "Projekt", beginnt mit "DE-" |
| Messenger | Nur Telegram, Nur Matrix |
| Aktive Module | Hat Broadcast aktiv |
| Status | Bot hat Fehler / Bot wurde entfernt |

### Collections

Gruppen können manuell zu Collections zusammengefasst werden.
Eine Gruppe kann in **mehreren Collections** gleichzeitig vorkommen.
Collections haben keine eigene Logik — sie sind nur ein Ordnungs-Werkzeug.

```
Collection "Köln" (12 Gruppen)
Collection "Projekt-Gruppen" (83 Gruppen)
  → "Projekt Köln" ist in beiden
```

### Aktionen auf mehrere Gruppen

Aus dem Filterergebnis oder einer Collection heraus:

```
Filter: Mitglieder > 100 → 34 Gruppen
  ☑ Gruppe A
  ☑ Gruppe B
  ☑ Gruppe C

[Broadcast senden] [Modul aktivieren] [In Collection] [Rechte setzen]
```

---

## Mitglieder-Interaktion

Bots können Mitglieder aktiv ansprechen — wenn sie die Rechte dazu haben:

- **Menüs / Inline-Tastaturen** (Telegram, Discord): Bot präsentiert Auswahlmöglichkeiten
- **Slash-Commands**: Standardmäßig verfügbar, je Gruppe konfiguriert
- **Direkt-Nachrichten**: Bot kann DMs senden (z.B. Erinnerungen, Bestätigungen)
- **Formulare** (Matrix, Rocket.Chat): Bot sendet strukturierte Anfragen

Jede Interaktionsmöglichkeit folgt den konfigurierten Rechten (wer darf was pro Gruppe).

---

## Audit-Log

Jede Bot-Instanz hat ein eigenes Log:

```
2026-03-20 14:23:11  alice         /broadcast → 12 Gruppen
2026-03-20 13:51:04  control-bot   Modul calendar aktiviert
2026-03-20 09:12:44  [System]      Verbindung Telegram verloren → wiederhergestellt
```

| Was wird geloggt | Beschreibung |
|---|---|
| User | Wer hat die Aktion ausgelöst (FSN-User oder System) |
| Aktion | Welcher Befehl / welches Ereignis |
| Ziel | Welche Gruppe, welches Modul |
| Ergebnis | Erfolgreich / Fehler + Fehlermeldung |
| Zeitstempel | UTC |

Der Control Bot kann auf die Logs seiner Kind-Bots zugreifen.
Der Bot Manager zeigt alle Logs aggregiert.

---

## Updates

Bot-Pakete werden manuell über den Store aktualisiert — wie alle anderen Pakete auch.

**Aktueller Stand:** Kein Automatismus. Update = manuell im Store.

**Offener Punkt (TODO):** Automatische Update-Benachrichtigung + One-Click-Update + Rollback.
Vor einem Update muss sichergestellt werden dass Konfiguration + Daten kompatibel bleiben.
Dieser Punkt wird in einer späteren Phase gelöst.

---

## Bus-Events (Überblick)

| Topic | Richtung | Beschreibung |
|---|---|---|
| `bot.broadcast` | BotManager → Bot | Nachricht in Gruppen senden |
| `bot.gatekeeper.approve` | BotManager → Bot | Beitrittsanfrage genehmigen |
| `bot.gatekeeper.deny` | BotManager → Bot | Beitrittsanfrage ablehnen |
| `bot.subscription.add` | BotManager → Bot | Subscription hinzufügen |
| `bot.subscription.remove` | BotManager → Bot | Subscription entfernen |
| `bot.status.request` | BotManager → Bot | Status abfragen |
| `bot.status.response` | Bot → BotManager | Status-Antwort |
| `chat.join_request` | Bot → BotManager | Neuer Beitrittsantrag |
| `chat.join_approved` | BotManager → Bot | Genehmigung ausführen |
| `calendar.event.upcoming` | Desktop → Bot | Termin-Erinnerung |

---

## Einheitliche Befehls-Schnittstelle

Alle Module und Bot-Typen implementieren denselben Trait:

```rust
trait BotCommand {
    fn name(&self) -> &str;             // "/status", "/sync", ...
    fn description(&self) -> &str;
    fn required_right(&self) -> Right;  // read / write / execute
    fn execute(&self, ctx: CommandContext) -> BotResponse;
}
```

Der Bot sammelt automatisch alle Befehle aus allen aktiven Modulen.
`/help` listet alle verfügbaren Befehle — egal welche Module geladen sind.
Neue Module fügen automatisch ihre Befehle hinzu, ohne Bot-Code zu ändern.

---

## fsn-channel — Messenger-Unabhängigkeit

Der Bot schreibt einmal, `fsn-channel` übersetzt für jeden Messenger:

```rust
bot.send("projekt-koeln", "Willkommen!").await?;

// fsn-channel übersetzt intern:
// Telegram:    grammers    → SendMessage
// Matrix:      matrix-sdk  → send_message
// Discord:     serenity    → send_message
// Rocket.Chat: reqwest     → POST /api/v1/chat.sendMessage
```

Welcher Messenger aktiv ist bestimmt das Inventory.
Der Bot-Code ändert sich nie wenn ein neuer Messenger hinzukommt.

`fsn-channel` lebt in `FreeSynergy.Lib`.

---

## Wichtiges Prinzip: Bots reden NIE direkt mit Services

```
FALSCH:
  Bot → HTTP-Request → Outline API → Seite erstellen

RICHTIG:
  Bot → Bus-Event (Rolle: wiki, Topic: page.create)
    → Bus → Bridge (outline-wiki-bridge) → Outline API → Seite erstellen
```

Wenn Outline durch ein anderes Wiki ersetzt wird, funktioniert der Bot weiterhin.

---

## Store-Verzeichnis

```
Store/
├── bots/
│   ├── bot-control/
│   ├── bot-broadcast/
│   ├── bot-gatekeeper/
│   ├── bot-calendar/
│   ├── bot-tickets/
│   ├── bot-tasks/
│   ├── bot-room-sync/
│   └── bundle-bots-all/
└── messenger-adapters/
    ├── adapter-telegram/
    ├── adapter-matrix/
    ├── adapter-discord/
    ├── adapter-rocketchat/
    ├── adapter-mattermost/
    ├── adapter-xmpp/
    ├── adapter-zulip/
    ├── adapter-revolt/
    ├── adapter-nextcloud-talk/
    ├── adapter-irc/
    ├── adapter-slack/
    ├── adapter-teams/
    ├── adapter-viber/
    ├── adapter-line/
    ├── adapter-whatsapp/
    ├── adapter-signal/
    ├── adapter-threema/
    ├── adapter-wire/
    ├── adapter-discourse/
    ├── adapter-lemmy/
    └── adapter-mastodon/
```

---

Weiter: [BotManager](../programme/botmanager/README.md) | [Tasks](tasks.md) | [Bus](bus.md) | [Inventory](inventory.md)
