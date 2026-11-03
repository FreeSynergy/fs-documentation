# Kbd

| Field | Value |
|-------|-------|
| **Category** | `basics` |
| **Inherits from** | `base` |
| **Variants** | `einzeln`, `kombination` |
| **States** | `active` (key pressed) |
| **Gestures** | none – display only |
| **Animations** | `press` |
| **Related** | `badge`, `tooltip`, `base` |
| **Status** | documented |

## Description

Kbd shows a single key or a key combination visually – as it appears on a key
cap. It is used in help texts, tooltips and the shortcut documentation of the
programs.

## Purpose

- Shortcuts in tooltips and context help (`Ctrl + S`)
- Keyboard shortcuts in overviews and onboarding tours
- Pressed/active state while learning shortcuts

## Variants

| Variant | Description |
|---------|-------------|
| **einzeln** | one key, e.g. `Esc` |
| **kombination** | several kbd elements with a "+" between them |

## Features

- Key cap with a border and a light shadow, like a key surface
- Modifiers (`Ctrl`, `Alt`, `⇧`) as their own caps
- `active` shows the state that is currently pressed

## Distinction

- **Do not confuse with** `code`: code snippets are running text in monospace;
  kbd is a key.

- **Do not confuse with** [badge](../../feedback/badge/): a badge shows status,
  not a key.

- Always set keyboard shortcuts as a combination of kbd elements, not as one
  block of text.

## Best Practices

- Name them correctly per language (German `Strg`, English `Ctrl`) – the caption
  follows the UI language.

- In tooltips: kbd on the right side of the text, with a gap.
- No more than three modifiers plus one key.

## See also

- [Tooltip](../../../widgets/overlays/tooltip/)
- [Command](../../../widgets/navigation/command/) – find and run shortcuts
- [Base component](../base.md)
