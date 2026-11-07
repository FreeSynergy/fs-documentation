# Confluence (Cloud, latest) · Events (webhooks)

Sources: S-numbers refer to [index.md](../index.md).

Two systems. Forge is the current one. Connect webhooks are legacy and Atlassian says new extensibility is delivered only on Forge. [S11]

## 1. Forge events (current) [S10]

Event names are `avi:confluence:<action>:<object>`. Payloads are mostly full objects (not IDs). Users are identified by `accountId`.

| Object | Events |
|--------|--------|
| Page / live doc / blog post | `created:page`, `updated:page`, `liked:page`, `viewed:page`, `archived:page`, `unarchived:page`, `moved:page`, `copied:page`, `children_reordered:page`, `permissions_updated:page`, `trashed:page`, `restored:page`, `deleted:page`; live docs: `initialized:page`, `started:page`, `snapshotted:page`, `published:page`; blog posts: `created:blogpost`, `updated:blogpost`, `liked:blogpost`, `viewed:blogpost`, `permissions_updated:blogpost`, `trashed:blogpost`, `restored:blogpost`, `deleted:blogpost` |
| Whiteboard | `created:whiteboard`, `moved:whiteboard`, `copied:whiteboard`, `permissions_updated:whiteboard` |
| Database | `created:database`, `moved:database`, `copied:database`, `permissions_updated:database` |
| Folder | `created:folder`, `moved:folder`, `copied:folder`, `permissions_updated:folder` |
| Smart link in tree | `created:embed`, `moved:embed`, `copied:embed` |
| Inline task | `created:task`, `updated:task`, `removed:task` (payload includes `oldTask` on update) |
| Comment | `created:comment`, `updated:comment`, `liked:comment`, `deleted:comment` |
| Space | `created:space:V2`, `updated:space:V2`, `permissions_updated:space:V2`, `deleted:space:V2` |
| Attachment | `created:attachment`, `updated:attachment`, `viewed:attachment`, `archived:attachment`, `unarchived:attachment`, `trashed:attachment`, `restored:attachment`, `deleted:attachment` |
| Custom content | `created:custom_content`, `updated:custom_content`, `permissions_updated:custom_content`, `trashed:custom_content`, `restored:custom_content`, `deleted:custom_content` |
| Label | `created:label`, `added:label`, `removed:label`, `deleted:label` |
| User | `created:user`, `deleted:user` |
| Group | `created:group`, `deleted:group` |
| Relation | `created:relation`, `deleted:relation` |
| Search | `performed:search` (query, accountType, result count; no content) |

Notes [S10]:
- Trashed and deleted events, and space permission events, need `write:confluence-content` or `write:confluence-space`.
- Cascading deletes do not emit one event per child.
- No beta or deprecation label is shown on Confluence events. The `:V2` suffix on space events is not explained.

Unverified: how a non-Forge frontend (for example our own server) would receive Forge events. Forge events run inside Forge apps on Atlassian's platform. A way to forward them to an external URL was not found in the pages read.

## 2. Connect webhooks (legacy) [S11]

Declared in the app descriptor `atlassian-connect.json` under `modules.webhooks`. Each entry has `event` (required), `url` (required, relative to the add-on baseUrl), `excludeBody` (default false), `filter` (optional), `conditions` (only `addon_is_licensed`), `propertyKeys` (Jira only). [S11]

Confluence event names listed in S11 (exact):

```
attachment_archived attachment_created attachment_removed attachment_restored
attachment_trashed attachment_unarchived attachment_updated attachment_viewed
blog_created blog_moved blog_removed blog_restored blog_trashed blog_updated blog_viewed
blueprint_page_created comment_removed
connect_addon_disabled connect_addon_enabled
content_created content_removed content_restored content_trashed content_updated content_permissions_updated
group_created group_removed
label_added label_created label_deleted label_removed
page_archived page_children_reordered page_created page_initialized page_copied page_moved
page_removed page_restored page_trashed page_unarchived page_updated page_started
page_snapshotted page_published page_viewed
relation_created relation_deleted search_performed
space_created space_logo_updated space_permissions_updated space_removed space_updated
theme_enabled user_reactivated user_removed
```

## 3. Earlier draft (removed)

The earlier `events.md`-equivalent listed `page.created`, `page.updated`, `page.deleted`, `comment.created`, `space.created` and the endpoint `POST /rest/webhooks/1.0/webhook`. None of these appears in the Cloud pages read. Removed. The `/rest/webhooks/1.0/` path belongs to Data Center (unverified detail).

## 4. Delivery notes [S9]

- 2026-10-16 announcement: new Atlassian IP ranges effective 2027-01-01. Requests from Atlassian, including webhooks, use these ranges. Allowlists must be updated before that date.
- 2026-09-25: Connect `uninstalled` lifecycle hook no longer fires when upgrading to a Forge-only version.

## Relevance for us

A live-update channel can use Forge events only if our integration runs as a Forge app or polls the REST API. Polling is subject to the points quota in [api.md](api.md).
