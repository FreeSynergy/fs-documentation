# History

`FreeSynergy.History` (`fs-history`) answers: **what have I, or we, done?** It shows your own data as a timeline, whether
for one person or for a project. This is what was first called `fs-timeline`.

**Status: planned, no code yet (2026-11-06).** See the [overall plan](../roadmap.md).

## Idea

Every program already keeps an activity log (ADR 0020), so the data is there. `fs-history` brings it together:

- **Personal:** what did I do last week, across every program?
- **Project:** what happened, when and by whom? A project report need not be written from memory.
- **Bookmarks in time:** a person can add their own entries, such as a diary.

## Open questions

1. **Does it have its own data?** It mainly reads other programs' logs. Its own data would be diary entries and notes.
   If that turns out to be all, it might be a workbench and not a program.
2. **Privacy:** personal history shows everything I did. It must stay mine unless I share it, and a group's view must
   not show more than I agreed to. This needs care.
3. **Time tracking:** can it be derived from history, so nobody has to fill in a form?
4. **Which entries matter?** A log contains too much. How do we show what is meaningful?
