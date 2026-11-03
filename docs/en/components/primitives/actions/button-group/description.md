# Button Group

| Field | Value |
|-------|-------|
| **Category** | `actions` |
| **Inherits from** | `base` |
| **Variants** | `verbund`, `segment`, `split` |
| **States** | `selected` (segment active) |
| **Gestures** | `tap` |
| **Animations** | `press`, `highlight` |
| **Related** | `toolbar`, `tabs`, `tags-input`, `button`, `base` |
| **Status** | documented |

## Description

A button group brings related buttons together into one visual and logical
unit. The belonging is already recognisable from the way the surfaces are joined.

## Purpose

- Alternatives that can be carried out together (font style, alignment)
- Exactly-one choice without its own dropdown (segmented control)
- Main action with an extended offering (split button with dropdown arrow)

## Variants

| Variant | Description |
|---------|-------------|
| **verbund** | buttons lined up next to each other, shared outer corners, but several independent actions |
| **segment** | segmented control, exactly one segment is active |
| **split** | main action plus a separated dropdown arrow with further options |

## Features

- Shared height and edges of the group elements
- Selection behaviour either single or multiple
- Can be arranged horizontally or vertically

## Distinction

- **Do not confuse with** [toolbar](../../../widgets/navigation/toolbar/): a toolbar
  gathers independent tools, a group shares one value or one action.

- **Do not confuse with** [tabs](../../../widgets/navigation/tabs/): tabs switch
  views, segments set a property.

- **Do not confuse with** [tags-input](../../fields/tags-input/): there records are
  created, here actions or properties are chosen.

## Best Practices

- At most five segments, otherwise use `select`.
- Label segments rather than only using icons, unless the icons are unambiguous
  (alignment, volume).

- Split buttons only when the main action is unambiguous.
- Mark the selection state with `aria-pressed`/`aria-checked` in addition to colour.

## See also

- [Button](../button/)
- [Toolbar](../../../widgets/navigation/toolbar/)
- [Tabs](../../../widgets/navigation/tabs/)
- [Base component](../../basics/base.md)
