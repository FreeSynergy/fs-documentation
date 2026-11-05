# Key Verification - Appearance

## Base layout

```
┌──────────────────────────────────────┐
│ Verify Anna's key                    │
│ 4F2A 91BC 77D0 1E5A                  │
│ 0B3C 9A44 D1E8 62F0     ▒▒▒▒ QR     │
│ [ They match ]  [ They differ ]      │
└──────────────────────────────────────┘
```

## Variants

| Variant | Appearance |
|---|---|
| **fingerprint** | monospace groups of four |
| **qr** | square QR code, caption below |
| **device-list** | rows with state glyph |

## Sizes

| Size | Height | Use |
|---|---|---|
| `medium` | 360 px | dialog |
| `large` | 480 px | with device list |

## Colours and states

| State | Appearance |
|---|---|
| `unverified` | warning tone |
| `verified` | success tone |
| `mismatch` | error tone |

## Hover and focus effects

| Effect | Description |
|---|---|
| `background` | button hover as for [button](../../../primitives/actions/button/) |

## Responsive

- Full-screen sheet on narrow screens.
- Fingerprint groups wrap into two lines.
