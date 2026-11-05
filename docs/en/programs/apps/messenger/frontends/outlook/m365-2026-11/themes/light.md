# Outlook m365-2026-11 — Theme "light"

Values are described (estimated from screenshots), not copied as files (ADR 0013). ✅ = seen.

## Colours
| Token (ours) | Role | Value (approx.) |
|--------------|------|-----------------|
| `color.surface` | panes, reading pane, list | white, #FFFFFF ✅ |
| `color.surface.sunken` | window background, folder pane, title bar | very light grey, ~#F5F5F5 ✅ |
| `color.text` | main text | near-black, ~#242424 ✅ |
| `color.text.muted` | preview line, time, hints | mid grey, ~#616161 ✅ |
| `color.accent` | primary buttons (New mail, Send), active tab underline, unread subject, links | Microsoft blue, ~#0F6CBD ✅ |
| `color.accent.subtle` | selected folder / selected row | pale blue, ~#DCE9F7 ✅ |
| `color.highlight` | flagged / highlighted row | pale yellow, ~#FFF8D6 ✅ |
| `color.danger` | report icon, flag | red, ~#C50F1F ✅ |
| `color.border` | dividers between groups and panes | light grey, ~#E0E0E0 ✅ |
| `color.accent` (variant) | alternative theme accent | violet, ~#8A4FD8 ✅ |

## Typography
- Sans serif UI font (Segoe UI Variable ⚠️), ~14 px in lists and ribbon, sender ~14 px regular,
  section heads ~14 px semibold ✅.
- Composer default body font "Aptos", 11 pt ✅.
- Unread: no bold body, but blue subject + left bar ✅.

## Spacing and shape
- Corner radius ~4 px on buttons and chips, ~8 px on the window and dialogs ✅.
- Rows ~64–72 px with three lines (sender, subject, preview) ✅; chips inside rows ✅.
- Thin 1 px dividers; soft shadow on popovers and the settings dialog ✅.
- Density adjustable ✅.

## Notable details
- Icons are outline style with a few coloured ones (red report, purple reply arrows, yellow quick steps) ✅.
- The Copilot button is the only gradient element ✅.
