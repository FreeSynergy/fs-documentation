# DAViCal – Structure (as of 1.1.13)

## Request flow

```
Client (Thunderbird/Merkuro/DAVx⁵/Apple)
   │  HTTPS, HTTP Basic
   ▼
Apache/nginx (alias /davical, rewrites for /.well-known & /principals)
   ▼
htdocs/caldav.php  ── front controller for everything DAV-related
   ├─ always.php        → load configuration, logging
   ├─ HTTPAuthSession   → authentication (DB/LDAP/PAM/Kerberos/session)
   ├─ CalDAVRequest     → gather path/method, send DAV headers
   └─ inc/caldav-<METHOD>.php → PROPFIND, REPORT-<type>, PUT-<format>, …
   ▼
PostgreSQL (objects, permissions, sync history)
```

Secondary entry points: `public.php` (anonymous, only publicly readable collections), `feed.php`, `freebusy.php`, `tz.php`, `metrics.php`, `autodiscover-handler.php`, `well-known.php` (incl. iSchedule).

## Directories of the source tree

| Directory | Contents |
|-----------|----------|
| `htdocs/` | front controllers (`caldav.php`, `admin.php`, `index.php`, `setup.php`, `upgrade.php`, `tools.php`), CSS/JS |
| `inc/` | method/REPORT handlers (`caldav-*.php`), sessions, principal/resource classes, drivers (`drivers_ldap.php` …), `ui/` for browser/editor pages |
| `dba/` | PostgreSQL schema (`davical.sql`), patches, `update-davical-database`, `create-database.sh` |
| `config/` | Apache example (`apache-davical.conf`), `example-config.php` |
| `scripts/` | CLI: LDAP sync, calendar import/export, alarm/timezone maintenance, `davical-cli` |
| `zonedb/`, `po/` | timezone data, translations |

## Configuration

On startup the host searches in order:
`/etc/davical/<SERVER_NAME>-conf.php` → `/etc/davical/config.php` → `/usr/local/etc/davical/…`
The template is `config/example-config.php` (object `$c`: database, auth drivers, scheduling, bind, metrics, debug).

## PostgreSQL schema (excerpt)

- **Principals**: `principal`, `principal_type` (user/resource/group/room), `group_member`
- **Collections/objects**: `collection`, `caldav_data` (raw ICS/vCard data), `calendar_item` (parsed, for REPORTs), `addressbook_resource`, `property`, `locks`
- **Permissions**: `grants` (ACL bits incl. scheduling privileges)
- **Sync**: `sync_tokens`, `sync_changes` (CTag/sync-token history)
- **Tickets**: `access_ticket`, `freebusy_ticket`
- **Bind subscriptions**: `dav_binding`
- **Timezones**: `timezones`, `tz_aliases`, `tz_localnames`

Migration: `dba/update-davical-database` applies the patches under `dba/patches/` automatically.

## Deployment forms

- **Apache + PHP-FPM** (reference): `Alias /davical /usr/share/davical/htdocs` plus the bundled rewrite rules; CSP headers for UI pages already in the example
- **nginx + PHP-FPM**: common (equivalent to the Apache alias); DAV methods must be passed through to the PHP script
- **Debian/Ubuntu**: package `davical` (1.1.13-2 as of May 2026), local PostgreSQL use is typical; Gentoo Sunrise and an Arch wiki guide exist
- TLS always via reverse proxy; no token/OAuth stack of its own
