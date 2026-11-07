# Notion — layout (2026-11-07)

Sources: [S12] sidebar, [S15] page menu, [S13] databases. Pixel sizes and visual details are not in the official pages read and are not given.

## Regions

```
+--------------------------------------------------------------------+
| (page tabs)                                       Inbox  New item  |
+-------------------+------------------------------------------------+
| Sidebar           | Page header: icon, cover, title   ... (page)   |
|                   |----------------------------------------------- |
| Home              | Content: blocks, or database view             |
| Chats with AI     |                                                |
| Meetings          |                                                |
| Library           |                                                |
| Templates         |                                                |
| Trash             |                                                |
| Settings          |                                                |
| (workspace name)  |                                                |
+-------------------+------------------------------------------------+
```

The sketch is ours. It shows the places named in [S12] and [S15], not measured positions.

## Sidebar [S12]

- Top-level tabs with their own shortcuts and sections.
- Top-right: Inbox (notifications) and the New item menu.
- Items named on the page: Search (cmd/ctrl+K), Home, Chats with Notion AI, Meetings, Inbox, Library, Templates, Trash, Settings. "Library" browses all workspace content.
- Bottom: workspace name opens the workspace switcher.
- Sections: Private, Shared, Teamspaces. Favorites appears after the first favourite. Clicking a section name collapses it.
- Drag pages to reorder or nest them. Dragging a page into Trash deletes it with its sub-pages.
- Right edge: drag to resize. "<<" and ">>" collapse the sidebar; cmd/ctrl+\ also toggles it [S12].

## Content area

- Page header: icon, cover, title [S15].
- Page menu (••• at top right): Appearance & layout group with Font, Small text, Full width, Table of contents [S15].
- Database page: a view switcher with table, list, board, calendar, gallery and chart views [S13].
- Full-screen mode for images and embeds: cmd/ctrl+Enter on a selected block [S11].

## Layout variants

| Variant | Source |
|---------|--------|
| Full width and small text (desktop and web only) | [S15] |
| Sidebar hidden | [S12] |
| Mobile apps have a different navigation | unverified (no official page read) |

## Removed from the earlier page

The earlier layout page listed sidebar items Pages, Database, Members, Dashboard and Settings, a right sidebar for metadata, a status bar with word count, and breadcrumbs. None of these is in the official pages read. See [changelog.md](../changelog.md).
