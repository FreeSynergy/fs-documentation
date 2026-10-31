# GNOME Planner - Beschreibung

## Was das Programm macht

Planner plant Projekte nach der klassischen Netzplan-/CPM-Logik: Vorgänge mit Dauern und Abhängigkeiten, Ressourcen mit Wochenkalender, kritischer Pfad als Berechnung. Das Ergebnis ist ein Gantt- oder PERT-Bild, das gedruckt oder als HTML exportiert wird. Es richtet sich an klassische (Wasserfall-)Projektplanung unter GNOME.

## Vorteile

- **Frei und lokal**: keine Cloud, `.ppx` bleibt eine lesbare XML-Datei
- **Echte Planungslogik**: FS/SS/FF/SF-Abhängigkeiten, Lag, Early/Late-Termine, kritischer Pfad
- **MS-Project-Import**: migriert `.mpp`-Altbestände ohne Lizenzzwang
- **GNOME-typische Schlichtheit**: drei Ansichten, keine Konten, kein Projektserver

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **GanttProject** | Java, ähnlich; dafür mit PMML/XML-Austausch und aktiverer Entwicklung. Planner ist GTK-nativer, GanttProject funktional breiter (Kosten, PMXML). |
| **ProjectLibre** | MS-Project-kompatibler Klon (Java), sehr nah an MPP; schwerfälliger, dafür import-/exportstärker |
| **MS Project** | kommerziell, mit Kostenrechnung, Ressourcenpool und Project-Server; Planner bewusst ohne alles davon |
| **Vikunja/OpenProject** | moderne webbasierte Projekte inkl. Aufgaben-Tracking; Planner ist reiner Desktop-Planer ohne Aufgaben-Ticketlogik |

## Technische Details

- **Backend/Logik**: C, libplanner (Planungs-Engine + Dateiformat-Handler)
- **Frontend**: GTK 3, Canvas-Zeichnung für Gantt/PERT
- **Datenhaltung**: Einzeldatei `.ppx` (XML); keine Datenbank
- **Authentifizierung**: keine (lokale Datei)
- **Plattformen**: Linux (GNOME), Paket in allen großen Distributionen; Windows-Builds unregelmäßig
- **Lizenz**: GPL

## Für wen geeignet

- Klassen- und Vereinsprojekte, Bau-/Handwerksplanung, Migrationsprojekte mit CPM-Denken
- MS-Project-Migrationen, bei denen Import + betrachten + drucken genügt
- als „Kalender-artige" Terminplanung, wenn Zeitachsen statt Terminkalender gefragt sind
