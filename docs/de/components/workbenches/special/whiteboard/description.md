# Whiteboard

| Feld | Wert |
| ------ | ------ |
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `zeichnung`, `formen`, `notizen`, `vorlage` |
| **States** | `gemeinsam`, `offline` |
| **Gestures** | `drag`, `tap`, `double-tap`, `pinch`, `spread` |
| **Animations** | `highlight`, `fade-in` |
| **Related** | `rich-text-editor`, `image`, `map-view`, `dashboard` |
| **Status** | documented |

## Beschreibung
Ein Whiteboard ist eine Zeichenfläche für die Zusammenarbeit.

## Zweck

- Brainstorming
- Planung
- Zusammenarbeit

## Varianten

| Variante | Beschreibung |
| ---------- | -------------- |
| **zeichnung** | freies Zeichnen mit Stift und Radiergummi |
| **formen** | Rechtecke, Pfeile und Verbinder, mit Einrasten |
| **notizen** | Haftnotizen als Karten auf der Fläche |
| **vorlage** | vorbereitete Fläche (Raster, Spalten, Swimlanes) |

## Funktionen

- Zeichnen
- Formen
- Text
- Schablonen
- Rückgängig/Wiederholen
- Export
- Zusammenarbeit

## Abgrenzung

- **Nicht verwechseln mit** [rich-text-editor](../../fields/rich-text-editor/): Dort entsteht
  Text, hier eine Fläche.
- **Nicht verwechseln mit** [map-view](../../../widgets/special/map-view/): Die Zeichenfläche hat keinen geografischen Bezug.
- **Nicht verwechseln mit** [gallery](../../../widgets/media/gallery/): Ein Whiteboard erzeugt Inhalte,
  eine Galerie zeigt vorhandene Inhalte.

## Best Practices

- Fläche ohne harte Grenze, der Anzeigebereich wird verwaltet; ein optionales Raster hilft beim Ausrichten.
- Rückgängig/Wiederholen gehört zum Whiteboard – auch nach gemeinsamer Bearbeitung.
- Beim Zusammenarbeiten sind die Zeiger der anderen Personen sichtbar und durch Farbe unterscheidbar.
- Formen rasten ein und zeigen Ausrichtungshilfen, sonst bleibt nichts lesbar.
- Als Bild **und** als bearbeitbare Daten exportieren, damit die Arbeit später weitergehen kann.

## Siehe auch

- [special – Übersicht](../index.md)
- [Rich Text Editor](../../fields/rich-text-editor/) — Text statt Fläche
- [Map View](../../../widgets/special/map-view/) — Fläche mit geografischem Bezug
- [Basiskomponente](../../../primitives/basics/base.md)
