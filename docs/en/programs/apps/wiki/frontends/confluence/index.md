# Confluence

> Category: [wiki](../../index.md)

## What it is

Confluence is a team wiki and collaboration product by Atlassian. Content is organised in spaces. Content types in Cloud include pages, live docs, blog posts, databases, whiteboards and folders. [S10][S14]

## Version facts

| Item | Value |
|------|-------|
| Product | Confluence Cloud (hosted by Atlassian) |
| Version label | `latest`. The official pages read do not give a numbered Cloud version. Cloud is updated continuously. |
| Data Center | Self-managed line. End of life 2029-03-28 (see Data Center notes below). [S20] |

Folder for this snapshot: `latest/`.

## Notable ideas (verified)

- Two REST API generations: v1 under `/wiki/rest/api/` and v2 under `/wiki/api/v2/`. v2 uses cursor pagination. [S1][S2]
- Page bodies have a named representation: `storage`, `atlas_doc_format` and `wiki` appear as enum values in the v2 schema. [S4]
- Editor accepts Markdown autoformat triggers (`**bold**`, `# ` headings, `1. ` lists, `> ` quotes, `---` dividers). [S12]
- Metadata (owner, status, labels, links, contributors) lives in a Details panel, not in a fixed right column. [S15]
- The top bar has an integrated AI chat entry (Rovo). [S14]
- Live updates exist through Forge events and, for legacy apps, Connect webhooks. [S10][S11]
- Atlassian publishes its own design tokens (Atlassian Design System). [S18][S19][S21]

## Data Center notes

- New Data Center purchases stopped on 2026-03-30. Renewals and expansions are possible until 2028-03-30 and renewals cannot run beyond 2029-03-28. End of life (read-only licences) is 2029-03-28 at 23:59 PST. [S20]

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 7/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |
| [themes/index.md](latest/themes/index.md) | Themes: colours, typography, spacing — what can be rebuilt |
| [states.md](latest/states.md) | UI states and transitions |
| [events.md](latest/events.md) | Events to the outside (webhooks, push, streams) |
| [limits.md](latest/limits.md) | Known limitations |
| [dependencies.md](latest/dependencies.md) | Which of our components a frontend in this style needs |
| [dialogs.md](latest/dialogs.md) | Every dialog: purpose, fields, buttons, default, cancel |
| [workflows.md](latest/workflows.md) | Step-by-step workflows: goal, prerequisites, steps, failures, undo |
| [acceptance.md](latest/acceptance.md) | Acceptance checklist: each workflow as a yes/no click test |
| [gaps.md](latest/gaps.md) | What our program cannot do for these workflows, and what it needs |
<!-- /gen:versions -->

## Sources

| Id | Title | URL |
|----|-------|-----|
| S1 | REST API v2 introduction | https://developer.atlassian.com/cloud/confluence/rest/v2/intro/ |
| S2 | REST API v1 introduction | https://developer.atlassian.com/cloud/confluence/rest/v1/intro/ |
| S3 | REST API v2, Page group | https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/ |
| S4 | OpenAPI v2 specification (JSON) | https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json |
| S5 | Rate limiting | https://developer.atlassian.com/cloud/confluence/rate-limiting/ |
| S6 | OAuth 2.0 (3LO) apps | https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/ |
| S7 | Basic auth for REST APIs | https://developer.atlassian.com/cloud/confluence/basic-auth-for-rest-apis/ |
| S8 | GraphQL API | https://developer.atlassian.com/cloud/confluence/graphql/ |
| S9 | Cloud changelog | https://developer.atlassian.com/cloud/confluence/changelog/ |
| S10 | Forge events reference (Confluence) | https://developer.atlassian.com/platform/forge/events-reference/confluence/ |
| S11 | Connect webhooks module | https://developer.atlassian.com/cloud/confluence/modules/webhook/ |
| S12 | Keyboard shortcuts, Markdown and autocomplete | https://support.atlassian.com/confluence-cloud/docs/keyboard-shortcuts-markdown-and-autocomplete |
| S13 | Find keyboard shortcuts | https://support.atlassian.com/confluence-cloud/docs/find-keyboard-shortcuts |
| S14 | Improved navigation | https://support.atlassian.com/confluence-cloud/docs/improved-confluence-navigation/ |
| S15 | New and simplified content layout (beta) | https://support.atlassian.com/confluence-cloud/docs/get-to-know-the-new-and-simplified-content-layout/ |
| S16 | Export content (Cloud) | https://support.atlassian.com/confluence-cloud/docs/export-content-to-word-pdf-html-and-xml/ |
| S17 | Apply a theme to a site | https://support.atlassian.com/confluence-cloud/docs/apply-a-theme-to-a-site/ |
| S18 | Atlassian Design System, colour | https://atlassian.design/foundations/color |
| S19 | Atlassian Design System, typography | https://atlassian.design/foundations/typography |
| S20 | Data Center end of life | https://www.atlassian.com/licensing/data-center-end-of-life |
| S21 | Atlassian Design System, spacing | https://atlassian.design/foundations/spacing |
| S22 | Connect app scopes (legacy; page shows Connect scopes only) | https://developer.atlassian.com/cloud/confluence/scopes/ |
| S23 | Create, update, and manage written content (fetched 2026-11-13) | https://support.atlassian.com/confluence-cloud/docs/create-edit-and-publish-a-page/ |
| S24 | Move, copy, and hide content items (fetched 2026-11-13) | https://support.atlassian.com/confluence-cloud/docs/move-copy-and-hide-pages/ |
| S25 | Delete, restore, or purge a content item (fetched 2026-11-13) | https://support.atlassian.com/confluence-cloud/docs/delete-restore-or-purge-a-page/ |
| S26 | Import external documents (fetched 2026-11-13) | https://support.atlassian.com/confluence-cloud/docs/import-content-into-confluence-cloud/ |
| S27 | Manage uploaded files (fetched 2026-11-13) | https://support.atlassian.com/confluence-cloud/docs/manage-uploaded-files/ |
| S28 | Archive content items (fetched 2026-11-13) | https://support.atlassian.com/confluence-cloud/docs/archive-pages/ |
| S29 | Upload a file (search-result summary only, 2026-11-13; page not fetched) | https://support.atlassian.com/confluence-cloud/docs/upload-a-file/ |
| S30 | Insert and manage links (search-result summary only, 2026-11-13; page not fetched) | https://support.atlassian.com/confluence-cloud/docs/insert-and-manage-links-on-your-pages/ |
| S31 | Format a page with a template (search-result summary only, 2026-11-13; page not fetched) | https://support.atlassian.com/confluence-cloud/docs/create-a-page-from-a-template/ |

"search summary" in the workflow pages means a search-engine summary (2026-11-13) of the Version history and Search documentation; those pages were not fetched, so the points taken from them (compare, restore comment, archived content in search) are of lower certainty. Sources S23 and S25 to S28 were fetched; the version-history page URL itself was not identified.

Pages that returned 404 or could not be read: webhooks landing page `https://developer.atlassian.com/cloud/confluence/webhooks/` (404 twice); OpenAPI request-body schemas (not reached in the JSON; see `api.md`).
