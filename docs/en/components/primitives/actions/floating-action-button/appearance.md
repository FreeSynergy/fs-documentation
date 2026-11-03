# Floating Action Button (FAB) - Appearance

## Base layout

A floating action button (FAB) is a round main-action button.

## Variants

### Standard FAB (large)

```
                    ┌─────────┐
                    │   +     │
                    └─────────┘
```

### Mini FAB (small)

```
                    ┌──────┐
                    │  +   │
                    └──────┘
```

### Extended FAB (with text)

```
                    ┌──────────────┐
                    │   +  New     │
                    └──────────────┘
```

## Sizes

| Size | Diameter | Use |
|------|----------|-----|
| standard | 56px | main action |
| mini | 40px | secondary action |
| extended | auto | action with text |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **primary** | primary colour | standard |
| **secondary** | secondary colour | secondary |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement (1.1x) |
| `shadow` | shadow becomes stronger |
| `ripple` | wave effect on click |

## Responsive

The FAB stays anchored to the screen (`position: fixed`) so the main action remains
reachable while scrolling. Scrolling down pushes it out of view (`scroll-hidden`),
scrolling up brings it back with `pop-in`; on narrow surfaces it becomes a mini FAB.

```css
.fab {
  position: fixed;
  right: 16px;
  bottom: 16px;
  width: 56px;
  height: 56px;
  box-shadow: 0 3px 5px rgba(0,0,0,0.2);
  transition: transform 150ms, box-shadow 150ms;
}
.fab:hover  { transform: scale(1.1); box-shadow: 0 6px 10px rgba(0,0,0,0.25); }
.fab:active { transform: scale(0.96); }

@media (max-width: 600px) {
  .fab { width: 40px; height: 40px; }   /* mini FAB on a narrow surface */
}
.fab--scroll-hidden { transform: translateY(80px); opacity: 0; }
```

## Positioning

| Position | Description |
|----------|-------------|
| **bottom right** | standard |
| **bottom left** | bottom left (RTL languages) |
| **center** | in the middle (rare) |
| **fixed** | fixed to the screen |

## Badge (with count/status)

```
                    ┌─────────┐
                    │   +     │
                    │  (3)    │
                    └─────────┘
```
