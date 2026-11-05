# Plausible - Beschreibung

## Was das Programm macht

Plausible beantwortet die vier großen Fragen: Wer kam woher, was wurde gelesen, wie erfolgreich war die Kampagne, wie oft das Ziel — als eine ehrliche Seite ohne Cookie-Infrastruktur.

## Vorteile

- **Compliance-leicht** (cookieless, EU-Cloud), minimaler Wartungsaufwand
- Stats-API = Diagramm-Skins ohne Analytics-Projekt
- Importe machen Umstieg einfach

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Matomo** | volle Berichtstiefe (Besucher-Logs!); Plausible reduziert |
| **GA4** | Attributionsmaschine; Plausible Faktenseite |
| **GoatCounter** | noch simpler/Open-Source; Plausible Feature-Rand (Goals/Funnels) |

## Technische Details

- **Stack**: Elixir/Phoenix, ClickHouse (self-hosted), Edge-Ingest
- **Authentifizierung**: E-Mail/Passwort + API-Keys (Cloud/Self-host identisch nutzbar)
- **Lizenz**: AGPL (Community), kommerzielle Cloud

## Für wen geeignet

- Verbands-/Projekt-Websites, die nur Traffic verstehen wollen
- FreeSynergy-Skins:leichte Stats-Widgets über Stats-API
