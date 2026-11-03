# Video - Appearance

## Base layout

Video players show control buttons, a progress bar, volume and time.

## Variants

### kompakt

```
┌─────────────────────────────────────────┐
│ [▶]  ▓▓▓▓▓▓▓▓░░░░░░  1:23 / 3:45       │
└─────────────────────────────────────────┘
```

### standard

```
┌─────────────────────────────────────────┐
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│ [🔊 80%]  0:00                3:45      │
│                                         │
└─────────────────────────────────────────┘
```

### minimal

```
┌─────────────────────────────────────────┐
│ [▶] [🔊]                               │
└─────────────────────────────────────────┘
```

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 320px | inline videos, comments |
| medium | 640px | cards, panels |
| large | 1280px | featured videos |
| full | 1920px | hero videos, fullscreen |

## Colours and states

```css
.video-player {
  --primary-color: var(--primary-color);
  --secondary-color: var(--secondary-color);
  --hover-color: var(--hover-color);
  --progress-color: var(--primary-color);
  --track-color: rgba(255,255,255,0.3);
}
```

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | scales the controls (1.1x) |
| `opacity` | the opacity changes |
| `border` | the border lights up |

## Responsive

| Breakpoint | Behaviour |
|------------|-----------|
| desktop (>768px) | full controls visible |
| tablet (480-768px) | compact layout |
| mobile (<480px) | minimal layout |

## Control buttons

| Button | Icon | Function |
|--------|------|----------|
| play/pause | ▶️ / ⏸️ | start/pause playback |
| previous | ⏮️ | previous video (playlist) |
| next | ⏭️ | next video (playlist) |
| volume | 🔊 | volume |
| mute | 🔇 | mute |
| fullscreen | ⛶ | fullscreen |
| settings | ⚙️ | settings |

## Progress bar

```
┌─────────────────────────────────────────┐
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░   │
│ ▲                                       │
│ hover tooltip (0:30)                    │
└─────────────────────────────────────────┘
```

## Overlay elements

### Loading overlay

```
┌─────────────────────────────────────────┐
│                                         │
│      🔄                                 │
│      Loading...                         │
│                                         │
└─────────────────────────────────────────┘
```

### Info overlay

```
┌─────────────────────────────────────────┐
│                                         │
│   🖼️                                   │
│   Title                                 │
│   Description                           │
│                                         │
└─────────────────────────────────────────┘
```
