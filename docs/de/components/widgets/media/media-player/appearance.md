# Media Player - Aussehen

## Grundlayout

Ein Media Player wiedergibt Videos und Audios.

## Varianten

### Video Player

```
┌─────────────────────────────────────────┐
│                                         │
│      📽️                                │
│      (Video-Player)                     │
│                                         │
│      [▶] [⏸] [Volume] [Fullscreen]     │
└─────────────────────────────────────────┘
```

### Audio Player

```
┌─────────────────────────────────────────┐
│  [▶] [⏸] [Volume] [Progress]  0:00     │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Small | 320x180px | Inline |
| Medium | 640x360px | Standard |
| Large | 1280x720px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Background** | Schwarz/Dunkel | Hintergrund |
| **Controls** | Weiß/Licht | Steuerungselemente |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `controls` | Controls erscheinen |
| `shadow` | Schatten stärker |

## Reaktiv

- Die Fläche hält das Seitenverhältnis der Datei (meist 16:9) und skaliert mit der Breite;
  `Full` füllt den Viewport, die Steuerleiste bleibt darunter oder darüber.
- Unter `small` Bildschirmbreite wird die Playlist unter die Fläche gesetzt und die
  Lautstärke weicht dem Untertitel-Knopf.
- Die Steuerung blendet im Spielzustand nach drei Sekunden aus (`fade-out`) und kommt bei
  Zeigerbewegung, Fokus oder Tastendruck zurück.

## Controls

| Control | Funktion |
|---------|----------|
| **Play/Pause** | Wiedergabe starten/pausieren |
| **Volume** | Lautstärke |
| **Progress** | Fortschrittsbalken |
| **Fullscreen** | Vollbild |
| **Captions** | Untertitel |

## Playlist

```
┌─────────────────────────────────────────┐
│ [▶]  Titel 1                            │
│ [⏸]  Titel 2                            │
│ [⏸]  Titel 3                            │
└─────────────────────────────────────────┘
```
