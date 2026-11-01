# Audio - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `src` | string | - | Audio-URL |
| `controls` | boolean | `true` | Steuerung anzeigen? |
| `autoplay` | boolean | `false` | Auto-Wiedergabe? |
| `muted` | boolean | `false` | Stumm? |
| `loop` | boolean | `false` | Wiederholen? |
| `volume` | number | `0.8` | Lautstärke (0-1) |
| `currentTime` | number | `0` | Startzeit in Sekunden |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onPlay` | function | Wird beim Start ausgeführt |
| `onPause` | function | Wird beim Pausieren ausgeführt |
| `onTimeUpdate` | function | Wird bei Zeitaktualisierung ausgeführt |
| `onEnded` | function | Wird beim Ende ausgeführt |
| `onVolumeChange` | function | Wird bei Lautstärkeänderung ausgeführt |

## Darstellung
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showVisualizer` | boolean | Audio-Visualizer anzeigen? |
| `visualizerStyle` | enum | Stil: `bars`, `waves`, `circle` |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | Responsive-Layout verwenden? |
| `compactOnMobile` | boolean | Kompakt-Layout auf Mobile? |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-live` | string | Live-Ankündigung: `polite`, `assertive` |

## Playlist-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `playlist` | array[] | Array von Audio-Objekten |
| `shuffle` | boolean | Zufällige Wiedergabe? |
| `currentIndex` | number | Aktueller Track-Index |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showPlayPause` | boolean | Play/Pause-Button anzeigen? |
| `showSkip` | boolean | Vor/Zurück-Buttons anzeigen? |
| `showVolume` | boolean | Lautstärkeregler anzeigen? |
| `showProgress` | boolean | Fortschrittsbalken anzeigen? |
| `showTime` | boolean | Zeitanzeige anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
