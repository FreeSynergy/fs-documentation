# Tabs - Aussehen

## Grundlayout

Tabs sind Reiter zum Umschalten zwischen Ansichten. Sie können horizontal oder vertikal platziert werden.

## Layout-Varianten

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

## Form-Varianten

| Variant | Beschreibung | CSS |
|---------|-------------|-----|
| **Default** | Standard-Reiter | `border-radius: 4px 4px 0 0` |
| **Pill** | Pillenform | `border-radius: 999px` |
| **Card** | In Karte integriert | `border-radius: 8px` |

## Größe-Varianten

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Small | 32px | Inline-Tabs |
| Medium | 48px | Standard-Tabs |
| Large | 64px | Featured-Tabs |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktiver Tab |
| **Inactive** | Grau | Inaktiver Tab |
| **Hover** | Heller | Hover-Zustand |
| **Disabled** |ausgegraut | Deaktivierte Tabs |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `border-bottom` | Unterstrich erscheint |
| `scale` | Leichte Vergrößerung |
| `shadow` | Schatten erscheint |

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

## Responsive Verhalten

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volle Tabs sichtbar |
| Tablet (480-768px) | Scrollable Tabs |
| Mobile (<480px) | Drawer oder Accordion |
