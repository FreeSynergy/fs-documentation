# Force Press - Appearance

## Basic Layout

The element sinks in while pressing; from the peek level a preview card appears
above the element and the background dims.

```
┌─────────────────────────────────────────┐
│  ┌─────────────┐                        │
│  │  Pop: open  │      ┌───────────┐     │
│  └─────────────┘      │ Preview:  │     │
│        ▲              │ card      │     │
│   press harder        └───────────┘     │
│  (background dimmed)                    │
└─────────────────────────────────────────┘
```

## Level Feedback

| Level | Feedback |
|-------|----------|
| Light Press | Element sinks in 1–2px (press animation) |
| Peek | Preview card grows out of the element, haptic tick |
| Pop | Preview fills the screen, the content behind scales back |

## Preview Sizes

| Size | Share of the screen | Usage |
|------|---------------------|-------|
| Small | ~25% | Link preview, short info |
| Large | ~66% | Article teaser, media preview |

## Duration

- Sinking in: 100–150ms
- Opening the peek: 200–300ms
- Pop transition: 300–400ms

## Difference from Long Press

- Force Press: force made visible through levels (sinks in, preview, opens)
- Long Press: time made visible through a countdown/feedback only at the end
