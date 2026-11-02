# Drag and Drop - Appearance

## Basic Layout

The grabbed element lifts (shadow), a ghost stays at the start position, target
zones light up.

```
┌─────────────────────────────────────────┐
│  ┆ (ghost, 30% opaque)                  │
│  ┆                                      │
│  ┆        ┌───────────┐                 │
│  └┄┄►     │ Element ▲ │ ← Lift, follows│
│           └───────────┘   the pointer  │
│  ┃ Insert indicator                     │
│  ▒▒▒▒▒▒▒▒▒▒▒▒▒ (zone highlighted)      │
└─────────────────────────────────────────┘
```

## Phases

| Phase | Appearance |
|-------|------------|
| **Grab** | Element lifts (shadow), haptic, the remainder becomes a ghost |
| **Pull** | Drag image follows the pointer/finger, zones mark acceptance |
| **Drop** | Insert indicator, then settle animation at the target |
| **Cancel** | The element flies back to the start position |

## Feedback Options

| Option | Description |
|--------|-------------|
| **Lift** | Shadow + slight scaling (1.03–1.1) |
| **Ghost** | Placeholder at the origin position |
| **Zone Highlight** | The drop zone colors/tints itself |
| **Insert Line** | 2px line between target positions |
| **Reorder** | Neighbouring elements get out of the way (reorder animation) |

## Lift Heights

| Height | Elevation | Usage |
|--------|-----------|-------|
| Low | 6–8dp | Reorder within one list |
| High | 12–18dp | Across areas/apps |

## Duration

- Lift: 100–150ms
- Reorder evasion: 200–300ms
- Settle/fly-back: 250–350ms

## Difference from Drag

- Drag and Drop: source → target with ghost, zones, drop feedback
- Drag: pure movement (scroll/pan) without target semantics
