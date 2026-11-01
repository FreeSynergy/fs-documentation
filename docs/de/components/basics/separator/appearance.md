# Separator (Trennlinie) - Aussehen

## Grundlayout

```
horizontal:
──────────────────────────────

mit-beschriftung:
────────────  oder  ───────────

vertical:
┌──────────┐ │ ┌──────────┐
│ Gruppe A │ │ │ Gruppe B │
└──────────┘ │ └──────────┘
```

## Varianten

| Variante | Aussehen |
|----------|----------|
| **horizontal** | 1 px Linie in neutraler Trennfarbe |
| **vertical** | 1 px Linie, Höhe = Zeilenhöhe der Nachbarn |
| **mit-beschriftung** | zwei Linienabschnitte mit Text dazwischen |
| **dekorativ** | gleiche Linie, oft stärker (2 px) und in Theme-Farbe |
| **inset** | Einzug so breit wie die Icon-Spalte der Liste |

## Größen

| Größe | Linienstärke |
|-------|--------------|
| `small` | 1 px |
| `medium` | 1 px |
| `large` | 2 px |

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Linie (neutral) | Trennfarbe, im hellen Theme hellgrau, im dunklen dunkler |
| Beschriftung | Sekundärtext |
| dekorativ | Theme-Akzent möglich |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| – | keine; ein Separator ist nicht bedienbar |

## Reaktiv

- Bei Umbruch von Leisten wird ein `vertical`-Separator zu `horizontal`.
