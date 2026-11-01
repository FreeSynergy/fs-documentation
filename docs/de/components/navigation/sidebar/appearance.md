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

## Varianten

| Variante | Aussehen |
|----------|----------|
| **angeheftet** | volle Breite mit Namen, Inhalt rückt daneben |
| **ikonenleiste** | schmaler Streifen mit Symbolen, kein Text |
| **einklappbar** | breit, Klappknopf im Kopf; zugeklappt wie `ikonenleiste` |

## Größen

| Größe | Breite | Icon | Schrift | Verwendung |
|-------|--------|------|---------|------------|
| Desktop | 240 px | 20 px | 14 px | Standard |
| eingeklappt | 64 px | 20 px | – | Ikonenleiste |
| mobil | 100 % | 20 px | 14 px | Overlay (Drawer) |

Abstände pro Punkt: 12 px oben/unten, 16 px links; Gruppenaustand 8 px.

## Farben und Zustände

| Element | Farbe | Hinweis |
|---------|-------|---------|
| Hintergrund | `--sidebar-bg` | Meist dunkler als Hauptinhalt |
| Text | `--sidebar-text` | Kontrast zum Hintergrund |
| Hover | `--sidebar-hover` | subtile Hervorhebung |
| Active | `--sidebar-active` | deutliche Markierung |
| Divider | `--sidebar-divider` | Trennlinie zwischen Gruppen |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Punkt bekommt eine Fläche, Text bleibt lesbar |
| `ring` | Fokus-Ring bei Tastaturnavigation |
| `tooltip` | Name erscheint bei Hover an der Ikonenleiste |
| `indicator` | schmaler Balken am linken Rand des aktiven Punkts |

## Reaktiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volle Sidebar sichtbar |
| Tablet (480-768px) | Optional collapsed oder Drawer |
| Mobile (<480px) | Drawer oder Bottom Navigation |

Die Leiste scrollt eigenständig (`scroll-area`), Kopf- und Fußbereich bleiben stehen.
- Beim Einklappen schrumpft die Breite, die Schrift verschwindet zuerst, Symbole bleiben
  an derselben Stelle (`expand`/`collapse`).
- Unter 480 px wird die Leiste zum Overlay ohne Restbreite; der Inhalt rückt nicht mehr.
