# How to help

FreeSynergy is built in the open and we are at the beginning, so fresh eyes help a lot. You do not need to write code.

## Read and tell us where you disagree

Read the [manifesto](../manifesto.md) and the [overall plan](../programs/apps/roadmap.md). If something looks wrong, unclear or missing, that is useful for us to know.

## Try things and report problems

Install the [Store](install.md) and a program, and open an **issue** in that program's repository on GitHub (<https://github.com/FreeSynergy>) when something is unclear or broken. Say what you did, what you expected, what happened. Every program says honestly what works and what does not; a bug is something it claims to do and does not.

## Review

Every repository has a `DESIGN.md` with a state table and a list of open points. Read one, and tell us what does not add up. We would rather hear it now.

## Build

Our stack is Rust, with a pure-Rust interface toolkit (Blinc). Pick a program, read its `DESIGN.md`, and start with something it lists as not built yet. The rules are short and apply to every change:

1. **Pattern first.** Choose a design pattern from the [coding conventions](https://github.com/FreeSynergy/fs-documentation/blob/main/conventions/coding.md) and justify it in one sentence. If none fits, do not invent one: ask.
2. **Then the trait.** Write the interface first, without an implementation, to match the contract in `fs-interfaces`. Between programs we always speak through [interfaces](../interfaces/index.md), never through another program's core.
3. **Then tests against the trait,** and only then the implementation.
4. Say what is missing, openly: what is not built answers `Unsupported` and is written in the `DESIGN.md`. No dummies, no tests that only test dummies.

## Rules that never bend

- **Nothing is copied.** We analyse what programs do, by function, and build it ourselves. Where an open standard exists we use it; where none exists we write one.
- **One standard, one owning program.** No second model of the same thing.
- **Free for everyone.** No paywall, no premium, no advertising.
- **Licence:** everything is `MIT OR Apache-2.0`.

## Improve this documentation

Every page has an edit button. The source language is English (`docs/en/`); German is translated from it. Open a pull request in [fs-documentation](https://github.com/FreeSynergy/fs-documentation). The decisions behind all of this are public: [Decisions](../decisions/index.md).
