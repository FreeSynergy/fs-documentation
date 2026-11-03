# Tabs - Appearance

## Base layout

Tabs sind Reiter zum Umschalten zwischen Ansichten. Sie können horizontal oder vertikal platziert werden.

## Variants
### Horizontal (Standard)
```
┌─────────────────────────────────────────────────────┐
│ Tab 1 │ Tab 2 │ Tab 3 │ Tab 4                      │
├─────────────────────────────────────────────────────┤
│                                                     │
│   Inhalt der aktiven Tab                           │
│                                                     │
└─────────────────────────────────────────────────────┘
```
### Vertical (Seitlich)
```
┌────────┬──────────────────────────────────────────┐
│ Tab 1  │                                          │
│ Tab 2  │   Inhalt der aktiven Tab                │
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
| **Active** | Primärfarbe | Aktiver Tab |
| **Inactive** | Grau | Inaktiver Tab |
| **Hover** | Heller | hover state |
| **Disabled** | ausgegraut | Deaktivierte Tabs |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `color` | the colour changes |
| `border-bottom` | an underline appears |
| `scale` | Leichte Vergrößerung |
| `shadow` | Schatten erscheint |

## Responsive

| Breakpoint | Behaviour |
| ------------ | ----------- |
| Desktop (>768px) | Volle Tabs sichtbar |
| Tablet (480-768px) | Scrollable Tabs |
| Mobile (<480px) | Drawer oder Accordion |

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
