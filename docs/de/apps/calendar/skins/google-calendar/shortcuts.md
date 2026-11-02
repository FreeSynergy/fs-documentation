# Google Kalender – Kurzbefehle (Stand: 2.11.2026)

Google Calendar **hat eigene Tastaturkürzel** für die Web-Oberfläche auf dem Computer. Grundlage ist der offizielle Hilfartikel „Tastenkombinationen in Google Kalender verwenden“ (`https://support.google.com/calendar/answer/37034`, Computer-Version).

## Aktivieren

Tastenkürzel sind nicht per Default an: **Zahnrad „Einstellungen“ → Kästchen „Tastenkombinationen aktivieren“ → „Speichern“**. Danach zeigt die Taste **`?`** (Fragezeichen) die vollständige, kontextbezogene Liste im Kalender selbst.

## Navigation

| Aktion | Taste |
|--------|-------|
| Zum nächsten Zeitraum blättern | `J` oder `N` |
| Kalender aktualisieren | `r` |
| Zum aktuellen Tag | `t` |
| Zum Abschnitt „Kalender hinzufügen“ | `+` |
| Cursor ins Suchfeld | `/` |
| Zur Seite „Einstellungen“ | `s` |
| Zu einem bestimmten Datum springen | `g` |
| Alle Kürzel anzeigen | `?` |

## Ansichten wechseln

| Ansicht | Taste |
|---------|-------|
| Tagesansicht | `1` oder `D` |
| Wochenansicht | `2` oder `W` |
| Monatsansicht | `3` oder `M` |
| Benutzerdefinierte Ansicht | `4` oder `X` |
| Terminübersicht (Schedule) | `5` oder `A` |

(Ein Kürzel für die Jahresansicht ist im offiziellen Artikel nicht aufgeführt.)

## Termine

| Aktion | Taste |
|--------|-------|
| Neuen Termin erstellen | `c` |
| Termindetails öffnen | `e` |
| Termin löschen | `Rücktaste` / `Entf` |
| Rückgängig machen | `z` |
| Termin speichern (Termindetailseite) | `⌘ + S` (Mac) / `Strg + S` (Windows) |
| Von Termindetails zurück zum Raster | `Esc` |

## Seitenleiste (Google Tasks und Google Notizen)

| Plattform | Tasten |
|-----------|--------|
| Windows | `Strg + Alt + .` oder `Strg + Alt + ,` |
| Chromebook | `Alt + Umschalt + .` oder `Alt + Umschalt + ,` |
| Mac | `⌘ + Wahltaste + .` oder `⌘ + Wahltaste + ,` |

## Mobile Apps

Für Android/iOS listet die Hilfe **keine eigenen Kurzbefehle** – dort gibt es nur die Touch-Bedienung.

## Direct-URLs und automatisierte Abläufe

- **Weboberfläche:** `https://calendar.google.com` – nach Login direkt in die Standardansicht
- **ICS-Adressen:** Die „Öffentliche Adresse im iCal-Format“ und „Privatadresse im iCal-Format“ stehen pro Kalender unter Dreipunkt-Menü → „Einstellungen und Freigabe“ (belegt im Export-Hilfartikel); sie lassen sich anderen Clients als Abo-URL geben
- **Kalender per URL abonnieren:** Über „Weitere Kalender hinzufügen“ → „Per URL“ (eigene Adressen in andere Tools übernehmen)
- **CLI/API-Workflows (Google-offiziell):** Terminganlegen ohne UI über die API, z. B.
  `POST https://www.googleapis.com/calendar/v3/calendars/primary/events/quickAdd?text=Zahnarzt+am+Freitag+um+15`
  (Methode `events.quickAdd`, Discovery v3); Änderungen per Push-Kanal abonnieren statt pollern (siehe [api.md](api.md))

## Kurzbefehle fremder Clients (nur client-seitig!)

Wer Google Kalender in anderen Programmen nutzt, bedient deren Tasten – sie gehören **nicht** zu Google Calendar:

- **Thunderbird:** `D/W/M` Ansichten, `Strg+N` neuer Termin – wirkt auf Google-Daten nur, wenn eine Brücke (Ergänzung) die Calendar API spiegelt; natives CalDAV gibt es bei Google nicht
- **Merkuro (KDE):** `Strg+N` neuer Termin – setzt ebenfalls eine API-/Sync-Brücke voraus
- **Outlook/Exchange-Wrapper:** Microsoft-eigene Kürzel, keine Google-Funktion

Alle diese Tasten erzeugen lediglich normale Anfragen an den jeweiligen Client; Google Calendar selbst kennt sie nicht.
