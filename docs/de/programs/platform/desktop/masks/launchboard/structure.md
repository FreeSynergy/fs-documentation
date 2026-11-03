# LaunchBoard - Struktur & UI/UX

## Übersicht

Nach der Anmeldung zeigt LaunchBoard genau eine Fläche: das aktive Board. Bedienelemente sitzen in einer Kopfzeile, Inhalte in einem Kachelraster. Der Editor legt sich als Panel über das Board, Einstellungsdialoge als Overlay. Die Oberfläche ist auf hohe Informationsdichte und mausorientierte Bedienung ausgelegt.

## Fenster-Struktur

### Board-Ansicht

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile: [Board ▾]   Suchleiste   [Bearbeiten]   [Konto ▾]      │
├──────────────────────────────────────────────────────────────────────┤
│  Raster mit Widget-Kacheln                                           │
│  ┌───────────────┐ ┌───────────────────┐ ┌──────────────────────┐   │
│  │ App-Kachel    │ │ Docker-Status     │ │ Medien / Streams     │   │
│  │ Icon · Name   │ │ 8 running · 1 err │ │ 3 aktiv              │   │
│  ├───────────────┤ ├───────────────────┤ ├──────────────────────┤   │
│  │ Ampel 200 OK  │ │ Diagramm Traffic  │ │ Pi-hole 1 240 block.  │   │
│  └───────────────┘ └───────────────────┘ └──────────────────────┘   │
│  ┌───────────────────────────────┐  ┌──────────────────────────┐    │
│  │ Notiz / Markdown              │  │ JSON-Wert aus HTTP-Widget │    │
│  └───────────────────────────────┘  └──────────────────────────┘    │
├──────────────────────────────────────────────────────────────────────┤
│  Toast-Meldungen (unten) · Ladezustand je Kachel                     │
└──────────────────────────────────────────────────────────────────────┘
```

### Bearbeitungsmodus

```
┌──────────────────────────┬──────────────────────────────────────────┐
│  Panel: Widget-Bibliothek│  Raster mit Greifpunkten                 │
│  ┌────────────────────┐  │  ┌[⋮]───────[✎][⧉][✕]─────┐              │
│  │ Suche nach Widgets │  │  │ Kachel                  │              │
│  ├────────────────────┤  │  │  Resize-Ecke ↘          │              │
│  │ Struktur           │  │  └─────────────────────────┘              │
│  │  App · Text · Bild │  │  Ausrichtungslinien beim Ziehen          │
│  │ Status             │  │                                          │
│  │  Ampel · Container │  │  Board-Optionen (Spalten, Abstand)       │
│  │ Integration        │  │  [Vorschau] [Fertig]                     │
│  │  Docker · Medien   │  │                                          │
│  └────────────────────┘  │                                          │
└──────────────────────────┴──────────────────────────────────────────┘
```

### Einstellungsdialog (Overlay)

```
┌──────────────────────────────────────────────┐
│  Widget-Einstellungen                [✕]     │
├──────────────────────────────────────────────┤
│  [Allgemein] [Datenquelle] [Anzeige] [Aktionen]│
│  Feld · Auswahl · Schalter · Intervall        │
│  Ergebnisvorschau der Datenquelle             │
├──────────────────────────────────────────────┤
│  [Entfernen]        [Testen] [Abbrechen] [Speichern]│
└──────────────────────────────────────────────┘
```

## Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfzeile | Oben | Board-Auswahl, Suche, Bearbeiten, Konto-Menü |
| Raster | Mitte | Widget-Kacheln in Spalten und Zeilen |
| Widget-Kachel | Im Raster | Titelzeile, Icon, Inhalt, Aktionen, Ladezustand |
| Widget-Bibliothek | Links (Editor) | kategorisierte Kacheln zum Hineinziehen |
| Board-Einstellungen | Seitenpanel/Overlay | Layout, Aussehen, Freigaben, Endgeräte |
| Instanz-Verwaltung | Eigene Ansicht mit Seitenleiste | Nutzer, Gruppen, Integrationen, Auth, Lizenz |
| Toast-Meldungen | Unten | Erfolg, Fehler, Verbindungstests |
| Protokoll | Instanz-Verwaltung | Ereignisliste der Instanz |

## UI/UX

### Design-Prinzipien

- **Maus vor Tastatur**: alles Wesentliche ist klickbar, keine versteckten Kombinationen
- **Sofortwirkung**: Layoutänderungen greifen ohne Speichern-Knopf
- **Kuratierte Auswahl**: Widget-Bibliothek statt unendlicher Möglichkeiten

### Farbschema und Themes

- **Hell und Dunkel** plus Systemeinstellung, pro Konto umschaltbar
- **Akzentfarbe** und Deckkraft/Blur für Kacheln, Eckenradius und Schatten einstellbar
- **Hintergrundbilder** pro Board (Upload oder URL), mit Abblendung für Lesbarkeit
- **Globale Themes** (Administratoren) gelten als Vorgabe für alle Boards

### Interaktionen

- **Drag & Drop**: Kachel aus der Bibliothek ins Raster ziehen, Zielbereich wird hervorgehoben
- **Verschieben/Skalieren**: Greifpunkt und Ecke, Einrasten am Raster, Hilfslinien
- **Rechtsklick**: Kontextmenü an der Kachel (abschaltbar)
- **Hover**: leichte Aufhellung, schwebende Werkzeugleiste im Editor
- **Animationen**: kurze Übergänge beim Umsortieren, Skeleton-Platzhalter beim Laden, sanftes Einblenden neuer Kacheln
- **Dialog-Übergänge**: Overlay blendet ein, Fokus springt ins erste Feld
- **Vorschau**: Datenquellen zeigen eine Miniaturansicht der Antwort, bevor die Kachel gespeichert wird

### Responsive Design

- **Desktop**: volles Raster, Editor als festes Seitenpanel, Verwaltung mit Seitenleiste
- **Tablet**: reduzierte Spaltenzahl, Panels als Overlay
- **Mobil**: eigenes, getrennt speicherbares Layout; Navigation über Dropdown, Widgets stapeln untereinander
- **Touch**: langes Drücken nimmt eine Kachel auf, Skalieren über Ecken mit Fingeraufkommen
- **Schriftgrößen** bleiben auf kleinen Bildschirmen lesbar; Kopfzeile kollabiert zu Icon-Leiste

### Zugänglichkeit

- **Tastatur**: Dialoge, Formulare und Menüs per `Tab` erreichbar, `Esc` schließt Overlays
- **Fokusanzeige**: fokussierte Elemente sind deutlich markiert
- **Screenreader**: ARIA-Rollen für Dialoge, Menüs und Statusmeldungen
- **Farbunabhängigkeit**: Status zusätzlich über Symbol und Text erkennbar
- **Zoom**: Browser-Zoom ohne abgeschnittene Bedienelemente
- **Grenze**: reines Drag & Drop lässt sich nicht vollständig durch Tastaturbewegung ersetzen – für Feinarbeit bleibt die Maus nötig

### Performance

- **Abfrageintervalle** je Widget, nicht permanent; träge Integrationen bremsen nur ihre Kachel
- **Serverseitiger Abruf**: Anfragen laufen über die Instanz, Schlüssel bleiben dort, CORS entfällt
- **Bündelung und Caching**: identische Abfragen im Zeitfenster werden zusammengefasst
- **Skeleton-Ansichten** verhindern springende Layouts beim Nachladen
- **Empfehlung**: wenige, sinnvolle Integrations-Widgets statt vieler Status-Checks mit kurzen Intervallen; Diagramme mit großer Historie ausdünnen

## Siehe auch

- [menu.md](menu.md) - Menüpunkte nach Rolle
- [features.md](features.md) - Widgets und Integrationen
- [shortcuts.md](shortcuts.md) - Tastatursteuerung
- [api.md](api.md) - Schnittstelle und OIDC
