# Video - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `src` | string | - | Video-URL |
| `controls` | boolean | `true` | Steuerung anzeigen? |
| `autoplay` | boolean | `false` | Auto-Wiedergabe? |
| `muted` | boolean | `false` | Stumm? |
| `loop` | boolean | `false` | Wiederholen? |
| `poster` | string | - | Vorschaubild |
| `playsInline` | boolean | `false` | Inline-Wiedergabe (Mobile)? |

## Verhalten

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onPlay` | function | Wird beim Start ausgeführt |
| `onPause` | function | Wird beim Pausieren ausgeführt |
| `onEnded` | function | Wird beim Ende ausgeführt |
| `onTimeUpdate` | function | Wird bei Zeitaktualisierung ausgeführt |

## Darstellung
| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | Responsives Layout? |
| `aspectRatio` | string | Seitenverhältnis (z.B. "16/9") |

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showLoading` | boolean | Loading-Zustand anzeigen? |
| `fadeIn` | boolean | Einblendung anzeigen? |
| `fadeInDuration` | number | Dauer in ms |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onLoad` | function | Wird beim Laden des Videos ausgeführt |
| `onError` | function | Wird bei Fehler ausgeführt |
| `onFullscreenChange` | function | Wird bei Fullscreen-Wechsel ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-live` | string | Live-Ankündigung |
| `captions` | string | URL zu Untertiteln |

## Steuerungs-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showPlayPause` | boolean | Play/Pause-Button anzeigen? |
| `showSkip` | boolean | Vor/Zurück-Buttons anzeigen? |
| `showVolume` | boolean | Lautstärkeregler anzeigen? |
| `showProgress` | boolean | Fortschrittsbalken anzeigen? |
| `showTime` | boolean | Zeitanzeige anzeigen? |
| `showFullscreen` | boolean | Vollbild-Button anzeigen? |

## Playlist-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `playlist` | array[] | Array von Video-Objekten |
| `shuffle` | boolean | Zufällige Wiedergabe? |
| `currentIndex` | number | Aktueller Video-Index |

## Video-Spezifische Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `crossorigin` | string | CORS-Attribut |
| `preload` | enum | `auto`, `metadata`, `none` |
| `poster` | string | Vorschaubild-URL |
| `quality` | enum | Standardqualität |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
