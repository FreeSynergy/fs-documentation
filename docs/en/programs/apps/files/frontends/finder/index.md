# Finder

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

The file manager of macOS. Part of the system; Spotlight and iCloud Drive sit beside it.

## Notable ideas

- **Tags as colours and names**, several per item, searchable, in the sidebar, usable to group and sort ✅. Control-1..7 toggle favourite tags, Control-0 clears ✅.
- **Smart Folders:** a folder that collects items by criteria you set ✅. Same idea as our "album as saved search".
- **Quick Look (Space):** full preview of most files, markup, trimming audio and video, slideshow, index sheet ✅.
- **Aliases:** a shortcut file that can sit anywhere ✅.
- **Gallery view** and a **Preview pane** ✅.
- **Custom icons** per folder: colour, symbol, emoji ✅.
- **Folders first when sorting** is an option ✅.

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| Sidebar, customisable | ✅ | |
| Display modes incl. Gallery | ✅ | Only Gallery is named on the page read; icons, list, columns ⚠️ |
| Sort and group by name, date last opened, tag | ✅ | |
| Tags | ✅ | |
| Smart Folders | ✅ | |
| Aliases | ✅ | |
| Quick Look | ✅ | |
| AirDrop, iCloud Drive, devices in the sidebar | ✅ | Named as related topics |
| Trash with Put Back, auto-empty | ⚠️ | The page fetched did not cover it |

## Name rules

⚠️ Not found on the pages read. rclone's mount page says macOS is case-insensitive but case-preserving and advises keeping Unicode normalisation on ✅ (https://rclone.org/commands/rclone_mount/).

## What we take

Tags and smart folders as one mechanism (`file.tag`, saved search). A quick preview on Space that does not open the app (`file.preview`). Aliases are the case for a file in several places; the contract has one folder per file.

## Sources (read 2026-11-06)

- https://support.apple.com/guide/mac-help/organize-files-in-folders-mchlp2605/mac
- https://support.apple.com/guide/mac-help/use-quick-look-to-preview-files-mh14119/mac
- https://support.apple.com/guide/mac-help/tag-files-and-folders-mchlp15236/mac
- https://support.apple.com/guide/mac-help/change-the-way-you-view-files-and-folders-mchlp2605/mac
