# Wiki Systems

## In short

FreeSynergy Wiki turns texts into connected pages. Pages link to each other, and you can see what links to a page. It answers the question: where do the things we write live, so that we can find, link and keep them?

## What is different here

- A text is stored as text plus layers, not as one flat file. The database is the truth, and files are exports.
- Saving is not exporting: nothing is written to your files until you press Export. If both the file and the database changed, the program shows you the conflict instead of overwriting either.
- You can import a folder of Markdown files, edit in the program, and export Markdown again when you decide to.
- Wiki owns the open text interface, so other programs can reach texts through one interface instead of keeping their own text model.

## Where it stands today

Latest tag: `v0.4.0`. You can create, edit, move, delete and list texts by path, with links, backlinks and search. Moving a text or a folder rewrites the links to it. Markdown can be imported and exported. An overwrite is refused when someone else saved first, and other programs are told when a text changes. A small server offers all of this over a local socket. There is a first window, the reader: a tree of pages, reading with formatting, following links, back, search, editing and saving, and an Export button. Unsaved drafts are backed up and offered back after a crash. The first start imports a documentation folder (about 30 seconds for 1,400 pages).

Not there yet (planned): typing in the real window has not been verified by tests; no other editors, no collections or shelves, no templates inside the program. The edit lock works inside one process only. Some characters (certain emoji) show as boxes, and very wide tables can run past the edge. The interface is a draft with no consumer yet.

## Overview

This section contains documentation for various wiki systems and knowledge platforms.

## Available Systems

- **wikijs** - Modern, lightweight wiki with markdown support
- **xwiki** - Enterprise wiki with extensions and macros
- **mediawiki** - Wikipedia's wiki engine
- **tango** - Capture clicks into step-by-step guides (tango.ai, not a wiki)
- **notion** - All-in-one workspace with wiki features
- **confluence** - Atlassian team collaboration
- **vscodium** - VS Code without telemetry (for local wiki hosting)
- **dokuwiki** - Simple file-based wiki
- **mediagoblin** - Federated media hosting platform

## What is a Wiki?

A wiki is a collaborative web system for creating, editing, and organizing knowledge bases, documentation, or community texts. Wiki systems are characterized by:

- Easy editing via web interface
- Revision tracking and version control
- Categorization and linking of content
- User roles and permission systems
- Search functions and indexing

## Application Areas

- **Technical Documentation**: Project documentation, API documentation
- **Knowledge Management**: Company wikis, knowledge bases
- **Education**: Teaching materials, course documentation
- **Community Projects**: Open-source documentation, community wikis

## Selection Criteria

When choosing a wiki system, consider the following criteria:

- **Features**: Which features are required?
- **Scalability**: How many users and pages?
- **Integration**: How well does the system fit into the existing infrastructure?
- **Ease of Use**: How user-friendly is it?
- **Costs**: Self-hosted or cloud service?
- **Open Source**: Are the license terms suitable?

## Related Categories

- [Messenger](../messenger/) - Communication and chat
- [Helpdesk](../helpdesk/) - Support and ticket systems
- [Project Management](../../suites/projectmanagement/) - Task and project management
- [Desktop](../../platform/desktop/) - Desktop applications for wiki work

## Quick Start

1. **Select wiki**: Choose a system based on requirements
2. **Installation**: Self-host or use cloud service
3. **Configuration**: Customize and configure the system
4. **Create content**: Create first wiki pages
5. **Invite users**: Invite team members and assign permissions

## More Information

Further information can be found in the documentation of individual wiki systems.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (8), by function, nothing copied (ADR 0012/0013):

- [Confluence](frontends/confluence/index.md) — Confluence is a team wiki and collaboration product by Atlassian.
- [MediaWiki](frontends/mediawiki/index.md) — MediaWiki is the wiki engine behind Wikipedia and the other Wikimedia projects.
- [Notion](frontends/notion/index.md) — Notion is a hosted all-in-one workspace for notes, documents and databases, built from typed blocks.
- [Tango](frontends/tango/index.md) — Tango turns recorded clicks into step-by-step guides; not a wiki, documented for its capture-to-guide idea.
- [Tango.io](frontends/tango.io/index.md) — Tango.io is a modern knowledge management platform focused on collaboration.
- [VSCodium](frontends/vscodium/index.md) — VSCodium is an open-source version of Microsoft Visual Studio Code.
- [Wiki.js](frontends/wikijs/index.md) — Wiki.js is an open-source, self-hosted wiki engine.
- [XWiki](frontends/xwiki/index.md) — XWiki is a powerful enterprise wiki platform with advanced features for knowledge management.

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
