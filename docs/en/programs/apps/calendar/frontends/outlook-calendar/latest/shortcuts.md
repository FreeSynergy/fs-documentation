# Outlook calendar – Keyboard shortcuts and direct workflows (as of 2026-11-02)

All shortcuts come from the official article "Keyboard shortcuts for Outlook" (support.microsoft.com, tabs *New Outlook for Windows*, *Classic Outlook*, *Outlook on the web*; US layout — other layouts may differ). According to the article the calendar shortcuts of Teams and Outlook are identical. Mac shortcuts: a separate article "Keyboard shortcuts in Outlook for Mac" (not taken over here in detail). Locations in [index.md](../index.md#sources).

## New Outlook for Windows / Outlook on the web

### Navigation and views

| Key(s) | Function |
|--------|----------|
| `Ctrl+2` | switch to the calendar view (in general: `Ctrl+1` Mail, `Ctrl+3` Copilot, `Ctrl+4` People) |
| `Alt+Shift+Y` / `Home` | today |
| `Ctrl+Alt+Left` / `Alt+Down` / `Alt+PageDown` | back: day / week / month |
| `Ctrl+Alt+Right` / `Alt+Up` / `Alt+PageUp` | forward: day / week / month |
| `Ctrl+Alt+Right` / `Ctrl+Alt+Left` | next/previous period |
| `Ctrl+Alt+1` | day view |
| `Ctrl+Alt+2` (also `Alt+-`) | week view; work week likewise `Ctrl+Alt+2` |
| `Ctrl+Alt+4` (also `Alt+ =`) | month view |
| `Alt+3` | 3-day view |
| – | list view (officially: "No shortcut") |
| `F6` / `Ctrl+Shift+Tab` | move between regions; `Tab`/`Shift+Tab` to the next/previous event |

### Actions

| Key | Function |
|-----|----------|
| `Ctrl+N` | create a new event (also "Invite Attendees" via New event) |
| `Enter` / `Delete` | open / delete the selected item |
| `?` | open the shortcut overview; `Alt` = key tips |

## Classic Outlook for Windows (calendar)

| Key | Function |
|-----|----------|
| `Ctrl+Shift+A` | appointment in any view; in the calendar view also `Ctrl+N` |
| `Ctrl+Shift+Q` | create a meeting request |
| `Alt+1`…`Alt+9`, `Alt+0` | day grid of 1–9 days respectively 10 days |
| `Alt+-` / `Ctrl+Alt+3` | whole week · `Ctrl+Alt+2` work week · `Alt+ =` / `Ctrl+Alt+4` month |
| `Ctrl+G` | "Go to date" (date picker) – in an open event: set the recurrence |
| `Alt+H, O, D` | show today · `Alt+H, X` next 7 days |
| `Ctrl+Left/Right` | previous/next day; `Alt+Up/Down` week; `Alt+PageUp/PageDown` month |
| `Alt+Home` / `Alt+End` | start / end of week |
| `Ctrl+Comma` / `Ctrl+Period` | previous/next event |
| `Alt+X` | scheduling assistant |
| `Alt+V,M` / `Alt+S` / `Alt+D` / `Alt+O` | reminder window / snooze / dismiss / open the event in the reminder |
| `Alt+H,S,V` (`Ctrl+Alt+5`) | schedule in horizontal layout (compare calendars) |
| `Alt+H,O,C` / `Alt+H,S,C` / `Alt+H,P,O` / `Alt+H,F,P` / `Alt+H,E` | add calendar / share / publish online / sharing rights / send calendar by e-mail |
| `Alt+F11` / `Alt+F8` | VBA editor / run macros (classic Outlook only) |

## Outlook for Mac

- Its own shortcuts page (linked in the article as "Keyboard shortcuts in Outlook for Mac") — **not** taken over in this pass; not verified.

## No command line of its own

- The calendar app itself has **no CLI/OCC-like commands**. Automation runs over **Microsoft Graph** (REST + SDKs, see [api.md](api.md)); server administration over **Exchange Online PowerShell** (`Set-MailboxFolderPermission` etc. belongs to the Exchange level, not to the app).

## Direct-URL/deep-link workflows

- The deep-link formats are **officially documented** through the `webLink` description of the event resource: current form `https://outlook.office365.com/calendar/item/{event-id}` (work/school account) or `https://outlook.live.com/calendar/item/{event-id}` (private account), where `{event-id}` is the URL-encoded event `id`. The old `…/owa/?itemid=…&path=/calendar/item` form only opens older web versions; the links do not work in an iFrame and otherwise prompt for a login.

## Shortcuts of third-party clients (by way of distinction)

- Thunderbird, Merkuro, Apple Calendar, DAVx⁵ etc. have their own client-side shortcuts with no relation to Outlook. Since Outlook accounts offer these clients no open CalDAV access anyway, connecting them only works through Microsoft apps or third-party connectors (unofficial).
