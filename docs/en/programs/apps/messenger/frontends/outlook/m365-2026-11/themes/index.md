# Outlook m365-2026-11 — Themes

What can be rebuilt with FreeSynergy theming (tokens) and what not. Values are estimated from
screenshots (ADR 0038); nothing is copied (ADR 0013). Token names are our proposals.

| Theme | File | Rebuildable |
|-------|------|-------------|
| Light (default) | [light](light.md) | yes |
| Dark | [dark](dark.md) | yes |
| Picture themes (image behind the panes, light or dark) | [picture](picture.md) | partly |

## Theming mechanism
- **Mode**: light, dark or follow the system ✅ (desktop settings and mobile, each with a small preview) ✅.
- **Themes** on top of the mode: an accent colour (one light variant shows a violet accent instead
  of blue ✅) and **picture themes** that place an image behind the window ✅; AI-generated themes
  ("custom", "weather", "location") ✅ on desktop and mobile.
- **Density** (mobile: separate tab next to design ✅; desktop: "density" in View ✅).
- The mobile header can carry the theme picture ✅.
- Microsoft's design system is Fluent 2 ⚠️ (token-based: neutral, brand, status colours).

## Not rebuildable / limits
- AI-generated and location/weather-driven themes (need a generator service) — no.
- Exact Fluent icon set and the Segoe/Aptos fonts — licence-bound; we use our icon set and a free
  sans serif of similar metrics ⚠️.
- Acrylic/mica translucency of the Windows window frame — platform effect; only an approximation
  with blur, if the renderer supports it ⚠️.
