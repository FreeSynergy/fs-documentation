# Skeleton - Erscheinungsbild

## Grundlayout

```
Text:
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓

Listeneintrag:
○ ▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓

Card:
┌──────────────┐
│ ▓▓▓▓▓▓▓▓▓▓  │
│ ▓▓▓▓▓▓▓      │
└──────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **text** | abgerundete Balken in Zeilenhöhe |
| **rect** | Fläche mit `round`-Ecken |
| **circle** | Kreis in der `size` |
| **card** | mehrere Rechtecke in Card-Anordnung |
| **list-item** | Kreis links, Balken rechts |
| **table-row** | Balken pro Spalte, Breite folgt der Spaltenbreite |
| **avatar** | Kreis plus zwei Balken |

## Größen

Breite und Höhe kommen aus den Attributen. Ist keines gesetzt, gilt die Größe der
Zielkomponente. Textbalken folgen der Größenskala:

| Größe | Zeilenhöhe |
|-------|------------|
| `small` | 14 px |
| `medium` | 18 px |
| `large` | 24 px |

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Fläche | neutrale Fläche, im hellen Theme grau, im dunklen heller |
| `shimmer` | ein hellerer Streifen läuft über die Fläche |
| `pulse` | die Fläche atmet zwischen zwei Deckkraft-Stufen |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| – | keine. Ein Skeleton ist nicht bedienbar. |

## Responsiv

- Skeletons übernehmen die responsive Breite des übergeordneten Bereichs.
- Mit `prefers-reduced-motion` wird die Animation zu `none`. Die Fläche bleibt statisch.
