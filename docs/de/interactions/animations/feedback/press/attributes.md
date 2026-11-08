# Press - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `press` | Name der Animation |
| `onPressStart` | function | - | läuft, wenn das Element nachgibt |
| `onPressEnd` | function | - | läuft nach der Rückkehr |
| `enabled` | boolean | `true` | Rückmeldung, solange der gedrückte Zustand anhält |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `120` | Dauer des Herunterdrückens in ms |
| `timingFunction` | string | `ease-out` | sofort reagieren, weich landen |
| `delay` | number | `0` | kein Anlauf, die Reaktion erfolgt sofort |
| `fillMode` | string | `forwards` | der gedrückte Zustand bleibt bis zum Loslassen |

## Druckattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `pressScale` | number | `0.97` | Zielgröße im gedrückten Zustand |
| `pressOffsetY` | number | `1` | zusätzliches Absenken nach unten in px |
| `pressOpacity` | number | `0.9` | leichtes Abdunkeln im gedrückten Zustand |
| `releaseScale` | number | `1` | Endgröße nach dem Loslassen |
| `releaseOvershoot` | number | `1` | ein kurzes Zurückfedern über 1 (1 = keins) |
| `nurBeiZeiger` | boolean | `false` | nur mit der Maus animieren, nicht bei Touch |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | - | beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `farbe` | die Größenänderung entfällt, die Zustandsfarbe bleibt |
