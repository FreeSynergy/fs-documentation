# DAViCal – API (version 1.1.13)

## Overview and status

DAViCal is a CalDAV/CardDAV server in PHP with PostgreSQL. **DAViCal's API is the DAV protocol itself** — there is no REST API. This documentation is based on the source code of the current release **1.1.13 (11 May 2026)**; the project is under active development (Debian packaging 1.1.13-2, May 2026).

Historically important: an XML-RPC access mentioned by some older documentation is **not included** in the release tags from 0.9.9.8 to this day — current administration runs through the web UI, scripts and the database.

**API surfaces at a glance (1.1.13)**

| Surface | Purpose | Status |
|---------|---------|--------|
| CalDAV (RFC 4791) | read/write calendars | official |
| CardDAV (RFC 6352) | address books | official |
| WebDAV + Sync (RFC 4918/6578) | collections, `sync-collection` | official |
| RFC 3744 ACL | permission management | official |
| Scheduling (RFC 6638) | invitations via inbox/outbox | official |
| iSchedule (CalConnect, Draft 01) | signed scheduling, domain keys | official (enabled via `enable_scheduling`) |
| Tickets (draft-ito-dav-ticket-00) | token-based grants | proprietary extension |
| `BIND` | include external calendars (subscription) | proprietary extension |
| Atom feed (`feed.php`) | feed over collection changes | official |
| FreeBusy (`freebusy.php`) | occupancy query via HTTP parameters | official |
| Timezone service (`tz.php`) | VTIMEZONE lookup | official |
| Prometheus metrics (`metrics.php`) | monitoring | official |
| Autodiscover | Outlook/ActiveSync discovery | official |
| REST admin API / webhooks | — | ❌ do not exist |

## DAV compliance (OPTIONS response)

The server sends (source: `htdocs/caldav.php`):

```
DAV: 1, 2, 3, access-control, calendar-access, calendar-schedule,
     extended-mkcol, bind, addressbook
```

Depending on configuration, additionally: `calendar-auto-schedule` (if `enable_auto_schedule`) and `calendar-proxy` (enabled by default, can be switched off with `disable_caldav_proxy`). Publicly readable accesses respond in reduced form with `DAV: 1, 2, calendar-access`.

## Endpoints and URL structure

The front controller is `caldav.php`; a typical Apache configuration mounts DAViCal under `/davical`:

| URL | Meaning |
|-----|---------|
| `/.well-known/caldav` | `301` to the principal root |
| `/.well-known/carddav` | `301` to the principal root |
| `/.well-known/timezone` | `301` to `tz.php` (with query parameters) |
| `/.well-known/…` (remaining) | iSchedule `GET`/`POST`, if `enable_scheduling` |
| `/autodiscover/autodiscover.xml` | autodiscover (Outlook) |
| `/davical/caldav.php/<user>/` | principal (default path under the server root) |
| `/davical/caldav.php/<user>/<calendar>/` | calendar/address book collection |
| `/davical/caldav.php/<user>/<proxy-user>/…` | principal proxy access (`calendar-proxy`) |
| `/davical/feed.php/<sammlung>/` | Atom feed of the recent changes |
| `/davical/freebusy.php/<user>/?start=…&end=…` | FreeBusy over HTTP |
| `/davical/tz.php?action=…&tzid=…` | timezone service (`urn:ietf:params:xml:ns:timezone-service`) |
| `/davical/metrics.php` | Prometheus format (`text/plain; version=0.4.0`) |

Apache rewrite examples from the project additionally map `/principals/users/…`, `/principals/resources/…`, `/calendars/__uids__/…` and `/addressbooks/__uids__/…` onto the principal paths.

## Authentication

- **HTTP Basic** against the principal table in PostgreSQL; optionally by e-mail address as the user identifier (`by_email`)
- **No tokens/OAuth** in the core; alternative auth drivers: LDAP (incl. SASL binds and group sync), PAM, Kerberos/GSSAPI, external PHP session; the IMAP driver was removed in 2024
- **Tickets** (`?ticket=…` in the query): time-limited access rights without login (see MKTICKET)
- Publicly readable collections can be read without authentication (`PublicSession`)

## Supported HTTP methods (per collection type)

Base set: `OPTIONS`, `PROPFIND`, `REPORT`, `DELETE`, `LOCK`, `UNLOCK`, `MOVE`.

| Method | Applies to | Purpose |
|--------|------------|---------|
| `GET`, `HEAD`, `PUT` | calendars, address books, inbox | read/write the object (`<uid>.ics`/`.vcf`); `PUT` distinguishes `text/calendar`, `text/vcard`, `text/x-vcard` |
| `POST` | schedule outbox | iMIP/iSchedule delivery; also `POST` with `text/vcard` or `add-member` |
| `PROPPATCH` | principal, calendar | display name, colour, permission properties |
| `MKCOL`, `MKCALENDAR` | principal/collection level | create collections (`extended-mkcol`) |
| `ACL` | calendars, collections, principal | set RFC 3744 permissions |
| `MKTICKET`, `DELTICKET` | calendars, collections, outbox | create/delete ticket |
| `BIND` | principal, collections | external collection subscription |

## Supported REPORTs

| REPORT | Namespace |
|--------|-----------|
| `calendar-query`, `calendar-multiget`, `free-busy-query` | `urn:ietf:params:xml:ns:caldav` |
| `addressbook-query`, `addressbook-multiget` | `urn:ietf:params:xml:ns:carddav` |
| `sync-collection` (RFC 6578, sync token) | `DAV:` |
| `principal-property-search`, `principal-search-property-set`, `principal-match`, `expand-property` | `DAV:` |

Unknown REPORT types answer with `403 Precondition Failed` on `DAV::supported-report`.

## Example: creating an event

```http
PUT /davical/caldav.php/anna/work/standup-2026-11-02.ics HTTP/1.1
Host: dav.example.org
If-None-Match: *
Content-Type: text/calendar; charset=utf-8

BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//FreeSynergy//DE
BEGIN:VEVENT
UID:standup-2026-11-02
DTSTAMP:20261031T100000Z
DTSTART:20261102T090000Z
DTEND:20261102T091500Z
SUMMARY:Tages-Standup
END:VEVENT
END:VCALENDAR
```

Response `201 Created` with an `ETag`; changes go through `PUT` with `If-Match`, deletions through `DELETE`.

## Example: MKTICKET (token-based access)

Follows the configured draft `draft-ito-dav-ticket-00` (Xythos/Cosmo variant, namespace `http://www.xythos.com/namespaces/StorageServer`):

```xml
<ticketinfo xmlns="http://www.xythos.com/namespaces/StorageServer">
  <timeout>Seconds-3600</timeout>
  <visits>Unlimited</visits>
  <privilege><read/></privilege>
</ticketinfo>
```

The response contains a ticket URL (`…?ticket=<id>`); expiry options such as `Seconds-3600`, `Uses-10`. Default privilege if none is given: `read-free-busy`. Requires the `DAV::bind` right.

## Administration (no API)

- **Web UI**: `index.php` (web calendar/login), `admin.php` (users, collections, permissions, settings), `setup.php`, `upgrade.php`, `tools.php`, `help.php`
- **Scripts/CLI**: `dba/update-davical-database`, `dba/create-database.sh`, `scripts/davical-cli` (Perl), `scripts/load_calendar.php`, `export_calendar.php`, `sync-remote-caldav.php`, `cron-sync-ldap.php`, `archive-old-events.php`, `refresh-alarms.php`, `tz-update.php`
- A programmatic remote-maintenance endpoint (REST/XML-RPC) does not exist in 1.1.13

## Rate limits and metrics

- Built-in rate limits: ❌ (only credential success/failure caching since 2024); protection via reverse proxy (nginx `limit_req`) and Fail2ban
- `metrics.php` delivers Prometheus metrics; access can be secured with `metrics_collectors` (IP whitelist) and `metrics_require_user`; style via `metrics_style` (`counters`/`memcache`/`both`)

## Clients and SDKs

- **Python**: `caldav`, `vdirsyncer`, `khal`
- **Android**: DAVx⁵ (jointly tested with the project)
- **Desktop**: Thunderbird (Thunderbird's own CalDAV/CardDAV), Evolution, Merkuro, Apple Calendar/Contacts
- **PHP**: the project's AWL libraries (`XMLDocument`, `DAVResource`); CalDAV client classes in `inc/caldav-client.php`
- **JS/raw access**: `fetch` with DAV methods (`PROPFIND`/`REPORT`), since no SDKs are maintained

## Frontend note

FreeSynergy frontends with a DAViCal backend address exactly these RFC endpoints; data models: [Event model](../../../../../../data/models.md), [ICS format](../../../../../../data/formats.md).
