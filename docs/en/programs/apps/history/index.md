# History

`FreeSynergy.History` (`fs-history`) answers: **what have I, or we, done?** It shows your own data as a timeline, whether
for one person or for a project. This is what was first called `fs-timeline`.

**Status: planned, no code yet (2026-11-06).** See the [overall plan](../roadmap.md).

## Idea

An **observer** of what happens. Every program already keeps an activity log (ADR 0020), and `fs-history` listens:

- **Personal:** what did I do last week, across every program? A diary (`fs-diary`) is then simply this, filtered to myself:
  a frontend with a built-in filter. Text written there is a wiki entry like any other (ADR 0031).
- **Project:** what happened, when and by whom? A project report need not be written from memory.
- **Telemetry as an import:** technical events can come in too, using a standard such as OpenTelemetry (candidate, not
  yet read). They stay **local unless you choose otherwise**: telemetry elsewhere means sending data away, and here it does not.

## Open questions

1. **Does it have its own data?** As an observer it mainly reads other programs' logs. If so, it might be a workbench and not a program.
2. **Privacy:** personal history shows everything I did. It must stay mine unless I share it, and a group's view must
   not show more than I agreed to. This needs care.
3. **Time tracking:** can it be derived from history, so nobody has to fill in a form?
4. **Which entries matter?** A log contains too much. How do we show what is meaningful?
