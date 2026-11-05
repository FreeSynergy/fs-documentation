# DAViCal – Shortcuts (as of 1.1.13)

## Web interface

DAViCal **does not provide its own keyboard shortcuts** — the web interface (principal/collection browsers and editors) is classic server-rendered HTML with no key bindings (`accesskey`/`keydown` are absent from the code). The browser's own handling (Tab/Enter, browser shortcuts) applies unchanged.

## Direct URLs as "shortcuts"

Frequent pages can be reached directly via fixed URLs (base `/davical`):

| URL | Target |
|-----|--------|
| `/davical/index.php` | principal overview / login |
| `/davical/admin.php?action=browse&t=principal&type=1` | user list |
| `/davical/admin.php?action=browse&t=principal&type=3` | group list |
| `/davical/admin.php?action=edit&t=principal` | create a new principal |
| `/davical/admin.php?action=browse&t=external` | external calendar subscriptions (BIND) |
| `/davical/tools.php` | import / LDAP sync tools |
| `/davical/upgrade.php` | database migration |

## Maintenance one-liners (CLI)

```sh
dba/update-davical-database          # update the schema
scripts/tz-update.php                # refresh the timezones
scripts/sync-remote-caldav.php       # counter reconciliation with the remote peer
scripts/load_calendar.php datei.ics  # import a calendar
```

## Shortcuts in the calendars (client side)

The actual calendar shortcuts are provided by the client, not by DAViCal:

- **Thunderbird (CALENDAR tab)**: `D` day, `W` week, `M` month, `N`/`P` next/previous, `T` today, `Ctrl+N` new event
- **Merkuro**: `Ctrl+N` new event, paging with `←`/`→` in the month view
- **Apple Calendar**: `Cmd+N` new event, `Cmd+1..6` views
- **Evolution**: `Ctrl+2` calendar, `Ctrl+N` new event

All of these commands belong to the respective client and reach DAViCal only as ordinary CalDAV operations (`PUT`/`REPORT`).
