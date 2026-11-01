# Empty State (Leerer Zustand) - Aussehen

## Grundlayout

```
        ┌───────────────────────────────┐
        │                               │
        │            ▤                  │  Icon 48 px, gedämpfte Farbe
        │   Noch keine Aufgaben         │  ein Satz, 15 px
        │   [ Erste Aufgabe anlegen ]   │  primary-Button
        │   Tastatur: Strg N            │  optional, gedämpft
        │                               │
        └───────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **leer** | Icon neutral, Aktion in Primärfarbe |
| **kein-treffer** | Such-Icon, Text nennt den Suchbegriff |
| **fehler** | Icon in Fehlerfarbe, Aktion „Erneut versuchen“ |

## Größen

| Größe | Icon | Textbreite | Mindesthöhe |
|-------|------|------------|-------------|
| `small` | 32 px | 320 px | 120 px |
| `medium` | 48 px | 420 px | 200 px |
| `large` | 72 px | 520 px | 320 px |

## Farben und Zustände

| Zustand | Aussehen |
|---------|----------|
| `default` | Icon und Text gedämpft, Aktion farbig |
| `hover` | nur die Aktion reagiert (Ton) |
| `loading` | Skeleton anstelle von Text und Aktion |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `tone` | wie beim [button](../../actions/button/) |
| `fade-in` | Einblenden, wenn die Liste leer wird |

## Reaktiv

- Auf schmalen Flächen stapeln sich Icon, Text und Aktion; Breite maximal 90 %.
- Der Text bricht in maximal drei Zeilen um.
