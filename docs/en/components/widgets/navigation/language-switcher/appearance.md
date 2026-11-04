# Language Switcher - Appearance

## Base layout

A language switcher shows the current language and allows switching.

## Variants

### Dropdown

```
┌─────────────────────────────────────────┐
│ 🇩🇪 Deutsch ▼                            │
├─────────────────────────────────────────┤
│ 🇬🇧 English                              │
│ 🇫🇷 Français                             │
│ 🇪🇸 Español                              │
└─────────────────────────────────────────┘
```

### Buttons

```
┌─────────────────────────────────────────┐
│ 🇩🇪  🇬🇧  🇫🇷  🇪🇸                         │
└─────────────────────────────────────────┘
```

### Icons

```
┌─────────────────────────────────────────┐
│ [🇩🇪] [🇬🇧] [🇫🇷]                         │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Use |
|------|-----|
| Small | in the header bar (24px) |
| Medium | in the settings (48px) |
| Large | on the start page (64px) |

## Colours and states

| State | Colour | Description |
|-------|--------|-------------|
| **Default** | normal | standard style |
| **Active** | primary colour | active language |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement |
| `color` | the colour changes |
| `shadow` | the shadow gets stronger |

## Responsive

- In the header and toolbar the switch sits in `small`; if space gets tight, only the
  language code (`DE`) remains and the name is dropped.
- On narrow screens the button row switches to the variant `kombiniert`; the remaining
  languages sit in the drop-down.
- Longer language names (`Español`, `Português`) are not truncated, they determine the
  width of the switch — which is why bars prefer the code.
