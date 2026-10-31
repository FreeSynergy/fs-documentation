# Flip - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start der Drehung ausgeführt |
| `onContentSwap` | function | - | Wird am Drehwinkel 90° ausgeführt (Seitenwechsel) |
| `onAnimateEnd` | function | - | Wird nach dem Stillstand der Rückseite ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `450` | Dauer der Drehung in ms |
| `timingFunction` | string | `ease-in-out` | Sanfter Start und sanftes Stoppen |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Rückseite bleibt nach der Drehung stehen |

## Achsen- und Perspektiv-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `axis` | string | `y` | Drehachse: `y` = links/rechts drehen, `x` = oben/unten kippen |
| `angle` | number | `180` | Drehwinkel in Grad (Standard für den Seitenwechsel) |
| `perspective` | number | `1000` | Perspektive in px; `0` = flache 2D-Drehung ohne 3D |
| `backfaceVisibility` | string | `hidden` | Rückseite erst ab 90° zeigen (`hidden`) oder mitdrehen (`visible`) |
| `flipState` | string | `front` | Aktuelle Seite: `front` oder `back` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `swap` – Inhalte ohne Drehung tauschen |
