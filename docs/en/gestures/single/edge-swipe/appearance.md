# Edge Swipe - Appearance

## Basic Layout

The finger starts in a narrow zone at the edge and pulls content inwards; the
layer underneath becomes visible as a preview.

```
┌─────────────────────────────────────────┐
│▌ ←                                       │
│▌   Edge zone (24px)                     │
│▌░░                                       │
│▌░░░  ►  Preview of the previous page    │
│▌░░░░░                                    │
└─────────────────────────────────────────┘
```

## Phases

| Phase | Description |
|-------|-------------|
| **Grab** | Edge detected, pre-shadow appears |
| **Pull** | Content follows the finger, the layer underneath becomes visible |
| **Completion** | Above threshold: load the target; below: spring back |

## Feedback Options

| Option | Description |
|--------|-------------|
| **Shadow Preview** | Shadow edge shows the depth of the layer underneath |
| **Parallax** | Both layers move at different speeds |
| **Highlight Edge** | Glowing edge at the border while swiping |
| **None** | No visual signal, transition only on release |

## Edge

| Edge | Typical sequence |
|------|------------------|
| Left | Previous page slides in from the left |
| Bottom | Home surface scales out of the content |
| Top | Panel unfolds down from the status bar |

## Duration

- Interactive: follows the finger, 100–400ms
- Completion animation: 200–350ms

## Difference from Swipe

- Edge Swipe: starts at the edge, navigation layer, preview of the next layer
- Swipe: starts in the content, action on the content, no layer preview
