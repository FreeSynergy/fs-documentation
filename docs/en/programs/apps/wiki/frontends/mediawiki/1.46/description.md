# MediaWiki 1.46 — Description

Version checked: 1.46.2 (current stable, https://www.mediawiki.org/wiki/MediaWiki_1.46). Support and release dates: https://www.mediawiki.org/wiki/Version_lifecycle

## What it does

- Hosts a wiki: pages with revisions, namespaces, categories, files, templates, users, rights and logs.
- Renders wikitext (its own markup language) to HTML on the server. Templates and parser functions run during rendering.
- Offers two editing routes: the wikitext source editor and the VisualEditor (an extension). Source: https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts (VisualEditor exists as a separate editor surface).
- Exposes two HTTP APIs: the Action API (`api.php`, all features) and the REST API (`rest.php`, smaller set of page, revision and search resources). Source: https://www.mediawiki.org/wiki/API:REST_API, https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/Rest/coreRoutes.json
- Keeps a revision history for every page and a recent-changes log. Source: https://www.mediawiki.org/wiki/API:RecentChanges

## Position in the field

MediaWiki is the reference model for public, large, multi-author wikis. Its strengths and costs for us:

| Aspect | Fact (verified) | Consequence for a "MediaWiki-style" frontend |
|--------|-----------------|-----------------------------------------------|
| Data model | Page + revisions + namespaces; talk is a namespace | We need a namespace concept and paired talk pages |
| Markup | Wikitext with templates and parser functions | Our engine stores a document (texts.capnp `document` as JSON), so the markup layer is a conversion, not the store |
| API | Large Action API, many modules, token-based writes | We use only the subset we need, through our own contract |
| Skin | Vector 2022 (default), server-rendered with progressive enhancement | Layout can be rebuilt from its structure (see `layout.md`) |
| Extensions | Most features are extensions (Echo, CodeMirror, ULS, VisualEditor) | Our feature list must say which parts are core and which are not |

Source for "Vector 2022 is default": https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/config-schema.php (key `DefaultSkin` = `vector-2022`).

## Who it suits (in our own words)

Large multi-author wikis with long-lived content, many languages and public reading. It is heavy to operate and its UI is built for experienced editors. It is not a team-chat or task tool.

## Technical facts used later

| Item | Value | Source |
|------|-------|--------|
| Language | PHP 8.3.0 or newer, with ctype, dom, fileinfo, iconv, intl, mbstring, xml | https://raw.githubusercontent.com/wikimedia/mediawiki/REL1_46/RELEASE-NOTES-1.46 (section Compatibility) |
| Database | MariaDB (recommended), MySQL 5.7+, PostgreSQL 10+, SQLite 3.8+ | same |
| Default DB type in config | `mysql` | config-schema.php, key `DBtype` |
| Core installers | MySQL, PostgreSQL, SQLite | `includes/Installer/*` in the REL1_46 tree |

Note: the existing page says "LDAP" is a core authentication method. LDAP is not in core. Unverified as core; treat as extension (see `../changelog.md`).
