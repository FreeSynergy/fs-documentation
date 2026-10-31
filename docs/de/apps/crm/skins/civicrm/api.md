# CiviCRM - API Dokumentation

## Übersicht

CiviCRM hat zwei generationen­gleiche APIs: **APIv3** (klassisch, Entity-Action) und **APIv4** (modern, verschachtelte Abfragen). Beide sind als REST-Calls über denselben Endpoint nutzbar; dazu kommt die PHP-Programmier-Schnittstelle.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST APIv3 `civicrm/ajax/api?entity=…&action=…` | Legacy-CRUD | offiziell |
| REST APIv4 `civicrm/api4` (JSON POST) | moderne Abfragen, SearchKit-Logik | offiziell |
| PHP `civicrm_api4()` | Hooks/Extensions | offiziell |
| Webhooks | — | ❌ nur via Extension (z.B. „Webhooks“-Ext) |

## Authentifizierung

- **site_key + auth_key** (aus `civicrm.settings.php`): Signatur-API `civicrm/php/rest` für serverseitige Skripte (HMAC), oder
- **Session**: Eingeloggter Civi-Benutzer im Browser (AJAX)
- APIv4-REST `civicrm/api4` benötigt CMS-Login mit `Access CiviCRM`

## APIv3 (Beispiel)

```http
GET /civicrm/ajax/api?json={"entity":"Contact","action":"get","sequential":1,"return":["display_name","email"],"email":{"LIKE":"%example.org"}}&key=SITE_KEY&key=AUTH_KEY HTTP/1.1
```

Response:

```json
{"values":[{"id":12,"display_name":"Berg, Andrea","email":"a@example.org"}]}
```

## APIv4 (empfohlen)

```http
POST /civicrm/api4?entity=Contact&action=get HTTP/1.1
Content-Type: application/json
X-Civi-Auth: Bearer <token>   (bzw. Session)

{
  "select": ["id", "display_name", "email.email"],
  "where": [["email.is_primary", "=", true]],
  "limit": 50
}
```

Create:

```json
{
  "values": {
    "contact_type": "Individual",
    "first_name": "Andrea",
    "last_name": "Berg",
    "email": [{ "email": "a@example.org", "is_primary": true }]
  }
}
```

Wichtige Entities: `Contact`, `Email`, `Phone`, `Group`, `Contribution`, `Event`, `EventParticipant`, `Membership`, `Activity`, `Relationship`, `CustomValue`, `Mailing`.

## Batch und Sequenzen

`civicrm/api4` akzeptiert `chain`/`Batch` für Abhängigkeiten („Create Contact, then Email from last created“).

## Rate Limits

Nicht eingebaut; CMS-/Webserver-Limits und Mailing-Scheduling beachten.

## SDKs und Client-Bibliotheken

- **offiziell**: PHP (Kern), JS (`crm.api4`), **CiviCRM-API-Wrapper** für Bash (WP-CLI-ähnlich `cv`-Tool)
- **cv** (CLI): `cv api4 Contact.get +w 'email.is_primary=1'` — Referenz für Automatisierung
- Community: Python `civicrm-api`-Pakete (APIv3), Zapier-Connector

## Skin-Hinweis

Constituent-Modell (Contact + Contribution/Event/Membership als Beziehungen) → Mapping auf [modelle.md](../../../../data/modelle.md).
