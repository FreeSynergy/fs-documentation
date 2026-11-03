# Nextcloud Calendar – Struktur (v6.6.4)

Fundstellen zu allen Aussagen in [index.md](index.md#quellen) (Quelltext-Tag v6.6.4).

## Request-/Programmablauf

1. **Aufruf:** Browser lädt `{base}/apps/calendar/…` → PHP-Route `calendar.view.index` (`ViewController`) rendert `templates/main.php` und liefert **Initial-State** (`CalendarInitialStateService`: `app_version`, `initial_view`, `show_weekends`, `show_week_numbers`, `event_limit`, `skip_popover`, `talk_enabled`, `hide_event_export`, `disable_appointments`, …) an das Frontend.
2. **SPA-Start:** Einstieg `src/main.js` initialisiert Vue 3 + Router + Pinia; `src/services/caldavService.js` baut einen `@nextcloud/cdav-library`-Client auf `rootUrl = {base}/remote.php/dav/` und verbindet (`connect({ enableCalDAV: true })`).
3. **Datenladen:** Kalenderliste per `PROPFIND` auf dem Calendar-Home; Termine pro Ansicht per `REPORT calendar-query` für das sichtbare Zeitfenster (Store `fetchedTimeRanges.js` vermeidet Doppelabfragen); Änderungen in Tabs von anderen Clients werden über Notify-Push-Meldung `calendar_sync` (`NotifyPushListener`) nachgezogen.
4. **Schreiben:** Terminänderungen sind `PUT`/`DELETE` auf die ICS-Objekte im DAV (ETag-basiert); Teilnehmer-Einladungen verarbeitet der Server (iTIP/schedule im `dav`-Backend).
5. **Sonderfunktionen:** Buchungs-, Vorschlags-, Autocomplete- und Konfigurations-Aktionen laufen über die eigenen Controller der App (siehe [api.md](api.md)); die Buchung schreibt den Termin am Ende über `BookingCalendarWriter` wieder per CalDAV in den Zielkalender.
6. **Öffentliche Ansichten:** `/p/{token}` und `/embed/{token}` rendern `templates/public.php`; der CalDAV-Client öffnet die öffentliche Kalender-Sammlung des Servers (`_createPublicCalendarHome`), ohne Nutzer-Login.

## Verzeichnis- und Modulstruktur (Repo)

```
appinfo/            info.xml (Metadaten, Navigations-Eintrag order 5), routes.php
templates/          main.php, public.php, appointments/
lib/                PHP-Backend der App (AppFramework)
├── AppInfo/        Application.php (Bootstrap: Widgets, Listener, Notifier), Capabilities.php
├── Controller/     View, PublicView, Appointment, Booking, AppointmentConfig,
│                   Contact (Autocomplete), Email, Settings, Object (Deep-Link-Resolver),
│                   Proposal, ProposalPublic
├── Service/
│   ├── Appointments/  Config-Service, Slot-Logik (AvailabilityGenerator, SlotExtrapolator,
│   │                  DailyLimitFilter, EventConflictFilter, TimezoneGenerator),
│   │                  BookingService, BookingCalendarWriter, MailService
│   ├── Proposal/      ProposalService (Vorschläge, Votes, Umwandeln in Termin)
│   └── CalendarInitialStateService, JSDataService, ContactsService, ObjectResolverService
├── Db/             Mapper/Entities für Buchungen, Configs und Vorschläge
├── Objects/        JSON-Modelle der Proposal-Domäne (Collection/Object/Vote/…)
├── Listener/       AppointmentBooked, CalendarReference, NotifyPush, UserDeleted
├── BackgroundJob/  CleanUpOutdatedBookingsJob
├── Migration/      DB-Schema (2040, 3000, 3010, 4050, 5050 ×4, 6060)
├── Dashboard/ Profile/ Reference/ Notification/ UserMigration/
└── Http/ Exception/
src/                Vue-3-Frontend (rspack-Bundles)
├── main.js, appointments/main-*.js, proposal-public.ts   ← Bundle-Entries
├── views/          Calendar.vue, EditSimple/EditFull, Appointments/, Proposal/,
│                   ContactsMenuAvailability.vue
├── components/     AppNavigation/ (Kalenderliste, Settings, Import, Shortcuts),
│                   Editor/ (Properties, Repeat, Alarm, Invitees, Resources, Talk,
│                   Attachments, FreeBusy), AppointmentConfigModal/, Appointments/,
│                   Proposal/, Shared/, Subscription/
├── store/          Pinia: calendars, calendarObjects, calendarObjectInstance, settings,
│                   appointmentConfigs, proposalStore, delegation, unscheduledTasks,
│                   importFiles, principals, contacts, davRestrictions, fetchedTimeRanges
├── services/       caldavService (cdav-library), proposalService, appointmentService,
│                   autocompleteService, freeBusyService, attachmentService, talkService …
├── fullcalendar/   View-Konfiguration, eventSources, Interaktion (eventDrop …)
└── models/ types/ utils/ mixins/
```

Build-Eintrittspunkte (`rspack.config.js`): `main` (Haupt-App), `reference` (Links-Vorschau), `contacts-menu` (Verfügbarkeit im Kontakte-Menü, vom `Application::boot()` global nachgeladen), `appointments-booking`, `appointments-confirmation`, `appointments-overview`, `proposal-public`.

## Konfiguration

- **Administrativ (App-Werte, per `occ config:app:set calendar …`):**
  - `hideEventExport=yes` blendet den ICS-Export einzelner Termine aus;
  - `disableAppointments=yes` schaltet die Buchungsfunktion ab.
- **Pro Nutzer** (über UI gespeichert, Endpunkt `POST /v1/config/{key}`; Schlüssel u. a. aus `src/store/settings.js`): `view` (Standardansicht), `timezone`, `showWeekends`, `showWeekNr`, `showTasks`, `tasksSidebar`, `eventLimit`, `skipPopover`, `slotDuration`, `defaultReminder`, `defaultReminderPartDay`, `defaultReminderFullDay`, `attachmentsFolder`.
- **Abhängigkeiten zur Laufzeit:** Nextcloud-App `dav` (CalDAV-Backend, zwingend), optional `talk` (Konferenzen), `contacts` (Autocomplete, Geburtstage), Circles, Tasks/Deck (VTODO-Quellen), `notify_push` (Live-Sync), Notifications-App (Erinnerungen/Buchungen).

## Datenmodell

- **Kalenderdomäne liegt nicht in der App-Datenbank**, sondern als ICS-Objekte (VEVENT/VTODO/VJOURNAL) im CalDAV-Backend des Servers; Kalendereigenschaften sind WebDAV-Properties (displayname, `{http://nextcloud.com/ns}calendar-color` …), Freigaben sind CalDAV-ACLs.
- **Eigene Tabellen** (`lib/Db`, Migrationen):
  - `calendar_appt_configs` – Terminbuchungs-Konfigurationen (Inhaber, Token, Zielkalender, Sichtbarkeit, Availability-JSON, Dauern/Limits)
  - `calendar_appt_bookings` – gebuchte/vorläufige Buchungen (Token, Slot, Status)
  - `calendar_proposal_dts` – Meeting-Vorschläge (UID, UUID/Token, Titel, Beschreibung, Ort, Dauer, `response_notify`), dazu
  - `calendar_proposal_pts` (Teilnehmer inkl. Realm/Status/Attendance),
  - `calendar_proposal_dats` (Kandidatentermine),
  - `calendar_proposal_vts` (Votes je Teilnehmer/Termin)
- **Keine Sync-Tabelle/Caches:** die App hält keine Terminspiegel; `fetchedTimeRanges` ist nur ein Laufzeit-Cache im Browser.

## Deployment

- **Regelweg:** Installation über den Nextcloud App Store (`apps.nextcloud.com/apps/calendar`) oder direkt in der Instanz; Release-Tarballs (signiert gebaut) hostet `github.com/nextcloud-releases/calendar`. App v6.6.4 benötigt Nextcloud **32–35** und PHP **8.1–8.5**; das CalDAV-Backend ist bereits Teil des Servers.
- **Entwickler-Build:** `composer install` + `npm ci`, Frontend-Build mit rspack (Node erforderlich); Artefakt wird wie eine normale Nextcloud-App unter `apps/calendar` bereitgestellt.
- **Browserunterstützung** laut README: Chrome/Chromium ≥ 76, Edge ≥ 40, Firefox ≥ 60, Safari ≥ 12.1 (IE 11 wird dort noch genannt – für aktuelle 6.x-Versionen anzweifeln, nicht separat verifiziert).
- **Betriebshinweis:** Nur hinter HTTPS; CalDAV-Basic/App-Passwörter und Tokens der öffentlichen Seiten sind ohne TLS ungeschützt. Cron des Servers bestimmt, wann Buchungs-Cleanup, Abo-Aktualisierung und E-Mail-Erinnerungen laufen.
