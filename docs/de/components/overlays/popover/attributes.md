# Popover (Inhaltspopover) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `content` | slot | - | Inhalt des Popovers (Aktionen, Text, Formular) |
| `open` | boolean | `false` | geöffnet? (gesteuert) |
| `variant` | enum | `inhalt` | `inhalt`, `aktionen`, `formular` |

## Verhalten
| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `trigger` | enum | `click` | `click`, `hover`, `focus` |
| `placement` | enum | `bottom` | `top`, `right`, `bottom`, `left`, `auto` |
| `dismiss` | enum | `beides` | `click-outside`, `escape`, `beides`, `none` |
| `arrow` | boolean | `true` | Pfeil zum Auslöser |
| `offset` | number | `8` | Abstand zum Auslöser in px |

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `autoFocus` | boolean | `true` | Fokus beim Öffnen in das Popover legen |
| `returnFocus` | boolean | `true` | Fokus beim Schließen zum Auslöser zurück |
| `closeOnAction` | boolean | `false` | nach einer Aktion im Popover schließen |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onOpen` | function | Popover wurde geöffnet |
| `onClose` | function | Popover wurde geschlossen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `dialog` bei `variant="formular"`, sonst `presentation` |
| – | – | Auslöser erhält `aria-expanded` und `aria-controls` |
| – | – | Popover erhält eine Beschriftung (`aria-label` oder Überschrift) |

## Geerbt von

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
