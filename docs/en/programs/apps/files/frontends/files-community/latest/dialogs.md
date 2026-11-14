# Files — Dialogs

> [Files](../index.md) · [description](description.md)

| Dialog | Purpose | Fields | Buttons | Default | Cancel | Mark |
|--------|---------|--------|---------|---------|--------|------|
| Delete confirmation | Ask before deleting (always / only permanent / never) | Item names | Confirm, Cancel | `[nicht belegt]` | Nothing deleted | ✅ exists, content `[nicht belegt]` |
| Extension change warning | Ask before changing an extension | | Yes, No | `[nicht belegt]` | Old name stays | ✅ exists |
| Conflict (replace / skip / keep both) | Name clash while copying or moving | File info | Replace, Skip, Keep both, "for all" | `[nicht belegt]` | | `[nicht belegt]` |
| Operation progress | Show running copy/move/delete | Bar, speed | Cancel, pause | | | `[nicht belegt]` |
| FTP/FTPS credentials | Log in to a server | User name, password | | | | ✅ prompt exists, fields not detailed |
| Customize toolbar | Choose buttons | Action list left, toolbar list right, labels toggle, mode drop-down | | | | ✅ |
| Restore default key bindings | Reset shortcuts | | Confirm | | | ✅ "with a confirmation prompt" |
| Settings (General, Appearance, Files & folders, Actions, Advanced) | Options | See [features](features.md) | | | | ✅ |
| Add/edit key binding | Bind keys to an action | Action, keys | | | | ✅ (editing described, form `[nicht belegt]`) |
| Properties | Item facts (Alt+Enter ✅) | | | | | content `[nicht belegt]` |
| Alias editor | Short names for folders | Alias (no `\` or `/`), folder | Add, edit, delete, restore defaults | | | ✅ |
| Tag editor | Create a tag | Name, colour | | | | ✅ |
| Extract / compress | Archive operations | | | | | `[nicht belegt]` |
| Open with | | | | | | `[nicht belegt]` |
| Settings | Configure the app | Pages General, Appearance, Files and folders, Actions, Advanced (the Appearance page was not opened) | Actions page: Edit, Delete, Add command, Restore defaults, Save, Yes (confirm reset) | | | ✅ (files.community/docs/customize-settings, 2026-11-14) |
| Delete confirmation setting | When to ask | Always / only for permanent delete / never | | | | ✅ setting; dialog text and buttons `[nicht belegt]` |
| Command Palette | Run any action | Search list of actions with their keys | | | | ✅ (files.community/docs/features/command-palette) |
