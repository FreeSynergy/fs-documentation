# Animations

Animations describe the time-controlled change of elements (entrance, exit, feedback, state change).

## Overview

| # | Animation | Group | Description |
|---|-----------|-------|-------------|
| 1 | **Fade In** | Entrance | Element appears gradually (opacity 0 → 1) |
| 2 | **Fade Out** | Exit | Element disappears gradually (opacity 1 → 0) |
| 3 | **Slide In** | Entrance | Element glides in from outside (left/right/top/bottom) |
| 4 | **Slide Out** | Exit | Element glides out to the outside |
| 5 | **Zoom In** | Entrance | Element scales from small to full size |
| 6 | **Zoom Out** | Exit | Element scales from full size to zero |
| 7 | **Bounce In** | Entrance | Element bounces in as it arrives |
| 8 | **Bounce Out** | Exit | Element bounces before disappearing |
| 9 | **Flip** | State change | Element rotates 180° (front/back side) |
| 10 | **Rotate** | State change | Element rotates around its own axis |
| 11 | **Spin** | Endless | Permanent rotation (loader, activity) |
| 12 | **Scale In** | Entrance | Element grows from 0% to 100% |
| 13 | **Scale Out** | Exit | Element shrinks from 100% to 0% |
| 14 | **Collapse** | Exit | Height/width reduced to 0 (accordion closes) |
| 15 | **Expand** | Entrance | Height/width grows from 0 to content (accordion opens) |
| 16 | **Unfold** | Entrance | Element unfolds like a sheet |
| 17 | **Shake** | Feedback | Element briefly rattles horizontally (error) |
| 18 | **Wiggle** | Feedback | Element wiggles slightly (edit mode) |
| 19 | **Pulse** | Endless | Cyclic swelling/fading (attention) |
| 20 | **Heartbeat** | Endless | Double pulse in the rhythm of a heart rate |
| 21 | **Ripple** | Feedback | Wave spreads from the click point |
| 22 | **Highlight** | Feedback | Background briefly lights up (found spot) |
| 23 | **Glow** | Endless | Luminous halo around the contour (selection, live status) |
| 24 | **Progress** | Endless | Progress indicator (bar, circle, skeleton) |
| 25 | **Skeleton** | Endless | Placeholder shimmer while loading |
| 26 | **Typing** | Endless | Typing indicator (three dots in chats) |
| 27 | **Elastic** | Feedback | Element springs beyond the final position |
| 28 | **Rubber Band** | Feedback | Excessive pulling springs back (over-scroll) |
| 29 | **Morph** | State change | Shape transforms smoothly into another shape |
| 30 | **Cross Fade** | State change | Two elements cross-fade each other |
| 31 | **Parallax** | Movement | Layers move at different speeds |
| 32 | **Stagger** | Organization | Child elements start offset one after another |

## Groups

### Entrance (Enter)

Fade In, Slide In, Zoom In, Scale In, Bounce In, Expand, Unfold

### Exit

Fade Out, Slide Out, Zoom Out, Scale Out, Bounce Out, Collapse

### Feedback (Interaction)

Shake, Wiggle, Ripple, Highlight, Elastic, Rubber Band

### Endless (Loop)

Spin, Pulse, Heartbeat, Glow, Progress, Skeleton, Typing, Parallax

### State Change (Transition)

Flip, Rotate, Morph, Cross Fade

### Organization

Stagger

## Animations as a Directory

Every animation has its own directory following the pattern `animations/<name>/`:

| File | Content |
|------|---------|
| `description.md` | What is the animation? What is it for? When to use it? |
| `attributes.md` | Attributes/options (duration, timing, amplitude, callbacks) |
| `appearance.md` | What does it look like? ASCII progression, variants, duration |

## Standard Attributes (for all animations)

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `animation` | string | `none` | Name of the animation |
| `duration` | number | `300` | Duration in ms |
| `timingFunction` | string | `ease` | `linear`, `ease-in`, `ease-out`, `ease-in-out`, `cubic-bezier(...)` |
| `delay` | number | `0` | Delay before the start in ms |
| `iterationCount` | number \| `infinite` | `1` | Number of repetitions |
| `direction` | string | `normal` | `normal`, `reverse`, `alternate`, `alternate-reverse` |
| `fillMode` | string | `none` | `none`, `forwards`, `backwards`, `both` |
| `playState` | string | `running` | `running`, `paused` |
| `onAnimateStart` | function | - | Executed at the start |
| `onAnimateEnd` | function | - | Executed at the end |

## Configuration (global)

| Attribute | Type | Description |
|-----------|------|-------------|
| `animationsEnabled` | boolean | Enable animations globally? |
| `defaultDuration` | number | Default duration for all animations |
| `respectReducedMotion` | boolean | Respect `prefers-reduced-motion`? |
| `staggerStep` | number | Offset between child elements in ms |

## Duration Guidelines

| Range | Duration | Usage |
|-------|----------|-------|
| Micro | 100–200ms | Hover, tap feedback |
| Standard | 200–400ms | Windows, menus, lists |
| Attention | 400–800ms | Onboarding, highlights |
| Loop | 800–2000ms | Loaders, pulse, skeleton |

## Accessibility

- `prefers-reduced-motion: reduce` → reduce animations to 0ms or fade
- Pause endless animations when the element is not visible
- Never use color animations as the only information (always add icon/text)

## See also

- [Gestures](../gestures/index.md) — Shake, Wiggle as feedback to gestures
- [Standardized Data](../data/index.md) — fields like `animation`, `duration` in component attributes
