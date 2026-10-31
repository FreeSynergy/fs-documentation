# Matomo - Funktionen

## Hauptfunktionen

- **volle Datenhoheit**: Events in eigener DB (MySQL/MariaDB), Export-Rohdaten, Löschrichtlinien je Site
- **Datenschutz-Modi**: cookieless-Tracking, Anonymisierung, Consent-APIs (Consent Manager integriert)
- Berichte in Tiefe (Besucher-Protokoll, Custom Segments, Funnels)
- Plugins: Heatmaps & Session Recordings (Premium), A/B-Testing, Media-Analytics
- **Tracking-HTTP-API**: `matomo.php?idsite=…` — auch für Server-/App-/CLI-Ereignisse (device ID steuerbar)

## Was Matomo NICHT kann

- keine Google-Suite-Automatik (Ads-Kopplung schwächer als GA4)
- Session-Replay/Heatmap/Tag-Manager-Anbindung teils **kostenpflichtig** (Premium-Plugins)
- Big-Data-Mengen (Milliarden-Events) → Infrastruktur-Know-how nötig (Archiv-Tabellen tun es)
- Kollaborations-Komfort (Kommentare/Sharing) dünner als GA-Umfeld

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| Analytics-REST-API (JSON) | offiziell (auch Cloud) |
| Tag Manager (Matomo-eigener GTM-Klon) | offiziell |
| WP-Plugin/Shop-Systeme | offiziell |
