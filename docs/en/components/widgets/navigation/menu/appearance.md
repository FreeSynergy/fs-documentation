# Menu (Menü) - Appearance

## Base layout

Ein Menu ist eine klickbare Menüleiste, die oft oben platziert wird.

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
| **Active** | Primärfarbe | Aktiver Menüpunkt |
| **Inactive** | Grau | Inaktive Menüpunkte |
| **Hover** | Heller | hover state |
| **Disabled** | ausgegraut | Deaktivierte Menüpunkte |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `color` | the colour changes |
| `background` | Hintergrund ändert sich |
| `border-bottom` | an underline appears |
| `shadow` | Schatten erscheint |

## Responsive

| Breakpoint | Behaviour |
| ------------ | ----------- |
| Desktop (>768px) | Volles Menu sichtbar |
| Mobile (<480px) | Hamburger-Menu |

## Dropdown-Menu

```
┌─────────────────────────────────────────┐
│ Home │ About ▼ │ Services ▼ │ Contact   │
├─────────────────────────────────────────┤
│   Untermenü                             │
│   Untermenü 2                           │
└─────────────────────────────────────────┘
```
