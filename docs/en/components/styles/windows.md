# Style: Windows

**Status: measurement sheet, draft (2026-11-10).** The Windows style is rebuilt 1:1, one Windows program per category,
preferably one that has no Linux counterpart (ADR 0066, addition of 2026-11-09). No Linux program is a template. This
sheet collects the measures from Microsoft's public guidelines with the source for each value. Values not found in the
public guidelines are marked **not published** and must be measured from screenshots.

Sources, used throughout:

- **Fluent 2, Spacing and proximity / Layout**: https://fluent2.microsoft.design/layout
- **Fluent 2, Shapes**: https://fluent2.microsoft.design/shapes
- **Fluent 2, Typography (web ramp)**: https://fluent2.microsoft.design/typography
- **Windows, Typography in Windows 11 (type ramp, font rules)**: https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography
- **Windows, Geometry in Windows 11 (corner radii)**: https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/geometry
- **Windows, Acrylic material**: https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic
- **Windows, Mica material**: https://learn.microsoft.com/en-us/windows/apps/design/style/mica
- **Windows, Keyboard accessibility**: https://learn.microsoft.com/en-us/windows/apps/design/accessibility/keyboard-accessibility

Fluent 2 and Windows 11 differ in places (noted below). Where they differ we use the Windows 11 value for the desktop
style and record the Fluent value next to it.

## 1. Font sizes and line heights

### Windows 11 type ramp (effective pixels, epx; Windows Typography page)

| Style | Weight | Size / line height |
|-------|--------|--------------------|
| Caption | Regular | 12 / 16 |
| Body | Regular | 14 / 20 |
| Body strong | Semibold | 14 / 20 |
| Body large | Regular | 18 / 24 |
| Body large strong | Semibold | 18 / 24 |
| Subtitle | Semibold | 20 / 28 |
| Title | Semibold | 28 / 36 |
| Title large | Semibold | 40 / 52 |
| Display | Semibold | 68 / 92 |

Source: Windows Typography page, "Type ramp" table. Bold and italic are not part of the ramp; use Semibold for emphasis.

### Fluent 2 web ramp (px; Fluent 2 Typography page)

| Style | Weight | Size / line height |
|-------|--------|--------------------|
| Caption 2 | Regular | 10 / 14 |
| Caption 1 | Regular | 12 / 16 |
| Body 1 | Regular | 14 / 20 |
| Subtitle 2 | Semibold | 16 / 22 |
| Subtitle 1 | Semibold | 20 / 26 |
| Title 3 | Semibold | 24 / 32 |
| Title 2 | Semibold | 28 / 36 |
| Title 1 | Semibold | 32 / 40 |
| Large Title | Semibold | 40 / 52 |
| Display | Semibold | 68 / 92 |

Source: Fluent 2 Typography page. Note the differences to the Windows ramp: Subtitle is 20 / 26 on the web and 20 / 28
in Windows 11; the web ramp has Caption 2 at 10 / 14 and Title 3 at 24 / 32, which Windows does not list.

### Legibility minimums (Windows 11)

- **14 px Semibold** or **12 px Regular** is the smallest text the Windows guidance allows (Windows Typography page,
  "Best practices" table). Smaller text is illegible in some languages.
- Sentence case for all UI text. Ellipses for most truncation; clipping only in rare cases.
- 50 to 60 letters per line for reading text (Windows Typography page, "Character count").

### Font family

- **Segoe UI Variable** is the Windows system font (Windows Typography page). Axes: weight 100 to 700 and an automatic
  optical size from 8 pt to 36 pt.
- We do not ship Segoe UI Variable (Microsoft's font). See section 9 for open replacements.

## 2. Spacing, grid, and geometry

- **Spacing ramp (web, Fluent 2 Layout page)**: a base unit of **4 px**. Tokens in px: 0, 2, 4, 6, 8, 10, 12, 16, 20,
  24, 28, 32, 36, 40, 48, 52, 56. The 2, 6 and 10 values are for icon padding.
- **Minimum touch target** (Fluent 2 Layout page, "Applying Fluent spacing"): 44 × 44 px for web and iOS, 48 × 48 for
  Android (the page gives no separate desktop value).
- **Breakpoints** (Fluent 2 Layout page): small 320–479 px, medium 480–639, large 640–1023, x-large 1024–1365, xx-large
  1366–1919, xxx-large 1920 and up.
- **Grid**: a 12-column framework is the usual choice; gutters and margins are multiples of the base unit and change by
  breakpoint. **No concrete margin or gutter value** is given on the page read.
- **Corner radii** (Windows Geometry page, "Rounded corners"):

| Element | Radius |
|---------|--------|
| Top-level containers: app windows, flyouts, dialogs | 8 px |
| In-page elements: buttons, list backplates, text boxes, list views | 4 px |
| Bar elements: progress bars, scroll bars, sliders | 4 px |
| Tooltip (exception) | 4 px |
| Snapped or maximised windows | 0 px |

  Global resources: `ControlCornerRadius` (4 px) and `OverlayCornerRadius` (8 px).
- **Fluent corner tokens** (Fluent 2 Shapes page): 0, 2, 4, 8, 12 px and circle. Windows uses 4 and 8 only.
- **Stroke width tokens** (Fluent 2 Shapes page, web): 1, 2, 3, 4 px.

## 3. Lists and rows

- **Row height, separator, icon size, padding of list items**: **not published** in the pages read. Windows 11 uses
  list views with 4 px corners (section 2). Measure from the Windows program templates (section 8).

## 4. Materials

### Mica (Microsoft Learn, Mica material)

- Opaque, dynamic material for the **base layer** of long-lived windows (apps and settings). It samples the wallpaper
  once and falls back to a solid colour when the window is inactive.
- Mica Alt is a variant with stronger tint, for tabbed title bars. Mica is visible in the title bar only if the app
  extends into the non-client area.
- Content layers sit on top with the low-opacity `LayerFillColorDefaultBrush` (standard pattern, or cards).
- Do not apply a backdrop material twice in one application. Do not apply it to a single element.
- Fallback colours: `SolidBackgroundFillColorBase` (Mica), `SolidBackgroundFillColorBaseAlt` (Mica Alt).
- **No numeric blur or opacity values** are given on the page read.

### Acrylic (Microsoft Learn, Acrylic material)

- Translucent texture for **transient surfaces** (menus, flyouts, popups: background acrylic) and **supporting panes**
  (in-app acrylic).
- Recipe (from the page): background, blur, exclusion blend layer (for contrast), colour tint, noise.
- Do not place multiple acrylic panes next to each other (visible seam). Do not put accent-coloured text on acrylic.
- Acrylic turns solid when transparency is off, in Battery Saver, on low-end hardware, or when a background window
  deactivates.
- **No numeric blur, noise or tint values** are given on the page read.

Our desktop style uses the flat Fluent surface: opaque layers, Mica-like base where it fits. Acrylic only for transient
surfaces, and the blur value is to be measured from the screenshots in section 10.

## 5. Colours

- The Windows colour values are **theme tokens** (for example `SolidBackgroundFillColorBase`); the public pages read give
  the token names and the light and dark behaviour, not the hex values. Values are not published in the pages read.
- Legibility: text must meet contrast on acrylic (Acrylic page). Use Windows' text colours, not custom accents, on
  translucent surfaces.

## 6. Focus

- **Keyboard focus visual** (Keyboard accessibility page): a dashed rectangle outline on the focused control, drawn in
  two colours (a white and a black stroke with a `1,1` dash array), shown on focus and hidden otherwise. The page gives
  **no pixel width or offset**; the WinUI resources hold them. Measure from a focused Windows control.
- Keyboard rules from the same page: every control reachable by Tab; tab order follows the visual order; arrow keys in
  lists and grids; Spacebar and Enter activate; F6 moves between major regions (must be implemented explicitly).
- Shortcuts are shown in tooltips and exposed as accelerator and access keys.

## 7. Contacts in Windows (People and Outlook, for People)

The classic People app is no longer part of current Windows 11 (secondary sources say it was removed in 24H2). Contacts
now live in the **new Outlook for Windows**, which shows a People view.

- **Layout** (per Topedia blog, 11 January 2026, a third-party report of Microsoft's refresh): a **modern, multi-column
  layout** with search; duplicate contacts are linked automatically; organisational profile data enriches contacts.
  Profile cards put **organisational information first**; a multiple-sources indicator appears for contacts linked to
  an Entra account; personal details are editable, organisational data is not; a contact can be unlinked.
- Sources: https://blog.topedia.com/2026/01/outlook-gets-an-improved-people-app/ (third party),
  https://mc.merill.net/message/MC927963 (Microsoft Message Center notice on the People Hub, rollout notice).
- **Dimensions** (pane widths, card width, row heights): **not published**. Measure from screenshots of the new Outlook
  and record them here with source and date.

## 8. Windows program templates (approved 2026-11-10)

Approved by the owner through the coordinator. The list is entered in `docs/en/programs/map.md`, section "Windows
templates". Three entries are open and need a decision (see the notes there): Whiteboard (the standalone Windows app
retires on 2026-10-16 according to Microsoft's support page), Forms and YouTube Studio (web services, no Windows app).

| Category | Windows program | Linux counterpart |
|----------|-----------------|-------------------|
| People | Outlook (People view) | none native |
| Mail | Outlook (Mail) | none native |
| Calendar | Outlook (Calendar) | none native |
| Groups | Microsoft Teams | none native |
| Tasks | Microsoft To Do | none native |
| Files | File Explorer | not a Linux program |
| Gallery (facet of Files) | Microsoft Photos | none native |
| Videos | Media Player (new app or Windows Media Player Legacy, to decide) | none native |
| Wiki | Microsoft OneNote | none native |
| Maps | Google Earth Pro (Windows; no Street View frontend) | to check (Linux desktop build) |
| Whiteboard | Microsoft Whiteboard (open: retirement) | web only |
| Surveys | Microsoft Forms (open: web only) | web only |
| Resources | Microsoft Excel | none native |
| Streaming | YouTube Studio (open: web only) | web only |
| Store | Microsoft Store | Linux stores are Linux programs; not used |
| Start | Start menu and Widgets | not a Linux program |
| Identity | Settings > Accounts, plus Windows Hello | a settings page |
| History | none | no template |

## 9. Open fonts (chosen)

| Font | Licence (checked 2026-11-10) | Use |
|------|------------------------------|-----|
| Selawik | SIL Open Font License 1.1; copyright Microsoft; the name "Selawik" is reserved, so derived versions must be renamed (Microsoft Learn font list: https://learn.microsoft.com/en-us/typography/font-list/selawik) | Windows style. Open replacement for Segoe UI, metrically compatible with it |
| Inter | SIL Open Font License 1.1 (licence file of https://github.com/rsms/inter, "Copyright (c) 2016 The Inter Project Authors") | Apple style, and fallback for Windows if Selawik does not suit |
| Noto Sans | SIL Open Font License 1.1 (licence file of https://github.com/notofonts/noto-fonts, "Copyright 2018 The Noto Project Authors") | Script fallback |

Before a release, ship the licence file next to each font file and check the reserved-name rule for Selawik.

## 10. Screenshots

Under `/srv/FreeSynergy/.scratch/reference/windows/` (never in a repository), each folder with a `SOURCES.txt`:

- `mica/`: `mica-light-theme.png`, `mica-dark-theme.png`, `mica-alt-tabs.png` (Microsoft Learn, Mica material)
- `acrylic/`: `acrylic-light-theme-base.png`, `acrylic-dark-theme-base.png` (Microsoft Learn, Acrylic material)
- `corners/`: `button.png`, `flyout.png` (Microsoft Learn, Geometry in Windows 11)

Still missing, per approved program:

- **Outlook and To Do**: Microsoft's support page "Use My Day with To Do in Outlook" has screenshots (`new-outlook-my-day-calendar-tab`, `new-outlook-to-do-my-day-to-do-tab-open-to-do`). The image links the tool returned do not resolve (404), so they are not downloaded.
- **File Explorer**: support page "File Explorer in Windows" (https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows); image links returned by the tool do not resolve yet.
- **Teams**: support page "Overview of teams and channels" (https://support.microsoft.com/en-us/office/overview-of-teams-and-channels-c3d63c10-77d5-4204-a566-53ddcf723b46).
- **Settings > Sign-in options**: https://support.microsoft.com/en-us/accounts-billing/security/sign-in-options-in-windows.
- **Photos, Media Player, OneNote, Excel, Google Earth Pro, Forms, YouTube Studio, Store, Start, Widgets**: no screenshot found in this pass; the support pages were searched, but their images were not fetchable.

Next step: open the official pages in a browser, check the image addresses there, and download them with a SOURCES.txt entry for each image.
