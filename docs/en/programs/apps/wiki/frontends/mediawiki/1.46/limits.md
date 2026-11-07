# MediaWiki 1.46 — Limits

Version: 1.46.2. Sources as given per row. "Config" means `includes/config-schema.php` at REL1_46 (https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/config-schema.php).

## Rate limits (write actions, core defaults)

Config key: `$wgRateLimits`, format `action => [ group => [ count, seconds ] ]`. Source: config-schema.php key `RateLimits`.

| Action | Group | Limit (count per seconds) |
|--------|-------|---------------------------|
| edit | ip | 8 per 60 s |
| edit | newbie | 8 per 60 s |
| edit | user | 90 per 60 s |
| move | newbie | 2 per 120 s |
| move | user | 8 per 60 s |
| upload | ip | 8 per 60 s |
| upload | newbie | 8 per 60 s |
| rollback | user | 10 per 60 s |

Other actions are listed in the same config key (mailpassword, sendemail, changeemail, purge, linkpurge, renderfile, stashedit, changetags, import and others). Only the rows above were read in full. The `RateLimitsExcludedIPs` key lists IPs exempt from limits.

Notes:
- The existing page's `$wgRateLimitLog`, `$wgUserRateLimit` and "50 requests per second per IP" are not in the config schema. See `../changelog.md`.
- Read requests: no default read limit found in the config schema. The API:Etiquette page says there is no hard speed limit on read requests but asks clients not to overload the site (summary-only).
- Exceeding a limit returns the error code `ratelimited` (`includes/Api/ApiBase.php`, mapped to `apierror-ratelimited`).

## Replication lag (maxlag)

- Clients may pass `maxlag=<seconds>`. If the lag is higher, the request is refused with error `maxlag`, and the response has a `Retry-After` header (`includes/Api/ApiMain.php`, `checkMaxLag`). Retry-After is at least 5 seconds.
- Use `maxlag` for bots and batch jobs, not for interactive use (API:Etiquette, summary-only).

## Size and time limits

Not checked in this run. Known, unverified defaults that the existing page did not mention are not listed here.

## Known functional limits (verified)

| Limit | Source |
|-------|--------|
| Recent changes list: `rclimit` max 500, default 10 | https://www.mediawiki.org/wiki/API:RecentChanges |
| Watchlist: `wlallrev` merges revisions per page in the timeframe | https://www.mediawiki.org/wiki/API:Watchlist |
| Watchlist labels off by default (`$wgEnableWatchlistLabels` = false) | RELEASE-NOTES-1.46 |
| Bot passwords per user: `$wgBotPasswordsLimit` default 100 | RELEASE-NOTES-1.46 |
| User JS preferences per user: `$wgUserJsPrefLimit` default 100 | RELEASE-NOTES-1.46 |
| Legacy PHP/DB minimums: PHP 8.3.0+, MariaDB 10.3+, MySQL 5.7+, PostgreSQL 10+, SQLite 3.8+ | RELEASE-NOTES-1.46 (Compatibility) |
| Upgrades from older than 1.39 need steps through LTS versions | https://www.mediawiki.org/wiki/Version_lifecycle |

## Support limits

- Stable: 1.46 (end of life July 2027). LTS: 1.43 (end of life December 2027). 1.47 LTS expected November 2026 (end of life November 2029). Source: https://www.mediawiki.org/wiki/Version_lifecycle
- Versions not in the lifecycle table receive no security fixes (same source).
