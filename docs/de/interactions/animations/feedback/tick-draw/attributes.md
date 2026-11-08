# Tick Draw - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `animation` | string | `tick-draw` | Name der Animation |
| `onDrawStart` | function | - | läuft, wenn das Zeichnen beginnt |
| `onDrawEnd` | function | - | läuft, sobald das Häkchen fertig ist |
| `behalten` | boolean | `true` | Häkchen nach der Animation sichtbar lassen |

## Animationsattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `duration` | number | `400` | Dauer des Zeichnens in ms |
| `timingFunction` | string | `ease-out` | schnell beginnen, ruhig auslaufen |
| `delay` | number | `150` | Anlauf für den Kreis oder Hintergrund |
| `fillMode` | string | `forwards` | das fertige Häkchen bleibt erhalten |

## Zeichenattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `strokeLength` | number | `auto` | vorbereitete Pfadlänge (auto: aus dem Icon gemessen) |
| `strokeWidth` | number | `2.5` | Strichstärke in px |
| `strokeFarbe` | string | `erfolg` | Farbe des Strichs, folgt dem Statusfarbsystem |
| `strichEnde` | string | `round` | `round`, `square` oder `butt` |
| `hintergrund` | string | `kreis` | `none`, `kreis` oder `flaeche` |
| `hintergrundDauer` | number | `200` | Dauer des Erscheinens von Kreis oder Fläche in ms |
| `nachziehen` | number | `0` | ein kurzes Überschwingen am Ende des Strichs in px |

## Barrierefreiheit

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `aria-label` | string | `Erledigt` | Text für Screenreader – nie nur das Zeichen |
| `respectReducedMotion` | boolean | `true` | Animation bei prefers-reduced-motion reduzieren? |
| `reducedMotionFallback` | string | `instant` | das Häkchen erscheint ohne Zeichenbewegung |
