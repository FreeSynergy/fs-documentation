# Nextcloud Calendar - API Dokumentation

## Übersicht

Die offizielle, standardisierte Schnittstelle von Nextcloud Calendar ist **CalDAV**: Der Nextcloud-Server betreibt ein CalDAV-Backend (sabre/dav) unter `/.well-known/caldav` bzw. `/remote.php/dav/`. Kalender, Ereignisse, Free-Busy-Abfragen und inkrementeller Sync laufen über WebDAV-Methoden (`PROPFIND`, `REPORT`, `PUT`, …) nach RFC 4791. Zusätzlich besitzt die Kalender-App kleine **REST-Endpunkte für den Eigenbedarf der Weboberfläche**; diese sind nicht als stabile öffentliche API dokumentiert. Talk-Terminumfragen und Verfügbarkeitsumfragen nutzen interne Endpunkte ohne öffentliches API-Versprechen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| CalDAV/WebDAV (`/remote.php/dav/…`) | Kalender und Ereignisse, Sync, Free-Busy, öffentliche Kalender-Exporte | Offiziell, IETF-Standard (RFC 4791, RFC 5995) |
| App-REST (`/index.php/apps/calendar/…`) | App-Konfiguration, Zeiträume, iTIP-Antworten, Kommentare | Intern, **(nicht dokumentiert)**, Versionsabhängig |
| Öffentliches Kalender-Template (`/index.php/apps/calendar/public/<token>`) | Abo-/Web-Ansicht öffentlicher Kalender | Teil der App, Linkformat kann variieren |
| Talk-/Verfügbarkeits-Umfragen | interne Endpunkte | ❌ Keine öffentliche API |
| Webhooks | ❌ Nicht vorhanden (nur Community-Webhooks-App, keine Kalender-Events) | — |
| OCC-Kommandos | Wartung (Geburtstagskalender, DAV-Konfiguration) | Offizielle Server-CLI |

## Authentifizierung

- **Browser**: Nextcloud-Session nach Login (Single Sign-On über alle Apps), optional Zwei-Faktor-Authentifizierung
- **CalDAV-Clients**: HTTP **Basic Auth** mit Nextcloud-Benutzername und Passwort; empfohlen sind **App-Passwörter** (Persönliche Einstellungen → Sicherheit → „Neues App-Passwort"), besonders bei Zwei-Faktor-Authentifizierung
- **Öffentliche Kalender**: Zugriff über Token im Pfad (`/remote.php/dav/public-calendars/<token>`), optional Passwort
- **Brute-Schutz**: Der Server staffelt Login-Verzögerungen (brute-force protection); Sperr-IPs wirken auch auf DAV-Anfragen

## CalDAV-Endpunkte

Basis-URL: `https://cloud.example.com`. Der Einstieg ist der Well-Known-Pfad.

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `PROPFIND` | `/.well-known/caldav` | Leitet auf den Nutzer-Principal um (CalDAV-Discovery) |
| `PROPFIND` | `/remote.php/dav/principals/users/<user>/` | Nutzer-Principal, Calendar-Home-Set |
| `PROPFIND` (Depth 1) | `/remote.php/dav/calendars/<user>/` | Eigene Kalender auflisten (Name, Farbe, Beschreibung) |
| `MKCALENDAR` | `/remote.php/dav/calendars/<user>/<slug>/` | Kalender anlegen |
| `PROPPATCH` | `/remote.php/dav/calendars/<user>/<slug>/` | Kalender umbenennen, Farbe/Zeitzone ändern |
| `DELETE` | `/remote.php/dav/calendars/<user>/<slug>/` | Kalender löschen |
| `GET` | `/remote.php/dav/calendars/<user>/<slug>/<objekt>.ics` | Einzelnes Ereignis als ICS |
| `PUT` | `/remote.php/dav/calendars/<user>/<slug>/<objekt>.ics` | Ereignis anlegen/ändern (`If-None-Match`/`If-Match`) |
| `DELETE` | `/remote.php/dav/calendars/<user>/<slug>/<objekt>.ics` | Ereignis löschen |
| `REPORT` (calendar-query) | Kalender oder Calendar-Home | Ereignisse im Zeitraum suchen (ICS-Filter) |
| `REPORT` (calendar-multiget) | Kalender-Home | Mehrere ICS-Objekte per URL holen |
| `REPORT` (sync-collection) | Kalender | Inkrementeller Sync mit Sync-Token (RFC 5995) |
| `REPORT` (free-busy-query) | Principal/Kalender | Verfügbarkeitsabfrage |
| `POST` | `/remote.php/dav/public-calendars/<token>?export` | Öffentlich geteilten Kalender als ICS exportieren |

## App-REST-Endpunkte (intern, nicht dokumentiert)

Von der Weboberfläche verwendet; Pfade können sich mit App-Versionen ändern. Basis: `https://cloud.example.com/index.php/apps/calendar/`.

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/config` | Persönliche App-Einstellungen (Zeitzone, Wochenanfang, Standardansicht, Filterschalter) |
| `GET` | `/timeobjects/<start>/<ende>` | Ereignisse eines Zeitraums (für Raster, Suche, Verfügbarkeiten) |
| `GET` | `/timezone-detections` | Zeit-Vorschlag anhand der Client-IP |
| `POST` | `/schedule/<kalendertyp>` | iTIP-Antwort auf eine Einladung (annehmen/ablehnen) aus der Web-UI |
| `GET`/`POST` | `/comment/<objektId>` | Kommentare zu einem Ereignis lesen/anlegen |
| `POST` | `/public-link/<kalenderId>` (Pfad variiert) | Öffentlichen Link anlegen; genaue Route **(nicht dokumentiert)** |

## Beispiele

### Kalender auflisten (PROPFIND)

```bash
curl -sk -u "alice:APP-PASSWORT" \
  -X PROPFIND -H "Depth: 1" \
  --data '<?xml version="1.0"?>
<d:propfind xmlns:d="DAV:" xmlns:c="urn:ietf:params:xml:ns:caldav"
            xmlns:cs="http://calendarserver.org/ns/">
  <d:prop>
    <d:displayname/>
    <cs:getctag/>
    <c:calendar-color/>
  </d:prop>
</d:propfind>' \
  "https://cloud.example.com/remote.php/dav/calendars/alice/"
```

Antwort (gekürzt, WebDAV-Multistatus-XML):

```xml
<?xml version="1.0"?>
<d:multistatus xmlns:d="DAV:">
  <d:response>
    <d:href>/remote.php/dav/calendars/alice/personal/</d:href>
    <d:propstat>
      <d:prop>
        <d:displayname>Privat</d:displayname>
        <cs:getctag>7428f7a2…</cs:getctag>
        <c:calendar-color>#0082c9</c:calendar-color>
      </d:prop>
    </d:propstat>
  </d:response>
</d:multistatus>
```

### Ereignisse eines Zeitraums (REPORT calendar-query)

```bash
curl -sk -u "alice:APP-PASSWORT" -X REPORT \
  -H "Content-Type: application/xml" \
  --data '<?xml version="1.0"?>
<c:calendar-query xmlns:d="DAV:" xmlns:c="urn:ietf:params:xml:ns:caldav">
  <d:prop><d:getetag/><c:calendar-data/></d:prop>
  <c:filter><c:comp-filter name="VCALENDAR">
    <c:comp-filter name="VEVENT">
      <c:time-range start="20261101T000000Z" end="20261108T000000Z"/>
    </c:comp-filter>
  </c:comp-filter></c:filter>
</c:calendar-query>' \
  "https://cloud.example.com/remote.php/dav/calendars/alice/team-vertrieb/"
```

Antwort: pro Treffer ein `<d:response>` mit `<c:calendar-data>` (vollständiger VEVENT-Block, gekürzt):

```
BEGIN:VEVENT
UID:8dfb1a3c-….ics
SUMMARY:Sprint-Planung
DTSTART:20261103T090000Z
DTEND:20261103T100000Z
END:VEVENT
```

### App-Konfiguration (JSON, inoffiziell)

```bash
curl -sk -b "session-cookie" \
  "https://cloud.example.com/index.php/apps/calendar/config"
```

Antwort (Beispiel, gekürzt):

```json
{
  "config": {
    "firstDayOfWeek": 1,
    "timezone": "Europe/Berlin",
    "defaultView": "day",
    "searchEnabled": true,
    "initiallyOpenCalendarList": true
  }
}
```

## Rate Limits

- Nextcloud bringt **keine dokumentierten offiziellen Rate Limits pro Endpunkt**.
- Der Server schützt sich über **Brute-Force-Verzögerungen** und IP-Sperren; aggressive Sync-Skripte können dadurch vorübergehend ausgesperrt werden.
- Empfehlung: Begrenzung im Reverse Proxy (nginx `limit_req`, Traefik-Rate-Limit-Middleware), `Sync-Token`-basierte REPORTs statt Vollabfragen, `getctag` zur Änderungserkennung nutzen.
- Hintergrundlast: Abo-Aktualisierungen und Einladungs-Mails laufen über Cron-Jobs; Cron-Intervall (Standard 5 Minuten) beeinflusst die Latenz, nicht das Limit.

## Webhooks

- ❌ **Keine offiziellen Webhooks** für Termin- oder Kalenderänderungen.
- Alternativen:
  - **Activity-App**: Aktivitäten der Instanz (eingeschränkt kalendertauglich)
  - **Community-App „Webhooks"**: generische Hooks auf Activity-Ereignisse, kein dokumentiertes Kalender-Event-Schema (nicht dokumentiert)
  - **Pull statt Push**: Skripte holen Änderungen per `sync-collection`-REPORT oder `getctag`-Vergleich

## SDKs und Client-Bibliotheken

- **Kein offizielles Nextcloud-Calendar-SDK** für Drittanwendungen.
- Serverseitige Referenz: **sabre/dav** (PHP) - das Nextcloud-DAV-Backend selbst.
- Client-Bibliotheken (CalDAV-Standard, gepflegt): **python-caldav**, **caldav.js**, **sabre/xml + sabre/http** (PHP), **ical.js** (ICS-Parsing), **FullCalendar** (Renderer), **@nextcloud/calendar-js** (offizielle JS-Bibliothek für Wiederholungsregeln, von Nextcloud gepflegt).
- Fertige Clients: Thunderbird, GNOME Evolution, Apple Kalender, DAVx⁵ (Android).

## OCC-Kommandos (Wartung)

```bash
php occ dav:sync-birthday-calendar <user>   # Geburtstagskalender (neu) aufsetzen
php occ config:app:set dav enableBirthdayCalendar --value yes
```

Weitere DAV-Einstellungen (Gruppenkalender, Adressbuch) laufen über `config.php` bzw. `occ config:*`; einzelne Schlüssel heißen je nach Serverversion anders und sind im Detail **(nicht dokumentiert)** - vor Änderung im Admin-Handbuch der eingesetzten Nextcloud-Version prüfen.

## Hinweise für den Betrieb

- Nur über **HTTPS** betreiben: CalDAV-Basic-Auth und App-Passwörter sind ohne TLS wertlos.
- App-Passwörter pro Client vergeben und rotieren; „normale" Passwörter für Skripte vermeiden.
- Bei Großeinführungen (Umzug von Google/Outlook) ICS-Importe drosseln: PUT pro Ereignis ist die teuerste Route.

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
