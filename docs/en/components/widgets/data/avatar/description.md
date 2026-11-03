# Avatar

| Field | Value |
|-------|-------|
| **Category** | `data` |
| **Inherits from** | `base` |
| **Variants** | `image`, `initials`, `icon`, `placeholder` |
| **States** | `geladen`, `fehler` |
| **Gestures** | `tap`, `long-press` |
| **Animations** | `fade-in`, `lift` |
| **Related** | `icon`, `image`, `badge`, `list-view` |
| **Status** | documented |

## Description
An avatar is a visual representation element for a user. It can be a photo, initials
or an icon.

## Purpose

- Showing user profiles in lists and chat
- Activity indicator (who did what?)
- Assigning users in comments, tasks, etc.

## Variants

| Variant (`variant`) | Description |
|---------------------|-------------|
| **image** | photo of the person, falls back to initials on a loading error |
| **initials** | one or two letters of the display name |
| **icon** | symbol for groups, roles or automatic users |
| **placeholder** | neutral silhouette when nothing is known |

The shape is not a variant but is controlled through `shape` (`circular`, `square`,
`pill`) and `size`.

## Features

- Fallback chain: photo → initials → icon → placeholder
- Status badge (online, away, busy) at a fixed position
- An alternative name is mandatory, otherwise the avatar is empty for screen readers
- Clickable only when a contact card or profile follows (`interactive`)

## Distinction

- **Do not confuse with** [icon](../../../primitives/media/icon/): an icon stands for a command or a
  thing, an avatar represents a subject.
- **Do not confuse with** [image](../../../primitives/media/image/): images show content, avatars identify.
- The status badge next to an avatar is a [badge](../../../primitives/feedback/badge/), not part of the avatar.

## Best Practices

- Always give the avatar an alt text (the user's name)
- Fall back to initials when no image is available
- Keep the shape consistent within one application
- Hover effect for interactivity

## Status badges
Avatars can show status badges:

| Status | Colour | Description |
|--------|--------|-------------|
| **Online** | green | the user is online |
| **Offline** | grey | the user is offline |
| **Away** | orange | the user is away |
| **Busy** | red | the user is busy |
| **In-meeting** | blue | the user is in a meeting |

## Hover effects

- **Zoom**: the avatar grows slightly
- **Border**: the border lights up
- **Shadow**: the shadow becomes stronger

## See also

- [data – overview](../index.md)
- [Base component](../../../primitives/basics/base.md)
