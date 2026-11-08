# Dots - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | string | `dots` | Name der Animation |
| `anzahl` | number | `3` | Anzahl der Punkte |
| `onAnimateStart` | function | - | Wird am Anfang ausgeführt |
| `onAnimateEnd` | function | - | Wird ausgeführt, wenn die Animation stoppt |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `1400` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | sanftes Anschwellen und Ausblenden |
| `delay` | number | `150` | Verzögerung der Anzeige, um Flackern zu vermeiden |
| `iterationCount` | number \| `infinite` | `infinite` | läuft, bis das Laden endet |
| `playState` | string | `running` | `paused` blendet die Punkte aus, ohne den Zustand zu löschen |

## Punktattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `dotSize` | number | `6` | Durchmesser eines Punktes in px |
| `dotSpacing` | number | `6` | Abstand zwischen den Punkten in px |
| `offsetProPunkt` | number | `160` | Zeitversatz der Punkte innerhalb eines Zyklus in ms |
| `hub` | number | `4` | Hubhöhe beim Steigen in px |
| `modus` | string | `bounce` | `bounce`, `fade` oder `scale` |
| `farbe` | string | `sekundaer` | Farbe der Punkte, folgt dem Theme |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | `Loading` | Beschreibung für Screenreader |
| `aria-live` | string | `polite` | Bereich, der den Ladezustand ansagt |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `static` | Die Punkte stehen still, statt zu pulsieren |
