# Press - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `press` | Name der Animation |
| `onPressStart` | function | - | Wird beim Absteigen ausgeführt |
| `onPressEnd` | function | - | Wird nach der Rückkehr ausgeführt |
| `enabled` | boolean | `true` | Feedback bei gedrücktem Zustand |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `120` | Dauer des Absteigens in ms |
| `timingFunction` | string | `ease-out` | sofort reagieren, weich landen |
| `delay` | number | `0` | kein Anlauf, Reaktion unmittelbar |
| `fillMode` | string | `forwards` | gedrückter Zustand bleibt bis zum Loslassen |

## Druck-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `pressScale` | number | `0.97` | Zielgröße im gedrückten Zustand |
| `pressOffsetY` | number | `1` | zusätzliche Absenkung nach unten in px |
| `pressOpacity` | number | `0.9` | leichte Abblendung im gedrückten Zustand |
| `releaseScale` | number | `1` | Endgröße nach dem Loslassen |
| `releaseOvershoot` | number | `1` | kurzer Rückprall über 1 hinaus (1 = keiner) |
| `nurBeiZeiger` | boolean | `false` | Animation nur bei Maus, nicht bei Touch |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `farbe` | Größenänderung weg, Zustandsfarbe bleibt |
