# Hover - Appearance

## Basic Layout

The pointer rests over an element without clicking; the element reacts by
lifting, highlighting, or showing an overlay.

```
┌─────────────────────────────────────────┐
│                  ⌖  (pointer, no click) │
│              ┌───────────┐              │
│              │ Element ▲ │  ← Lift/shadow
│              └───────────┘              │
│              ┌────────────────┐         │
│              │ Tooltip        │         │
│              └────────────────┘         │
└─────────────────────────────────────────┘
```

## Reactions

| Reaction | Description |
|----------|-------------|
| **Lift** | Element rises, shadow grows (lift animation) |
| **Highlight** | Background/border color changes |
| **Overlay** | Tooltip, menu, or preview appears |
| **None** | No reaction (callback only) |

## Shadow Levels

| Level | Elevation | Usage |
|-------|-----------|-------|
| Flat | 0–2dp | List, table row |
| Standard | 4–8dp | Button, card |
| Raised | 8–16dp | Preview cards, drag preview |

## Duration

- Transition: 100–250ms
- Tooltip delay: 300–700ms
- Minimum visible time: 1024ms (WCAG 1.4.13)

## Difference from Press

- Hover: without contact, reversible preparation
- Press: with contact, binding intention
