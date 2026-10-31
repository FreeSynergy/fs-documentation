# Hotjar - API Dokumentation

## Übersicht

Hotjars API ist **Lese-API für Organisation/Recordings/Surveys** plus **Identify-API** im Tracking-Skript. Heatmap-Rohdaten sind nicht API-exponiert (nur UI/Reports).

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST `https://data.hotjar.com/v1/…` (Team-Token) | Recordings, Survey-Antworten | offiziell |
| Identify-API (`hj('identify', id)`) | Nutzer-Zuordnung im Tracking | offiziell |
| Site-Management (API) | Sites/Mitglieder | eingeschränkt |
| Webhooks | — | ❌ |
| GraphQL | — | ❌ |

## Authentifizierung

- API-Token pro Team (Einstellungen → API): `Authorization: Bearer <token>` (Daten-API)
- Identify: Skript-Konfiguration, kein Token im Public-Code

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v1/sites/{site_id}/recordings` | Recordings (Filter erstellt/Seiten) |
| `GET` | `/v1/sites/{site_id}/recordings/{uuid}` | Metadaten einer Sitzung |
| `GET` | `/v1/sites/{site_id}/surveys/{id}/responses` | Umfrageantworten |

*(Endpunkt-Namen gemäß aktueller Entwickler-Doku; Version/Plan prüfen.)*

## Beispiel

```http
GET /v1/sites/123456/recordings?limit=50&after=2026-10-01 HTTP/1.1
Authorization: Bearer <team-token>
```

Response: `{ "recordings": [ { "id": "…", "pages": [...],
"rage_click_count": 2, "visitor_id": "…" } ] }`

Identify (im Seiten-Code):

```js
_hj('identify', 'teilnehmer-4711');
```

## Rate Limits

dokumentiert pro Team (moderat); Interview-/Recording-Volumen je Abo begrenzt.

## Skin-Hinweis

Datenschutz-Vorbehalt: Replays nur mit Consent + Masken; FreeSynergy-Skin verlinkt Heatmap-Befunde auf Issue-Skins (Rage-Click → Bug-Ticket via Zapier-Kette).
