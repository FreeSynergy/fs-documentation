# Tick Draw - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `animation` | string | `tick-draw` | Name der Animation |
| `onDrawStart` | function | - | Wird beim Beginn des Zeichnens ausgeführt |
| `onDrawEnd` | function | - | Wird ausgeführt, wenn der Haken vollständig ist |
| `behalten` | boolean | `true` | Haken nach der Animation sichtbar lassen |

## Animations-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `duration` | number | `400` | Dauer des Zeichnens in ms |
| `timingFunction` | string | `ease-out` | schnell beginnen, ruhig auslaufen |
| `delay` | number | `150` | Vorlauf für Kreis oder Hintergrund |
| `fillMode` | string | `forwards` | fertigen Haken beibehalten |

## Zeichen-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `strokeLength` | number | `auto` | zubereitende Pfadlänge (auto: aus dem Icon gemessen) |
| `strokeWidth` | number | `2.5` | Strichdicke in px |
| `strokeFarbe` | string | `erfolg` | Farbe des Strichs, folgt dem Statusfarbsystem |
| `strichEnde` | string | `round` | `round`, `square` oder `butt` |
| `hintergrund` | string | `kreis` | `none`, `kreis` oder `flaeche` |
| `hintergrundDauer` | number | `200` | Dauer des Erscheinens von Kreis oder Fläche in ms |
| `nachziehen` | number | `0` | kurzer Overshoot am Ende des Strichs in px |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `aria-label` | string | `Erledigt` | Text für Screenreader – nie nur das Zeichen |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `instant` | Haken erscheint ohne Zeichenbewegung |
