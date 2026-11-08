# Flip - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `onAnimateStart` | function | - | Wird ausgeführt, wenn die Drehung beginnt |
| `onContentSwap` | function | - | Wird beim Drehwinkel von 90° ausgeführt (Seitenwechsel) |
| `onAnimateEnd` | function | - | Wird ausgeführt, nachdem die Rückseite zur Ruhe gekommen ist |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `450` | Dauer der Drehung in ms |
| `timingFunction` | string | `ease-in-out` | sanfter Start und sanftes Ende |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `forwards` | die Rückseite bleibt nach der Drehung stehen |

## Achsen- und Perspektivattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `axis` | string | `y` | Drehachse: `y` = links/rechts drehen, `x` = oben/unten kippen |
| `angle` | number | `180` | Drehwinkel in Grad (der Standard zum Seitenwechsel) |
| `perspective` | number | `1000` | Perspektive in px; `0` = eine flache 2D-Drehung ohne 3D |
| `backfaceVisibility` | string | `hidden` | Rückseite erst ab 90° zeigen (`hidden`) oder mitdrehen (`visible`) |
| `flipState` | string | `front` | die aktuelle Seite: `front` oder `back` |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `swap` – den Inhalt ohne Drehung tauschen |
