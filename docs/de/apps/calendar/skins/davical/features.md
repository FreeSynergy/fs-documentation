# DAViCal – Funktionen (Stand 1.1.13)

## Kalender- undkontaktdaten

- **CalDAV (RFC 4791)**: Kalender als Sammlungen, Objekte als `<uid>.ics`
- **CardDAV (RFC 6352)**: Adressbücher mit `addressbook-query`/`addressbook-multiget`
- **Termine, Aufgaben, Journale**: `VEVENT`, `VTODO`, `VJOURNAL` werden in Kalender-Sammlungen gespeichert und in REPORTs ausgewertet
- **Wiederholungen serverseitig**: RRULE-Expansion in PostgreSQL (`rrule_functions.sql`), Datumsbereich 1–9999 n. Chr.
- **Synchronisation**: `sync-collection` (RFC 6578) mit Sync-Token, ETag/CTag, `calendar-multiget`
- **Änderungshistorie** der Objekte in der Datenbank

## Teilen und Rechte

- **ACL nach RFC 3744** (`ACL`-Methode): Rechte je Principal auf Sammlungen und Objekte
- **Principal-Proxy** (`calendar-proxy`): Kalendervertretung, z. B. Assistent ↔ Chef
- **Gruppen** als Principal-Typ; LDAP-Gruppensync möglich
- **Ressourcen**: Principal-Typen `ROOM` (seit 1.1.13) u. a. für Räume/Material
- **Öffentlich lesbare Sammlungen**: Lesezugriff ohne Login
- **Tickets** (MKTICKET/DELTICKET nach draft-ito-dav-ticket-00): befristete/zählbare Zugangs-URLs ohne Authentifizierung
- **Kalender-Abo/BIND**: `webcal://`- und DAV-Fremdkalender als abonnierte Sammlungen einbinden, Auto-Refresh (`external_refresh`, Default 60 min), Einblendbarkeit je Client steuerbar (`hide_bound`)

## Einladungen (Scheduling)

- **Inbox/Outbox** je Principal (RFC 6638), Annahme/Ablehnung über Clients
- **Automatisches Inviten** (`enable_auto_schedule`, optional)
- **iSchedule** (CalConnect Draft 01, optional via `enable_scheduling`): server-zu-server Scheduling mit signierten Nachrichten (Domain Keys), `POST` gegen `/.well-known/`

## Zusätzliche Dienste

- **FreeBusy**: `free-busy-query` REPORT und HTTP-Endpoint `freebusy.php` (Parameter `start/end/period/user/format`), optional öffentlich (`public_freebusy_url`)
- **Zeitzone-Service** `tz.php` mit Aktionen `capabilities/get/expand/list` plus Redirect `/.well-known/timezone`; mitgeführte Zonedb, aktualisierbar per `tz-update.php`
- **Atom-Feed** `feed.php` über letzte Änderungen einer Sammlung
- **Autodiscover** (`/autodiscover/autodiscover.xml`) für Outlook-Clients
- **Prometheus-Metriken** (`metrics.php`, IP-Whitelist/Benutzerschutz)
- **Alarmwerte**: VALARMs werden ausgewertet; `refresh-alarms.php` berechnet anstehende Alarmzeitpunkte in der DB

## Verwaltung

- **Web-Administration**: Principal-Browser/-Editor (Benutzer, Gruppen, Ressourcen), Collection-Browser/-Editor, Rechtevergabe, Setup-/Upgrade-Seiten
- **Authentifizierungs-Treiber**: lokale DB, LDAP (SASL-Binds, Gruppen-Sync, `cron-sync-ldap.php`), PAM, Kerberos/GSSAPI, externe PHP-Session; HTTP-Digest optional erzwingerbar
- **CLI/Wartung**: `update-davical-database`, `davical-cli` (Perl), Kalender-Import/Export (`load_calendar.php`, `export_calendar.php`), Counter-Abgleich mit Gegenstellen (`sync-remote-caldav.php`), `archive-old-events.php`

## Was DAViCal NICHT bietet

- ❌ Keine REST-/Verwaltungs-API und keine Webhooks (nur DAV, Web-UI, Skripte, DB)
- ❌ Kein WebDAV-Push/Benachrichtigungen (Client-Polling)
- ❌ Kein OAuth/Login mit Tokens (nur Basic/Digest/Ticket)
- ❌ Keine eingebaute Ratenbegrenzung (Reverse Proxy/Fail2ban nötig)
- ❌ Kein vollständiger Web-Kalender als Client-Ersatz: Das Web-UI ist Browser/Editor für Principals und Sammlungen; Termine arbeiten die Clients
- ❌ Apple-`calendarserver`-Sharing-Protokoll wird nicht implementiert (Teilen über ACL/Proxy/Tickets)
