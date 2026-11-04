# Embed

| Field | Value |
|-------|-------|
| **Category** | `special` |
| **Inherits from** | `base` |
| **Variants** | `app`, `widget`, `iframe` |
| **States** | `geladen`, `fehler` |
| **Gestures** | `tap`, `drag` (only with `interactive`) |
| **Animations** | `fade-in` |
| **Related** | `map-view`, `whiteboard`, `dashboard`, `base` |
| **State** | documented |

!!! info "Standardisation"
    The former components `app-embed`, `widget-embed` and `iframe-embed` became the `source`
    attribute of `embed`: `app`, `widget`, `iframe`.

## Description

An **embed** includes foreign content in a FreeSynergy surface: another FreeSynergy
program, a widget or an external page. The content does not belong to the application; it
is shown in its own surface and addressed through a clearly named interface.

## Purpose

- Embedding one FreeSynergy program into another (e.g. a calendar inside a dashboard)
- Placing a widget (weather, clock, counter) on a page or a dashboard
- Embedding an external page or an external player

## Variants

| Variant | Description |
|---------|-------------|
| **app** | another FreeSynergy program in the window |
| **widget** | small program with its own configuration |
| **iframe** | external page via `src` |

## Features

- Uniform size via `size` and `ratio`, responsive behaviour can be switched off
- Message exchange with the embedded content (`postMessage`) with origin checking
- Loading and error states are part of the component, not of the embedded content
- Sandbox and permissions only take effect with `source = iframe`

## Distinction

- **Do not confuse with** `app-embed`, `widget-embed` and `iframe-embed`: these three
  former standalone components became `source` values inside `embed`.

- **Do not confuse with** [map-view](../../../widgets/special/map-view/) and [whiteboard](../whiteboard/):
  those are components of their own with their own data structure, not an embedding.

- **Do not confuse with** [iframe](https://developer.mozilla.org/docs/Web/HTML/Element/iframe):
  `embed` is the surface including states and permissions.

## Best Practices

- Always treat external content separately in the `media-src` and `scripts-src` modes;
  the default is no script execution.

- Always set `origin` when `postMessage` is active.
- For embedded programs: no double menu. The embedding program hides its own headers
  when `source = app`.

- An embed is never the only way to reach the content — also offer a link outwards.

## See also

- [Dashboard](../dashboard/) — embeds as building blocks
- [Base component](../../../primitives/basics/base.md)
