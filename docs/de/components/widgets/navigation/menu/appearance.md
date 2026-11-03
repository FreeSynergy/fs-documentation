# Menu (Menü) - Aussehen

## Grundlayout

Ein Menu ist eine klickbare Menüleiste, die oft oben platziert wird.

## Varianten

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

## Größen

| Größe | Höhe | Schriftgröße | Verwendung |
|-------|------|-------------|------------|
| Small | 32px | 12px | Inline |
| Medium | 48px | 14px | Standard |
| Large | 64px | 16px | Featured |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktiver Menüpunkt |
| **Inactive** | Grau | Inaktive Menüpunkte |
| **Hover** | Heller | Hover-Zustand |
| **Disabled** |ausgegraut | Deaktivierte Menüpunkte |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `background` | Hintergrund ändert sich |
| `border-bottom` | Unterstrich erscheint |
| `shadow` | Schatten erscheint |

## Reaktiv

| Breakpoint | Verhalten |
|------------|-----------|
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
