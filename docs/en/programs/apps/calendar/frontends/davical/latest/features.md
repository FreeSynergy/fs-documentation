# DAViCal – Features (as of 1.1.13)

## Calendar and contact data

- **CalDAV (RFC 4791)**: calendars as collections, objects as `<uid>.ics`
- **CardDAV (RFC 6352)**: address books with `addressbook-query`/`addressbook-multiget`
- **Events, tasks, journals**: `VEVENT`, `VTODO`, `VJOURNAL` are stored in calendar collections and evaluated in REPORTs
- **Server-side recurrences**: RRULE expansion in PostgreSQL (`rrule_functions.sql`), date range 1–9999 AD
- **Synchronisation**: `sync-collection` (RFC 6578) with sync token, ETag/CTag, `calendar-multiget`
- **Change history** of the objects kept in the database

## Sharing and permissions

- **ACL per RFC 3744** (`ACL` method): rights per principal on collections and objects
- **Principal proxy** (`calendar-proxy`): calendar delegation, e.g. assistant ↔ boss
- **Groups** as a principal type; LDAP group sync possible
- **Resources**: principal types `ROOM` (since 1.1.13) among others for rooms/materials
- **Publicly readable collections**: read access without login
- **Tickets** (MKTICKET/DELTICKET per draft-ito-dav-ticket-00): time-limited/countable access URLs without authentication
- **Calendar subscription/BIND**: include `webcal://` and DAV foreign calendars as subscribed collections, auto-refresh (`external_refresh`, default 60 min), visibility per client controllable (`hide_bound`)

## Invitations (scheduling)

- **Inbox/outbox** per principal (RFC 6638), accept/decline via clients
- **Automatic inviting** (`enable_auto_schedule`, optional)
- **iSchedule** (CalConnect Draft 01, optional via `enable_scheduling`): server-to-server scheduling with signed messages (domain keys), `POST` against `/.well-known/`

## Additional services

- **FreeBusy**: `free-busy-query` REPORT and HTTP endpoint `freebusy.php` (parameters `start/end/period/user/format`), optionally public (`public_freebusy_url`)
- **Timezone service** `tz.php` with actions `capabilities/get/expand/list` plus redirect `/.well-known/timezone`; bundled zone database, updatable via `tz-update.php`
- **Atom feed** `feed.php` over the recent changes of a collection
- **Autodiscover** (`/autodiscover/autodiscover.xml`) for Outlook clients
- **Prometheus metrics** (`metrics.php`, IP whitelist/user protection)
- **Alarm values**: VALARMs are evaluated; `refresh-alarms.php` computes upcoming alarm times in the DB

## Administration

- **Web administration**: principal browser/editor (users, groups, resources), collection browser/editor, permission assignment, setup/upgrade pages
- **Authentication drivers**: local DB, LDAP (SASL binds, group sync, `cron-sync-ldap.php`), PAM, Kerberos/GSSAPI, external PHP session; HTTP Digest can be enforced optionally
- **CLI/maintenance**: `update-davical-database`, `davical-cli` (Perl), calendar import/export (`load_calendar.php`, `export_calendar.php`), counter reconciliation with remote peers (`sync-remote-caldav.php`), `archive-old-events.php`

## What DAViCal does NOT offer

- ❌ No REST/administration API and no webhooks (only DAV, web UI, scripts, DB)
- ❌ No WebDAV push/notifications (client polling)
- ❌ No OAuth/token-based login (only Basic/Digest/ticket)
- ❌ No built-in rate limiting (reverse proxy/Fail2ban needed)
- ❌ No full web calendar as a client replacement: the web UI is a browser/editor for principals and collections; the clients do the event work
- ❌ The Apple `calendarserver` sharing protocol is not implemented (sharing via ACL/proxy/tickets)
