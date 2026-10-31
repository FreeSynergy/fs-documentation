# Adhocracy4 - API Dokumentation

## Übersicht

Adhocracy4 exponiert **REST-Endpunkte pro Modul** (Ideas, Comments, Ratings, Projects, Maps-Punkte; JSON, Token-Auth für Schreibzugriffe). Auswertungs-Dashboards lesen direkt über die API.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `…/ideas/`, `…/comments/`, `…/ratings/`, `/api/projects/` | Modul-CRUD (lesend offen, schreiben auth) | offiziell |
| Token-Auth (Nutzer-Token im Header) | Schreibzugriff | offiziell |
| Export (CSV, Verwaltung) | Projektdaten sichern | offiziell |
| Webhooks/GraphQL | — | ❌ |

## Authentifizierung

- Lesend: öffentlich (sichtbare Projekte)
- Schreibend: `Authorization: Token <user-token>` (Session-Token der Plattform)

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/projects/{id}/` | Projektmeta (Phasen, Module) |
| `GET` | `/ideas/?project={id}` | Ideenliste (Modul-Pfad je Deployment) |
| `GET/POST` | `…/ideas/{id}/comments/` | Kommentare |
| `GET/POST` | `…/ideas/{id}/ratings/` | Ratings (point +1/-1/0) |
| `POST` | `/ideas/` | Idee anlegen (API-Clients = Moderation) |

## Beispiel

Request:

```http
GET /api/modules/87/ideas/?ordering=-positive_rating_count HTTP/1.1
Accept: application/json
```

Response:

```json
{ "count": 142, "results": [
  { "id": 903, "name": "Brunnen statt Parkstreifen",
    "positive_rating_count": 31, "comment_count": 7,
    "point": { "type": "Point", "coordinates": [13.404, 52.517] } } ] }
```

## Rate Limits

deployment-seitig (Standard: keine dokumentierten harten Limits).

## Skin-Hinweis

`point`-GeoJSON = Andockpunkt an Maps-Skins ([standpunkte.md](../../../maps/standpunkte.md)); Rating-Zähler in [modelle.md](../../../../data/modelle.md) „Support“ abbilden.
