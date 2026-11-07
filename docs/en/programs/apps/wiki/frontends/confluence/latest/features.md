# Confluence (Cloud, latest) · Features

Sources: S-numbers refer to the table in [index.md](../index.md).

## Can do (verified)

| Area | Function | Source |
|------|----------|--------|
| Editing | Markdown autoformat while typing (headings, lists, quotes, code, dividers, action items, decisions, emoji `:`, mention `@`, macro `{`) | [S12] |
| Editing | Toolbar placement: fixed top bar or inline toolbar on text selection | [S15] |
| Editing | Insert: link, files and images, markup, macro, table; quick insert with `/` | [S12] |
| Editing | Tables: add row above/below, add column before/after | [S12] |
| Editing | Undo/redo; find and replace | [S12] |
| Editing | Publish (Ctrl/Cmd+Enter), publish with note | [S12] |
| Content | Watch, share, edit labels, favourite, view attachments, comment | [S12] |
| Content | Version history ("Version history (view changes)" under the more-actions menu) | [S15] |
| Content | Archive and delete; templates and import from the more-actions menu | [S15] |
| Content | Details panel: owner, views, read time, contributors, creator, status, classification, labels, linked files, attachments, Jira links, Smart Links | [S15] |
| Content | Presenter mode | [S12] |
| Export | Page or live doc or blog post to Word and PDF | [S16] |
| Export | Space (or selected pages) to PDF, CSV, HTML, XML by a space admin | [S16] |
| Navigation | Customise sidebar order and visibility (More > Customize sidebar) | [S14] |
| Navigation | Space sidebar items set per space (Space settings > General > Features) | [S14] |
| Navigation | Quick search (Win: Alt+Shift+Z; Mac: Ctrl+Opt+Z) | [S12] |
| Theme | Per user Light or Dark | [S17] |
| Theme | Site default theme: Settings > Look and feel > Themes | [S17] |
| API | REST v1 and v2, GraphQL, OAuth 2.0 (3LO), basic auth | [S1][S2][S6][S7][S8] |
| Events | Forge events for most content types; Connect webhooks (legacy) | [S10][S11] |

## Cannot do or limited (verified)

| Area | Limit | Source |
|------|-------|--------|
| Shortcuts | Shortcuts cannot be remapped in the docs read. General shortcuts can be turned off. (Customising: unverified) | [S12] |
| Export | Word files open only in Microsoft Word, not LibreOffice, OpenOffice or Google Docs | [S16] |
| Export | Only published content is exported | [S16] |
| Export | Space PDF export: comments are never included; blog posts are excluded from PDF and HTML space exports; Team Calendars are excluded from all space exports | [S16] |
| Export | PDF layout customisation applies only to the multi-page method, not the single-page method | [S16] |
| Events | Connect webhooks: no new Connect features; Connect apps can no longer be published on the Marketplace | [S11] |
| API | Beta GraphQL fields can change without notice | [S8] |
| API | REST page updates in spaces that require publishing approval return HTTP 409 (announced, rollout date not announced) | [S9] |
| Theme | Dark mode is a personal setting; site default is set by admins | [S17] |

## Not verified (do not build on these yet)

- Macro syntax (`{note}`, `{code}`, `{jira:...}`): not documented in any Cloud page read.
- Wiki Markup source editor as a Cloud mode: not documented in the pages read.
- Code block language list: not verified.
- Mobile app features, auto-save behaviour, offline mode: not verified.
- Comparison table with other wikis: not an official source. Removed.
