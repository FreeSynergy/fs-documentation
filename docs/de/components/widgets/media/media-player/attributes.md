# Media Player - Attribute

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|----------|-----|----------|--------------|
| `src` | string | - | Quell-URL |
| `controls` | boolean | `true` | Bedienelemente anzeigen? |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `autoplay` | boolean | `false` | automatisch abspielen? |
| `muted` | boolean | `false` | stumm? |
| `loop` | boolean | `false` | wiederholen? |
| `playlist` | array[] | - | Playlist |

## Ereignisse

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onPlay` | function | wird beim Start ausgeführt |
| `onPause` | function | wird beim Pausieren ausgeführt |
| `onEnded` | function | wird am Ende ausgeführt |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | ARIA-Rolle: `video`/`audio` |

## Funktions-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `showCaptions` | boolean | `false` | Untertitel anzeigen? |
| `showPlaylist` | boolean | `false` | Playlist anzeigen? |
| `showFullscreen` | boolean | `true` | Vollbild erlauben? |

## Wiedergabe-Attribute

| Attribut | Typ | Standard | Beschreibung |
|---|---|---|---|
| `defaultPlaybackRate` | number | `1` | Standard-Wiedergabegeschwindigkeit |
| `playbackRates` | array[] | `[0.5, 1, 1.5, 2]` | Geschwindigkeiten |

## Geerbt von

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
