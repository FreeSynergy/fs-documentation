# Audio

| Field | Value |
|-------|-------|
| **Category** | `media` |
| **Inherits from** | `base`, `media-player` |
| **Variants** | `einzeln`, `playlist`, `kompakt` |
| **States** | `spielend`, `pausiert` |
| **Gestures** | `tap`, `drag` |
| **Animations** | `progress`, `pulse` |
| **Related** | `media-player`, `video`, `progress` |
| **Status** | documented |

## Description
An audio element plays audio files in various formats. It offers controls such as
play/pause and volume.

## Purpose

- Playing podcasts
- Playing music
- Voice messages
- Sound effects
- Instruction videos without video

## Variants

| Variant | Description |
|---------|-------------|
| **einzeln** | one file with full controls |
| **playlist** | several files with previous/next and a list |
| **kompakt** | voice message: play, duration, progress, no volume |

## Features

- Play/pause button
- Volume control
- Progress bar
- Time display (current position / total time)
- Timeline seek (click to jump)
- Playlist

## Distinction

- **Do not confuse with** [media-player](../media-player/): the media player is the parent class
  with controls, playlist and subtitles; the audio element inherits from it and shows only sound.
- **Do not confuse with** [video](../video/): without a picture it is audio, with a picture video — a
  single video still is an [image](../../../primitives/media/image/).
- A voice message in chat is this component in the variant `kompakt`, not a component of
  its own.

## Best Practices

- Always show `controls`, except for background audio
- Use `muted` with `autoplay` (browser requirement)
- Provide alt text for accessibility
- Provide several formats for compatibility

## Formats

| Format | Description | Use |
|--------|-------------|-----|
| **MP3** | standard format, widely used | all audio uses |
| **WAV** | uncompressed, high quality | high-quality audio |
| **OGG** | open source | web applications |
| **AAC** | compressed, high quality | streaming |

## Control attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `src` | string | audio URL |
| `controls` | boolean | show controls? |
| `autoplay` | boolean | autoplay? |
| `muted` | boolean | muted? |
| `loop` | boolean | repeat? |
| `volume` | number | volume (0-1) |
| `currentTime` | number | current playback position |
| `duration` | number | total duration of the audio |

## Hover effects

| Effect | Description |
|--------|-------------|
| `zoom` | the controls grow |
| `opacity` | the opacity changes |
| `border` | the border lights up |

## See also

- [media – overview](../index.md)
- [Media Player](../media-player/) — shared controls
- [Video](../video/) — with a picture
- [Base component](../../../primitives/basics/base.md)
