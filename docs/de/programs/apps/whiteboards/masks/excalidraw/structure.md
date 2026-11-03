# Excalidraw - Struktur & UI/UX

## Übersicht

Excalidraw zeigt genau eine Fläche: einen unendlichen Canvas. Bedienelemente liegen als schmale Leiste und ein-/ausklappbare Panels darüber. Im View-Modus für Lesende verschwindet die gesamte Bearbeitungsoberfläche.

## Fenster-Struktur

### Bearbeitungsansicht

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile: Hauptmenü | Werkzeuge | Rückgängig/Zoom | Kollaboration  │
├────────────┬──────────────────────────────────────────┬──────────────┤
│ Eigenschaften│                                       │ Bibliothek   │
│ (nur bei     │        Unendlicher Canvas              │ (rechts,     │
│ Auswahl)     │   [Elemente, Cursors der Teilnehmenden]│  einklappbar)│
│ - Linie      │                                        │ - eigene     │
│ - Füllung    │                                        │   Sammlungen │
│ - Deckkraft  │                                        │ - öffentliche│
│ - Schrift    │                                        │              │
├────────────┴──────────────────────────────────────────┴──────────────┤
│  Optional: Hilfe-Fenster, Statistik (Elemente, FPS), Zoom-Anzeige    │
└──────────────────────────────────────────────────────────────────────┘
```

### Panel-Bereiche

| Bereich | Position | Inhalt |
|---------|----------|--------|
| Kopfzeile | oben | Hauptmenü, Werkzeugpalette, Undo/Redo, Zoom, Kollaboration |
| Eigenschaften-Panel | links (nur bei Auswahl) | Farben, Strich, Füllung, Text, Ebenen |
| Bibliotheks-Panel | rechts | Formensammlungen, Import/Export |
| Canvas | Mitte | freie Zeichenfläche, unendlich groß |
| Hilfe/Statistik | Einblendungen | Shortcuts-Übersicht, Performance-Werte |

## UI/UX

### Design-Prinzipien

- **Canvas zuerst**: Werkzeuge treten hinter die Zeichenfläche zurück
- **Wenig Auswahl**: neun Grundwerkzeuge statt voller Menübäume
- **Direktmanipulation**: alles wird durch Ziehen, Klicken und Tippen geändert
- **Skizzen-Ästhetik**: handgezeichnete Linien (Rough.js) nehmen Bewertungsdruck aus Entwürfen

### Farbschema und Themes

- **Hell**: weiße Zeichenfläche, dunkle Linien (`#1e1e1e` als Standard-Stiftfarbe)
- **Dunkel**: dunkle Zeichenfläche, angepasste Elementfarben (Umschaltbar im Hauptmenü)
- **Elementpalette**: gedämpfte Standardfarben für Strich und Füllung, frei wählbar im Panel
- **Schrift**: handgezeichnete Standardschrift, zusätzlich normale und Monospace-Schrift

### Interaktionen

- **Zeichnen**: Werkzeug wählen, auf dem Canvas ziehen; Auswahlrahmen mit Eckenpunkten
- **Shift**: winkeltreues Zeichnen und proportionales Skalieren
- **Alt+Ziehen**: Klonen; **Doppelklick**: Text bearbeiten
- **Zoomen**: scrollen oder Leiste; Zoom folgt dem Cursor
- **Cursors**: farbige Namen der Teilnehmenden bewegen sich weich mit
- **Animationen**: kurze Einblend-Impulse beim Erstellen, sanfte Zoom-Übergänge; keine schweren Animationen

### Responsives Verhalten

- **Desktop**: volle Panels und Werkzeugpalette
- **Tablet/Touch**: Zeichengesten mit Stift oder Finger, Pinch-Zoom, Panels über Symbole
- **Smartphone**: kompakte Leiste, eingeschränkte Panel-Nutzung; Zeichnen bleibt vollständig möglich

### Lese-/View-Modus

```
┌──────────────────────────────────────────────────────────────────────┐
│  Kopfzeile: Titel | Zoom | Kollaboration (nur ansehen)               │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│        Canvas (Elemente fixiert, Verschieben und Zoomen erlaubt)     │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

- Keine Werkzeugpalette, kein Eigenschaften-Panel, kein Bibliotheks-Panel
- Teilnehmende sehen weiterhin die Cursors der anderen

### Mobile Ansicht (Kompaktlayout)

```
┌────────────────────────────────┐
│ Menü | Auswahl | Undo | Teilen │
├────────────────────────────────┤
│                                │
│   Canvas (Stift- und           │
│   Touch-Zeichnen)              │
│                                │
├────────────────────────────────┤
│ Werkzeuge (Symbolleiste unten) │
└────────────────────────────────┘
```

### Typography

- **Elemente**: handgezeichnete Standardschrift für alle Beschriftungen
- **Oberfläche**: neutrale Systemschrift für Panels und Menüs
- **Größen**: vier Schriftstufen für Texte, umschaltbar über Panel oder Tastenziffern

## Zugänglichkeit

- **Tastatur**: Werkzeugwahl und die meisten Aktionen sind per Shortcuts erreichbar
- **Screenreader**: eingeschränkt — Inhalte liegen als gezeichnete Elemente vor, nicht als semantischer Text
- **Kontrast**: Standardfarben sind kontrastreich; Elementfarben frei anpassbar
- **Hinweis**: Für barrierefreie Alternativen Text-Export (SVG enthält Textelemente) nutzen

## Performance

- **Canvas-Rendering**: nur geänderte Bereiche werden neu gezeichnet; große Szenen mit tausenden Elementen bleiben flüssig
- **Kollaboration**: es werden nur Element-Differenzen (mit `version`) übertragen, nicht die ganze Szene
- **Bild-Größen**: eingefügte Bilder werden komprimiert gespeichert (in `files` der Szene)
- **Statistik-Fenster**: zeigt Elementanzahl und FPS zur Diagnose an
- **Selbst-Hosted**: Leistung hängt vom Kollaborationsserver ab; Räume ohne Persistenz sind leichter
