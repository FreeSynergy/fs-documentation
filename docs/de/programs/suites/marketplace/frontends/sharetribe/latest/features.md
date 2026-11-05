# Sharetribe - Funktionen

## Hauptfunktionen

### Marktplatz-Grundausstattung
- Listings mit Varianten/Sperren, Kartensuche (Google Maps oder **Mapbox/OpenStreetMap-Wege je Version prüfen** — OSM-Unterstützung ausbauen), Kalender-Buchungen
- Transaktions-Prozesse: Inquiry → Angebot → Bestellung/Pre-Booking (Autorisierung) mit Stripe-Zahlungen + Auszahlungen
- beidseitige Bewertungen, Profil-Verifizierung, Chat

### Flex/Marketplace-Plattform (Entwicklerpfad)
- **API-first**: eigenes Frontend (React-Ressource-Template „default-templates“), Custom Fields/Listing types
- Webhooks für Lifecycle-Ereignisse, Marketplace-Console als Admin-Overlay

### SaaS-Varianten
- Sharetribe Go (Klick-Baukasten), Sharetribe One (aktuelles Produkt); Community-Edition = alter OSS-Zweig (Gemeinschafts-Forks)

## Was Sharetribe NICHT kann

- **kein Voll-Self-Hosting mehr für die aktuelle Version** (SaaS-Kern; OSS nur Legacy-Fork)
- keine Lagerkomplexe/Versand-Logistik (eher Dienstleistungen/lokale Vermietung)
- Auktionsformate fehlen (fixe Preise/Verhandlung)
- Payment nur Stripe (Geo-Verfügbarkeit beachten)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| REST-API + Webhooks | offiziell |
| React-Template (default-templates) | offiziell |
| Google Analytics/Pixel | eingebaut |
