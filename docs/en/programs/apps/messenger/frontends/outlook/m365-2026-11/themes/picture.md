# Outlook m365-2026-11 — Theme "picture"

A picture theme puts a photo or illustration behind the window; panes sit on top as opaque or
slightly translucent cards. Values estimated (ADR 0013). ✅ = seen.

## Colours
| Token (ours) | Role | Value (approx.) |
|--------------|------|-----------------|
| `color.backdrop` | image behind the panes (landscape, abstract) | image, not a colour ✅ |
| `color.surface` | list, reading pane | white (light) or dark navy (dark) ✅ |
| `color.surface.sunken` | folder pane, ribbon | light: ~#EEF3F8 tinted from the image ✅ |
| `color.accent` | buttons | picked to match the image (blue in all seen samples) ✅ |

## Typography
As [light](light.md) / [dark](dark.md).

## Spacing and shape
- Panes become separate rounded cards with gaps that let the image show through ✅.

## Notable details
- On mobile, the picture fills the header behind the title, bell and search ✅.
- Rebuildable: **partly** — a backdrop image token plus card layout is possible; image-derived
  accent colours need a colour extraction step ⚠️; AI-generated images are out of scope.
