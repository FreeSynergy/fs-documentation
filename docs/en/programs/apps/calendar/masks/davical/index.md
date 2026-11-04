# DAViCal Documentation

## Overview

DAViCal is a CalDAV/CardDAV server written in PHP on PostgreSQL — a lean, protocol-faithful self-hosted calendar/contact store with web administration. For FreeSynergy it is the backend skin sitting behind Merkuro, Thunderbird, DAVx⁵ and Apple devices; maintained and actively developed (1.1.13, May 2026).

## File structure

- [description.md](description.md) - What DAViCal does, benefits, how it differs from Radicale/Nextcloud/Xandio
- [features.md](features.md) - CalDAV/CardDAV, ACLs, proxy, tickets, BIND subscriptions, scheduling, what it does NOT do
- [structure.md](structure.md) - Server layout: PHP/PostgreSQL, htdocs/schema, deployment
- [menu.md](menu.md) - Menu items of the web administration
- [shortcuts.md](shortcuts.md) - Keyboard shortcuts
- [api.md](api.md) - Exact API 1.1.13: DAV methods, REPORTs, endpoints, tickets, metrics

## Sources

Every statement in this section comes from the official source code of the current release:

| Source | Location / URL | Used for |
|--------|----------------|----------|
| Source release **r1.1.13** (2026-05-11) | `https://gitlab.com/api/v4/projects/davical-project%2Fdavical/repository/archive.tar.gz?ref=r1.1.13` | all files |
| GitLab project | `https://gitlab.com/davical-project/davical` (tags, ChangeLog) | version state, development active |
| `htdocs/caldav.php` | front controller, DAV headers, method dispatch | api.md, structure.md |
| `inc/DAVResource.php` | `FetchSupportedMethods`, `FetchSupportedReports` | api.md |
| `inc/interactive-page.php` | main menu Home/User Functions/Administration/Help | menu.md |
| `inc/ui/principal-*.php`, `collection-edit.php` | browser columns, editor fields, permission matrix | menu.md |
| `dba/davical.sql` | database tables | structure.md |
| `config/apache-davical.conf`, `config/example-config.php` | Apache deployment, configuration options, `/etc/davical/…` search path | structure.md, features.md |
| `inc/caldav-MKTICKET.php`, `caldav-BIND.php`, `well-known.php`, `iSchedule*.php` | tickets, BIND/webcal, Well-Known, iSchedule | api.md, features.md |
| `htdocs/metrics.php`, `freebusy.php`, `tz.php`, `feed.php` | metrics, FreeBusy, timezone and feed endpoints | api.md |
| `scripts/` and `dba/` | CLI/migration tools | shortcuts.md, structure.md |
| Debian package | `https://packages.debian.org/davical` (1.1.13-2, May 2026) | packaging, usage |
| DAViCal wiki | `https://wiki.davical.org/` (release notes) | version history |
| AWL library | `https://gitlab.com/davical-project/awl` | framework origin |

Research note: the XML-RPC API claimed by older third-party documentation is not contained in any release tag from 0.9.9.8 onwards (verified by source-code search, likewise in the AWL repository).
