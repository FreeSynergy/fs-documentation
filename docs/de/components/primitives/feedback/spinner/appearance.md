# Spinner - Erscheinungsbild

## Grundlayout

```
einfach:          mit-text:               inline:
   ◌              ◌  Lädt…                Text … ◌
```

Der Ring besteht aus einem offenen Kreis, dessen vorderes Segment sich dreht.

## Varianten

| Variante | Erscheinungsbild |
|----------|------------------|
| **einfach** | offener Ring, ein Segment in der Primärfarbe |
| **mit-text** | Spinner links, Text in der Sekundärfarbe rechts |
| **inline** | Ring in Texthöhe, ohne zusätzlichen Abstand |

## Größen

| Größe | Durchmesser | Ringstärke |
|-------|-------------|------------|
| `small` | 16 px | 2 px |
| `medium` | 24 px | 3 px |
| `large` | 40 px | 4 px |

## Farben und Zustände

| Teil | Farbe |
|------|-------|
| drehendes Segment | Primärfarbe |
| `track` (Hintergrundring) | neutrale Spur, 30 % Deckkraft |
| begleitender Text | Sekundärfarbe |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| – | keine. Ein Spinner ist nicht bedienbar. |

## Responsiv

- Bei reduzierter Bewegung (`prefers-reduced-motion`) wird die Drehung durch
  ein pulsierendes Segment ersetzt.
