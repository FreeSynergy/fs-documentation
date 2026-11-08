# History

## In short

History is a timeline of your own work, without anyone watching you. It notices what happens across your FreeSynergy programs and keeps a short line for each event, such as "edited this page" or "finished that task". It answers the question: what have I, or we, done?

**Command:** `fs-history`, one command per program with subcommands ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); programs are switched over when they are next touched, so not every one is yet).

## What is different here

- It keeps a summary, never the content. A diary text stays a wiki page, and History only points to it.
- The history is local to you. Sensitive things never arrive in it, and it never reads relationships or survey answers.
- Forgetting is real for the past: matching entries are removed, and a record keeps only salted hashes of what you forgot, so a forgotten project name is not stored in readable form.
- You can scroll the timeline, filter it, and collapse a busy hour into one line.
- History owns its interface, `history.capnp` in `fs-interfaces`. It is a draft and marked provisional.

## Where it stands today

Latest tag: `v0.1.1`. There is **no window and no server yet**.

Today there is a timeline of activities from other programs, newest first, with filters and paging. A digest groups runs of events on the same object. You can forget entries by filter, for the past only. It reads from the FreeSynergy hub through the adapter `fs-history-hub`, tested against a real hub. It has 49 tests and was checked by an independent reviewer over three rounds.

What is not there yet: who did something is empty for now, and the time is when the entry arrived, not necessarily when it happened. Forgetting covers this index only, not the hub's own log. There is no sharing and no group view, no import of telemetry and no time tracking. A hub connection that dies is not reconnected by itself.

`FreeSynergy.History` (`fs-history`) answers: **what have I, or we, done?** It shows your own data as a timeline, whether
for one person or for a project. This is what was first called `fs-timeline`.

**Status: [core](https://github.com/FreeSynergy/fs-history) v0.1.1, no GUI; provisional draft interface (2026-11-06).** See the [overall plan](../roadmap.md).

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

**Known limits:** a lost connection to the hub is not reconnected. The hub delivers the program as the actor and the receive time as the time. Until it passes on the originals, "person" means
the object's `attributedTo`, so "what I edited in someone else's object" cannot be answered.
