# Google Analytics - Beschreibung

## Was das Programm macht

Google Analytics zählt Besuche und Ereignisse im Netz und erzählt daraus Nutzerwege. GA4 vereinheitlicht Web+App, finanziert über das Google-Ökosystem — kostenlos, mächtig, datenschutzpolitisch abwägungsbedürftig.

## Vorteile

- Kostenfreier Umfang + Google-Bündel (Search Console/Ads)
- Explorer für eigene Analysen ohne SQL
- BigQuery-Rohdaten für Data-Warehouse-Skins

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Matomo** | self-hostbar, volle Datenhoheit |
| **Plausible** | Minimalismus, cookieless, EU-hostbar |
| **Piwik PRO** | Enterprise-Privacy-Zwilling |

## Technische Details

- **Messung**: gtag.js/GTM, Server-Tags; Consent Signals
- **APIs**: Data API v4 (Report-Abruf), Management API (Verwaltung), Export (BigQuery)
- **Modelle**: Property → Streams → Events/Dimensionen; Benutzer-ID optional (Einstellungen!)

## Für wen geeignet

- Teams mit rechtskonformer Consent-Infrastruktur und Google-Stack
- FreeSynergy-Skins: Data-API-Reader für Report-Skins (mit Privacy-Hinweispflicht)
