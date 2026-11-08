# Audio - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `src` | string | - | URL des Audios |
| `controls` | boolean | `true` | Bedienelemente anzeigen? |
| `autoplay` | boolean | `false` | automatisch abspielen? |
| `muted` | boolean | `false` | stumm? |
| `loop` | boolean | `false` | wiederholen? |
| `volume` | number | `0.8` | Lautstärke (0–1) |
| `currentTime` | number | `0` | Startzeit in Sekunden |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onPlay` | function | wird beim Start ausgeführt |
| `onPause` | function | wird beim Pausieren ausgeführt |
| `onTimeUpdate` | function | wird bei einer Zeitaktualisierung ausgeführt |
| `onEnded` | function | wird am Ende ausgeführt |
| `onVolumeChange` | function | wird ausgeführt, wenn sich die Lautstärke ändert |

## Darstellung
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showVisualizer` | boolean | Audio-Visualisierung anzeigen? |
| `visualizerStyle` | enum | Stil: `bars`, `waves`, `circle` |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | responsives Layout verwenden? |
| `compactOnMobile` | boolean | kompaktes Layout auf dem Smartphone? |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-live` | string | Live-Ansage: `polite`, `assertive` |

## Playlist-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `playlist` | array[] | Array mit Audio-Objekten |
| `shuffle` | boolean | Zufallswiedergabe? |
| `currentIndex` | number | Index des aktuellen Titels |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showPlayPause` | boolean | Abspielen/Pause-Knopf anzeigen? |
| `showSkip` | boolean | Vor-/Zurück-Knöpfe anzeigen? |
| `showVolume` | boolean | Lautstärkeregler anzeigen? |
| `showProgress` | boolean | Fortschrittsleiste anzeigen? |
| `showTime` | boolean | Zeitanzeige anzeigen? |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
