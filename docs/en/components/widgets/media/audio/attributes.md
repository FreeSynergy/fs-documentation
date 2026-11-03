# Audio - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | string | - | audio URL |
| `controls` | boolean | `true` | show controls? |
| `autoplay` | boolean | `false` | autoplay? |
| `muted` | boolean | `false` | muted? |
| `loop` | boolean | `false` | repeat? |
| `volume` | number | `0.8` | volume (0-1) |
| `currentTime` | number | `0` | start time in seconds |

## Behaviour

| Attribute | Type | Description |
|-----------|------|-------------|
| `onPlay` | function | runs on start |
| `onPause` | function | runs when pausing |
| `onTimeUpdate` | function | runs on a time update |
| `onEnded` | function | runs at the end |
| `onVolumeChange` | function | runs when the volume changes |

## Presentation
| Attribute | Type | Description |
|-----------|------|-------------|
| `showVisualizer` | boolean | show an audio visualizer? |
| `visualizerStyle` | enum | style: `bars`, `waves`, `circle` |

| Attribute | Type | Description |
|-----------|------|-------------|
| `responsive` | boolean | use a responsive layout? |
| `compactOnMobile` | boolean | compact layout on mobile? |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-live` | string | live announcement: `polite`, `assertive` |

## Playlist attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `playlist` | array[] | array of audio objects |
| `shuffle` | boolean | random playback? |
| `currentIndex` | number | current track index |

## Control attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `showPlayPause` | boolean | show the play/pause button? |
| `showSkip` | boolean | show the forward/back buttons? |
| `showVolume` | boolean | show the volume control? |
| `showProgress` | boolean | show the progress bar? |
| `showTime` | boolean | show the time display? |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
