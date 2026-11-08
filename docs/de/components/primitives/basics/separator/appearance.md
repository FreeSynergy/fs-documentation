# Separator – Erscheinungsbild

## Grundlayout

```
horizontal:
──────────────────────────────

mit-beschriftung:
────────────  oder  ────────────

vertical:
┌──────────┐ │ ┌──────────┐
│ Gruppe A │ │ │ Gruppe B │
└──────────┘ │ └──────────┘
```

## Varianten

| Variante | Erscheinungsbild |
|---------|------------|
| **horizontal** | 1 px Linie in einer neutralen Trennfarbe |
| **vertical** | 1 px Linie, Höhe = Zeilenhöhe der Nachbarn |
| **mit-beschriftung** | zwei Linienstücke mit Text dazwischen |
| **dekorativ** | dieselbe Linie, oft stärker (2 px) und in der Themenfarbe |
| **inset** | eingerückt um die Breite der Icon-Spalte der Liste |

## Größen

| Größe | Linienstärke |
|------|-------------|
| `small` | 1 px |
| `medium` | 1 px |
| `large` | 2 px |

## Farben und Zustände

| Teil | Farbe |
|------|------|
| Linie (neutral) | Trennfarbe, helles Grau im hellen Theme, dunkler im dunklen |
| Beschriftung | Sekundärtext |
| dekorativ | Themen-Akzent möglich |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|-------------|
| – | keine; ein Separator ist nicht bedienbar |

## Responsiv

- Wenn Leisten umbrechen, wird ein `vertical`-Separator zu `horizontal`.
