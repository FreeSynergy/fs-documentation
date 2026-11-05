# Apple Mail iOS 26 — Themes

What can be rebuilt with FreeSynergy theming (tokens) and what not. Values are estimated from
screenshots (ADR 0038); nothing is copied (ADR 0013).

| Theme | File | Rebuildable |
|-------|------|-------------|
| Light | [light](light.md) | partly (glass effect) |
| Dark | — not seen ⚠️ | — |

## Theming mechanism
- Mail follows the system appearance (light/dark) ⚠️; no theme choice inside Mail ✅ (none seen).
- Accent colour is the system blue ✅; contact cards take a tint from the contact's poster ✅.
- iOS 26 "glass": translucent, blurred floating controls with a soft highlight edge ✅.
- Text size follows the system (Dynamic Type) ⚠️.

## Not rebuildable / limits
- Real-time refraction/blur of the glass material — only an approximation with blur and
  transparency if the renderer supports it ⚠️.
- SF Pro font and SF Symbols — Apple licence; we use a free sans serif and our own icons.
- Memoji avatars — Apple content.
