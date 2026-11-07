# Notion — description (2026-11-07)

## What it is

Notion is a web and desktop workspace in which people write pages, organise them in databases and share them [S22, S12]. Notion calls its product an AI workspace for teams and their agents [S22]. The core model is a tree of pages. Each page holds blocks. Databases are pages with a collection of rows and views [S13, S9].

## Why it matters for a wiki frontend

- Content is block-based. A frontend must render and edit a tree of typed blocks [S9].
- Structure comes from pages and sub-pages in a sidebar tree [S12].
- Databases are a second kind of content, with schema, rows and views [S7, S13].
- The product has a public API with OAuth and webhooks [S3, S4].

## Notable ideas

1. **Block as the unit.** Every paragraph, list item, table, image and embed is a block with an id and a type. Blocks can have children [S9, S18].
2. **Markdown input while typing.** Typing `# `, `- `, `[] ` and similar prefixes creates the matching block [S11].
3. **Database views on one data set.** Table, list, board, calendar, gallery and chart are views of the same data [S13].
4. **Schema per data source.** Since API version `2025-09-03` a database can hold several data sources, each with its own properties [S7].
5. **Trash with restore.** Deleted pages stay for 30 days and can be restored [S14].

## Who it suits (from the product page, not a judgement)

Notion targets teams and individuals who want notes, wikis and small databases in one tool [S22, S13]. Notion does not publish a market segment list on the pages read.

## Differences to note

Notion is a hosted service. No self-hosted edition was found in the official pages read [unverified]. Notion's data model is proprietary. Export is possible (see [features.md](features.md)).

## Sources

[S22], [S12], [S13], [S9], [S7], [S3], [S4], [S14]. The earlier comparisons with other products (Tango.io, Confluence, XWiki) are not verified and are removed here.
