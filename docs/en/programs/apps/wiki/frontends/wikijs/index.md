# Wiki.js

> Category: [wiki](../../index.md)

## What it is

Wiki.js is an open-source, self-hosted wiki engine. The project describes itself as "The open source wiki engine. Built and maintained in the open since 2017." Source: https://js.wiki/

The current line is 3.x. The server is Node.js (Fastify), the UI is Vue 3, and content is stored in PostgreSQL with the page content mirrored to optional storage targets (disk, git, S3-compatible, Azure, GCS, SFTP). Sources: https://github.com/requarks/wiki/blob/3.1.1/backend/CLAUDE.md , https://github.com/requarks/wiki/blob/3.1.1/frontend/CLAUDE.md , https://github.com/requarks/wiki/blob/3.1.1/backend/package.json

## Version facts

| Item | Value | Source |
|------|-------|--------|
| Version documented here | **3.1.1** (newest 3.x release) | https://github.com/requarks/wiki/releases/tag/3.1.1 |
| Release date | 2026-11-06 (GitHub `published_at`) | `gh api repos/requarks/wiki/releases/tags/3.1.1` |
| Marked "Latest" on GitHub | yes | https://github.com/requarks/wiki/releases |
| Also released | 3.1.0 (2026-11-05), 3.0.2, 3.0.1 (first stable 3.0), 3.0.0-beta.* | https://github.com/requarks/wiki/releases |
| Does 3.1 exist | **yes**: tags 3.1.0 and 3.1.1 are released, not pre-release | same |
| Newest 2.x | v2.5.315 (2026-09-21) | https://github.com/requarks/wiki/releases/tag/v2.5.315 |

The owner asked for 3.1. Both 3.1.0 and 3.1.1 exist; 3.1.1 is documented because it is the newest and only has bug and security fixes over 3.1.0 (see `3.1.1/description.md`).

## Notable ideas

Only ideas that are verified in the 3.1.1 source are listed here.

1. **One wiki, many storage targets.** Content lives in the database. A site can additionally keep the same page tree on disk, in a git repository (commit per change, sync with a remote), or in object storage. Source: https://github.com/requarks/wiki/blob/3.1.1/.claude/rules/storage.md
2. **Eight editors per site.** Markdown (Monaco), Visual (ProseMirror), AsciiDoc, Excalidraw drawing, Blog, Feedback board, Redirect. Each can be switched on or off. Live notes are a separate page type under `/n/`. Sources: https://github.com/requarks/wiki/blob/3.1.1/backend/models/sites.ts , https://docs.js.wiki/guide/editors
3. **Real-time co-editing.** The Markdown and Visual editors share a Yjs document over a websocket. Sources: https://github.com/requarks/wiki/blob/3.1.1/frontend/src/editor/visual/collab.js , https://github.com/requarks/wiki/blob/3.1.1/backend/controllers/collab.ts
4. **Per-user personal access tokens with scopes**, separate from system API keys. A personal token acts as its owner and is limited to declared scopes. Source: https://github.com/requarks/wiki/blob/3.1.1/.claude/rules/personal-access-tokens.md
5. **MCP server** at `/_mcp`, so AI assistants can search and read the wiki with a personal token. Source: https://github.com/requarks/wiki/blob/3.1.1/.claude/rules/mcp.md
6. **Per-site appearance settings in the database** (colours, fonts, content width, sidebar side, injected CSS/HTML), not a theme file. Source: https://github.com/requarks/wiki/blob/3.1.1/backend/models/sites.ts

## Important differences from 2.x

| Topic | 2.5.x | 3.1.1 | Source |
|-------|-------|-------|--------|
| Frontend | Vue 2, Vuetify 2, Apollo | Vue 3, Vite, Pinia, Tailwind 4 | https://github.com/requarks/wiki/blob/3.1.1/frontend/package.json |
| API | GraphQL (`server/graph/schemas/*.graphql`) | REST under `/_api` (Fastify), OpenAPI page at `/_api`; no GraphQL in the tree | https://github.com/requarks/wiki/tree/v2.5.315/server/graph/schemas , https://github.com/requarks/wiki/blob/3.1.1/backend/index.ts |
| Auth modules | many (auth0, okta, keycloak, …) | local, ldap, oidc, saml, github, google, discord, entra | `backend/modules/authentication/` at each tag |
| Node.js | >= 20 | >= 26 | package.json `engines` at each tag |

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [3.1.1](3.1.1/description.md) | 7/7 |
| [latest](latest/description.md) | 6/7 |

### 3.1.1

| File | Contents |
|------|----------|
| [description.md](3.1.1/description.md) | Detailed description, differentiation, who it suits |
| [features.md](3.1.1/features.md) | What the program can do — and what not |
| [layout.md](3.1.1/layout.md) | Window structure, regions, panels |
| [menus.md](3.1.1/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](3.1.1/shortcuts.md) | Keyboard shortcuts |
| [api.md](3.1.1/api.md) | APIs and protocols, authentication, rate limits |
| [themes/index.md](3.1.1/themes/index.md) | Themes: colours, typography, spacing — what can be rebuilt |
| [events.md](3.1.1/events.md) | Events to the outside (webhooks, push, streams) |
| [limits.md](3.1.1/limits.md) | Known limitations |
| [dependencies.md](3.1.1/dependencies.md) | Which of our components a frontend in this style needs |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->

## Sources

- Official site: https://js.wiki/
- Official docs (site structure checked; not read page by page): https://docs.js.wiki/
- Release list: https://github.com/requarks/wiki/releases
- Source at tag 3.1.1: https://github.com/requarks/wiki/tree/3.1.1
- Source at tag v2.5.315: https://github.com/requarks/wiki/tree/v2.5.315

Other files in this set: `3.1.1/` (per-version analysis) and `corrections.md` (what the old pages got wrong).
