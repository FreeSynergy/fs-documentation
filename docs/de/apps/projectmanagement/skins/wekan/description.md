# Wekan - Beschreibung

## Was das Programm macht

Wekan holt das Trello-Prinzip auf den eigenen Server: Bretter mit Karten, dazu Swimlanen als zusätzliche Hierarchieebene und Webhooks in beide Richtungen. Es ist bewusst funktional statt schick — dafür vollständig Datenkontrolle.

## Vorteile

- **echtes Self-Hosted-Kanban** (MIT-Lizenz, Docker in Minuten)
- **Swimlanen** für Organisationsebenen, die Trello nicht bietet
- **Invoke-Hooks** = E-Mail-/Alert-Pipeline ohne Zusatztool

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Trello** | SaaS-Komfort/Power-Ups; Wekan Datenhoheit |
| **Planka** | schlanker, moderne React-Oberfläche; Wekan feldreicher (Swimlanen/Custom Fields) |
| **Focalboard (eingestellt)** | desktoplastig; Wekan bleibt aktiver Web-Dienst |

## Technische Details

- **Stack**: Node/Meteor + MongoDB, React-Client (DDP-Echtzeit)
- **Authentifizierung**: Passwort, LDAP, OAuth2 (Casdoor/Keycloak), SAML; API: persönlicher Token
- **Deploy**: Docker/Snap/K8s; S3-Backend für Anhänge
- **Lizenz**: MIT

## Für wen geeignet

- DevOps-/Selfhosting-Umgebungen mit Kanban-Bedarf und Alert-Pipelines
- FreeSynergy-Skins: Board/List/Card + Swimlane als erweitertes Kanban-Modell
