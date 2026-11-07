# Confluence (Cloud, latest) · Themes

Sources: S-numbers refer to [index.md](../../index.md).

## What the product offers [S17]

- Per-user theme: Light or Dark. Each user chooses. The choice is separate from the site default.
- Site default: Settings > Look and feel > Themes > choose theme > Confirm (admin).
- Themes beyond the built-in list must be installed from the Atlassian Marketplace first. [S17]
- Space theme: a space with "Global look and feel" inherits the site theme and its customisations. How to set another theme for one space: unverified.
- Custom colours or CSS in Cloud: unverified (S17 mentions "customizations" without listing them).

## Design tokens (Atlassian Design System)

Atlassian's own apps use design tokens. These are published and describe the system used by Atlassian products. They are reference material for us: we use the structure (token names, scales), not copied values or palettes. [S18][S19][S21]

| Area | Facts | Source |
|------|-------|--------|
| Colour | All colour tokens start with `color`, then property (background, border, icon, text). Light and dark theme: each token maps to a value per theme. | [S18] |
| Colour | 10 accent colours, each with background, text, border and icon tokens. Accent tokens should not carry meaning (information, warning, success). | [S18] |
| Colour | Input tokens: `color.border.input`, `color.background.input` | [S18] |
| Colour | Atlassian states WCAG AA contrast for its tokens | [S18] |
| Typography | Font families: Atlassian Sans (app font), Atlassian Mono (code). Apps not yet on the system use system fonts. | [S19] |
| Typography | Units: rem; 1 rem = 16 px | [S19] |
| Typography | Type scale tokens: `font.heading.xxlarge` (2 rem / 32 px, line 36 px) down to `font.heading.xxsmall` (0.75 rem / 12 px); `font.body.large` (16 px / 24 px), `font.body` (14 px / 20 px), `font.body.small` (12 px / 16 px); `font.metric.*` for figures; `font.code` (12 px / 20 px) | [S19] |
| Spacing | Base token `space.100` = 8 px = 0.5 rem. Scale: `space.025` (2 px), `space.050` (4 px), `space.075` (6 px), `space.100` (8 px), `space.150` (12 px), `space.200` (16 px), `space.250` (20 px), `space.300` (24 px), `space.400` (32 px), `space.500` (40 px), `space.600` (48 px), `space.800` (64 px), `space.1000` (80 px) | [S21] |

## What can be rebuilt

| Element | Rebuild? | Note |
|---------|----------|------|
| Light and dark themes with a token layer | Yes | Use our own token names and values. |
| Type scale with 14 px body and 16 px large body | Yes | Structure is standard; values are generic. |
| 8 px spacing base | Yes | Structure only. |
| 10-accent palette | Only as our own choice | Do not reproduce Atlassian's hex values. Use our brand palette (the dataviz skill can supply placeholder palettes). |
| Confluence's exact colours, layout tokens and CSS | No | Not published as a copyable resource here; not verified. |

## Not verified

- Hex or RGB values of Confluence's own UI.
- Confluence sidebar and header widths (earlier draft: 50 px and 30 px).
- Confluence-specific font sizes in the editor.
