# Outlook Kalender - API Dokumentation

## Übersicht

Der Outlook Kalender wird programmatisch über **Microsoft Graph** bedient: Kalender, Kalendergruppen, Termine, Freigaben, Zeitpläne und Besprechungssuche sind als REST-Ressourcen unter `https://graph.microsoft.com/v1.0` (und `/beta`) modelliert. Änderungen lassen sich über **Change Notifications** (Webhooks mit Abonnement) abonnieren. Die ältere **Exchange Web Services**-Schnittstelle (EWS) war über Jahrzehnte der Standard für Kalenderzugriff und ist für Exchange Online abgelöst angekündigt; On-Premises-Exchange-Server bedienen sie weiterhin.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Microsoft Graph REST (`/v1.0`, `/beta`) | Kalender, Termine, Serien, Freigaben, Zeitplan, Besprechungssuche | ✅ Offiziell, empfohlener Weg |
| Graph Change Notifications | Webhooks für neue/geänderte Termine | ✅ Offiziell (Abo-basiert) |
| Microsoft Graph Delta (`/me/calendar/delta`) | Inkrementelle Änderungen seit letztem Stand | ✅ Offiziell |
| Exchange Web Services (EWS) | Termine, Kalendersichten, Ordner (SOAP/XML) | ⚠️ Veraltet, für Exchange Online abgelöst angekündigt |
| MAPI over HTTP, Exchange ActiveSync, IMAP4 | Client-Protokolle (Synchronisation) | 🔒 Nicht als öffentliche Integrations-API gedacht |
| CalDAV (`/.well-known/caldav`) | Offener Kalenderstandard | ❌ Wird nicht angeboten |
| ICS-Import/-Export als API-Endpunkt | Kalender als `.ics` ziehen/schieben | ❌ Kein dokumentierter Endpunkt (nur UI-Aktionen) |
| Outlook Calendar REST API (`api.outlook.com`) | Frühere „Calendar API" | ❌ Eingestellt, durch Graph ersetzt |
| Microsoft Bookings API | Externe Terminbuchung | ⚠️ Eigenes Produkt, Graph-Zugriff eingeschränkt/vorschau |

## Authentifizierung

Outlook Kalender nutzt OAuth 2.0 / OpenID Connect über **Microsoft Entra ID** (ehem. Azure AD).

- **Delegated Access**: Der Nutzer meldet sich an, die App erhält einen Access-Token in seinem Namen. Flow: Authorization Code mit PKCE für Web-/Native-Apps.
- **Application Permissions (Client Credentials)**: Daemon-Skripte und Dienste ohne angemeldeten Nutzer; benötigt `Calendars.Read` bzw. `Calendars.ReadWrite` mit **Administratorzustimmung** und greift dann auf Postfächer im Mandanten zu (Zugriff muss gezielt konfiguriert werden).
- **Scopes**: `Calendars.Read`, `Calendars.ReadWrite`, `Calendars.ReadWrite.Shared`, `User.Read` für Profilangaben, `Mail.Read` falls Besprechungsanfragen mitgelesen werden.
- **Token-Endpoint**: `https://login.microsoftonline.com/<tenant-id>/oauth2/v2.0/token`
- **Access-Token** sind kurzlebig (typisch 60–90 Minuten), Refresh-Token erneuern sie.

### Header

```
Authorization: Bearer <access-token>
Content-Type: application/json
Prefer: outlook.timezone="Europe/Berlin"
```

Die `Prefer`-Kopfzeile stellt Datumsangaben in einer Wunschzeitzone zu; ohne sie liefert Graph UTC.

## Endpunkte

Grundpfad: `https://graph.microsoft.com/v1.0`

### Kalender

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/me/calendars` | Eigene Kalender auflisten |
| `GET` | `/me/calendars/{id}` | Einzelnen Kalender lesen |
| `POST` | `/me/calendars` | Kalender anlegen (Name, Farbe, Zeitzone) |
| `PATCH` | `/me/calendars/{id}` | Kalender ändern |
| `DELETE` | `/me/calendars/{id}` | Kalender löschen |
| `GET` | `/me/calendar` | Standardkalender des Kontos |
| `GET` | `/me/calendar/groups` | Kalendergruppen auflisten |
| `POST` | `/me/calendar/groups` | Kalendergruppe anlegen |
| `GET` | `/me/calendars/{id}/calendarView?startDateTime=…&endDateTime=…` | Termine eines Kalenders im Zeitraum |

### Termine

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/me/calendar/events` | Termine des Standardkalenders (liste) |
| `GET` | `/me/calendar/events/{id}` | Einzelnen Termin lesen (`$expand=attachments,instances` möglich) |
| `POST` | `/me/calendar/events` | Termin im Standardkalender anlegen |
| `PATCH` | `/me/calendar/events/{id}` | Termin ändern (Serien: `seriesMasterId` beachten) |
| `DELETE` | `/me/calendar/events/{id}` | Termin löschen |
| `GET` | `/me/events` | Termine kontoweit (Alternative zu `calendarview`) |
| `GET` | `/me/calendarview?startDateTime=2026-10-01T00:00:00Z&endDateTime=2026-10-31T23:59:59Z` | Termine im Zeitraum, Serien aufgelöst |
| `GET` | `/me/events/{id}/instances?startDateTime=…&endDateTime=…` | Einzelne Termine einer Serie |
| `GET` | `/me/events/{id}/attachments` | Anlagen eines Termins |
| `POST` | `/me/events/{id}/attachments` | Anlage hinzufügen |
| `POST` | `/me/events/{id}/forward` | Termin weiterleiten |
| `POST` | `/me/events/{id}/accept` \| `acceptTentatively` \| `decline` \| `cancel` \| `snooze` | Antwortaktionen auf eine Besprechung |

### Zeitplan, Besprechungssuche, Freigaben

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/me/calendar/getSchedule` | Free/Busy und Termine mehrerer Postfächer im Zeitraum |
| `POST` | `/me/calendars/{id}/getSchedule` | Zeitplan eines konkreten Kalenders |
| `POST` | `/me/findMeetingTimes` | Freie Zeiten für Teilnehmer und Räume (Planungsassistent) |
| `GET` | `/me/calendars/{id}/getCalendarPermissions` | Wer darf einen Kalender sehen/bearbeiten |
| `POST` | `/me/calendars/{id}/addCalendarPermission` | Freigabe erteilen (Rolle: `Reviewer`, `Author`, `Editor`, `Owner`, `AvailabilityOnly`, `LimitedDetails`) |
| `POST` | `/me/calendars/{id}/removeCalendarPermission` | Freigabe entziehen |
| `GET` | `/me/calendars/listCalendarPermissions` | Freigaben mehrerer Kalender in einem Aufruf |
| `GET` | `/me/calendar/delta` | Änderungen seit dem letzten Stand (inkrementell) |

### Andere Postfächer (mit entsprechenden Rechten)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/users/{id}/calendarview?startDateTime=…&endDateTime=…` | Zeitplan eines anderen Nutzers lesen |
| `GET` | `/users/{id}/events` | Termine eines anderen Postfachs |
| `POST` | `/users/{id}/events` | Termin in fremdem Kalender anlegen (nur mit Delegierten-/Editorrecht) |
| `GET` | `/groups/{id}/calendar/events` | Gruppenkalender (M365-Gruppe) |
| `GET` | `/me/onlineMeetings` | Onlinebesprechungen (Teams) auflösen, `joinUrl` lesen (eigene Berechtigung) |

### Nützige Query-Parameter

| Parameter | Wirkung |
|-----------|---------|
| `$select=subject,start,end,isAllDay,categories` | Reduziert die Antwort auf benötigte Felder |
| `$expand=attachments,instances,extensions` | Zusätzliche Objekte mitliefern |
| `$filter=start/dateTime ge '2026-10-01T00:00'` | Eingrenzung (Datumsfilter nur in `calendarview` zuverlässig indexiert) |
| `$search="Suchtext"` | Volltextsuche, benötigt Header `ConsistencyLevel: eventual` |
| `$orderby=start/dateTime` | Sortierung |
| `$top` / `$skip` | Seitengröße/Offset; weitere Seiten über `@odata.nextLink` |

## Beispiele

### Termine eines Zeitraums abrufen

```bash
curl -s "https://graph.microsoft.com/v1.0/me/calendarview?\
startDateTime=2026-11-01T00:00:00Z&endDateTime=2026-11-07T23:59:59Z&\
\$select=subject,start,end,isAllDay,organizer&\$orderby=start/dateTime" \
  -H "Authorization: Bearer <access-token>" \
  -H "Prefer: outlook.timezone=\"Europe/Berlin\""
```

Antwort (gekürzt):

```json
{
  "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(microsoft.graph.event)",
  "@odata.nextLink": "https://graph.microsoft.com/v1.0/me/calendarview?startDateTime=...&$skip=10",
  "value": [
    {
      "id": "AAMkAGI2AAA=",
      "subject": "Team-Jour fixe",
      "isAllDay": false,
      "start": { "dateTime": "2026-11-03T09:00:00.0000000", "timeZone": "Europe/Berlin" },
      "end":   { "dateTime": "2026-11-03T09:30:00.0000000", "timeZone": "Europe/Berlin" },
      "organizer": { "emailAddress": { "name": "Anna Beispiel", "address": "anna@example.com" } },
      "categories": ["Team"],
      "isCancelled": false,
      "responseStatus": { "response": "none", "time": "0001-01-01T00:00:00Z" }
    }
  ]
}
```

### Termin anlegen (mit Teilnehmer und Teams-Besprechung)

```bash
curl -s -X POST "https://graph.microsoft.com/v1.0/me/calendar/events" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Workshop Kalender-Anbindung",
    "body": { "contentType": "html", "content": "<p>Agenda: ICS, Graph, Freigaben</p>" },
    "start": { "dateTime": "2026-11-05T10:00:00", "timeZone": "Europe/Berlin" },
    "end":   { "dateTime": "2026-11-05T12:00:00", "timeZone": "Europe/Berlin" },
    "location": { "displayName": "Raum 3.4" },
    "categories": ["Projekt"],
    "isOnlineMeeting": true,
    "attendees": [
      { "emailAddress": { "address": "ben@example.com", "name": "Ben Beispiel" },
        "attendeeType": "required", "status": { "response": "none", "time": "0001-01-01T00:00:00Z" } }
    ],
    "reminders": [ { "method": "email", "remindersMinutesBeforeStart": 15 } ],
    "recurrence": {
      "pattern": { "type": "weekly", "dayOfWeeks": [ "monday" ], "interval": 2 },
      "range": { "type": "endDate", "startDate": "2026-11-05", "endDate": "2026-12-24" }
    }
  }'
```

Antwort: `201 Created` mit dem vollständigen Terminobjekt, darunter `id`, `seriesMasterId`, `onlineMeeting.joinUrl` und `webLink`.

### Webhook-Abo auf Terminänderungen

```bash
curl -s -X POST "https://graph.microsoft.com/v1.0/subscriptions" \
  -H "Authorization: Bearer <access-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "changeType": "created,updated,deleted",
    "notificationURL": "https://example.org/hooks/outlook-calendar",
    "resource": "/me/events",
    "clientState": "langes-zufälliges-geheimnis",
    "lifecycleNotificationURL": "https://example.org/hooks/outlook-lifecycle"
  }'
```

Graph validiert die `notificationURL` mit einem `validationCode`-POST; danach liefert es JSON-Nachrichten mit `resource`, `changeType` und `clientState`.

## Rate Limits

- Graph drosselt **je App und Postfach**; bei Überschreitung kommt `HTTP 429` mit `Retry-After` (Sekunden) – dann exponentiell zurückwarten.
- Für Microsoft Graph wird ein anwendungsbezogener Richtwert von **20.000 Requests pro rollierenden 10 Minuten** genannt; Exchange-Workloads (Kalenderzugriff auf ein Postfach) haben zusätzliche, feinere Grenzwerte. Exakt dokumentierte Werte je Workload: nicht dokumentiert bzw. mandantabhängig.
- Antwort-Header zur Beobachtung: `Retry-After`, `client-request-id`, `request-id`; Drosselungsgründe stehen im Fehlerobjekt (`throttlingType`).
- Praktische Empfehlung: `calendarview` mit Zeitraum statt vieler Einzelabfragen, `$select` nutzen, Änderungen über Delta oder Webhooks statt Polling.

## Webhooks und Ereignisverarbeitung

- **Change Notifications**: `POST /subscriptions` auf `/me/events`, `/me/calendars` oder `/users/{id}/events`; Lieferung per HTTPS-POST an die registrierte URL.
- **Lebensdauer**: Abonnements laufen ab und müssen verlängert werden (`PATCH /subscriptions/{id}` mit `renewNow`). Für Exchange-Ressourcen liegen die Maximalwerte im Bereich mehrerer Tage; genaue Werte sind versionsabhängig (nicht eindeutig dokumentiert).
- **Lebenszyklus-Nachrichten**: `removed`, `renewed`, `expired`, `missedChanges` an die `lifecycleNotificationURL`.
- **Delta-Query** als Webhook-Ersatz: `GET /me/calendar/delta` liefert Änderungen samt `@odata.deltaLink` für den nächsten Durchlauf.
- **Kein klassischer ausgehender Webhook** aus der Weboberfläche: ohne Graph-App versendet Outlook keine Termin-Ereignisse an Fremd-URLs; Alternativweg ist Power Automate mit Kalender-Trigger.

## SDKs und Client-Bibliotheken

- **C#/.NET**: `Microsoft.Graph` (+ `Azure.Identity`/MSAL)
- **JavaScript/TypeScript**: `@microsoft/microsoft-graph-client`, `@azure/msal-node`, `@azure/msal-browser`
- **Python**: `msgraph-sdk` (+ `msal`)
- **Java**: `com.microsoft.graph:microsoft-graph` (+ `msal4j`)
- **Go**: `github.com/microsoftgraph/msgraph-sdk-go`
- **PowerShell**: `Microsoft.Graph`-Modul (`Get-MgUserCalendarView`, `New-MgUserEvent`)
- **Low-Code**: Graph-Connectoren in Power Automate, Power Apps und Logic Apps

```bash
npm install @microsoft/microsoft-graph-client @azure/msal-node
pip install msgraph-sdk msal
```

## Vergleich mit anderen Kalendersystemen

| System | Typischer Einstiegspunkt | Anmerkung |
|--------|--------------------------|-----------|
| Outlook Kalender | `https://graph.microsoft.com/v1.0/me/calendar/events` | OAuth 2.0 mit Entra ID |
| Nextcloud Kalender | `/.well-known/caldav` → CalDAV-Reports (XML) | Basic/Bearer-Auth, offener Standard |
| DAViCal / SabreDAV | CalDAV-Endpunkt des Servers | RFC 4791, keine REST-JSON-API |
| Google Kalender | `https://www.googleapis.com/calendar/v3/calendars` | REST + CalDAV |

## Hinweise für den Betrieb

- **App-Registrierierung in Entra ID** mit minimalen Berechtigungen: nur `Calendars.Read`, wenn nichts geschrieben wird; `Calendars.ReadWrite` nur für Postfächer, die tatsächlich benötigt werden.
- **Geheimnisse/Zertifikate** mit Ablauf hinterlegen und rotieren; Client Secrets im Klartext sind ein häufiger Audit-Fund.
- **Datenregion und Data Boundary**: Zugriffe auf Mandantendaten laufen über die Microsoft-Graph-Endpunkte; für besondere Anforderungen existieren nationale Clouds bzw. Platzhalter-Tenant-Verarbeitung (Details: nicht dokumentiert bzw. vertraglich geregelt).
- **EWS-Neuentwicklung vermeiden**: Neue Integrationen gehören auf Microsoft Graph; bestehende EWS-Nutzung: Migration planen (Zeitrahmen mandantabhängig).

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
