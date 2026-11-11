# Whiteboard

| Feld | Wert |
| ------ | ------ |
| **Kategorie** | `special` |
| **Erbt von** | `base` |
| **Varianten** | `zeichnung`, `formen`, `notizen`, `vorlage` |
| **Zustände** | `gemeinsam`, `offline` |
| **Gesten** | `drag`, `tap`, `double-tap`, `pinch`, `spread` |
| **Animationen** | `highlight`, `fade-in` |
| **Verwandt** | `rich-text-editor`, `image`, `map-view`, `dashboard` |
| **Status** | dokumentiert |

## Beschreibung
Ein Whiteboard ist eine Zeichenfläche für die Zusammenarbeit.

## Verwendungszweck
- Brainstorming
- Planung
- Zusammenarbeit

## Varianten

| Variante | Beschreibung |
| ---------- | -------------- |
| **zeichnung** | freies Zeichnen mit Stift und Radierer |
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

- **Nicht verwechseln mit** [rich-text-editor](../../fields/rich-text-editor/): dort entsteht Text,
  hier eine Fläche.
- **Nicht verwechseln mit** [map-view](../../../widgets/special/map-view/): die Zeichenfläche hat keinen geografischen Bezug.
- **Nicht verwechseln mit** [gallery](../../../widgets/media/gallery/): ein Whiteboard erzeugt Inhalte,
  eine Galerie zeigt vorhandene Inhalte.

## Best Practices

- Fläche ohne harte Grenze, der Viewport wird verwaltet; ein optionales Raster hilft beim
  Ausrichten.
- Rückgängig/Wiederholen gehört zum Whiteboard – auch nach gemeinsamer Bearbeitung.
- Bei gemeinsamer Arbeit sind die Zeiger der anderen Personen sichtbar und durch Farbe unterscheidbar.
- Formen rasten ein und zeigen Ausrichtungshilfen, sonst bleibt nichts lesbar.
- Als Bild **und** als bearbeitbare Daten exportieren, damit die Arbeit später weitergehen kann.

## Siehe auch

- [special – Übersicht](../index.md)
- [Rich-Text-Editor](../../fields/rich-text-editor/) — Text statt Fläche
- [Kartenansicht](../../../widgets/special/map-view/) — Fläche mit geografischem Bezug
- [Basiskomponente](../../../primitives/basics/base.md)
