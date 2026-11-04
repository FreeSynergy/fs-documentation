# Tabs - Appearance

## Base layout

Tabs are tabs for switching between views. They can be placed horizontally or vertically.

## Variants
### Horizontal (Standard)
```
┌─────────────────────────────────────────────────────┐
│ Tab 1 │ Tab 2 │ Tab 3 │ Tab 4                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│   Content of the active tab                        │
│                                                     │
└─────────────────────────────────────────────────────┘
```
### Vertical (side)
```
┌────────┬──────────────────────────────────────────┐
│ Tab 1  │                                          │
│ Tab 2  │   Content of the active tab              │
│ Tab 3  │                                          │
│ Tab 4  │                                          │
└────────┴──────────────────────────────────────────┘
```

| Variant | Description | CSS |
| --------- | ------------- | ----- |
| **Default** | Standard-Reiter | `border-radius: 4px 4px 0 0` |
| **Pill** | Pillenform | `border-radius: 999px` |
| **Card** | In Karte integriert | `border-radius: 8px` |

## Sizes

| Size | Height | Use |
| ------- | ------ | ------------ |
| Small | 32px | Inline-Tabs |
| Medium | 48px | Standard-Tabs |
| Large | 64px | Featured-Tabs |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Active** | primary colour | active tab |
| **Inactive** | grey | inactive tab |
| **Hover** | lighter | hover state |
| **Disabled** | greyed out | disabled tabs |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `color` | the colour changes |
| `border-bottom` | an underline appears |
| `scale` | slight enlargement |
| `shadow` | a shadow appears |

## Responsive

| Breakpoint | Behaviour |
| ------------ | ----------- |
| Desktop (>768px) | full tabs visible |
| Tablet (480-768px) | scrollable tabs |
| Mobile (<480px) | drawer or accordion |

## Active-Indicator

```
┌─────────────────────────────────────────────────────┐
│ Tab 1 │ Tab 2 │ Tab 3 │ Tab 4                      │
│ ━━━━━━                                      │
└─────────────────────────────────────────────────────┘
```

## Closable-Tabs

```
┌─────────────────────────────────────────────────────┐
│ Tab 1 ✕ │ Tab 2 ✕ │ Tab 3                         │
├─────────────────────────────────────────────────────┤
│                                                     │
└─────────────────────────────────────────────────────┘
```
