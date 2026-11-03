# Pol.is - API Dokumentation

## Übersicht

Die **Data API** (`https://pol.is/api/v3/…`, dokumentiert auf developers.pol.is) liefert Gespräche, Kommentare, Bewertungen und Cluster **lesend**. Schreiben geschieht durch die eingebettete Anwendung (Teilnehmer-Aktionen).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Data API read (`/api/v3/conversations/{id}/…`) | Kommentare, votes, clusters, math-report | offiziell |
| Embed (iframe/js) | Teilnahme in eigener Seite | offiziell |
| Write-API für Inhalte | Organisator-Import (Zugangsvergabe) | eingeschränkt |
| Webhooks/GraphQL | — | ❌ |

## Authentifizierung

- öffentliche Conversations: API-Key (Anfrage beim Betreiber) für Data-Exporte
- private Gespräche: session-basiert (Organisator-Konto)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v3/conversations/{id}/summary` | Kennzahlen |
| `GET` | `/api/v3/conversations/{id}/comments` | alle Kommentare (moderation-status) |
| `GET` | `/api/v3/conversations/{id}/votes` | Bewertungen (anonymous-voter-id) |
| `GET` | `/api/v3/conversations/{id}/math-report` | Cluster-Mathematik (group votes) |

## Beispiel

```http
GET /api/v3/conversations/12345/comments HTTP/1.1
x-api-key: <key>
```

Response (Auszug):

```json
[ { "comment_id": 903, "txt": "Mehr Bäume, weniger Parkstreifen",
    "moderation": 0, "aggregate_authorship_display": true } ]
```

## Rate Limits

API-Key-abhängig; große Exporte per Batch-Download im Organisator-Panel.

## Skin-Hinweis

Ergebnis-Skin: `math-report` → Konsens-/Gruppen-Widgets ins Wiki einbetten; Personenbezug vermeiden (anonymisierte voter-ids bleiben anonymisiert).
