# Baïkal/Davical - API Dokumentation

## Übersicht

Die API von Baïkal/Davical **ist** das CalDAV-/CardDAV-Protokoll (RFC 4791/6352 über HTTP). Eine zusätzliche REST-Verwaltungs-API existiert nicht — Administration läuft über Web-UI und CLI. Genau diese Protokollreinheit macht den Server zum Referenz-Backend für standardisierte Kalender-/Kontaktdaten.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| CalDAV (PROPFIND/REPORT/PUT/DELETE) | Kalender lesen/schreiben | offiziell |
| CardDAV (PROPFIND/REPORT/PUT/DELETE) | Adressbücher | offiziell |
| WebDAV-Sync (RFC 6578) | inkrementelle Änderungen via Sync-Token | offiziell |
| REST-Admin-API | — | ❌ Nicht vorhanden (nur Web-UI/CLI) |
| Webhooks / Push | — | ❌ Nicht vorhanden |

## Authentifizierung

- **HTTP Basic** über TLS; Principal-Tabelle in der Datenbank
- Optional offene Registrierung (legt Principal über das Registrierungsformular an)
- Keine Token, kein OAuth — Passwörter gehören in den Client-Keyring

## Discovery und Basis-Endpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/.well-known/caldav` | Redirect auf Principal-URL |
| `GET` | `/.well-known/carddav` | Redirect auf Principal-URL |
| `PROPFIND` | `/` (Depth 0) | `current-user-principal` ermitteln |
| `PROPFIND` | `<principal>` (Depth 1) | `calendar-home-set`, `addressbook-home-set` |
| `PROPFIND` | `<calendar-home>` (Depth 1) | Kalenderliste: `displayname`, `calendar-color`, Rechte |
| `OPTIONS` | `/` | `DAV: 1,2,3, calendar-access, addressbook` |

## Kalenderoperationen

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `MKCALENDAR` | `<calendar-home>/name/` | neuen Kalender anlegen |
| `REPORT` | `<calendar-url>` | `calendar-query` (Zeitraum) oder `sync-collection` |
| `PUT` | `<calendar-url>/<uid>.ics` | Ereignis anlegen/ändern (If-Match / If-None-Match) |
| `GET` | `<calendar-url>/<uid>.ics` | einzelnes Ereignis inkl. ETag |
| `DELETE` | `<calendar-url>/<uid>.ics` | Ereignis löschen |
| `PROPPATCH` | `<calendar-url>` | Kalendername/-farbe ändern |

## Beispiel: Ereignis anlegen

Request:

```http
PUT /dav.php/calendars/anna/work/standup-2026-11-02.ics HTTP/1.1
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

Response: `HTTP/1.1 201 Created` mit `ETag`.

## Beispiel: calendar-query

```xml
<C:calendar-query xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:caldav">
  <D:prop><D:getetag/><C:calendar-data/></D:prop>
  <C:comp name="VCALENDAR"><C:comp name="VEVENT"/></C:comp>
  <C:timerange start="20261101T000000Z" end="20261108T000000Z"/>
</C:calendar-query>
```

Antwort als `D:multistatus` mit ICS-Daten je Ereignis.

## Rate Limits

Eingebaute Limits: ❌. Absicherung über Reverse Proxy (nginx `limit_req`) und Fail2ban gegen Basic-Auth-Bruteforce.

## Administration („Admin-API")

- **Web-UI** `/admin/`: Benutzer, Kalender, Adressbücher, Freigaben, Einstellungen
- **CLI**: `baikal.php` (Setup/Wartung), Davical-Core-Skripte
- Direkte Datenbankänderungen sind nicht unterstützt (Sync-Token-Caching)

## SDKs und Clients

- **Python**: `caldav`, `vdirsyncer`
- **PHP**: Davical-Core `Cal::DAV::Server` (im Server selbst)
- **JS**: `js-calendav`, `ts-caldav`, oder rohes `fetch` mit DAV-Methoden
- **CLI**: `vdirsyncer`, `khal`

## Skin-Hinweis

FreeSynergy-Skins mit „Davical-Backend" sprechen dieselben RFC-Endpunkte; Felder/Modelle: [Event-Modell](../../../../data/modelle.md), [ICS-Format](../../../../data/formate.md).
