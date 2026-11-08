# Video - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `src` | string | - | Video-URL |
| `controls` | boolean | `true` | Bedienelemente anzeigen? |
| `autoplay` | boolean | `false` | automatisch abspielen? |
| `muted` | boolean | `false` | stumm? |
| `loop` | boolean | `false` | wiederholen? |
| `poster` | string | - | Vorschaubild |
| `playsInline` | boolean | `false` | Wiedergabe im Inline-Modus (Mobil)? |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onPlay` | function | wird beim Start ausgeführt |
| `onPause` | function | wird beim Pausieren ausgeführt |
| `onEnded` | function | wird am Ende ausgeführt |
| `onTimeUpdate` | function | wird bei einer Zeitaktualisierung ausgeführt |

## Darstellung
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | responsives Layout? |
| `aspectRatio` | string | Seitenverhältnis (z. B. "16/9") |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showLoading` | boolean | Ladezustand anzeigen? |
| `fadeIn` | boolean | Einblenden anzeigen? |
| `fadeInDuration` | number | Dauer in ms |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onLoad` | function | wird ausgeführt, wenn das Video geladen ist |
| `onError` | function | wird bei einem Fehler ausgeführt |
| `onFullscreenChange` | function | wird ausgeführt, wenn sich der Vollbildzustand ändert |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-live` | string | Live-Ansage |
| `captions` | string | URL der Untertitel |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showPlayPause` | boolean | Abspielen/Pause-Knopf anzeigen? |
| `showSkip` | boolean | Vor-/Zurück-Knöpfe anzeigen? |
| `showVolume` | boolean | Lautstärkeregler anzeigen? |
| `showProgress` | boolean | Fortschrittsleiste anzeigen? |
| `showTime` | boolean | Zeitanzeige anzeigen? |
| `showFullscreen` | boolean | Vollbild-Knopf anzeigen? |

## Playlist-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `playlist` | array[] | Array mit Video-Objekten |
| `shuffle` | boolean | Zufallswiedergabe? |
| `currentIndex` | number | Index des aktuellen Videos |

## Video-spezifische Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `crossorigin` | string | CORS-Attribut |
| `preload` | enum | `auto`, `metadata`, `none` |
| `poster` | string | URL des Vorschaubildes |
| `quality` | enum | Standardqualität |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
