# Bounce Out - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onAnimateStart` | function | - | Wird beim Start des Verabschiedens ausgeführt |
| `onAnticipation` | function | - | Wird beim Ausholen (Stauchung) ausgeführt |
| `onAnimateEnd` | function | - | Wird nach dem vollständigen Verschwinden ausgeführt |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `400` | Gesamtdauer aus Ausholen und Aussprung in ms |
| `timingFunction` | string | `ease-in` | Beschleunigender Absprung |
| `delay` | number | `0` | Verzögerung bis zum Start in ms |
| `fillMode` | string | `forwards` | Unsichtbarer Endzustand bleibt erhalten |

## Antizipations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `anticipation` | number | `8` | Ausholen gegen die Ausflugsrichtung in % der Elementgröße |
| `squash` | number | `0.9` | Stauchung der Skalierung vor dem Aussprung (1 = keine) |
| `exitDirection` | string | `up` | Richtung des Aussprungs: `up`, `down`, `left`, `right` |
| `endScale` | number | `0.2` | Skalierung beim Verschwinden (0 = vollständig geschrumpft) |
| `removeOnEnd` | boolean | `true` | Element nach dem Verschwinden aus dem DOM entfernen? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | - | `instant` – ohne Federung sofort ausblenden |
