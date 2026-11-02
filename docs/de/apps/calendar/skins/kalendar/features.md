# Kalendar / Merkuro – Funktionen (verifiziert an Merkuro 26.08.2)

Aktuell dokumentierte Version: **Merkuro Calendar 26.08.2** (Kalendar heißt seit KDE Gear 23.08 „Merkuro“). Alle Punkte stammen aus dem Quelltext des Release-Tarballs; Fundstellen in [index.md](index.md#quellen).

## Ansichten

- Sieben Betriebsarten laut `CalendarApplication::Mode`-Enum: **Monat, Woche, 3 Tage, Tag, Terminplan (Schedule), Aufgaben, Arbeitswoche**; Umschalten über Menü/Shortcuts, Vorwärts/Rückwärts/Heute.
- **Wischbare Monats-/Wochen-/Terminplan-Raster** (Swipeable- und Basic-Varianten umschaltbar in `kalendarrc`), Wochennummern, ausrichtbare/benannte Wochentagsköpfe.
- **Terminplan-Ansicht** als Liste kommender Termine (Wochen-Header, leere Tage ausblendbar).
- **Aufgabenansicht** als Baum (Unteraufgaben), Sortierung nach Fälligkeit/Alphabet/Priorität, auf-/absteigend, erledigte ein-/ausblenden.
- Termininfo wahlweise als **Pop-up oder Drawer** (`useIncidenceInfoPopup`).
- Abschießbare Seitenleiste mit Kalender-/Tags-Abschnitten (`MainDrawer`), auf Mobil Bottom-Toolbar.

## Termine, Aufgaben, Journale

- **Termin-Editor** (Desktop als Dialog, mobil als Seite): Titel, Beschreibung, Start/Ende, **ganztägig**, **Zeitzone je Termin**, Kalender-/Sammlungs­wahl.
- **Wiederholungen**: nie/täglich/wöchentlich/monatlich/jährlich/**benutzerdefiniert** (RRULE), „Every“-Intervall, „On“-Regel, Ende (nie/Datum/nach n Vorkommen), **Ausnahmen (Exdate)**.
- **Teilnehmer** aus Kontakten oder manuell (Name/E-Mail), Status, **RSVP anfordern**.
- **Erinnerungen** (Reminders mit Zeiteinheit), **Priorität 1–9**, **Fortschritt %** (Tasks), **Tags/Kategorien**, **Dateianhänge**.
- Auch **Journal-Einträge (VJOURNAL)** und **Unteraufgaben** im Editor.
- **Undo/Redo** für Änderungen (Signale der App-Klasse).
- **ICS-Import**: Dateien/URLs als Argument, Doppelklick auf `.ics` (`MimeType=text/calendar`), Import-Bestätigung.

## Kalender und Quellen

- Datenhaltung über **Akonadi**: lokale Kalender + Online-Kalender (**Nextcloud, Google Calendar, Outlook, CalDAV u. v. m.**) über Ressourcen aus `kdepim-runtime`; Kontenpflege teils über `SystemAccountsForm`/Akonadi-Einstellungen.
- **Feiertage nach Region** (KF6::Holidays; `showHolidaysInCalendarViews`, `holidayRegions`), Feiertagszeile in Wochenansicht.
- Aufgaben (VTodos) einblendbar in allen Kalenderansichten, inkl. Unteraufgaben.
- **Verfügbarkeits-Veröffentlichung (Free/Busy)**: automatische Veröffentlichung mit einstellbarem Mindestabstand (Minuten) konfigurierbar (`FreeBusySettingsPage`) – Basis, damit Andere bei Einladungen die Belegung sehen.
- **Orts-Karten** optional (QtLocation; `enableMaps`, Marker-Typ Kreis/Pin) für Veranstaltungsorte.
- **Mail-Integration** als optionale Brücke zur Mail-Komponente der Suite (`enableMailIntegration`).

## Konfiguration und Integration

- KConfig-Datei **`kalendarrc`** mit feinen Ansichtsoptionen (Rastermodi, Kopfzeilen, Wochennummern, Randbreiten, Dimmung vergangener Termine, zuletzt geöffnete Ansicht …).
- **D-Bus**: `showIncidenceByUid` zum gezielten Öffnen eines Termins (Details in [api.md](api.md)); Single-Instance.
- Konvergente UI: identische App auf Desktop und **Plasma Mobile** (Kirigami, `Kirigami.Settings.isMobile`-Weichen).
- Vollständige Übersetzungen (AppData für Dutzende Sprachen).

## Was Kalendar/Merkuro NICHT bietet

- **Kein Server, keine Weboberfläche** – reine Desktop-/Mobile-App; öffentliche Freigaben, Einbettung oder Buchungsfremde gibt es nur über den jeweiligen Kalender-Server (z. B. Nextcloud Calendar).
- **Keine Webhooks/REST-API** und kein SDK für Drittanbieter; Automatisierung nur über D-Bus, CLI-Argumente und Akonadi-Bibliotheken.
- **Keine Terminbuchungsseiten / keine Terminumfragen** (Doodle-artige Vorschläge existieren nicht; auch kein Slot-Finder für gemeinsame Verfügbarkeit – eine „gemeinsame freie Zeit finden“-Funktion wurde in 26.08.2 nicht gefunden).
- **Keine eigenen Push-Benachrichtigungen über lokale Erinnerungen hinaus** – Erinnerungen laufen über Akonadi/KDE-Benachrichtigungen; browserbasierte Alarme wie beim Webkalender entfallen.
- **Keine Kalender-Serversynchronisation zu Dritt-Servern über CalDAV hinaus** (keine Exchange-MAPI/Google-API-Spezialfunktionen wie Kalender-Delegation oder Ressourcenbuchung; diese hängen an den kdepim-runtime-Ressourcen, nicht an Merkuro).
- **Keine Team-Funktionen** (Kommentare an Terminen, Freigabe-Abstufungen etc. sind nicht in der App; was der Server bietet, zeigt Merkuro nur soweit Akonadi es abbildet – **nicht verifiziert**, in 26.08.2 keine entsprechenden UI-Elemente gefunden).
