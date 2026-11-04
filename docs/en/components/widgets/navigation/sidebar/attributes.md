# Sidebar - Attributes

## Main attributes

| Attribute | Type | Default | Description |
| ---------- | ----- | --------- | -------------- |
| `position` | enum | `left` | position: `left`, `right` |
| `width` | number/string | `240` | width in px or a CSS unit |
| `collapsed` | boolean | `false` | sidebar collapsed? |
| `collapsible` | boolean | `true` | can the user collapse it? |

## Events

| Attribute | Type | Description |
| ---------- | ----- | -------------- |
| `onSelect` | function | runs on click |
| `onToggle` | function | runs on opening/closing |

## Menu attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `items` | array[] | array of menu items |
| `groups` | array[] | array of menu groups |
| `showIcons` | boolean | show icons? |
| `showLabels` | boolean | show text labels? |

## Item attributes (per menu item)

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | yes | unique ID |
| `label` | string | yes | display text |
| `icon` | string | no | icon name (e.g. "mdi:mail") |
| `path` | string | no | target path/navigation |
| `badge` | string/number | no | small badge text (e.g. "3") |
| `children` | array[] | no | sub-menus (dropdown/tree) |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
