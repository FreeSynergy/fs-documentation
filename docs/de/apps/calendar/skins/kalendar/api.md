# Kalendar / Merkuro – API (Merkuro Calendar 26.08.2, Stand: 2026‑11‑02)

## Namensgebung zuerst (wichtig für diese Sektion)

Das unter dem Namen **Kalendar** begonnene KDE-Kalenderprogramm wurde **mit KDE Gear 23.08 (August 2023) in Merkuro umbenannt**, weil die App über Termine hinauswuchs (Kontakte, geplante E‑Mail-Integration). Repo und Releases laufen seither unter `pim/merkuro` (Invent) bzw. `KDE/merkuro` (GitHub); das GitHub-Mirror `KDE/kalendar` endet beim letzten Kalendar-Tag v23.04.3. Die Produktentwicklung lebt vollständig weiter: aktuellster Release ist **Merkuro 26.08.2** (KDE Release Service, Tag 2026‑10‑08), letzter Aktivitätscommit 2026‑11‑02. Diese Dokumentation beschreibt den Nachfolgezustand.

## Versionsstand und Entwicklung

| Eigenschaft | Wert |
|-------------|------|
| Aktuelle Version | **26.08.2** (`RELEASE_SERVICE_VERSION` in `CMakeLists.txt`), Release Service 26.08 vom Oktober 2026 |
| Versionsschema | YY.MM.x seit KDE Release Service (ehemals 22.12, 23.04 …) |
| Entwicklung | aktiv (Maintainer Carl Schwan, Clau Cambra; tägliche Commits; Bugs über bugs.kde.org, Produkt „merkuro“) |
| Lizenz | GPL‑3.0-or-later (`KAboutData … KAboutLicense::GPL_V3`) |
| Plattform | KDE/Qt: Qt ≥ 6.9, KDE Frameworks ≥ 6.25, KDE-PIM-Bibliotheken 6.8.2 (Akonadi, AkonadiCalendar, AkonadiContact, KCalCore …) |
| Programme der Suite | `merkuro-calendar`, `merkuro-contact`, `merkuro-mail`, `merkurolauncher` – diese Doku behandelt `merkuro-calendar` |

## Grundarchitektur für die API-Frage

Merkuro Calendar ist ein **reiner Desktop-Client ohne eigenen Netzwerk-Server und ohne eigene REST-/HTTP-API**. Termine und Aufgaben hält nicht die App, sondern der **Akonadi-PIM-Dienst** (eigene lokale Datenbank + Synchronisations-Ressourcen aus `kdepim-runtime`: CalDAV, Google, Exchange/WebDAV …). Jede „Integration“ läuft daher über eine dieser drei Ebenen:

1. D-Bus-Schnittstelle der laufenden App (unten),
2. Akonadi als Datenschicht (Agent-API/Ressourcen),
3. CLI-Argumente (ICS-Import).

## D-Bus-Schnittstelle der App (verifiziert an 26.08.2)

- **Single-Instance:** `KDBusService(KDBusService::Unique)` in `src/calendar/main.cpp`; der Bus-Name leitet sich vom Desktop-Dateinamen ab (`org.kde.merkuro.calendar`). Ein zweiter Start aktiviert die laufende Instanz und übergibt Argumente (`activateRequested`).
- **Registriertes Objekt:** `/Calendar` im Session-Bus (`QDBusConnection::sessionBus().registerObject(u"/Calendar", this)` in `calendarapplication.cpp`).
- **Interface `org.kde.calendar.Calendar`** (introspektierbar über `src/calendar/org.kde.calendar.Calendar.xml`):

| Methode | Signaturen | Zweck |
|---------|-----------|-------|
| `showIncidenceByUid` | `uid: s`, `occurrence: QDateTime` (Marshalling `((iii)(iiii)i)`), `xdgActivationToken: s` | Öffnet/anwendend den Termin einer iCal-**UID** (mit optionalem Wiederholungs-Instant); der Activation-Token folgt dem XDG-Activation-Standard für fokussierendes Öffnen |

Beispiel:

```bash
qdbus org.kde.merkuro.calendar /Calendar \
  org.kde.calendar.Calendar.showIncidenceByUid \
  "uid-1234@example" "$(date -u +%Y-%m-%dT%H:%M:%S)" ""
```

(Das exakte Marshalling des QDateTime-Arguments kann je nach qdbus-Version Anpassung erfordern – das Interface selbst ist Quelltext-verifiziert.)

## CLI / Datei-Assoziation

- Start: `merkuro-calendar [PFAD|URL …]`. Positionale Argumente werden im laufenden Betrieb an den **ICS-Importer** durchgereicht (`Importer::importCalendarFromFile` in `main.cpp`/`importer.cpp`); beim Erststart importiert derselbe Weg über `Importer`.
- Desktop-Datei: `Exec=merkuro-calendar %u`, `MimeType=text/calendar`, `SingleMainWindow=true`, Kategorie `Office;Calendar` – die App ist als Standard-Handler für `.ics` registrierbar (`xdg-mime default org.kde.merkuro.calendar.desktop text/calendar`).
- Standard-KDE-Optionen via `KAboutData` (`--help`, `--version`, Qt-/KF-Flags). Eigene Sonderflags existieren in 26.08.2 nicht.

## Datenschicht: Akonadi (die eigentliche Kalender-API)

- Merkuro liest/schreibt ausschließlich über **Akonadi**: `Akonadi::ETMCalendar` (App hält einen `ETMCalendar::Ptr`), Akonadi-Agenten, D-Bus-Dienst `org.freedesktop.Akonadi.*`.
- **Konsolensteuerung:** `akonadictl start|stop|restart|status` (Akonadi, nicht Merkuro). Nach Installation von `kdepim-runtime` empfiehlt die offizielle README ein `akonadictl restart`, damit Online-Ressourcen (CalDAV & Co.) erscheinen.
- **Programmatische Nutzung:** C++/Qt-Bibliotheken `Akonadi`, `AkonadiCalendar`, `AkonadiContact`, `KCalCore` (gleiche Schicht, mit der Merkuro selbst baut) – ein sprachunabhängiges öffentliches API der App existiert nicht.
- **Online-Kalender** (Nextcloud, Google, Outlook, CalDAV) werden von Ressourcen aus `kdepim-runtime` synchronisiert; deren Zugangsdaten/Protokolle sind deren API, nicht Merkuros.

## Konfiguration (Dateiebene)

- KConfig-Datei **`kalendarrc`** (`calendarconfig.kcfg`): Gruppen `General` (u. a. `showMenubar`, `enableMaps`, `enableMailIntegration`, `lastOpenedView`), `GeneralView` (Feiertage `showHolidaysInCalendarViews`, `holidayRegions`, Aufgaben ein/aus), `MonthView`/`WeekView`/`ScheduleView` (Darstellung, Wochennummern), `TaskView` (Sortierung DueTime/Alphabetically/Priority).
- Konten/Collections liegen nicht in Merkuro, sondern bei Akonadi (`~/.local/share/akonadi/`).

## Webhooks / Push

- **Nicht vorhanden und nicht vorgesehen.** Aktualisierungen kommen aus Akonadi-Ressourcen (Client-seitiges Polling/Sync der jeweiligen Online-Kalender); Merkuro bietet keine Endpunkte für Dritte.

## Limits

- App-seitig keine dokumentierten Rate-Limits; praktisch relevant sind die Limits der angebundenen Kalenderdienste (über kdepim-runtime-Ressourcen) und die Akonadi-Datenbank.

## Quellen (Fundstellen, alle 26.08.2)

- Offizielles Release-Archiv: `https://download.kde.org/stable/release-service/26.08.2/src/merkuro-26.08.2.tar.xz` (abgerufen 2026‑11‑02; lokal gelesen: `CMakeLists.txt`, `README.md`, `src/calendar/{main.cpp,calendarapplication.{h,cpp},calendarconfig.kcfg,org.kde.calendar.Calendar.xml,org.kde.merkuro.calendar.desktop,org.kde.merkuro.calendar.metainfo.xml}`, `src/{launcher,mail,contacts}/CMakeLists.txt`).
- GitLab-API Projekt-/Tagliste `pim/merkuro` (`https://invent.kde.org/api/v4/projects/pim%2Fmerkuro/repository/tags`): neuster Tag `v26.08.2` (2026‑10‑08); Projekt `pim/kalendar` leitet auf `pim/merkuro` (Projekt-ID 7106, `last_activity_at` 2026‑11‑02).
- Offizielle Produktseiten: `https://apps.kde.org/merkuro.calendar/` („Merkuro Calendar“; früher „Kalendar“), README-Zeile „Merkuro was formerly known as Kalendar.“ im Quelltext.
- Umbenennungs-Berichterstattung zur Release-Serie: KDE-Gear-23.08-Ankündigungen („Kalendar Becoming Merkuro“, Aug 2023; linuxiac/phoronix als Sekundärquellen).
