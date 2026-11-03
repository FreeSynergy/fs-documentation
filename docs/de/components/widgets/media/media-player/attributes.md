# Media Player - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `src` | string | - | Quell-URL |
| `controls` | boolean | `true` | Steuerung anzeigen? |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `autoplay` | boolean | `false` | Auto-Wiedergabe? |
| `muted` | boolean | `false` | Stumm? |
| `loop` | boolean | `false` | Wiederholen? |
| `playlist` | array[] | - | Playlist |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onPlay` | function | Wird beim Start ausgeführt |
| `onPause` | function | Wird beim Pausieren ausgeführt |
| `onEnded` | function | Wird beim Ende ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `video`/`audio` |

## Features-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `showCaptions` | boolean | `false` | Untertitel anzeigen? |
| `showPlaylist` | boolean | `false` | Playlist anzeigen? |
| `showFullscreen` | boolean | `true` | Vollbild erlauben? |

## Playback-Attribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `defaultPlaybackRate` | number | `1` | Standard-Wiedergabegeschwindigkeit |
| `playbackRates` | array[] | `[0.5, 1, 1.5, 2]` | Geschwindigkeiten |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../basics/base/)
