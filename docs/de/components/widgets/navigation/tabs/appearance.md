# Tabs - Aussehen

## Grundlayout

Tabs sind Reiter zum Umschalten zwischen Ansichten. Sie können horizontal oder vertikal platziert werden.

## Varianten
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

| Variant | Beschreibung | CSS |
|---------|-------------|-----|
| **Default** | Standard-Reiter | `border-radius: 4px 4px 0 0` |
| **Pill** | Pillenform | `border-radius: 999px` |
| **Card** | In Karte integriert | `border-radius: 8px` |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Small | 32px | Inline-Tabs |
| Medium | 48px | Standard-Tabs |
| Large | 64px | Featured-Tabs |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktiver Tab |
| **Inactive** | Grau | Inaktiver Tab |
| **Hover** | Heller | Hover-Zustand |
| **Disabled** |ausgegraut | Deaktivierte Tabs |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `border-bottom` | Unterstrich erscheint |
| `scale` | Leichte Vergrößerung |
| `shadow` | Schatten erscheint |

## Reaktiv

| Breakpoint | Verhalten |
|------------|-----------|
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
