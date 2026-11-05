# Pop In - Appearance

## Base layout

The element keeps its layout position and changes only opacity and its own
size. The overshoot acts on the rendering alone – adjacent elements do not
move.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│   0 ms          100 ms          180 ms       250 ms  │
│                                                      │
│  (empty)       ▒▒ Chip ▒▒      [ Chip ]     [ Chip ] │
│  s = 0.80      s = 1.06        s = 0.98     s = 1.00 │
│  α = 0         α = 0.8         α = 1        α = 1    │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Standard** | overshoot 1.06, one after-oscillation (250 ms) |
| **Flat** | `overshoot: 1` – grows without overshooting (looks sober) |
| **Fast** | 150–200 ms for badges and counters |
| **From corner** | `origin: bottom-left` – grows out of the icon corner |

## Duration

- Typical: 200–300 ms
- Default value: 250 ms

## See also

- [Animations overview](../../index.md)
- [Pop Out](../../exit/pop-out/description.md)
- [Scale In](../scale-in/description.md)
- [Bounce In](../bounce-in/description.md)
