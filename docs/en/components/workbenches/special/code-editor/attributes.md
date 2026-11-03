# Code Editor - Attribute

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `value` | string | - | Wert (Code) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `language` | string | `javascript` | Sprache |
| `readOnly` | boolean | `false` | Nur-Lese-Modus? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onKeyDown` | function | runs on a key press |

## Accessibility

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `role` | string | ARIA role: `textbox` |

## Features attributes

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `showLineNumbers` | boolean | `true` | Zeilennummern anzeigen? |
| `showGutter` | boolean | `true` | Gutter anzeigen? |
| `autoCompletion` | boolean | `true` | Autovervollständigung aktivieren? |

## Editor-Attribute

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `lineHeight` | number | `1.5` | Zeilenhöhe |
| `fontSize` | number | `14` | Font size |
| `tabSize` | number | `2` | Tab-Größe |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
