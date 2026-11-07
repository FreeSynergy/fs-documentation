# Confluence (Cloud, latest) · Layout

Sources: S-numbers refer to the table in [index.md](../index.md). Layout is labelled as beta by Atlassian for the new content layout. [S15]

## Global frame

```
+--------------------------------------------------------------------------+
| Top bar: Search · Create · Chat (Rovo) · Notifications · Help · Profile  |
+----------------+-----------------------------------------+---------------+
| Sidebar        | Content area                            | (Details      |
| (collapsible)  | breadcrumbs (hidden while editing)      |  panel opens  |
|                | header: title, "Last updated"           |  on the right |
|                | title area: owner, status, labels, etc. |  on demand)   |
|                | body (view or editor)                   |               |
|                |                                         |               |
|                                  floating action bar (bottom right)     |
+----------------+-----------------------------------------+---------------+
```

Sources: top bar items [S14]; sidebar items [S14]; header and title area [S15]; floating bar [S15].

## Top bar [S14]

| Item | Function |
|------|----------|
| Search | Finds pages, live docs, spaces and other content |
| Create | New page, live doc, database, Loom video, whiteboard or slides |
| Chat | Opens chat with Rovo |
| Notifications | Activity on watched items and spaces, replies, mentions, task assignments |
| Help | Online help and "what's new" |
| Your profile and settings | Personal space, Confluence settings, feedback |

## Sidebar [S14]

Order by default, top to bottom: Expand/Collapse, app switcher, Confluence logo (returns to "For you"), For you, Recent, Starred, Spaces, Apps, More, Teams, Drafts, Company Hub (only if the organisation has published one), Customize sidebar.

## Content header and title area [S15]

- Breadcrumbs are hidden at the top left while working. The down caret shows the full path.
- The header holds the "Last updated" timestamp. Hovering or focusing it shows the last editor.
- Title area shows, when relevant: content owner, classification, status, emoji reactions, read time, views.
- "..." (More actions) holds: Watch settings, Version history (view changes), Find and replace, Templates and import, Archive and delete. Some header items moved here or to the Details panel.
- Marketplace app buttons in the header are not supported in the new layout.

## Floating action bar [S15]

Fixed bottom right. Opens: comments panel, Details panel, emoji reactions, Loom video creation, and Atlassian Intelligence (Premium and Enterprise only).

## Details panel [S15]

Opens on the right. Contents: ownership, views and analytics, read time, contributors, creator, status, classification, labels, linked files, attachments, Jira links and Smart Links.

## Space sidebar [S14]

Contains the space overview, pages, live docs, blogs and whiteboards. Collapse with the Expand/Collapse icon at the upper left. Space items are changed in More actions (•••) next to the space name > Space settings > General > Features. Space admins can add and reorder space shortcuts.

## Editor toolbar [S15]

Choice in "..." of the toolbar: fixed top toolbar, or inline toolbar shown when text is selected.

## Not in this layout (corrections)

The earlier draft showed a persistent right column with page info, versions, author, permissions and tags, a left sidebar with Dashboard and Templates, and a three-column Wiki Markup preview. None of these is confirmed by the current Cloud docs. See [changelog.md](../changelog.md).

## Typography, colour and spacing

See [themes/index.md](themes/index.md).

## Responsive and mobile

Not verified. The mobile apps are separate products; their layout is not documented in the sources read.

## Accessibility

Atlassian states that its design system tokens meet WCAG AA contrast ratios. [S18] Statement about Confluence's own UI: unverified.
