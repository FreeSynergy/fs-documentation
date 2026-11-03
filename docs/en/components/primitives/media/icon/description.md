# Icon

| Field | Value |
|-------|-------|
| **Category** | `media` |
| **Inherits from** | `base` |
| **Variants** | `outline`, `gefüllt`, `animiert` |
| **States** | `aktiv` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `pulse`, `spin`, `highlight` |
| **Related** | `avatar`, `button`, `badge`, `image`, `emoji-picker` |
| **Status** | documented |

## Description
An icon is a symbolic graphic element that visually represents a function or an
object. Unlike icons in other contexts (e.g. an avatar), the icons here stand
generically for functions, file types or actions.

## Purpose

- Mark functions visually (e.g. 🏠 for "Home")
- Show file types (e.g. 📄 for PDF, 📸 for images)
- Symbolise actions (e.g. ✏️ for edit, 🗑️ for delete)

## Variants

| Variant | Description |
|---------|-------------|
| **outline** | line drawing, standard in toolbars |
| **gefüllt** | active or emphasised presentation |
| **animiert** | moves (`spin`, `pulse`), e.g. loading or sending |

Shape and size are not variants but the attributes `shape` and `size`.

## Features

- SVG, so it scales without steps and can be coloured via the text colour
- One set per application, mixed sets look restless
- Alt text or `aria-label` when the icon carries the only information
- Purely decorative icons are hidden from screen readers

## Distinction

- **Do not confuse with** [avatar](../../../widgets/data/avatar/): an avatar represents a subject,
  an icon a function or a file type.
- **Do not confuse with** emojis from the [emoji-picker](../../../widgets/fields/emoji-picker/): emojis are
  content, icons are the user interface.
- **Do not confuse with** [image](../image/): icons are small, monochrome and part of the surface.
- A clickable icon is not an icon element on its own, but a
  [button](../../actions/button/) in the icon-only variant.

## Best Practices

- Consistent icon size within one component
- Ensure contrast against the background
- Hover effect for interactive icons
- Alt text for accessibility

## Shape variants

| Shape | Description | Use |
|-------|-------------|-----|
| **circular** | round shape | buttons, avatars, status indicators |
| **square** | square shape | icons in grids, list items |
| **rectangular** | rectangular shape | toolbar icons, tab icons |
| **hexagonal** | hexagonal shape | special status icons, decorations |
| **pill** | rounded rectangle | tags, badges, chips |

## Size variants

| Size | Pixels | Use |
|------|--------|-----|
| small | 16px | inline icons, list items |
| medium | 24px | navigation, buttons |
| large | 32px | cards, panels |
| XL | 48px | hero sections, featured items |
| XXL | 64px+ | hero areas, landing pages |

## Colour variants

| Colour | Use |
|--------|-----|
| **primary** | main colour of the application |
| **secondary** | secondary actions |
| **success** | success messages |
| **warning** | warnings |
| **error** | error messages |
| **neutral** | ordinary icons |

## See also

- [media – overview](../index.md)
- [Button](../../actions/button/) — icon-only buttons
- [Avatar](../../../widgets/data/avatar/) — people instead of functions
- [Base component](../../basics/base.md)
