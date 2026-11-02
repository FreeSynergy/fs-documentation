# DAViCal – Struktur (Stand 1.1.13)

## Request-Ablauf

```
Client (Thunderbird/Kalendar/DAVx⁵/Apple)
   │  HTTPS, HTTP Basic
   ▼
Apache/nginx (Alias /davical, Rewrites für /.well-known & /principals)
   ▼
htdocs/caldav.php  ── Front-Controller für alles DAV-mäßige
   ├─ always.php        → Konfiguration laden, Logging
   ├─ HTTPAuthSession   → Authentifizierung (DB/LDAP/PAM/Kerberos/Session)
   ├─ CalDAVRequest     → Pfad/Methode sammeln, DAV-Header senden
   └─ inc/caldav-<METHODE>.php → PROPFIND, REPORT-<typ>, PUT-<format>, …
   ▼
PostgreSQL (Objekte, Rechte, Sync-Historie)
```

Nebeneinstiege: `public.php` (anonym, nur öffentlich lesbare Sammlungen), `feed.php`, `freebusy.php`, `tz.php`, `metrics.php`, `autodiscover-handler.php`, `well-known.php` (inkl. iSchedule).

## Verzeichnisse des Quellbaums

| Verzeichnis | Inhalt |
|-------------|--------|
| `htdocs/` | Front-Controller (`caldav.php`, `admin.php`, `index.php`, `setup.php`, `upgrade.php`, `tools.php`), CSS/JS |
| `inc/` | Methoden-/REPORT-Handler (`caldav-*.php`), Sessionen, Principal-/Ressourcenklassen, Treiber (`drivers_ldap.php` …), `ui/` für Browser/Editor-Seiten |
| `dba/` | PostgreSQL-Schema (`davical.sql`), Patches, `update-davical-database`, `create-database.sh` |
| `config/` | Apache-Beispiel (`apache-davical.conf`), `example-config.php` |
| `scripts/` | CLI: LDAP-Sync, Kalender-Import/Export, Alarm-/TZ-Pflege, `davical-cli` |
| `zonedb/`, `po/` | Zeitzonendaten, Übersetzungen |

## Konfiguration

Der Rechner sucht beim Start der Reihe nach:
`/etc/davical/<SERVER_NAME>-conf.php` → `/etc/davical/config.php` → `/usr/local/etc/davical/…`
Vorlage ist `config/example-config.php` (Objekt `$c`: Datenbank, Auth-Treiber, Scheduling, Bind, Metriken, Debug).

## PostgreSQL-Schema (Auszug)

- **Principals**: `principal`, `principal_type` (Benutzer/Ressource/Gruppe/Raum), `group_member`
- **Sammlungen/Objekte**: `collection`, `caldav_data` (ICS/vCard-Rohdaten), `calendar_item` (parset, für REPORTs), `addressbook_resource`, `property`, `locks`
- **Rechte**: `grants` (ACL-Bits inkl. Scheduling-Privilegien)
- **Sync**: `sync_tokens`, `sync_changes` (CTag-/Sync-Token-Historie)
- **Tickets**: `access_ticket`, `freebusy_ticket`
- **Bind-Abos**: `dav_binding`
- **Zeitzonen**: `timezones`, `tz_aliases`, `tz_localnames`

Migration: `dba/update-davical-database` wendet die Patches unter `dba/patches/` automatisch an.

## Deployment-Formen

- **Apache + PHP-FPM** (Referenz): `Alias /davical /usr/share/davical/htdocs` plus die mitgelieferten Rewrite-Regeln; CSP-Header für UI-Seiten bereits im Beispiel
- **nginx + PHP-FPM**: üblich (entspricht dem Apache-Alias); DAV-Methoden müssen ans PHP-Skript durchgereicht werden
- **Debian/Ubuntu**: Paket `davical` (1.1.13-2 Stand Mai 2026), PostgreSQL-Lokalnutzung typisch; Gentoo-Sunrise, Arch-Wiki-Anleitung vorhanden
- TLS immer über Reverse Proxy; kein eigener Token/OAuth-Stack
