# Morph - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `startForm` | string | - | SVG-Pfad oder Form des Ausgangszustands |
| `endForm` | string | - | SVG-Pfad oder Form des Zielzustands |
| `zustand` | string | `start` | `start`/`ende` schaltet die Form um |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `400` | Dauer der Formumwandlung in ms |
| `timingFunction` | string | `ease-in-out` | weiche Anfangs- und Endphase |
| `delay` | number | `0` | verzögerter Start in ms |
| `direction` | string | `normal` | `reverse` morpht zurück |

## Form-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `randRadiusStart` | number | `0` | Eckenradius der Ausgangsform in px |
| `randRadiusEnd` | number | `0` | Eckenradius der Zielform in px |
| `punktabgleich` | string | `auto` | Stützpunkte beider Pfade zuordnen (`auto`, `manuell`) |
| `colorTransition` | boolean | `true` | Füll- und Randfarbe weich übergehen |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
