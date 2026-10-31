# Menu (Menü) - Aussehen

## Grundlayout

Ein Menu ist eine klickbare Menüleiste, die oft oben platziert wird.

## Layout-Varianten

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

## Dropdown-Menu

```
┌─────────────────────────────────────────┐
│ Home │ About ▼ │ Services ▼ │ Contact   │
├─────────────────────────────────────────┤
│   Untermenü                             │
│   Untermenü 2                           │
└─────────────────────────────────────────┘
```

## Größe-Varianten

| Größe | Höhe | Schriftgröße | Verwendung |
|-------|------|-------------|------------|
| Small | 32px | 12px | Inline |
| Medium | 48px | 14px | Standard |
| Large | 64px | 16px | Featured |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktiver Menüpunkt |
| **Inactive** | Grau | Inaktive Menüpunkte |
| **Hover** | Heller | Hover-Zustand |
| **Disabled** |ausgegraut | Deaktivierte Menüpunkte |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `background` | Hintergrund ändert sich |
| `border-bottom` | Unterstrich erscheint |
| `shadow` | Schatten erscheint |

## Responsive Verhalten

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volles Menu sichtbar |
| Mobile (<480px) | Hamburger-Menu |
