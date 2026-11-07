# FreeSynergy — software that belongs to you

**Free for everyone, forever. Your data stays yours. Programs that work alone and work together.**

You are tired of apps that want your money, your data or your attention. Of a calendar that does not talk to your tasks. Of messages scattered over five programs. Of a subscription that ends and takes your work with it.

FreeSynergy is built differently, from the ground up. It is a family of programs for everyday work together: contacts, calendar, tasks, files, texts, messages, polls, and more. We are building it in the open, and we are at the beginning. Please read the status column below before you get excited.

## Why

- **Free, with no paywall, ever.** No premium, no ads, not today and not later. Someone with little money gets the same software as a company.
- **Your data stays with you.** You work on your own copy, and it is kept for you. Saving is not exporting: only an export produces a file you hand on. Nothing leaves your machine unless you say so.
- **One engine, many faces.** A message is a message, whichever program brought it. Under each program sits one engine, and on top of it sit frontends from very simple to complete. You pick one and can switch; your data goes with you.
- **Everything speaks to everything.** Each program runs alone. Together they share the work, through open interfaces.
- **Alone first, together later.** A diary, a list, a project can start with you and become shared. You do not decide up front.
- **People first, AIs welcome but marked.** An AI takes part as a participant, never as a hidden listener. It is marked, and it does not act without your release.
- **Open to the last block.** Where an open standard exists we use it. Where none exists we write one and give it away.

Why we do this is written down in the [manifesto](https://freesynergy.github.io/fs-documentation/en/manifesto/).

## The programs

Status is as of 2026-11-07 and kept honest. "Core" means the engine works and is tested, but there is nothing to click yet. "First window" means a provisional window exists. Tags are the latest on GitHub.

| Program | Purpose | Repo | Status |
|---------|---------|------|--------|
| People | know who someone is | [fs-people](https://github.com/FreeSynergy/fs-people) | Core and a first window, `v0.5.0` |
| Calendar | be somewhere at some time | [fs-calendar](https://github.com/FreeSynergy/fs-calendar) | Core and a first window, `v0.6.0` |
| Tasks | know what to do next | [fs-tasks](https://github.com/FreeSynergy/fs-tasks) | Core and a first window (list and status view, no real boards), `v0.7.0` |
| Files | keep and find anything | [fs-files](https://github.com/FreeSynergy/fs-files) | Core and server, no window, `v0.5.0` |
| Maps | know where | [fs-maps](https://github.com/FreeSynergy/fs-maps) | Core (tiles, offline regions, places), no map drawing yet, `v0.1.1` |
| Wiki | write and know together | [fs-wiki](https://github.com/FreeSynergy/fs-wiki) | Core and a first reader window with editing, `v0.3.0` |
| Messenger | say something to someone | [fs-messenger](https://github.com/FreeSynergy/fs-messenger) | Core, AI guard and mail connector, no window, `v0.3.0` |
| Groups | belong together | [fs-groups](https://github.com/FreeSynergy/fs-groups) | Core, no window, `v0.1.1` |
| History | remember what I or we did | [fs-history](https://github.com/FreeSynergy/fs-history) | Core, no window, `v0.1.1` |
| Resources | know what we have and need | [fs-resources](https://github.com/FreeSynergy/fs-resources) | Core, no window, `v0.1.0` |
| Surveys | ask, and decide together | [fs-surveys](https://github.com/FreeSynergy/fs-surveys) | Core, no window, `v0.1.0` |
| Whiteboard | think visually | [fs-whiteboard](https://github.com/FreeSynergy/fs-whiteboard) | Core (stage 1), no window, `v0.1.0` |
| Streaming | show something, and bring it everywhere | [fs-streaming](https://github.com/FreeSynergy/fs-streaming) | Stage 1 (forward and record), tested on loopback only, `v0.1.0` |
| Store | install and keep everything up to date | not public yet (local repo `fs-launcher`) | Design and a small core, coming |

Building blocks, which matter because everything above stands on them:

| Block | Purpose | Repo | Status |
|-------|---------|------|--------|
| Objects | one place for what programs keep | [fs-objects](https://github.com/FreeSynergy/fs-objects) | Working, `v0.5.0` |
| Hub | let the programs find each other | [fs-hub](https://github.com/FreeSynergy/fs-hub) | Working on one device, Linux, `v0.3.1` |
| Identity | know who is allowed in | [fs-identity](https://github.com/FreeSynergy/fs-identity) | Only a Kanidm adapter for groups, no sign-in yet, `v0.1.1` |
| Interfaces | the contracts everything agrees on | [fs-interfaces](https://github.com/FreeSynergy/fs-interfaces) | All drafts, none 1.0, `v0.44.0` |
| JSCalendar | the same time for everyone | [fs-jscalendar](https://github.com/FreeSynergy/fs-jscalendar) | Library, `v0.1.3` |
| Components | one look, one feel | [fs-components](https://github.com/FreeSynergy/fs-components) | Working, partly provisional, `v0.3.0` |
| Capnpc | build the contracts with Rust alone | [fs-capnpc](https://github.com/FreeSynergy/fs-capnpc) | Working, `v0.1.1` |
| Release | one way to ship, free of charge | [fs-release](https://github.com/FreeSynergy/fs-release) | In use, first run green, no tag yet |

What we do not have yet, plainly: no program has a finished app for ordinary users, there is no sign-in, nothing syncs between devices, and every interface is still a draft. Messages and some data stay on the device they were made on until a key vault exists.

## How to try it

The store, FreeSynergy's own app for installing everything with one click and keeping it up to date, is **coming**. It is not available yet, and we will announce it here when it is.

Until then you can try things from source if you are comfortable with a terminal. You need a Rust toolchain on Linux.

- Each core has a small example, for instance `cargo run -p fs-messenger-core --example demo` or `cargo run -p fs-people-core --example demo`.
- People, Calendar, Tasks and Wiki have first windows (`fs-people-app`, `fs-calendar-app`, `fs-tasks-app`, `fs-wiki-app`); the DESIGN file in each repo lists the options and what to try.
- Streaming has `cargo run --example relay`, as described in its README.

Expect rough edges. These windows are provisional and say so.

## How to help

- **Read** the [manifesto](https://freesynergy.github.io/fs-documentation/en/manifesto/) and the [overall plan](https://freesynergy.github.io/fs-documentation/en/programs/apps/roadmap/). Tell us where you disagree. That is useful.
- **Try** a program from source and open an issue in its repository when something is unclear or broken.
- **Review.** Every repo has a DESIGN.md with a state table and open points. Fresh eyes find things.
- **Build.** Rust and a pure-Rust GUI (Blinc) are our stack. Pick a program, read its DESIGN.md, and start with what it lists as not built.
- **Say what is missing.** Ideas that are good and new are welcome, and we would rather support them than settle for the old and slow.

All the documentation lives in [fs-documentation](https://github.com/FreeSynergy/fs-documentation), with a reading version at <https://freesynergy.github.io/fs-documentation/>.

## Licence

Our code is MIT OR Apache-2.0.

> We do not only write software. We write a promise that others can take along.
