# ERPNext – API

Das Frappe-Framework bietet eine REST-Schnittstelle. Quellen: [REST API](https://docs.frappe.io/framework/user/en/api/rest), abgerufen 2026-11-10.

| Teil | Verwendung |
|------|------------|
| `/api/resource/<doctype>` | Liste (Filter, Felder, Sortierung, Seiten) und Anlegen |
| `/api/resource/<doctype>/<name>` | Lesen, Teil-Aktualisierung, Löschen |
| `/api/method/<dotted.path>` | eine freigegebene Server-Methode aufrufen |
| Dateiupload | Endpunkt für Multipart-Upload |

## Authentifizierung

- API-Schlüssel und Geheimnis im Header `Authorization`; Anfragen laufen mit den Rollen dieses Benutzers.
- Anmeldung mit Passwort und Sitzungs-Cookie.
- OAuth-Bearer-Zugriffstoken.

Rate Limits und Webhooks: offen (die Seite behandelt sie nicht).
