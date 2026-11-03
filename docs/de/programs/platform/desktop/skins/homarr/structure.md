# Homarr - Struktur & UI/UX

## Übersicht

Homarr zeigt nach dem Anmelden genau eine Fläche: das aktive Board. Bedienelemente sitzen in einer schmalen Kopfzeile, Inhalte in einem Raster aus Kacheln. Bearbeitungs- und Einstellungsdialoge legen sich als Overlay über das Board.

## Fenster-Struktur

### Board-Ansicht

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile: Board-Wechsler | Suchleiste | Bearbeiten | Konto-Menü    │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   Raster (Grid) mit Widget-Kacheln                                   │
│   ┌───────────────┐ ┌───────────────┐ ┌──────────────────────────┐   │
│   │ App-Kachel    │ │ Docker        │ │ Kalender / RSS           │   │
│   │ Icon + Name   │ │ Containerliste│ │ Einträge                 │   │
│   ├───────────────┤ ├───────────────┤ └──────────────────────────┘   │
│   │ Status        │ │ Diagramm      │ ┌──────────────────────────┐   │
│   │ URL-Ampel     │ │ Traffic       │ │ JSON-Wert / Info         │   │
│   └───────────────┘ └───────────────┘ └──────────────────────────┘   │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│  Meldungen (Toast unten) · Statuszeile der Widgets                   │
└──────────────────────────────────────────────────────────────────────┘
```

### Bearbeitungsmodus

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile: Bearbeiten aktiv (hervorgehoben) | Speichern/Schließen   │
├───────────────┬──────────────────────────────────────────────────────┤
│  Palette      │  Raster mit Griffpunkten                             │
│  Widget-Aus-  │  ┌─[⋮]────────[✎][✕]─┐                              │
│  wahl, Suche  │  │  Kachel (Resize-   │                              │
│  nach Namen   │  │  ecke unten rechts)│                              │
│               │  └────────────────────┘                              │
│  Board-Optionen│                                                     │
└───────────────┴──────────────────────────────────────────────────────┘
```

### Einstellungsdialog (Overlay)

```
┌──────────────────────────────────────────┐
│  Titel des Dialogs              [✕]      │
├──────────────────────────────────────────┤
│  Formular (Gruppen, Tabs)                │
│  Feld · Feld · Auswahl · Schalter        │
├──────────────────────────────────────────┤
│           [Abbrechen]  [Speichern]       │
└──────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfzeile | Oben | Board-Wechsler, Suche, Bearbeiten, Konto-Menü |
| Raster | Mitte | Widget-Kacheln in Spalten/Zeilen |
| Widget-Kachel | Im Raster | Titelzeile, Icon, Inhalt, Aktionen |
| Widget-Palette | Links (Bearbeitung) | verfügbare Kacheln zum Hineinziehen |
| Board-Einstellungen | Overlay/Seitenpanel | Raster, Hintergrund, Farben, Freigaben |
| Instanzeinstellungen | Separate Ansicht | Nutzer, Einladungen, Integrationen, Zertifikate |
| Toast-Meldungen | Unten | Erfolg, Fehler, Verbindungsstatus |

## UI/UX

### Design-Prinzipien

- **Inhalt vor Chrom**: Kacheln dominieren, Bedienelemente bleiben klein
- **Sofortige Rückmeldung**: Änderungen am Layout wirken sofort, Fehler erscheinen als Meldung
- **Ein Board pro Ansicht**: kein Dauer-Nebeneinander mehrerer Dashboards
- **Wiederverwendbare Bausteine**: Mantine-Komponenten für Formulare, Dialoge, Menüs

### Farbschema und Themes

- **Hell und Dunkel** plus Systemeinstellung, pro Konto umschaltbar
- **Akzentfarbe** und Deckkraft/Blur für Kacheln einstellbar
- **Hintergrundbilder** pro Board (Upload oder URL)
- **Kontrast** bleibt in beiden Schemata hoch; Warn- und Erfolgsfarben sind fest definiert

### Interaktionen

- **Drag & Drop**: Kachel an der Griffzone aufnehmen, Zielbereich wird hervorgehoben, Einrasten am Raster
- **Größe ändern**: an der Unteren Kante/Ecke ziehen, Rasterschritte als Vorschau
- **Rechtsklick**: Kontextmenü an der Kachel (abschaltbar)
- **Hover**: Schweben zeigt Symbolleiste und leichte Aufhellung
- **Animationen**: kurze Übergänge beim Umsortieren, Laden als Skelett-/Platzhalterdarstellung
- **Autocomplete**: Dropdown-Auswahl in Integrations- und Suchfeldern

### Responsive Design

- **Desktop**: volles Raster, alle Kopfzeilen-Elemente, Board- und Instanzeinstellungen
- **Tablet**: reduzierte Spaltenanzahl, Menüs als Overlay
- **Mobil**: eigenes, separat speicherbares Layout; Navigation über Dropdown und Touch-Gesten
- **Schriftgrößen** bleiben auf kleinen Bildschirmen lesbar, Kacheln Stapeln untereinander

### Zugänglichkeit

- **Tastatur**: Dialoge, Formulare und Menüs sind per Tab erreichbar, `Esc` schließt Overlays
- **Screenreader**: Mantine setzt ARIA-Rollen für Dialoge, Menüs und Meldungen
- **Fokusanzeige**: fokussierte Elemente sind sichtbar markiert
- **Farbunabhängigkeit**: Status wird zusätzlich über Symbol und Text vermittelt
- **Zoom**: Browser-Zoom ohne abgeschnittene Bedienelemente

### Performance

- **Datenabruf**: Widgets fragen Integrations-Endpunkte in Intervallen ab, nicht permanent
- **Server-seitige Entlastung**: Anfragen an Ziel-Dienste laufen über den Homarr-Server (CORS und Schlüssel bleiben dort)
- **Caching**: zwischengespeckte Werte in der Instanz, Ladezustand pro Kachel
- **Träge Integrationen** bremsen das Board nicht: betroffene Kacheln zeigen einen Lade- oder Fehlerzustand
- **Empfehlung**: wenige, dafür sinnvolle Integrations-Widgets statt vieler Statuschecks mit kurzen Intervallen

## Siehe auch

- [menu.md](menu.md) - Menüpunkte nach Rolle
- [features.md](features.md) - Widgets und Integrationen
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
- [api.md](api.md) - Interne API und Integrations-Proxy
