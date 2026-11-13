# Windows Explorer 11 — Acceptance checklist

> [Windows Explorer](../index.md) · [workflows](workflows.md) · [gaps](gaps.md)

Derived from [workflows](workflows.md). Click through in the frontend under test; answer yes or no. A frontend "in this style" passes when every applicable line is **yes**. W6 is not applicable to this style.

| # | Workflow | Test | yes / no |
|---|----------|------|----------|
| A1 | W1 | Open: start page shows pinned and recent folders; Home folder, root, every drive and mounted USB stick and a network location can be opened | ☐ |
| A2 | W2 | Open a folder, go back, forward, up; click a path segment; type a path and open it; a wrong path shows an error | ☐ |
| A3 | W3 | Select one, several (Ctrl), a range (Shift), all; with and without check boxes | ☐ |
| A4 | W4 | Copy and move via clipboard into another folder; the source stays (copy) or disappears (move) | ☐ |
| A5 | W5 | Drag to a folder: no key moves or copies by rule; with modifier the other; shortcut with the third | ☐ |
| A6 | W7 | Paste a name that exists: a dialog offers replace / skip / decide each; "for all" is possible; nothing is overwritten silently | ☐ |
| A7 | W8 | A large copy shows progress; it can be cancelled; what was copied stays | ☐ |
| A8 | W9 | Rename with F2; Esc cancels; a forbidden or taken name is refused with a message | ☐ |
| A9 | W10 | Rename several selected items with a common base name | ☐ |
| A10 | W11 | Delete moves to the bin; permanent delete asks and cannot be undone | ☐ |
| A11 | W12 | Restore from the bin to the old place; empty the bin after confirmation | ☐ |
| A12 | W13 | Undo and redo of the last copy, move, rename, delete | ☐ |
| A13 | W14 | New folder and new file appear with their name ready to edit | ☐ |
| A14 | W15 | Properties show type, place, size, dates | ☐ |
| A15 | W16 | Search by name in the current folder; from Home across everything | ☐ |
| A16 | W17 | Sort by name/date/size/type, reverse; group | ☐ |
| A17 | W18 | Switch icons / list / details / compact; icon size changes | ☐ |
| A18 | W19 | Open, switch, close tabs by keyboard; the last tab closes the window | ☐ |
| A19 | W20 | Open with the default program; choose another program | ☐ |
| A20 | W21 | Make a ZIP from a selection; open and extract it | ☐ |
| A21 | states | Empty folder, loading, error, selection, offline each show something sensible ([states](states.md)) | ☐ |
| A22 | shortcuts | Every key of [shortcuts](shortcuts.md) does what it says | ☐ |
