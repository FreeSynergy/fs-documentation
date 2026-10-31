# Matomo - Beschreibung

## Was das Programm macht

Matomo ist Web-Analyse mit eigenen Regeln: Tracking-Code rein, Berichte raus — und alles liegt im eigenen Keller. Die Datenschutz-Modi (cookieslos, Consent-APIs) machen es zum Standard-Replace für GA in deutschen Kommunal-/Verbandswebsites.

## Vorteile

- **DSGVO-tauglich by design** (Self-Hosting, keine Drittübermittlung)
- GA-Import (Daten aus GA importierbar) für Migration
- Tracking-HTTP-API = serverseitige Ereignis-Skins ohne Browser

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **GA4** | kostenlos/Google-Kopplung; Matomo Datenhoheit |
| **Plausible** | noch minimalistischer (eine Zahl, ein Skript); Matomo volle Berichtstiefe |
| **Piwik PRO** | Privacy-Enterprise-Zwilling (kommerziell) |

## Technische Details

- **Stack**: PHP 8, MySQL/MariaDB (Archiv-Tabellen + Visitors/Visits), Optional: Redis
- **Auth**: Login + `token_auth` (API), 2FA
- **Deploy**: Shared-Hosting-tauglich, Docker-Images offiziell, Matomo Cloud
- **Lizenz**: GPL (Core), Premium-Plugins kommerziell

## Für wen geeignet

- Organisationen mit Compliance-Pflicht + Analyseanspruch
- FreeSynergy-Skins: Matomo als Standard-Analytics-Layer ([modelle.md](../../../../data/modelle.md): Ereignis→Besuch→Conversion)
