# Elastic - Appearance

## Base layout

A visible element travels into a fixed final position, shoots past it, and then
settles (`|` = target position).

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│rest          overshoot      back          final      │
│                                                      │
│[■]·····|      ·····|·[■]     ···[■]··|      ····[■]| │
│                                                      │
│past the target, then gently swinging in              │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Gentle** | `overshoot: 10`, one oscillation |
| **Strong** | `overshoot: 40`, three oscillations (game feel) |
| **Scale** | springs in size instead of in position |
| **Damped** | `abklingfaktor: 0.2`, settles quickly |
| **Axis** | only `x`, only `y` or diagonal |

## Duration

- Typical: 400–800 ms

## See also

- [Animations overview](../../index.md)
- [Rubber Band](../rubber-band/description.md)
- [Cross Fade](../../transition/cross-fade/description.md)
