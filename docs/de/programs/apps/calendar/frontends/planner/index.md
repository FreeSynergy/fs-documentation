# GNOME Planner Dokumentation

## Übersicht

Planner ist der Projektplaner unter GNOME (App-ID `app.drey.Planner`): Vorgänge mit Anfang/Ende, Aufwand, Kosten und Abhängigkeiten (FS/SS/FF/SF mit Lag), Ressourcen mit eigenen Arbeitskalendern, kritischer Pfad und Slacks — dargestellt in vier Ansichten (Gantt, Aufgaben, Ressourcen, Ressourcennutzung). Projekte bleiben XML-Dateien (`*.planner`, DTD `mrproject-0.6`); optional speichert ein experimentelles Plugin in PostgreSQL. Import: MS Project XML und Evolution-/LDAP-Kontakte; Export: HTML und Druck/PDF. Stand: **0.14.92 (Dezember 2023)** — nach langem Stillstand wieder gepflegt (Übersetzungen bis 2026; in Debian stable und Arch extra), aber als Beta gekennzeichnet. In dieser Kalender-Serie führt ihn die Arbeitskalender-/Zeitachsenlogik, nicht ein Termin-Kalender.

## Dateistruktur

- [description.md](latest/description.md) - Was Planner macht, Vorteile, Abgrenzung zu MS Project, GanttProject, OpenProject, Nextcloud
- [features.md](latest/features.md) - Verifizierte Funktionen (0.14.92) und was Planner NICHT bietet
- [structure.md](latest/layout.md) - Fensteraufbau, Programm-/Modulstruktur (src, libplanner, Plugins), Konfiguration, Deployment
- [menu.md](latest/menus.md) - Menü-, Leisten- und Kontextmenüs aus den GtkBuilder-Dateien
- [shortcuts.md](latest/shortcuts.md) - Kurzbefehle aus dem Quelltext (u. a. Öffnen = F3!)
- [api.md](latest/api.md) - Kein REST: Dateiformat `*.planner`, DTD, Einheiten, SQL-Ablage, Import/Export-Wege

## Quellen

Alle Aussagen dieser Sektion stammen aus dem offiziellen Quelltext des aktuellen Releases und den offiziellen Projektseiten:

| Quelle | Fundstelle / URL | Wofür benutzt |
|--------|------------------|----------------|
| Quelltext-Release **0.14.92** (16.12.2023) | `https://download.gnome.org/sources/planner/0.14/planner-0.14.92.tar.xz` (lokal ausgepackt gelesen) | alle Dateien |
| GitLab-Repositorium (aktiv, letzte Commits April 2026) | `https://gitlab.gnome.org/World/planner` + API `…/api/v4/projects/World%2Fplanner/repository/commits` | Pflege-/Nutzungsstatus |
| Release-Downloadverzeichnis | `https://download.gnome.org/sources/planner/0.14/` (LATEST-IS-0.14.92; NEWS zu 0.14.91/0.14.92) | Versionsstand, Changes |
| `NEWS`, `README`, `planner.doap` im Tarball | Maintainer (Mart Raudsepp), GPL v2+, Homepage, Abhängigkeiten | api.md, description.md |
| `src/planner-window.c` (Zeilen 209–300) | Action-Tabelle: Menüs + Acceleras (Ctrl+N, F3, Ctrl+R, F1 …), registrierte Ansichten (Zeilen 664–667) | menu.md, shortcuts.md, structure.md |
| `src/planner-task-view.c`, `planner-resource-view.c`, `planner-gantt-view.c`, `planner-usage-view.c` | ansichtsspezifische Aktionen und Kurzbefehle (Ctrl+I/D/A, Ctrl+Shift+E/I/U, Zoom) | shortcuts.md, features.md |
| `data/ui/main-window.ui`, `task-view.ui`, `resource-view.ui`, `gantt-view.ui`, `sql-plugin.ui`, `eds-plugin.ui` | echte Menüstruktur inkl. Import-/Export-Untermenüs und Platzhalter | menu.md |
| `src/planner-task-popup.c`, `data/ui/resource-view.ui` (popup) | Kontextmenüs | menu.md |
| `data/dtd/mrproject-0.6.dtd`, `examples/sample-1.planner`, `tests/files/*.planner` | exaktes Dateiformat, Elemente/Attribute, Beispiel | api.md |
| `data/mime/app.drey.Planner.xml.in`, `data/app.drey.Planner.desktop.in`, `data/app.drey.Planner.gschema.xml` | MIME `application/x-planner`, Endungen `*.planner`/`*.mrproject`, GSettings-Schema mit Ansichten/Spalten | api.md, structure.md |
| `libplanner/mrp-time.h`, `mrp-task.h`, `mrp-types.h`, `mrp-resource.h`, `mrp-project.h` | Zeiteinheiten (64-Bit-Sekunden), Early/Late, kritischer Pfad, Constraint-Typen (ALAP/FNLT unimplementiert), Material-Ressourcen, Kosten | api.md, features.md |
| `meson.build`, `meson_options.txt`, `src/meson.build` | Abhängigkeiten (GTK ≥ 3.22, libgda/EDS optional), In-Tree-Plugins als shared modules, EDS-Backend nicht gebaut | structure.md, features.md |
| `docs/user-guide/C/planner.xml` (User Guide V0.14) | vier Ansichten, Mehrfach-Projekte, SQL-Konfiguration (PostgreSQL), MSP-XML-Grenzen, HTML-Inhalt, Druck-Dialog, Prioritäts-Scheduling | features.md, description.md, structure.md |
| Debian-Paket | `https://packages.debian.org/search?keywords=planner` (trixie: planner 0.14.92-1.1; planner-dev nur bis bullseye) | Nutzungsstatus, libplanner jetzt privat |
| Arch-Paket | `https://archlinux.org/packages/extra/x86_64/planner/` (0.14.92-4, 30.04.2025) | Nutzungsstatus |
| GNOME-Wiki (retro, aber offiziell) | `https://wiki.gnome.org/Apps/Planner` | Kurzbeschreibung, Windows-Builds |
| Flathub-Suche `app.drey.Planner` | kein Treffer (Stand der Recherche) | „kein Flatpak“ |

**Korrekturen gegenüber der alten Fassung dieser Sektion** (auf Basis des 0.14.92-Quelltexts): Die PERT-/Abhängigkeitsnetz-Ansicht existiert nicht mehr (heute vier Ansichten inkl. Ressourcennutzung); die Endung `.ppx` und der „LibMSP“-`.mpp`-Import kommen im Release nicht mehr vor (nur MS-Project-XML); libplanner ist seit 0.14.91 eine private Bibliothek ohne Fremd-Plugin-Support; „kein Kostenmodul“ ist falsch (Ressourcen-Kostensätze, Kosten-/Slack-Spalten); die Kurzbefehle Öffnen=F3 und Wiederholen=Ctrl+R wurden korrigiert; das Projekt ist nicht eingestellt, sondern wieder gepflegt.
