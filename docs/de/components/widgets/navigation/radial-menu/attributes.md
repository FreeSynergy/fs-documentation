# Radial Menu - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `items` | array[] | - | Array der Menüeinträge; Unterpunkte im Feld `children` |
| `activeItem` | string/number | - | aktiver Eintrag — seine Unterpunkte erscheinen im nächsten Ring |
| `onChange` | function | - | Ereignis bei Auswahl |
| `isOpen` | boolean | `false` | ist es geöffnet? |
| `onToggle` | function | - | Ereignis beim Öffnen/Schließen |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | enum | `ring` | Form: `ring`, `sektoren`, `facher`, `launcher`, `kontext` |
| `anchor` | string | `center` | Anker: `center`, `top`, `right`, `bottom`, `left`, `top-right` …, Koordinaten `{x, y}`, CSS-Selektor, `pointer` oder `fab` |
| `levels` | number | `2` | Anzahl der Ringe (Ebenen), höchstens 3 |
| `trigger` | enum | `hover` | Auslöser: `hover`, `tap`, `long-press`, `right-click` |
| `hoverDelay` | number | `100` | ms bis zum Öffnen beim Überfahren |
| `closeDelay` | number | `200` | Toleranz beim Zeigerweg in ms; das Menü schließt sich erst danach |
| `clamp` | boolean | `true` | einen vollen Kreis am Rand zu einem Viertel-/Halbfächer begrenzen? |
| `pinnable` | boolean | `true` | ein Klick hält das Menü offen (`pinned`) |
| `dimInactive` | boolean | `false` | alle Ringe außer dem aktiven abdunkeln? |
| `keyboardNavigation` | boolean | `true` | Pfeiltasten, `Enter`, `Esc`? |
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `220` | Dauer in ms (siehe [radial-out](../../../../interactions/animations/entrance/radial-out/)) |

## Geometrie

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `radius` | number | `72` | Radius von Ring 1 (Ankermitte → Eintragsmitte) |
| `ringGap` | number | `12` | Abstand zwischen zwei Ringen |
| `itemSize` | number | `40` | Durchmesser eines Eintrags |
| `startAngle` | number | `0` | Ausrichtung des ersten Eintrags (0° = oben) |
| `sweepAngle` | number | `360` | Winkelbereich des Rings (`clamp` verkleinert ihn) |
| `coneAngle` | number | `90` | Winkelbereich, in dem der Unterpunkt-Ring erscheint |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `size` | enum | `medium` | `small`, `medium`, `large` |
| `shape` | enum | `kreis` | Form der Einträge: `kreis`, `quadrat`, `abgerundet`, `squircle`, `dreieck`, `fuenfeck`, `sechseck`, `achteck`, `vieleck`, `keil`, `bluete`, `stern` |
| `sides` | number | `6` | Eckenzahl für `vieleck` (3–12) |
| `cornerRadius` | number | `0` | Eckenrundung: `0` = scharf, halbe Seitenlänge = nahe am Kreis |
| `rotation` | number | `0` | dreht die Form, sodass eine Ecke/Spitze nach außen zeigt |
| `showLabels` | boolean | `false` | Beschriftung dauerhaft sichtbar; sonst nur am aktiven Eintrag (`label-reveal`) |
| `color` | enum | `default` | Farbe: `default`, `light`, `primary` |

## Effekte beim Überfahren

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `grow` | boolean | `true` | Eintrag wächst auf 110 % |
| `shift` | number | `6` | Eintrag rückt radial nach außen (px) |
| `lift` | boolean | `true` | der Schatten wächst, der Eintrag hebt sich |
| `glow` | boolean | `false` | Leuchten um den aktiven Eintrag |
| `morphShape` | boolean | `false` | die Form des aktiven Eintrags wechselt sanft |
| `ringRotate` | boolean | `false` | der Ring dreht sich, bis der aktive Eintrag oben steht |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | wird ausgeführt, wenn ein Eintrag gewählt wird |
| `onOpen` | function | wird beim Öffnen ausgeführt |
| `onClose` | function | wird beim Schließen ausgeführt |
| `onLevelChange` | function | wird ausgeführt, wenn sich der aktive Ring ändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `menu` |
| `aria-expanded` | boolean | ist das Menü geöffnet? |
| `aria-haspopup` | boolean | Eintrag hat Unterpunkte |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
