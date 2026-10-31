# OpenProject - Struktur & UI/UX

## Übersicht

OpenProject nutzt ein klassisches Drei-Bereichs-Layout: schmaler Kopfbereich mit Projektauswahl, linke Modul-Leiste, großer Inhaltsbereich. Arbeitspakete ergänzen diesen Rahmen um einen rechten Detail-Split (Tab-Ansicht) und eine optionale Vollbild-Tabelle.

## Fenster-Struktur

### Hauptlayout

```
+------------------------------------------------------------------+
| Leiste: [Projekt wechseln v] [Suche]        [Glocke] [Avatar v]  |
+----------+-------------------------------------------------------+
| Modul-   |  Inhalt (Modul)                                       |
| leiste   |  +--------------------------------------------------+ |
|          |  | Filterleiste / Query-Werkzeuge                   | |
| Uebersicht|  +--------------------------------------------------+ |
| Aktivitaet|  |                                                  | |
| Meilensteine| | Tabelle / Gantt / Board / Wiki                | |
| Arbeitspakete| |                                               | |
| Board    |  |                                                  | |
| Gantt    |  +--------------------------------------------------+ |
| Wiki ... |  | Pagination                                       | |
+----------+-------------------------------------------------------+
```

### Arbeitspaket-Ansicht mit Detail-Split

```
+------------------------------------------------------------------+
| Leiste / Modul-Leiste (wie oben)                                 |
+--------------------------------------------+---------------------+
|  Tabellen- oder Listenansicht              |  Detail-Split       |
|  [WP-Nummer] [Titel] [Status] [Datum]      |  Register:          |
|  [x] Auftrag A  ...                        |  Details | Aktivi-  |
|  [ ] Auftrag B  ...                        |  taeten | Kommentare |
|                                            |  Uebergang-Buttons  |
+--------------------------------------------+---------------------+
```

### Bereichs-Tabelle

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfleiste | oben | Projektauswahl, globale Suche, Benachrichtigungen, Benutzermenü |
| Modul-Leiste | links | Module des gewählten Projekts, aufklappbar, mobil einklappbar |
| Query-Werkzeuge | über Inhalt | Filter, Sortierung, Gruppen, Spaltenauswahl, Speichern |
| Hauptinhalt | Mitte | Tabelle, Gantt, Board, Wiki-Inhalt, Meeting-Liste |
| Detail-Split | rechts | Arbeitspaket-Details, Aktivitäten, Kommentare (aufklappbar) |
| Fußzeile | unten | Versionsnummer, Datenschutz-/Impressumslinks (konfigurierbar) |

## UI/UX

### Design-Prinzipien

- **Modularität**: jedes Thema ist ein eigenes Modul mit eigener URL und eigenem Menüpunkt
- **Tabellenzentrierung**: Massenpflege über inline bearbeitbare Tabellen statt Dialogflut
- **Split-Screen statt Modal**: Kontext bleibt sichtbar, wenn ein Arbeitspaket geöffnet wird
- **Rechtegesteuerte UI**: nicht erlaubte Aktionen werden ausgeblendet, nicht nur deaktiviert

### Farbschema und Themes

- **Helle Standardoberfläche** mit blauer Akzentfarbe
- **Dunkles Farbschema** (Dark Mode) wählbar; weitere eigene Themes über die Instanzeinstellungen (versionsabhängig)
- **Benutzerdefiniertes Theme**: Admins können Farbpalette der Instanz anpassen
- Status- und Prioritätsfarben sind über Aufzählungen konfigurierbar

### Interaktionen

- **Inline-Bearbeitung**: Zellen in Tabellen direkt editierbar, Speichern mit Tab/Enter (versionsabhängig)
- **Drag & Drop**: Gantt-Balken, Board-Karten, Wiki-Struktur (Reihenfolge versionsabhängig)
- **Register und Auf-/Zuklappen**: Detail-Split, Filterleiste und Modul-Leiste sind einklappbar
- **Animationen**: dezente Übergänge beim Öffnen des Detailsplits, Skeleton-/Ladeanzeigen; keine aufwendigen Effekte
- **Autocomplete**: Benutzer-, Versions- und Projekt-Auswahlfelder mit Vorschlägen

### Responsive Design

- **Desktop**: volles Drei-Spalten-Layout mit Detail-Split
- **Tablet**: Modul-Leiste einklappbar, Detail-Ansicht als volle Seite
- **Mobil**: Hamburger-Menü, Tabellen reduzieren auf Karteikarten-Layout, Boards horizontal scrollbar
- Eigene native Apps fehlen; die Webansicht ist für Touch optimiert

## Zugänglichkeit

- **Fokussteuerung**: Tastaturfokus folgt Tab-Reihenfolge durch Leiste, Filter, Tabelle
- **Screenreader**: Grundlegende ARIA-Beschriftungen an Filtern und Tabellen (Ausbau je Version, Stand versionsabhängig)
- **Kontrast**: dunkles Schema und konfigurierbare Farben verbessern Kontrast; WCAG-Anpassungen sind wiederkehrendes Thema der Roadmap
- **Skalierung**: Oberfläche skaliert mit Browser-Zoom ohne Funktionsverlust

## Performance

- **Serverseitige Pagination**: Tabellen und Aktivitäten chronologisch seitenweise geladen (Standardseite 30, konfigurierbar, versionsabhängig)
- **Caching**: Rails-Asset-Caching plus optionaler Cache Store (Datei/Memcached); Instanz-Konfiguration empfohlen
- **Nachladen**: Aktivitätsstrom und Boards aktualisieren per Polling/WebSocket-Anteilen (versionsabhängig)
- **Kostenloser Tipp**: gespeicherte Abfragen mit engen Filtern halten die Tabellenansicht schnell
