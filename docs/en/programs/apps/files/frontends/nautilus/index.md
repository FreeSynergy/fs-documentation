# Nautilus (GNOME Files)

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

The file manager of the GNOME desktop. Few options, many tasks done in one window. ⚠️ (project facts not read on the pages below.)

## Notable ideas

- **Same window for network shares:** "Browsing files on servers or network shares" is a normal task in the help ✅. WebDAV works with `dav://` and `davs://` ✅ (Nextcloud manual).
- **Rename keeps the extension:** only the part before the last period is selected ✅.
- **Delete is undoable for a few seconds**, with a permanent delete that asks (Shift+Delete) ✅.
- **Rename music files from their embedded data** ✅ (named in the help index).
- **Sort folders before files** as an option, off by default ✅.

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| Browse, copy, move, delete, preview without opening | ✅ | Help index |
| Rename one, many; undo (Ctrl+Z); F2 | ✅ | |
| Trash, restore, empty, permanent delete with confirmation | ✅ | |
| Search by name and type; sort by name, size, type, time | ✅ | Help index |
| Type a path in the location bar; bookmarks | ✅ | Help index |
| Properties, permissions, default apps | ✅ | Help index |
| Purge interval for trash and temporary files | ✅ | Help index |
| Share by e-mail; file history can be limited or turned off | ✅ | Help index |
| Select by name pattern; hide files; templates | ✅ | Help index |
| Tabs, list and grid view | ⚠️ | Not found on the pages read |

## Name rules

✅ https://help.gnome.org/users/gnome-help/stable/files-rename.html
- Two items cannot share a name in one folder; the rename is blocked.
- Names are case-sensitive; `File.txt` and `FILE.txt` differ, but this is discouraged.
- Only `/` is forbidden. Avoid `| \ ? * < " : >` because other file systems restrict them.
- A leading period hides the file.
- Some file systems limit names to 255 characters.

This is the closest match to ADR 0055: the file system sets the rules, the program warns.

## What we take

Rename that blocks collisions with a clear message. A warning list for characters that break other systems. Purge interval for trash as a setting. File history that can be turned off (privacy).

## Sources (read 2026-11-06)

- https://help.gnome.org/users/gnome-help/stable/files.html
- https://help.gnome.org/users/gnome-help/stable/files-rename.html
- https://help.gnome.org/users/gnome-help/stable/files-delete.html
- https://help.gnome.org/users/gnome-help/stable/nautilus-views.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html (WebDAV in Nautilus)
