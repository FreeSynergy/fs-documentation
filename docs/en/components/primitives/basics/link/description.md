# Link

| Field | Value |
|-------|-------|
| **Category** | `basics` |
| **Inherits from** | `base` |
| **Variants** | `standard`, `muted`, `icon`, `unterstrichen` |
| **States** | `visited`, `current` |
| **Gestures** | `tap` |
| **Animations** | `highlight` |
| **Related** | `button`, `breadcrumb`, `tabs`, `base` |
| **Status** | documented |

## Description

A link changes the address – it leads to another page, another object, or a
place inside the current view. It is the navigation element par excellence.

## Purpose

- Branching between objects (wiki articles, contacts, tasks)
- External references to websites and files
- Jump markers inside long documents

## Variants

| Variant | Description |
|---------|-------------|
| **standard** | text in the primary colour, underlined on hover |
| **muted** | secondary colour, for footers and meta lines |
| **icon** | icon before or after the text (e.g. an external arrow) |
| **unterstrichen** | underlined throughout (in running text) |

## Features

- `external` opens a new tab and marks that visibly
- Download references as their own case (`download`)
- Marking the current target in navigation (`aria-current`)

## Distinction

- **Do not confuse with** [button](../../actions/button/): a button triggers an
  action without changing the address.

- **Do not confuse with** [breadcrumb](../../../widgets/navigation/breadcrumb/): the
  breadcrumb shows a path, its entries are links.

- **Do not confuse with** [tabs](../../../widgets/navigation/tabs/): tabs switch a
  view within the same page.

## Best Practices

- The link text must be unambiguous without context ("privacy policy", not "here").
- In running text, always underline.
- Mark external links additionally in the text or with an icon plus `aria-label`.
- Icon-only links are not allowed.

## See also

- [Button](../../actions/button/)
- [Breadcrumb](../../../widgets/navigation/breadcrumb/)
- [Base component](../base.md)
