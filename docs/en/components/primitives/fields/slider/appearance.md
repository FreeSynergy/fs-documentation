# Slider - Appearance

## Base layout
A slider is a value range with a sliding control.

```
┌─────────────────────────────────────────┐
│ Volume                                  │
├─────────────────────────────────────────┤
│ 0% [●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━] 100%│
└─────────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---------|------------|
| **einfach** | one handle, filled area on the left |
| **bereich** | two handles, the section between them is filled |

Vertical sliders are not a variant of their own but `orientation = vertikal`.

## Sizes

| Size | Width | Use |
|------|-------|-----|
| small | 200px | inline |
| medium | 300px | standard |
| large | 400px | featured |
| full | 100% | full width |

## Colours and states

| Status | Colour | Description |
|--------|--------|-------------|
| **track** | grey | track colour |
| **filled** | primary colour | filled colour |
| **thumb** | primary colour | thumb colour |
| **disabled** | grey | deactivated |

## Hover and focus effects

| Effect | Description |
|--------|-------------|
| `scale` | enlargement |
| `shadow` | shadow becomes stronger |

## Responsive

- The track fills the available width (`full` in toolbars), the handles stay
  16 px (desktop) or 24 px (touch) large; the hit area around the handle stays 44 px.
- On narrow screens the value and the scale ends slip above or below the track,
  not beside it.
- A tap on the track jumps to the point hit, the handle follows with `elastic`.

## With labels

```
┌─────────────────────────────────────────┐
│ 10                     [●━━━━━━━━━━]    │
│     50                  100             │
└─────────────────────────────────────────┘
```

## Vertical slider

```
┌─────────────────────────────────────────┐
│ 100                                     │
│   ●                                     │
│  75                                     │
│  50                                     │
│  25                                     │
│   0                                     │
└─────────────────────────────────────────┘
```
