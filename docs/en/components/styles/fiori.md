# Style: SAP Fiori (Admin style)

**Status: measurement sheet, draft (2026-11-10).** The Admin frontend is generated and looks like SAP Fiori (ADR 0066;
Nachtrag 2026-11-09: "Admin-Stil = SAP Fiori, Maße aus den öffentlichen Fiori-Richtlinien"). This sheet gives the
measures with their source.

**Important:** the official SAP Fiori web guidelines pages (sap.com/design-system and experience.sap.com) answer with
HTTP 403 to automated fetching, so the values below are **not** read from those pages. They come from the public theme
tokens that SAP publishes in its open-source repository `SAP/fundamental-styles` (licence Apache-2.0), file
`docs/design-tokens.json`, theme `sap_horizon` (the current Fiori theme). The token file was read on 2026-11-10 and
carries no version number of its own; re-read it before each release. Values in rem are converted to px at the root
size of 16 px.

Sources:

- **Design tokens (sap_horizon)**: https://github.com/SAP/fundamental-styles/blob/main/docs/design-tokens.json (copy of the read file kept in `.scratch`, not in a repository)
- **Theme sources**: https://github.com/SAP/fundamental-styles/tree/main/packages/styles/src/theming
- **Fiori Design Guidelines, Content Density (Cozy and Compact)** (page exists; not reachable by automated fetch):
  https://www.sap.com/design-system/fiori-design-web/v1-120/foundations/visual/cozy-compact

## 1. Font

- The Fiori font is **72**, SAP's own typeface (tokens: `--sapFontFamily` = `"72", "72full", Arial, Helvetica, sans-serif`).
- **We do not use 72.** It is SAP's font; its licence does not allow us to ship it. The open replacement is in section 6.

## 2. Font sizes

Source: `font` category of the token file.

| Token | Value | px |
|-------|-------|----|
| `--sapFontSmallSize` | .75rem | 12 |
| `--sapFontSize` (default, "medium") | .875rem | 14 |
| `--sapFontLargeSize` | 1rem | 16 |
| `--sapFontHeader6Size` | .875rem | 14 |
| `--sapFontHeader5Size` | 1rem | 16 |
| `--sapFontHeader4Size` | 1.25rem | 20 |
| `--sapFontHeader3Size` | 1.5rem | 24 |
| `--sapFontHeader2Size` | 2rem | 32 |
| `--sapFontHeader1Size` | 3rem | 48 |

Use the 14 px default for controls and table cells. The 16 px "large" size is for stand-out items; the Fiori guidance
(search snippet of the Content Density and Typography pages, not read in full) places titles in standard list items there.

## 3. Heights, radii, borders

Source: `element` category of the token file ("Element heights and borders").

| Token | Value | px | Use |
|-------|-------|----|-----|
| `--sapElement_Height` | 2.25rem | 36 | control height (default) |
| `--sapElement_LineHeight` | 2.75rem | 44 | cozy line height and touch target |
| `--sapElement_Compact_Height` | 1.625rem | 26 | compact control height |
| `--sapElement_Compact_LineHeight` | 2rem | 32 | compact line height and row height |
| `--sapElement_Condensed_Height` | 1.375rem | 22 | condensed height |
| `--sapElement_Condensed_LineHeight` | 1.5rem | 24 | condensed line height |
| `--sapElement_BorderCornerRadius` | .75rem | 12 | corner radius of elements |
| `--sapElement_BorderWidth` | .0625rem | 1 | element border |
| `--sapList_BorderWidth` | .0625rem | 1 | list border |

Density (SAP guidelines, Content Density page, as summarised by the search snippet): **cozy** is the default for most
controls and for touch devices; **compact** keeps font size and shrinks the components and gaps, for mouse and keyboard.
Cozy and compact are never mixed on one page. **Proposal (not a SAP rule):** the Admin frontend starts in **compact**,
because it shows dense data, with cozy as a setting. This needs the owner's decision.

## 4. Spacing and layout

Source: `content_ui` and `shell` categories of the token file.

| Token | Value | px |
|-------|-------|----|
| `--sapContent_Space_Tiny` | 0.5rem | 8 |
| `--sapContent_Space_S` / `_Small` | 1rem | 16 |
| `--sapContent_Space_M` / `_Medium` | 2rem | 32 |
| `--sapContent_Space_L` / `_Large` | 2rem / 3rem | 32 / 48 |
| `--sapContent_Space_XL` | 3rem | 48 |
| `--sapContent_Gap` | 1rem | 16 |
| `--sapContent_Margin_S` / `_Tiny` | 0 0 1rem | 0 0 16 |
| `--sapContent_Margin_M` / `_Small` | 1rem | 16 |
| `--sapContent_Margin_Medium` / `_L` | 1rem 2rem | 16 32 |
| `--sapContent_Margin_Large` / `_XL` | 1rem 3rem | 16 48 |
| `--sapContent_Padding_S` | 0 | 0 |
| `--sapContent_Padding_M` / `_L` | 2rem | 32 |
| `--sapContent_Padding_XL` | 3rem | 48 |
| `--sapShell_Gap_S` | .5rem | 8 |
| `--sapShell_Gap_M` / `_L` / `_XL` | 1rem | 16 |
| `--sapShell_GroupGap_S` | 2rem | 32 |
| `--sapShell_GroupGap_M` / `_L` / `_XL` | 3rem | 48 |

The rhythm is 8 px at the smallest step, then 16, 32 and 48 px. The base unit of 4 px appears only in icon padding
(not in these tokens).

## 5. Colours and focus

Source: `list`, `field`, `content_ui`, `text` categories.

- **Focus**: `--sapContent_FocusColor` = `#0032a5`, `--sapContent_FocusStyle` = solid, `--sapContent_FocusWidth` =
  .125rem (**2 px**). Field focus border: `--sapField_Focus_BorderColor` = `#0032a5`, background `#fff`.
- **Lists**: background `--sapList_Background` `#fff`; alternating rows `--sapList_AlternatingBackground` `#f5f6f7`;
  border `--sapList_BorderColor` `#e5e5e5`, width 1 px; active row `--sapList_Active_Background` `#dee2e5`, text
  `#131e29`; group header border `#a8b2bd`.
- Contrast: check text against the list and field backgrounds in light and in the high-contrast theme (the tokens
  have `_hc` variants).

## 6. Open font with similar measures

| Font | Licence | Note |
|------|---------|------|
| Noto Sans | SIL Open Font License 1.1 | Neutral humanist sans with a large x-height; similar text width to 72 at 14 px. Licence from memory; check before shipping. |
| Inter | SIL Open Font License 1.1 | Designed for interface text at 12 to 16 px; close to 72 in use. Licence from memory; check before shipping. |

Use **Inter** for the Admin style first; Noto Sans as the fallback where a script is missing. Check the measures with
the metric test before the tag (text width of long labels in table cells).

## 7. Screenshots

- None downloaded. The guidelines pages block automated access (403), and the SAP sample pages found do not contain a
  stable image path. Next step: take official screenshots from SAP's documentation or the SAP Fiori Launchpad demo, if
  its terms allow, and store them in `/srv/FreeSynergy/.scratch/reference/fiori/<programm>/` with `SOURCES.txt`.
