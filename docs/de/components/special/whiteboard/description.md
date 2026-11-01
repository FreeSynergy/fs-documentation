# Whiteboard (Whiteboard)

| Feld | Wert |
|------|------|
| **Kategorie** | `special` |
| **Erbt von** | `base` |
| **Varianten** | `zeichnung`, `formen`, `notizen`, `vorlage` |
| **Zustände** | `gemeinsam`, `offline` |
| **Gesten** | `drag`, `tap`, `double-tap`, `pinch`, `spread` |
| **Animationen** | `highlight`, `fade-in` |
| **Verwandt** | `rich-text-editor`, `image`, `map-view`, `dashboard` |
| **Status** | dokumentiert |

## Beschreibung
Ein Whiteboard ist eine Zeichenfläche für Kollaboration.

## Verwendungszweck

- Brainstorming
- Planung
- Kollaboration

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **zeichnung** | freies Zeichnen mit Stift und Radierer |
| **formen** | Rechtecke, Pfeile und Verbinder, einrastend |
| **notizen** | Notizzettel als Karten auf der Fläche |
| **vorlage** | vorbereitete Fläche (Raster, Spalten, Ablaufschienen) |

## Features

- Drawing
- Shapes
- Text
- Stencils
- Undo/Redo
- Export
- Collaboration

## Abgrenzung

- **Nicht verwechseln mit** [rich-text-editor](../../fields/rich-text-editor/): dort entsteht
  Text, hier eine Fläche.
- **Nicht verwechseln mit** [map-view](../map-view/): die Zeichenfläche hat keinen Geo-Bezug.
- **Nicht verwechseln mit** [gallery](../../media/gallery/): ein Whiteboard erzeugt Inhalte,
  eine Galerie zeigt vorhandene.

## Best Practices

- Fläche ohne harte Grenze, der Ausschnitt wird verwaltet; ein optionales Raster hilft beim
  Ausrichten.
- Rückgängig/Wiederholen gehört zum Whiteboard dazu — auch nach gemeinsamer Bearbeitung.
- Bei gemeinsamer Arbeit sind die Zeiger der anderen sichtbar und farbig unterscheidbar.
- Formen rasten ein und zeigen Ausrichtungslinien, sonst wird nichts lesbar.
- Export als Bild **und** als bearbeitbare Daten, damit später weitergearbeitet werden kann.

## Siehe auch

- [special – Übersicht](../index.md)
- [Rich Text Editor](../../fields/rich-text-editor/) — Text statt Fläche
- [Map View](../map-view/) — Fläche mit Geo-Bezug
- [Basiskomponente](../../basics/base/)
