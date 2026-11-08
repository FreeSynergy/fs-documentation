# Morph - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `startForm` | string | - | SVG-Pfad oder Form des Startzustands |
| `endForm` | string | - | SVG-Pfad oder Form des Zielzustands |
| `zustand` | string | `start` | `start`/`ende` wechselt die Form |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `duration` | number | `400` | Dauer des Formwechsels in ms |
| `timingFunction` | string | `ease-in-out` | weiche Start- und Endphase |
| `delay` | number | `0` | verzögerter Start in ms |
| `direction` | string | `normal` | `reverse` morpht zurück |

## Formattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `randRadiusStart` | number | `0` | Eckenradius der Startform in px |
| `randRadiusEnd` | number | `0` | Eckenradius der Zielform in px |
| `punktabgleich` | string | `auto` | Stützpunkte beider Pfade zuordnen (`auto`, `manuell`) |
| `colorTransition` | boolean | `true` | Füll- und Rahmenfarbe weich überblenden |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `aria-label` | string | - | Beschreibender Text |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
