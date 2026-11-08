# Parallax - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `parallax` | boolean | `true` | Parallax für den Container aktivieren |
| `ebenen` | array | - | Ebenen, von hinten nach vorn sortiert |
| `trigger` | string | `scroll` | `scroll`, `zeiger` oder `gyroskop` |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `200` | Nachzieh-Zeit bei Sprüngen (Anker, Ende) |
| `timingFunction` | string | `ease-out` | ein sanftes Auslaufen nach dem Stoppen des Scrollens |

## Ebenenattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `faktorProEbene` | array | `[0.2, 0.5, 1]` | 0 = steht still, 1 = normale Geschwindigkeit |
| `achse` | string | `y` | `x`, `y` oder `beide` |
| `maxAusschlag` | number | `0` | Grenze des Ebenenversatzes in px (0 = frei) |
| `tiefe` | number | `0` | ein zusätzlicher 3D-Versatz über Perspektive in px |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
