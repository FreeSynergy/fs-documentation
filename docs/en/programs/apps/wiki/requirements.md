# Wiki — Requirements

What `FreeSynergy.Wiki` must and can do, derived from the [frontends](frontends/index.md)
(ADR 0006, 0013). Each capability names its data standard (ADR 0014) and our status.

Status: `implemented` · `planned` · `proposed`

## Required (common to the analysed programs)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Read revision history, restore a revision | Confluence, MediaWiki, Notion, Wiki.js, Tango | texts contract | proposed |
| Trash with restore | Confluence, MediaWiki, Notion, Wiki.js | texts contract | proposed |
| Permissions and sharing | Confluence, Notion, Wiki.js, Tango | Sharing interface (open) | proposed |
| Spaces / folders / namespaces, order of sibling pages | Confluence, MediaWiki, Wiki.js | texts contract | proposed |
| Templates, redirects | Confluence, MediaWiki, Wiki.js | texts contract | proposed |
| Search with snippets and filters, prefix search | Confluence, MediaWiki, Wiki.js | texts contract | proposed |
| Comments, talk pages | Confluence, MediaWiki, Notion | messages, with a reference to the page | proposed |
| Attachments | Confluence, Notion, Tango | files, with a reference | proposed |
| Labels, tags, categories | Confluence, MediaWiki, Wiki.js | shared tag field (open) | proposed |
| Watch, notifications | Confluence, MediaWiki, Wiki.js | `subscribe` in the hub | proposed |

Known defect: `editIf` reports a conflict as a text prefix, not as a typed `Problem`.

## Optional (notable ideas)

| Capability | Seen in | Data / standard | Status |
|------------|---------|-----------------|--------|
| Blocks and databases with views | Notion | open, larger decision | proposed |
| Real-time co-editing | Wiki.js (Yjs) | open, belongs to P2P (ADR 0059) | proposed |
| Capture clicks into a step-by-step guide | Tango | open | proposed |

## Not planned (deliberately)

Nothing yet.
