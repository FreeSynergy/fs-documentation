# Zammad - Beschreibung

## Was das Programm macht

Zammad bündelt Support-Anfragen aus allen Kanälen in einer gemeinsamen Timeline pro Ticket. Kunden werden wie Kontakte behandelt (Organisationen, Historie, Produkte), SLAs werden über Servicezeiten berechnet, und fast alles ist über API und Trigger automatisierbar.

## Vorteile

- **moderne UX** mit Volltextsuche und Massenspeed — deutlich über klassischen PHP-Helpdesks
- **API-first**: jeder UI-Klick ist ein API-Call; Webhooks/Trigger ersetzen Plugin-Wildwuchs
- **Self-Hosted mit klarem Pfad**: Pakete, Docker, source; Cloud-Abo optional
- **Echtes Team-Werkzeug**: geteilte Tickets, Aufgabenzuweisung, Dashboards

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **osTicket** | schlanker, PHP-Klassik ohne Elasticsearch/API-Komfort; Zammad ist schneller und API-reicher. |
| **GLPI** | ITSM mit Assets/CIs — wer Inventar braucht, nimmt GLPI; wer Support-Timeline braucht, Zammad. |
| **Request Tracker** | bewährt, aber Perl-konservativ und maskenlastig; Zammad mit modernem Frontend und Automatisierung. |

## Technische Details

- **Backend**: Ruby on Rails, Background-Jobs (DelayedJob), WebSocket-Echtzeit
- **Suche**: Elasticsearch/OpenSearch (Pflichtkomponente)
- **Datenbank**: PostgreSQL (MySQL nicht mehr unterstützt in neuen Versionen)
- **Frontend**: Vue-basiertes Web-UI, responsive
- **Authentifizierung**: intern + LDAP/OIDC/SAML/CAS/Microsoft; API-Token und OAuth2
- **Hosting**: Ubuntu/Debian-Pakete, Docker Compose, Managed Cloud
- **Lizenz**: AGPLv3

## Für wen geeignet

- Support-Teams, die E-Mail-lastige Arbeit mit moderner Maske und SLAs brauchen
- FreeSynergy-Helpdesk-Skins mit Standard-Ticket-/Comment-/User-Modell
- Migrationen aus Zendesk/RT/OTRS dank Importassistenten
