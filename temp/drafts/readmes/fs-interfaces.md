# FreeSynergy Interfaces — the contracts everything agrees on

**This is a building block. It is why you can swap one program for another and your data goes with you.**

FreeSynergy Interfaces holds the contract for each topic: messages, files, people, groups, tasks, events, places, texts and more. A contract says what any provider of that topic can do. Every provider offers all of it, or answers plainly "not possible". Anyone can implement a topic without our programs, and our programs can be replaced by yours.

What is different here: an interface is a target, not something that grows. It is published as a draft, tested by at least two independent users, then fixed as 1.0. After that it changes only by a clear jump to a new version, with old and new offered side by side. Where an open standard exists we follow it; where none exists we write one and offer it to everyone. Each standard has exactly one owning program, so there is one point of truth.

## What it can do today

Latest tag: `v0.44.0`.

- Cap'n Proto schemas for: common types, tasks, messenger, hub, people, groups, files, events, places and texts, and, according to the design file, surveys, history, resources, whiteboard and streaming. The README table lists the first ten; the DESIGN file has the full list.
- The Rust code generated from them is committed, so a normal build needs no schema compiler.
- A shared provider rule: `Unsupported` and `Capabilities` for "what can you do?" and "this is not possible".
- Shared server and client code for local sockets (feature `rpc`): errors in the RFC 9457 form, paging, change feeds.
- Every generated file is checked to be identical to what the official Cap'n Proto compiler produces.
- `fs-mcp`: a first stage that lists, from the contracts, the tools an AI could be offered, with risk classes. It has no server and runs nothing.

## What is not there yet

- No interface is 1.0. All are drafts; most have no second independent user yet.
- Several (files, history, resources, surveys, whiteboard, streaming) are marked provisional because no frontends have been analysed.
- The usage example in the README names an old tag; use the latest.

## Part of FreeSynergy

Interfaces is the common language of the programs. FreeSynergy is a family of programs that are free for everyone, forever, and that keep your data yours. The documentation, the manifesto and the overall plan live in [fs-documentation](https://github.com/FreeSynergy/fs-documentation); the reading version is at <https://freesynergy.github.io/fs-documentation/>. Start with the [manifesto](https://freesynergy.github.io/fs-documentation/en/manifesto/) if you want to know why we do this.


## For developers

- Workspace crates: `fs-interfaces` (generated code and the provider rule), `regenerate` (rebuilds the generated code with our own compiler [fs-capnpc](https://github.com/FreeSynergy/fs-capnpc)), `fs-mcp`.
- Each schema in `schema/` starts with a header naming status, owner and consumers. Never renumber or remove a field; only append.
- Use it by git tag: `fs-interfaces = { git = "https://github.com/FreeSynergy/fs-interfaces", tag = "v0.44.0" }`.
- After a schema change: `cargo run -p regenerate` and `cargo test -p fs-interfaces`. No C++ toolchain needed.
- Design and the full state table: [DESIGN.md](DESIGN.md).
- Licence: MIT OR Apache-2.0.
