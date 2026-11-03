# Hover - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onHoverStart` | function | - | Zeiger betritt Element |
| `onHoverMove` | function | - | Zeiger bewegt sich über Element |
| `onHoverEnd` | function | - | Zeiger verlässt Element |

## Timing-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `enterDelay` | number | `300` | Verzögerung bis Aktivierung in ms |
| `exitDelay` | number | `100` | Verzögerung bis Deaktivierung in ms |
| `hoverTimeout` | number | `0` | Auto-Aus nach Zeit in ms (0 = nie) |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `hoverAnimation` | string | `lift` \| `highlight` \| `none` | Reaktion des Elements |
| `tooltip` | string \| node | - | Tooltip-Inhalt |
| `liftElevation` | number | `4` | Schatten-Stufe beim Anheben |
| `showOnTouch` | boolean | `false` | Touch-Nachbau: erster Tap zeigt Hover-Inhalt? |

## Zeiger-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `pointerTypes` | string[] | `mouse, pen` | Welche Zeigerarten lösen aus? |
| `requirePrecise` | boolean | `true` | Nur präzisen Zeiger (Maus/Touchpad/Stift) akzeptieren? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `focusEquivalent` | boolean | `true` | Zeigt denselben Inhalt bei Tastatur-Fokus? |
| `dismissible` | boolean | `true` | Mit Escape schließbar? |
| `hoverPersist` | boolean | `true` | Inhalt bleibt lange genug sichtbar (WCAG 1.4.13)? |
