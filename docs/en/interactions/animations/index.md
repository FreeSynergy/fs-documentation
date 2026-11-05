# Animations

Animations describe the time-controlled change of elements (entrance, exit, feedback,
state change). They sit in **8 categories**, and every animation has its own directory
with three files.

## Categories

| Category | Directory | Count | Content |
|----------|-----------|-------|---------|
| Entrance | [entrance](entrance/) | 9 | Making elements appear |
| Exit | [exit](exit/) | 8 | Making elements disappear |
| Feedback | [feedback](feedback/) | 9 | Answer to an input |
| Endless | [loop](loop/) | 4 | repeated signals |
| Loading | [loading](loading/) | 4 | Bridging waiting time |
| State change | [transition](transition/) | 6 | Changing state without creating elements |
| Movement | [movement](movement/) | 1 | scroll-dependent layers |
| Organisation | [organization](organization/) | 2 | Spreading start times across children |

**43 documented animations** (as of this file).

## Overview

| # | Animation | Category | Description |
|---|-----------|----------|-------------|
| 1 | **Fade In** | entrance | Element appears gradually (opacity 0 → 1) |
| 2 | **Fade Out** | exit | Element disappears gradually (opacity 1 → 0) |
| 3 | **Slide In** | entrance | Element glides in from outside (left/right/top/bottom) |
| 4 | **Slide Out** | exit | Element glides out to the outside |
| 5 | **Zoom In** | entrance | Element scales from small to full size |
| 6 | **Zoom Out** | exit | Element scales from full size to zero |
| 7 | **Bounce In** | entrance | Element springs in as it arrives |
| 8 | **Bounce Out** | exit | Element springs before disappearing |
| 9 | **Pop In** | entrance | Fade in with a brief overshoot (chips, badges) |
| 10 | **Pop Out** | exit | Brief pull-back, then folded away |
| 11 | **Flip** | transition | Element rotates 180° (front/back side) |
| 12 | **Rotate** | transition | Element rotates around its own axis |
| 13 | **Spin** | loop | Permanent rotation (loader, activity) |
| 14 | **Scale In** | entrance | Element grows from 0 % to 100 % |
| 15 | **Scale Out** | exit | Element shrinks from 100 % to 0 % |
| 16 | **Collapse** | exit | Height/width reduced to 0 (accordion closes) |
| 17 | **Expand** | entrance | Height/width grows from 0 to content (accordion opens) |
| 18 | **Unfold** | entrance | Element unfolds like a sheet |
| 19 | **Shake** | feedback | Element briefly rattles horizontally (error) |
| 20 | **Wiggle** | feedback | Element wiggles slightly (edit mode) |
| 21 | **Press** | feedback | Element sinks minimally when pressed |
| 22 | **Lift** | feedback | Element rises on hover/focus (shadow grows) |
| 23 | **Tick Draw** | feedback | Success tick is drawn as a line |
| 24 | **Pulse** | loop | Cyclic swelling/fading (attention) |
| 25 | **Heartbeat** | loop | Double pulse in the rhythm of a heart rate |
| 26 | **Ripple** | feedback | Wave spreads from the click point |
| 27 | **Highlight** | feedback | Background briefly lights up (found spot) |
| 28 | **Glow** | loop | Luminous halo around the contour (selection, live status) |
| 29 | **Progress** | loading | Progress indicator (bar, circle) |
| 30 | **Skeleton** | loading | Placeholder shimmer while loading |
| 31 | **Typing** | loading | Typing indicator (three dots in chats) |
| 32 | **Dots** | loading | Three loading dots as a compact activity indicator |
| 33 | **Elastic** | feedback | Element springs beyond the final position |
| 34 | **Rubber Band** | feedback | Excessive pulling springs back (over-scroll) |
| 35 | **Morph** | transition | Shape transforms smoothly into another shape |
| 36 | **Cross Fade** | transition | Two elements cross-fade each other |
| 37 | **Cross Slide** | transition | Two elements push each other out of view |
| 38 | **Reorder** | transition | List items smoothly swap places (FLIP) |
| 39 | **Parallax** | movement | Layers move at different speeds |
| 40 | **Stagger** | organization | Child elements start offset one after another |
| 41 | **Cascade** | organization | Offset start along one direction |
| 42 | **Radial Out** | entrance | Points grow radially out of the anchor (radial menu) |
| 43 | **Radial In** | exit | Points travel back to the anchor (radial menu) |

## Tree

The directories are the tree. Within the categories the animations are grouped into
**families**: entrance and exit are always the same animation in opposite direction.

```
animations/
│
├── entrance/          fade-in, slide-in, zoom-in, scale-in,
│                      bounce-in, pop-in, expand, unfold, radial-out
│     Opacity ········ fade          Size ············ zoom, scale, bounce, pop
│     Position ······· slide         Layout size ····· expand      (drop ⁺, wipe ⁺,
│                                                        swing ⁺, blur ⁺)
│
├── exit/              fade-out, slide-out, zoom-out, scale-out,
│                      bounce-out, pop-out, collapse, radial-in
│     same families, direction out  (fold ⁺ as the counterpart of unfold)
│
├── feedback/          shake, wiggle, ripple, press, lift,
│                      tick-draw, highlight, elastic, rubber-band
│     Rejection ······ shake, wiggle            (nudge ⁺)
│     Operation ······ press, lift, ripple      Confirmation · tick-draw (cross-draw ⁺)
│     Physics ········ elastic, rubber-band     (tilt ⁺)
│     Signal ········· highlight                (flash ⁺, count-up ⁺)
│
├── loop/              spin, pulse, heartbeat, glow
│     Signal ········· pulse, heartbeat, glow   (breathing ⁺, blink ⁺)
│     Rotation ······· spin
│
├── loading/           progress, skeleton, typing, dots
│     Activity ······· dots, typing             Structure ··· skeleton
│     Value ·········· progress                 (barber-pole ⁺)
│
├── transition/        flip, rotate, morph, cross-fade,
│                      cross-slide, reorder
│     2D ············· flip, morph, cross-fade, cross-slide
│     Layout ········· reorder                  (resize ⁺, magic-line ⁺)
│     Layer / 3D ····· –                         (shared-element ⁺, page-transition ⁺,
│     cube ⁺)
│
├── movement/          parallax
│     Ambience ······· parallax                 (float ⁺, drift ⁺, marquee ⁺,
│     wave ⁺, ken-burns ⁺)
│
└── organization/      stagger, cascade
      Timing ········· stagger, cascade         (sequence ⁺, orchestration ⁺)
```

⁺ = not documented yet (candidate, see [Further animations](#further-animations-candidates))

## Families: the same animation in two directions

The direction pairs are redundancy. One document per family covers both sides through
attributes – the names remain as shorthand (`animation: "fade-in"` is an abbreviation
for `fade` + `direction: in`).

| Family | Documents | Merged by |
|--------|-----------|-----------|
| `fade` | [fade-in](entrance/fade-in/description.md), [fade-out](exit/fade-out/description.md) | `direction: in \| out`, `fromOpacity`, `toOpacity` |
| `slide` | [slide-in](entrance/slide-in/description.md), [slide-out](exit/slide-out/description.md) | `direction`, `from: left \| right \| top \| bottom`, `distance` |
| `zoom` | [zoom-in](entrance/zoom-in/description.md), [zoom-out](exit/zoom-out/description.md) | `direction`, `fromScale`, `toScale` |
| `scale` | [scale-in](entrance/scale-in/description.md), [scale-out](exit/scale-out/description.md) | `direction`, `origin` |
| `bounce` | [bounce-in](entrance/bounce-in/description.md), [bounce-out](exit/bounce-out/description.md) | `direction`, `amplitude`, `bounces` |
| `pop` | [pop-in](entrance/pop-in/description.md), [pop-out](exit/pop-out/description.md) | `direction`, `overshoot`, `anticipation` |
| `radial` | [radial-out](entrance/radial-out/description.md), [radial-in](exit/radial-in/description.md) | `direction: in \| out`, `staggerStep`, `ringStep`, `order` |
| `collapse` | [expand](entrance/expand/description.md), [collapse](exit/collapse/description.md) | `direction`, `dimension: height \| width \| both` |
| `rotate` | [rotate](transition/rotate/description.md), [spin](loop/spin/description.md) | `iterationCount: infinite` turns Rotate into Spin |
| `pulse` | [pulse](loop/pulse/description.md), [heartbeat](loop/heartbeat/description.md) | `waveform: pulse \| heartbeat`, `intensity` |
| `fade` + blur | – | already covered: the `blur` attribute of [Fade In](entrance/fade-in/attributes.md) |

**Possible:** 43 documents → **33 family documents** (10 pairs merge). Deliberately not
done yet: merging would change every cross-reference and the navigation in `mkdocs.yml`
again. In addition, Skeleton/Shimmer and Typing/Dots are overlaps that are kept as
*variants* inside the existing documents.

## Animations as a directory

Every animation has its own directory following the pattern
`animations/<category>/<name>/`:

| File | Content |
|------|---------|
| `description.md` | What is the animation? What is it for? When to use it? |
| `attributes.md` | Attributes/options (duration, timing, amplitude, callbacks) |
| `appearance.md` | What does it look like? ASCII progression, variants, duration |

Every category has its own overview (`<category>/index.md`); this file lists them all.

## Standard attributes (for all animations)

Attribute names follow the convention from [data/konventionen.md](../../data/konventionen.md): `camelCase` and ASCII. Terms with an umlaut are named in English (`overshoot`, `dotSize`, `intensity`).

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

Directions of family pairs are represented additionally:

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `direction` (family) | string | `in` | `in` (entrance) or `out` (exit) |
| `mirrorOf` | string | - | Name of the opposite animation (`fade-in` → `fade-out`) |

## Configuration (global)

| Attribute | Type | Description |
|-----------|------|-------------|
| `animationsEnabled` | boolean | Enable animations globally? |
| `defaultDuration` | number | Default duration for all animations |
| `respectReducedMotion` | boolean | Respect `prefers-reduced-motion`? |
| `staggerStep` | number | Offset between child elements in ms |

## Duration guidelines

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
- Movements in the field of view (Parallax, Lift, Reorder) are the strongest triggers –
  always keep them switchable off
- Blinking and flashing signals (`glow`, planned `blink`/`flash`) never longer than
  five cycles without user action

## Further animations (candidates)

Sensible additions, sorted by category. Priority: **high** = needed in every UI,
medium = depends on the feature, low = decoration. Candidates that already have a
directory are no longer listed here.

### entrance / exit

| Candidate | Description | Prio |
|-----------|-------------|------|
| `drop-in` / `drop-out` | Element falls in with gravity, bounces on arrival | medium |
| `wipe` / `reveal` | Becomes visible via a mask (`clip-path`), diagonal or radial | medium |
| `swing-in` / `swing-out` | Pendulums around a hanger (menus on bars) | medium |
| `blur-in` / `blur-out` | Blur → sharp (focus, background overlay); `blur` is already an attribute of Fade | medium |
| `fold` | Counterpart to Unfold (paper or accordion folding) | low |

### feedback

| Candidate | Description | Prio |
|-----------|-------------|------|
| `cross-draw` | A cross is drawn (cancel, error in a field) | medium |
| `count-up` | Number flips upward (counters, totals, statistics) | medium |
| `flash` | Brief change of brightness instead of surface colour | medium |
| `nudge` | Mini-shake vertically: "not selectable" without signalling an error | medium |
| `tilt` | Element tilts in 3D towards the pointer (cards, tiles) | low |

### loop / loading

| Candidate | Description | Prio |
|-----------|-------------|------|
| `breathing` | Slow, deep swelling and fading (AI active, connection holds) | medium |
| `blink` | Cursor/recording indicator (on/off in rhythm) | medium |
| `barber-pole` | Stripe pattern travels (indeterminate progress) | medium |

### transition

| Candidate | Description | Prio |
|-----------|-------------|------|
| `resize` | Size change of a container smoothly followed (panel, split view) | medium |
| `magic-line` | Marker line travels from one tab to the next | medium |
| `shared-element` | The same element travels from list to detail view | medium |
| `page-transition` | Full-page transition between programs/areas | medium |
| `cube` | Cube rotation with four sides (wizard steps) | low |

### movement

| Candidate | Description | Prio |
|-----------|-------------|------|
| `float` | Element hovers calmly up and down (illustrations, onboarding) | medium |
| `marquee` | Text runs through its field (headings, notes) | medium |
| `ken-burns` | Image pans/zooms slowly (background, slideshow) | low |
| `wave` / `drift` | Wave-like movement of rows of points or icons | low |

### organization

| Candidate | Description | Prio |
|-----------|-------------|------|
| `sequence` | Sequence of several animations as a timeline (chained via `onAnimateEnd`) | medium |
| `orchestration` | Parent element starts, children follow, reversed on exit | medium |

## See also

- [Gestures](../gestures/) — Shake, Wiggle as feedback to gestures
- [Components](../../components/) — `toast`, `modal`, `drawer`, `accordion` use animations
- [Standardised data](../../data/) — fields like `animation`, `duration` in component attributes
