# Skeleton (Platzhalter) - Aussehen

## Grundlayout

```
text:
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓

list-item:
○ ▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓

card:
┌──────────────┐
│ ▓▓▓▓▓▓▓▓▓▓  │
│ ▓▓▓▓▓▓▓      │
└──────────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **text** | abgerundete Balken in Zeilenhöhe |
| **rect** | Fläche mit `round`-Ecken |
| **circle** | Kreis in `size` |
| **card** | mehrere Rechtecke in Kartenanordnung |
| **list-item** | Kreis links, Balken rechts |
| **table-row** | Balken je Spalte, Breite nach Spaltenbreite |
| **avatar** | Kreis plus zwei Balken |

## Größen

Breite und Höhe kommen aus den Attributen; ohne Angabe gilt die Größe der
Zielkomponente. Textbalken folgen dem Größen-Raster:

| Größe | Zeilenhöhe |
|-------|------------|
| `small` | 14 px |
| `medium` | 18 px |
| `large` | 24 px |

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Fläche | neutrale Fläche, im hellen Theme grau, im dunklen heller |
| `shimmer` | heller Streifen wandert über die Fläche |
| `pulse` | Fläche atmet zwischen zwei Deckkraftstufen |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| – | keine; ein Skeleton ist nicht bedienbar |

## Reaktiv

- Skeletons erben die responsive Breite des Elternbereichs.
- Bei `prefers-reduced-motion` Animation auf `none`; die Fläche bleibt statisch.
