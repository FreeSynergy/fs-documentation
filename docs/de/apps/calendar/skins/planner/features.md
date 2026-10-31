# GNOME Planner - Funktionen

## Hauptfunktionen

### Aufgabenplanung
- Aufgaben mit Anfang/Ende, Aufwand (Man-hours), Completion-Prozent, Priorität
- Hierarchie (Vorgang → Teilvorgang), Meilensteine (Dauer 0)
- Vier Abhängigkeitstypen: Ende-Beginn (FS), Beginn-Beginn (SS), Ende-Ende (FF), Beginn-Ende (SF) inkl. Verzögerung (Lag)
- Kritischer Pfad (rot hervorgehoben), Vorwärts-/Rückwärtsterminierung (Early/Late)

### Ressourcen
- Ressourcen mit Standard-Stunden/Tag, Kalenderwochen (freie Tage), Zuordnung zu Aufgaben
- Ressourcen-Usage-Ansicht mit Überlastungsanzeige

### Diagramme und Ausgabe
- Gantt-Balken (inklusiv Meilensteindiamanten) und PERT-Netzwerk
- Drucken/PDF der Gantt-, Ressourcen- und PERT-Ansicht

### Dateiformate
- Nativ: `.ppx` (Planner XML)
- Import: Microsoft Project `.mpp` (via LibMSP), Import-Assistent
- Export: HTML (Tabellen), Druck via PDF; `.moe` (OpenProj) eingeschränkt

## Was Planner NICHT kann

- **Keine Mehrbenutzerbearbeitung**: eine Datei, kein Server, keine Sperrungen — Kollaboration nur über Dateiablage/Versionskontrolle
- **Keine Kalender-Sync** (kein CalDAV, keine ICS-Ausgabe als Standard — Druck/exportierte Ansichten nur indirekt)
- **Keine agilen Modi** (kein Kanban/Scrum-Board, keine Burndown)
- **Kein Kosten-/Budgetmodul** (nur Aufwand in Stunden, keine Sätze)
- **Keine Online-/Web-Version** und keine API für Live-Zugriffe
- **Ressourcenkalender ohne Feiertags-Import** (Feiertage manuell pflegen)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| libplanner | C-Bibliothek; Format-Reader/Writer (`.ppx`, `.mpp`) — Grundlage für Konverter |
| GanttProject | `.gan`-Dateien sind NICHT direkt lesbar; Umweg über MS-Project-/PMXML-Export von GanttProject |
| Druck-Pipeline | GTK-Druckdialog → PDF |
| Skripte | `.ppx` ist XML → eigene Konverter mit libplanner oder XSLT |
