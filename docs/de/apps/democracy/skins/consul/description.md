# Consul - Beschreibung

## Was das Programm macht

Consul bündelt die klassischen Beteiligungsformate einer Stadt unter einem Dach — Vorschläge, Haushalt, Abstimmungen, Debatten — und verbindet Online mit kommunaler Verifizierung. Es entstand in Madrid („decide.madrid.es“) und wurde hundertfach weitergenutzt.

## Vorteile

- **bewährte Formatbibliothek** (Haushalte sind das Aushängeschild)
- Apache-Lizenz (agiler als Decidims AGPL)
- öffentliche API für Auswertungs-Dashboards

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Decidim** | Phasen-Prozessgerüst; Consul Formatkacheln |
| **pol.is** | Deliberations-Wellen statt Antragskatalog |
| **LiquidFeedback** | interne Gruppenentschlüsse (delegativ) |

## Technische Details

- **Stack**: Ruby on Rails, PostgreSQL
- **Auth**: Konten mit Verifizierungsstufen (konfigurierbar), OAuth2
- **Lizenz**: Apache-2.0; Deploy: Docker, klassische Rails-Server

## Für wen geeignet

- Kommunen/Regionen mit klassischer Beteiligungs-Palette
- FreeSynergy-Skins: Budget-/Support-Muster ([modelle.md](../../../../data/modelle.md))
