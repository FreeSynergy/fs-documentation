# Jira - Workflows

> [Jira](../index.md) · [dialogs](dialogs.md) · [shortcuts](shortcuts.md) · [acceptance](acceptance.md) · [gaps](gaps.md)

Format: goal, requirement, steps (user does X -> program shows Y), errors, undo. Platform: web, Jira Cloud (Software). Read from the official Atlassian help, pages under https://support.atlassian.com/jira-software-cloud/docs/ , on 2026-11-14 (summarising fetch); our own words (ADR 0013). `[nicht belegt]` = not on a page read. IDs J1..J9. "Space" is the help's word for what older text calls project.

## J1 Create a work item (create-a-work-item-and-a-subtask)
Requirement: `[nicht belegt]`.
1. Click the Create symbol in the navigation -> the Quick Create dialog opens.
2. Fill Title and the shown fields -> the description grows with the text.
3. Optionally tick "Create another" -> the dialog stays for the next item with the same space and work type.
4. Click "Create" -> the work item is made. Or expand to the full form with all fields.
Errors: `[nicht belegt]`. Undo: `[nicht belegt]`.

## J2 Change status (transition-an-issue)
Requirement: the transition is allowed in the workflow of the work type, and the user may do it.
1. Open the "Status" menu in the work item -> the allowed statuses show.
2. Choose one -> the status changes; if the transition has required fields, a dialog asks for them first.
3. Or drag the card to another board column -> the status follows; with several status sections in a column the section under the pointer counts. In a kanban backlog a parent drags with its subtasks; moving the last open subtask to Done asks whether the parent moves too.
Errors: a message at the lower left, "Unable to transition the work items to [status]. Check if all transition conditions are met." (admin rules: conditions, validators, post functions). A status visible on the board but not allowed for the work type fails. Missing permission: ask the Jira admin. Undo: `[nicht belegt]`.

## J3 Clone a work item (clone-an-issue)
Requirement: permission "Create work items" in the space.
1. More actions > Clone -> the clone dialog opens (title `[nicht belegt]`).
2. Edit "Summary" (prefixed "Clone"), "Assignee", "Reporter"; tick what to "Include".
3. Click "Clone" -> the copy appears, linked to the original.
Errors: `[nicht belegt]`. Undo: the link can be removed any time; deleting the clone as undo `[nicht belegt]`.

## J4 Start a sprint (plan-a-sprint)
1. Open the Backlog tab -> the sprints show.
2. Click "Start sprint" at the sprint -> the dialog proposes start and end dates.
3. Set "Sprint name", dates, optionally "Sprint goal"; click "Start" -> "Active sprints" opens.
After the start, adding or removing work items changes the scope and the burndown chart. Requirement and errors `[nicht belegt]` (several active sprints need parallel sprints). Undo `[nicht belegt]`.

## J5 Complete a sprint (complete-a-sprint)
Requirement: Jira administrator or permission "Manage Sprints"; open subtasks keep the parent from finishing cleanly (the parent is moved).
1. Open "Active sprints" in the space; with several active sprints pick one in the drop-down -> "Complete Sprint" shows.
2. Click "Complete Sprint" -> done items (those in the last column) leave "Active sprints".
3. For open items choose "Backlog", "Any future sprint" or "New sprint" -> the items go there.
Errors: a sprint shared by several boards moves only the finishing board's open items into future or new sprints; the others go to the backlog. Undo: `[nicht belegt]` (an article "Reopen a sprint" exists, not read).

## J6 Delete a sprint (delete-a-sprint)
1. Backlog tab > More actions at the sprint > "Delete sprint" -> confirmation wording `[nicht belegt]`.
2. Result: the work items move to the next sprint in the list; if the sprint was active they keep their status there. Completed sprints follow another article. Errors and undo `[nicht belegt]`.

## J7 Bulk change and bulk delete (edit-multiple-issues..., delete-multiple-issues)
Requirement: permissions in the space; at most 1,000 items for delete, 50 for labels, assignee, priority, estimate.
1. Select items with checkboxes, `Ctrl`/`Cmd`-click or Shift -> the selection is marked.
2. Right-click or More actions > "Bulk change" -> the action list shows (flags, fields, move, archive, delete).
3. For delete: "Delete work items", "Next", optional e-mail choice, "Next", "Confirm", "Acknowledge".
Errors: an action missing from the menu means missing permission or a reached limit; adjust the count. Messages `[nicht belegt]`. Undo `[nicht belegt]`.

## J8 Configure board columns (configure-columns)
Requirement: space or board administrator; company-managed spaces.
1. More actions beside the board name > "Board settings" > Layout > "Columns" -> the mapping shows.
2. "Add" a column (name, category), rename by clicking the name and Enter, drag the head to move, "Delete".
3. Drag a status from "Unmapped statuses" into a column to map it; back to unmap. Under "Column constraints" choose "Work item count" or "Work item count, excluding subtasks" and enter minimum and maximum; "None" clears.
Effects: deleting a column returns its statuses to "Unmapped statuses"; unmapped statuses hide their items on board and backlog; only the rightmost column counts as done. Missing items: check the board filter (Board settings > Details), the mapping, and the Backlog feature in the space settings. Undo `[nicht belegt]`.

## J9 Choose swimlanes (configure-swimlanes)
Requirement: space or board administrator.
1. More actions > "Board settings" > "Layout" > "Swimlanes" -> "Select method" shows.
2. Pick "Queries", "Stories", "Assignees", "Epics", "Spaces" or "No Swimlanes".
3. For "Queries": More actions on a query > "Edit" -> change the name or the JQL; drag the grip to reorder.
Notes: with queries the defaults are "Expedite" (priority = Blocker) and "Everything Else" (cannot be deleted); ORDER BY in the JQL is not used, order follows rank. Adding or deleting a swimlane, errors, undo: `[nicht belegt]`.
