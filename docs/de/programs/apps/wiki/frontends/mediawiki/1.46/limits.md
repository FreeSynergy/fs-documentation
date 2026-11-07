# MediaWiki 1.46 — Grenzwerte

Version: 1.46.2. Quellen je Zeile wie angegeben. "Konfiguration" meint `includes/config-schema.php` im REL1_46 (https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/config-schema.php).

## Ratenbegrenzungen (Schreibaktionen, Standardwerte des Kerns)

Konfigurationsschlüssel: `$wgRateLimits`, Format `action => [ group => [ count, seconds ] ]`. Quelle: config-schema.php, Schlüssel `RateLimits`.

| Aktion | Gruppe | Grenzwert (Anzahl pro Sekunden) |
|--------|--------|---------------------------------|
| edit | ip | 8 pro 60 s |
| edit | newbie | 8 pro 60 s |
| edit | user | 90 pro 60 s |
| move | newbie | 2 pro 120 s |
| move | user | 8 pro 60 s |
| upload | ip | 8 pro 60 s |
| upload | newbie | 8 pro 60 s |
| rollback | user | 10 pro 60 s |

Weitere Aktionen stehen im selben Konfigurationsschlüssel (mailpassword, sendemail, changeemail, purge, linkpurge, renderfile, stashedit, changetags, import und andere). Nur die oben genannten Zeilen wurden vollständig gelesen. Der Schlüssel `RateLimitsExcludedIPs` listet IPs auf, die von den Grenzwerten ausgenommen sind.

Hinweise:
- `$wgRateLimitLog`, `$wgUserRateLimit` und "50 Anfragen pro Sekunde pro IP" der bestehenden Seite sind im Konfigurationsschema nicht enthalten. Siehe `../changelog.md`.
- Leseanfragen: im Konfigurationsschema kein Standard-Lesegrenzwert gefunden. Die Seite API:Etiquette sagt, dass es bei Leseanfragen keine harte Geschwindigkeitsgrenze gibt, bittet Clients aber, die Seite nicht zu überlasten (nur Zusammenfassung).
- Eine Überschreitung liefert den Fehlercode `ratelimited` (`includes/Api/ApiBase.php`, zugeordnet zu `apierror-ratelimited`).

## Replikationsverzögerung (maxlag)

- Clients können `maxlag=<seconds>` übergeben. Ist die Verzögerung höher, wird die Anfrage mit dem Fehler `maxlag` abgelehnt, und die Antwort enthält einen Header `Retry-After` (`includes/Api/ApiMain.php`, `checkMaxLag`). Retry-After beträgt mindestens 5 Sekunden.
- `maxlag` für Bots und Stapelaufträge verwenden, nicht für interaktive Nutzung (API:Etiquette, nur Zusammenfassung).

## Größen- und Zeitgrenzen

In diesem Lauf nicht geprüft. Bekannte, nicht bestätigte Standardwerte, die die bestehende Seite nicht erwähnt hat, sind hier nicht aufgeführt.

## Bekannte funktionale Grenzen (geprüft)

| Grenzwert | Quelle |
|-----------|--------|
| Liste der letzten Änderungen: `rclimit` maximal 500, Standard 10 | https://www.mediawiki.org/wiki/API:RecentChanges |
| Beobachtungsliste: `wlallrev` fasst Versionen pro Seite im Zeitraum zusammen | https://www.mediawiki.org/wiki/API:Watchlist |
| Beobachtungsliste-Markierungen standardmäßig aus (`$wgEnableWatchlistLabels` = false) | RELEASE-NOTES-1.46 |
| Bot-Passwörter pro Benutzer: `$wgBotPasswordsLimit`, Standard 100 | RELEASE-NOTES-1.46 |
| JS-Einstellungen pro Benutzer: `$wgUserJsPrefLimit`, Standard 100 | RELEASE-NOTES-1.46 |
| Mindestanforderungen für PHP/DB früher: PHP 8.3.0+, MariaDB 10.3+, MySQL 5.7+, PostgreSQL 10+, SQLite 3.8+ | RELEASE-NOTES-1.46 (Compatibility) |
| Upgrades von Versionen vor 1.39 benötigen Schritte über LTS-Versionen | https://www.mediawiki.org/wiki/Version_lifecycle |

## Support-Grenzen

- Stabil: 1.46 (Ende der Lebensdauer Juli 2027). LTS: 1.43 (Ende der Lebensdauer Dezember 2027). 1.47 LTS wird für November 2026 erwartet (Ende der Lebensdauer November 2029). Quelle: https://www.mediawiki.org/wiki/Version_lifecycle
- Versionen, die nicht in der Lebenszyklustabelle stehen, erhalten keine Sicherheitskorrekturen (gleiche Quelle).
