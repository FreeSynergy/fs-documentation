# n8n - Description

## What the program does

n8n connects systems: a webhook triggers a flow, nodes fetch data, transform it and write it elsewhere. Everything stays as a versionable JSON workflow file and runs on your own server or in the n8n cloud.

## Advantages

- **Self-hosting + cloud** of your choice (data sovereignty!), fair license model
- **Code escape hatches**: JavaScript/Python nodes where no-code ends
- **Very fast template ecosystem**

## Differentiation

| System | Difference |
|--------|-------------|
| **Make** | More visually powerful, pure SaaS, priced by operations |
| **Zapier** | Largest app selection, no own infrastructure |
| **Node-RED** | IoT/flows, MQTT-heavy; n8n is an SaaS integration engine |

## Technical details

- **Stack**: Node.js/TypeScript, Vue editor; DB: SQLite (demo) / Postgres/MySQL; Redis optional
- **Authentication**: user+password/LDAP/SAML; API key (`X-N8N-API-KEY`); webhook auth (header/Basic)
- **Deployment**: Docker/Docker Compose, Helm (community), cloud subscription
- **License**: "Sustainable Use License" (fair-code)

## Who it is for

- Technically minded teams that want to run automation themselves
- FreeSynergy scenarios: n8n as the integration backbone between skins (API → webhook models)
