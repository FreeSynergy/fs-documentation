# Arcemall - API Dokumentation

## Übersicht

Arcemall stellt API-Zugänge für Marktplatz-Objekte bereit (Angebote, Buchungen, Nutzer) plus Webhooks für Statuswechsel — **der publizizierte Detailumfang ist schmal**; diese Seite erfindet keine Endpunktnamen, sondern markiert Integrationsmuster.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| REST-API (Marktplatz-Objekte) | Lesen/Schreiben von Listings/Buchungen | offiziell (Detailreferenz im Herstellerportal) |
| API-Keys im Betreiber-Cockpit | Authentifizierung | offiziell |
| Webhooks | Buchungs-/Zahlungsereignisse → Callback | offiziell |
| GraphQL/Webhooks-Signatur-Spezialfälle | — | Stand prüfen |

## Muster (schemaoffen)

```
GET  /…/listings?geo=lat,lng&r=5000        → Angebotsliste (Geo-Filter)
POST /…/bookings  { listing, slot }        → Buchungsanfrage
Webhook: booking.created / booking.confirmed → n8n/FreeSynergy-Event
```

(Feldnamen gemäß API-Doku der eingesetzten Version.)

## Beispiel-Flow (FreeSynergy)

```
FreeSynergy-DB (Angebote) → API-Import-Skript → Arcemall-Listings
Arcemall-Buchung → Webhook → FreeSynergy Termin-/Nachrichten-Skin
```

## Rate Limits

herstellerseitig; nicht öffentlich standardisiert — verhandeln.

## Skin-Hinweis

Arcemall-Skin = **Adapter-Muster** (Import + Webhook-Reader) wie bei allen Plattform-Skins; Geo-Filterung an [standpunkte.md](../../../maps/standpunkte.md) andocken.
