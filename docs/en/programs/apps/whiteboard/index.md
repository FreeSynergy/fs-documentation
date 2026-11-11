# Whiteboards

## In short

Whiteboard is an endless board for ideas. You put down pages, shapes, text, connectors and drawings, and several people can change the same board at the same time. It answers the question: how do we think together on one picture without getting in each other's way?

**Command:** `fs-whiteboard`, one command per program with subcommands ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); programs are switched over when they are next touched, so not every one is yet).

## What is different here

- Two people changing the same board are merged property by property. If you move a shape while someone else recolours it, both changes stay.
- The merge does not depend on the order in which changes arrive. Property tests check this.
- Your undo only undoes your own steps. It skips a property that someone else has changed since.
- A board can be exported as SVG.
- Whiteboard owns its interface, `whiteboard.capnp` in `fs-interfaces`. It is a draft and marked provisional.

## Where it stands today

Latest tag: `v0.0.1` (stage 1 of the design). There is **no window and no server yet**.

What works today is the core: boards, pages and every kind of element in the contract; merging of changes from two sides; undo for each editor; groups, copy, align, lock and reorder; a fast way to find what is in view; and export to SVG. PNG and PDF export answer "not possible". It has 104 tests with real stores and was checked by an independent reviewer over several rounds.

What is not there yet: nothing sends changes between devices, so the merge is not used anywhere. Live presence, sharing, libraries, templates and comments are planned, not built.

**Status: first core `v0.0.1` in [`fs-whiteboard`](https://github.com/FreeSynergy/fs-whiteboard), no window yet (stage 1).** See the [design](design.md), the [requirements](requirements.md) and the [roadmap](../roadmap.md).

## Overview

This section contains documentation for various whiteboard and collaboration tools.

## Available Systems

- **mural** - Visual collaboration platform
- **miro** - Online whiteboard for team collaboration
- **excalidraw** - Collaborative whiteboard
- **figma** - Interface design tool with whiteboard features
- **jamboard** - Google's digital whiteboard
- **leantime** - Open source project management with whiteboard
- **stormboard** - Collaborative brainstorming tool
- **whimsical** - Visual collaboration for teams
- **gitmind** - Mind mapping tool
- **mindmeister** - Online mind mapping

## What is a Whiteboard?

A whiteboard is a digital tool for visual collaboration and brainstorming. Whiteboards enable:

- Visual brainstorming and idea gathering
- Real-time collaborative work
- Mind mapping and concept development
- Create diagrams and flowcharts
- Use templates and pre-built layouts
- Remote work support

## Application Areas

- **Brainstorming**: Gather and develop ideas
- **Product Planning**: Plan product features
- **Project Management**: Visualize tasks and processes
- **Workshops**: Workshops and retrospectives
- **Team Meetings**: Visual collaboration in teams
- **Education**: Education and teaching

## Benefits of Whiteboards

- **Visual clarity**: Visualize complex concepts
- **Collaboration**: Real-time collaboration
- **Flexibility**: Unlimited customization and editing
- **Remote work**: Ideal for remote teams
- **Templates**: Pre-built templates
- **Integration**: Connection with other tools

## Selection Criteria

When choosing a whiteboard tool, consider the following criteria:

- **Features**: Which features are required?
- **Ease of use**: How user-friendly is it?
- **Collaboration**: How good is real-time collaboration?
- **Integration**: How well does the system fit into the existing infrastructure?
- **Price**: Free or paid?
- **Security**: Data protection and security

## Related Categories

- [Project Management](../../suites/projectmanagement/) - Project management tools
- [Helpdesk](../helpdesk/) - Support and ticket systems
- [Messenger](../messenger/) - Communication and chat

## Quick Start

1. **Select whiteboard**: Choose a whiteboard based on requirements
2. **Installation/Account**: Install tool or create account
3. **Use templates**: Use pre-built templates
4. **Invite team**: Invite team members
5. **Start brainstorming**: Start first session

## More Information

Further information can be found in the documentation of individual whiteboard tools.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (7), by function, nothing copied (ADR 0012/0013):

- [draw.io](frontends/drawio/index.md) — draw.io (diagrams.net) is a free diagram tool for flowcharts, network plans, UML and BPMN.
- [Excalidraw](frontends/excalidraw/index.md) — Excalidraw is a free, open-source collaborative whiteboard in a hand-drawn style.
- [FigJam](frontends/figjam/index.md) — FigJam is the whiteboard product of Figma.
- [Miro](frontends/miro/index.md) — Miro is the commercial online whiteboard (SaaS) for visual collaboration: infinite canvas, shapes/sticky notes, frames, template library (retros, workshops, customer journeys), voting/timer and boa…
- [Mural](frontends/mural/index.md) — Mural is the workshop whiteboard suite (SaaS) with strong facilitation: canvas with shapes/notes, "Facilitation Sequence" (moderation flows), participation control and templates.
- [OpenBoard](frontends/openboard/index.md) — OpenBoard is a free interactive whiteboard tool (C++, Qt) for teaching and presentations: multi-page "boards", pens/text/images, integrated browser, document and note tools, offline-first with a lo…
- [tldraw](frontends/tldraw/index.md) — tldraw is an open-source infinite-canvas whiteboard library and app in TypeScript: ready to use on tldraw.com and as a React SDK (`tldraw`) for your own canvas applications.

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
