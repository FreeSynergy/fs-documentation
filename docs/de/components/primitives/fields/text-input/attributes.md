# Text Input (Einzeiliges Textfeld) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert |
| `onChange` | function | - | Event bei Änderung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `type` | enum | `text` | `text`, `email`, `url`, `phone`, `password` (`email`/`url`/`phone` ersetzen die früheren Eigenkomponenten) |
| `placeholder` | string | `null` | Placeholder-Text |
| `readOnly` | boolean | `false` | Nur-Lese-Modus? |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showLabel` | boolean | `true` | Label anzeigen? |
| `showIcon` | boolean | `false` | Icon anzeigen? |
| `prefix` | string | - | Präfix |
| `suffix` | string | - | Suffix |
| `countryCode` | string | `DE` | Standard-Ländercode (nur `type="phone"`) |
| `showCountryCode` | boolean | `true` | Ländercode anzeigen (nur `type="phone"`) |
| `icon` | string | `email` | Icon-Name |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onKeyDown` | function | Wird bei Tastendruck ausgeführt |
| `onSubmit` | function | Wird bei Submit ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `textbox` |

## Validation-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `required` | boolean | `false` | Erforderlich? |
| `error` | string | - | Fehlermeldung |
| `minLength` | number | - | Minimale Länge |
| `maxLength` | number | - | Maximale Länge |
| `pattern` | string | - | Regex-Muster |
| `isValidEmail` | function | - | Eigene E-Mail-Validierung (bei `type="email"`) |
| `isValidURL` | function | - | Eigene URL-Validierung (bei `type="url"`) |
| `isValidPhone` | function | - | Eigene Telefon-Validierung (bei `type="phone"`) |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
