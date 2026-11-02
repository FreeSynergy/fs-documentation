# Kalendar / Merkuro – Menü- und Navigationsstruktur (Merkuro Calendar 26.08.2)

Alle Einträge aus dem QML-/C++-Quelltext des Tarballs 26.08.2 (`src/calendar/calendarapplication.cpp`, `src/components/…`, `src/calendar/qml/…`); Original-Labels englisch zitiert. Fundstellen in [index.md](index.md#quellen).

## Desktop: Menüleiste (abschaltbar, `showMenubar`)

Die Menüs stammen aus `src/components/qml/` und werden durch die zentral registrierten `QAction`s der `mainCollection()` gefüllt:

- **File**: *Quit Merkuro*
- **Edit**: *Undo Text*, *Redo Text*, *Cut*, *Copy*, *Paste*, *Delete*, *Select All* (Textfeld-Standardaktionen)
- **Window**: *Enter/Exit Full Screen*
- **Settings**: u. a. *Show Menubar* (Umschalter), *Manage Tags…*
- **Help**: *Merkuro Handbook*
- Dazu die von der App-Klasse registrierten Aktionen (unten), die in Menüleiste/Werkzeugleiste erscheinen; Standard-Menübausteine (Thema, Kurzübersicht …) kommen aus Kirigami Addons.

## Zentrale Aktionen (`CalendarApplication::setupActions`)

### Ansichten (gegenseitig exklusive Gruppe, Shortcuts in [shortcuts.md](shortcuts.md))

| Aktion | Standard-Kürzel |
|--------|-----------------|
| *Month View* | Strg+1 |
| *Week View* | Strg+2 |
| *Work Week View* | Strg+2 (Quelltext so – gleiches Kürzel wie Week View, Kollision im Code) |
| *3 Day View* | Strg+3 |
| *Day View* | Strg+4 |
| *Schedule View* | Strg+5 |
| *Tasks View* | Strg+6 |

### Navigation

- *Backwards*, *Forwards* (im Aufgabenansicht-Modus deaktiviert), *To Today*, *To Date…*

### Erstellen / Import / Bearbeitung

- *New Event…*, *New Task…* (ohne Default-Kürzel registriert), *Import Calendar…*
- *Undo*, *Redo* (Termin-/Aufgabenänderungen)

### Aufgabenansicht-Feinsteuerung

- Sortierung: *Alphabetically*, *By Due Date*, *By Priority Level*
- Reihenfolge: *Ascending order*, *Descending Order*
- Filter: *Show Completed Tasks*, *Show Today Only*

### Sonstiges

- *Refresh All* (F5), *Manage Tags…*, Anwendungssprache wechseln (*switch_application_language*)

## Mobil (Plasma Mobile / Touch)

- **BottomToolBar** (`src/calendar/qml/BottomToolBar.qml`): Umschalter **Month / 3-Day / Day / Schedule / Tasks** + „New Event“-Aktion.
- Navigation über **Kirigami-Seiten-Stack** (`pageStack.layers`): Editoren und Einstellungen werden als Ebenen übereinander geschoben; Wisch-Gesten zwischen Monats-/Wochenrastern (Swipeable-Modi).
- Keine klassische Menüleiste; Aktionen erreichen das UI über Global-Drawer und ToolBar-Menüs.

## Seitenleiste / Global Drawer (`MainDrawer.qml`)

- Abschnitt **Kalender/Collections** (Sichtbarkeit pro Kalender, Farben) und Abschnitt **Tags** (`collectionsSectionExpanded`, `tagsSectionExpanded` in `kalendarrc`).
- Darunter Einstieg in **Einstellungen** mit Seiten:
  - **ViewSettingsPage** (Ansichts-Feineinstellungen),
  - **Configure Availability / FreeBusySettingsPage** („Publish your availability information automatically“, Mindestabstand in Minuten),
  - **SourceSettingsPage** (Kalenderquellen),
  - **ConfigurationsView** (Gesamtübersicht),
  - Kontenverwaltung über `SystemAccountsForm`/Akonadi-Ressourcen.
- Termininfo erscheint als **Drawer** (`IncidenceInfoDrawer`) oder Pop-up (`useIncidenceInfoPopup`), Bearbeiten als Dialog (Desktop) bzw. Seite (Mobil).

## Externer Einstiegspunkt

- Über D-Bus kann ein Termin per `showIncidenceByUid` direkt geöffnet werden (siehe [api.md](api.md)); Dateisystem-Aufruf `merkuro-calendar datei.ics` öffnet den Importdialog statt eines Menüs.
