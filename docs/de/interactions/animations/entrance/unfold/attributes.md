# Unfold - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | string | `unfold` | Name der Animation |
| `foldOrigin` | string | `top` | Falzkante: `top`, `bottom`, `left`, `right` |
| `startAngle` | number | `-90` | Startwinkel in Grad (90 = hochkant) |
| `endAngle` | number | `0` | Zielwinkel in Grad (flach liegend) |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `450` | Dauer in ms |
| `timingFunction` | string | `ease-out` | schwungvoller Start, weiches Ende |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `fillMode` | string | `both` | der gefaltete Startzustand gilt auch vor dem Start |
| `onAnimateEnd` | function | - | Wird ausgeführt, nachdem das Element vollständig entfaltet ist |

## Falzattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `perspective` | number | `800` | Kameraabstand in px (kleiner = stärkerer 3D-Effekt) |
| `segments` | number | `1` | Anzahl der Falze (mehrere Segmente = wellenförmig) |
| `segmentStagger` | number | `60` | Versatz der Segmente in ms |
| `backfaceVisible` | boolean | `false` | Ist die Rückseite während des Schwingens sichtbar? |
| `shadow` | string | `auto` | mitlaufender Schatten beim Entfalten |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `fallbackAnimation` | string | `expand` | Ersatz ohne die 3D-Drehung |
