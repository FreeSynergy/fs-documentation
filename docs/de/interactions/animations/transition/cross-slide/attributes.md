# Cross Slide - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `animation` | string | `cross-slide` | Name der Animation |
| `altesElement` | node | - | das Element, das die Fläche verlässt |
| `neuesElement` | node | - | das Element, das hereinkommt |
| `onTransitionEnd` | function | - | Wird ausgeführt, nachdem der Tausch abgeschlossen ist |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `280` | Dauer des Tauschs in ms |
| `timingFunction` | string | `ease-in-out` | beide Elemente bewegen sich symmetrisch |
| `delay` | number | `0` | Verzögerung vor dem Start in ms |
| `iterationCount` | number \| `infinite` | `1` | ein einmaliger Tausch |

## Richtungsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `richtung` | string | `left` | `left`, `right`, `up`, `down` |
| `distanz` | string | `100%` | zurückgelegter Weg, meist die volle Breite; auch in px möglich |
| `anteilUeberlappung` | number | `1` | 1 = beide bewegen sich gleichzeitig, 0 = nacheinander |
| `deckkraftAmRand` | number | `1` | optionales Ausblenden an den Rändern während des Gleitens |
| `abgeschnitten` | boolean | `true` | Elemente außerhalb der Fläche sind nicht sichtbar |
| `nurNeues` | boolean | `false` | stattdessen verschwindet das alte Element per Fade Out |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `aria-live` | string | `polite` | den Wechsel des Inhalts ansagen |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `cross-fade` | Ersatz: Überblenden statt Gleiten |
