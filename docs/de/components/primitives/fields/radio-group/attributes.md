# Radio Group - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `options` | array[] | - | Liste der Optionsobjekte |
| `value` | string/number | - | aktueller Wert |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `variant` | enum | `default` | Stil: `default`, `toggle` |
| `name` | string | - | Name für das Formular |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showIcons` | boolean | `false` | Icons anzeigen? |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `radiogroup` |

## Attribute der Optionen

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `value` | string/number | Wert |
| `label` | string | Beschriftung |
| `icon` | string | Name des Icons |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
