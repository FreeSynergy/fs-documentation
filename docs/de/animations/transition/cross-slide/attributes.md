# Cross Slide - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `cross-slide` | Name der Animation |
| `altesElement` | node | - | Element, das die Fläche verlässt |
| `neuesElement` | node | - | Element, das hineinkommt |
| `onTransitionEnd` | function | - | Wird nach dem vollständigen Tausch ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `280` | Dauer des Tauschs in ms |
| `timingFunction` | string | `ease-in-out` | beide Elemente bewegen sich symmetrisch |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `iterationCount` | number \| `infinite` | `1` | einmaliger Tausch |

## Richtungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `richtung` | string | `left` | `left`, `right`, `up`, `down` |
| `distanz` | string | `100%` | Wegstrecke, meist volle Breite; auch in px möglich |
| `anteilUeberlappung` | number | `1` | 1 = beide bewegen sich gleichzeitig, 0 = nacheinander |
| `deckkraftAmRand` | number | `1` | optionales Ausblenden an den Rändern während des Schiebens |
| `abgeschnitten` | boolean | `true` | Elemente außerhalb der Fläche nicht sichtbar |
| `nurNeues` | boolean | `false` | altes Element verschwindet stattdessen per Fade Out |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `aria-live` | string | `polite` | Inhaltswechsel ansagen |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `cross-fade` | ersatzweise überblenden statt schieben |
