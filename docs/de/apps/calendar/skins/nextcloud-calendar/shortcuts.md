# Nextcloud Calendar – Tastenkürzel und Direkt-Workflows (v6.6.4)

Die App registriert **eigene, echte Tastenkürzel** über `useHotKey` (aus `@nextcloud/vue`) – im Gegensatz zu vielen anderen Tools hier ist die Liste also tatsächlich implementiert, nicht nur dekoriert. Eine Übersichtsliste zeigt die App selbst unter **Kalendereinstellungen → ShortcutOverview** (`src/components/AppNavigation/Settings/ShortcutOverview.vue`). Fundstellen in [index.md](index.md#quellen).

## Verifizierte Kürzel (Registrierung im Quelltext belegt)

### Navigation

| Taste(n) | Funktion | Beleg |
|----------|----------|-------|
| `P` oder `K` | Vorheriger Zeitraum | `AppNavigationHeaderDatePicker.vue: useHotKey(['p','k'], …)` |
| `N` oder `J` | Nächster Zeitraum | `AppNavigationHeaderDatePicker.vue: useHotKey(['n','j'], …)` |
| `T` | Heute | `AppNavigationHeaderTodayButton.vue: useHotKey('t', …)` |

### Ansichten

| Taste(n) | Ansicht | Beleg |
|----------|---------|-------|
| `1` oder `D` | Tag (`timeGridDay`) | `AppNavigationHeaderViewMenu.vue` |
| `2` oder `W` | Woche (`timeGridWeek`) | dito |
| `3` oder `M` | Monat (`dayGridMonth`) | dito |
| `4` oder `Y` | Jahr (`multiMonthYear`) | dito |
| `5` oder `L` | Liste (`listMonth`) | dito |

### Aktionen

| Taste | Funktion | Beleg |
|-------|----------|-------|
| `C` | Neuen Termin anlegen | `AppNavigationHeaderNewEvent.vue: useHotKey('c', …)` |
| `H` | Kürzelübersicht zeigen | **nur in der Übersichtsliste aufgeführt; in v6.6.4 keine Registrierung via `useHotKey` im Quelltext gefunden – Funktion nicht verifiziert** (die Übersicht öffnet sich sonst per Klick auf die Einstellungen) |

### Termin-Editor (nur im geöffneten Editor; `src/mixins/EditorMixin.js`)

| Taste | Funktion | Beleg |
|-------|----------|-------|
| `Escape` | Editor schließen | `useHotKey('Escape', …)` |
| `Strg` + `Enter` | Termin speichern | `useHotKey('Enter', …, { ctrl: true, allowInInput: true })` |
| `Strg` + `Entf` | Termin löschen | `useHotKey('Delete', …, { ctrl: true })` |
| `Strg` + `D` | Termin duplizieren | `useHotKey('d', …, { ctrl: true })` |

Hinweise: `useHotKey` ignoriert die Kürzel außerhalb des Editors in Textfeldern (Editor-Kürzel teils mit `allowInInput`); Mac nutzt ⌘ statt Strg, da `ctrl: true` die Cmd-Taste mit abdeckt – in diesem Detail **nicht verifiziert**, da die Composable in `@nextcloud/vue` liegt und nicht im App-Repo.

## Keine App-eigene Kommandozeile

Es existiert **kein OCC-Kommando und keine CLI dieser App** – die App kennt nur Web-Routen und einen automatischen Hintergrund-Job (`CleanUpOutdatedBookingsJob`). Serverweite DAV-Wartung (z. B. Geburtstagskalender-Sync) gehört zur `dav`-App des Nextcloud-Servers, nicht zu Nextcloud Calendar.

## Direct-URL-Workflows (die „Schnellstart-API“ der App)

Alle URLs relativ zu `{base}/index.php/apps/calendar/` (Kurzform `{base}/apps/calendar/…`), gültig nach Login im Browser:

| URL | Effekt |
|-----|--------|
| `…/new` | Neuen Termin öffnen |
| `…/new/{isAllDay}/{dtStart}/{dtEnd}` | Vorbelegten neuen Termin öffnen (z. B. `…/new/0/20261103T090000/20261103T100000`) |
| `…/edit/{objectId}` | Termin bearbeiten; `objectId` = Base64 von `/remote.php/dav/calendars/{user}/{kalender}/{objekt}.ics` |
| `…/object/{uid}` bzw. `…/object/{uid}/{recurrenceId}` | Dauerhafter Link nur nach iCal-UID (weiterleiten; `recurrenceId` = Unix-Timestamp oder `next`) |
| `…/{view}/{timeRange}` | Ansicht+Zeitfenster, `view` ∈ `timeGridDay`, `timeGridWeek`, `dayGridMonth`, `multiMonthYear`, `listMonth` |
| `…/p/{token}` | öffentlichen Kalender anzeigen; `…/embed/{token}` ohne Nextcloud-Oberfläche (iframe-tauglich) |
| `…/appointments/{userId}` | Buchungsseiten eines Nutzers |
| `{base}/calendar/proposal/{token}` | Abstimmungsseite eines Meeting-Vorschlags |

## Kürzel fremder Clients (abgrenzend)

Thunderbird, Thunderbird-Sonnation, Kalendar, Apple Kalender, DAVx⁵ usw. haben **eigene, client-seitige** Kürzel, die nichts mit dieser App zu tun haben – sie wirken nur im jeweiligen Programm, nicht in der Nextcloud-Web-App. Wer per CalDAV (nicht per Web-UI) arbeitet, hat ohnehin keine App-Kürzel; Automatisierung läuft dort über CalDAV-Requests (siehe [api.md](api.md)).
