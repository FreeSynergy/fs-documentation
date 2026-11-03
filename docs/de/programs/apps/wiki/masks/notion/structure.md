# Notion - Struktur & UI/UX

## Übersicht

Notion hat eine klare, benutzerfreundliche Struktur mit einer linken Sidebar-Navigation und einem zentralem Content-Bereich.

## Fenster-Struktur

### Hauptbereiche

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (Workspace, Suche, Benutzermenü)                        │
├────────────┬────────────────────────────────────────────────────┤
│            │                                                     │
│  Sidebar   │     Content-Bereich                                 │
│  (Links)   │     (Hauptinhalt)                                   │
│            │                                                     │
│ - Home     │  ┌─────────────────────────────────────────────┐   │
│ - Pages    │  │  Seite/Inhalt                               │   │
│ - Database │  │                                             │   │
│ - Templates│  │  [Editor oder Anzeige]                      │   │
│ - Members  │  │                                             │   │
│ - Dashboard│  │                                             │   │
│ - Settings │  └─────────────────────────────────────────────┘   │
│            │                                                     │
└────────────┴────────────────────────────────────────────────────┘
```

### Sidebar (Links)

Die Sidebar ist linksbündig platziert und enthält die Hauptnavigation:

| Element | Größe | Funktion |
|---------|-------|----------|
| Logo | ~40px | Notion-Logo |
| Navigationselemente | variable | Menüpunkte |
| Workspace-Auswahl | ~40px | Workspace wechseln |

### Content-Bereich (Mitte)

Der Content-Bereich nimmt den größten Teil des Bildschirms ein:

- **Header**: Seite Titel, Menü (Bearbeiten, Teilen, etc.)
- **Breadcrumbs**: Navigationspfad
- **Main Content**: Seite/Inhalt (Editor oder Anzeige)
- **Sidebar (Rechts)**: Optionale Metainformationen (Versionen, Autor, etc.)

### Layout-Varianten

1. **Standard-Layout**: Sidebar Links + Content + Sidebar Rechts
2. **Kompakt-Layout**: Sidebar Links + Content (ohne rechte Sidebar)
3. **Vollbild-Editor**: Nur Editor ohne Navigationsleisten

## UI/UX

### Design-Prinzipien

- **Minimalismus**: Reduzierte UI-Elemente
- **Klarheit**: klare Hierarchie und Struktur
- **Sofortigkeit**: Schnelles Feedback bei Interaktionen
- **Konsistenz**: Einheitliches Design über alle Bereiche

### Farbschema

- **Light Theme**: Klassisches helles Farbschema
- **Dark Theme**: Dunkles Farbschema für Nachtnutzung
- **Benutzerdefiniert**: Anpassbare Farben (Theme-System)

### Typography

- **Headings**: Klare Hierarchie (H1-H6)
- **Text**: Lesbare Schriftgrößen (14-16px)
- **Code**: Monospace-Schriftart
- **Lists**: Klare Aufzählungen

### Interaktionen

- **Hover-Effekte**: Visuelles Feedback beim Hover
- **Click-Feedback**: Direktes Feedback bei Klicks
- **Drag & Drop**: Für Medien-Uploads
- **Auto-save**: Automatisches Speichern im Editor

### Responsive Design

- **Desktop**: Volle Funktionen mit Sidebar
- **Tablet**: reduzierte Sidebar, optimierte Ansichten
- **Mobile**: Hamburger-Menü, optimierte Editor-Funktionen

## Editior-Struktur

### Block-basierter Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Block-Menü (Menü für jeden Block)                             │
├─────────────────────────────────────────────────────────────────┤
│  Content-Bereich (Vollbild)                                     │
│                                                                 │
│  [Text, Tabellen, Bilder, etc.]                                 │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Statusleiste (Wörter, Zeichen, Vorschau-Button)               │
└─────────────────────────────────────────────────────────────────┘
```

## Zugänglichkeit

- **Tastaturnavigation**: Komplette Steuerung per Tastatur
- **Screenreader-Unterstützung**: ARIA-Attribute
- **Kontrast**: Hoher Kontrast für bessere Lesbarkeit
- **Zoom**: Skalierbare UI ohne Funktionsverlust

## Performance

- **Schnelles Laden**: Lazy Loading für Bilder
- **Caching**: Client-seitiges Caching
- **Pagination**: Für große Listen
- **Debounce**: Für Suchfunktionen
