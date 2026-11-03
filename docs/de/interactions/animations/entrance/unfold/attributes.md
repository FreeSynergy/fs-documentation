# Unfold - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `unfold` | Name der Animation |
| `foldOrigin` | string | `top` | Knickkante: `top`, `bottom`, `left`, `right` |
| `startAngle` | number | `-90` | Ausgangswinkel in Grad (90 = kantig) |
| `endAngle` | number | `0` | Zielwinkel in Grad (liegende Ebene) |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `450` | Dauer in ms |
| `timingFunction` | string | `ease-out` | schwungvoller Start, weiches Ende |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `both` | geklappter Startzustand auch vor dem Start |
| `onAnimateEnd` | function | - | Wird nach dem vollständigen Aufklappen ausgeführt |

## Falt-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `perspective` | number | `800` | Kameraabstand in px (kleiner = stärkerer 3D-Effekt) |
| `segments` | number | `1` | Anzahl Falze (mehrere Segmente = wellenförmig) |
| `segmentStagger` | number | `60` | Versatz der Segmente in ms |
| `backfaceVisible` | boolean | `false` | Rückseite während des Schwenks sichtbar? |
| `shadow` | string | `auto` | Wandernder Schatten während des Klappens |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `fallbackAnimation` | string | `expand` | Ersatz ohne 3D-Drehung |
