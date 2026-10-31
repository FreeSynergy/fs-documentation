# Parallax - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `parallax` | boolean | `true` | Parallax für den Container aktivieren |
| `ebenen` | array | - | Ebenen, von hinten nach vorne geordnet |
| `trigger` | string | `scroll` | `scroll`, `zeiger` oder `gyroskop` |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `200` | Nachziehzeit bei Sprüngen (Anker, Ende) |
| `timingFunction` | string | `ease-out` | weiches Auslaufen nach Scroll-Stopp |

## Ebenen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `faktorProEbene` | array | `[0.2, 0.5, 1]` | 0 = steht still, 1 = normale Geschwindigkeit |
| `achse` | string | `y` | `x`, `y` oder `beide` |
| `maxAusschlag` | number | `0` | Grenze des Ebenenversatzes in px (0 = frei) |
| `tiefe` | number | `0` | zusätzlicher 3D-Versatz über Perspective in px |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
