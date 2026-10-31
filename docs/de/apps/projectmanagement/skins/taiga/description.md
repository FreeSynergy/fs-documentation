# Taiga - Beschreibung

## Was das Programm macht

Taiga ist schlanke, schöne Agile-Software zum Selbsthosten: ein Projekt wählt Scrum oder Kanban, Epics halten das Große im Blick, Issues den Alltag. Als AGPL-Projekt (früher Taiga project, heute mit kommerziellem SaaS-Betrieb) ist es die offenste unter den modernen Agile-Suiten.

## Vorteile

- **schnell + hübsch**: wenige Klicks, klare Tafeln
- **selbst hostbar** (Docker), Cloud optional
- **Dev-Integration**: Referenzen/Branches aus Git heraus

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **OpenProject** | umfassender (Gantt/CPM, Kosten, Zeiterfassung); Taiga agiler/schlanker |
| **Redmine** | altgedient, pluginlastig; Taiga modern |
| **Jira** | Workflow-Tiefe/Kommerz; Taiga OSS-Einfachheit |

## Technische Details

- **Backend**: Python/Django (taiga-back), PostgreSQL, RabbitMQ (Events), Celery
- **Frontend**: Taigo (Angular), separate Services (events, subscriptions)
- **Auth**: OAuth2 (Passwort-Grant für Skripte), Bearer-Tokens; LDAP/OIDC (Enterprise)
- **Deploy**: offizielle Docker-Compose, Helm-Charts (Community), Taiga Cloud SaaS
- **Lizenz**: AGPL (Core)

## Für wen geeignet

- kleine/mittlere Dev-Teams, die OSS + Scrum/Kanban ohne Ballast wollen
- FreeSynergy-Skins: Sprint/Story/Epic-Begriffe direkt als Agile-Modell ([modelle.md](../../../../data/modelle.md))
