# Audio - Erscheinungsbild

## Grundlayout

Audio-Elemente zeigen Bedienknöpfe, eine Fortschrittsleiste und eine Zeitanzeige.

## Varianten
### kompakt
```
┌──────────────────────────────┐
│ [▶]  ▓▓▓▓▓▓▓▓░░░░░  1:23 / 3:45  │
└──────────────────────────────┘
```
### standard
```
┌─────────────────────────────────────────┐
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ [🔊 80%]                                │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░  │
│ 0:00                                              3:45 │
└─────────────────────────────────────────┘
```
### minimal
```
┌──────────────┐
│ [▶] [🔊]    │
└──────────────┘
```

| Icon | Funktion |
|------|----------|
| ⏯️ | Abspielen/Pause (Umschalter) |
| ⏭️ | nächster Titel |
| ⏮️ | vorheriger Titel |
| 🔊 | Lautstärke |
| 🔇 | stummschalten |
| 🔄 | Wiederholen |
| 📋 | Playlist |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| compact | 32px | inline, Chat, Listen |
| small | 48px | Karten, Panels |
| medium | 64px | Standard |
| large | 80px | hervorgehobenes Audio |
| XL | 120px | Audio als Blickfang |

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
| `scale` | vergrößert die Bedienelemente (1,1-fach) |
| `color` | die Farbe ändert sich |
| `shadow` | der Schatten wird stärker |
| `opacity` | die Deckkraft ändert sich |

## Responsiv

| Breakpoint | Verhalten |
|------------|-----------|
| Desktop (>768px) | alle Bedienelemente sichtbar |
| Tablet (480–768px) | kompaktes Layout |
| Mobil (<480px) | minimales Layout |

## Gestaltung der Fortschrittsleiste

```css
.audio-progress {
  background: var(--track-color);
}

.audio-progress-fill {
  background: var(--progress-color);
  transition: width 0.1s ease;
}
```
