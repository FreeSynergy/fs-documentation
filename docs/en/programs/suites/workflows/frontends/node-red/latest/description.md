# Node-RED - Description

## What the program does

Node-RED is assembly-line programming: messages run through wired nodes, with JavaScript snippets in between. It originated for IoT (MQTT, sensors) and today covers general automation: webhooks, Telegram bots, dashboards, Home Assistant logic.

## Advantages

- **Apache-2.0, tiny, runs on a Raspberry Pi** as well as in the data center
- **Real-time instead of batch**: events, timers, protocols
- **Huge community ecosystem**

## Differentiation

| System | Difference |
|--------|-------------|
| **n8n** | SaaS integrations and credential management; Node-RED is a tinkerer/protocol tool |
| **Make/Zapier** | No-code SaaS; Node-RED is self-hosted with code access |
| **Airflow** | Scheduled data pipelines; Node-RED reacts to events |

## Technical details

- **Stack**: Node.js, flow engine in-process, managed via admin REST API
- **Files**: `flows.json` (+ `_cred` encrypted via secret)
- **Auth**: optional `adminAuth` (read/write), no end-user roles
- **License**: Apache-2.0 (OpenJS Foundation)

## Who it is for

- Makers, building technology, home labs, prototypes, event pipelines
- FreeSynergy skins for **node-flow interaction** (palette/canvas/debug panel)
