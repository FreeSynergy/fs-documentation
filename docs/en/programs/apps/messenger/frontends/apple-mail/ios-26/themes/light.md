# Apple Mail iOS 26 — Theme "light"

Values are described (estimated from screenshots), not copied as files (ADR 0013). ✅ = seen.

## Colours
| Token (ours) | Role | Value (approx.) |
|--------------|------|-----------------|
| `color.surface` | list background | white, #FFFFFF ✅ |
| `color.surface.sunken` | grouped background behind cards and sheets | light grey, ~#F2F2F7 ✅ |
| `color.text` | titles, sender, subject | black, ~#000000 ✅ |
| `color.text.muted` | preview, time, subtitle | grey, ~#8A8A8E ✅ |
| `color.accent` | active chip, Done button, links, icons | system blue, ~#007AFF (chip ~#3E8EED) ✅ |
| `color.danger` | delete action | red, ~#FF3B30 ✅ |
| `color.warning` | flag action, flag icon | orange, ~#FF9500 ✅ |
| `color.neutral` | "More" action, inactive chips | grey, ~#C7C7CC / ~#E5E5EA ✅ |
| `color.vip` | VIP star | yellow, ~#FFCC00 ✅ |
| flag palette | flag colours | orange, red, purple, cyan, yellow, green, grey ✅ |
| category icons | Transactions / Updates / Promotions | green / purple / pink ✅ |

## Typography
- Large title ~34 pt bold ✅; sender ~17 pt semibold; subject ~15 pt; preview ~15 pt regular grey ✅.
- System sans serif (SF Pro ⚠️).

## Spacing and shape
- Generous rows (~100 pt with two-line preview) ✅; hairline separators inset to the text ✅.
- Capsules everywhere: chips, search, buttons ✅; sheets and cards with large radius (~26–32 pt) ✅.
- Swipe action buttons are circles (~56 pt) with a label underneath ✅.
- Floating controls with soft shadow and translucent glass ✅.

## Notable details
- No visible dividers between header and content; content scrolls under floating controls ✅.
- Contact card sheet is tinted (mauve in the sample) from the contact's chosen colour ✅.
