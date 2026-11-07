# MediaWiki

> Category: [wiki](../../index.md)

## What it is

MediaWiki is the wiki engine behind Wikipedia and the other Wikimedia projects. It is a PHP web application with a relational database. The core ships a server-rendered skin (Vector 2022, the default since `$wgDefaultSkin` = `vector-2022`), a wikitext source editor, the VisualEditor extension, the Action API (`api.php`) and a smaller REST API (`rest.php`). Sources: https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/config-schema.php (DefaultSkin), https://www.mediawiki.org/wiki/API:REST_API

## Version facts

| Item | Value | Source |
|------|-------|--------|
| Documented version | 1.46 (current stable, point release 1.46.2) | https://www.mediawiki.org/wiki/MediaWiki_1.46 |
| 1.46.0 release date | 30 June 2026 | https://www.mediawiki.org/wiki/Version_lifecycle |
| Next release | 1.47, LTS, listed as "future version" with release November 2026 | https://www.mediawiki.org/wiki/Version_lifecycle |
| Previous LTS | 1.43, released 21 December 2024, end of life December 2027 | https://www.mediawiki.org/wiki/Version_lifecycle |

Plan: the frontend in our style should target 1.46 now. Check again when 1.47 is tagged, because 1.47 changes the default source editor (see `1.46/features.md`).

## Notable ideas (for our purpose)

- **Action API as the stable contract.** Every operation is a module with a named `action` and typed parameters, with a token-based write model. The API is documented on mediawiki.org and the parameter list is self-describing (`action=help`, Special:ApiSandbox). Source: https://www.mediawiki.org/wiki/API:Main_page
- **Everything is a page in a namespace.** Talk pages, categories, files, templates and user pages are ordinary pages in numbered namespaces. A "Talk" tab is a link to the paired namespace. Source: https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts (namespace rows), https://github.com/wikimedia/mediawiki/blob/REL1_46/resources/src/mediawiki.util/jquery.accessKeyLabel.js
- **Revisions are the unit of history.** Every save creates a revision. History, diff and rollback work on revisions, not on files. Source: https://www.mediawiki.org/wiki/API:RecentChanges
- **Access keys as the keyboard model.** Actions have single-letter access keys combined with a browser-specific modifier, not Ctrl-based shortcuts. Source: https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts
- **Layered skin system.** Vector 2022 is built on Codex design tokens and CSS custom properties (ADR 0002). Source: https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/doc/adr/0002-use-css-custom-properties.md
- **Pluggable everything** through extensions (VisualEditor, Echo, CodeMirror, ULS). Core is small; many features in the pages we know are extensions. Source: https://www.mediawiki.org/wiki/Extension:Echo, https://www.mediawiki.org/wiki/Extension:CodeMirror

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [1.46](1.46/description.md) | 7/7 |

### 1.46

| File | Contents |
|------|----------|
| [description.md](1.46/description.md) | Detailed description, differentiation, who it suits |
| [features.md](1.46/features.md) | What the program can do — and what not |
| [layout.md](1.46/layout.md) | Window structure, regions, panels |
| [menus.md](1.46/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](1.46/shortcuts.md) | Keyboard shortcuts |
| [api.md](1.46/api.md) | APIs and protocols, authentication, rate limits |
| [themes/index.md](1.46/themes/index.md) | Themes: colours, typography, spacing — what can be rebuilt |
| [events.md](1.46/events.md) | Events to the outside (webhooks, push, streams) |
| [limits.md](1.46/limits.md) | Known limitations |
| [i18n.md](1.46/i18n.md) | Localisation, writing direction |
| [dependencies.md](1.46/dependencies.md) | Which of our components a frontend in this style needs |
<!-- /gen:versions -->

## Sources used

- https://www.mediawiki.org/wiki/API:Main_page
- https://www.mediawiki.org/wiki/API:Login
- https://www.mediawiki.org/wiki/API:Watchlist
- https://www.mediawiki.org/wiki/API:RecentChanges
- https://www.mediawiki.org/wiki/API:REST_API
- https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts
- https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts
- https://www.mediawiki.org/wiki/MediaWiki_1.46
- https://www.mediawiki.org/wiki/Version_lifecycle
- https://raw.githubusercontent.com/wikimedia/mediawiki/REL1_46/RELEASE-NOTES-1.46
- https://github.com/wikimedia/mediawiki/tree/REL1_46 (config-schema.php, Api/*.php, resources/src/mediawiki.util, languages/i18n/en.json, includes/Rest/coreRoutes.json)
- https://github.com/wikimedia/mediawiki-skins-Vector/tree/REL1_46 (Vector 2022 templates, JS, LESS variables, configuration.md)
- https://github.com/wikimedia/codex/tree/main/packages/codex-design-tokens/src (theme and mode token files)

Known gaps in this research: mediawiki.org returned HTTP 403 to automated fetch for API:Etiquette and API:Authentication. The rules for those pages were read through the WebFetch summary, which is a weaker source than the page text. Marked "summary-only" where it matters.
