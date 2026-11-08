# Edit

## What you see

After you press "Edit" the page turns into a text area with the Markdown text of the page. Above it are the buttons "Save" and "Cancel". If you left an edit earlier without saving, a notice says "A draft you did not save was backed up earlier." with the buttons "Restore" and "Discard".

## What you can do

To change a page:

1. Open the page and press "Edit".
2. Change the text.
3. Press "Save". The page shows your change and says "Saved." If nothing changed it says "Nothing was changed." The text is saved in the wiki. No file is written.

To give up:

1. Press "Cancel". If you changed something, it says "You have unsaved changes. Press Cancel again to discard them."
2. Press "Cancel" again to throw the changes away.

If someone else saved the page first:

1. Save reports the conflict and says your text is kept.
2. Press "Save" again to replace their version knowingly.

If the text area cannot hold something exactly, a note says "Saving will also change" and what.

To get a draft back:

1. Press "Edit" on the same page.
2. Press "Restore" to use the draft, or "Discard" to throw it away. If you had already typed something, Restore asks once more: "Restoring replaces what you typed. Press Restore again to do it."
3. Nothing is written until you press "Save". If the page changed since the draft, Save asks before it replaces the newer version.

Your draft is backed up about half a second after you stop typing, and at least every five seconds while you type.

## Keyboard

Ctrl+S saves. Esc is not used, so it can never throw a draft away.

## Not there yet

- Typing in the real window has not been verified by tests. The design notes list what to try by hand.
- No other editors, no templates in the program.
- The edit lock works inside one process. Two programs on the same store are not covered.
- The text area wraps narrower than its box.
