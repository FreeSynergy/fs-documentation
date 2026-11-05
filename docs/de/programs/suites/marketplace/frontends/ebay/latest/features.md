# eBay - Funktionen

## Hauptfunktionen

- **Formate**: Auktion, Sofort-Kaufen, Preisvorschlag; Lokale Abholung (standortbezogen — Maps-Bezug)
- **Seller-Werkzeuge**: Bulk-Listings (File Exchange), Preis-/Lager-API, Promotions, Versandlabels
- **Katalog-/Kategoriesystem** (Browse API) mit Produkt-Identifikatoren (MPN/GTIN)
- Käuferschutz/Betrugserkennung, Bewertungs-Double-Opt-In, fallbasierte Streitbeilegung (falls)

## Was man NICHT darf / eBay NICHT kann

- **kein Vollzugriff**: APIs erlauben Listings/Bestellungen, aber keine Community-Features (Chats nur beschränkt), keine Webhooks an beliebige Endpunkte (Notification-Systeme je API nutzen)
- Kontosperren bei Regelverstößen — Automatisierung muss Policies einhalten
- Auktionsmechanik ist proprietär; kein Export kompletter Marktplatz-Daten
- Gebührenstruktur macht Kleinstmengen unattraktiv

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Sell/Browse/Inventory/Fulfillment/Marketing API | offiziell (Zulassungsstufen) |
| Notification-Systeme (pull/`getListings`-poll vs. Push je API) | offiziell |
| WaWi/ERP-Konnektoren (lexoffice, JTL…) | Partner |
