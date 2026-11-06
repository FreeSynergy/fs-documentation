# History

`FreeSynergy.History` (`fs-history`) answers: **what have I, or we, done?** It shows your own data as a timeline, whether
for one person or for a project. This is what was first called `fs-timeline`.

**Status: provisional draft interface, [core](https://github.com/FreeSynergy/fs-history) in progress (2026-11-06).** See the [overall plan](../roadmap.md).

## Idea

An **observer** of what happens. Every program already keeps an activity log (ADR 0020), and `fs-history` listens:

- **Personal:** what did I do last week, across every program? A diary (`fs-diary`) is then simply this, filtered to myself:
  a frontend with a built-in filter. Text written there is a wiki entry like any other (ADR 0031).
- **Project:** what happened, when and by whom? A project report need not be written from memory.
- **Telemetry as an import:** technical events can come in too, using a standard such as OpenTelemetry (candidate, not
  yet read). They stay **local unless you choose otherwise**: telemetry elsewhere means sending data away, and here it does not.

## Open questions

All answers are provisional. Details: [`DESIGN.md`](https://github.com/FreeSynergy/fs-history/blob/main/DESIGN.md).

1. **Does it have its own data?** No content of its own, but a derived local index, because the hub cannot search by time, person or
   project. So it stays a small program, not only a view.
2. **Privacy:** it stays local. There is no sharing and no group view until the sharing interface exists. Role assignments and survey
   answers are never read. `forget` removes an entry from this index only; the hub's log keeps it. Every delete blanks the name and context of
   that object's entries, because an object that became sensitive arrives as a plain delete and the two cases look the same.
3. **Time tracking:** not built.
4. **Which entries matter?** `digest` groups changes to one object by one program within a time window.

**Known limit:** the hub delivers the program as the actor and the receive time as the time. Until it passes on the originals, "person" means
the object's `attributedTo`, so "what I edited in someone else's object" cannot be answered.
