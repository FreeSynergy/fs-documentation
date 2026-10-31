# Kontact - Struktur & UI/UX

## Übersicht

Kontact hat eine klassische, funktionsreiche UI mit Activity Bar, Navigationbereich, Content-Bereich und Statusleiste, optimiert für das KDE-Desktop-Environment.

## Fenster-Struktur

### Hauptbereiche

```
┌─────────────────────────────────────────────────────────────────┐
│  Titelleiste (Menü, Titel, Fenster-Steuerung)                   │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Sidebars        │
│  Bar  │   (Links)        │   (Mitte)        │   (Rechts)        │
│ (Ext.)│  - Kontact       │  - E-Mail        │  - Kalender       │
│       │  - E-Mail        │  - Kalender      │  - Kontakte       │
│       │  - Kalender      │  - Kontakte      │  - Aufgaben       │
│       │  - Kontakte      │  - Aufgaben      │  - Notizen        │
│       │  - Aufgaben      │  - Notizen       │  - Schnellsuche   │
│       │  - Notizen       │                  │                   │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Links)

Die Activity Bar enthält die Hauptnavigation und ist am linken Rand:

| Element | Funktion |
|---------|----------|
| Kontact | Hauptansicht (Übersicht) |
| E-Mail | E-Mail-Ansicht (KMail) |
| Kalender | Terminübersicht (KOrganizer) |
| Kontakte | Adressverwaltung (KAddressBook) |
| Aufgaben | Aufgabenliste (Todo-Listen) |
| Notizen | Notizverwaltung (KNotes) |
| News | News-Reader (KNode) |

### Navigation (Links-Seitenleiste)

Neben der Activity Bar (in der aktuellen Ansicht):

| Element | Funktion |
|---------|----------|
| Posteingang | E-Mail-Ordner |
| Gesendete Elemente | Gesendete Nachrichten |
| Entwürfe | Entwürfe |
| Papierkorb | Gelöschte Elemente |
| Junk-E-Mail | Spam-Ordner |
| Kalender | Kalenderübersicht |
| Kontakte | Kontaktordner |
| Aufgaben | Aufgabenlisten |
| Notizen | Notizen |

### Content-Bereich (Mitte)

Der Content-Bereich nimmt den größten Teil des Bildschirms ein:

- **Postfächer-Liste**: Ausgewähltes Postfach
- **Ordner-Liste**: Unterordner (für E-Mail)
- **Elemente-Liste**: Nachrichten/Termine/Kontakte/Aufgaben/Notizen
- **Kalender-Ansicht**: Monats-/Wochenansicht (für Kalender)
- **Termine**: Terminliste mit Zeitachse

### Sidebars (Rechts)

Optional rechts: Anzeige von Details abhängig vom ausgewählten Element

- **E-Mail-Vorschau**: Inhalt ausgewählter Nachricht
- **Termin-Vorschau**: Details ausgewählter Termin
- **Kontakt-Vorschau**: Details ausgewählter Kontakt
- **Aufgaben-Vorschau**: Details ausgewählte Aufgabe
- **Notiz-Vorschau**: Inhalt ausgewählter Notiz

## UI/UX

### Design-Prinzipien

- **KDE-native**: Befolgt KDE Human Interface Guidelines
- **Funktional**: Funktion über Form
- **Konsistent**: Einheitliches Design über alle Bereiche
- **Anpassbar**: Vielgestaltige Layout-Optionen
- **Plasma-Integration**: Nahtlose Integration mit KDE Plasma

### Farbschema

- **Light Theme**: Klassisches helles Farbschema (Breeze Light)
- **Dark Theme**: Dunkles Farbschema (Breeze Dark)
- **Benutzerdefiniert**: Anpassbare Farben über Systemeinstellungen
- **Kontextbezogene Farben**: Farben für Kalender, Kategorien

### Typography

- **Headings**: Klare Hierarchie (H1, H2, H3)
- **Text**: Lesbare Schriftgrößen (9-12pt)
- **Lists**: Klare Aufzählungen mit Kontrollkästchen
- **Monospace**: Für E-Mail-Headers und Code

### Interaktionen

- **Hover-Effekte**: Visuelles Feedback beim Hover (Breeze-Theme)
- **Click-Feedback**: Direktes Feedback bei Klicks
- **Drag & Drop**: Für Verschieben von E-Mails, Terminen, Kontakten
- **Auto-save**: Automatisches Speichern von Entwürfen, Notizen
- **Kontextmenüs**: Rechtsklick für Kontextaktionen

### Responsive Design

- **Desktop**: Volle Funktionen mit Sidebar
- **Tablet**: Eingeschränkt (Desktop-App)
- **Mobile**: Separaten App (KDE Mobile Apps)

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

### Kontakt-Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Allgemein                                                       │
├─────────────────────────────────────────────────────────────────┤
│  Name: [Vorname] [Nachname]                                     │
│  Organisation: [Organisation]                                   │
├─────────────────────────────────────────────────────────────────┤
│  Kontaktdaten                                                    │
├─────────────────────────────────────────────────────────────────┤
│  E-Mail: [E-Mail]      Telefon: [Telefon]                       │
│  Web: [Webseite]       Fax: [Fax]                               │
├─────────────────────────────────────────────────────────────────┤
│  Adresse                                                         │
├─────────────────────────────────────────────────────────────────┤
│  Straße: [Straße]      Stadt: [Stadt]                           │
│  PLZ: [PLZ]            Land: [Land]                             │
├─────────────────────────────────────────────────────────────────┤
│  Benutzerdefinierte Felder                                       │
└─────────────────────────────────────────────────────────────────┘
```

## Zugänglichkeit

- **Tastaturnavigation**: Komplette Steuerung per Tastatur
- **Screenreader-Unterstützung**: AT-Support (AT-SPI)
- **Kontrast**: Hoher Kontrast für bessere Lesbarkeit
- **Zoom**: Skalierbare UI (100-400%)
- **Barrierefreiheit**: KDE-barrierefreiheit Einstellungen

## Performance

- **Schnelles Laden**: Schnelles Öffnen von Nachrichten
- **Caching**: Client-seitiges Caching
- **Pagination**: Für große Listen
- **Debounce**: Für Suchfunktionen
- **Threading**: Multithreading für schnelle Rechenoperationen
