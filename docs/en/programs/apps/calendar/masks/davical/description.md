# DAViCal – Description

## What the program does

DAViCal is a CalDAV/CardDAV server in PHP that stores calendar and contact data in **PostgreSQL** and serves it to standard clients over the open DAV protocol (RFC 4791/6352). It is primarily a backend, but also ships a plain web interface (a web calendar for viewing/editing), web administration, and built-in timezone, FreeBusy and feed services. Events, tasks (VTODO), journals (VJOURNAL) and contacts are kept in the database as ICS/vCard objects with a change history (sync token).

## Benefits

- **Database-centred**: PostgreSQL as the store — referential integrity, SQL access for reporting, clean migration/backup path
- **Fine-grained permissions**: real RFC 3744 ACLs, principal proxy (calendar delegation), groups, publicly readable collections, and ticket URLs for access without login
- **Calendar subscription & inclusion**: `BIND` incorporates foreign calendars as subscribed collections
- **Scheduling included**: inbox/outbox (RFC 6638), automatic inviting, plus signed iSchedule (domain keys) — only a few open-source servers offer this
- **Mature and maintained**: developed since 2006/2007, release 1.1.13 (May 2026), packaged in Debian/Arch/Gentoo
- **Genuinely open source**: GPL v2 (individual parts v3), no cloud dependency

## How it differs

| System | Difference |
|--------|------------|
| **Baïkal** | Uses a maintained fork of the DAViCal core, targets SQLite/a single admin account and provides **no** web frontend of its own; DAViCal itself is the complete server including web calendar, ACLs and scheduling |
| **Radicale** | Python, per-calendar ICS files on the filesystem; simpler, but without SQL reporting and without DAViCal's own extensions (tickets, BIND, proxy) |
| **Nextcloud (CalDAV app)** | Suite with files/web UI; DAViCal is the lean pure DAV service for infrastructure that needs calendar data as standardised models |
| **Xandio Enterprise Server** | Java, commercial ticket, Outlook/Windows integration; DAViCal is lighter and community-driven |

## Technical details

- **Language/frameworks**: PHP 8.x (setup checks the PHP version; PHP 8.2 compatible since 1.1.13), built on the AWL library (Andrew's Web Library)
- **Database**: PostgreSQL (8.2+), schema including principal, collection, resource and change-history tables (`dba/davical.sql`, `update-davical-database`)
- **Frontend**: server-rendered PHP UI for the web calendar (`index.php`) and administration (`admin.php`)
- **Authentication**: HTTP Basic; drivers for the local DB, LDAP (SASL, group sync), PAM, Kerberos/GSSAPI, external session
- **Hosting**: Apache/nginx + PHP-FPM, standard Apache config with alias `/davical` in the project; TLS via reverse proxy
- **Licence**: GPL v2 or later (individual components v3)

## Who it suits

- Self-hosters, associations, families and small to medium teams running calendars/contacts with real partial permissions
- Environments with PostgreSQL infrastructure that want to evaluate calendar data via SQL
- FreeSynergy scenarios that need standardised ICS/vCard models with scheduling and calendar subscriptions
