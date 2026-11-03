# Node-RED - Beschreibung

## Was das Programm macht

Node-RED ist Fließband-Programmierung: Nachrichten laufen über verdrahtete Knoten, dazwischen Javascript-Stückarbeit. Es entstand für IoT (MQTT, Sensoren), deckt heute generalisierte Automation: Webhooks, Telegram-Bots, Dashboard, Home-Assistant-Logik.

## Vorteile

- **Apache-2.0, winzig, läuft auf dem Raspberry Pi** wie im Rechenzentrum
- **Echtzeit statt Batch**: Events, Timer, Protokolle
- **Gigantisches Community-Ökosystem**

## Abgrenzung

| System | Unterschied |
|--------|-------------|
| **n8n** | SaaS-Integrationen und Credential-Verwaltung; Node-RED ist Bastler-/Protokoll-Werkzeug |
| **Make/Zapier** | no-code SaaS; Node-RED ist self-hosted mit Code-Zugriff |
| **Airflow** | geplante Datenpipelines; Node-RED reagiert auf Ereignisse |

## Technische Details

- **Stack**: Node.js, Flow-Engine im Prozess, Verwaltung per Admin-REST-API
- **Dateien**: `flows.json` (+`_cred` verschlüsselt via secret)
- **Auth**: optionale `adminAuth` (read/write), keine Endnutzer-Rollen
- **Lizenz**: Apache-2.0 (OpenJS Foundation)

## Für wen geeignet

- Maker, Gebäudetechnik, HomeLab, Prototypen, Event-Pipelines
- FreeSynergy-Skins für **Node-Flow-Interaktion** (Palette/Canvas/Debug-Panel)
