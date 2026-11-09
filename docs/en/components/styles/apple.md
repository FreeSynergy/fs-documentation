# Style: Apple

**Status: measurement sheet, draft (2026-11-10).** The Apple style is rebuilt 1:1 from Apple's own apps (ADR 0066,
addition of 2026-11-09). This sheet collects the measures from Apple's public guidelines, with the source for each value.
Values not found in the public guidelines are marked **not published**. They must be measured from screenshots of
Apple's apps and are never copied from this sheet into a repository as "Apple's values".

Sources, used throughout:

- **HIG Typography**: https://developer.apple.com/design/human-interface-guidelines/typography.md
- **HIG Layout**: https://developer.apple.com/design/human-interface-guidelines/layout.md
- **HIG Lists and tables**: https://developer.apple.com/design/human-interface-guidelines/lists-and-tables.md
- **HIG Materials**: https://developer.apple.com/design/human-interface-guidelines/materials.md
- **HIG Color**: https://developer.apple.com/design/human-interface-guidelines/color.md
- **HIG Accessibility**: https://developer.apple.com/design/human-interface-guidelines/accessibility.md
- **Apple Contacts user guide (Mac)**: https://support.apple.com/guide/contacts/adrb003645bb/mac

The HIG pages were read in their Markdown form on 2026-11-10. Apple's pages may change; re-check before a release.

## 1. Font sizes and line heights

### macOS text styles (points, HIG Typography, "macOS built-in text styles")

| Text style | Weight | Size (pt) | Line height (pt) | Emphasised weight |
|------------|--------|-----------|------------------|-------------------|
| Large Title | Regular | 26 | 32 | Bold |
| Title 1 | Regular | 22 | 26 | Bold |
| Title 2 | Regular | 17 | 22 | Bold |
| Title 3 | Regular | 15 | 20 | Semibold |
| Headline | Bold | 13 | 16 | Heavy |
| Body | Regular | 13 | 16 | Semibold |
| Callout | Regular | 12 | 15 | Semibold |
| Subheadline | Regular | 11 | 14 | Semibold |
| Footnote | Regular | 10 | 13 | Semibold |
| Caption 1 | Regular | 10 | 13 | Medium |
| Caption 2 | Medium | 10 | 13 | Semibold |

Source: HIG Typography, table under "macOS built-in text styles".

### Default Dynamic Type sizes, iOS and iPadOS (points, for reference)

| Text style | Size (pt) | Line height (pt) |
|------------|-----------|------------------|
| Large Title | 34 | 41 |
| Body | 17 | 22 |
| Caption 2 | 11 | 13 |

Source: HIG Typography, iOS Dynamic Type table, default (Large) row. Use only for the iPhone-shaped variant of the
Simple style, not for the desktop style.

### Recommended sizes and minimums

| Platform | Default text size | Minimum text size |
|----------|-------------------|-------------------|
| macOS | 13 pt | 10 pt |
| iOS, iPadOS | 17 pt | 11 pt |

Source: HIG Typography, "Ensuring legibility", and HIG Accessibility, "Vision" table.

Enlargement: give people the option to enlarge text by at least 200 % (HIG Accessibility, "Support larger text sizes").

### Font family

- **SF Pro** is the system font of macOS and iOS (from memory; not confirmed in the pages read in this pass).
- **Licence**: Apple's font licence covers development for Apple platforms only, so SF must not be shipped in our
  packages (from memory; check Apple's developer site). We use an open font (section 9).

## 2. Spacing, grid, and layout

- **Grid (8-point)**: **not found** in the HIG pages read. Do not assume an 8-point grid for Apple style until measured.
- **Padding around controls** (HIG Accessibility, "Offer sufficiently sized controls"): about **12 pt** around elements
  with a bezel (buttons, fields), about **24 pt** around elements without a bezel, measured to the visible edge.
- **Control size** (HIG Accessibility, table "Offer sufficiently sized controls"): macOS default **28 × 28 pt**,
  minimum **20 × 20 pt**. Use the default for the desktop style.
- **Margins, window gutters, sidebar and list widths**: **not published** in the pages read (HIG Layout gives only
  qualitative rules: safe areas, layout guides, "avoid placing controls at the bottom of a window" on macOS).

## 3. Lists and rows

- **Row height, separator inset, icon size, row padding**: **not published** in the HIG Lists and tables page (it gives
  rules only: row-based format for text, alternating row colours in multicolumn tables on macOS, click a column heading
  to sort, resizable columns, outline views for hierarchy).
- Measure from Apple's own apps (Contacts, Mail, Finder) and write the values into this sheet with the screenshot's
  file name.
- **Alternating row backgrounds**: macOS uses the system colour "Alternating content background colors" (HIG Color,
  macOS table). No value.

## 4. Radii

- **Corner radii of windows, sheets, and controls**: **not published** in the HIG pages read. Liquid Glass shapes are
  described as concentric, but no radius value was found in the text. Measure from screenshots.

## 5. Materials (Liquid Glass and standard materials)

Source: HIG Materials.

- **Liquid Glass** forms the functional layer over the content: navigation, toolbars, sidebars. Do not use it in the
  content layer.
- **Variants**: *regular* (blurs and adjusts luminosity; default for most system components, sidebars, alerts,
  popovers) and *clear* (highly translucent; for components over photos and video).
- **Dimming layer for clear Liquid Glass**: if the content underneath is bright, add a **dark dimming layer of 35 %
  opacity**. Not needed over dark or media playback controls.
- **Standard materials** (content layer, macOS): the platform's standard materials with blur and vibrancy. The HIG gives
  no numbers for blur radius or opacity. The thin material brings attention to interactive elements, regular separates
  sidebars and grouped tables, thick gives dark elements that stay distinct.
- **Liquid Glass colour**: apply colour sparingly, to the background of primary actions only (HIG Color, Liquid Glass
  colour).

## 6. Colours

Source: HIG Color, "Specifications / System colors" (values are Apple's reference values; the HIG says they may change
between releases, so do not hard-code them in code, only in this sheet for the look).

| System colour | Default light (RGB) | Default dark (RGB) |
|---------------|---------------------|--------------------|
| Blue | 0, 136, 255 | 0, 145, 255 |
| Red | 255, 56, 60 | 255, 66, 69 |
| Green | 52, 199, 89 | 48, 209, 88 |
| Orange | 255, 141, 40 | 255, 146, 48 |
| Yellow | 255, 204, 0 | 255, 214, 0 |
| Gray (iOS systemGray) | 142, 142, 147 | 142, 142, 147 |

- **Semantic colours** (HIG Color, macOS table): label, secondary label, tertiary label, separator, control background,
  window background, selected content background, keyboard focus indicator colour, control accent. We use the semantic
  names, not the values.
- **Contrast** (HIG Accessibility, WCAG AA as guidance): text up to 17 pt needs **4.5 : 1**; 18 pt and above, or any
  bold text, needs **3 : 1**. Check in light and dark appearance.

## 7. Focus

- Apple names the **keyboard focus indicator colour** (HIG Color, macOS table). The HIG pages read give **no width or
  offset** for the focus ring. Measure from a focused control in the app and record the value here.
- Keyboard use must work with Full Keyboard Access (HIG Accessibility, "Speech").

## 8. Contacts on macOS (layout, for People)

Source: Apple Contacts user guide (see link above), layout only; dimensions are **not published**.

- The window has three parts: a **sidebar** of lists and Smart Lists (toggle with View > Show Lists / Hide Lists; drag
  the separator; drag all the way left to hide), a **contact list** in the middle, and the **card** of the selected
  contact on the right.
- Double-click a contact, or choose Card > Open in Separate Window, to open the card in its own window.
- Name sort order is a preference. Older guides call lists "groups".

Measures to be filled from screenshots of Contacts (window default size, sidebar width, list row height, card width):
**not published**.

## 9. Open fonts with similar measures

No open font is a copy of SF; the measures above are reproduced with our own metrics. Candidates (licence checked as
noted):

| Font | Licence | Note |
|------|---------|------|
| Inter | SIL Open Font License 1.1 | Neutral grotesque, large x-height, close to SF in use. Licence from memory, to be checked on the font's page before shipping. |
| Noto Sans | SIL Open Font License 1.1 | Wide language coverage. Licence from memory, to be checked. |

For the Apple style use **Inter** first; it has the closest feel for the text styles above. Check the licence text in
the font package before any release.

## 10. Screenshots

- None downloaded yet. Apple's HIG images are not reachable at the guessed paths (404), and no official screenshot of
  Contacts was found in this pass. Next step: take them from Apple's own press pages or the App Store listing, store
  them under `/srv/FreeSynergy/.scratch/reference/apple/<programm>/` with a `SOURCES.txt`, never in a repository.
