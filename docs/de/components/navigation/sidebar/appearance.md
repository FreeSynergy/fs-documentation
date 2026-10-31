# Sidebar - Aussehen

## Grundlayout

```
┌─────────────┐
│  Logo/Title │
├─────────────┤
│  📩 Mail    │
│  📅 Kalend. │
│  👥 Kont.   │
├─────────────┤
│  📝 Wiki    │
│  💬 Chat    │
│  📋 Tasks   │
├─────────────┤
│  ─────────  │
│  👤 User    │
│  ⚙️ Einst.  │
└─────────────┘
```

## Farben & Styling

| Element | Farbe | Hinweis |
|---------|-------|---------|
| Hintergrund | `--sidebar-bg` | Meist dunkler als Hauptinhalt |
| Text | `--sidebar-text` | Kontrast zum Hintergrund |
| Hover | `--sidebar-hover` | subtile Hervorhebung |
| Active | `--sidebar-active` | deutliche Markierung |
| Divider | `--sidebar-divider` | Trennlinie zwischen Gruppen |

## Abstände (Spacing)

```
Sidebar width: 240px (Desktop)
              64px (collapsed)
              100% (mobile overlay)

Item padding:   12px 16px
Group margin:   8px top/bottom
Icon size:      20px
Text size:      14px
```

## Responsive Verhalten

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volle Sidebar sichtbar |
| Tablet (480-768px) | Optional collapsed oder Drawer |
| Mobile (<480px) | Drawer oder Bottom Navigation |
