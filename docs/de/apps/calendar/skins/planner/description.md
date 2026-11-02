# GNOME Planner - Beschreibung

**Versionsstand: 0.14.92 (16.12.2023)** — nach langem Stillstand seit Mitte der 2010er wieder aktiv gepflegt (Releases 0.14.91/0.14.92, Übersetzungen bis 2026, in Debian stable und Arch extra verpackt).

## Was das Programm macht

Planner ist der klassische Projektplaner unter GNOME: Projekte werden nach Netzplan-/CPM-Logik aufgebaut — Vorgänge (Tasks) mit Anfang/Ende, Aufwand, Fortschritt, Priorität und Abhängigkeiten (FS/SS/FF/SF inkl. Verzögerung), Ressourcen mit Arbeitskalendern und Zuordnungen, dazu Meilensteine, Phasen, Projekt-/Ressourcengruppen und benutzerdefinierte Felder. Die Engine berechnet Vorwärts-/Rückwärtstermine (früheste/späteste Zeitpunkte), Slacks und den kritischen Pfad. Geplant wird in vier Ansichten (Gantt-Diagramm, Aufgaben, Ressourcen, Ressourcennutzung); Ergebnisse lassen sich drucken (auch PDF) oder als HTML exportieren. Projekte bleiben einfache XML-Dateien (`*.planner`); optional speichert ein Plugin sie in PostgreSQL.

## Vorteile

- **Frei und lokal:** GPL v2+, keine Cloud, keine Konten; `.planner` bleibt lesbare XML-Datei mit DTD im Quelltext
- **Echte Planungslogik:** vier Abhängigkeitstypen mit Lag, Early/Late-Termine, Slacks, kritischer Pfad, Fixdauer-/Fixaufwand-Modi, Constraints (SNET/MSO)
- **Arbeitskalender als Erstklass-Objekt:** Basis-/Ressourcenkalender mit Arbeitstagen, Tageszeitintervallen und Feiertagen — Kalenderwochen „von Hand“, ohne Zwang zu externen Kalenderdiensten
- **Kostenansatz eingebaut:** Kostensätze je Ressource, taskweise Kosten- und Slacks-Spalten
- **Zwei Ablageorte:** Einzeldatei *oder* PostgreSQL-Datenbank (experimentell) — gut für Versionierung und Skripting
- **GTK3/Meson wieder taufrisch:** seit 0.14.91 Port auf GTK 3.22, GSettings, Meson; Y2038-feste Zeitbehandlung
- **Weiterverbreitet:** in allen großen Distributionen paketiert; Windows-Builds über das Projekt-Wiki

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **MS Project** (und **ProjectLibre** als Klon) | kommerziell bzw. Java, importiert natives `.mpp`, mit Budget-/Berichtswesen und Projektserver; Planner importiert nur MS-Project-**XML** und verzichtet bewusst auf Kostenrechnung und Server |
| **GanttProject** | Java, ähnlich; dafür PMML-/PDF-/MS-Project-Export und aktive Weiterentwicklung; Planner ist GTK-nativer und kann in SQL-Datenbanken sparen, GanttProject kann PERT-ähnliche Ansichten |
| **OpenProject / Planka / Taiga / Wekan** (Serie: Projektmanagement) | webbasierte Aufgaben-/Ticket-Systeme mit Mehrbenutzern; Planner ist Einzelplatz-Desktop ohne Ticketlogik, agile Boards oder Webzugriff |
| **Nextcloud Calendar/Tasks, ownCloud Tasks** | CalDAV-/ICS-basierte Termin-/Aufgabenserver mit Geräte-Sync; Planner kann weder ICS lesen/schreiben noch CalDAV — es plant Zeitachsen und Vorgangsnetze, keine Termine |
| **GNOME Merkuro / Thunderbird** (Serie: Kalender) | Terminkalender mit Wiederholungen/Einladungen; Planner hat kein Terminmodell, keine Erinnerungen |
| **Todoist & Co.** | persönliche To-do-Listen mit Synchronisation; Planner plant Vorgangsnetze mit Abhängigkeiten und Ressourcen, ohne Sync |

## Technische Details

- **Sprache/Toolkit:** C, GObject; GTK ≥ 3.22, GLib ≥ 2.56; UI teils noch GtkUIManager (GtkBuilder-Dateien unter `data/ui/`)
- **Planungs-Engine:** libplanner (`Mrp*`-Klassen), seit 0.14.91 **privat** (nicht installiert, keine stabile ABI)
- **Datenhaltung:** Einzeldatei `*.planner` (XML, DTD `mrproject-0.6`); optional PostgreSQL über libgda-Plugin (experimentell)
- **Weitere Bibliotheken:** libxml2, libxslt (HTML-Export, MSP-XML-Import); optional evolution-data-server (Ressourcen-Import, standardmäßig aus)
- **Plattformen:** Linux (in allen großen Distributionen), Windows-Installer im Quelltext (`installer/`, NSIS) und über das Projekt-Wiki; kein Mac-Build im Projekt
- **Lizenz:** GPL v2 oder neuer
- **Reifegrad:** 0.14.9x sind als „source code only beta“ gekennzeichnet; Experimente (SQL, EDS, Prioritäts-Scheduling) nur per Meson-Schalter

## Für wen geeignet

- Vereins-, Bau-, Handwerks- und Migrationsprojekte mit klassischer (Wasserfall-)Planung und CPM-Denken
- MS-Project-Altbestände, die als XML vorliegen und nur weitergepflegt/betrachtet/gedruckt werden sollen
- Alle, die Projektstände als versionierbare XML-Datei (Git-tauglich) oder in einer eigenen Datenbank ablegen wollen
- **Weniger geeignet** für Team-Terminplanung, agile Boards oder mobile Erfassung — dafür sind die Kalender-/PM-Vertreter der Serie die bessere Wahl
