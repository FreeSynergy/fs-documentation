# Node-RED - Funktionen

## Hauptfunktionen

### Flows und Nodes
- Nachrichtenbasierte Verdrahtung (msg-Objekte), function-Nodes (JS), switch/trigger/delay-rerouting, Subflows mit Ein-/Ausgängen, Flow-Tabs
- HTTP-In/Out (REST-Server), Websockets, MQTT, MQTT-SN, CoAP, Serial/GPIO (Hardware)
- Parser (JSON/CSV/XML/YAML), Time-/Cron-Trigger, Context-Speicher (flow/global)

### Dashboards und Visualisierung
- node-red-dashboard (Pages/Groups/Widgets: Charts, Taster, Tabellen) — de facto Standard für Selbstbau-UIs
- node-red-contrib-ui (neuere UI-Bausteine)

### Betrieb
- `flows.json`/`flows_cred.json` versionierbar, Deployment-Hot-Reload, Unit-Test-Framework, `node-red-admin` CLI
- Paletten-Registry: >10.000 Community-Nodes

## Was Node-RED NICHT kann

- **kein SSO/Mandanten**: Ein-Instanz-Werkzeug ohne Benutzermodell out of the box
- **keine grafische Daten-Transformation ohne JS** (im Vergleich zu n8n-Edit-Fields)
- **kein Batch-Scheduling großer Datenmengen** (Airflow) — Echt-Nachrichten, keine Jobsuiten
- **Dashboard-Widgets veraltet technisch** (AngularJS-Linie) für neue Projekte abwägen
- Web-Serverschutz (`adminAuth`) nötig — ohne Konfiguration offen!

## Erweiterungen und Integrationen

| Integration | Weg |
|-------------|-----|
| npm-Paletten | Settings → Palette |
| Home Assistant/Ethernet/IP/Modbus | Community-Nodes |
| REST via HTTP-Nodes | eigener Endpunkt pro Flow |
