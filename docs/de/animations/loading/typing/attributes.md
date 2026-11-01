# Typing - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aktiv` | boolean | `false` | Indikator ein-/ausblenden |
| `punktzahl` | number | `3` | Anzahl Punkte bzw. Balken |
| `wellenform` | string | `welle` | `welle`, `blinken`, `huepfen` |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `1200` | Dauer eines Zyklus in ms |
| `timingFunction` | string | `ease-in-out` | weiches Heben und Senken |
| `iterationCount` | number \| `infinite` | `infinite` | läuft, solange `aktiv` ist |
| `delay` | number | `0` | Start nach dem Tipp-Ereignis verzögern |

## Typing-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `dotSize` | number | `6` | Durchmesser eines Punktes in px |
| `punktAbstand` | number | `8` | Abstand zwischen den Punkten in px |
| `farbe` | string | `muted` | Punktfarbe, passend zum Chat-Thema |
| `sprechblase` | boolean | `true` | Punkte in Blase über dem Eingabefeld anzeigen |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
