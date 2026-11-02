# Radial Menu (Kreismenü) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Array von Menüpunkten; Unterpunkte im Feld `children` |
| `activeItem` | string/number | - | Aktiver Punkt — seine Unterpunkte erscheinen im nächsten Ring |
| `onChange` | function | - | Event bei Auswahl |
| `isOpen` | boolean | `false` | Ist geöffnet? |
| `onToggle` | function | - | Event beim Öffnen/Schließen |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `ring` | Bauform: `ring`, `sektoren`, `facher`, `launcher`, `kontext` |
| `anchor` | string | `center` | Anker: `center`, `top`, `right`, `bottom`, `left`, `top-right` …, Koordinaten `{x, y}`, CSS-Selektor, `pointer` oder `fab` |
| `levels` | number | `2` | Anzahl Ringe (Ebenen), höchstens 3 |
| `trigger` | enum | `hover` | Auslösung: `hover`, `tap`, `long-press`, `right-click` |
| `hoverDelay` | number | `100` | ms, bevor Hover öffnet |
| `closeDelay` | number | `200` | Wegfahr-Toleranz in ms; Menü schließt erst danach |
| `clamp` | boolean | `true` | Vollkreis am Rand zum Viertel-/Halbfächer klemmen? |
| `pinnable` | boolean | `true` | Klick hält das Menü offen (`pinned`) |
| `dimInactive` | boolean | `false` | Alle Ringe außer dem aktiven dämpfen? |
| `keyboardNavigation` | boolean | `true` | Pfeiltasten, `Enter`, `Esc`? |
| `animate` | boolean | `true` | Animationen aktivieren? |
| `animationDuration` | number | `220` | Dauer in ms (siehe [radial-out](../../../animations/entrance/radial-out/)) |

## Geometrie

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `radius` | number | `72` | Radius Ring 1 (Ankermitte → Punktmitte) |
| `ringGap` | number | `12` | Abstand zweier Ringe zueinander |
| `itemSize` | number | `40` | Durchmesser eines Punktes |
| `startAngle` | number | `0` | Ausrichtung des ersten Punktes (0° = oben) |
| `sweepAngle` | number | `360` | Winkelbereich des Ringes (`clamp` reduziert ihn) |
| `coneAngle` | number | `90` | Winkelbereich, in dem der Unterpunkt-Ring erscheint |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `size` | enum | `medium` | `small`, `medium`, `large` |
| `shape` | enum | `kreis` | Form der Punkte: `kreis`, `quadrat`, `abgerundet`, `squircle`, `dreieck`, `fuenfeck`, `sechseck`, `achteck`, `vieleck`, `keil`, `bluete`, `stern` |
| `sides` | number | `6` | Eckzahl bei `vieleck` (3–12) |
| `cornerRadius` | number | `0` | Eckrundung: `0` = scharf, halbe Seitenlänge = kreisnah |
| `rotation` | number | `0` | dreht die Form, damit eine Ecke/Zacke nach außen zeigt |
| `showLabels` | boolean | `false` | Beschriftung dauerhaft; sonst nur am aktiven Punkt (`label-reveal`) |
| `color` | enum | `default` | Farbe: `default`, `light`, `primary` |

## Hover-Effekte

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `grow` | boolean | `true` | Punkt wächst auf 110 % |
| `shift` | number | `6` | Punkt wandert radial nach außen (px) |
| `lift` | boolean | `true` | Schatten wächst, Punkt hebt sich |
| `glow` | boolean | `false` | Leuchten um den aktiven Punkt |
| `morphShape` | boolean | `false` | Form des aktiven Punktes wechselt weich |
| `ringRotate` | boolean | `false` | Ring dreht, bis der aktive Punkt oben steht |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Wird bei Auswahl eines Punktes ausgeführt |
| `onOpen` | function | Wird beim Öffnen ausgeführt |
| `onClose` | function | Wird beim Schließen ausgeführt |
| `onLevelChange` | function | Wird beim Wechsel des aktiven Ringes ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `menu` |
| `aria-expanded` | boolean | Ist das Menü geöffnet? |
| `aria-haspopup` | boolean | Punkt hat Unterpunkte |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
