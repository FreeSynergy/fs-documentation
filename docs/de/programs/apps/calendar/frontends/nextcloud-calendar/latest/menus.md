# Nextcloud Calendar – Menü- und Navigationsstruktur (v6.6.4)

Alle Einträge sind dem Quelltext des Tags v6.6.4 entnommen (Komponenten unter `src/views/Calendar.vue`, `src/components/AppNavigation/…`, `src/views/EditFull.vue`; englische Original-Labels zitiert, deutsche Übersetzung kann abweichen). Fundstellen in [index.md](../index.md#quellen).

## Gesamtlayout der Web-App

```
Nextcloud-Header (Server: App-Liste, Avatar, Suche)
└── Calendar-App (NcContent)
    ├── linke Seitenleiste (NcAppNavigation)
    │   ├── Kopf: Ereignisfilter, Datumsauswahl, Neuer Termin, Heute, Ansichtsmenü
    │   ├── Liste: Kalender, Abos, Vorschläge, Buchungen, Papierkorb
    │   └── Fuß: Kalendereinstellungen
    ├── Hauptbereich: Kalender-Raster (FullCalendar) + Umschalter „Unscheduled tasks“
    └── Editor-Ebene: schneller Editor / Detail-Editor / Modals
```

## Seitenleiste – Kopfzeile (`AppNavigationHeader.vue`)

- Suchfeld **„Filter events …“** (filtert Termine in der aktuellen Ansicht)
- **Datumsauswahl** (Date Picker, `AppNavigationHeaderDatePicker`)
- **„New event“** (`AppNavigationHeaderNewEvent`, nur eingeloggte Nutzer)
- **„Today“** (Heute-Button)
- **Ansichtsmenü** (`AppNavigationHeaderViewMenu`): **Day / Week / Month / Year / List** – exakt die fünf FullCalendar-Views der Routen (`timeGridDay`, `timeGridWeek`, `dayGridMonth`, `multiMonthYear`, `listMonth`)

## Seitenleiste – Liste (`CalendarList.vue`)

- Abschnitt **„My calendars“** mit „Add new“-Menü (`CalendarListNew.vue`):
  - **New calendar** (neuer Kalender)
  - **New calendar with task list** (Kalender mit Aufgabenliste)
  - **New subscription from link (read-only)** (WebCal-Abo aus `http(s)://`, `webcal(s)://`-Link)
  - **Add public holiday calendar** (Feiertagskalender)
  - **Add custom public calendar** (eigener öffentlicher Kalender)
- **Kalendereinträge** (`CalendarListItem.vue`, Kontextmenü je Kalender):
  - **Disable/Enable calendar** (ein-/ausblenden)
  - Beschriftungen **„Shared with you by …“** / **„Delegated to you by …“**
  - **Copy public link** (öffentlichen Link kopieren)
  - **Edit and share calendar** bzw. **Edit calendar** (`EditCalendarModal`: Details, Teilen mit Nutzern/Gruppen/Circles, **PublishCalendar** für die öffentliche Freigabe, Internal link, Löschen)
- Abschnitt **öffentliche Kalender** (`PublicCalendarListItem.vue`)
- **Meeting-Vorschläge**: `ProposalEditor` + `ProposalList` (nur eingeloggt)
- **Terminbuchungen**: `AppointmentConfigList.vue` („New appointment config“-Einstieg, Buchungslinks verwalten)
- **Papierkorb** (`Trashbin.vue`, erscheint bei gelöschten Objekten/Kalendern)

## Seitenleiste – Fuß (`Settings.vue`)

Einstiegspunkt **„Calendar settings“**, darunter Gruppen:

- **General**: voreingestellter Kalender für eingehende Einladungen (*Default calendar for incoming invitations*), **Availability settings** (eigene Erreichbarkeit), **CalDAV**-Block mit kopierbaren URLs: **CalDAV URL** und **Server Address for iOS and macOS**
- **Appearance**: **Birthday calendar**, **Tasks in calendar**, **Weekends**, **Week numbers**, **Limit number of events shown in Month view**, **Density in Day and Week View**
- **Editing**: **Default reminder for part-day events**, **Default reminder for full-day events**, **Simple event editor** (Option: „More details“ öffnet den Detail-Editor)
- **Files**: Anlage-Ordner für Termin-Anlagen (`SettingsAttachmentsFolder.vue`)
- **Delegation**: Delegierende/Delegationen mit Lese-/Schreibrecht verwalten (`SettingsDelegationSection.vue`)
- **ICS-Import** (`SettingsImportSection.vue`, Import-Bildschirm mit Fortschritt pro Datei)
- **Tastaturkürzel-Übersicht** (`ShortcutOverview.vue`)

## Hauptbereich

- **Kalender-Raster** (`CalendarGrid.vue`): FullCalendar mit Vor-/Zurück und Zeitsprung (Datumsauswahl sitzt in der Seitenleisten-Kopfzeile), Termine per Drag & Drop verschieb-/resizebar.
- **„Show unscheduled tasks“**-Umschalter (NcActions-Button) öffnet rechte Seitenleiste **„Unscheduled tasks“** (`UnscheduledTasksList.vue`).
- Leere Ansicht `EmptyCalendar.vue`, wenn kein Kalender vorhanden ist.

## Termin-Editor

**Schneller Editor** (`EditSimple.vue`): Titel, Start/Ende/Dauer, Kalender, ganztägig, „More details“-Übergang.

**Detail-Editor** (`EditFull.vue`, Titel **„Detailed event editor“**):

- Actions-Menü oben rechts: **Copy link**, **Export** (ICS-Download, serverseitig sperbar via `hideEventExport`), **Duplicate**, **Delete** – bei Serien zusätzlich **Delete this occurrence** / **Delete this and future occurrences** / **Delete entire series**
- Kopf: Titel, Kalender-Picker mit Farbe, ganztägig-Schalter
- Abschnitte (Komponentenordner `src/components/Editor/`):
  - **Properties** (Zeit/Zeitzone, Ort, Ressourcen/Räume, Beschreibung, Kategorie-Flags)
  - **Repeat** (Wiederholungs-Editor)
  - **Alarm** (Erinnerungen, mehrere, Zeiteinheiten)
  - **Invitees** (Teilnehmer verwalten; Abschnittsname **„Managing shared access“**; Free/Busy-Einblendung, Slotvorschläge)
  - **Attachments** (Dateianhänge aus Files)
  - **Add Talk conversation** (Konferenzraum anlegen/verknüpfen)
  - Einladungs-Annahmebuttons (**InvitationResponseButtons**: annehmen/vorläufig/ablehnen)
- Speichern-Buttons (`SaveButtons.vue`), Verwerfen-Bestätigung (**Discard changes?**)

## Öffentliche/ eingebettete Ansichten (eigene Navigation)

- `/p/{token}`: Nextcloud-Header mit Kalendername + Ansichtsmenü (keine Seitenleisten-Bearbeitung).
- `/embed/{token}`: `EmbedTopNavigation.vue`/`EmbedHeader.vue` – schlanleiste mit Titel, Ansichtsumschalter, „Open in Nextcloud“-Einstieg.
- **Buchungsseite** (`/appointments/{userId}`, `/appointment/{token}`): Slotliste + Formular, keine Kalender-Navigation.
- **Abstimmungsseite** (`/calendar/proposal/{token}`): Vorschlag mit Kandidatenterminen und Voting-UI, eigene Minimalnavigation (`ProposalPublic.vue`).

## Server-seitige Einstiegspunkte außerhalb der App

- Nextcloud-**Dashboard**: Widget „kommende Termine“ (`CalendarWidget.php`).
- **Kontakte-Menü/Avatar**: Verfügbarkeitsanzeige (`ContactsMenuAvailability.vue`).
- **Profilseite**: Link „Termine buchen“ (Profile-Link-Action `AppointmentsAction.php`).
