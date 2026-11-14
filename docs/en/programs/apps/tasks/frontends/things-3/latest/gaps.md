# Things 3 — Gaps of our program

> [Things 3](../index.md) · [workflows](workflows.md) · [acceptance](acceptance.md)

Our program `fs-tasks`: state read from the local worktree on 2026-11-14 (`DESIGN.md` and `crates/fs-tasks-app`, version 0.0.7 in progress; the Things-style frontend is the **Day list**). `[nicht belegt]` = not checked in code.

| Workflow | Our state | Gap |
|----------|-----------|-----|
| T1/T2 quick capture | "+" at the bottom of a list: type, Enter; quick add in Today gives 17:00 | No capture popover from outside the window, no global key, no Autofill link |
| T3 Magic Plus | None | Missing |
| T4 start date | Lists are derived from readiness and due date; no When dialog | No dialog, no This Evening list, no Clear |
| T5 deadline | Due date is the one date; a due time is needed | No separate deadline, no Deadlines list |
| T6/T7 repeat | Repeating tasks listed as `Unsupported` in the classic frontend; series sheet explains | No Repeat dialog |
| T8 tags | Labels shown as the project list at the left; no tag window or tag keys | No Tags window, no filter by several tags |
| T9 Quick Find | A search bar is "not built" | Missing |
| T10 move | "Move to" panel on the board; Day list moves by tick | No Move dialog, no key moves in the Day list |
| T11 complete, log | Round box: tick completes, again reopens; Logbook list | No cancel, no "move completed to Logbook" key |
| T12 calendar, sync | None in the window | Missing |
| Menus | Day list shows only the menu **Frontend** | The Things menu bar (File, Items, View, Window) has no counterpart |
| Shortcuts | None for the Day list `[nicht belegt]` | All of [shortcuts](shortcuts.md) |
