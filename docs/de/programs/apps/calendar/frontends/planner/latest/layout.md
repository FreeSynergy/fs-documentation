# GNOME Planner - Struktur und UI/UX

Basis: Quelltext-Release **0.14.92**.

## Fensterstruktur

```
┌────────────────────────────────────────────────────────────────────┐
│ Datei Bearbeiten Ansicht Aktionen Projekt Hilfe                    │
│ [🆕][📂][💾] [🖨][🔍] [↩][↪] │ [ansichtstypische Symbole]          │
├────┬──────────────────────────┬────────────────────────────────────┤
│ A  │ Aufgabenbaum             │ Gantt-Canvas                       │
│ n  │ # Name     Start Ende    │  W27   W28   W29   W30            │
│ s  │ ├─ Konzept 01.06         │  ▐█░░░░░░░                        │
│ i  │ │ └─ Review 10.06        │  ▐███░░░░░  ← kritischer Pfad rot │
│ c  │ └─ Umsetzung 20.06       │      ◆      (Meilenstein)         │
│ h  │   [Dauer] [%] [Kosten]   │   Abhängigkeitspfeile ziehbar     │
│ t  │                          │                                    │
│ e  │                          │                                    │
│ n  │                          │                                    │
│ ▸4 │                          │                                    │
│ ⌄  │                          │                                    │
├────┴──────────────────────────┴────────────────────────────────────┤
│ Statusleiste (Kontextinfos zu Menüpunkten/Aktionen)                │
└────────────────────────────────────────────────────────────────────┘
```

- Die linke Leiste (`src/planner-sidebar.c`) enthält die vier Ansichts-Symbole: **Gantt** (Standardansicht beim Start), **Aufgaben**, **Ressourcen**, **Ressourcennutzung** (`planner-window.c` Zeilen 664–667 registriert genau diese vier Views).
- Jede Ansicht kombiniert links eine GtkTreeView-Tabelle mit rechts einem Canvas (Gantt-Balken bzw. Auslastungsdiagramm der Usage-Ansicht).
- Ein Projekt = ein Fenster; mehrere Projekte = mehrere Fenster (Strg+N).

## Programmablauf (Request-Flow)

1. **Start:** `planner [Datei …]` → `PlannerApplication` (GtkApplication, App-ID `app.drey.Planner`, `src/planner-application.c`); übergebene Dateien/URIs öffnen je ein `PlannerWindow`.
2. **Öffnen:** Dateiauswahl (Filter `*.planner`, `*.mrproject`) → `MrpProject` lädt über Storage-Modul `libplanner/mrp-storage-mrproject.c` (Format mrproject v2, DTD); sehr alte Formate (≤ 0.11) zweigt `mrp-old-xml.c` um; alternativ SQL-Laden über libgda.
3. **Berechnen:** `MrpTaskManager` führt Vorwärts-/Rückwärtsterminierung aus (`mrp_task_get_latest_start/finish`), markiert kritischen Pfad, berechnet Slacks/Kosten; Änderungen triggern Neuscheduling.
4. **Bearbeiten:** UI-Aktionen laufen über den `PlannerCmdManager` (`planner-cmd-manager.c`) → Undo/Redo; Modelle (`planner-list-model.c`, `planner-gantt-model.c`, `planner-usage-model.c`) spiegeln `Mrp*`-Objekte in GtkTreeModels.
5. **Speichern:** Storage-Modul schreibt XML atomar zurück; bei SQL-Ablage `Save to Database`.
6. **Ausgabe:** Drucken über `planner-print-job.c` (eine Seite je angewählter Ansicht, PDF über GTK-Dialog); HTML über `planner-html-plugin.c` + libxslt-Stylesheets.

## Verzeichnis-/Modulstruktur (Tarball)

| Verzeichnis | Inhalt |
|-------------|--------|
| `src/` | GTK-UI: Fenster, die vier Views, Dialoge, Canvas-Zeichnung (`planner-gantt-*.c`), Plugins `planner-{html,msp,sql,eds,test}-plugin.c`, vendiertes `libgnomecanvas/` für den Canvas |
| `libplanner/` | Planungs-Engine `Mrp*` (Projekt, Task, Relation, Resource, Assignment, Calendar, Property, Zeit `mrp-time.c`), Storage-Module (`mrp-storage-mrproject.c`, `mrp-storage-sql.c`, `mrp-storage-module-xml.c`), Pfad-/XDG-Helfer |
| `data/` | `ui/` (GtkBuilder-Dateien inkl. aller Menüs), `dtd/mrproject-0.6.dtd`, `sql/` (PostgreSQL-Schema + Migrationen), `stylesheets/` (HTML-Export, `msp2planner.xsl`), `mime/`, `images/`, Desktop-/GSettings-Dateien |
| `docs/` | Benutzerhandbuch (DocBook, C/es/eu), private libplanner-API-Doku (gtk-doc-Option) |
| `examples/` | Beispieldateien `kitchen.planner`, `sample-1.planner` |
| `po/` | Übersetzungen (50+ Sprachen, auch Deutsch) |
| `tests/` | C-Tests, `files/*.planner`, Alt-Python-Test |
| `installer/` | NSIS-Skript für Windows-Builds |
| `eds-backend/` | altes Experiment eines EDS-Kalender-Backends – **wird nicht mehr gebaut** (im Meson auskommentiert) |

## Konfiguration

- **GSettings (dconf):** Schema `app.drey.Planner` (`data/app.drey.Planner.gschema.xml`): Fenstergeometrie, letzte Ansicht, letzter Ordner; Kind-Schemas je Ansicht mit Spalten (`order`/`visible`/`width` für Name, Start, Ende, Dauer, Arbeit, Kosten, Slack, WBS, Zugewiesen, Fertig) und Gantt-Optionen (kritischer Pfad hervorheben, Hilfslinien, Nichtstandardtage, Drucken erlaubt); Plugin-Schemas (msp, sql-Verbindungen).
- **Migration:** beim ersten Start unter GTK3 werden alte GConf2-Einstellungen einmalig übernommen (Mapping `data/planner.convert`); Druckeinstellungen liegen in `~/.config/planner-print-config`.
- **Umgebungsvariablen:** `PLANNER_DATADIR`, `PLANNER_PLUGINDIR` überschreiben Daten-/Pluginpfade (`libplanner/mrp-paths-gnome.c`).
- **Bauoptionen** (`meson_options.txt`): `database-gda` (PostgreSQL-Plugin), `eds` (EDS-Import), `simple-priority-scheduling` (experimentell), `gtk_doc`, `examples`.

## Datenmodell (Klassen / Format)

- `MrpProject` → Aufgabenbaum (`MrpTask` mit Eltern/Kindern, Wurzel = Projekt), `MrpRelation` (FS/FF/SS/SF + Lag), `MrpAssignment` (Ressource↔Task, units %), `MrpResource` (Arbeit/Material, Kosten, Kalender), `MrpGroup`, `MrpCalendar`/`MrpDay` (Wochen-/Tagesintervalle), `MrpProperty` (Custom-Felder), Phasen.
- Zeiten: `mrptime` = int64 Sekunden seit Epoche (Y2038-fest), Dauer/Aufwand in Sekunden; Datum im XML als `YYYYMMDDTHHMMSSZ`.
- Persistierung: XML `*.planner` (DTD mrproject-0.6) **oder** PostgreSQL-Schema (`data/sql/database.sql`: Tabellen für tasks, resources, relations, calendars …, Migrationen für 0.6→0.11→0.13).

## Plugin-Architektur

Plugins sind geteilte Module (`.so`) im Installations-Plugindir, die `planner-plugin-loader.c` zur Laufzeit lädt (`mrp_paths_get_plugin_dir`); sie melden Aktionen in die Menü-Platzhalter `/MenuBar/File/Import placeholder` und `/MenuBar/File/Export placeholder`. Out-of-Tree-Plugin-Support existiert seit 0.14.91 nicht mehr (libplanner privat) — erweiterbar ist de facto nur noch durch Patches im Quelltext.

## Deployments

- **Bauen:** `meson build && ninja -C build install`; Abhängigkeiten GLib ≥ 2.56, GTK ≥ 3.22, libxml2, libxslt; optional libgda 5 und evolution-data-server ≥ 3.6.
- **Distributionen:** Debian (`planner`, `planner-data`, `planner-doc`; trixie: 0.14.92-1.1), Arch (`planner` 0.14.92-4 in extra), weitere Packaging-Repos (Fedora/openSUSE ebenfalls mit 0.14.9x). Ein `planner-dev`-Paket gibt es seit bookworm nicht mehr (privates libplanner).
- **Windows:** NSIS-Installer im Quelltext (`installer/`), vorgebaute Builds über die Download-Seite des Projekt-Wikis.
- **Flatpak:** nicht vorhanden (kein Eintrag auf Flathub, Stand der Recherche).
- **Desktop-Integration:** `.desktop` mit Kategorien `Office;ProjectManagement;`, Icon `gnome-planner`, MIME `application/x-planner`.

## UI/UX und Accessibility

- Klassisches GTK3-Desktop-Layout, nicht responsive; auf kleinen Bildschirmen horizontal scrollen.
- Standardschrift/-thema des Desktops; keine eigenen Themes. Dialoge sind modale GtkDialoge mit Reitern (Aufgabe: Allgemein/Ressourcen/Vorgänger/Notizen; Ressource: Allgemein/Kalender/Notizen; Projekt: Allgemein/Custom).
- Gantt-Balken: Ziehen verschiebt, Ziehen eines Pfeils von Balken zu Balken erzeugt FS-Abhängigkeit; Maßstabs-/Zoomleiste; kantenbegradigte Darstellung seit 0.14.91.
- Accessibility: Tabellen/Dialoge folgen GTK-Standard; der Gantt-/Usage-Canvas ist reine Zeichnung und **nicht** screenreader-erschlossen.

## Performance

- Engine rechnet inkrementell (Änderung → Re-Scheduling betroffener Task-Zweige); auch mehrere hundert Vorgänge bleiben interaktiv.
- Der Gantt-Canvas zeichnet pro Zeile eigene Reihen-Objekte (`planner-gantt-row.c`); bei sehr vielen Ressourcen wird die Usage-Ansicht träge — konkrete Grenzen sind nicht offiziell dokumentiert (nicht verifiziert).
