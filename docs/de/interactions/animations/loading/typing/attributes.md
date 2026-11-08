# Typing - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aktiv` | boolean | `false` | Indikator ein- oder ausblenden |
| `punktzahl` | number | `3` | Anzahl der Punkte oder Balken |
| `wellenform` | string | `welle` | `welle`, `blinken`, `huepfen` |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `1200` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | sanftes Anheben und Absenken |
| `iterationCount` | number \| `infinite` | `infinite` | läuft, solange `aktiv` gesetzt ist |
| `delay` | number | `0` | verzögert den Start nach dem Tippereignis |

## Typing-Attribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `dotSize` | number | `6` | Durchmesser eines Punktes in px |
| `punktAbstand` | number | `8` | Abstand zwischen den Punkten in px |
| `farbe` | string | `muted` | Farbe der Punkte, passend zum Chat-Theme |
| `sprechblase` | boolean | `true` | Punkte in einer Blase über dem Eingabefeld zeigen |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
