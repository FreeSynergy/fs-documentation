# GNOME Planner - Tastatur-Shortcuts

Alle Kurzbefehle sind der Action-Tabelle des Quelltext-Release **0.14.92** entnommen: `src/planner-window.c` (Zeilen 209–300) sowie `planner-task-view.c`, `planner-resource-view.c`, `planner-gantt-view.c`. Die Acceleratoren sind im GtkUIManager-Format (`<Control>`/`<Shift>`) fest im Programm kodiert; sie sind nicht in GSettings konfigurierbar.

> Stand: Planner 0.14.92 (GTK 3.22+, App-ID `app.drey.Planner`).

## Datei

| Shortcut | Funktion | Quelle |
|----------|----------|--------|
| `Strg+N` | Neues Projekt (öffnet weiteres Fenster) | `FileNew` |
| `F3` | Projekt öffnen … | `FileOpen` |
| `Strg+S` | Speichern | `FileSave` |
| `Strg+⇧+S` | Speichern unter … | `FileSaveAs` |
| `Strg+P` | Drucken … | `FilePrint` |
| `Strg+⇧+P` | Druckvorschau | `FilePrintPreview` |
| `Strg+W` | Projekt schließen | `FileClose` |
| `Strg+Q` | Beenden | `FileExit` |

**Achtung:** Öffnen hat **kein** Strg+O, sondern **F3** – ein typischer Reflexfehler in Planner.

## Bearbeiten

| Shortcut | Funktion | Quelle |
|----------|----------|--------|
| `Strg+Z` | Rückgängig | `EditUndo` |
| `Strg+R` | Wiederholen (**nicht** Strg+⇧+Z) | `EditRedo` |
| `Strg+A` | Alles auswählen (Aufgaben-/Ressourcenliste) | `SelectAll` je Ansicht |

## Aufgaben- und Ressourcen-Aktionen (Ansichten Aufgaben, Gantt, Ressourcen)

| Shortcut | Funktion | Quelle |
|----------|----------|--------|
| `Strg+I` | Aufgabe bzw. Ressource einfügen | `InsertTask` / `InsertResource` |
| `Strg+D` | Markierte Aufgabe(n)/Ressource entfernen | `RemoveTask` / `RemoveResource` |
| `Strg+⇧+E` | Aufgabe bearbeiten / Ressourceneigenschaften bearbeiten | `EditTask` / `EditResource` |
| `Strg+⇧+I` | Aufgabe einrücken (Unterstruktur bilden) | `IndentTask` |
| `Strg+⇧+U` | Aufgabe ausrücken | `UnindentTask` |

Für Verknüpfen/Verknüpfung lösen (Link/Unlink Tasks), Verschieben nach oben/unten, Constraint zurücksetzen, Meilensteine und die Abhängigkeitstypen gibt es **keine** Kurzbefehle — sie liegen im Menü **Aktionen** bzw. im Kontextmenü; Abhängigkeiten lassen sich im Gantt auch per Ziehen eines Pfeils zwischen Balken anlegen.

## Gantt-Ansicht

| Shortcut | Funktion | Quelle |
|----------|----------|--------|
| `Strg+Plus` | Zoom vergrößern | `ZoomIn` (`planner-gantt-view.c` Zeile 177) |
| `Strg+Minus` | Zoom verkleinern | `ZoomOut` (Zeile 180) |

„Einpassen“ (Zoom to fit) hat keinen Accelerator, sondern Toolbar-/Menüpunkt.

## Hilfe

| Shortcut | Funktion |
|----------|----------|
| `F1` | Benutzerhandbuch (yelp) |

## Sonstiges

- **Menüzugriff:** klassische GTK-Mnemonics (`Alt` + unterstrichener Buchstabe der Menüs Datei/Bearbeiten/Ansicht/Aktionen/Projekt/Hilfe).
- **Ansichtswechsel:** ohne Kurzbefehl – über die Ansichtsleiste links oder Menü **Ansicht** (Radio-Punkte).
- **Zellenbearbeitung:** in den Tabellen durch Doppelklick/Überschreiben der Spalte (GtkTreeView-Standard), kein eigener Planner-Accelerator.
- **Dateien direkt öffnen:** `planner projekt.planner` auf der Konsole oder Doppelklick im Dateimanager (Desktop-Datei `Exec=planner %F`, MIME `application/x-planner`); mehrere Dateien als mehrere Fenster.
- **Keine Mac-Version:** offizielle Builds sind Linux (Distributionen) und Windows (Projekt-Wiki); ein Homebrew-Build ist nicht Teil des Projekts.

## Ausdrücklich nicht vorhanden

- Kein Strg+O (Öffnen = F3), kein Strg+W für „Aufgabe entfernen“ (Strg+W = Fenster schließen)
- Keine Shortcuts für Ansichtswechsel, Import/Export, Kalenderdialoge
- Keine konfigurierbaren Kurzbefehle (keine Keyboard-Schemas in `app.drey.Planner.gschema.xml`)
