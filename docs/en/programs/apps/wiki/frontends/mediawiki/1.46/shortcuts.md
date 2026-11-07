# MediaWiki 1.46 — Keyboard shortcuts

Version: 1.46.2. Sources:
- Access-key table: https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts (its own notice says that the section part of the page is outdated, so rows that depend on sections are not used here).
- Modifier logic: https://raw.githubusercontent.com/wikimedia/mediawiki/REL1_46/resources/src/mediawiki.util/jquery.accessKeyLabel.js
- VisualEditor keys: https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts
- CodeMirror: https://www.mediawiki.org/wiki/Extension:CodeMirror (it has a keyboard shortcut help dialog; its key list was not read)

## Core rule: access keys

MediaWiki does not use Ctrl+letter for page actions. Each action has one letter, the access key. The browser adds a modifier. The access key letter is the same on every system; the modifier depends on browser and OS.

## Modifier by browser and OS (from jquery.accessKeyLabel.js)

| Browser | Windows / Linux / ChromeOS | macOS |
|---------|------------------------------|-------|
| Firefox | Alt+Shift (Windows and Linux) | Ctrl+Option (Firefox 14+) |
| Chrome / Chromium | Alt (Windows and ChromeOS); Alt+Shift on Linux | Ctrl+Option |
| Safari | Alt (fallback) | Ctrl+Option |
| Other | Alt | Ctrl+Option or Ctrl |

Source: `accessKeyModifiers` branches in `jquery.accessKeyLabel.js` (lines 38 to 78 in the REL1_46 file). The page https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts gives the same Firefox and Safari examples. The code is authoritative; the Chrome row is a summary of several branches, so test before relying on it.

## Access keys (core, from Help:Keyboard_shortcuts)

Letters are the page's values. Where two actions share a letter, the context decides.

| Key | Action | Context |
|-----|--------|---------|
| e | Edit this page | any page |
| h | View page history | any page |
| m | Move this page | any page (if allowed) |
| d | Delete this page | any page (if allowed) |
| u | Upload a file | any page |
| w | Watch this page / unwatch | any page (logged in); the edit form has a toggle with the same key |
| t | View the talk page | non-talk page |
| c | View the content page (subject namespace tab) | any namespace |
| r | Recent changes | any page |
| x | Random page | any page |
| z | Main page | any page |
| q | Special pages index | any page |
| f | Search (jumps to the search box) | any page; the Vector search input carries this access key |
| j | What links here | any page |
| k | Related changes | any page |
| l | My watchlist | logged in |
| y | My contributions | any page |
| n | My talk page | any page |
| . | My user page | logged in |
| o | Log in | not logged in |
| p | Printable version | any page |
| p | Preview (edit form) | edit form (same letter as printable version) |
| s | Save ("Publish changes") | edit form (on special pages also "save") |
| v | Show changes (diff) | edit form |
| i | Mark as minor edit | edit form |
| b | Edit summary field | edit form |
| = | Protect or unprotect | any page |
| + | New section | talk page |
| . (for IP) | IP user page | not logged in |

Keys on special pages (block, export, import, upload, user rights, watchlist editing) also use `s` for "save" within their own form. Full list: https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts.

## Editor shortcuts (VisualEditor, extension)

Verified from https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts (page last edited 11 April 2026 per its own history; the page has no outdated notice). Windows and Linux first, Mac in the Mac column.

| Windows / Linux | Mac | Function |
|-----------------|-----|----------|
| Ctrl+B | Cmd+B | Bold |
| Ctrl+I | Cmd+I | Italic |
| Ctrl+K | Cmd+K | Insert link |
| Ctrl+Shift+K | Cmd+Shift+K | Insert citation (labelled "Cite") |
| Ctrl+Z | Cmd+Z | Undo |
| Ctrl+Shift+Z | Cmd+Shift+Z | Redo |
| Ctrl+Shift+V | Cmd+Shift+V | Paste as plain text |
| Ctrl+\ or Ctrl+M | Cmd+\ or Cmd+M | Clear formatting |
| Tab / Shift+Tab | same | Indent / outdent list |
| Alt+S | Ctrl+Option+S | Save ("Publish changes") |
| Ctrl+Shift+X | Cmd+Shift+X | Toggle writing direction (LTR/RTL) in the editor |
| Ctrl+D | Cmd+D | Add a template (in the template dialog) |
| Ctrl+Shift+D | Cmd+Shift+D | Add an undocumented parameter (template dialog) |

The VisualEditor page lists more keys for the template dialog. Only the common ones are shown.

## Wikitext source editor

| Shortcut | Status |
|----------|--------|
| Ctrl+B, Ctrl+I, Ctrl+K in the plain editor | unverified; the existing page's list is not confirmed |
| CodeMirror help dialog | exists (extension); key list not read |
| WikiEditor toolbar keys | not read; https://www.mediawiki.org/wiki/Help:WikiEditor returned HTTP 404 in this run |

Do not copy any source-editor shortcut from the existing page until it is verified.

## Vector 2022 specific keys

No `keydown` handler was found in the Vector 2022 JavaScript sources (searched `resources/skins.vector.js` and `resources/skins.vector.search`, REL1_46). Vector therefore adds no key bindings of its own beyond the access keys in the table above. This is a search of the files read in this run, not a full audit.

## Notes for our frontend

- Use access keys if we want MediaWiki-like keys. Mac and Windows differ, so the frontend should show the correct key label per platform (the logic in `jquery.accessKeyLabel.js` shows how).
- Keys that collide with browser shortcuts (for example Alt+E, Alt+D, Alt+F in Chromium) are the reason for the Alt+Shift fallback in Firefox and Chrome on Linux (see the comments in `jquery.accessKeyLabel.js`).
- Our own shortcut list is designed separately. Do not reuse the existing page's Ctrl+Shift list.
