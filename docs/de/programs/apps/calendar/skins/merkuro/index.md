# Merkuro Calendar

> **Umbenennung:** Das 2021 als **Kalendar** gestartete KDE-Kalenderprogramm heißt seit **KDE Gear 23.08 (August 2023) Merkuro**; Repos, Binaries und AppStream-ID folgen dem neuen Namen (`pim/merkuro`, `merkuro-calendar`, `org.kde.merkuro.calendar`). Diese Sektion dokumentiert den aktuellen Stand des Nachfolgers.

Merkuro Calendar ist der **moderne Kalender-Client der KDE-Desktop-Umgebung** (Qt 6/QML/Kirigami, konvergent auf Desktop und Plasma Mobile). Termine, Aufgaben (VTodo) und Journale werden nicht von der App selbst gespeichert, sondern über den KDE-PIM-Dienst **Akonadi** verwaltet, der lokale und Online-Kalender (Nextcloud, Google, Outlook, CalDAV … via `kdepim-runtime`) synchronisiert. Seit 2025/26 ist Merkuro eine kleine Suite: Kalender, Kontakte, Mail und Launcher.

- **Kategorie:** calendar (nativer Groupware-Client)
- **Lizenz:** GPL-3.0-or-later
- **Aktuell dokumentierte Version:** **26.08.2** (KDE Release Service, Tag 2026‑10‑08); Projektaktivität unverändert hoch (letzter Aktivitäts-Eintrag 2026‑11‑02)
- **Entwicklungsstatus:** aktiv; Maintainer Carl Schwan und Clau Cambra (KDE PIM)

## Dateistruktur dieser Sektion

| Datei | Inhalt |
|-------|--------|
| [description.md](description.md) | Was das Programm macht, Vorteile, Abgrenzung (u. a. zu Nextcloud Calendar, Davical, KOrganizer), technische Details, Für-wen-geeignet |
| [features.md](features.md) | Verifizierte Funktionsliste + „Was Merkuro NICHT bietet“ |
| [api.md](api.md) | D-Bus-Interface `org.kde.calendar.Calendar`, CLI/ICS-Import, Akonadi als Datenschicht, Konfiguration, Versionsstand |
| [menu.md](menu.md) | Menüstruktur (Datei/Bearifen/Ansicht/Einstellungen, Mobile-Toolbar) aus dem QML-Quelltext |
| [shortcuts.md](shortcuts.md) | Verifizierte Tastenkürzel der QML-Oberfläche |
| [structure.md](structure.md) | Modul-/Verzeichnisstruktur, Request-Ablauf (Akonadi-Modelle), Konfiguration, Deployment |

## Quellen

Stand aller Aussagen: Quelltext-Tarball und offizielle Seiten, Prüfdatum 2026‑11‑02, Versionsstand **26.08.2**, sofern nicht anders angegeben.

1. **Offizielles Release-Archiv (Primärquelle):** `https://download.kde.org/stable/release-service/26.08.2/src/merkuro-26.08.2.tar.xz` – lokal ausgelesen: `CMakeLists.txt` (Version 26.08.2, Qt ≥ 6.9, KF ≥ 6.25), `README.md`, `src/calendar/*` (inkl. `main.cpp`, `calendarapplication.{h,cpp}`, `calendarconfig.kcfg`, `org.kde.calendar.Calendar.xml`, Desktop-/Metainfo-Dateien, QML unter `src/calendar/qml/`), `src/components/*`, `src/{launcher,contacts,mail}`.
2. **GitLab-Invent-API** (Projekt- und Tagliste): `https://invent.kde.org/api/v4/projects/pim%2Fmerkuro` und `…/repository/tags` – neuster Tag `v26.08.2` (2026‑10‑08), letzter Commit auf Tag-Commit 2026‑10‑06; Projekt `pim/kalendar` antwortet als Redirect auf `pim/merkuro` (Projekt-ID 7106, `last_activity_at` 2026‑11‑02) – belegt die Umbenennung direkt am Repo.
3. **Offizielle Produktseiten:** `https://apps.kde.org/merkuro.calendar/` (Merkuro Calendar) und `https://apps.kde.org/en-gb/merkuro/`; README-Zitat „Merkuro was formerly known as Kalendar.“
4. **GitHub-Mirror:** `https://github.com/KDE/merkuro` (aktiv); der Mirror `https://github.com/KDE/kalendar` endet bei `v23.04.3` – nützlich als Untergrenze der Umbenennung.
5. **Umbenennungs-Bekanntwerden (Sekundärquellen, zur Datierung):** KDE-Gear-23.08-Veröffentlichungen („Kalendar Becomes Merkuro“, August 2023; linuxiac.com, phoronix.com).

Wiederholungs-Rezept: Tarball gemäß Quelle 1 holen; Versionsnummer in `CMakeLists.txt`, D-Bus-Interface in `src/calendar/org.kde.calendar.Calendar.xml`, Einstellungen in `src/calendar/calendarconfig.kcfg`, Kürzel in `src/calendar/calendarapplication.cpp`/`src/components/abstractmerkuroapplication.cpp` mit dieser Doku abgleichen.
