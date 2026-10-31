# Sharetribe - Beschreibung

## Was das Programm macht

Sharetribe liefert das Komplettpaket, um **eigenen Marktplätzen** beizubringen, wie eBay & Co funktionieren: Anbieter stellen Angebote ein, Interessenten suchen inkl. Karte, Buchung/Bezahlung/Bewertung laufen über die Plattform mit Treuhand-Logik via Stripe.

## Vorteile

- schnellster Weg zu einem lauffähigen C2C-Marktplatz
- API-first-Pfad für eigenes Frontend (Skin-freundlich!)
- Zahlungs-/Vertrauenslayer bereits gelöst

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Arcemall/CS-Cart MV** | Shop-basierter Multivendor (Produkte/Versand); Sharetribe = Vermietung/Dienstleistung |
| **eBay/Etsy** | fremde Marktplätze; Sharetribe = eigener Marktplatz |
| **WooCommerce+Plugin** | WP-Bastelei; Sharetribe durchdachter Buchungsfluss |

## Technische Details

- **Modell**: SaaS (neue Versionen), Legacy-Community-Edition Ruby on Rails (OSS, alt)
- **Zahlen**: Stripe Connect (Auszahlungen an Anbieter)
- **APIs**: Marketplace REST API (v1), OAuth2-Client-Credentials + Nutzer-Tokens
- **Karten**: Mapbox (neu)/Google; OSM-Anbindung selbst baubar ([maps-Skins](../../../maps/index.md))

## Für wen geeignet

- Initiativen mit regionalem Tausch-/Dienstleistungsmarktplatz
- FreeSynergy-Szenarien: Angebots-/Standortmodell in [modelle.md](../../../../data/modelle.md); Listing-Geo → [standpunkte.md](../../../maps/standpunkte.md)
