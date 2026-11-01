# Button Group (Schaltflächengruppe) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `items` | array[] | - | Buttons bzw. Segmente der Gruppe |
| `value` | string \| array | `null` | aktuell gewählter Wert (bei `segment`) |
| `selectionMode` | enum | `single` | `single`, `multiple` (nur bei `segment`) |
| `attached` | boolean | `true` | Elemente ohne Zwischenraum aneinander |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `variant` | enum | `verbund` | `verbund`, `segment`, `split` |
| `orientation` | enum | `horizontal` | `horizontal`, `vertical` |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onSelect` | function | Auswahl geändert (nur bei `segment`) |
| `onAction` | function | Aktion eines Elements ausgelöst |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `group`; bei `segment` zusätzlich `radiogroup` oder `tablist` |
| `aria-label` | string | Gruppenbeschriftung, wenn kein sichtbarer Titel |
| `aria-pressed` | boolean | Zustand eines `verbund`-Elements |
| `aria-checked` | boolean | Zustand eines Segments |

## Geerbt von

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
