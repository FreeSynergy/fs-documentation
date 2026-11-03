# Audio - Appearance

## Base layout

Audio elements show control buttons, a progress bar and a time display.

## Variants
### kompakt
```
┌──────────────────────────────┐
│ [▶]  ▓▓▓▓▓▓▓▓░░░░░  1:23 / 3:45  │
└──────────────────────────────┘
```
### standard
```
┌─────────────────────────────────────────┐
│ [⏮] [◀] [▶] [▶] [⏭]                   │
│ [🔊 80%]                                │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░  │
│ 0:00                                              3:45 │
└─────────────────────────────────────────┘
```
### minimal
```
┌──────────────┐
│ [▶] [🔊]    │
└──────────────┘
```

| Icon | Function |
|------|----------|
| ⏯️ | play/pause (toggle) |
| ⏭️ | next track |
| ⏮️ | previous track |
| 🔊 | volume |
| 🔇 | mute |
| 🔄 | repeat |
| 📋 | playlist |

## Sizes

| Size | Height | Use |
|------|--------|-----|
| compact | 32px | inline, chat, lists |
| small | 48px | cards, panels |
| medium | 64px | standard |
| large | 80px | featured audio |
| XL | 120px | hero audio |

## Colours and states

```css
.audio-player {
  --primary-color: var(--primary-color);
  --secondary-color: var(--secondary-color);
  --hover-color: var(--hover-color);
  --progress-color: var(--primary-color);
  --track-color: var(--track-color);
}
```

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | scales the controls (1.1x) |
| `color` | the colour changes |
| `shadow` | the shadow becomes stronger |
| `opacity` | the opacity changes |

## Responsive

| Breakpoint | Behaviour |
|------------|-----------|
| desktop (>768px) | full controls visible |
| tablet (480-768px) | compact layout |
| mobile (<480px) | minimal layout |

## Progress bar styling

```css
.audio-progress {
  background: var(--track-color);
}

.audio-progress-fill {
  background: var(--progress-color);
  transition: width 0.1s ease;
}
```
