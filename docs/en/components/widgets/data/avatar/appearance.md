# Avatar - Appearance

## Base layout

Avatars are visual representations of users that can be shown in different shapes and
sizes.

## Variants

```css
/* Circular - standard */
.avatar-circular {
  border-radius: 50%;
  aspect-ratio: 1 / 1;
}

/* Square */
.avatar-square {
  border-radius: 4px;
}

/* Pill */
.avatar-pill {
  border-radius: 999px;
  aspect-ratio: auto;
}
```

## Sizes

| Size | Pixels | Use |
|------|--------|-----|
| XSmall | 24px | in list items, minimal chat |
| Small | 32px | standard in lists |
| Medium | 48px | profiles, cards |
| Large | 64px | featured profiles |
| XL | 96px | generous display |
| XXL | 128px+ | hero sections |

## Colours and states

| Colour | Initials |
|--------|----------|
| blue | A-D |
| green | E-H |
| orange | I-L |
| red | M-P |
| pink | Q-T |
| purple | U-Z |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `zoom` | the avatar grows slightly (1.1x) |
| `border` | the border lights up |
| `shadow` | the shadow becomes stronger |
| `none` | no effect |

## Responsive

- In lists the avatar stays constant at `small` (32 px), even on narrow screens;
  it only grows in profile displays.
- The click area around a small avatar grows to 44 px without the image size changing.
- If the image loads slowly, the initials fallback appears first and the photo then
  fades in with `fade-in`.

## Status badge positions

| Position | Description |
|----------|-------------|
| **Bottom-right** | bottom right (standard) |
| **Top-right** | top right |
| **Bottom-left** | bottom left |
| **Center** | in the middle |

## Styling attributes

| Attribute | Value | Description |
|-----------|-------|-------------|
| `size` | `xsmall`, `small`, `medium`, `large`, `xl`, `xxl` | size |
| `shape` | `circular`, `square`, `pill` | shape |
| `variant` | `image`, `initials`, `icon`, `placeholder` | content |
| `status` | `online`, `offline`, `away`, `busy`, `in-meeting` | status |
| `interactive` | `true`, `false` | clickable? |
