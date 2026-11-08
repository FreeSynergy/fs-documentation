# Code-Editor – Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
| ---------- | ----- | --------- | -------------- |
| `value` | string | - | Wert (Code) |
| `onChange` | function | - | Ereignis bei Änderung |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `language` | string | `javascript` | Sprache |
| `readOnly` | boolean | `false` | Nur-Lesen-Modus? |

## Ereignisse

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `onKeyDown` | function | läuft bei einem Tastendruck |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
| ---------- | ----- | -------------- |
| `role` | string | ARIA-Rolle: `textbox` |

## Funktionsattribute

| Attribut | Typ | Standard | Beschreibung |
| --- | --- | --- | --- |
| `showLineNumbers` | boolean | `true` | Zeilennummern anzeigen? |
| `showGutter` | boolean | `true` | Randspalte anzeigen? |
| `autoCompletion` | boolean | `true` | Autovervollständigung aktivieren? |

## Editor-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `lineHeight` | number | `1.5` | Zeilenhöhe |
| `fontSize` | number | `14` | Schriftgröße |
| `tabSize` | number | `2` | Tabulatorbreite |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
