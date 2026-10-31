# Sharetribe - API Dokumentation

## Übersicht

Die **Marketplace API** (`https://api.sharetribe.com/v1/`, JSON) ist das Herz der Flex/One-Plattform: Listings, Nutzer, Buchungen, Transactions, Bewertungen, Bilder, Webhooks. Eigene Frontends bauen darauf.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST v1 (`/listings`, `/people`, `/bookings`, `/transactions`, `/reviews`) | Marktplatz-CRUD | offiziell |
| OAuth2 (Client-Credentials; `Sharetribe-Application-Key`, `Sharetribe-Marketplace-ID`-Header) | App-Auth | offiziell |
| Webhooks | Transaktions-/Listing-Ereignisse (signiert) | offiziell |
| GraphQL | — | ❌ |

## Authentifizierung

```
POST /v1/token  (grant_type=client_credentials)
→ access_token (App-Identität; für Nutzer-Aktionen `On-Behalf-Of: <userId>`-Header)
```

## Kernendpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/v1/listings/search?public_search=…&lat=&lng=&bound_n_km=5` | Suche (Geo!) |
| `POST` | `/v1/listings` | Listing anlegen (listing_type, price, images) |
| `POST` | `/v1/images` | Bild-Upload (Base64) |
| `POST` | `/v1/people/create` | Nutzer registrieren |
| `POST` | `/v1/booking` | Buchung anfragen (listing, start/end) |
| `POST` | `/v1/transactions/initiate` | Transaction starten (prozesstyp-abhängig) |
| `POST` | `/v1/transactions/{id}/accept|transition` | Prozess-Schritte |
| `GET` | `/v1/reviews?listing=…` | Bewertungen |

## Beispiel

Geo-Suche:

```http
GET /v1/listings/search?public_search=fahrrad%20lenen&
    lat=52.517&lng=13.404&bound_n_km=6 HTTP/1.1
Authorization: Bearer <token>
Sharetribe-Application-Key: <app-key>
Sharetribe-Marketplace-ID: <mp-id>
```

Response: `{ "data": [ { "id": "…", "attributes": { "title": "Lastenrad",
"price": { "amount": 1200, "currency": "EUR" }, "publicData": { "location": … }}}],
"meta": { "totalItems": 14 } }`

## Webhooks

Console → Integrationen: Events (`transaction transition requested/accepted`, `new listing`) → POST mit `X-Sha1-HMAC`-Signatur (Secret).

## Rate Limits

Dynamisch nach Marketplace-Volumen dokumentiert (Spikes throttled; 429 mit Backoff).

## Skin-Hinweis

Listing-`publicData.location` = GeoJSON-Anschluss an Maps-Skins; Transaktions-/Prozessmodell → [modelle.md](../../../../data/modelle.md) (Angebot/Anfrage/Zusage/Bewertung).
