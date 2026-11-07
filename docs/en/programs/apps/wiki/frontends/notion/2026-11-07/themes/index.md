# Notion — themes (2026-11-07)

Notion publishes no design tokens (colours, font sizes, spacing values) on the pages read. Only the options a user can choose are documented. Values in pixels or hex codes are not given here. The earlier file gave values (14–16px text, a light and a dark palette) that are not in any official source read: removed.

## Account-level theme

| Option | Source |
|--------|--------|
| System, light, dark (desktop Appearance setting) | [S23] (search snippet, page not fetched) |
| Toggle dark and light: cmd/ctrl + shift + L | [S11] |

## Page-level styling [S15]

Found under the page menu (••• at top right), group "Appearance & layout".

| Option | Values | Notes |
|--------|--------|-------|
| Font | Default, Serif, Mono | Applies to all text on the page |
| Small text | on / off | Shrinks page text |
| Full width | on / off | Shrinks margins, widens content |
| Table of contents | on / off | Headings in callouts are also listed |

Small text and full width are desktop and web only [S15].

## Icons and covers [S15]

| Element | Options | Size note |
|---------|---------|-----------|
| Page icon | emoji, icon, uploaded image | about 280 × 280 px recommended |
| Cover | Notion gallery, upload, pasted link, Unsplash search | at least 1500 px wide |

## Text colour and highlight

- `/color` changes text colour or highlight; `/default` removes it; cmd/ctrl + shift + H reapplies the last colour [S11].
- The list of colour names is not in the pages read: unverified.

## What can be rebuilt

| Item | Rebuildable | Note |
|------|-------------|------|
| Light and dark mode, switch from system | yes | Options are documented; exact palette is not |
| Font choice per page (Default, Serif, Mono) | yes | Use our own font stacks |
| Small text and full width toggles | yes | Desktop and web |
| Table of contents from headings | yes | Behaviour as documented [S15] |
| Icon and cover | yes | Behaviour as documented; use our own image pipeline |
| Colour palette, font sizes, spacing | no source | Design our own; do not copy Notion values |

## Sources

[S11], [S15], [S23]. Palette and spacing: no official source found.
