# Plausible - Funktionen

## Hauptfunktionen

- **ein Skript (~1 KB), keine Cookies/IP-Kürzung nötig** → meist ohne Consent-Banner betreibbar (DSGVO-Einschätzung trotzdem dokumentieren)
- **Goals/Custom Events** (`plausible('Spende', {props:{betrag:50}})`), Funnels, Revenue
- **Stats-API**: Dashboard-Kennzahlen per HTTP (filterbar) für eigene Widgets
- Datenimport (GA/anderer Tools), GSC-Keywords, Newsletter-UTCs
- Self-hosted (ClickHouse + Elixir) oder Cloud-Abo (EU-Infra wählbar)

## Was Plausible NICHT kann

- **keine Besucher-Protokolle/Single-Visitor-Ansicht** (bewusst!)
- keine E-Commerce-Attributionstiefe (Produkt-Reports rudimentär)
- keine Session-Replays/Heatmaps
- User-Journeys/Trichter nur über Funnel-Ziele (begrenzte Komplexität)

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Stats-API + Events-API | offiziell |
| WordPress/Ghost/Shopify-Integrationen | offiziell/Community |
| Plausible-Proxy (`/plausible.io/...` selbst) | Skript-First-Party-Weg |
