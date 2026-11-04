# Embed - Attributes

Only **own** attributes. Everything else comes from the base class, see
[base](../../../primitives/basics/base.md).

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `source` | enum | `iframe` | kind of embedding: `app`, `widget`, `iframe` |
| `src` | string | - | source URL (only `source = iframe`) |
| `appId` | string | - | program id (only `source = app`) |
| `config` | object | - | configuration of the embedded content |
| `title` | string | - | title of the header |
| `showBorder` | boolean | `true` | show a border? |
| `borderColor` | string | `#ccc` | border colour |
| `widgetId` | string | - | widget ID |

## Behaviour

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `responsive` | boolean | `true` | the surface adapts to the width |
| `interactive` | boolean | `true` | allow input in the embedded content |
| `ratio` | enum | `auto` | aspect ratio: `auto`, `16:9`, `4:3`, `1:1` |
| `allowFullscreen` | boolean | `true` | allow fullscreen |
| `sandbox` | string | `null` | sandbox settings, only `source = iframe` |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onLoad` | function | the content is ready |
| `onError` | function | the content could not be loaded |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | `region` for `app` and `widget`, `iframe` for `iframe` |
| `title` | string | also serves as the naming text for assistive technologies |

## Communication

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `postMessage` | boolean | `false` | message exchange with the content |
| `origin` | string | - | allowed origin, required with `postMessage` |

## Inherited from

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Base component](../../../primitives/basics/base.md)
