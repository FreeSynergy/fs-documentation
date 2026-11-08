# Empty State - Erscheinungsbild

## Grundlayout

```
        ┌───────────────────────────────┐
        │                               │
        │            ▤                  │  Icon 48 px, gedämpfte Farbe
        │   Noch keine Aufgaben         │  ein Satz, 15 px
        │  [ Erste Aufgabe anlegen ]    │  Primärbutton
        │   Tastatur: Strg N            │  optional, gedämpft
        │                               │
        └───────────────────────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **leer** | neutrales Icon, Aktion in der Primärfarbe |
| **kein-treffer** | Suchicon, der Text nennt den Suchbegriff |
| **fehler** | Icon in der Fehlerfarbe, Aktion „Erneut versuchen“ |

## Größen

| Größe | Icon | Textbreite | Mindesthöhe |
|-------|------|------------|-------------|
| `small` | 32 px | 320 px | 120 px |
| `medium` | 48 px | 420 px | 200 px |
| `large` | 72 px | 520 px | 320 px |

## Farben und Zustände

| Zustand | Erscheinungsbild |
|---------|------------------|
| `default` | Icon und Text gedämpft, Aktion farbig |
| `hover` | nur die Aktion reagiert (tone) |
| `loading` | ein Skeleton statt Text und Aktion |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `tone` | wie beim [Button](../../actions/button/) |
| `fade-in` | blendet ein, wenn die Liste leer wird |

## Responsiv

- Auf schmalen Flächen stapeln sich Icon, Text und Aktion. Die Breite ist höchstens 90 %.
- Der Text umbricht auf höchstens drei Zeilen.
