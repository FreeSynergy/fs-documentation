# Button-Gruppe – Attribute

Nur **eigene** Attribute. Alles Weitere kommt von der Basisklasse, siehe
[base](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `items` | array[] | - | die Buttons oder Segmente der Gruppe |
| `value` | string \| array | `null` | aktuell gewählter Wert (für `segment`) |
| `selectionMode` | enum | `single` | `single`, `multiple` (nur für `segment`) |
| `attached` | boolean | `true` | Elemente liegen ohne Abstand aneinander |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `variant` | enum | `verbund` | `verbund`, `segment`, `split` |
| `orientation` | enum | `horizontal` | `horizontal`, `vertical` |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onSelect` | function | Auswahl hat sich geändert (nur für `segment`) |
| `onAction` | function | Aktion eines Elements wurde ausgelöst |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | `group`; für `segment` zusätzlich `radiogroup` oder `tablist` |
| `aria-label` | string | Gruppenbezeichnung, wenn es keinen sichtbaren Titel gibt |
| `aria-pressed` | boolean | Zustand eines `verbund`-Elements |
| `aria-checked` | boolean | Zustand eines Segments |

## Geerbt von

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base.md)
