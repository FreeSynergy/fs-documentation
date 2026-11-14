# Windows Explorer 11 — Dialogs

> [Windows Explorer](../index.md) · [description](description.md)

The official page names **no dialog**. All below is `[nicht belegt]`: known from the product, to be verified on Windows.

| Dialog | Purpose | Fields / content | Buttons | Default | Cancel behaviour |
|--------|---------|------------------|---------|---------|------------------|
| Copy / move progress | Show a running transfer | Source, target, progress bar, speed, time left, chart in "more details" | Pause, Cancel | none | Cancel stops; already copied files stay |
| Replace or skip files | Name clash at the target | Source and target info (size, date), the file name | Replace the file in the destination / Skip this file / Let me decide for each file | first (replace) | Closing the dialog cancels the operation |
| File name clash, same folder | Pasting into the folder of origin | Offers a copy with a numbered name | Automatic | | |
| Confirm delete | Before deleting to the Recycle Bin or permanently | Item name, "permanently delete" wording | Yes / No | Yes | No leaves everything |
| File in use | A program holds the file | Name, program hint | Try again / Cancel / Skip | Try again | Cancel stops |
| Access denied | No right | Message, "continue" | Continue (admin) / Skip / Cancel | | |
| Rename extension warning | Extension changed | Warning text | Yes / No | | No keeps the old name |
| Invalid name | Forbidden character typed | Lists forbidden characters (see index) | OK | OK | Name stays in edit |
| Properties | Item facts | Tabs: General (type, location, size, dates, attributes), Security, Details, Previous versions | OK / Cancel / Apply | OK | Cancel discards edits |
| Open with | Choose a program | Program list, "always use" box | OK | OK | Cancel |
| Folder options | Start page, extensions, hidden items ✅ | Check boxes, drop-down | OK / Cancel / Apply | OK | Cancel discards |
| Compress to ZIP | Name the archive | Inline: name edit field | — | | |
| Share | Share targets | Targets list (✅ button exists) | | | |

Properties opens with Alt+Enter ✅; Options as described in [menus](menus.md) ✅.

## Additions from opened Microsoft support pages (2026-11-14)

| Dialog | Purpose | Fields / content | Buttons | Mark |
|--------|---------|------------------|---------|------|
| Folder options | Behaviour of the Explorer | "Open File Explorer to" (This PC or Home); on the View tab: hide extensions of known types, show hidden files, use check boxes to select; reached via See more > Options | Apply, OK | ✅ (page file-explorer-in-windows, set-file-explorer-to-open-to-this-pc) |
| Previous versions | Restore an older state of a folder or drive | List of versions | Open (also in File History), Restore, Restore to…; restoring replaces the current version and cannot be undone | ✅ (page backup-and-restore-with-file-history) |
| Open with | Choose a program | Choose another app | Always, Just once | ✅ (page use-a-screen-reader…) |
| Sensitivity label (Purview) | Label a file | Apply, Close | Apply, Close | ✅ (page label-and-protect-files…) |
| Customize menu | Pick context-menu entries (preview) | Switches for Send to, Create shortcut, Print, text labels | | ✅ (Windows 11 preview update notes, 2026-10) |
| Delete confirmation | Before deleting | Only a setting named; dialog text and buttons not described | | `[nicht belegt]` |
