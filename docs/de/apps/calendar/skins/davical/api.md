# DAViCal – API (Version 1.1.13)

## Übersicht und Status

DAViCal ist ein CalDAV-/CardDAV-Server in PHP mit PostgreSQL. **Die API von DAViCal ist das DAV-Protokoll selbst** – es gibt keine REST-API. Diese Dokumentation basiert auf dem Quellcode des aktuellen Release **1.1.13 (11. Mai 2026)**; das Projekt wird aktiv weiterentwickelt (Debian-Paketierung 1.1.13-2, Mai 2026).

Versionshistorisch wichtig: Ein XML-RPC-Zugang, den manche Alt-Dokumentationen erwähnen, ist in den Release-Tags ab 0.9.9.8 bis heute **nicht enthalten** – aktuelle Administration läuft über Web-UI, Skripte und Datenbank.

**API-Oberflächen im Überblick (1.1.13)**

| Oberfläche | Zweck | Status |
|-----------|-------|--------|
| CalDAV (RFC 4791) | Kalender lesen/schreiben | offiziell |
| CardDAV (RFC 6352) | Adressbücher | offiziell |
| WebDAV + Sync (RFC 4918/6578) | Sammlungen, `sync-collection` | offiziell |
| RFC 3744 ACL | Rechteverwaltung | offiziell |
| Scheduling (RFC 6638) | Einladungen via Inbox/Outbox | offiziell |
| iSchedule (CalConnect, Draft 01) | signiertes Scheduling, Domain Keys | offiziell (aktiviert über `enable_scheduling`) |
| Tickets (draft-ito-dav-ticket-00) | tokenbasierte Freigaben | proprietäre Erweiterung |
| `BIND` | externe Kalender einbinden (Subscription) | proprietäre Erweiterung |
| Atom-Feed (`feed.php`) | Feed über Sammlungsänderungen | offiziell |
| FreeBusy (`freebusy.php`) | Belegungsabfrage per HTTP-Parameter | offiziell |
| Timezone-Service (`tz.php`) | VTIMEZONE-Lookup | offiziell |
| Prometheus-Metriken (`metrics.php`) | Monitoring | offiziell |
| Autodiscover | Outlook-/ActiveSync-Entdeckung | offiziell |
| REST-Admin-API / Webhooks | — | ❌ existieren nicht |

## DAV-Compliance (OPTIONS-Antwort)

Der Server sendet (Quelle: `htdocs/caldav.php`):

```
DAV: 1, 2, 3, access-control, calendar-access, calendar-schedule,
     extended-mkcol, bind, addressbook
```

Je nach Konfiguration zusätzlich: `calendar-auto-schedule` (wenn `enable_auto_schedule`) und `calendar-proxy` (standardmäßig aktiv, abschaltbar über `disable_caldav_proxy`). Öffentlich-lesbare Zugänge antworten reduziert mit `DAV: 1, 2, calendar-access`.

## Endpunkte und URL-Struktur

Front-Controller ist `caldav.php`; typische Apache-Konfiguration bindet DAViCal unter `/davical` ein:

| URL | Bedeutung |
|-----|-----------|
| `/.well-known/caldav` | `301` auf Principal-Wurzel |
| `/.well-known/carddav` | `301` auf Principal-Wurzel |
| `/.well-known/timezone` | `301` auf `tz.php` (mit Query-Parametern) |
| `/.well-known/…` (übrige) | iSchedule `GET`/`POST`, falls `enable_scheduling` |
| `/autodiscover/autodiscover.xml` | Autodiscover (Outlook) |
| `/davical/caldav.php/<user>/` | Principal (Standardpfad unter Serverwurzel) |
| `/davical/caldav.php/<user>/<calendar>/` | Kalender-/Adressbuch-Sammlung |
| `/davical/caldav.php/<user>/<proxy-user>/…` | Principal-Proxy-Zugriff (`calendar-proxy`) |
| `/davical/feed.php/<sammlung>/` | Atom-Feed der letzten Änderungen |
| `/davical/freebusy.php/<user>/?start=…&end=…` | FreeBusy als HTTP |
| `/davical/tz.php?action=…&tzid=…` | Timezone-Service (`urn:ietf:params:xml:ns:timezone-service`) |
| `/davical/metrics.php` | Prometheus-Format (`text/plain; version=0.4.0`) |

Apache-Rewrite-Beispiele aus dem Projekt mappen zusätzlich `/principals/users/…`, `/principals/resources/…`, `/calendars/__uids__/…` und `/addressbooks/__uids__/…` auf die Principal-Pfade.

## Authentifizierung

- **HTTP Basic** gegen Principal-Tabelle in PostgreSQL; optional per E-Mail-Adresse als Benutzerkennung (`by_email`)
- **Keine Tokens/OAuth** im Kern; alternative Auth-Treiber: LDAP (inkl. SASL-Binds und Gruppen-Sync), PAM, Kerberos/GSSAPI, externe PHP-Session; IMAP-Treiber wurde 2024 entfernt
- **Tickets** (`?ticket=…` im Query): befristete Zugangsberechtigungen ohne Login (siehe MKTICKET)
- Öffentlich-lesbare Sammlungen sind ohne Authentifizierung lesbar (`PublicSession`)

## Unterstützte HTTP-Methoden (pro Sammlungstyp)

Grundmenge: `OPTIONS`, `PROPFIND`, `REPORT`, `DELETE`, `LOCK`, `UNLOCK`, `MOVE`.

| Methode | Gilt für | Zweck |
|---------|----------|-------|
| `GET`, `HEAD`, `PUT` | Kalender, Adressbücher, Inbox | Objekt (`<uid>.ics`/`.vcf`) lesen/schreiben; `PUT` unterscheidet `text/calendar`, `text/vcard`, `text/x-vcard` |
| `POST` | Schedule-Outbox | iMIP-/iSchedule-Versand; auch `POST` mit `text/vcard` oder `add-member` |
| `PROPPATCH` | Principal, Kalender | Displayname, Farbe, Rechte-Eigenschaften |
| `MKCOL`, `MKCALENDAR` | Principal-/Collection-Ebene | Sammlungen anlegen (`extended-mkcol`) |
| `ACL` | Kalender, Collections, Principal | RFC-3744-Rechte setzen |
| `MKTICKET`, `DELTICKET` | Kalender, Collections, Outbox | Ticket erzeugen/löschen |
| `BIND` | Principal, Collections | externe Sammlungs-Subscription |

## Unterstützte REPORTs

| REPORT | Namespace |
|--------|-----------|
| `calendar-query`, `calendar-multiget`, `free-busy-query` | `urn:ietf:params:xml:ns:caldav` |
| `addressbook-query`, `addressbook-multiget` | `urn:ietf:params:xml:ns:carddav` |
| `sync-collection` (RFC 6578, Sync-Token) | `DAV:` |
| `principal-property-search`, `principal-search-property-set`, `principal-match`, `expand-property` | `DAV:` |

Unbekannte REPORT-Typen antworten mit `403 Precondition Failed` auf `DAV::supported-report`.

## Beispiel: Ereignis anlegen

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

Antwort `201 Created` mit `ETag`; Änderungen laufen über `PUT` mit `If-Match`, Löschungen über `DELETE`.

## Beispiel: MKTICKET (tokenbasierter Zugang)

Folgt dem eingestellten Draft `draft-ito-dav-ticket-00` (Xythos/Cosmo-Variante, Namespace `http://www.xythos.com/namespaces/StorageServer`):

```xml
<ticketinfo xmlns="http://www.xythos.com/namespaces/StorageServer">
  <timeout>Seconds-3600</timeout>
  <visits>Unlimited</visits>
  <privilege><read/></privilege>
</ticketinfo>
```

Antwort enthält eine Ticket-URL (`…?ticket=<id>`); Ablaufoptionen wie `Seconds-3600`, `Uses-10`. Standardprivileg ohne Angabe: `read-free-busy`. Benötigt `DAV::bind`-Recht.

## Administration (keine API)

- **Web-UI**: `index.php` (Web-Calender/Login), `admin.php` (Benutzer, Kollektionen, Rechte, Einstellungen), `setup.php`, `upgrade.php`, `tools.php`, `help.php`
- **Skripte/CLI**: `dba/update-davical-database`, `dba/create-database.sh`, `scripts/davical-cli` (Perl), `scripts/load_calendar.php`, `export_calendar.php`, `sync-remote-caldav.php`, `cron-sync-ldap.php`, `archive-old-events.php`, `refresh-alarms.php`, `tz-update.php`
- Ein programmatischer Fernwartungs-Endpunkt (REST/XML-RPC) existiert in 1.1.13 nicht

## Rate Limits und Metriken

- Eingebaute Rate Limits: ❌ (nur Credential-Erfolg/Fehler-Caching seit 2024); Schutz über Reverse Proxy (nginx `limit_req`) und Fail2ban
- `metrics.php` liefert Prometheus-Metriken; Zugriff absicherbar über `metrics_collectors` (IP-Whitelist) und `metrics_require_user`; Stil via `metrics_style` (`counters`/`memcache`/`both`)

## Clients und SDKs

- **Python**: `caldav`, `vdirsyncer`, `khal`
- **Android**: DAVx⁵ (vom Projekt gepflegt mitgetestet)
- **Desktop**: Thunderbird (Thunderbird-eigenes CalDAV/CardDAV), Evolution, Kalendar, Apple Kalender/Kontakte
- **PHP**: AWL-Bibliotheken des Projekts (`XMLDocument`, `DAVResource`); CalDAV-Client-Klassen `inc/caldav-client.php`
- **JS/Rohe Zugriffe**: `fetch` mit DAV-Methoden (`PROPFIND`/`REPORT`), da keine SDKs gepflegt werden

## Skin-Hinweis

FreeSynergy-Skins mit DAViCal-Backend sprechen exakt diese RFC-Endpunkte; Datenmodelle: [Event-Modell](../../../../data/modelle.md), [ICS-Format](../../../../data/formate.md).
