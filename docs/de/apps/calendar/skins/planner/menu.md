# GNOME Planner - Menüpunkte

Quelle: `data/ui/main-window.ui` plus die Action-Tabellen in `src/planner-window.c`, `planner-task-view.c`, `planner-resource-view.c`, `planner-gantt-view.c`, `planner-usage-view.c` und den Plugin-`.ui`-Dateien (Release 0.14.92). Deutsche Bezeichnungen = offizielle Übersetzung (`po/de`), in Klammern der englische Original-Label.

## Fensteraufbau

Menüleiste oben, darunter die Werkzeugleiste, links die **Ansichten-Leiste mit den vier Ansichts-Symbolen** (User Guide), rechts der Arbeitsbereich; unten Statusleiste. Die Ansichten (Gantt, Aufgaben, Ressourcen, Ressourcennutzung) werden über die linke Leiste oder das Menü **Ansicht** gewechselt; Menü- und Leisteninhalte von **Bearbeiten**, **Ansicht** und **Aktionen** ändern sich mit der aktiven Ansicht.

## Hauptmenüs

| Menü | Einträge |
|------|----------|
| **Datei** (File) | Neues Projekt (Strg+N) · Öffnen … (**F3**) · Zuletzt geöffnet · **Importieren ▶** · ─ · Speichern (Strg+S) · Speichern unter … (Strg+⇧+S) · **Exportieren ▶** · ─ · Seite einrichten … · Drucken … (Strg+P) · Druckvorschau (Strg+⇧+P) · ─ · Schließen (Strg+W) · Beenden (Strg+Q) |
| **Bearbeiten** (Edit) | Rückgängig (Strg+Z) · Wiederholen (**Strg+R**) · ─ · Alles auswählen (Strg+A) |
| **Ansicht** (View) | Radio: Gantt-Diagramm · Aufgaben · Ressourcen · Ressourcennutzung · ─ · ansichtsspezifische Punkte (siehe unten) |
| **Aktionen** (Actions) | vollständig ansichtsabhängig (siehe unten) |
| **Projekt** (Project) | Kalender verwalten … (Manage Calendars) · Tagestypen bearbeiten … (Edit Day Types) · ─ · Projektphasen bearbeiten … (Edit Project Phases) · ─ · Projekteigenschaften bearbeiten … (Edit Project Properties) |
| **Hilfe** (Help) | Benutzerhandbuch (F1) · Info (About) |

Einträge mit „ … “ öffnen Dialoge; Punkte ohne Accelerator-Angabe haben keinen Kurzbefehl.

## Importieren- und Exportieren-Untermenüs (Plugin-abhängig)

| Ort | Eintrag | Plugin |
|-----|---------|--------|
| Datei → Importieren | MS Project XML … | msp (immer gebaut) |
| Datei → Importieren | EDS (Evolution/LDAP-Ressourcen) | eds (experimentell, Standardbau aus) |
| Datei → Importieren | Open from Database … | sql (bei libgda-Gegenüber) |
| Datei → Exportieren | HTML … | html |
| Datei → Exportieren | Save to Database | sql |

Hinweis: Das im Benutzerhandbuch noch erwähnte „Export → Planner-0.11-Format“ wurde in 0.14.92 entfernt (NEWS #248); der Menüpunkt existiert nicht mehr. Ebenso gibt es kein Menü „Einstellungen“ mehr (der Präferenzen-Eintrag ist im Quelltext auskommentiert; Ansichts-Feineinstellungen liegen in GSettings).

## Aktionen-Menü je Ansicht

**Aufgaben (Tasks)** — `task-view.ui`:
Aufgabe einfügen (Strg+I) · Aufgaben einfügen … (Insert Tasks…) · Aufgabe entfernen (Strg+D) · Aufgaben verknüpfen (Link Tasks) · Verknüpfung lösen (Unlink Task) · ─ · Aufgabe einrücken (Strg+⇧+I) · Aufgabe ausrücken (Strg+⇧+U) · ─ · Aufgabe nach oben / unten verschieben · ─ · Constraint zurücksetzen · ─ · Aufgabe bearbeiten (Strg+⇧+E) · ─ · Benutzerdefinierte Eigenschaften bearbeiten …

**Gantt (Gantt Chart)** — `gantt-view.ui`:
wie Aufgaben, jedoch ohne „Benutzerdefinierte Eigenschaften bearbeiten“.

**Ressourcen (Resources)** — `resource-view.ui`:
Ressource einfügen (Strg+I) · Ressourcen einfügen … · Ressource entfernen (Strg+D) · ─ · Ressourceneigenschaften bearbeiten … (Strg+⇧+E) · Gruppen bearbeiten … (Edit Groups) · Benutzerdefinierte Eigenschaften bearbeiten …

**Ressourcennutzung (Resource Usage)** — keine Einträge im Aktionen-Menü.

## Ansicht-Menü: zuschaltbare Punkte je Ansicht

| Ansicht | Punkte |
|---------|--------|
| Aufgaben | Sichtbare Spalten bearbeiten (Edit Visible Columns) · Kritische Vorgänge hervorheben (Highlight Critical Tasks) |
| Gantt | Zoom vergrößern/verkleinern/einpassen · Sichtbare Spalten bearbeiten · Kritische Vorgänge hervorheben · Hilfslinien anzeigen (Show Guide Lines) · Nichtstandardtage (Nonstandard Days) |
| Ressourcen | Sichtbare Spalten bearbeiten |
| Ressourcennutzung | Zoom vergrößern/verkleinern/einpassen · Sichtbare Spalten bearbeiten |

## Werkzeugleiste

Feste Punkte: Neues Projekt · Öffnen · Speichern · ─ · Drucken · Druckvorschau · ─ · Rückgängig · Wiederholen; danach die typischen Aktionen der aktiven Ansicht (z. B. Aufgabe einfügen/entfernen, verknüpfen/lösen, ein-/ausrücken, nach oben/unten, Zoom).

## Kontextmenüs (Rechtsklick)

**Aufgabenbaum/Gantt** (`src/planner-task-popup.c`):
Aufgabe einfügen · Teilaufgabe einfügen · Aufgabe entfernen · ─ · Verknüpfung lösen · ─ · Ressourcen zuweisen … · Aufgabe bearbeiten …

**Ressourcenliste** (`data/ui/resource-view.ui`, Popup):
Ressource einfügen · Ressource entfernen · Ressourceneigenschaften bearbeiten …

## Menüs nach Rolle

Planner ist Einzelplatz-Software ohne Benutzerkonten — **keine rollenabhängigen Menüs**.
