# Code Editor - Attributes

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `value` | string | - | value (code) |
| `onChange` | function | - | event on change |

## Behaviour

| Attribute | Type | Default | Description |
| --- | --- | --- | --- |
| `language` | string | `javascript` | language |
| `readOnly` | boolean | `false` | read-only mode? |

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
| `showLineNumbers` | boolean | `true` | show line numbers? |
| `showGutter` | boolean | `true` | show the gutter? |
| `autoCompletion` | boolean | `true` | enable autocompletion? |

## Editor attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `lineHeight` | number | `1.5` | line height |
| `fontSize` | number | `14` | font size |
| `tabSize` | number | `2` | tab size |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
