# VSCodium - Struktur & UI/UX

## Übersicht

VSCodium hat eine modulare Layout-Struktur mit Activity Bar, Sidebar, Editor-Bereich und Statusleiste.

## Fenster-Struktur

### Hauptbereiche

```
┌─────────────────────────────────────────────────────────────────┐
│  Title Bar (Menü, Fenster-Steuerung)                            │
├───────┬───────────────────────────────────────────────────────────┤
│       │                                                           │
│  Act. │   Sidebar (Dateibaum, Suche, Git, Debug, Erweiterungen)│
│  Bar  │                                                           │
│ (Links│  ┌───────────────────────┬─────────────────────────────┐ │
│  )    │  │  Explorer           │  Suchfenster                 │ │
│       │  │  - Projekte         │  - Suchfeld                  │ │
│       │  │  - Dateibaum        │  - Filter                    │ │
│       │  └───────────────────────┴─────────────────────────────┘ │
│       │                                                           │
│       │   Editor-Bereich (Mitte)                                  │
│       │  ┌─────────────────────────────────────────────────────┐  │
│       │  │  Dateiname 1    Dateiname 2    Dateiname 3          │  │
│       │  ├─────────────────────────────────────────────────────┤  │
│       │  │                                                     │  │
│       │  │  Code-Editor                                        │  │
│       │  │                                                     │  │
│       │  │  [Code mit Syntax-Highlighting]                     │  │
│       │  │                                                     │  │
│       │  └─────────────────────────────────────────────────────┘  │
│       │                                                           │
│       │   Statusleiste (Unten)                                    │
│       │  ┌─────────────────────────────────────────────────────┐  │
│       │  │  Zeile:Spalte  |  Syntax  |  Git  | Encoding  |  🐛 │  │
│       │  └─────────────────────────────────────────────────────┘  │
└───────┴───────────────────────────────────────────────────────────┘
```

### Activity Bar (Links)

Die Activity Bar ist linksbündig platziert und enthält die Hauptnavigation:

| Element | Größe | Funktion |
|---------|-------|----------|
| Explorer | ~50px | Dateibaum |
| Suche | ~50px | Dateisuche |
| Source Control | ~50px | Git |
| Debugging | ~50px | Debuggen |
| Erweiterungen | ~50px | Plugins |

### Editor-Bereich (Mitte)

Der Editor-Bereich nimmt den größten Teil des Bildschirms ein:

- **Tab-Leiste**: Offene Dateien
- **Editor**: Code-Editor mit Syntax-Highlighting
- **Sidebar (Rechts)**: Optional (Symbol-Definition, Suchergebnisse)

### Statusleiste (Unten)

Die Statusleiste zeigt wichtige Informationen:

| Element | Funktion |
|---------|----------|
| Zeile:Spalte | Cursor-Position |
| Syntax | Aktuelle Syntax |
| Git | Git-Status |
| Encoding | Datei-Kodierung |
| Linter | Linter-Status |

## UI/UX

### Design-Prinzipien

- **Minimalismus**: Reduzierte UI-Elemente
- **Klarheit**: Klare Hierarchie und Struktur
- **Flexibilität**: Anpassbare Layouts
- **Konsistenz**: Einheitliches Design über alle Bereiche

### Farbschema

- **Light Theme**: Klassisches helles Farbschema
- **Dark Theme**: Dunkles Farbschema für Nachtnutzung
- **Benutzerdefiniert**: Anpassbare Farben (Theme-System)

### Typography

- **Code**: Monospace-Schriftart
- **UI**: Sans-Serif-Schriftart
- **Lists**: Klare Aufzählungen

### Interaktionen

- **Hover-Effekte**: Visuelles Feedback beim Hover
- **Click-Feedback**: Direktes Feedback bei Klicks
- **Drag & Drop**: Für Datei-Operationen
- **Auto-save**: Automatisches Speichern (optional)

### Responsive Design

- **Desktop**: Volle Funktionen mit Sidebar
- **Tablet**: reduzierte Sidebar, optimierte Ansichten
- **Mobile**: Eingeschränkt (Desktop-App)

## Editior-Struktur

### Code-Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Tab-Leiste (Offene Dateien)                                    │
├─────────────────────────────────────────────────────────────────┤
│  Content-Bereich (Vollbild)                                     │
│                                                                 │
│  [Code mit Syntax-Highlighting]                                 │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Statusleiste (Zeile, Spalte, Syntax, Git, etc.)               │
└─────────────────────────────────────────────────────────────────┘
```

## Zugänglichkeit

- **Tastaturnavigation**: Komplette Steuerung per Tastatur
- **Screenreader-Unterstützung**: ARIA-Attribute
- **Kontrast**: Hoher Kontrast für bessere Lesbarkeit
- **Zoom**: Skalierbare UI ohne Funktionsverlust

## Performance

- **Schnelles Laden**: Schnelles Öffnen von Dateien
- **Caching**: Client-seitiges Caching
- **Pagination**: Für große Listen
- **Debounce**: Für Suchfunktionen
