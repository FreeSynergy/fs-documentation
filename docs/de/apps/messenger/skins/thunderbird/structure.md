# Thunderbird - Struktur & UI/UX

## Übersicht

Thunderbird hat eine klassische, funktionale UI mit Activity Bar, Navigationbereich, Content-Bereich und Statusleiste, optimiert für E-Mail-Kommunikation.

## Fenster-Struktur

### Hauptbereiche

```
┌─────────────────────────────────────────────────────────────────┐
│  Titelleiste (Menü, Titel, Fenster-Steuerung)                   │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Sidebar         │
│  Bar  │   (Links)        │   (Mitte)        │   (Rechts)        │
│ (Int.)│  - Konten        │  - Nachrichten   │  - Vorschau        │
│       │  - Kalender      │  - Termine       │  - Kontakte        │
│       │  - Kontakte      │  - Kontakte      │  - Suchergebnisse  │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Links)

Die Activity Bar enthält die Hauptnavigation (integriert in die Navigationsleiste):

| Element | Funktion |
|---------|----------|
| Konten | Kontoverwaltung |
| Posteingang | E-Mail-Ordner |
| Gesendete Elemente | Gesendete Nachrichten |
| Entwürfe | Entwürfe |
| Papierkorb | Gelöschte Elemente |
| Junk-E-Mail | Spam-Ordner |
| Kalender | Terminübersicht (Lightning) |
| Adressbuch | Adressverwaltung (Lightning) |

### Navigation (Links)

Links in der Navigationsleiste:

| Element | Funktion |
|---------|----------|
| Postfächer | E-Mail-Ordner |
| Konten | Kontoverwaltung |
| Kalender | Kalenderübersicht (Lightning) |
| Adressbuch | Adressbuch (Lightning) |
| Abonnement-Feeds | RSS/Atom-Feeds |

### Content-Bereich (Mitte)

Der Content-Bereich nimmt den größten Teil des Bildschirms ein:

- **Postfächer-Liste**: Ausgewähltes Postfach
- **Ordner-Liste**: Unterordner
- **Elemente-Liste**: Nachrichten/Termine/Kontakte
- **Kalender-Ansicht**: Monats-/Wochenansicht (für Kalender)

### Sidebar (Rechts)

Optional rechts: Anzeige von Details abhängig vom ausgewählten Element

- **Vorschaufenster**: Inhalt ausgewählter Nachricht
- **Termin-Vorschau**: Details ausgewählter Termin
- **Kontakt-Vorschau**: Details ausgewählter Kontakt
- **Suchergebnisse**: Live-Suchergebnisse

## UI/UX

### Design-Prinzipien

- **Funktional**: Funktion über Form
- **Konsistent**: Einheitliches Design über alle Bereiche
- **Anpassbar**: Vielgestaltige Layout-Optionen
- **Mozilla-Style**: Befolgt Mozilla-Design-Richtlinien
- **Barrierefrei**: Fokus auf Zugänglichkeit

### Farbschema

- **Light Theme**: Klassisches helles Farbschema
- **Dark Theme**: Dunkles Farbschema
- **Benutzerdefiniert**: Anpassbare Farben über Theme-System
- **Kontextbezogene Farben**: Farben für Kalender, Kategorien

### Typography

- **Headings**: Klare Hierarchie
- **Text**: Lesbare Schriftgrößen (10-12pt)
- **Lists**: Klare Aufzählungen mit Kontrollkästchen
- **Monospace**: Für E-Mail-Headers

### Interaktionen

- **Hover-Effekte**: Visuelles Feedback beim Hover
- **Click-Feedback**: Direktes Feedback bei Klicks
- **Drag & Drop**: Für Verschieben von E-Mails, Terminen
- **Auto-save**: Automatisches Speichern von Entwürfen
- **Kontextmenüs**: Rechtsklick für Kontextaktionen

### Responsive Design

- **Desktop**: Volle Funktionen mit Sidebar
- **Tablet**: Eingeschränkt (Desktop-App)
- **Mobile**: Separaten App (Thunderbird Mobile in Entwicklung)

## Editor-Struktur

### E-Mail-Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Betreff                                                         │
├─────────────────────────────────────────────────────────────────┤
│  An: [Empfänger]                                                │
│  Cc: [Kopie]                                                    │
│  Bcc: [Blindkopie]                                              │
├─────────────────────────────────────────────────────────────────┤
│  Formatierungsleiste (Menü)                                     │
├─────────────────────────────────────────────────────────────────┤
│  Content-Bereich (Vollbild)                                     │
│                                                                 │
│  [E-Mail-Text]                                                  │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Anhänge                                                         │
└─────────────────────────────────────────────────────────────────┘
```

### Kalender-Editor (Lightning)

```
┌─────────────────────────────────────────────────────────────────┐
│  Betreff                                                         │
├─────────────────────────────────────────────────────────────────┤
│  Von: [Datum]     Bis: [Datum]                                  │
│  Ort: [Ort]                                                     │
│  Teilnehmer: [Teilnehmer]                                       │
├─────────────────────────────────────────────────────────────────┤
│  Beschreibung                                                   │
│                                                                 │
│  [Termin-Beschreibung]                                          │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Optionen (Dauer, Erinnerung, Farbe, etc.)                     │
└─────────────────────────────────────────────────────────────────┘
```

## Zugänglichkeit

- **Tastaturnavigation**: Komplette Steuerung per Tastatur
- **Screenreader-Unterstützung**: ARIA-Attribute
- **Kontrast**: Hoher Kontrast für bessere Lesbarkeit
- **Zoom**: Skalierbare UI (100-400%)
- **Barrierefreiheit**: Mozilla-barrierefreiheit Einstellungen

## Performance

- **Schnelles Laden**: Schnelles Öffnen von Nachrichten
- **Caching**: Client-seitiges Caching
- **Pagination**: Für große Listen
- **Debounce**: Für Suchfunktionen
- **Lazy Loading**: Für große Kalender und Adressbücher
