# Jira - Gaps of our program

> [Jira](../index.md) · [workflows](workflows.md) · [acceptance](acceptance.md)

Our program `fs-tasks`: state read from the local worktree on 2026-11-14 (`DESIGN.md`, `crates/fs-tasks-app`, version 0.0.7 in progress); the Jira-style frontend is the **Board** frontend. `[nicht belegt]` = not checked in code.

| Workflow | Our state | Gap |
|----------|-----------|-----|
| J1 create | "+ Create" at the end of a column: an entry line, Enter makes the task in that column; form of the classic frontend with Save | No create dialog, no Create-another, no work types, no full form |
| J2 status | Panel "Move to" edits the task's status; the classic view moves a card by keyboard or buttons | No drag by mouse, no workflow with conditions, no transition message |
| J3 clone | None | Missing |
| J4-J6 sprints | None; Calendar and Timeline are drawn locked | No sprints, no backlog tab, no start/complete/delete |
| J7 bulk | None | Missing |
| J8 columns | Columns are the five values of the progress; limits only reported | No own boards, no column editing, no limits |
| J9 swimlanes | None | Missing |
| Menus | Board shows only the menu **Frontend** | The sidebar, space navigation and context menus of the inventory |
| Shortcuts | `[nicht belegt]` for the Board frontend | All of [shortcuts](shortcuts.md) |
