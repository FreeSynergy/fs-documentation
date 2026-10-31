# Helodesk - API Dokumentation

## Übersicht

Helodesk stellt eine **REST-API** (JSON) für Kontakte, Cases und Nachrichten bereit, dazu **Webhooks** für Anruf-/Case-Ereignisse. Die API ist funktional, aber kleiner als die von Zendesk/Freshdesk; Telefonie-Konfiguration (IVR) ist nur teilweise automatisierbar. Für Skin-Arbeit: Kontakt + Case lesen/schreiben, Events empfangen.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST JSON (`api.helodesk.com`) | Kontakte, Cases, Notizen, Anruf-Logs (read) | offiziell |
| Webhooks | Anruf-/Case-Events als POST | offiziell |
| Embed-Widgets | Chat/Callback/Formular per Skript | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

- API-Token (Administration → API/Entwickler) als `Authorization: Bearer <token>` (Details je Accountversion in der Helodesk-Entwicklerdoku)
- HTTPS-only; IP-Freigaben je Vertrag möglich

## Endpunkte (Konzept, Stand prüfen)

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET/POST` | `/contacts` | Kontakte suchen/anlegen (Telefon, Mail) |
| `GET/PATCH` | `/contacts/{id}` | Detail/Ändern |
| `GET/POST` | `/cases` | Cases (Filter Status/Queue) |
| `GET/PATCH` | `/cases/{id}` | Status, Owner, Custom Fields |
| `POST` | `/cases/{id}/notes` | Notiz anhängen |
| `GET` | `/calls` | Anruf-Logs (Duration, Queue, Recording-Link falls aktiv) |
| `POST` | `/webhooks` | Webhook-Endpunkte verwalten |

> Hinweis: Helodesk pflegt die Detailreferenz hinter der Entwickleroberfläche; Feldnamen vor Integration gegen die dokumentierte Schema-Referenz prüfen — hier wird bewusst nichts erfunden.

## Beispiel (Konzept)

```http
GET /cases?status=open&queue=support HTTP/1.1
Host: api.helodesk.com
Authorization: Bearer <token>
```

```json
{ "cases": [ { "id": "4821", "subject": "Reklamation", "channel": "call",
               "status": "open", "queue": "support", "contact_id": "9734" } ] }
```

## Webhooks

Events u.a.: eingehender Anruf, Case erstellt/aktualisiert, Nachricht empfangen. Payload-Formate in der Entwicklerdoku; Endpunkt mit Retry.

## Rate Limits

nicht öffentlich standardisiert; Integrationen freundlich (Backoff bei 429) gestalten.

## SDKs und Client-Bibliotheken

- offizielle SDKs: ❌; Connectoren für HubSpot/Salesforce/Pipedrive + Zapier/Make decken Standardfälle
- REST für eigene Anbindung ausreichend

## Skin-Hinweis

Kontakt-Case-Kanal-Dreiklang entspricht dem Modellansatz ([modelle.md](../../../../data/modelle.md): Contact ↔ Event/Comment ↔ Task); Recording-Links als File-Referenzen.
