# Pull to Refresh - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onRefresh` | function | - | Wird nach dem Loslassen im Armed-Zustand ausgeführt |
| `onPullProgress` | function | - | Fortschritt 0–1 während des Ziehens |
| `onArm` | function | - | Threshold erreicht (Armed) |
| `refreshing` | boolean | `false` | Ladezustand (Indicator sichtbar, bis `false`) |

## Trigger-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `edge` | string | `top` \| `bottom` \| `left` \| `right` | Startkante des Ziehens |
| `triggerDistance` | number | `80` | Distanz in px bis Armed |
| `maxPull` | number | `200` | Max. Auslenkung in px |
| `rubberBand` | boolean | `true` | Widerstand mit Gummiband-Kurve? |
| `enabled` | boolean | `true` | Geste aktiv? |

## Indikator-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `indicatorStyle` | string | `spinner` \| `progress` \| `custom` | Aussehen des Indikators |
| `indicatorColor` | color | Akzentfarbe | Farbe des Indikators |
| `holdDuringRefresh` | boolean | `true` | Liste während des Ladens arretiert? |
| `autoHideDelay` | number | `300` | Ausblenden-Delay nach Abschluss in ms |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `hapticFeedback` | boolean | `true` | Vibration beim Arretieren? |
| `releaseLabel` | string | „Loslassen zum Aktualisieren“ | Text im Armed-Zustand |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `refreshButton` | boolean | `true` | Expliziter Aktualisieren-Button als Alternative? |
| `aria-live` | string | `polite` | Statusänderungen ansagen |
| `respectReducedMotion` | boolean | `true` | Ohne Gummiband-/Rotier-Animation? |
