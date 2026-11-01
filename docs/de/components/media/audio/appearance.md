# Audio - Aussehen

## Grundlayout

Audio-Elemente zeigen Steuerungsknöpfe, Fortschrittsbalken und Zeitanzeige an.

## Varianten
### Compact (Kompakt)
```
┌──────────────────────────────┐
│ [▶]  ▓▓▓▓▓▓▓▓░░░░░  1:23 / 3:45  │
└──────────────────────────────┘
```
### Standard (Standard)
```
┌─────────────────────────────────────────┐
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ [🔊 80%]                                │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░  │
│ 0:00                                              3:45 │
└─────────────────────────────────────────┘
```
### Minimal (Minimal)
```
┌──────────────┐
│ [▶] [🔊]    │
└──────────────┘
```

| Icon | Funktion |
|------|----------|
| ⏯️ | Play/Pause (Toggle) |
| ⏭️ | Nächster Track |
| ⏮️ | Vorheriger Track |
| 🔊 | Lautstärke |
| 🔇 | Stumm |
| 🔄 | Wiederholen |
| 📋 | Wiedergabeliste |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Compact | 32px | Inline, Chat, Listen |
| Small | 48px | Cards, Panels |
| Medium | 64px | Standard |
| Large | 80px | Featured-Audio |
| XL | 120px | Hero-Audio |

## Farben und Zustände

```css
.audio-player {
  --primary-color: var(--primary-color);
  --secondary-color: var(--secondary-color);
  --hover-color: var(--hover-color);
  --progress-color: var(--primary-color);
  --track-color: var(--track-color);
}
```

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `scale` | Controls skaliert (1.1x) |
| `color` | Farbe ändert sich |
| `shadow` | Schatten wird stärker |
| `opacity` | Deckkraft ändert sich |

## Reaktiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | Volle Steuerung sichtbar |
| Tablet (480-768px) | Kompakt-Layout |
| Mobile (<480px) | Minimal-Layout |

## Progress Bar Styling

```css
.audio-progress {
  background: var(--track-color);
}

.audio-progress-fill {
  background: var(--progress-color);
  transition: width 0.1s ease;
}
```
