# MediaWiki - Struktur & UI/UX

## Übersicht

MediaWiki hat eine klassische Layout-Struktur mit Sidebar-Navigation und zentralem Content-Bereich. Das Layout ist stark benutzerrechte-abhängig.

## Fenster-Struktur

### Hauptbereiche

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (Navigation, Suche, Benutzermenü)                       │
├─────────────┬───────────────────────────────────────────────────┤
│             │                                                   │
│  Sidebar    │   Main Content                                    │
│  (Links)    │   (Hauptinhalt)                                   │
│             │                                                   │
│ - Aktionen  │  ┌─────────────────────────────────────────┐     │
│ - Werkzeuge │  │  Seite/Inhalt                           │     │
│ - Spezial   │  │                                         │     │
│             │  │  [Editor oder Anzeige]                  │     │
│             │  │                                         │     │
│             │  └─────────────────────────────────────────┘     │
└─────────────┴───────────────────────────────────────────────────┘
```

### Sidebar (Links)

Die Sidebar ist linksbündig platziert und enthält die Hauptnavigation:

| Element | Größe | Funktion |
|---------|-------|----------|
| Logo | ~40px | MediaWiki-Logo |
| Navigation | variable | Aktionen, Werkzeuge |
| Suche | ~30px | Suchfeld |
| Sprachen | variable | Interwiki-Links |

### Content-Bereich (Mitte)

Der Content-Bereich nimmt den größten Teil des Bildschirms ein:

- **Header**: Seite Titel, Aktionen-Menü (Bearbeiten, Teilen, etc.)
- **Breadcrumbs**: Navigationspfad (optional)
- **Main Content**: Seite/Inhalt (Editor oder Anzeige)
- **Footer**: Footer-Informationen (Seitenautor, Lizenz, etc.)

## UI/UX

### Design-Prinzipien

- **Minimalismus**: Reduzierte UI-Elemente
- **Klarheit**: Klare Hierarchie und Struktur
- **Funktion**: Funktion über Form
- **Konsistenz**: Einheitliches Design über alle Bereiche

### Farbschema

- **Light Theme**: Klassisches helles Farbschema
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

### Visueller Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Formatierungsleiste (Menü)                                     │
├─────────────────────────────────────────────────────────────────┤
│  Content-Bereich (Vollbild)                                     │
│                                                                 │
│  [Text, Tabellen, Bilder, etc.]                                 │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Statusleiste (Wörter, Zeichen, Vorschau-Button)               │
└─────────────────────────────────────────────────────────────────┘
```

### Quelltext-Editor

```
┌─────────────────────┬───────────────────────────────────────────────┐
│  Editor (Links)     │  Diff/Preview (Rechts)                        │
│                     │                                               │
│  [WikiText]         │  [Geparsed HTML]                              │
│                     │                                               │
└─────────────────────┴───────────────────────────────────────────────┘
```

## Zugänglichkeit

- **Tastaturnavigation**: Komplette Steuerung per Tastatur
- **Screenreader-Unterstützung**: ARIA-Attribute
- **Kontrast**: Hoher Kontrast für bessere Lesbarkeit
- **Zoom**: Skalierbare UI ohne Funktionsverlust

## Performance

- **Schnelles Laden**: Server-seitiges Caching
- **Client-seitiges Caching**: Browser-seitiges Caching
- **Pagination**: Für große Listen
- **Debounce**: Für Suchfunktionen
