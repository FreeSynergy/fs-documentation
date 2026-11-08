# Media Player - Erscheinungsbild

## Grundlayout

Ein Media Player spielt Videos und Audio ab.

## Varianten

### Videoplayer

```
┌─────────────────────────────────────────┐
│                                         │
│      📽️                                │
│      (Videoplayer)                      │
│                                         │
│      [▶] [⏸] [Lautstärke] [Vollbild]   │
└─────────────────────────────────────────┘
```

### Audioplayer

```
┌─────────────────────────────────────────┐
│  [▶] [⏸] [Lautstärke] [Fortschritt]  0:00 │
└─────────────────────────────────────────┘
```

## Größen

| Größe | Breite/Höhe | Verwendung |
|-------|-------------|------------|
| Small | 320x180px | inline |
| Medium | 640x360px | Standard |
| Large | 1280x720px | hervorgehoben |
| Full | 100% | volle Breite |

## Farben und Zustände

| Zustand | Farbe | Beschreibung |
|---------|-------|--------------|
| **Background** | schwarz/dunkel | Hintergrund |
| **Controls** | weiß/hell | Bedienelemente |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `controls` | die Bedienelemente erscheinen |
| `shadow` | stärkerer Schatten |

## Responsiv

- Die Fläche behält das Seitenverhältnis der Datei (meist 16:9) und skaliert mit der Breite;
  `Full` füllt den Viewport, die Bedienleiste bleibt darunter oder darüber.
- Unterhalb einer kleinen Bildschirmbreite (`small`) wird die Playlist unter die Fläche gesetzt,
  und die Lautstärke macht Platz für den Untertitel-Knopf.
- Die Bedienelemente blenden beim Abspielen nach drei Sekunden aus (`fade-out`) und erscheinen
  bei Mausbewegung, Fokus oder Tastendruck wieder.

## Bedienelemente

| Bedienelement | Funktion |
|---------------|----------|
| **Play/Pause** | Wiedergabe starten/anhalten |
| **Lautstärke** | Lautstärke |
| **Fortschritt** | Fortschrittsleiste |
| **Vollbild** | Vollbild |
| **Untertitel** | Untertitel |

## Playlist

```
┌─────────────────────────────────────────┐
│ [▶]  Titel 1                            │
│ [⏸]  Titel 2                            │
│ [⏸]  Titel 3                            │
└─────────────────────────────────────────┘
```
