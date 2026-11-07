# Wiki.js 3.1.1 — events

Events that leave the wiki, and live updates inside the UI. The old page's webhook list (`page.create`, `page.update`, `page.move`, `page.revert`, …) is wrong for 3.1.1. The real names are below.

## Outgoing webhooks

Configured in Admin → Webhooks. Each webhook has a URL, a list of events, and an optional authorization header. Delivery is an HTTP POST with a JSON body. Source: `backend/models/hooks.ts`, `HOOK_EVENTS` (https://github.com/requarks/wiki/blob/3.1.1/backend/models/hooks.ts).

### Event names (the 14 in `HOOK_EVENTS`)

| Event | Emitted when | Emit call sites (count) |
|-------|--------------|-------------------------|
| `page:create` | a page is created | 2 |
| `page:edit` | a page's content is saved | 1 |
| `page:rename` | a page is moved or renamed | 1 |
| `page:delete` | a page is deleted | 2 |
| `asset:upload` | a file is uploaded | 2 |
| `asset:edit` | a file is edited | 1 |
| `asset:rename` | a file is renamed | 1 |
| `asset:delete` | a file is deleted | 2 |
| `comment:new` | a comment is posted | 2 |
| `comment:edit` | a comment is edited | 1 |
| `comment:delete` | a comment is deleted | 2 |
| `user:join` | a user account is created | 1 |
| `user:login` | a user logs in | 1 |
| `user:logout` | a user logs out | 1 |

The comment in `hooks.ts` says every event has an `emit()` call in the server. The counts above come from a grep over the server source; they are call-site counts, not behaviour tests.

### Payload

```
{ "hookId": <id>, "event": "<event name>", "data": { ... }, "instance": <instance id> }
```

Source: `backend/models/hooks.ts` (`payload: { hookId, event, data, instance }`). The shape of `data` depends on the event; per-event data was not read.

### Delivery

| Property | Value | Source |
|----------|-------|--------|
| Method | POST | `hooks.ts` |
| Content type | `application/json` | `hooks.ts` |
| User-Agent | `Wiki.js/<version>` | `hooks.ts` |
| Authorization | copied from the webhook's `authHeader` setting when set | `hooks.ts` |
| Signature header | none found | `hooks.ts` |
| Retry policy | not read | — |
| Delivery status | stored per webhook (`hooks.ts`, "recording the outcome on the webhook") | `hooks.ts` |
| TLS | an option to accept untrusted certificates exists (`acceptUntrusted`) | `hooks.ts` |

Note for us: no signature means a receiver must rely on the authorization header or a private network.

## Notification categories (inside the wiki)

These feed the inbox and mail, not external systems. Source: `backend/notifications/categories/`.

| Category file | Meaning |
|---------------|---------|
| `pageCreated` | new page |
| `pageDeleted` | deleted page |
| `pageLifecycle` | lifecycle rule event |
| `watchedPage` | change on a watched page |
| `watchedPageComment` | comment on a watched page |
| `commentReply` | reply to a comment |
| `mention` | a user was mentioned |
| `reviewRequested` | a review was requested |
| `feedbackStatus` | a feedback idea changed status |

Users can switch categories off (`ProfileNotifications.vue`, `AdminNotifications.vue`).

## Live updates in the UI

| Feature | Transport | Source |
|---------|-----------|--------|
| Collaborative editing (Markdown, Visual, Excalidraw) | websocket with Yjs | `backend/controllers/collab.ts`, `frontend/src/composables/collab.js`, `frontend/src/editor/visual/collab.js`, `frontend/src/editor/excalidraw/collab.js` |
| Live cursors and "recent edits" marks | same websocket (awareness) | release notes of 3.0.0-beta.705 ("show live cursors only on hover + dotted underline for recent edits"), https://github.com/requarks/wiki/releases/tag/3.0.0-beta.705 |
| Notification badge in the header | fetched; push not verified | `HeaderNav.vue` (`notificationsStore.badge`) |
| Multi-instance coordination | Postgres LISTEN/NOTIFY on separate channels (collab) and the event bus | `backend/index.ts` comment, `backend/core/db.ts` |

No server-sent events endpoint was found. Unverified: whether the notification badge refreshes by polling.

## What we can learn for our frontend

- Use the same event names as Wiki.js only if we want to be compatible. Our own contract (`fs-interfaces/schema/texts.capnp`) uses `subscribe` with a `ChangeListener` and a `Change` union of `created`, `updated`, `deleted` (`common.capnp`). See `dependencies.md`.
- A webhook without a signature needs the authorization header or a private network. Our own design should add a signature.
