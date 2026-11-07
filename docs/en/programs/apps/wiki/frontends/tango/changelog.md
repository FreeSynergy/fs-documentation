# Changelog

## 2026-11-07: rewritten from official sources

The earlier pages were written from memory; these statements were wrong.

Pages checked: `fs-documentation/docs/en/programs/apps/wiki/frontends/tango.io/` (index.md, latest/*.md). Status key: **wrong** = contradicted by a source; **invented** = no source found, claim removed; **unverified** = no source found in this review.

Overall: the existing pages describe a different product (a block-based team wiki with a public REST API). The product that matches the name is a capture-to-guide tool at tango.ai. Nearly all API, shortcut and menu content is invented.

### index.md

| Existing statement | Status | Correct fact | Source |
|---|---|---|---|
| "Tango.io is a modern knowledge-management platform that focuses on collaboration." | wrong | Tango (tango.ai) records a process and turns it into a step-by-step how-to guide. Not a wiki. | https://help.tango.ai/en/ |
| Implied product is tango.io | wrong | `tango.io` is a services company "Tango" with no capture product. The product is at tango.ai. | https://tango.io/ ; https://www.tango.ai/ |
| Version table "6/7", `themes/index.md` missing | fixed | Themes file now written; branding is the only theme surface documented. | [themes](latest/themes/index.md) |
| "Notable ideas: to do" | fixed | Capture-to-guide, shareable views, Tango MCP. | [index](index.md) |

### latest/api.md (entire file)

| Existing statement | Status | Correct fact | Source |
|---|---|---|---|
| REST API at `https://api.tango.io/v1` | invented | No public API documented. | https://help.tango.ai/en/collections/3466202-team-workspaces ; search for public API found nothing |
| Endpoints `/v1/pages`, `/v1/workspaces`, `/v1/users`, `/v1/comments`, `/v1/search`, `/oauth/token`, `/oauth/authorize` | invented | None documented. | same |
| OAuth2 authorization-code and client-credentials flows, `X-API-Key` header | invented | None documented. The only documented sign-in is for the Tango MCP connector (OAuth) and SSO for users. | https://help.tango.ai/en/articles/17890522-how-do-i-connect-tango-to-my-ai-assistant ; https://www.tango.ai/pricing |
| Rate limits 1000/h, 100/min, `X-RateLimit-*` headers | invented | No API, no limits documented. | — |
| Webhooks (`page.created`, `comment.created`, …) and "Settings > Webhooks" | invented | No webhooks documented. | — |
| SDKs `@tangoio/sdk`, `tangoio-sdk`, `tangoio-go`, `tangoio-java-sdk`, install commands | invented | None found. Do not install these names: they are unverified and may belong to others. | — |
| Python, Node.js, curl examples | invented | Not applicable. | — |
| Support page calls (`GET /v1/pages/:id` etc.) | invented | Not applicable. | — |

### latest/description.md

| Existing statement | Status | Correct fact | Source |
|---|---|---|---|
| "Knowledge-management platform focused on collaboration and document management" | wrong | Process documentation and in-app guidance. | https://www.tango.ai/ |
| Backend Node.js, database PostgreSQL, frontend React | unverified | No source. Remove from our docs. | — |
| Authentication OAuth2, SSO | partly wrong | SSO and SCIM are Enterprise. OAuth applies only to the MCP connector. | https://www.tango.ai/pricing ; https://help.tango.ai/en/articles/17890522-how-do-i-connect-tango-to-my-ai-assistant |
| "Real-time collaboration" | unverified | No source. | — |
| "Strong embeds: 100+ embeds" | unverified | Embeds exist (iframe into knowledge bases; one-click for Notion, Confluence, Zendesk). The count is not stated. | https://help.tango.ai/en/articles/7142097-how-do-i-embed-a-tango-into-my-website-or-knowledge-base |
| "Cheaper than Confluence", comparisons with Notion, Confluence, Wiki.js | unverified | Vendor's pricing is published; comparisons are not. | https://www.tango.ai/pricing |
| "Block-based" editing | wrong | Step list with screenshots and text per step. | https://help.tango.ai/en/articles/7966907-how-do-i-use-tango-for-documentation |
| "Commercial, comes with support" | partly | Commercial, yes. Support tiers not checked. | https://www.tango.ai/pricing |
| Target audience (teams, startups, design teams) | unverified | Vendor's own help centre names onboarding, support and IT documentation. | https://help.tango.ai/en/ |

### latest/features.md

| Existing statement | Status | Correct fact | Source |
|---|---|---|---|
| "Visual editor modelled on Notion" with H1–H6, task lists, emojis, page links, @mentions, timestamps | invented | No such editor documented. Editor works on steps. | https://help.tango.ai/en/collections/4063296-capturing-editing |
| 12 block types (text, table, to-do, quote, file …) and `-[ ]`, `*`, `1.` shortcuts | invented | Not documented. | — |
| Code blocks with 20+ languages | invented | Not documented. | — |
| Tables with filter, sort, column formulas | invented | Not documented. | — |
| Templates (meeting minutes, bug report …) | invented | No template feature found in help-centre collections read. | https://help.tango.ai/en/collections/3466202-team-workspaces |
| Embeds: YouTube, Figma, Spotify … 100+ | unverified | Only "Video embeds" (Pro) is documented as a feature name. | https://www.tango.ai/pricing |
| "No Markdown" in editor | unverified | Markdown is an export format (Pro/Ent). | https://www.tango.ai/pricing |
| Comparison table and "Recommendation" section | invented | Marketing content, not verifiable. Removed. | — |
| Real features missing from the page | gap | Capture, step reorder, branching, Live Blur, Secure Blur, annotation, branding, Guide Me, Pins. | [features](latest/features.md) |

### latest/layout.md

| Existing statement | Status | Correct fact | Source |
|---|---|---|---|
| Left sidebar: Home, Pages, Files, Templates, Members, Dashboard, Settings; workspace selector | unverified | Not documented. Documented areas: side panel in browser, capture controller, editor, Share & Export, Team Library, Settings & members. | [layout](latest/layout.md) |
| Header with workspace, search, user menu | unverified | Not documented. | — |
| Three layout variants (standard, compact, full-screen editor) | unverified | Not documented. | — |
| Light / dark / custom colour themes | unverified | Not documented. Only branding (logo, action-box colours, badge). | https://help.tango.ai/en/articles/5971709-can-i-add-my-own-branding-to-tango-workflows |
| Responsive: tablet and mobile with hamburger menu | wrong | No mobile app; no capture on phones or tablets; guides open in mobile browser. | https://help.tango.ai/en/articles/17359491-where-does-tango-work |
| Accessibility (ARIA, high contrast, zoom) and performance (lazy loading, debounce) | unverified | An accessibility article exists but was not read. | https://help.tango.ai/en/articles/6081830-what-accessibility-features-does-tango-include |
| Auto-save | unverified | Not documented. | — |
| ASCII block-editor diagram | invented | Not applicable. | — |

### latest/menus.md

| Existing statement | Status | Correct fact | Source |
|---|---|---|---|
| 12 main items (Home, Workspace, Pages, Templates, Files, People, Settings, Search, Dashboard, Notifications, Bookmark, Recently viewed) | invented | Not documented as a menu. Side panel shows starred and recently viewed guides; Team Library; Insights & Analytics collection exists. | https://help.tango.ai/en/articles/7926363-how-do-i-use-the-tango-side-panel ; https://help.tango.ai/en/collections/15535477-insights-analytics |
| Page context menu: Edit, Copy, Move, Delete, Share, Print, Export | unverified | Share & Export and bulk actions are documented. | [menus](latest/menus.md) |
| Member, file menus | unverified | Members via Settings & members. | — |
| Workspace import/export, workspace statistics | unverified | Audit log download is documented (Enterprise). | https://help.tango.ai/en/articles/13259730-how-do-i-download-a-workspace-wide-audit-log |

### latest/shortcuts.md (almost entire file)

| Existing statement | Status | Correct fact | Source |
|---|---|---|---|
| About 150 shortcuts: Ctrl+Shift+P command palette, Ctrl+K add link, Ctrl+B bold, Ctrl+Shift+1–6 headings, Ctrl+Shift+J/P/H/C/S/M/E code syntax, Ctrl+S save, Ctrl+P print, F11 full screen, Ctrl+Shift+I dev tools, and Mac duplicates | invented | Not documented. The same key combination is listed for different actions in the same table (e.g. Ctrl+Shift+X cut and strikethrough; Ctrl+Shift+P command palette, paragraph and Python; Ctrl+Shift+C code block, CSS and copy). A table with such collisions is not a real key map. | — |
| Only shortcuts verified | fact | Ctrl/Cmd+Z undo, Ctrl/Cmd+Y redo (editor, edit mode). Team Library: Shift+Click, Ctrl/Cmd+A, Ctrl/Cmd+Click, Esc. Cmd+K search (search snippet). | [undo](https://help.tango.ai/en/articles/17747616-how-do-i-undo-changes-in-the-tango-editor) ; [bulk actions](https://help.tango.ai/en/articles/16652169-how-do-i-use-bulk-actions-in-the-team-library) ; [shortcuts](latest/shortcuts.md) |
| "Summary" paragraph about Mac and code syntax | invented | Not applicable. | — |

### Other

- The page "Tango.io" name is a naming collision. The docs tree should name the product "Tango" and link tango.ai, with a note that tango.io is a different company.
- The `changelog.md` rule (ADR 0012, ≥ 2 versions) is not met: one version only.
