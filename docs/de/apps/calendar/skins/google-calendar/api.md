# Google Kalender - API Dokumentation

## Übersicht

Der programmatische Zugang zu Google Kalender läuft über die **Google Calendar REST API v3** (JSON über HTTPS, Basis `https://www.googleapis.com/calendar/v3`). Zusätzlich existieren **CalDAV** für klassische Kalender-Clients, **ICS-Abonnement- und Embed-URLs** für öffentliche Kalender sowie **Push-Benachrichtigungskanäle** (Webhook-artig). Alle Zugriffe sind an ein Google-Konto bzw. ein Google-Cloud-Projekt mit OAuth 2.0 gebunden; es gibt keine Möglichkeit, die API auf eigener Hardware bereitzustellen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST Calendar API v3 (`https://www.googleapis.com/calendar/v3`) | Kalender, Termine, wiederkehrende Serien, ACL, Farben, Einstellungen, Free/Busy | ✅ Offiziell, vollständig dokumentiert |
| Batch (`https://www.googleapis.com/batch/calendar/v3`) | Mehrere Aufrufe in einer HTTP-Anfrage (Multipart) | ✅ Offiziell |
| Push-Kanäle (`…/events/watch`, `…/calendarList/watch`, `…/channels/stop`) | Änderungsbenachrichtigungen an HTTPS-Endpunkt | ✅ Offiziell |
| CalDAV (RFC 4791) | Kalender-Clients (Thunderbird, Apple Kalender, Evolution, DAVx5) | ✅ Unterstützt, für Workspace-Accounts administrativ freizuschalten |
| ICS-Abonnement / Embed | Öffentliches Lesen und Einbetten | ✅ Offiziell |
| Google Tasks API (`https://tasks.googleapis.com/tasks/v1/...`) | Aufgabenliste neben dem Kalender | ✅ Eigener Dienst |
| Apps Script-Dienst `CalendarApp` | Skriptsteuerung innerhalb des Google-Kontos | ✅ Offiziell |
| Calendar API v2 | Altbestand | ❌ Eingestellt |
| GraphQL / OData / eigene Server-API | — | ❌ Nicht vorhanden |
| API für Terminpläne (Buchungsseiten) | — | ❌ Nicht dokumentiert |
| Self-Hosting der API/des Servers | — | ❌ Nicht möglich |

**Discovery-Dokument**: `https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest`

## Authentifizierung

- **OAuth 2.0** (Standardweg): Access-Token im Header `Authorization: Bearer <token>`, dazu Refresh-Token für langlebige Integrationen. Consent-Screen je Scope.
- **Service Account mit Domain-wide Delegation**: Server-zu-Server-Zugriff auf Kalender einer Workspace-Domäne; die Delegierung wird in der Admin Console vergeben.
- **API-Schlüssel**: nur für **lesende** Zugriffe auf **öffentliche** Kalender sinnvoll (`?key=<apikey>`), ohne Nutzerkontext.
- **CalDAV**: OAuth 2.0 wird empfohlen; klassische Passwort-/App-Passwort-Nutzung ist nur vorhanden, wenn 2-Schritt-Bestätigung und Drittanbieterzugriff es zulassen. Für Workspace muss der Administrator **"Zugriff auf Kalender und Kontakte über Drittanbieter-APIs"** aktivieren.
- **Session-Cookies** der Web-Oberfläche sind nicht als API-Authentifizierung dokumentiert und für Skripte ungeeignet.

**Scopes (Auswahl)**

| Scope | Berechtigung |
|-------|--------------|
| `https://www.googleapis.com/auth/calendar` | Vollzugriff auf Kalender und Termine |
| `https://www.googleapis.com/auth/calendar.events` | Termine lesen und schreiben |
| `https://www.googleapis.com/auth/calendar.events.readonly` | Termine nur lesen |
| `https://www.googleapis.com/auth/calendar.readonly` | Kalender und Termine nur lesen |
| `https://www.googleapis.com/auth/calendar.freebusy` | Nur Free/Busy-Abfragen |
| `https://www.googleapis.com/auth/calendar.settings.readonly` | Kontoeinstellungen lesen |
| `https://www.googleapis.com/auth/calendar.push` | Push-Benachrichtigungskanäle anlegen/löschen |

**Kalender-IDs**: `primary` (Standardkalender des angemeldeten Nutzers), E-Mail-Adresse (Privat- oder Gruppenkalender), Ressourcenkalender-ID (Raum/Gerät), Kalender-ID eines öffentlichen Kalenders.

## Endpunkte

### Kalenderliste (Sichtbarkeit und Anzeige pro Nutzer)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/calendar/v3/users/{user}/calendarList` | Kalender des Nutzers auflisten (`maxResults`, `pageToken`, `syncToken`, `showDeleted`, `minAccessRole`) |
| `GET` | `/calendar/v3/users/{user}/calendarList/{calendarId}` | Einzelnen Kalendereintrag lesen |
| `POST` | `/calendar/v3/users/{user}/calendarList` | Kalender zur eigenen Liste hinzufügen (Abonnement/freigegebener Kalender) |
| `PATCH` / `PUT` | `/calendar/v3/users/{user}/calendarList/{calendarId}` | Anzeigefarben, Erinnerungsvorgaben, Zusammenfassungs- und Sichtbarkeitsoptionen ändern |
| `DELETE` | `/calendar/v3/users/{user}/calendarList/{calendarId}` | Kalender aus der eigenen Liste entfernen (nicht löschen) |
| - | - | Die Rolle des Nutzers wird nicht separat abgefragt, sondern steht als `accessRole` im Kalender- bzw. Calendarlist-Eintrag |

### Kalender

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/calendar/v3/users/{user}/calendars/{calendarId}` | Kalender-Metadaten (Zeitzone, Ort, Zugriffsrolle) |
| `POST` | `/calendar/v3/users/{user}/calendars` | Neuen Kalender anlegen |
| `PATCH` / `PUT` | `/calendar/v3/users/{user}/calendars/{calendarId}` | Kalender ändern (Name, Zeitzone, Beschreibung, Farbe) |
| `DELETE` | `/calendar/v3/users/{user}/calendars/{calendarId}` | Kalender löschen (nur Besitzer) |
| `POST` | `/calendar/v3/users/{user}/calendars/{calendarId}/clear` | Alle Termine eines Kalenders löschen (entleeren) |

### Termine (Events)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/calendar/v3/calendars/{calendarId}/events` | Termine auflisten (`timeMin`, `timeMax`, `singleEvents=true`, `orderBy=startTime`, `q`, `showDeleted`, `syncToken`, `updatedMin`, `maxResults`, `pageToken`, `timeZones`) |
| `GET` | `/calendar/v3/calendars/{calendarId}/events/{eventId}` | Einzelnen Termin lesen (`alwaysIncludeEndTime`, `maxAttendees`, `timeZones`) |
| `POST` | `/calendar/v3/calendars/{calendarId}/events` | Termin anlegen (`sendUpdates=all|none`, `supportsAttachments`) |
| `PATCH` | `/calendar/v3/calendars/{calendarId}/events/{eventId}` | Termin teilweise ändern |
| `PUT` | `/calendar/v3/calendars/{calendarId}/events/{eventId}` | Termin vollständig ersetzen |
| `DELETE` | `/calendar/v3/calendars/{calendarId}/events/{eventId}` | Termin absagen/löschen (`sendUpdates`) |
| `POST` | `/calendar/v3/calendars/{calendarId}/events/{eventId}/move` | Termin in anderen Kalender verschieben (`targetCalendarId`, `previousStartDateTime`) |
| `GET` | `/calendar/v3/calendars/{calendarId}/events/{eventId}/instances` | Aufgelöste Instanzen einer Terminserie |
| `POST` | `/calendar/v3/calendars/{calendarId}/events/watch` | Push-Kanal für Termine dieses Kalenders einrichten |
| ❌ | - | Kein öffentlicher Import-/Export-Endpunkt für ICS-Dateien dokumentiert; ICS-Import und -Export laufen über die Weboberfläche bzw. über `events.insert` mit eigenen Daten |

### Berechtigungen (ACL) pro Kalender

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/calendar/v3/users/{user}/settings` | Kontoeinstellungen des Nutzers auflisten |
| `GET` | `/calendar/v3/users/{user}/settings/{setting}` | Einzelne Einstellung lesen |
| `GET` | `/calendar/v3/users/{user}/calendars/{calendarId}/acl` | Freigabeliste eines Kalenders |
| `GET` | `/calendar/v3/users/{user}/calendars/{calendarId}/acl/{ruleId}` | Einzelne Freigaberegel |
| `POST` | `/calendar/v3/users/{user}/calendars/{calendarId}/acl` | Freigabe erteilen (`user`, `group`, `domain`, `default` mit Rolle) |
| `PATCH` / `PUT` | `/calendar/v3/users/{user}/calendars/{calendarId}/acl/{ruleId}` | Rolle ändern (`reader`, `writer`, `owner`, freie/belegte Zeiten via `role`-Wert der API) |
| `DELETE` | `/calendar/v3/users/{user}/calendars/{calendarId}/acl/{ruleId}` | Freigabe entziehen |

### Farben, Free/Busy und Kanäle

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/calendar/v3/colors` | Verfügbare Kalender- und Terminfarben (`colorId`) |
| `POST` | `/calendar/v3/freeBusy` | Belegungszeiten mehrerer Kalender in einem Aufruf |
| `POST` | `/calendar/v3/users/{user}/calendarList/watch` | Push-Kanal für Kalenderliste einrichten |
| `POST` | `/calendar/v3/channels/stop` | Push-Kanal beenden (`id`, `resourceId`) |

## Beispiele

### Termine eines Zeitraums laden

```bash
curl -s \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  "https://www.googleapis.com/calendar/v3/calendars/primary/events?singleEvents=true&orderBy=startTime&timeMin=2026-10-27T00:00:00%2B02:00&timeMax=2026-10-31T23:59:59%2B01:00&maxResults=50"
```

Antwort (gekürzt):

```json
{
  "kind": "calendar#events",
  "etag": "\"1234567890123400\"",
  "summary": "Hauptkalender",
  "timeZone": "Europe/Berlin",
  "updated": "2026-10-27T07:12:03.000Z",
  "itemsPerPage": 50,
  "nextSyncToken": "MTcxNzAwMDAwMDAwMDAwMDAwMA",
  "items": [
    {
      "kind": "calendar#event",
      "etag": "\"3999000000000000\"",
      "id": "2f8k1a0b9c7d6e5f1a2b3c4d5e",
      "iCalUID": "2f8k1a0b9c7d6e5f1a2b3c4d5e@google.com",
      "status": "confirmed",
      "htmlLink": "https://www.google.com/calendar/event?eid=MmY4azFhMGI5YzdkN2U1ZjFhMmIzYzRkNWU",
      "created": "2026-10-20T09:00:00.000Z",
      "updated": "2026-10-26T18:41:22.000Z",
      "summary": "Team-Meeting",
      "description": "Sprint-Review, Raum 3",
      "location": "Raum 3",
      "start": { "dateTime": "2026-10-27T09:00:00+02:00", "timeZone": "Europe/Berlin" },
      "end": { "dateTime": "2026-10-27T09:30:00+02:00", "timeZone": "Europe/Berlin" },
      "creator": { "email": "anna@example.com", "displayName": "Anna" },
      "organizer": { "email": "anna@example.com", "displayName": "Anna" },
      "attendees": [
        { "email": "anna@example.com", "displayName": "Anna", "responseStatus": "accepted", "organizer": true },
        { "email": "ben@example.com", "displayName": "Ben", "responseStatus": "needsAction" }
      ],
      "attendeesOmitted": false,
      "transparency": "opaque",
      "visibility": "default",
      "eventStatus": "confirmed",
      "reminders": { "useDefault": true },
      "sequence": 1,
      "conferenceData": { "entryPoints": [ { "entryPointType": "video", "uri": "https://meet.google.com/abc-defg-hij" } ] }
    }
  ]
}
```

### Termin mit Serie und Gästen anlegen

```bash
curl -s -X POST \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "summary": "1:1 mit Customer",
    "location": "Meet",
    "description": "Monatliches Gespräch",
    "start": { "dateTime": "2026-11-03T14:00:00+01:00", "timeZone": "Europe/Berlin" },
    "end": { "dateTime": "2026-11-03T14:30:00+01:00", "timeZone": "Europe/Berlin" },
    "recurrence": [ "RRULE:FREQ=MONTHLY;BYDAY=1MO" ],
    "attendees": [
      { "email": "kunde@beispiel.de", "displayName": "Kunde" }
    ],
    "reminders": {
      "useDefault": false,
      "overrides": [
        { "method": "popup", "minutes": 10 },
        { "method": "email", "minutes": 1440 }
      ]
    },
    "extendedProperties": { "private": { "crm_ticket_id": "T-4711" } }
  }' \
  "https://www.googleapis.com/calendar/v3/calendars/primary/events?sendUpdates=all"
```

Antwort enthält den angelegten Termin (u. a. `id`, `iCalUID`, `status`, `created`, `updated`, `htmlLink`).

### Free/Busy abfragen

```bash
curl -s -X POST \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "timeMin": "2026-11-02T00:00:00Z",
    "timeMax": "2026-11-03T00:00:00Z",
    "timeZone": "Europe/Berlin",
    "items": [ { "id": "primary" }, { "id": "team@beispiel.de" } ]
  }' \
  "https://www.googleapis.com/calendar/v3/freeBusy"
```

Antwort (gekürzt):

```json
{
  "kind": "calendar#freeBusy",
  "timeMin": "2026-11-02T00:00:00.000Z",
  "timeMax": "2026-11-03T00:00:00.000Z",
  "calendars": {
    "primary": { "busy": [ { "start": "2026-11-02T09:00:00Z", "end": "2026-11-02T09:30:00Z" } ] },
    "team@beispiel.de": { "busy": [ { "start": "2026-11-02T13:00:00Z", "end": "2026-11-02T14:00:00Z" } ] }
  }
}
```

### Öffentlichen Kalender per ICS abonnieren

```
https://calendar.google.com/calendar/ical/<KALENDER_ID>/public/basic.ics
```

Einbetten in eine Website:

```
https://calendar.google.com/calendar/embed?src=<KALENDER_ID>&ctz=Europe%2FBerlin
```

*(Diese URL-Formate sind die öffentlich genutzten Formen; für eigene Integrationen ist die API der stabilere Weg.)*

### CalDAV

- Client-Konfiguration: Kalender-Clients fragen die Kalender-URL aus den Kalendereinstellungen ab; für Workspace-Accounts muss der Administrator den Drittanbieter-/CalDAV-Zugriff einschalten.
- Der in der Google-Hilfe genannte CalDAV-Serverpfad lautet in der klassischen Form `https://apidata.googleusercontent.com/caldav/v2/<email>/user`; für aktuelle Kontotypen ist die **genaue Basis-URL nicht eindeutig dokumentiert** - im Zweifel aus der Client-Einrichtung übernehmen.
- Schreibende CalDAV-Nutzung ist möglich, deckt aber nicht alle Kalender-API-Funktionen ab (Konferenzdaten, Anhänge, Arbeitsort-Attribute).

## Rate Limits

- Google Calendar API nutzt **kontingentbasierte Quotas pro Google-Cloud-Projekt und pro Nutzer** (typischerweise in Anfragen pro 100 Sekunden gemessen). Die konkreten Zahlen hängen vom Projekt und freigeschalteten Kontingenten ab und stehen in der API-Referenz bzw. in **Google Cloud Console → APIs & Dienste → Quotas**; Erhöhungen sind dort beantragbar.
- Überschreitungen liefern **HTTP 429** mit Fehlergründen wie `userRateLimitExceeded` oder `rateLimitExceeded`; empfohlen ist **exponentielles Backoff mit Jitter**.
- **ETags** (`If-None-Match`) und **`syncToken`** reduzieren die Last deutlich: nur geänderte Ressourcen werden übertragen. Ein `syncToken` ist zeitlich begrenzt; nach Ablauf ist ein vollständiger Abgleich mit `showDeleted=true` nötig.
- **Batch-Anfragen** bündeln mehrere Aufrufe (Multipart/`related`); Google begrenzt die Anzahl der Aufrufe pro Batch (je nach API-Dokumentation, üblicherweise einige Dutzend).
- **Push statt Polling**: Ein `watch`-Kanal auf Termine ersetzt das Intervallabfragen; die Kanallaufzeit ist begrenzt und muss verlängert werden (`events.sync` bzw. erneutes `watch`).
- Praktische Richtwerte: ein einziges Projekt mit Backoff für Synchronisationsläufe, `maxResults` bis 250, nie mehr als nötig parallel; für Organisationssynchronisation Kalenderlisten- und Termine-Sync getrennt takten.

## Webhooks (Push-Benachrichtigungskanäle)

Google Kalender versendet **keine klassischen Webhooks mit JSON-Nutzlast**, sondern **Ressourcen-Benachrichtigungen** an einen registrierten HTTPS-Endpunkt.

Kanal einrichten:

```bash
curl -s -X POST \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "sync-2026-teamkalender-01",
    "type": "web_hook",
    "token": "<eigenes_geheimnis>",
    "address": "https://example.com/calendar/notify",
    "params": { "ttl": "600" }
  }' \
  "https://www.googleapis.com/calendar/v3/calendars/team@beispiel.de/events/watch"
```

Eintreffende Benachrichtigung (Kopfzeilen, Body leer):

```
POST /calendar/notify
X-Goog-Channel-ID: sync-2026-teamkalender-01
X-Goog-Channel-Expiration: 2026-10-28T09:00:00.000Z
X-Goog-Resource-ID: <resourceId>
X-Goog-Resource-State: sync
X-Goog-Resource-URI: https://www.googleapis.com/calendar/v3/calendars/team@beispiel.de/events
X-Goog-Message-Number: 3
```

Hinweise:
- Die Meldung enthält **nicht**, was geändert wurde - der Client muss danach mit `events.list?syncToken=…` nachziehen.
- **Keine Signatur**: Die Authentizität der Anfrage wird über die Kanal-`id`, den eigenen `token` und die Prüfung der `resourceId` sichergestellt; ein HMAC-Secret wie bei anderen Diensten gibt es nicht.
- Endpunkt muss öffentlich per HTTPS erreichbar und bei der Registrierung gültig sein.
- Kanal beenden: `POST /calendar/v3/channels/stop` mit `id` und `resourceId`.

## SDKs und Client-Bibliotheken

| Sprache | Bibliothek |
|---------|------------|
| Python | `google-api-python-client` (`build("calendar", "v3", ...)`) |
| Node.js | `googleapis` (`google.calendar({version: "v3", auth})`) |
| Java | `google-api-services-calendar` |
| PHP | `google/apiclient` (`Google\Service\Calendar`) |
| Ruby | `google-api-client` (`Google::Apis::CalendarV3`) |
| .NET | `Google.Apis.Calendar.v3` |
| Go | `google.golang.org/api/calendar/v3` |

- **Discovery-Dokument** als Grundlage für Codegenerierung und OpenAPI-ähnliche Werkzeuge.
- **Apps Script**: `CalendarApp` (Kalender, Termine, Gäste, Wiederholungen) für Automatisierung innerhalb des Kontos.
- **CalDAV-Clients** bringen ihre eigenen Bibliotheken mit (Thunderbird, Apple Calendar, Evolution, DAVx5, Radicale-Client-Werkzeuge).
- **Kein eigenes Kalender-SDK von Google für mobile Apps** im Sinne einer Offline-Datenbank; mobile Integrationen nutzen die REST-API oder den Kalender des Betriebssystems.

## Betriebshinweise

- API in der Google Cloud Console für das Projekt aktivieren und OAuth-Zustimmungsbildschirm konfigurieren.
- Terminkennung sauber halten: `iCalUID` für Serieneintrag, `id` für Instanz, eigene Schlüssel in `extendedProperties.private` für die Zuordnung zu Quellsystemen.
- Änderungen an Serienterminen erzeugen neue Instanz-IDs; eine Terminserie ist über `iCalUID` plus `recurrence` wiedererkennbar, nicht über die Einzel-ID.
- Zeitangaben immer mit Zeitzonen-Offset senden (`dateTime` + `timeZone`), sonst greift die Kalenderzeitzone.
- Für Gastrechte die Kalender-ACL-Regeln und die Terminfelder `guestsCanModify`, `guestsCanSeeOtherGuests`, `anyoneCanAddSelf` gezielt setzen.
- Da der Dienst proprietär ist: Exportstrategie (ICS/Takeout) mitplanen, um Vendor-Lock-in zu begrenzen.

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
