# PeerTube - Beschreibung

## Was das Programm macht
PeerTube hostet hochgeladene Videos und Live-Streams, organisiert in Kanälen, mit einbettbarem Player. Die Föderation lässt Inhalte einer Instanz in anderen und im weiteren Fediverse erscheinen.

## Vorteile
- Freie Software (AGPL-3.0), ohne Werbung und ohne Bezahlmodell pro Ansicht; Urheber können einen Unterstützungslink hinzufügen.
- Föderation und optionale P2P-Auslieferung senken die Last je Instanz.
- Dokumentierte REST-API sowie eine Schnittstelle für Plugins und Themes.

## Abgrenzung
| System | Unterschied |
|--------|-------------|
| Owncast | Server für eine einzelne streamende Person; PeerTube ist eine Plattform für viele Nutzende mit Uploads. |
| YouTube Studio | Zentrale proprietäre Plattform; PeerTube ist dezentral. |

## Technische Details
Web-Client in Angular; pnpm-Workspaces; Docker wird unterstützt (README). Serversprache und Datenbank: offen.
