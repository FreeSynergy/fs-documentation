# Nextcloud Calendar – API (App-Version 6.6.4, Stand: 2026‑11‑02)

## Versionsstand und Entwicklung

- **App `calendar`, Version 6.6.4** (Release 2026‑10‑26, Repo `github.com/nextcloud/calendar`). Das Projekt ist aktiv: letzte Tags im Oktober 2026, tägliche Commit-Aktivität, keine Ankündigung eines End-of-Life.
- `appinfo/info.xml` v6.6.4 verlangt **PHP 8.1–8.5** und **Nextcloud Server 32–35** und deklariert explizit `<backend>caldav</backend>`.
- **Grundarchitektur für die API-Frage:** die App ist nur das Web-Frontend (Vue.js). Der eigentliche Datenzugriff auf Kalender und Termine läuft über das **CalDAV-Backend des Nextcloud-Servers** (sabre/dav), das nicht Teil dieser App ist. Die App bringt zusätzlich eigene HTTP-Routen mit: HTML-Views, ein kleines internes JSON-API (`/v1/...`), die Terminbuchungs-API und – neu in der 6.x-Serie – eine OCS-API für Meeting-Vorschläge (Doodle-artige Terminumfragen).

| API-Ebene | Basis-URL | Status |
|-----------|-----------|--------|
| CalDAV (Termine, Kalender, Sync) | `{base}/remote.php/dav/` | Server-Backend, IETF-Standards RFC 4791/5995, stabil |
| App-Routen (Views, Public, Booking) | `{base}/index.php/apps/calendar/` | aus `appinfo/routes.php` der App, versionsgebunden |
| App-JSON-API (`/v1/...`) | `{base}/index.php/apps/calendar/v1/` | interne API des Frontends, nicht als öffentliches API versprochen |
| Meeting-Proposals | `{base}/ocs/v2.php/calendar/proposal/...` | im Quelltext per `#[ApiRoute]`-Attribut definiert |
| Webhooks | – | nicht vorhanden (siehe unten) |

## CalDAV-Backend (eigentliche Datenzugriffsebene)

Das Frontend der App nutzt selbst den offiziellen Client **`@nextcloud/cdav-library`** mit `rootUrl = generateRemoteUrl('dav')`, also `{base}/remote.php/dav/` (`src/services/caldavService.js`). Damit gilt für jede Integration exakt der Weg, den die App selbst geht:

- **Discovery:** `/.well-known/caldav` → leitet auf den Nutzer-Principal um.
- **Principal:** `PROPFIND {base}/remote.php/dav/principals/users/{user}/` (liefert `calendar-home-set`).
- **Calendar-Home:** `{base}/remote.php/dav/calendars/{user}/` – eigene Kalender; `PROPFIND` (Depth 1) zum Auflisten, `MKCALENDAR` zum Anlegen, `PROPPATCH` für displayname/Farbe/Zeitzone, `DELETE` zum Löschen.
- **Termine:** `PUT`/`GET`/`DELETE` auf `{base}/remote.php/dav/calendars/{user}/{calendar}/{object}.ics` (ICS nach RFC 5545; Konkurrent via `ETag`/`If-Match`).
- **Abfragen:** `REPORT calendar-query` (Zeitraumsuche), `REPORT calendar-multiget`, `REPORT sync-collection` (inkrementeller Sync, RFC 5995), `REPORT free-busy-query`.
- **Öffentliche Kalender:** token-basierte Sammlung unter `/remote.php/dav/public-calendars/{token}`; Export als ICS über `POST ...?export`. Die App baut ihre Public-/Embed-Ansicht über dieselbe öffentliche CalDAV-Sammlung auf (`_createPublicCalendarHome` in `caldavService.js`).
- **Nextcloud-spezifischer Header:** die App sendet `X-NC-CalDAV-Webcal-Caching: On` (bzw. `Off` zum expliziten Auflisten von WebCal-Abos) – ein Server-Erweiterungsheader, kein Standard.
- Geburtstagskalender und weitere Server-seitige Kalenderquellen erscheinen im selben Calendar-Home.

Die CalDAV-Endpunkte gehören zum Nextcloud-Server (Admin-Handbuch → Groupware); Details wie `getctag` zur Änderungs-Erkennung sind dort dokumentiert.

## App-Routen laut `appinfo/routes.php` (v6.6.4)

Basis `{base}/index.php/apps/calendar/` (Kurzform `{base}/apps/calendar/…`).

### HTML-/Deep-Link-Routen (GET)

| URL | Zweck |
|-----|-------|
| `/` | App-Start |
| `/new` bzw. `/new/{isAllDay}/{dtStart}/{dtEnd}` | Editor für neuen Termin öffnen (direkter Link) |
| `/edit/{objectId}` bzw. `/edit/{objectId}/{recurrenceId}` | Termin bearbeiten; `objectId` ist **Base64 des DAV-Pfads** `/remote.php/dav/calendars/{user}/{calendarUri}/{objectUri}` (im Quelltext `ObjectController`/`ViewController` verifiziert) |
| `/{view}/{timeRange}` | Ansicht+Zeitfenster; `view` exakt: `timeGridDay`, `timeGridWeek`, `dayGridMonth`, `multiMonthYear`, `listMonth` |
| `/{view}/{timeRange}/new/{mode}/{isAllDay}/{dtStart}/{dtEnd}` bzw. `…/edit/{mode}/{objectId}/{recurrenceId}` | Editor aus einer Ansicht heraus |
| `/object/{uid}` und `/object/{uid}/{recurrenceId}` | **permanenter Deep Link** nur nach iCal-UID; löst den Termin auf und leitet auf `/edit/…` weiter (`recurrenceId`: Unix-Timestamp oder `next`) |
| `/p/{token}`, `/p/{token}/{view}/{timeRange}`, `/p/{token}/{fancyName}` | öffentliche, gebrandete Kalenderansicht |
| `/embed/{token}…` | öffentliche Ansicht ohne Nextcloud-Chrome (Embedding) |
| `/public/{token}` | Legacy-Alias |
| `/appointments/{userId}` | Terminbuchungsseite eines Nutzers |
| `/appointment/{token}` | konkrete Buchungsseite einer Termin-Konfiguration |
| `/appointment/confirm/{token}` | Bestätigungsseite nach Terminbuchung (GET Formular, POST Bestätigen) |
| `{base}/calendar/proposal/{token}` | öffentliche Abstimmungsseite eines Meeting-Vorschlags (`#[FrontpageRoute]` mit `root: '/calendar'` in `ProposalPublicController`) |

### Internes JSON-API `/v1/…` (vom Frontend genutzt)

| Methode | Endpunkt | Parameter (aus Controllern) |
|---------|----------|------------------------------|
| POST | `/v1/autocompletion/attendee` | `search` – Teilnehmer-Vervollständigung aus Contacts/Circles |
| POST | `/v1/autocompletion/location` | `search` – Raum-/Ortsvorschläge (Ressourcen) |
| POST | `/v1/autocompletion/photo` | `search` – Fototreffer |
| POST | `/v1/autocompletion/groupmembers` | `groupName` – Mitglieder einer Contact-Group |
| GET | `/v1/circles/getmembers` | `circleId` – Mitglieder eines Circles-Teams |
| POST | `/v1/config/{key}` | App-Einstellung des Nutzers speichern (Schlüssel aus `SettingsController`) |
| POST | `/v1/public/sendmail` | `recipient` u. a. – öffentlichen Kalenderlink mailen |

Alle `/v1/`-Endpunkte erfordern eine eingeloggte Nextcloud-Session (`@NoAdminRequired`); sie sind nicht als stabiles externes API dokumentiert und können sich zwischen App-Versionen ändern.

### Terminbuchung (Booking, PublicPage + Token)

| Methode | Endpunkt | Rate-Limit (Attribute im Code) |
|---------|----------|-------------------------------|
| GET | `/appointment/{appointmentConfigToken}/slots` | – |
| POST | `/appointment/{appointmentConfigToken}/book` | Anonym 10/1200 s, Nutzer 10/300 s |
| POST | `/appointment/confirm/{token}` | – |

Buchungsablauf: `slots` liefert buchbare Intervalle (berechnet aus `availability` des Konfigs minus Belegung), `book` reserviert vorläufig, `confirm` nach Bestätigungs-E-Mail schreibt den Termin in den Zielkalender (`BookingCalendarWriter`). Verwaiste Reservierungen räumt der Hintergrund-Job `CleanUpOutdatedBookingsJob` weg.

### Termin-Konfigurationen (REST-Ressource, eingeloggte Nutzer)

Ressource `appointmentConfig` auf `/v1/appointment_configs`:

- `GET /v1/appointment_configs` – eigene Konfigurationen
- `GET /v1/appointment_configs/{id}` – Einzelseite
- `POST /v1/appointment_configs` – anlegen (Rate-Limit 10/1200 s)
- `PUT /v1/appointment_configs/{id}` – ändern
- `DELETE /v1/appointment_configs/{id}` – löschen

Feldschema `create` (validiert in `AppointmentConfigController::create`): `name`, `description`, `location`, `visibility` (`PUBLIC`/`CONFIRMED`), `targetCalendarUri`, `availability` = `{ timezoneId, slots: { MO…SU: [ {start,end} ] } }`, `length`, `increment`, `preparationDuration`, `followupDuration`, `timeBeforeNextSlot`, `dailyMax`, `calendarFreeBusyUris`, `start`, `end`, `futureLimit` (Sekunden bzw. Unix-Timestamps).

### Meeting-Proposals (OCS-API, Serie 6.x)

Alle Aufrufe sind **POST im OCS-Format** (`OCS-APIRequest: true`), Basis `{base}/ocs/v2.php/calendar/proposal/` – verifiziert über `#[ApiRoute(root: '/calendar')]` im `ProposalController` und `generateOcsUrl('/calendar/proposal/…')` im Frontend:

| Endpunkt | Payload | Zugriff / Rate-Limit |
|----------|---------|----------------------|
| `/list` | `{ user? }` | eingeloggt (nur eigene Daten; Admins fremde via `user`), 10/60 s |
| `/fetch` | `{ token }` | PublicPage, Anon 10/300 s |
| `/create` | `{ proposal }` | eingeloggt, 10/60 s |
| `/modify` | `{ proposal }` | eingeloggt, 10/60 s |
| `/destroy` | `{ id, user? }` | eingeloggt, 10/60 s |
| `/convert` | `{ proposalId, dateId, options }` | eingeloggt, 10/60 s; wandelt gewählten Vorschlag in echten Termin um (optional Talk-Raum, Einladungen an Teilnehmer) |
| `/response` | `{ response }` | PublicPage (Abstimmung per Token), Anon 10/300 s |

Proposal-Datenmodell (`src/types/proposals/proposalInterfaces.ts`): `proposal` mit `id`, `uid`, `uuid` (Token), `title`, `description`, `location`, `duration`, `responseNotify`, `participants[]` (`address`, `attendance`, `status`, `realm`), `dates[]` (`date`), `votes[]` (`date`, `participant`, `vote`).

## Authentifizierung und Berechtigungen

- **Nextcloud-typisch, keine feingranularen Scopes:** jeder Zugang erbt die vollen Rechte des Nutzers.
- **Browser:** Nextcloud-Session-Cookie + `RequestToken` (CSRF) für die JSON-/Schreibrouten.
- **CalDAV und OCS:** HTTP Basic mit **App-Passwort** (empfohlen), Bearer-Token oder Nextcloud-Session; OCS zusätzlich `OCS-APIRequest: true`.
- **PublicPages (Public-/Embed-Ansichten, Booking, Proposal fetch/response):** autorisiert ausschließlich über den Token im Pfad; optionale Passwort-Protectung öffentlicher Kalender ist Server-Funktion.
- Brute-Force-Schutz des Servers (gestaffelte Verzögerungen, IP-Sperren) gilt auch für DAV-Routen.

## Limits

- Keine dokumentierten globalen Rate-Limits; die App definiert **pro Endpunkt** `#[UserRateLimit]`/`#[AnonRateLimit]` (oben tabelliert: 10 Anfragen je 60–1200 s je nach Endpunkt).
- Server-seitig: Brute-Force-Throttling, PHP-/Webserver-Einstellungen, Reverse-Proxy-Limits selbst zu setzen.
- Praktische Grenze großer Einführungen: jeder Termin ist ein separates `PUT`-Objekt unter CalDAV.

## Push / Webhooks

- **Keine ausgehenden Webhooks.**
- Die App hört auf die Server-Events `CalendarObjectCreated/Updated/Deleted` und schiebt die Nachricht `calendar_sync` (mit Kalender-URL) in die Queue der **Notify-Push-App** (`lib/Listener/NotifyPushListener.php`) – aber nur, wenn diese installiert ist; sie aktualisiert nur eigene Browser-Tabs des Nutzers, ist kein Drittanbieter-Hook.
- Benachrichtigungen über Buchungen/Einladungen laufen als E-Mails und über die Nextcloud-**Notifications**-App (Notifier der Kalender-App).
- Pull-Alternative für Integrationen: `sync-collection`-REPORT bzw. `getctag`-Vergleich.

## SDKs und Clients

- **Kein SDK für die App-eigenen Endpunkte** (bewusst intern).
- Vom Hersteller gepflegte JS-Bibliotheken, die die App selbst nutzt: `@nextcloud/cdav-library` (CalDAV-Client), `ical.js` (ICS-Parsing), FullCalendar (Rendering), `@nextcloud/calendar-js` (Wiederholungsregeln).
- Server-seitige Referenzimplementierung: **sabre/dav** (PHP).
- Externe Integration: jeder Standard-CalDAV-Client (Thunderbird, GNOME Evolution, Apple Kalender, DAVx⁵, python-caldav …) spricht dieselbe Datenbasis an.

## Abgrenzung / Warnungen

- Frühere App-Versionen hatten andere interne Endpunkte (z. B. `timeobjects`, `schedule`, `comment`) – in v6.6.4 existieren diese Routen **nicht** mehr (`appinfo/routes.php`). Skripte, die darauf bauen, brechen mit modernen Versionen.
- Alles unter `/v1/` und `/ocs/v2.php/calendar/…` ist nicht als öffentliches API versioniert; Stabilität über App-Major-Versionen ist nicht zugesagt. Die stabile Integrationsschiene ist **CalDAV**.

## Quellen (Fundstellen, alle v6.6.4)

- Quelltext-Tag `v6.6.4` (Tarball `github.com/nextcloud/calendar/archive/refs/tags/v6.6.4.tar.gz`, abgerufen 2026-11‑02): `appinfo/routes.php`, `appinfo/info.xml`, `lib/Controller/{AppointmentConfig,Booking,Contact,Email,Object,Proposal,ProposalPublic,PublicView,Settings,View}Controller.php`, `lib/Listener/NotifyPushListener.php`, `lib/Migration/Version6060Date20260801000000.php`, `src/services/{caldavService.js,proposalService.ts,appointmentConfigService.js}`, `src/types/proposals/proposalInterfaces.ts`, `CHANGELOG.md`.
- GitHub-API-Tagliste `nextcloud/calendar` (neuster Tag `v6.6.4`, 2026‑10‑26).
- Nextcloud-Server-Doku Groupware (CalDAV-Grundpfade `/remote.php/dav/`, App-Passwörter): docs.nextcloud.com, Admin-/User-Handbuch (in `info.xml` als offizielle Doku referenziert).
