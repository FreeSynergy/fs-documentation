# Mastodon - Struktur & UI/UX

## Übersicht

Mastodon hat eine moderne, klare UI mit Activity Bar, Navigationbereich, Content-Bereich und Statusleiste, optimiert für Mikroblogging.

## Fenster-Struktur

### Hauptbereiche

```
┌─────────────────────────────────────────────────────────────────┐
│  Titelleiste (Menü, Titel, Fenster-Steuerung)                   │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Sidebar         │
│  Bar  │   (Links)        │   (Mitte)        │   (Rechts)        │
│ (Int.)│  - Timeline      │  - Toots         │  - Benutzer       │
│       │  - Toots         │  - Timeline      │  - Benachrichtig. │
│       │  - Profile       │                  │  - Profil         │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Links)

Die Activity Bar enthält die Hauptnavigation (integriert in die Navigationsleiste):

| Element | Funktion |
|---------|----------|
| Timeline | Timeline-Übersicht |
| Toots | Toot-Eingabefeld |
| Profile | Eigenes Profil |
| Benachrichtigungen | Benachrichtigungen |
| Direktnachrichten | Direktnachrichten |

### Navigation (Links)

Links in der Navigationsleiste:

| Element | Funktion |
|---------|----------|
| Home | Home-Timeline |
| Local | Local-Timeline |
| Federated | Federated-Timeline |
| Hashtags | Hashtag-Timeline |
| Profile | Eigenes Profil |
| Benachrichtigungen | Benachrichtigungen |
| Direktnachrichten | Direktnachrichten |

### Content-Bereich (Mitte)

Der Content-Bereich nimmt den größten Teil des Bildschirms ein:

- **Timeline-Übersicht**: Timeline-Auswahl (Home, Local, Federated)
- **Toot-Liste**: Toots in chronologischer Reihenfolge
- **Toot-Eingabefeld**: Toots eingeben

### Sidebar (Rechts)

Optional rechts: Anzeige von Details abhängig vom ausgewählten Element

- **Benutzer-Profile**: Profilinformationen
- **Benachrichtigungen**: Liste der Benachrichtigungen
- **Profil**: Eigenes Profil
- **Suche**: Suche in der Timeline

## UI/UX

### Design-Prinzipien

- **Minimal**: Minimalistisches Design mit Fokus auf Inhalt
- **Klar**: Klare Hierarchie und Navigation
- **Funktional**: Funktion über Form
- **Konsistent**: Einheitliches Design über alle Bereiche

### Farbschema

- **Light Theme**: Helles Farbschema (Standard)
- **Dark Theme**: Dunkles Farbschema
- **Benutzerdefiniert**: Anpassbare Farben über Theme-System
- **Kontextbezogene Farben**: Farben für Toot-Status

### Typography

- **Headings**: Klare Hierarchie
- **Text**: Lesbare Schriftgrößen (14-16pt)
- **Lists**: Klare Aufzählungen
- **Monospace**: Für Code-Blöcke

### Interaktionen

- **Hover-Effekte**: Visuelles Feedback beim Hover
- **Click-Feedback**: Direktes Feedback bei Klicks
- **Drag & Drop**: Für Medien-Uploads
- **Auto-save**: Automatisches Speichern von Entwürfen
- **Live-Vorschau**: Live-Vorschau bei Toot-Eingabe

### Responsive Design

- **Desktop**: Volle Funktionen mit Sidebar
- **Tablet**: Eingeschränkt (Desktop-App)
- **Mobile**: Separate Mobile-Apps (iOS, Android)

## Editor-Struktur

### Toot-Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Neuer Toot                                                     │
├─────────────────────────────────────────────────────────────────┤
│  [Toot-Eingabefeld]                                             │
├─────────────────────────────────────────────────────────────────┤
│  Medien                                                         │
├─────────────────────────────────────────────────────────────────┤
│  [Bild/Videos auswählen]                                        │
├─────────────────────────────────────────────────────────────────┤
│  Sensitiv                                                                       │
├─────────────────────────────────────────────────────────────────┤
│  [Sensitiv-Kontrollkästchen]                                    │
├─────────────────────────────────────────────────────────────────┤
│  Sichtbarkeit                                                   │
├─────────────────────────────────────────────────────────────────┤
│  [Public/Unlisted/Private/Direct]                               │
├─────────────────────────────────────────────────────────────────┤
│  [Toot senden]                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Timeline-Ansicht

```
┌─────────────────────────────────────────────────────────────────┐
│  Timeline-Header                                                │
├─────────────────────────────────────────────────────────────────┤
│  Home  Local  Federated  Hashtags                              │
├─────────────────────────────────────────────────────────────────┤
│  Toot-Liste                                                     │
├─────────────────────────────────────────────────────────────────┤
│  [Toot]                                                         │
│  [Toot]                                                         │
│  [Toot]                                                         │
└─────────────────────────────────────────────────────────────────┘
```

## Zugänglichkeit

- **Tastaturnavigation**: Komplette Steuerung per Tastatur
- **Screenreader-Unterstützung**: ARIA-Attribute
- **Kontrast**: Hoher Kontrast für bessere Lesbarkeit
- **Zoom**: Skalierbare UI (100-400%)
- **Barrierefreiheit**: WCAG-Konformität

## Performance

- **Schnelles Laden**: Schnelles Öffnen von Toots
- **Caching**: Client-seitiges Caching
- **Pagination**: Für große Listen
- **Debounce**: Für Suchfunktionen
- **Lazy Loading**: Für große Timelines
