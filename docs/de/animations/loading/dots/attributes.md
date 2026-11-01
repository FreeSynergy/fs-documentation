# Dots - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `dots` | Name der Animation |
| `anzahl` | number | `3` | Anzahl der Punkte |
| `onAnimateStart` | function | - | Wird beim Start ausgeführt |
| `onAnimateEnd` | function | - | Wird beim Stoppen ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `1400` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | weiches An- und Abschwellen |
| `delay` | number | `150` | Anzeigeverzögerung, um Flackern zu vermeiden |
| `iterationCount` | number \| `infinite` | `infinite` | läuft bis zum Ladeende |
| `playState` | string | `running` | `paused` blendet die Punkte aus, ohne den Zustand zu löschen |

## Punkte-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `dotSize` | number | `6` | Punktdurchmesser in px |
| `dotSpacing` | number | `6` | Abstand zwischen den Punkten in px |
| `offsetProPunkt` | number | `160` | Zeitversatz der Punkte innerhalb eines Zyklus in ms |
| `hub` | number | `4` | Hubhöhe beim Heben in px |
| `modus` | string | `bounce` | `bounce`, `fade` oder `scale` |
| `farbe` | string | `sekundaer` | Punktfarbe, folgt dem Theme |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | `Lädt` | Beschreibung für Screenreader |
| `aria-live` | string | `polite` | Bereich, der den Ladezustand ansagt |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `static` | Punkte stehen still statt zu pulsieren |
