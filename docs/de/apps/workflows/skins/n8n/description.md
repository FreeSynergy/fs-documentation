# n8n - Beschreibung

## Was das Programm macht

n8n verbindet Systeme: Ein Webhook löst einen Ablauf aus, Nodes holen Daten, transformieren sie, schreiben sie woanders hin. Alles bleibt als JSON-Workflow-Datei versionierbar und läuft auf dem eigenen Server oder in der n8n-Cloud.

## Vorteile

- **Self-Hosting + Cloud** wählbar (Datenhoheit!), faires Lizenzmodell
- **Code-Fluchtventile**: JavaScript/Python-Nodes, wo No-Code endet
- **Template-Ökosystem** enorm schnell

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **Make** | visuell-mächtiger, reines SaaS, Preis nach Operations |
| **Zapier** | größte App-Auswahl, keine eigene Infrastruktur |
| **Node-RED** | IoT/Flows, MQTT-lastig; n8n ist SaaS-Integrationsmaschine |

## Technische Details

- **Stack**: Node.js/TypeScript, Editor Vue; DB: SQLite (Demo) / Postgres/MySQL; Redis optional
- **Authentifizierung**: User+Pass/LDAP/SAML; API-Key (`X-N8N-API-KEY`); Webhook-Auth (Header/Basic)
- **Deploy**: Docker/Docker Compose, Helm (Community), Cloud-Abo
- **Lizenz**: „Sustainable Use License“ (fair-code)

## Für wen geeignet

- Techniknahe Teams, die Automatisierung selbst betreiben wollen
- FreeSynergy-Szenarien: n8n als Integrations-Rückgrat zwischen Skins (API → Webhook-Modelle)
