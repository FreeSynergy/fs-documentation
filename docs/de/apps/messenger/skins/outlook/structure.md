# Outlook - Struktur & UI/UX

## Übersicht

Outlook hat eine klassische, funktionsreiche UI mit einer Activity Bar, Navigationbereich, Content-Bereich und Statusleiste.

## Fenster-Struktur

### Hauptbereiche

```
┌─────────────────────────────────────────────────────────────────┐
│  Titelleiste (Menü, Titel, Fenster-Steuerung)                   │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Preview         │
│  Bar  │   (Links)        │   (Mitte)        │   (Rechts)        │
│ (Ext.)│  - Postfächer    │  - Nachrichten   │  - Nachrichten    │
│       │  - Kalender      │  - Termine       │  - Vorschau       │
│       │  - Kontakte      │  - Kontakte      │  - Details        │
│       │  - Aufgaben      │  - Aufgaben      │                   │
│       │  - Notizen       │  - Notizen       │                   │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Links)

Die Activity Bar enthält die Hauptnavigation:

| Element | Funktion |
|---------|----------|
| Postfächer | E-Mail-Ansicht |
| Kalender | Terminübersicht |
| Kontakte | Adressverwaltung |
| Aufgaben | Aufgabenliste |
| Notizen | Notizverwaltung |

### Navigation (Links)

Neben der Activity Bar:

| Element | Funktion |
|---------|----------|
| Posteingang | E-Mail-Ordner |
| Gesendete Elemente | Gesendete Nachrichten |
| Entwürfe | Entwürfe |
| Papierkorb | Gelöschte Elemente |
| Junk-E-Mail | Spam-Ordner |
| Kalender | Kalenderübersicht |
| Kontakte | Kontaktordner |

### Content-Bereich (Mitte)

Der Content-Bereich nimmt den größten Teil des Bildschirms ein:

- **Postfächer-Liste**: Ausgewähltes Postfach
- **Ordner-Liste**: Unterordner
- **Elemente-Liste**: Nachrichten/Termine/Kontakte

### Preview-Bereich (Rechts)

Optional rechts:
- **Nachrichtenvorschau**: Inhalt ausgewählter Nachricht
- **Termin-Vorschau**: Details ausgewählter Termin
- **Kontakt-Vorschau**: Details ausgewählter Kontakt

## UI/UX

### Design-Prinzipien

- **Klassisch**: Traditionelle Office-Anwendung
- **Funktional**: Funktion über Form
- **Konsistenz**: Einheitliches Design über alle Bereiche
- **Anpassbar**: Vielgestaltige Layout-Optionen

### Farbschema

- **Light Theme**: Klassisches helles Farbschema
- **Dark Theme**: Dunkles Farbschema (neuer)
- **Benutzerdefiniert**: Anpassbare Farben

### Typography

- **Headings**: Klare Hierarchie
- **Text**: Lesbare Schriftgrößen (10-12pt)
- **Lists**: Klare Aufzählungen

### Interaktionen

- **Hover-Effekte**: Visuelles Feedback beim Hover
- **Click-Feedback**: Direktes Feedback bei Klicks
- **Drag & Drop**: Für Verschieben von E-Mails
- **Auto-save**: Automatisches Speichern von Entwürfen

### Responsive Design

- **Desktop**: Volle Funktionen mit Sidebar
- **Tablet**: Eingeschränkt (Desktop-App)
- **Mobile**: Separaten App (Outlook Mobile)

## Editior-Struktur

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

### Kalender-Editor

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

## Performance

- **Schnelles Laden**: Schnelles Öffnen von Nachrichten
- **Caching**: Client-seitiges Caching (OST-Dateien)
- **Pagination**: Für große Listen
- **Debounce**: Für Suchfunktionen
