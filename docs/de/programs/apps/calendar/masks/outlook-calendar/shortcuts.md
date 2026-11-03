# Outlook-Kalender – Tastenkürzel und Direkt-Workflows (Stand: 2026-11-02)

Alle Kürzel stammen aus dem offiziellen Artikel „Keyboard shortcuts for Outlook“ (support.microsoft.com, Reiter *New Outlook for Windows*, *Classic Outlook*, *Outlook on the web*; US-Layout – andere Layouts können abweichen). Die Kalenderkürzel von Teams und Outlook sind laut Artikel identisch. Mac-Kürzel: eigener Artikel „Keyboard shortcuts in Outlook for Mac“ (hier nicht im Detail übernommen). Fundstellen in [index.md](index.md#quellen).

## Neues Outlook für Windows / Outlook on the web

### Navigation und Ansichten

| Taste(n) | Funktion |
|----------|----------|
| `Strg+2` | Zur Kalenderansicht wechseln (allgemein: `Strg+1` Mail, `Strg+3` Copilot, `Strg+4` People) |
| `Alt+Shift+Y` / `Home` | Heute |
| `Strg+Alt+Left` / `Alt+Down` / `Alt+PageDown` | zurück: Tag / Woche / Monat |
| `Strg+Alt+Right` / `Alt+Up` / `Alt+PageUp` | vor: Tag / Woche / Monat |
| `Strg+Alt+Right` / `Strg+Alt+Left` | nächster/vorheriger Zeitraum |
| `Strg+Alt+1` | Tagesansicht |
| `Strg+Alt+2` (auch `Alt+-`) | Wochenansicht; Arbeitswoche ebenfalls `Strg+Alt+2` |
| `Strg+Alt+4` (auch `Alt+ =`) | Monatsansicht |
| `Alt+3` | 3-Tage-Ansicht |
| – | Listenansicht (offiziell: „No shortcut“) |
| `F6` / `Strg+Shift+Tab` | zwischen Bereichen wechseln; `Tab`/`Shift+Tab` zu nächstem/vorherigem Termin |

### Aktionen

| Taste | Funktion |
|-------|----------|
| `Strg+N` | neuen Termin anlegen (auch „Invite Attendees“ über New-Event) |
| `Enter` / `Delete` | markiertes Objekt öffnen / löschen |
| `?` | Kürzelübersicht öffnen; `Alt` = Key-Tips |

## Klassisches Outlook für Windows (Kalender)

| Taste | Funktion |
|-------|----------|
| `Strg+Shift+A` | Termin (appointment) in jeder Ansicht; in Kalenderansicht auch `Strg+N` |
| `Strg+Shift+Q` | Meeting-Anfrage erstellen |
| `Alt+1`…`Alt+9`, `Alt+0` | Tagesraster 1–9 Tage bzw. 10 Tage |
| `Alt+-` / `Ctrl+Alt+3` | Ganze Woche · `Ctrl+Alt+2` Arbeitswoche · `Alt+ =` / `Ctrl+Alt+4` Monat |
| `Strg+G` | „Gehe zu Datum“ (Date Picker) – im geöffneten Termin: Wiederholung festlegen |
| `Alt+H, O, D` | heute zeigen · `Alt+H, X` nächste 7 Tage |
| `Strg+Left/Right` | vorheriger/nächster Tag; `Alt+Up/Down` Woche; `Alt+PageUp/PageDown` Monat |
| `Alt+Home` / `Alt+End` | Wochenanfang / -ende |
| `Strg+Comma` / `Strg+Period` | vorheriger/nächster Termin |
| `Alt+X` | Assistent für die Terminplanung |
| `Alt+V,M` / `Alt+S` / `Alt+D` / `Alt+O` | Erinnerungsfenster / Snooze / Verwerfen / Termin im Reminder öffnen |
| `Alt+H,S,V` (`Strg+Alt+5`) | Schedule im horizontalen Layout (Kalender vergleichen) |
| `Alt+H,O,C` / `Alt+H,S,C` / `Alt+H,P,O` / `Alt+H,F,P` / `Alt+H,E` | Kalender hinzufügen / freigeben / online veröffentlichen / Freigaberechte / Kalender per Mail senden |
| `Alt+F11` / `Alt+F8` | VBA-Editor / Makros ausführen (nur klassisches Outlook) |

## Outlook für Mac

- Eigene Kürzelseite („Keyboard shortcuts in Outlook for Mac“ im Artikel verlinkt) – wurde in diesem Durchlauf **nicht** übernommen; nicht verifiziert.

## Keine eigene Kommandozeile

- Die Kalender-App selbst hat **keine CLI/OCC-artischen Kommandos**. Automatisierung läuft über **Microsoft Graph** (REST + SDKs, siehe [api.md](api.md)); Server-Verwaltung über **Exchange Online PowerShell** (`Set-MailboxFolderPermission` etc. gehört zur Exchange-Ebene, nicht zur App).

## Direkt-URL/Deep-Link-Workflows

- Deep-Link-Formate sind über die `webLink`-Beschreibung der event-Ressource **offiziell dokumentiert**: aktuelle Form `https://outlook.office365.com/calendar/item/{event-id}` (Arbeits-/Schulkonto) bzw. `https://outlook.live.com/calendar/item/{event-id}` (Privatkonto), `{event-id}` = URL-kodierte Event-`id`. Die alte `…/owa/?itemid=…&path=/calendar/item`-Form öffnet nur ältere Web-Versionen; Links funktionieren nicht im iFrame und fordern andernfalls zum Login auf.

## Kürzel fremder Clients (abgrenzend)

- Thunderbird, Merkuro, Apple Kalender, DAVx⁵ usw. haben eigene client-seitige Kürzel ohne Bezug zu Outlook. Da Outlook-Konten für diese Clients ohnehin keinen offenen CalDAV-Zugang bieten, läuft deren Anbindung nur über Microsoft-Apps oder Drittanbieter-Connectoren (inoffiziell).
