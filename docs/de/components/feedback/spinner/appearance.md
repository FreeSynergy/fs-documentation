# Spinner (Ladeanzeige) - Aussehen

## Grundlayout

```
einfach:          mit-text:              inline:
   ◌              ◌  Wird geladen…       Text … ◌
```

Der Ring besteht aus einem offenen Kreis, dessen vorderes Segment rotiert.

## Varianten

| Variante | Aussehen |
|----------|----------|
| **einfach** | offener Ring, ein Segment in Primärfarbe |
| **mit-text** | links Spinner, rechts Text in Sekundärfarbe |
| **inline** | Ring auf Schriftzhöhe, ohne Zusatzabstand |

## Größen

| Größe | Durchmesser | Ringstärke |
|-------|-------------|------------|
| `small` | 16 px | 2 px |
| `medium` | 24 px | 3 px |
| `large` | 40 px | 4 px |

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| Rotierendes Segment | Primärfarbe |
| `track` (Hintergrundring) | neutrale Spur, 30 % Deckkraft |
| Begleittext | Sekundärfarbe |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| – | keine; ein Spinner ist nicht bedienbar |

## Reaktiv

- Bei reduzierter Bewegung (`prefers-reduced-motion`) wird die Drehung durch
  ein pulsierendes Segment ersetzt.
