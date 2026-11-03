# GNOME Planner - Funktionen

Alle Funktionen verifiziert am Quelltext-Release **0.14.92** (Dateien in Klammern) und der mitgelieferten Benutzeranleitung (`docs/user-guide/C/planner.xml`, Stand V0.14).

## Aufgabenplanung (Task-Ansicht)

- Aufgaben hierarchisch verschachtelt; Meilensteine als Aufgabe mit Dauer 0; Summenaufgaben implizit aus Kindern (`mrp-storage-mrproject.c`, `task-dialog.ui`)
- Eigenschaften je Aufgabe: Name, Anfang/Ende, Aufwand (work), Dauer, Fortschritt (%), Priorität, Notizen, Typ Milestone, Modus „feste Dauer“ (`fixed-work`/`fixed-duration`) (`task-dialog.ui`, DTD)
- Abhängigkeiten FS/SS/FF/SF mit Verzögerung (lag), anlegbar im Dialog „Predecessors“ **oder** durch Ziehen eines Pfeils zwischen Balken im Gantt (dann stets FS) (`mrp-relation.h`, User Guide „Creating Dependencies with the Gantt Chart“)
- Constraints: ASAP (Standard), „start not earlier than“ (SNET), „must start on“ (MSO); Rückgängig über Aktionen → Constraint zurücksetzen. ALAP und „finish not later than“ sind deklariert, aber **nicht implementiert** (`mrp-types.h`)
- Berechnung: Vorwärts-/Rückwärtsterminierung (`mrp_task_get_latest_start/finish`), Slacks, kritischer Pfad (`mrp_task_get_critical`), in Gantt/Aufgaben hervorhebbar (`planner-gantt-*`, GSettings `highlight-critical-path`)
- Bilden/Ändern von Hierarchie per Ein-/Ausrücken, Verschieben mit/ohne Abhängigkeit, Mehrfachauswahl
- Experimentelles prioritätsgesteuertes Scheduling (Ressourcenabzug zugunsten einer Aufgabe mit Priorität 9999 und festem Start) — nur bei Bau mit Meson-Option `simple-priority-scheduling` (`meson_options.txt`, User Guide „Scheduling“)

## Ressourcen und Kosten

- Ressourcen vom Typ **Arbeit** oder **Material**, Kurzname, E-Mail, Gruppen, Zuweisungsgrad (units %), Notizen (`resource-dialog.ui`, `mrp-resource.h`)
- Kostensatz je Ressource; task- und projektweise Kostenberechnung; Kosten-Spalte in Aufgaben-/Gantt-Ansicht (`mrp-resource.c` „standard cost“, `mrp_task_get_cost`, Spalte `cost` in `planner-task-tree.c`)
- Zuweisungen (allocations) Aufgabe↔Ressource mit Prozent; Ansicht **Ressourcennutzung** mit Auslastungsdiagramm und Zoom (`planner-usage-view.c`, `planner-usage-chart.c`)
- Ressourcen-Import aus Evolution-Kontakten oder LDAP (EDS-Plugin, experimentell, standardmäßig deaktiviert) (`planner-eds-plugin.c`, `meson_options.txt`)

## Kalender

- Projekt-Basiskalender mit Standardwoche und Tages-**intervallen** (z. B. 08:00–12:00, 13:00–17:00) (`mrproject-0.6.dtd`, `planner-calendar-dialog.c`)
- Eigene Kalendertypen (day types) mit Beschreibung, übersteuerbare Wochentage, einzelne Abweichungen/Feiertage pro Datum (`calendar-dialog.ui`, `day-type-dialog.ui`, `working-time-dialog.ui`)
- Basiskalender-Hierarchie (Unterkalender erben) und **eigener Kalender je Ressource**; Aufgaben folgen dem Kalender der zugewiesenen Ressource (`mrp-calendar.c`, User Guide „Calendar Tab“)

## Projektverwaltung

- Projekteigenschaften: Name, Start, Organisation, Manager, Phase, Standardkalender; feste Projektphasen mit Phasenwechsel (`project-properties.ui`, `planner-phase-dialog.c`)
- **Benutzerdefinierte Eigenschaften** (custom properties) auf Projekt-, Aufgaben- und Ressourcenebene mit Typen date/duration/float/int/text/text-list/cost; erscheinen als Spalten (`mrp-property.c`, DTD, User Guide)
- Mehrere Projekte gleichzeitig offen, jedes im eigenen Fenster (`planner-window.c`, User Guide „Editing Multiple Projects“)
- Undo/Redo für die meisten Aktionen, aber ausdrücklich nicht für alle (User Guide „Caution“)

## Diagramme und Ausgabe

- Gantt-Diagramm mit Balken, Meilenstein-Rauten, Abhängigkeitspfeilen, Nichtstandardtagen, Hilfslinien, Zoom (`planner-gantt-chart.c`, Ansichtsoptionen)
- Drucken/PDF: GTK-Druckdialog; wählbare Ansichten per Häkchen (Gantt/Aufgaben/Ressourcen/Nutzung), Papier-/Layout-Tab, Druckvorschau (`planner-print-dialog.c`, `planner-print-job.c`)
- HTML-Export als Einzeldatei: Gantt-Bild, Aufgabenliste (% komplett, Start, Ende, Arbeit, Ressourcen), Ressourcentabelle; auch an Web-Adresse publishbar (`planner-html-plugin.c`, `data/stylesheets/html1_*.xsl`)

## Import, Export, Ablage

- Nativ: `*.planner` (auch `*.mrproject` lesbar), MIME `application/x-planner`, DTD-Version 2 (`data/mime/`, `mrp-storage-mrproject.c`)
- Altformate (Planner ≤ 0.11) werden beim Öffnen noch gelesen (`mrp-old-xml.c`); der Export ins 0.11-Format wurde in 0.14.92 entfernt (NEWS #248)
- Import: MS Project **XML** (MS Project 2002+; kein natives `.mpp`), ohne Kalender/Gruppen/custom Felder (`planner-msp-plugin.c`, `msp2planner.xsl`)
- Ablage optional in **PostgreSQL**: „Open from Database…“/„Save to Database…“, Datenbank bei Bedarf automatisch anlegen; Schema unter `data/sql/` (experimentell) (`planner-sql-plugin.c`, User Guide „Configuring a Planner database“)

## Was Planner NICHT bietet

- **Kein Kalender-Sync:** kein CalDAV, kein ICS-Import/-Export, keine Anbindung an Google/Outlook/Nextcloud-Kalender — die Kalender sind interne Arbeitszeitkalender
- **Keine PERT-/Netzwerkansicht** mehr: die früheren drei Ansichten (inkl. Abhängigkeitsnetz) gibt es so nicht; heute: Gantt, Aufgaben, Ressourcen, Ressourcennutzung (`planner-window.c` registriert genau diese vier)
- **Kein Import nativer `.mpp`-Dateien** nur MS-Project-XML
- **Keine Mehrbenutzer-Bearbeitung:** kein Sperr-/Kollisionsmanagement; die SQL-Ablage teilt Daten, öffnet Projekte aber weiterhin pro Arbeitsplatz
- **Keine Web-/Mobile-Version**, keine Online-Kollaboration, keine API für Live-Zugriffe
- **Keine agile Mode** (Kanban/Scrum/Burndown) und kein Ticketsystem
- **Kein Budget-/Auftragswesen:** nur Kostensätze und einfache Kostenaddition; keine Rechnungen, Deckungsbeiträge, Zahlungsverfolgung
- **Keine Erinnerungen/Benachrichtigungen** und kein Terminmodell
- **Keine erweiterbaren Fremd-Plugins:** libplanner ist seit 0.14.91 privat, Out-of-Tree-Plugin-Support entfallen; die mitgelieferten Plugins (html, msp, sql, eds) sind In-Tree-Module
- **Ressourcenkalender ohne Feiertags-Import** aus externen Diensten (Feiertage manuell als einzelne Tage pflegen)
- **Kein GTK4/Libadwaita:** weiterhin GTK3 (teils GtkUIManager); kein Flatpak-Paket

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| PostgreSQL | SQL-Plugin (libgda), Meson `database-gda`; Schema `data/sql/database.sql` |
| Evolution Data Server / LDAP | EDS-Plugin für Ressourcen-Import, Meson `eds` (Standard: aus) |
| MS Project | nur XML-Austausch über `msp2planner.xsl` |
| HTML-Websites | HTML-Export-Dialog (Datei oder URL) |
| Druck-PDF | GTK-Druckdialog „In Datei drucken“ |
| Skripte/Konverter | `.planner` ist XML; SQL-Schema als strukturierter Zweit Zugang |
