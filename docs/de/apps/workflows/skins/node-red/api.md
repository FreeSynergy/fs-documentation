# Node-RED - API Dokumentation

## Übersicht

Node-RED stellt zwei API-Flächen: (1) selbst definierte HTTP-Endpunkte über **HTTP-In-Nodes** (die eigentliche Integrations-API), (2) die interne **Admin-REST-API** (Flows verwalten) sowie Dateiaustausch über `flows.json` und `node-red-admin`.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| HTTP-In/Out (`http://host:1880/<pfad>`) | eigene REST/Webhook-Endpunkte | offiziell (Nutzerdesign) |
| Admin-REST `/<adminRoot>/flows` | Flow-JSON lesen/schreiben | offiziell-intern |
| MQTT/WebSocket | Message-Busse | offiziell |
| Webhooks (outbound) | via Function/HTTP-Request-Nodes | DIY |
| GraphQL | — | ❌ |

## Authentifizierung

- HTTP-Endpunkte: selbst gebaut (z.B. `httpNodeAuth` Basic-Auth, Token-Check im Function-Node)
- Admin-API: `adminAuth` in `settings.js` (Login-Cookie/Basic), `read/write`-Stufen

## Admin-Endpunkte

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/flows` | komplette Flow-JSON |
| `POST` | `/flows` | Flows ersetzen (Deploy) |
| `POST` | `/flow` | einzelner Flow-Tab |
| `GET` | `/nodes` | laufende Nodes + Status |
| `POST` | `/nodes/<id>/inject` | inject-Knoten auslösen |
| `POST` | `/settings` | Node-RED-Version/Settings lesen |

## Beispiel: Webhook-Endpunkt (HTTP-In)

HTTP-In-Node `POST /hooks/ticket`:

```json
// eingehend
{ "ticket": { "id": 9982, "state": "closed" } }
```

Function-Node:

```js
if (msg.payload.ticket?.state === "closed") {
  node.warn("Ticket " + msg.payload.ticket.id + " geschlossen");
  return msg; // → HTTP-Response
}
return null;
```

## flows.json als Austauschformat

Import/Export über Kopfmenü oder `node-red-admin import`; Credentials-Export separat und verschlüsselt.

## Rate Limits

Instanzseitig (Node.js-Prozess); HTTP-Limits über Reverse Proxy.

## SDKs und Client-Bibliotheken

- `node-red-admin` (CLI), `flows` JSON-Schema in Doku
- REST-Test-Tools: jeder HTTP-Client

## Skin-Hinweis

Node+Draht-Modell = [Flow-Modell](../../../../data/modelle.md): Knoten mit Ports, msg-Payload als Standard-Nachrichtenformat.
