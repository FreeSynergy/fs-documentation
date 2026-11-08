# Text Input - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `value` | string | - | Wert |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `type` | enum | `text` | `text`, `email`, `url`, `phone`, `password` (`email`/`url`/`phone` ersetzen die früheren eigenen Komponenten) |
| `placeholder` | string | `null` | Platzhaltertext |
| `readOnly` | boolean | `false` | Nur-Lese-Modus? |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showLabel` | boolean | `true` | Label anzeigen? |
| `showIcon` | boolean | `false` | Icon anzeigen? |
| `prefix` | string | - | Präfix |
| `suffix` | string | - | Suffix |
| `countryCode` | string | `DE` | Standard-Ländercode (nur `type="phone"`) |
| `showCountryCode` | boolean | `true` | Ländercode anzeigen (nur `type="phone"`) |
| `icon` | string | `email` | Name des Icons |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onKeyDown` | function | wird bei einem Tastendruck ausgeführt |
| `onSubmit` | function | wird beim Absenden ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `textbox` |

## Validierungsattribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `required` | boolean | `false` | Pflichtfeld? |
| `error` | string | - | Fehlermeldung |
| `minLength` | number | - | minimale Länge |
| `maxLength` | number | - | maximale Länge |
| `pattern` | string | - | Regex-Muster |
| `isValidEmail` | function | - | eigene E-Mail-Prüfung (für `type="email"`) |
| `isValidURL` | function | - | eigene URL-Prüfung (für `type="url"`) |
| `isValidPhone` | function | - | eigene Telefonprüfung (für `type="phone"`) |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base-Komponente](../../basics/base.md)
