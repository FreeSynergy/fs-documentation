# Edge Swipe - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onEdgeSwipe` | function | - | Wird beim Edge Swipe ausgeführt |
| `onEdgeSwipeStart` | function | - | Wird beim Start ausgeführt |
| `onEdgeSwipeProgress` | function | - | Fortschritt 0–1 während des Wischens |
| `onEdgeSwipeCancel` | function | - | Wisch wurde zurückgebrochen |

## Rand-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `edge` | string | `left` \| `right` \| `top` \| `bottom` | Aktiver Rand |
| `edgeSize` | number | `24` | Breite der Randzone in px |
| `swipeThreshold` | number | `50` | Ab dieser Distanz gilt die Geste als abgeschlossen |
| `predictive` | boolean | `true` | Prädiktiven Pfad auswerten (iOS/Android)? |

## Navigations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `action` | string | `back` \| `panel` \| `home` | Aktion des Rand-Wischs |
| `interactive` | boolean | `true` | Übergang folgt dem Finger (interaktives Navigieren)? |
| `cancelOnReturn` | boolean | `true` | Zurückziehen unter Threshold bricht ab |
| `enabled` | boolean | `true` | Geste aktiv? |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `shadowPreview` | boolean | `true` | Vorschatten des darunterliegenden Views |
| `hapticFeedback` | boolean | `false` | Vibration beim Überschreiten des Threshold |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Zurück-Button / Tastenkürzel als Ersatz |
| `aria-label` | string | - | Beschreibung der Randaktion |
| `respectReducedMotion` | boolean | `true` | Übergang ohne Animation? |
