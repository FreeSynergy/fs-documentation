# Popover - Attribute

Nur **eigene** Attribute. Alles Übrige kommt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `content` | slot | - | Inhalt des Popovers (Aktionen, Text, Formular) |
| `open` | boolean | `false` | geöffnet? (gesteuert) |
| `variant` | enum | `inhalt` | `inhalt`, `aktionen`, `formular` |

## Verhalten
| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `trigger` | enum | `click` | `click`, `hover`, `focus` |
| `placement` | enum | `bottom` | `top`, `right`, `bottom`, `left`, `auto` |
| `dismiss` | enum | `beides` | `click-outside`, `escape`, `beides`, `none` |
| `arrow` | boolean | `true` | Pfeil, der auf den Auslöser zeigt |
| `offset` | number | `8` | Abstand zum Auslöser in px |

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `autoFocus` | boolean | `true` | beim Öffnen den Fokus ins Popover setzen |
| `returnFocus` | boolean | `true` | beim Schließen den Fokus zum Auslöser zurückgeben |
| `closeOnAction` | boolean | `false` | nach einer Aktion im Popover schließen |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | das Popover wurde geöffnet |
| `onClose` | function | das Popover wurde geschlossen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `dialog` bei `variant="formular"`, sonst `presentation` |
| – | – | der Auslöser erhält `aria-expanded` und `aria-controls` |
| – | – | das Popover erhält eine Beschriftung (`aria-label` oder eine Überschrift) |

## Geerbt von

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../../primitives/basics/base.md)
