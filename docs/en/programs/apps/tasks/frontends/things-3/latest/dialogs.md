# Things 3 — Dialogs

> [Things 3](../index.md) · [features](features.md) · [menus](menus.md) · [workflows](workflows.md)

Platform: Mac unless stated. All rows are read from official vendor support articles on 2026-11-14, through a summarising fetch (checked by a sample against the raw page text, see BERICHT.md); behaviour is in our own words (ADR 0013). `[nicht belegt]` = not found on a page read. Sources: Quick Entry https://culturedcode.com/things/support/articles/2249437/ (Q), Gestures/Magic Plus https://culturedcode.com/things/support/articles/2803582/ (G), When/Deadline https://culturedcode.com/things/support/articles/2803579/ (W), Repeat https://culturedcode.com/things/support/articles/2803564/ (R), Tags https://culturedcode.com/things/support/articles/2803581/ (T), Quick Find https://culturedcode.com/things/support/articles/2803584/ (F), Calendar https://culturedcode.com/things/support/articles/2803583/ (C), Cloud https://culturedcode.com/things/support/articles/2803590/ (S), Import https://culturedcode.com/things/support/articles/2803555/ (I), shortcuts https://culturedcode.com/things/support/articles/2785159/ (K).

| Dialog | Purpose | Fields and options | Buttons and shortcuts | Cancel | Source |
|--------|---------|--------------------|-----------------------|--------|--------|
| Quick Entry | Capture a to-do without leaving the current app; on by default | Title and details; the usual keys for list, tag and start date work inside it, the mouse too | Save, or `Cmd+Return`, saves and closes; opens with `Ctrl+Space` (changeable in Settings > Quick Entry) | `Esc` closes and drops the input | Q |
| Quick Entry with Autofill | Like Quick Entry, and puts a link to the current web page, mail or file in the notes (for Mail, Safari, Finder) | As Quick Entry; can file the to-do under a heading | `Ctrl+Opt+Space`; switched on in Settings > Quick Entry ("Enable shortcut for Quick Entry with Autofill"), then a helper app is installed | `Esc` | Q |
| Quick Entry popover of Magic Plus | After a to-do is dropped on the Inbox target (iPhone/iPad gesture) it is saved and a popover offers to file it elsewhere | Button "Inbox" to pick another list | Other buttons `[nicht belegt]` | `[nicht belegt]` | G |
| Error: Things not responding (Autofill) | Shown when Autofill hangs | none | OK, then restart the Mac | | Q |
| Repeat | Make a repeating to-do or project, or set the schedule of an existing one | Pattern "After completion", or daily / weekly / monthly / yearly; days to pick for week, month, year; checkbox "Add deadlines" with "days earlier"; a reminder time; end date `[nicht belegt]` | OK; opened by File > New Repeating To-Do or Items > Repeat; `Shift+Cmd+R` | `[nicht belegt]` | R, K |
| Repeat (iPhone/iPad) | Same, other controls | "After Completion" or "Regularly" with "Every"; days under "On" | Back, Save | `[nicht belegt]` | R |
| When (start date) | Say from when work on the item starts (not an appointment with a duration) | Calendar grid; quick choices | Today, This Evening, Someday, Clear (back to Anytime); `Cmd+S` opens it | `[nicht belegt]` | W |
| Deadline | Say by when the item must be done | Date choice as for When; the list "Deadlines" shows all | Flag button in the item; Clear removes it; `Shift+Cmd+D` | `[nicht belegt]` | W |
| Tags window (Mac) | Create, delete, rename, sort and group tags; give a tag a key | A shortcut box right of each tag; a tag group | Window > Tags, `Ctrl+Cmd+T`; `Shift+Cmd+T` edits tags of the selected item | `[nicht belegt]` | T |
| Tags popover (iPhone/iPad) | Same as the window | "New Tag", group option | Manage Tags, Save, Done | `[nicht belegt]` | T |
| Quick Find | Find lists, projects, areas, tags and to-dos and go there | Entry field with suggestions while typing; names first, "Continue Search" widens to notes, checklists, logbook; special lists Tomorrow, Deadlines, Repeating, All Projects, Logged Projects | Opens by typing or `Cmd+F` | Arrow keys and `Esc` `[nicht belegt]` | F |
| Navigation popover | Jump to a list or area while the sidebar is hidden | List of all lists | `Shift+Cmd+O`; `Cmd+1` to `Cmd+6` jump straight | `[nicht belegt]` | K |
| Settings: Quick Entry | Set the Quick Entry keys | Shortcut field (click, press keys); Autofill option; since macOS 15.2 a shortcut needs Shift | | `[nicht belegt]` | Q |
| Settings: Calendar Events | Show calendar events in Today and Upcoming | Master checkbox "Show Calendar Events in Today and Upcoming lists", one checkbox per calendar | Things > Settings > Calendar Events | `[nicht belegt]` | C |
| Settings: Things Cloud | Switch sync on or off, log in again | Switch "Things Cloud" | "Log back in" | `[nicht belegt]` | S |
| Merge question after logging in again | Decide what happens to the to-dos | none read | "Keep all to-dos (recommended)" | `[nicht belegt]` | S |
| Import | Bring tasks from other apps | Direct importers: Apple Reminders, Todoist, OmniFocus; others via Apple Reminders, paste, text script | Steps `[nicht belegt]` (sub-articles not read) | | I |
| Move dialog (to a list) | Move an item to another list | `[nicht belegt]` | `Shift+Cmd+M` | `[nicht belegt]` | K |
| Project / area / checklist / reminder dialogs | Create them | `[nicht belegt]` (only the shortcuts `Opt+Cmd+N`, `Shift+Cmd+C` are listed) | | | K |
| Trash, general Settings tabs, undo | | `[nicht belegt]` | | | |
