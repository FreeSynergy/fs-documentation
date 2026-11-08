# Video - Erscheinungsbild

## Grundlayout

Videoplayer zeigen Bedienknöpfe, eine Fortschrittsleiste, Lautstärke und Zeit.

## Varianten

### kompakt

```
┌─────────────────────────────────────────┐
│ [▶]  ▓▓▓▓▓▓▓▓░░░░░░  1:23 / 3:45       │
└─────────────────────────────────────────┘
```

### standard

```
┌─────────────────────────────────────────┐
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [🔊 80%]  0:00                3:45      │
│                                         │
└─────────────────────────────────────────┘
```

### minimal

```
┌─────────────────────────────────────────┐
│ [▶] [🔊]                               │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| small | 320px | Videos inline, Kommentare |
| medium | 640px | Karten, Panels |
| large | 1280px | hervorgehobene Videos |
| full | 1920px | Videos als Blickfang, Vollbild |

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
| `scale` | vergrößert die Bedienelemente (1,1-fach) |
| `opacity` | die Deckkraft ändert sich |
| `border` | der Rand leuchtet auf |

## Responsiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | alle Bedienelemente sichtbar |
| Tablet (480–768px) | kompaktes Layout |
| Mobil (<480px) | minimales Layout |

## Bedienknöpfe

| Knopf | Icon | Funktion |
|-------|------|----------|
| Play/Pause | ▶️ / ⏸️ | Wiedergabe starten/anhalten |
| zurück | ⏮️ | vorheriges Video (Playlist) |
| weiter | ⏭️ | nächstes Video (Playlist) |
| Lautstärke | 🔊 | Lautstärke |
| stumm | 🔇 | stummschalten |
| Vollbild | ⛶ | Vollbild |
| Einstellungen | ⚙️ | Einstellungen |

## Fortschrittsleiste

```
┌─────────────────────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░   │
│ ▲                                       │
│ Hover-Tooltip (0:30)                    │
└─────────────────────────────────────────┘
```

## Overlay-Elemente

### Lade-Overlay

```
┌─────────────────────────────────────────┐
│                                         │
│      🔄                                 │
│      Lädt...                            │
│                                         │
└─────────────────────────────────────────┘
```

### Info-Overlay

```
┌─────────────────────────────────────────┐
│                                         │
│   🖼️                                   │
│   Titel                                 │
│   Beschreibung                          │
│                                         │
└─────────────────────────────────────────┘
```
