# Video - Aussehen

## Grundlayout

Video-Player zeigen Steuerungsknöpfe, Fortschrittsbalken, Lautstärke und Zeit an.

## Varianten

### Compact (Kompakt)

```
┌─────────────────────────────────────────┐
│ [▶]  ▓▓▓▓▓▓▓▓░░░░░░  1:23 / 3:45       │
└─────────────────────────────────────────┘
```

### Standard (Standard)

```
┌─────────────────────────────────────────┐
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [🔊 80%]  0:00                3:45      │
│                                         │
└─────────────────────────────────────────┘
```

### Minimal (Minimal)

```
┌─────────────────────────────────────────┐
│ [▶] [🔊]                               │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 320px | Inline-Videos, Kommentare |
| Medium | 640px | Cards, Panels |
| Large | 1280px | Featured-Videos |
| Full | 1920px | Hero-Videos, Fullscreen |

## Farben und Zustände

```css
.video-player {
  --primary-color: var(--primary-color);
  --secondary-color: var(--secondary-color);
  --hover-color: var(--hover-color);
  --progress-color: var(--primary-color);
  --track-color: rgba(255,255,255,0.3);
}
```

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Controls skaliert (1.1x) |
| `opacity` | Deckkraft ändert sich |
| `border` | Rand leuchtet auf |

## Reaktiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volle Steuerung sichtbar |
| Tablet (480-768px) | Kompakt-Layout |
| Mobile (<480px) | Minimal-Layout |

## Steuerungs-Buttons

| Button | Icon | Funktion |
|--------|------|----------|
| Play/Pause | ▶️ / ⏸️ | Wiedergabe starten/pausieren |
| Previous | ⏮️ | Vorheriges Video (Playlist) |
| Next | ⏭️ | Nächstes Video (Playlist) |
| Volume | 🔊 | Lautstärke |
| Mute | 🔇 | Stumm |
| Fullscreen | ⛶ | Vollbild |
| Settings | ⚙️ | Einstellungen |

## Progress Bar

```
┌─────────────────────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░   │
│ ▲                                       │
│ Hover-Tooltip (0:30)                    │
└─────────────────────────────────────────┘
```

## Overlay-Elemente

### Loading Overlay

```
┌─────────────────────────────────────────┐
│                                         │
│      🔄                                 │
│      Laden...                           │
│                                         │
└─────────────────────────────────────────┘
```

### Info Overlay

```
┌─────────────────────────────────────────┐
│                                         │
│   🖼️                                   │
│   Titel                                 │
│   Beschreibung                          │
│                                         │
└─────────────────────────────────────────┘
```
