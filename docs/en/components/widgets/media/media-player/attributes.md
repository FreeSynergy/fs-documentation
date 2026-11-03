# Media Player - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | string | - | source URL |
| `controls` | boolean | `true` | show controls? |

## Behaviour

| Attribute | Type | Default | Description |
|---|---|---|---|
| `autoplay` | boolean | `false` | autoplay? |
| `muted` | boolean | `false` | muted? |
| `loop` | boolean | `false` | repeat? |
| `playlist` | array[] | - | playlist |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onPlay` | function | runs at the start |
| `onPause` | function | runs when pausing |
| `onEnded` | function | runs at the end |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `role` | string | ARIA role: `video`/`audio` |

## Features attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `showCaptions` | boolean | `false` | show subtitles? |
| `showPlaylist` | boolean | `false` | show the playlist? |
| `showFullscreen` | boolean | `true` | allow fullscreen? |

## Playback attributes

| Attribute | Type | Default | Description |
|---|---|---|---|
| `defaultPlaybackRate` | number | `1` | default playback speed |
| `playbackRates` | array[] | `[0.5, 1, 1.5, 2]` | speeds |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
