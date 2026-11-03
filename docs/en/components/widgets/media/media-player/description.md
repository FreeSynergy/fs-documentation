# Media Player

| Field | Value |
|-------|-------|
| **Category** | `media` |
| **Inherits from** | `base` |
| **Variants** | `einzeln`, `playlist`, `steuerung` |
| **States** | `spielend`, `pausiert`, `vollbild` |
| **Gestures** | `tap`, `drag`, `double-tap` |
| **Animations** | `fade-out`, `progress`, `spin` |
| **Related** | `audio`, `video`, `progress`, `embed` |
| **Status** | documented |

## Description
A media player plays videos and audio.

## Purpose

- Videos
- Audio
- Media

## Variants

| Variant | Description |
|---------|-------------|
| **einzeln** | one file, surface and controls belong together |
| **playlist** | several files, a list with next/previous |
| **steuerung** | only the bar; the picture or sound surface is supplied by the user |

## Features

- Play/pause
- Volume
- Progress
- Fullscreen
- Captions

## Distinction

- This component is the **parent class** of [audio](../audio/) and [video](../video/):
  controls, playlist and subtitles are defined here, the two children only name their
  differences (plan section 4, line 13).
- **Do not confuse with** [embed](../../../workbenches/special/embed/): an embedded player of a foreign
  platform is not a player of its own.
- **Do not confuse with** [progress](../../../primitives/feedback/progress/): there the bar is a display,
  here it is a jump marker inside the file.

## Best Practices

- Always offer subtitles, even when the sound is off by default.
- Hide the controls after three seconds, but keep them reachable at any time by keyboard and focus.
- Autoplay only without sound; otherwise the application waits for a deliberate decision.
- Make the buffering and loading status visible, show time always as `mm:ss`.
- Offer fullscreen and picture-in-picture so playback does not block the work area.

## See also

- [media – overview](../index.md)
- [Audio](../audio/) and [Video](../video/) — the two children
- [Embed](../../../workbenches/special/embed/) — players from other providers
- [Base component](../../../primitives/basics/base.md)
