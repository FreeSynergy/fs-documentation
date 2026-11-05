# Merkuro – Struktur (Merkuro Calendar 26.08.2)

Fundstellen zu allen Aussagen in [index.md](../index.md#quellen) (Quelltext-Tarball 26.08.2).

## Request-/Programmablauf

1. **Start:** `merkuro-calendar` initialisiert Qt/KF (`KAboutData` „merkuro.calendar“, Icon `org.kde.merkuro.calendar`), meldet sich als Single-Instance am Session-D-Bus (`KDBusService::Unique`) und lädt das QML-Modul `org.kde.merkuro.calendar` (`Main.qml`).
2. **Datenzugang:** Die App verbindet sich mit **Akonadi** (`Akonadi::ETMCalendar`). `CalendarManager` (QML-Singleton) exponiert Sammlungen (`collections`, `todoCollections`, `viewCollections`, `allCalendars` als `Akonadi::CollectionFilterProxyModel`), einen `Akonadi::IncidenceChanger` (Zentralstelle aller Schreibvorgänge inkl. Undo/Redo) und Fabrikmethoden für `IncidenceWrapper`.
3. **Modelle → Views:** C++-Qt-Modelle (`monthmodel`, `multidayincidencemodel`, `hourlyincidencemodel`, `incidenceoccurrencemodel`, `holidaymodel`, `attendeesmodel`, `attachmentsmodel`, `itemtagsmodel`, `todosortfilterproxymodel`, `infinitemerkurocalendarviewmodel` …) füttern die QML-Ansichten (`MonthView`, `WeekView`, `DayView`, `ScheduleView`, `TodoView` mit Swipeable/Basic-Varianten).
4. **Schreiben:** Editor (`IncidenceWrapper` → `IncidenceEditorDialog`/`IncidenceEditorPage`) übergibt an `IncidenceChanger`; Akonadi persistiert und synchronisiert (bei Online-Kalendern über die betreffende kdepim-runtime-Ressource, z. B. CalDAV).
5. **Import:** `.ics`-Argumente/Desktop-Aufruf laufen durch `Importer` nach Akonadi.
6. **Reminders:** `RemindersModel` pflegt VALARMs; Auslösung übernimmt die KDE-PIM-Infrastruktur (Akonadi/ Benachrichtigungen), nicht die App zur Laufzeit.

## Verzeichnisstruktur (Repo `pim/merkuro`)

```
CMakeLists.txt            Release-Service-Version (26.08.2), Qt ≥6.9, KF ≥6.25, PIM-Bibs 6.8.2
src/
├── org.kde.merkuro.desktop.in / org.kde.merkuro.metainfo.xml   Suite-Einstieg
├── launcher/             merkurolauncher (App-Auswahl der Suite)
├── components/           gemeinsame Suite-Bausteine
│   ├── abstractmerkuroapplication.{h,cpp}  Basis-App-Klasse (Aktionen, Menü)
│   ├── accountsmodel, collectionutils, sortedcollectionproxymodel
│   └── qml/              BaseApplication, Menüs (File/Edit/Help/Settings/Window + Native-*),
│                         SystemAccountsForm, Delegates, Bars, Controls, Location …
├── calendar/             ← Kern dieser Doku (Binary merkuro-calendar)
│   ├── main.cpp          CLI, D-Bus-Single-Instance, Importer-Anbindung
│   ├── calendarapplication.{h,cpp}  Aktionen/Shortcuts, D-Bus-Objekt /Calendar
│   ├── calendarmanager.{h,cpp}      Akonadi-Zugriff, Collections, IncidenceChanger
│   ├── datetimestate, filter, incidencewrapper, mousetracker, remindersmodel, utils
│   ├── models/           Month/MultiDay/Hourly/Occurrence/Holiday/Attendees/
│   │                     Attachments/Tags/TodoSortFilter/TimezoneList …
│   ├── calendarconfig.kcfg(c)       → kalendarrc
│   ├── importer.{h,cpp}             ICS-Import
│   ├── org.kde.calendar.Calendar.xml  D-Bus-Interface
│   ├── org.kde.merkuro.calendar.desktop / .metainfo.xml
│   └── qml/              Main.qml, BottomToolBar, Drawers (MainDrawer, IncidenceInfoDrawer),
│                         MainViews/ (MonthView, WeekView, DayView, ScheduleView, TodoView,
│                         Swipeable*/Basic* Grids), Dialogs/ (IncidenceEditorDialog/Page),
│                         incidenceeditor/, Settings/ (ViewSettings, FreeBusy, Source, Configurations),
│                         IncidenceEditorManager.qml (Singleton)
├── contacts/             merkuro-contact (Schwester-App)
└── mail/                 merkuro-mail (Schwester-App, noch in Arbeit)
po/                       Übersetzungen
```

QML-Modul-URI: `org.kde.merkuro.calendar` (`qt_add_qml_module`).

## Konfiguration

- **`kalendarrc`** (KConfig, Schema `calendarconfig.kcfg`): Gruppen `General` (`showMenubar`, `forceCollapsedMainDrawer`, `enableMaps`, `enableMailIntegration`, `locationMarker`, `lastOpenedView`), `MainDrawer`, `Editor` (zuletzt genutzte Event-/Todo-Sammlung), `GeneralView` (Feiertage/Regionen, Aufgaben ein/aus, Pop-up vs. Drawer), `MonthView`/`WeekView`/`ScheduleView` (Rastermodi, Wochennummern, Kopfzeilen), `TaskView` (Sortierung, Richtung, erledigte Unteraufgaben, Dimmung).
- **Konten/Ordner:** liegen bei Akonadi (`~/.config/akonadi/`, Datenbank unter `~/.local/share/akonadi/`); Ressourcen werden über KDE-Einstellungen bzw. `SystemAccountsForm` angelegt.
- Kurzanpassung über die KDE-Shortcut-Einstellungen (Aktionen wie `open_month_view` sind KAuthorized-basiert überschreibbar, gespeichert u. a. in `actionentry.rc`).

## Datenmodell

- **Master-Datenhaltung ist Akonadi**, nicht die App: Collections = Kalender/Aufgabenlisten; Items = Incidences (VEVENT, VTODO, VJOURNAL) als KCalCore-Objekte; Tags/Kategorien, Anhänge (Akonadi-Relationen), Teilnehmer (CTA), Erinnerungen (VALARM).
- App-interne Modelle: `IncidenceWrapper` (Editor-Zustand inkl. RRULE-Feldern: Daily/Weekly/Monthly/Yearly/Custom, Exceptions), `DateTimeState` (Datums-Navigation), Occurrence-/Sortier-Proxy-Modelle.
- **Keine eigene Datenbank/kein Cache in der App**; alle Lese-/Schreibpfade führen durch Akonadi.

## Deployment

- **Distro-Pakete:** App heißt in den meisten Distributionen weiterhin `kalendar`-bis-23.08, seither `merkuro` (Paket `merkuro`, Binaries `merkuro-*`); Flatpak/NEON über KDE-Repositories.
- **Selbstbau:** CMake ≥ 3.29, Ninja empfohlen; zwingend aktuelle KDE-PIM-Bibliotheken – die README empfiehlt ausdrücklich **kdesrc-build**; vor dem ersten Start `kdepim-runtime` installieren und `akonadictl restart` ausführen, sonst fehlen Online-Ressourcen.
- **Laufzeit:** KDE-Desktop-Umgebung nicht Pflicht, aber Akonadi-Dienst muss laufen; Qt 6.9+, KF 6.25+; Mobilvariante identischer Code (Kirigami passt UI an).
- **Beziehungen:** Schwester-Projekte `pim/akonadi`, `pim/kdepim-runtime` (Ressourcen), `pim/merkuro`-Suite untereinander gekoppelt; Fehlermeldungen laufen über bugs.kde.org (Produkt „merkuro“).
