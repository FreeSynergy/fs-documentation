# Kalendar - API Dokumentation

## Übersicht

Kalendar stellt **keine eigene API** bereit — es ist ein reiner Client. Die programmatischen Schnittstellen sind die Standards, auf die es zugreift: CalDAV/CardDAV (RFC 4791/6352) gegen den jeweiligen Server, KAlCalismasse/ICS als Dateiformat und D-Bus/Akonadi nur intern. Für einen FreeSynergy-Skin ist deshalb die **CalDAV-Schnittstelle des angebundenen Servers** die relevante API.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| CalDAV (HTTP, RFC 4791) | Kalender lesen/schreiben (der eigentliche Datenweg) | Standard, serverseitig |
| `.ics`-Dateien / `webcal://` | Import, Export, Kalenderabos | Standard |
| D-Bus / Akonadi | interne Prozesskommunikation unter KDE | intern, nicht für Skin-Integration empfohlen |
| Eigene REST-API | — | ❌ Nicht vorhanden |
| Webhooks | — | ❌ Nicht vorhanden (ereignisseitig nur serverseitige Push/Benachrichtigungen) |

## Authentifizierung

- **Basic / Digest Auth** über HTTPS (Basic nur mit TLS)
- **OAuth 2.0** bei Servern, die das verlangen (z.B. persönliche google-Kalender via OAuth-Client — Kalendar nutzt dazu die KDE-Integration/Passwort-Agent)
- **App-Passwörter** bei Two-Factor-Servern (Nextcloud, Fastmail)
- Passwörter liegen im **KWallet/Plasma-Wallet**, nicht in Konfigurationsdateien

## CalDAV-Endpunkte (RFC 4791, serverabhängig)

Discovery: `GET /.well-known/caldav` → 3xx auf Principal-URL.

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `PROPFIND` | `/` (Principal) | Kalendersätze (`calendar-home-set`) ermitteln |
| `PROPFIND` | `<calendar-home>` | Kalenderliste mit Namen, Farbe (`calendar-color`), Rechten (`read-write`/`read`) |
| `GET` | `<calendar-url>?content-type=text/calendar` | Kalender als ICS-Strom abrufen |
| `REPORT` | `<calendar-url>` | `calendar-query`: Ereignisse im Zeitraum (`DAV:prop`, `C:comp filter: VEVENT`) |
| `PUT` | `<calendar-url>/<uid>.ics` | Ereignis anlegen/ändern |
| `DELETE` | `<calendar-url>/<uid>.ics` | Ereignis löschen |
| `GET` | `<calendar-url>/<uid>.ics?ETag` | Einzelnes Ereignis (If-Match bei Änderung) |

## Beispiel: calendar-query

Request:

```http
REPORT /remote.php/dav/calendars/anna/privat/ HTTP/1.1
Host: cloud.example.org
Depth: 1
Content-Type: application/xml

<?xml version="1.0"?>
<C:calendar-query xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:caldav">
  <D:prop><D:getetag/><C:calendar-data/></D:prop>
  <C:comp name="VCALENDAR"><C:comp name="VEVENT"/></C:comp>
  <C:timerange start="20261101T000000Z" end="20261108T000000Z"/>
</C:calendar-query>
```

Response (Auszug):

```xml
<?xml version="1.0"?>
<D:multistatus xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:caldav">
  <D:response>
    <D:href>/remote.php/dav/calendars/anna/privat/8f1c2.ics</D:href>
    <D:propstat><D:prop>
      <D:getetag>"etag-17"</D:getetag>
      <C:calendar-data>BEGIN:VCALENDAR ... BEGIN:VEVENT
SUMMARY:Standup
DTSTART:20261102T090000Z
DTEND:20261102T091500Z
END:VEVENT END:VCALENDAR</C:calendar-data>
    </D:prop><D:status>HTTP/1.1 200 OK</D:status></D:propstat>
  </D:response>
</D:multistatus>
```

## Rate Limits

Clientseitig keine; serverseitig je nach CalDAV-Server (Nextcloud-Bruteforce-Schutz, Kolab-Limits). Kalendar/Akonadi synchronisieren inkrementell über ETags — wenige Requests pro Intervall.

## Webhooks und Push

- ❌ Kalendar-seitig nicht vorhanden
- Serverseitig: CalDAV-Sync-Erweiterung (RFC 5995) bzw. Push (Nextcloud Notifications) — die Clients lösen dann ein `REPORT` aus

## SDKs und Client-Bibliotheken

- **libkcalcore / KCalCore** (C++): KAlCalismasse-Parsen, von Kalendar genutzt
- **Python**: `caldav`, `caldav`-Bibliotheken (RFC-4791-Client) — gleicher Datenweg wie Kalendar
- **JavaScript**: `js-calendav` bzw. Fetch mit `REPORT` — für FreeSynergy-Skins der empfohlene Weg

## Skin-Hinweis

Ein Kalendar-Skin bildet primär die **Oberfläche** nach (Ansichten, Schnellerfassung, Seitenleiste) und spricht datenseitig dieselbe CalDAV-API wie Kalendar selbst — siehe [Standardisierte Daten: ICS](../../../../data/formate.md) und [Event-Modell](../../../../data/modelle.md).
