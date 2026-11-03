# Video - Attributes

## Main attributes

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `src` | string | - | video URL |
| `controls` | boolean | `true` | show controls? |
| `autoplay` | boolean | `false` | autoplay? |
| `muted` | boolean | `false` | muted? |
| `loop` | boolean | `false` | repeat? |
| `poster` | string | - | preview image |
| `playsInline` | boolean | `false` | inline playback (mobile)? |

## Behaviour

| Attribute | Type | Description |
|-----------|------|-------------|
| `onPlay` | function | runs on start |
| `onPause` | function | runs when pausing |
| `onEnded` | function | runs at the end |
| `onTimeUpdate` | function | runs on a time update |

## Presentation
| Attribute | Type | Description |
|-----------|------|-------------|
| `responsive` | boolean | responsive layout? |
| `aspectRatio` | string | aspect ratio (e.g. "16/9") |

| Attribute | Type | Description |
|-----------|------|-------------|
| `showLoading` | boolean | show the loading state? |
| `fadeIn` | boolean | show the fade-in? |
| `fadeInDuration` | number | duration in ms |

## Events

| Attribute | Type | Description |
|-----------|------|-------------|
| `onLoad` | function | runs when the video loads |
| `onError` | function | runs on an error |
| `onFullscreenChange` | function | runs when the fullscreen state changes |

## Accessibility

| Attribute | Type | Description |
|-----------|------|-------------|
| `aria-live` | string | live announcement |
| `captions` | string | URL of the subtitles |

## Control attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `showPlayPause` | boolean | show the play/pause button? |
| `showSkip` | boolean | show the forward/back buttons? |
| `showVolume` | boolean | show the volume control? |
| `showProgress` | boolean | show the progress bar? |
| `showTime` | boolean | show the time display? |
| `showFullscreen` | boolean | show the fullscreen button? |

## Playlist attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `playlist` | array[] | array of video objects |
| `shuffle` | boolean | random playback? |
| `currentIndex` | number | current video index |

## Video-specific attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `crossorigin` | string | CORS attribute |
| `preload` | enum | `auto`, `metadata`, `none` |
| `poster` | string | preview image URL |
| `quality` | enum | standard quality |

## Inherited from

`visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`,
`aria-label`, `aria-*` → [Base component](../../../primitives/basics/base.md)
