# Toast - Appearance

## Base layout
A toast is a pop-up notification that usually appears top right.

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Title                           │
│      Description text...                │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Colour | Description |
|---------|--------|-------------|
| **info** | blue | information message |
| **success** | green | success message |
| **warning** | orange/yellow | warning message |
| **error** | red | error message |

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 250px | short messages |
| medium | 350px | standard |
| large | 450px | long messages |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **info** | blue | information message |
| **success** | green | success message |
| **warning** | orange | warning message |
| **error** | red | error message |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `shadow` | shadow becomes stronger |
| `transform` | slight lifting |

## Responsive

Toasts sit in a stack at a screen corner; new messages slide in below with `stagger`.
Hovering pauses the auto-dismiss counter (`paused`), swiping away (`swipe`) removes the
message with `fade-out`. On a narrow surface the toast takes the full width and sits at
the bottom so it stays reachable.

```css
.toast-stack { position: fixed; top: 16px; right: 16px; display: flex;
               flex-direction: column; gap: 8px; z-index: 40; }
.toast           { animation: slide-in 200ms; }
.toast--leaving  { animation: fade-out 150ms forwards; }

@media (max-width: 600px) {
  .toast-stack { left: 0; right: 0; top: auto; bottom: 0; }
  .toast { width: 100%; }
}
```

## Positioning

| Position | Description |
|----------|-------------|
| **top right** | standard |
| **bottom right** | bottom right |
| **top left** | top left |
| **bottom left** | bottom left |
| **center** | in the middle |

## Auto-dismiss

```
┌─────────────────────────────────────────┐
│ [✕]  📢 Title                           │
│      Description text...                │
│      ━━━━━━━━━━━━━━━━━━━━━              │
└─────────────────────────────────────────┘
```
