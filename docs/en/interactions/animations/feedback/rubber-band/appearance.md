# Rubber Band - Appearance

## Base layout

The content lies flush against the edge; pulling past the edge creates a damped
gap that snaps shut again after release.

## Visual progress

```
┌──────────────────────────────────────────────────────┐
│edge position     pull-out            springing back  │
│                                                      │
│[content·····]  ┈┈┈ edge ┈┈┈       [content·····]     │
│[············]  [    gap      ]    [············]     │
│[····end·····]  [ content··· ]     [····end·····]     │
│[············]  [ follows pull]    [············]     │
└──────────────────────────────────────────────────────┘
```

## Variants

| Variant | Description |
|---------|-------------|
| **Vertical** | the standard for lists and articles |
| **Horizontal** | paged carousels and tables |
| **One-sided** | only at the top (e.g. the start of pull-to-refresh) |
| **Tough** | `widerstand: 0.15`, strong rubber-band resistance |
| **Off** | hard edges without any deflection (reduced motion) |

## Duration

- Typical: springing back 300–500 ms

## See also

- [Animations overview](../../index.md)
- [Elastic](../elastic/description.md)
- [Stagger](../../organization/stagger/description.md)
