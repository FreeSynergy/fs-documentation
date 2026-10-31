# Trello - Beschreibung

## Was das Programm macht

Trello visualisiert Arbeit als Spalten mit Karten — der Zustand einer Sache ist ihre Position. Es ist bewusst einfach: jede:r versteht es ohne Schulung, Automatisierung kommt später per Butler und Power-Ups.

## Vorteile

- **Einstieg in Minuten**, kostenlos solide
- **Flexibel**: Retrospektiven, Recruiting-Pipelines, Inhaltskalender
- **API sauber und stabil** — Prototyp einer guten Kanban-Schnittstelle

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Jira** | Issue-Tracking mit Workflows/Sprints; Trello bleibt Brett |
| **Planka** | Self-Hosted-Klon mit fast gleicher Mechanik, ohne Power-Up-Ökosystem |
| **Asana** | Aufgaben statt Karten mit Feldtiefe; Trello ist positioneller |

## Technische Details

- **Modell**: SaaS (Atlassian), Boards in Workspaces
- **Authentifizierung**: Atlassian-Konto (Passwort/SSO); API: REST-Key+Token bzw. OAuth2 für Power-Ups
- **Offline/Mobil**: Apps mit Basis-Offline-Persistenz
- **Tarife**: Free/Standard/Premium/Enterprise

## Für wen geeignet

- Teams, die Status visueller als felddetailsbedürftig ist
- FreeSynergy-Skins: Trello-Boardmodell (Board/List/Card/Label/Checklist) als kanonischer [Task-Skin](../../../../data/modelle.md)
