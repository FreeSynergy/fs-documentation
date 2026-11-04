# Google Calendar – Shortcuts (as of 2026-11-02)

Google Calendar **does have its own keyboard shortcuts** for the web interface on a computer. The basis is the official help article "Use keyboard shortcuts in Google Calendar" (`https://support.google.com/calendar/answer/37034`, computer version).

## Enabling

Shortcuts are not on by default: **gear "Settings" → tick box "Enable keyboard shortcuts" → "Save"**. Afterwards the key **`?`** (question mark) shows the complete, context-sensitive list inside the calendar itself.

## Navigation

| Action | Key |
|--------|-----|
| Move to the next period | `J` or `N` |
| Refresh the calendar | `r` |
| Go to the current day | `t` |
| Go to the "Add a calendar" section | `+` |
| Move the cursor into the search field | `/` |
| Go to the settings page | `s` |
| Jump to a specific date | `g` |
| Show all shortcuts | `?` |

## Switching views

| View | Key |
|------|-----|
| Day view | `1` or `D` |
| Week view | `2` or `W` |
| Month view | `3` or `M` |
| Custom view | `4` or `X` |
| Schedule view | `5` or `A` |

(A shortcut for the year view is not listed in the official article.)

## Events

| Action | Key |
|--------|-----|
| Create a new event | `c` |
| Open event details | `e` |
| Delete the event | `Backspace` / `Delete` |
| Undo | `z` |
| Save the event (event detail page) | `⌘ + S` (Mac) / `Ctrl + S` (Windows) |
| From event details back to the grid | `Esc` |

## Sidebar (Google Tasks and Google Keep)

| Platform | Keys |
|----------|------|
| Windows | `Ctrl + Alt + .` or `Ctrl + Alt + ,` |
| Chromebook | `Alt + Shift + .` or `Alt + Shift + ,` |
| Mac | `⌘ + Option + .` or `⌘ + Option + ,` |

## Mobile apps

For Android/iOS the help lists **no shortcuts of its own** — there is only touch operation there.

## Direct URLs and automated flows

- **Web interface:** `https://calendar.google.com` — after login straight into the default view
- **ICS addresses:** the "public iCal address" and "private iCal address" are available per calendar under the three-dot menu → "Settings and sharing" (evidenced in the export help article); they can be given to other clients as a subscription URL
- **Subscribing to a calendar by URL:** via "Add other calendars" → "By URL" (reusing your own addresses in other tools)
- **CLI/API workflows (Google-official):** creating events without a UI via the API, e.g.
  `POST https://www.googleapis.com/calendar/v3/calendars/primary/events/quickAdd?text=Zahnarzt+am+Freitag+um+15`
  (method `events.quickAdd`, discovery v3); subscribe to changes via a push channel instead of polling (see [api.md](api.md))

## Shortcuts of third-party clients (client-side only!)

Anyone using Google Calendar inside other programs operates those programs' keys — they are **not** part of Google Calendar:

- **Thunderbird:** `D/W/M` views, `Ctrl+N` new event — only affects Google data if a bridge (extension) mirrors the Calendar API; Google has no native CalDAV
- **Merkuro (KDE):** `Ctrl+N` new event — likewise requires an API/sync bridge
- **Outlook/Exchange wrappers:** Microsoft's own shortcuts, not a Google feature

All these keys merely produce ordinary requests in the respective client; Google Calendar itself does not know them.
