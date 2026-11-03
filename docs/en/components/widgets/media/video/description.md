# Video

| Field | Value |
|-------|-------|
| **Category** | `media` |
| **Inherits from** | `base`, `media-player` |
| **Variants** | `einzeln`, `hintergrund`, `live` |
| **States** | `spielend`, `vollbild`, `gepuffert` |
| **Gestures** | `tap`, `drag`, `double-tap`, `pinch` |
| **Animations** | `fade-out`, `progress` |
| **Related** | `media-player`, `audio`, `image`, `embed` |
| **Status** | documented |

## Description
A video element plays videos in various formats. It offers controls such as
play/pause, volume and fullscreen.

## Purpose

- Showing instruction videos
- Presenting product videos
- Playing video comments
- Showing live streams
- Background videos

## Variants

| Variant | Description |
|---------|-------------|
| **einzeln** | ordinary playback with full controls |
| **hintergrund** | endless, muted and without controls behind other content |
| **live** | running stream without skipping ahead, the time display is replaced by "live" |

## Features

- Play/pause button
- Volume control
- Progress bar
- Fullscreen mode
- Subtitles
- Quality selection
- Speed setting

## Distinction

- The video inherits from [media-player](../media-player/) and here only names what is added:
  picture surface, preview image and fullscreen.
- **Do not confuse with** [audio](../audio/): without a picture it is audio — the still image alone is
  an [image](../../../primitives/media/image/).
- **Do not confuse with** [embed](../../../workbenches/special/embed/): videos from other platforms are
  embedded, not played.

## Best Practices

- Always set a preview image (`poster`), otherwise there is nothing to see before the start.
- Autoplay only muted and in an endless loop; otherwise playback only starts on request.
- Carry subtitles along — for meetings and voice messages too.
- Choose the quality automatically and keep it switchable manually.
- Play inline on mobile (`playsInline`), otherwise the system jumps into its own player.

## Formats

| Format | Description | Use |
|--------|-------------|-----|
| **MP4** | standard format, widely used | all video uses |
| **WEBM** | open source, small file size | web applications |
| **OGV** | open source format | alternative format |
| **MKV** | container format, many streams | high-quality videos |

## Control attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `src` | string | video URL |
| `controls` | boolean | show controls? |
| `autoplay` | boolean | autoplay? |
| `muted` | boolean | muted? |
| `loop` | boolean | repeat? |
| `poster` | string | preview image |
| `playsInline` | boolean | inline playback (mobile) |
| `volume` | number | volume (0-1) |

## See also

- [media – overview](../index.md)
- [Media Player](../media-player/) — shared controls
- [Audio](../audio/) — without a picture
- [Base component](../../../primitives/basics/base.md)
