# Language Switcher - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `languages` | array[] | - | Array von Sprachen |
| `currentLanguage` | string | - | Aktuelle Sprache |
| `onChange` | function | - | Event bei Sprachwechsel |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `combobox` |

## Sprach-Attribute

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `code` | string | Sprachcode (z.B. 'de', 'en') |
| `label` | string | Anzeigename |
| `flag` | string | Flaggen-Emoji |

## Varianten-Attribute

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showCurrentLanguage` | boolean | `true` | Aktuelle Sprache anzeigen? |
| `showFlags` | boolean | `true` | Flaggen anzeigen? |

## Features attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `autoDetect` | boolean | `false` | Automatische Erkennung? |
| `persist` | boolean | `true` | Einstellung speichern? |
| `reload` | boolean | `false` | Seite neu laden? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
