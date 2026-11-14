# KDE Discover — Gaps of our program

> [KDE Discover](../index.md) · [workflows](workflows.md) · [acceptance](acceptance.md)

Our program `fs-store`: state read from the code of the local store work tree on 2026-11-14 (`crates/fs-store-app`: menu model, words, views). `[nicht belegt]` = not checked in code.

| Workflow | Our state | Gap |
|----------|-----------|-----|
| W1 search | Search field in the filter row of the card page; filters All, Installed, Updates, Not installed; sort by name, newest, size; kinds in the navigation (programs, frontends, components, themes, servers, icon sets) | Search is not scoped by a category list like Discover's; add-on categories of a desktop do not apply |
| W2 install | Install and Update buttons; one preview question with a confirming button ("Install now") and a note that the system asks for the password | Source choice per program (several sources for one program): `[nicht belegt]` |
| W3 uninstall | "Uninstall" in the more menu of a card, one question "Uninstall {name}? Your data stays." with Uninstall and Cancel | Separate Installed view exists as a filter tab, not as a list with its own remove button `[nicht belegt]` |
| W4 update | Updates tab, "Update all (n)", per-program automatic updates, jobs list | No hold-back check box per row in an update list `[nicht belegt]` |
| W5 check by hand | Settings page: "Look now", interval (off, at start, daily, hourly), timer | Equal or better |
| W6 sources | Sources page: add by Git address, switch on and off, remove, refresh | No "make default source per program"; no advanced external tool |
| W7 bug report | None found | Missing |
| Keys | Ctrl+Q quit, F1 help page of the current view, Escape closes the open detail | No Ctrl+F focus on the search field, no Alt+Left/Right `[nicht belegt]` |
