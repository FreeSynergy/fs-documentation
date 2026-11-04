# Outlook calendar – Menu and navigation structure (as of 2026-11-02)

Evidenced by two official support.microsoft.com articles: "Keyboard shortcuts for Outlook" (tabs *New Outlook* / *Classic Outlook* / *Outlook on the web*) and "Use a screen reader to explore and navigate Outlook Calendar" (which describes the regions/layouts explicitly). The original English labels are quoted. Locations in [index.md](index.md#sources).

## New Outlook for Windows / Outlook on the web

```
Horizontal navigation bar (top: search centred; right My Day, notifications, help, settings)
├── Ribbon tabs ("Home" preselected)
├── Left navigation window
│   ├── "New event" button (top)
│   ├── Date selector
│   ├── Calendar list
│   └── far left: view switcher Mail / Calendar / Contacts / To Do
└── Current calendar (main area)
    └── Toolbar on top: month/year, back/forward, month picker,
        view (Day, Work week, Week, Month, Today), sharing (Share)
```

- **Ribbon tab "Home":** among other things new appointment, meeting request, share a calendar — named explicitly in the screen-reader article.
- **Tab "View" → "Calendar settings":** opens the settings window with the tab *Calendar > View* and **sub-tabs** (category navigation via arrow keys); evidenced settings: **work hours and work days**, **out-of-office replies**, **default reminder time**.
- **Search** (top centre) also finds commands/actions ("type the search words for the action").
- **Event editor:** `Ctrl+N` opens the **Event Composer as its own window** (field "Add a title", tab through the fields, "Save" button; discard: Alt+F4).
- **My Day / notifications / help / settings** in the header (the region list of the article).
- **Views:** Day, Work week, Week, Month (+ Today jump); via shortcuts additionally the 3-day and list views (see shortcuts.md).

## Classic Outlook for Windows (calendar module)

```
Ribbon tabs (top)
├── Folder pane (left) – "Calendar folders": your own calendars,
│   the country's public-holiday calendar, shared calendars of colleagues
├── Current calendar view (right)
└── Status bar (bottom)
```

- **Home tab:** new appointment, meeting request, share a calendar — named explicitly in the article.
- **Folder pane:** show/hide calendars with the space bar, expand/collapse folders (arrow keys).
- **Date selection:** `Ctrl+G` opens the date picker; back to today `Alt+H, O, D`.
- **Menu items evidenced by the shortcut list** (the access-key paths name the menus):
  - *Add a shared calendar / create a new calendar:* `Alt+H,O,C`
  - **Share calendar:** `Alt+H,S,C` · **Publish calendar online:** `Alt+H,P,O`
  - **View/change folder sharing permissions:** `Alt+H,F,P`
  - **Send calendar by e-mail:** `Alt+H,E`
  - **Scheduling assistant:** `Alt+X` (from the meeting window)
  - **Reminder window:** `Alt+V,M`; snooze `Alt+S`, dismiss `Alt+D`
  - **Schedule side by side (horizontal layout):** `Alt+H,S,V`
  - **Views:** day grid 1–10 days `Alt+1`…`Alt+0`, month `Alt+ =`, whole week `Alt+-`, work week `Ctrl+Alt+2`, "Next 7 days" `Alt+H,X`
  - **Options dialog for calendars:** `Alt+H,C,O`

## Mobile clients (Outlook for iOS/Android)

- Calendar view with month/week/day switcher and a calendar list; the detail menus are internal to the app — **not** evidenced by the cited articles (only "Outlook for iOS/Android" is named as applies-to), so they are not documented here in detail.

## Server/admin level (Exchange Online)

- Calendar organisation happens through the **Exchange Admin Center / PowerShell** (mailboxes, resources, sharing policies, cross-tenant availability) — a separate product surface, not part of the calendar app's menus; evidence: the migration article "Migrate to Microsoft 365 Cross-Tenant Access Policy" (learn.microsoft.com).

## Limits of this chapter

- The web/client menus change with Microsoft 365 ring releases ("released gradually" — a note in the official article). The items named here come exclusively from the cited official articles; items that could not be evidenced (e.g. "Add subscription", the birthday calendar entry) were left out.
