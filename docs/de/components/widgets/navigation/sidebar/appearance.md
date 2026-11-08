# Sidebar - Erscheinungsbild

## Grundaufbau

```
┌─────────────┐
│  Logo/Titel │
├─────────────┤
│  📩 Mail    │
│  📅 Kalender│
│  👥 Kontakte│
├─────────────┤
│  📝 Wiki    │
│  💬 Chat    │
│  📋 Aufgaben│
├─────────────┤
│  ─────────  │
│  👤 Nutzer  │
│  ⚙️ Einstell.│
└─────────────┘
```

## Varianten

| Variante | Erscheinungsbild |
| ---------- | ---------- |
| **angeheftet** | volle Breite mit Namen, der Inhalt rückt daneben |
| **ikonenleiste** | schmaler Streifen mit Icons, ohne Text |
| **einklappbar** | breit, Einklappknopf im Kopf; eingeklappt wie `ikonenleiste` |

## Größen

| Größe | Breite | Icon | Schrift | Verwendung |
|------------|-------|------|---------|-------------------|
| Desktop | 240 px | 20 px | 14 px | Standard |
| eingeklappt | 64 px | 20 px | – | Icon-Leiste |
| Mobil | 100 % | 20 px | 14 px | Overlay (Drawer) |

Abstand pro Punkt: 12 px oben/unten, 16 px links; Einrückung einer Gruppe 8 px.

## Farben und Zustände

| Element | Farbe | Hinweis |
|---------|-------|---------|
| Hintergrund | `--sidebar-bg` | meist dunkler als der Hauptinhalt |
| Text | `--sidebar-text` | Kontrast zum Hintergrund |
| Hover | `--sidebar-hover` | dezente Hervorhebung |
| Aktiv | `--sidebar-active` | deutliche Markierung |
| Trennlinie | `--sidebar-divider` | Trenner zwischen Gruppen |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
| -------- | -------------- |
| `background` | der Punkt bekommt eine gefüllte Fläche, der Text bleibt lesbar |
| `ring` | Fokusrahmen bei der Tastaturnavigation |
| `tooltip` | der Name erscheint beim Hover in der Icon-Leiste |
| `indicator` | schmaler Balken am linken Rand des aktiven Punkts |

## Responsives Verhalten

| Breakpoint | Verhalten |
| ------------ | ----------- |
| Desktop (>768px) | volle Sidebar sichtbar |
| Tablet (480–768px) | wahlweise eingeklappt oder als Drawer |
| Mobil (<480px) | Drawer oder untere Navigation |

Die Leiste scrollt unabhängig (`scroll-area`), Kopf- und Fußbereich bleiben an ihrem Platz.
- Beim Einklappen wird die Breite kleiner; der Text verschwindet zuerst, die Icons bleiben
  an derselben Stelle (`expand`/`collapse`).
- Unter 480 px wird die Leiste zum Overlay ohne verbleibende Breite; der Inhalt wird
  nicht mehr zur Seite geschoben.
