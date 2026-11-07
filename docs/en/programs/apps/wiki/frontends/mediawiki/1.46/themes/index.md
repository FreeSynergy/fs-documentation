# MediaWiki 1.46 — Themes (Vector 2022 and Codex tokens)

Version: 1.46.2. Sources:
- Codex light theme tokens: https://github.com/wikimedia/codex/blob/main/packages/codex-design-tokens/src/themes/wikimedia-ui.json
- Codex dark mode tokens: https://github.com/wikimedia/codex/blob/main/packages/codex-design-tokens/src/modes/dark.json
- Codex application tokens (spacing, radius, font-size scale): https://github.com/wikimedia/codex/blob/main/packages/codex-design-tokens/src/application.json
- Vector 2022 LESS variables: https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/resources/skins.vector.styles/variables.less
- Vector ADR 0002 (CSS custom properties): https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/doc/adr/0002-use-css-custom-properties.md
- Vector configuration (appearance preferences): https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/doc/configuration/configuration.md

## How themes work

- Vector 2022 styles come from Codex design tokens (the "WikimediaUI" theme). The token names carry over into Vector's LESS variables. Source: `variables.less`, comment on the font stack.
- Vector's own tokens are few and marked `@private` and `@experimental` in ADR 0002. They should not be relied on by an outside frontend. Use the Codex token names and values instead.
- Appearance is a user preference, not a separate theme file. Night mode is `vector-theme` with values `day`, `night`, `os`. Logged-in users can force night mode with `?vectornightmode=night` or `=1` (configuration.md).
- Text size: `vector-font-size` = 0 (regular), 1 (large), 2 (x-large) (configuration.md).
- Width: `vector-limited-width` = 1 (limited) or 0 (full width) (configuration.md).

## Colours (light theme, Codex WikimediaUI)

Read from `themes/wikimedia-ui.json`. Mapping of `wmui-color.base*` tokens (the text and background scale):

| Token | Resolves to | Hex |
|-------|-------------|-----|
| `base0` | black | #000 |
| `base10` | gray900 | #202122 (main text) |
| `base20` | gray600 | #54595d |
| `base30` | gray500 | #72777d |
| `base50` | gray400 | #a2a9b1 |
| `base70` | gray300 | #c8ccd1 |
| `base80` | gray100 | #eaecf0 |
| `base90` | gray50 | #f8f9fa (page background tint) |
| `base100` | white | #fff |
| `modifier-base10--lighten` | gray700 | #404244 |

Accent (links, progressive actions): the light value of `color.progressive` was not read in this run. The `accent` token resolves to `blue700` (themes/wikimedia-ui.json, `color.accent`). Verify the progressive hex before use.

## Colours (dark mode, Codex)

Read from `modes/dark.json`:

| Token | Resolves to |
|-------|-------------|
| `color.progressive` | blue400 |
| `color.progressive--hover` | blue300 |
| `color.progressive--active` | blue200 |
| `background-color.progressive-subtle` | blue1000 |
| `border-color.progressive` | blue500 |
| `box-shadow.color.progressive--focus` | blue500 |

Hex values of the blue scale were not read in this run. Base text and background dark values were not read either. Take them from `modes/dark.json` directly when building.

## Typography

From `themes/wikimedia-ui.json` (font-family tokens):

| Token | Stack (first entries) |
|-------|------------------------|
| `font-family.sans-100` | -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Inter, Helvetica, Arial, sans-serif |
| `font-family.serif-100` | 'Linux Libertine', Georgia, Times, 'Source Serif 4', serif |
| `font-family.monospace-100` | Menlo, Consolas, 'Liberation Mono', 'Fira Code', 'Courier New', monospace |

Vector sizes (variables.less):

| Variable | Value |
|----------|-------|
| `@font-size-heading-1` | 1.8em |
| `@font-size-heading-2` | 1.5em |
| `@font-size-heading-3` | 1.2em |
| `@font-size-footer` | 12px equivalent (12/16 em) |
| `@font-size-search-input` | 13px equivalent (13/16 em) |
| `@line-height-base` | 1.6 |
| `@line-height-code` | 1.3 |
| `@line-height-nav` | 1.125em |
| `@size-icon` | 20px equivalent (20/16 em) |

Codex font-size scale (application.json): x-small = 75, small = 90, medium = 100, large = 110, x-large = 125, xx-large = 150, xxx-large = 175 (percent-style tokens).

## Spacing and radius

| Token | Mapping (application.json) |
|-------|----------------------------|
| `spacing.25` … `spacing.400` | each maps to `dimension.<n>`; exact px values for `dimension.*` were not read in this run |
| `border-radius.base` | `dimension.absolute.2` (2 px) |
| `border-radius.pill` | `dimension.absolute.9999` |
| `border-radius.circle` | `dimension.half` |

Vector uses `@spacing-150` and `@spacing-300` for content box padding (variables.less). Their px values come from `dimension.*` and were not read in this run.

## Layout tokens

Vector layout values (variables.less): page container max 1596px, content max 948px, desktop side padding 44px (52px on wide screens), header 50px, search max 500px, grid gap 24px, heading scroll margin 75px. Full table in `../layout.md`.

## What can be rebuilt

| Item | Rebuildable? | Notes |
|------|--------------|-------|
| Light and dark palette using Codex token names | yes | Use the values above. Verify the progressive colour and the dark base values first. |
| Font stacks | yes | Copy the names of the families, not the files. Fonts are the OS stacks. |
| Type scale and line height | yes | From the LESS variables; values are listed above. |
| Three-column grid and widths | yes | From `layout.md`. |
| Sticky header and pinned panels | yes, as behaviour | Behaviour is in Vector JS; we describe it and build our own. |
| Vector's exact icons and images | no | Icons are assets in the Vector repo. We must not copy them (ADR 0013 rule: no copying). Use our own icons. |
| Vector's CSS custom properties | not as an API | `@private` and `@experimental` in ADR 0002. Use our own tokens named after the Codex names. |

## Not verified

- Hex values of blue (progressive) in light mode.
- Dark base and surface colours.
- Exact px values of Codex spacing and radius tokens.
- Vector breakpoints for the responsive variant.
