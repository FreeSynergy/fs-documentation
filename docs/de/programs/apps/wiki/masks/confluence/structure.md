# Confluence - Struktur & UI/UX

## Übersicht

Confluence hat eine klassische dreispaltige Layout-Struktur mit Sidebar-Navigation und zentralem Content-Bereich.

## Fenster-Struktur

### Hauptbereiche

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (Navigation, Suche, Benutzermenü)                       │
├─────────────┬──────────────────────┬────────────────────────────┤
│             │                      │                            │
│  Sidebar    │   Main Content       │  Right Sidebar             │
│  (Links)    │   (Hauptinhalt)      │  (Metainformationen)       │
│             │                      │                            │
│ - Pages     │  ┌────────────────┐  │  - Page Info               │
│ - Spaces    │  │  Seite/Inhalt  │  │  - Versionen               │
│ - Dashboard │  │                │  │  - Autor                   │
│ - Templates │  │  [Editor oder  │  │  - Berechtigungen          │
│ - ...       │  │   Anzeige]     │  │  - Tags                    │
│             │  └────────────────┘  │                            │
└─────────────┴──────────────────────┴────────────────────────────┘
```

### Sidebar (Links)

Die Sidebar ist linksbündig platziert und enthält die Hauptnavigation:

| Element | Größe | Funktion |
|---------|-------|----------|
| Logo | ~50px | Confluence-Logo |
| Pages | variable | Seiten-Navigation |
| Spaces | variable | Space-Auswahl |
| Dashboard | ~30px | Dashboard-Zugriff |
| Templates | variable | Vorlagen-Zugriff |

### Content-Bereich (Mitte)

Der Content-Bereich nimmt den größten Teil des Bildschirms ein:

- **Header**: Seite Titel, Actions-Menü (Bearbeiten, Teilen, etc.)
- **Breadcrumbs**: Navigationspfad
- **Main Content**: Seite/Inhalt (Editor oder Anzeige)
- **Footer**: Footer-Informationen

### Rechte Sidebar

Optionale rechte Sidebar mit Metainformationen:

| Element | Funktion |
|---------|----------|
| Page Info | Metainformationen |
| Versionen | Versionsverlauf |
| Tags | Tag-Informationen |
| Weblinks | Verknüpfungen |

## UI/UX

### Design-Prinzipien

- **Klassisch**: Traditionelles Wiki-Design
- **Klarheit**: Klare Hierarchie und Struktur
- **Funktion**: Funktion vor Form
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

### Wiki Markup Editor

```
┌─────────────────────┬───────────────────────────────────────────────┐
│  Editor (Links)     │  Vorschau (Rechts)                            │
│                     │                                               │
│  [Wiki Markup]      │  [Geparsed HTML]                              │
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
