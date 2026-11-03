# Radio Group - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `options` | array[] | - | Array von Options-Objekten |
| `value` | string/number | - | Aktueller Wert |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `default` | Stil: `default`, `toggle` |
| `name` | string | - | Name für Form |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Icons anzeigen? |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `radiogroup` |

## Option-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `value` | string/number | Wert |
| `label` | string | Label-Text |
| `icon` | string | Icon-Name |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
