# MediaWiki 1.46 — Events to the outside

Version: 1.46.2. Sources as given per row.

MediaWiki core has no general webhook system. Options that exist:

| Mechanism | Scope | Status | Source |
|-----------|-------|--------|--------|
| Recent changes feed (RSS/Atom) | core | module `action=feedrecentchanges` exists; parameters not read | `includes/Api/ApiFeedRecentChanges.php`; feed config keys `Feed`, `FeedLimit` (50), `FeedCacheTimeout` (60), `FeedDiffCutoff` (32768) in `includes/config-schema.php` |
| RCFeeds (push of recent-change entries to a feed backend) | core, sysadmin config | config key `RCFeeds` exists in `includes/config-schema.php`; backend list not read | config-schema.php |
| EventStreams (SSE) | Wikimedia-operated public service, not MediaWiki core | public stream `https://stream.wikimedia.org/v2/stream/recentchange` | https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams (summary) |
| EventBus | MediaWiki extension that produces the events used by EventStreams | extension; not read | (EventStreams page says recent changes come from MediaWiki through EventBus) |
| Echo | extension: in-wiki notifications, web and email notifications, push settings | notifications, not webhooks | https://www.mediawiki.org/wiki/Extension:Echo |

## EventStreams (not core)

Source: https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams (read through summary).

- Transport: Server-Sent Events (SSE). `Accept: application/json` gives newline-delimited JSON.
- Streams: `recentchange`, `revision-create`; several streams can be combined with commas.
- Public endpoint: `https://stream.wikimedia.org/v2/stream/recentchange`. An internal endpoint exists for Wikimedia only.
- Connection timeout on the server: 15 minutes. Clients reconnect and resume with `Last-Event-ID`.
- No server-side filtering. Discard events with `meta.domain === 'canary'`.
- Intended for small-scale external tools. No numeric rate limit published.
- Our frontend does not depend on EventStreams. A self-hosted wiki would need its own event producer.

## Recent changes in the UI

- Recent changes page (`Special:RecentChanges`) and watchlist use the same data model. Source: https://www.mediawiki.org/wiki/API:RecentChanges and https://www.mediawiki.org/wiki/API:Watchlist.
- Polling is the normal way for a frontend to refresh the list. The config key `StructuredChangeFiltersLiveUpdatePollingRate` = 3 in `includes/config-schema.php` appears to set a polling interval for the Special:RecentChanges filter UI (name-based reading, not confirmed by a doc page). It is a polling setting, not a push channel.

## Not verified

- Whether any core hook can send an HTTP request to a configured URL on each edit. Not found in core; no webhook code path was read.
- Payload format of `action=feedrecentchanges` items.
