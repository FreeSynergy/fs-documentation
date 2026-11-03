# Media Player - Appearance

## Base layout

A media player plays videos and audio.

## Variants

### Video player

```
┌─────────────────────────────────────────┐
│                                         │
│      📽️                                │
│      (video player)                     │
│                                         │
│      [▶] [⏸] [Volume] [Fullscreen]     │
└─────────────────────────────────────────┘
```

### Audio player

```
┌─────────────────────────────────────────┐
│  [▶] [⏸] [Volume] [Progress]  0:00     │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Width/height | Use |
|------|--------------|-----|
| Small | 320x180px | Inline |
| Medium | 640x360px | Standard |
| Large | 1280x720px | Featured |
| Full | 100% | Full width |

## Colours and states

| State | Colour | Description |
|-------|--------|-------------|
| **Background** | black/dark | background |
| **Controls** | white/light | control elements |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `controls` | the controls appear |
| `shadow` | stronger shadow |

## Responsive

- The surface keeps the aspect ratio of the file (usually 16:9) and scales with the width;
  `Full` fills the viewport, the control bar stays below or above it.
- Below `small` screen width the playlist is placed under the surface and the volume
  makes room for the subtitle button.
- The controls fade out after three seconds while playing (`fade-out`) and return on
  pointer movement, focus or a key press.

## Controls

| Control | Function |
|---------|----------|
| **Play/Pause** | start/pause playback |
| **Volume** | volume |
| **Progress** | progress bar |
| **Fullscreen** | fullscreen |
| **Captions** | subtitles |

## Playlist

```
┌─────────────────────────────────────────┐
│ [▶]  Title 1                            │
│ [⏸]  Title 2                            │
│ [⏸]  Title 3                            │
└─────────────────────────────────────────┘
```
