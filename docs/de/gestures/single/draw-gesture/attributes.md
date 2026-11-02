# Draw Gesture - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onDrawGesture` | function | - | Wird nach erkannter Form ausgeführt |
| `onDrawStart` | function | - | Zeichnen begonnen |
| `onDrawProgress` | function | - | Aktueller Pfad während des Zeichnens |
| `onDrawUnknown` | function | - | Keine Vorlage erkannt |

## Erkennungs-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `shapes` | string[] | `[]` | Erlaubte Formen/Buchstaben (`v`, `c`, `circle`, …) |
| `matchThreshold` | number | `0.8` | Ab welcher Ähnlichkeit (0–1) gilt eine Form als erkannt? |
| `sampleRate` | number | `60` | Punkte pro Sekunde beim Aufzeichnen |
| `strokeWidth` | number | `3` | Zeichenstrich in px (nur visuell) |
| `caseInsensitive` | boolean | `true` | Groß/Kleinschreibung bei Buchstaben ignorieren? |

## Kontext-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `activationArea` | string | `fullscreen` \| `overlay` | Wo Zeichnen ausgelöst werden kann |
| `confirmation` | boolean | `false` | Aktion erst nach Bestätigung ausführen? |
| `showShapeHint` | boolean | `true` | Erlaubte Formen einblenden? |
| `maxStrokes` | number | `3` | Max. Striche pro Geste |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `trail` | boolean | `true` | Gezeichneten Pfad anzeigen? |
| `recognizeLive` | boolean | `false` | Während des Zeichnens bereits teilweise erkennen? |
| `hapticFeedback` | boolean | `true` | Vibration bei Erkennung? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | zwingend nötig: Button/Kommando statt Form (WCAG 2.5.1) |
| `alternativeLabel` | string | - | Beschreibung der Alternative |
