# Things 3 — Workflows

> [Things 3](../index.md) · [dialogs](dialogs.md) · [shortcuts](shortcuts.md) · [acceptance](acceptance.md) · [gaps](gaps.md)

Format: goal, requirement, steps (user does X -> program shows Y), errors, undo. Platform Mac. Read from official vendor articles on 2026-11-14 (summarising fetch; URL per workflow); in our own words (ADR 0013). `[nicht belegt]` = not on a page read. IDs T1..T12.

## T1 Capture a to-do quickly
Goal: a new to-do without switching away. Requirement: Quick Entry on (default). Source: https://culturedcode.com/things/support/articles/2249437/
1. Press `Ctrl+Space` -> the Quick Entry popover opens.
2. Type a title, optionally details and the usual keys (list, tag, start date) -> the popover takes them.
3. Press `Cmd+Return` or choose Save -> the to-do is saved and the popover closes.
Errors: none described `[nicht belegt]`. Undo: `Esc` drops unsaved input; undo of a saved to-do `[nicht belegt]`.

## T2 Capture with a link to the current page, mail or file
Requirement: Autofill switched on in Settings > Quick Entry, helper app installed. Source: as T1.
1. Press `Ctrl+Opt+Space` -> the popover shows with the link in the notes.
2. Save as in T1.
Errors: if Things hangs, after about 90 to 120 seconds a message appears; OK, then restart the Mac. Undo: `[nicht belegt]`.

## T3 Drop a to-do into the Inbox target (iPhone/iPad gesture)
Source: https://culturedcode.com/things/support/articles/2803582/ (described for iPhone/iPad; Mac flow `[nicht belegt]`).
1. Drag the Magic Plus button to the Inbox target at the lower left -> the to-do is saved and a popover shows a button "Inbox".
2. Choose another list there -> the to-do is filed there.
Errors and undo: `[nicht belegt]`.

## T4 Set or clear a start date
Source: https://culturedcode.com/things/support/articles/2803579/
1. Select the item, press `Cmd+S` or click the calendar symbol -> the When dialog shows.
2. Pick Today, This Evening, Someday or a day -> the item moves to Today on that day, to Upcoming before it.
3. Clear -> the date goes and the item sits in Anytime.
Errors: `[nicht belegt]`. Undo: Clear.

## T5 Set or clear a deadline
Source: as T4.
1. Press `Shift+Cmd+D` or click the flag -> a date chooser shows.
2. Pick a date -> the deadline is set; the list "Deadlines" shows it. For more than a day of lead time also set a start date.
3. Clear removes it.
Errors and general undo: `[nicht belegt]`.

## T6 Make an item repeat
Requirement: File > New Repeating To-Do, or Items > Repeat on an existing item. Source: https://culturedcode.com/things/support/articles/2803564/
1. Pick "After completion" or a daily, weekly, monthly or yearly pattern -> day choices show for week, month, year.
2. Optionally "Add deadlines" with "days earlier", and a reminder time -> the copy appears earlier in Today.
3. OK -> the schedule is saved.
Errors: a to-do inside a repeating project has no schedule of its own; with several items selected one can pause, resume or end repetition but not change the schedule. Messages `[nicht belegt]`. Undo `[nicht belegt]`.

## T7 Complete a repeating item
1. Tick the copy in Today -> the next copy is made by the pattern. The template or a copy in Upcoming can be ticked early.
2. Checklist points are ticked in the copy only; edits to a copy apply to it alone, edits to the template to later copies.
Source: as T6. Errors and undo: `[nicht belegt]`.

## T8 Tag, filter and un-tag
Source: https://culturedcode.com/things/support/articles/2803581/
1. Open an item, click Tags, type a name, Return -> the tag is made and set; or Window > Tags (`Ctrl+Cmd+T`) to manage tags.
2. Several items: select, `Shift+Cmd+T` -> a tag chooser; or drag a tag onto an item.
3. Remove: click the tag on the item, press Delete -> the link goes, the tag stays.
4. Filter: `Cmd`+click several tags -> only items with all of them; All resets; `Ctrl+Esc` leaves the filter.
Tags of a project or area are not shown on the to-do but count when filtering. Errors and undo: `[nicht belegt]`.

## T9 Find and go anywhere (Quick Find)
Source: https://culturedcode.com/things/support/articles/2803584/
1. Type at once or press `Cmd+F` -> Quick Find shows.
2. Type a name -> suggestions of to-dos, projects, areas, tags.
3. Choose one -> Things opens it. "Continue Search" widens to notes, checklists and logbook.
Errors, Esc and arrow keys: `[nicht belegt]`.

## T10 Move an item to another list or place
Source: https://culturedcode.com/things/support/articles/2785159/ (keys only), https://culturedcode.com/things/support/articles/9651894/ (Items > Move, Move… in a project's context menu).
1. Select, `Shift+Cmd+M` or Items > Move -> a choice of destination (dialog details `[nicht belegt]`).
2. Or copy with `Cmd+C`, go to the target, `Opt+Cmd+V` -> the item is moved there.
3. Within a list `Cmd+Up/Down` one place, `Opt+Cmd+Up/Down` to top or bottom.
Errors and undo: `[nicht belegt]`.

## T11 Complete, cancel, log
Source: as T10 (keys).
1. `Cmd+K` -> completed; `Opt+Cmd+K` -> cancelled.
2. `Shift+Cmd+Y` -> completed items move to the Logbook; `Cmd+6` shows it.
Errors and undo `[nicht belegt]` (no undo key on the page).

## T12 Show calendar events; fix sync
Calendar: Things > Settings > Calendar Events -> tick "Show Calendar Events in Today and Upcoming lists" and the calendars -> events show in Today and Upcoming, read-only and local; only Apple Calendar is read. Source https://culturedcode.com/things/support/articles/2803583/ . Undo: switch the box off.
Sync: Things > Settings > Things Cloud -> check the switch, "Log back in"; after a new login choose "Keep all to-dos (recommended)". Source https://culturedcode.com/things/support/articles/2803590/ . Error texts are not fixed; the vendor asks to note the wording and contact support.
