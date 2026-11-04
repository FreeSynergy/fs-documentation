# Menu - Appearance

## Base layout

A menu is a clickable menu bar, often placed at the top.

## Variants

### Horizontal (Standard)

```
┌─────────────────────────────────────────┐
│ Home │ About │ Services │ Contact       │
└─────────────────────────────────────────┘
```

### Vertical (Sidebar)

```
┌─────────┐
│ Home    │
│ About   │
│ Services│
│ Contact │
└─────────┘
```

## Sizes

| Size | Height | Font size | Use |
| ------- | ------ | ------------- | ------------ |
| Small | 32px | 12px | Inline |
| Medium | 48px | 14px | Standard |
| Large | 64px | 16px | Featured |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Active** | primary colour | active menu item |
| **Inactive** | grey | inactive menu items |
| **Hover** | lighter | hover state |
| **Disabled** | greyed out | disabled menu items |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `color` | the colour changes |
| `background` | the background changes |
| `border-bottom` | an underline appears |
| `shadow` | a shadow appears |

## Responsive

| Breakpoint | Behaviour |
| ------------ | ----------- |
| Desktop (>768px) | full menu visible |
| Mobile (<480px) | hamburger menu |

## Dropdown menu

```
┌─────────────────────────────────────────┐
│ Home │ About ▼ │ Services ▼ │ Contact   │
├─────────────────────────────────────────┤
│   Submenu                               │
│   Submenu 2                             │
└─────────────────────────────────────────┘
```
