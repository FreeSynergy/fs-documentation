# Language Switcher - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `languages` | array[] | - | array of languages |
| `currentLanguage` | string | - | current language |
| `onChange` | function | - | event on language change |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onOpen` | function | runs when opened |
| `onClose` | function | runs when closed |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `combobox` |

## Language attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `code` | string | language code (e.g. 'de', 'en') |
| `label` | string | display name |
| `flag` | string | flag emoji |

## Variant attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showCurrentLanguage` | boolean | `true` | show the current language? |
| `showFlags` | boolean | `true` | show flags? |

## Feature attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `autoDetect` | boolean | `false` | automatic detection? |
| `persist` | boolean | `true` | save the setting? |
| `reload` | boolean | `false` | reload the page? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
