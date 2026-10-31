# gethomepage (Bibliothek) - API der Bibliotheksschicht

## Übersicht

Diese Datei beschreibt die **Programmier-Schnittstelle der Clientschicht**: welche Funktionen es gibt, welche Parameter sie erwarten und was sie zurückgeben. Zwei Schnittstellen sind relevant:

1. **Browser → Anwendung**: Der Hook `useWidgetAPI` und die davon erzeugte Proxy-URL
2. **Server intern**: Deskriptor-Objekte, Handler-Funktionen und die Werkzeugfunktionen in `src/utils/proxy/`

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| JavaScript-Module (ESM) | interner Aufruf innerhalb der Anwendung | maßgebliche Schnittstelle |
| HTTP/JSON `/api/services/proxy` | Datenabruf aus dem Browser | intern, nicht versioniert |
| npm-Paket | ❌ Nicht vorhanden – die Schicht ist nicht veröffentlicht | — |
| Webhooks | ❌ Nicht vorhanden | — |
| GraphQL | ❌ Nicht vorhanden | — |

## Authentifizierung und Sicherheit der Clients

- **Keine eigene Authentifizierung**: Die Schicht erbt den Schutz der Anwendung (Host-Prüfung, optional Sitzungsanmeldung).
- **Dienst-Zugangsdaten** kommen aus der Konfiguration (`key`, `key2`, `username`/`password`, Token) und werden je Handler unterschiedlich verwendet: Query-Parameter, Header oder Login-Ablauf.
- **Secrets aus Umgebung**: `{{HOMEPAGE_VAR_*}}` und `{{HOMEPAGE_FILE_*}}` werden beim Laden eingesetzt, damit keine Schlüssel in Dateien stehen.
- **Cookies** für Login-Dienste leben in einem eigenen Jar im Prozess und werden nicht an den Browser ausgegeben.

## Kern-API der Module

### Deskriptor (`src/widgets/<dienst>/widget.js`)

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `api` | String | Schablone, z. B. `{url}/api/v3/{endpoint}?apikey={key}` |
| `apiv5` … | String | weitere Schablonen für alternative Versionen |
| `proxyHandler` | Function | Handlermodul, sonst generischer Handler |
| `fields` | Object | Pflichtfelder der Konfiguration, z. B. `{ key: true, version: false }` |
| `mappings` | Object | erlaubte Endpunkte mit `endpoint`, `method`, `body`, `params`, `optionalParams`, `segments`, `headers`, `map`, `validate` |
| `primaryField` | String | Kennzeichnung des Hauptwerts für die Kachel |

### Browser-Hook

```javascript
// useWidgetAPI(widget, endpoint, queryParams, swrConfig)
const { data, error, mutate } = useWidgetAPI(widget, "queue", { limit: 5 });
```

| Parameter | Bedeutung |
|-----------|-----------|
| `widget` | Widget-Objekt aus der Konfiguration (Typ, URL, Gruppenname, Index) |
| `endpoint` | Schlüssel aus `mappings`; leerer String unterdrückt die Anfrage |
| `queryParams` | zusätzliche Parameter, als JSON im Query-Parameter `query` |
| `swrConfig.refreshInterval` | Aktualisierungsintervall in Millisekunden |

Erzeugte URL: `/api/services/proxy?group=<gruppe>&service=<name>&index=<n>&endpoint=<ep>&query=<json>`

### Werkzeugfunktionen (`src/utils/proxy/api-helpers.js`)

| Funktion | Signatur | Ergebnis |
|----------|----------|----------|
| `formatApiCall` | `(schablone, werte)` | einsatzfertige URL, Platzhalter ersetzt |
| `parseVersionForUrl` | `(version, Standard)` | numerische Version für URL-Bausteine |
| `getURLSearchParams` | `(widget, endpoint)` | `URLSearchParams` mit `group`, `service`, `index` |
| `formatProxyUrl` | `(widget, endpoint, queryParams)` | Proxy-URL für den Browser |
| `asJson` | `(daten)` | geparstes JSON oder Original |
| `jsonArrayTransform` | `(daten, transform)` | transformiertes Array |

### HTTP-Schicht (`src/utils/proxy/http.js`)

| Funktion | Signatur | Ergebnis |
|----------|----------|----------|
| `httpProxy` | `(url, options)` | Antwort (Status, Headers, Body) einer einzelnen Anfrage |
| `cachedRequest` | `(url, sekunden)` | Antwort aus dem Cache oder frisch geladen |
| Redirect-Handling | – | folgt Umlenkungen über `follow-redirects` |

### Handler-Vertrag (`src/utils/proxy/handlers/*`)

```javascript
// jeder Handler: async (req, res) => void
async function genericProxyHandler(req, res) {
  const widget = getServiceWidget(req.query.group, req.query.service, req.query.index);
  const url = formatApiCall(widget.api, { url: widget.url, endpoint: req.query.endpoint, key: widget.key });
  const response = await httpProxy(url, { headers, method: req.method, body: req.body });
  return res.status(response.status).json(antwort);
}
```

## Endpunkte der Clientschicht

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/services/proxy` | generischer Datenabruf je konfiguriertem Dienst |
| `GET` | `/api/services/proxy?endpoint=<name>` | über `mappings` freigegebener Endpunkt |
| `GET` | `/api/services/proxy?segments=<json>` | Pfadsegmente (IDs) für Endpunkte mit Platzhaltern |

## Client-Beispiele je Diensttyp

| Dienst | Schablone | Authentifizierung | typischer Endpunkt |
|--------|-----------|-------------------|--------------------|
| Sonarr/Radarr | `{url}/api/v3/{endpoint}?apikey={key}` | API-Key in Query | `queue`, `series`, `history` |
| Pi-hole (V6) | `{url}/api/{endpoint}` | Session/Login intern | `stats/summary` |
| qBittorrent | `{url}/api/v2/{endpoint}` | Login → Cookie | `transfer/info`, `torrents/info` |
| Jellyfin | `{url}/api/{endpoint}` | `api_key` | `Sessions` |
| Proxmox | `{url}/api2/json/{endpoint}` | Token-Header | `nodes`, `cluster/resources` |
| UniFi | eigener JSON-RPC-Ablauf | Benutzer/Passwort | Status- und Client-Listen |
| Synology | `{url}/webapi/entry.cgi` | Session (`_sid`) plus OTP möglich | `SYNO.API.Auth`, `SYNO.Core.*` |

## Beispiele

### Handler-Aufruf im Test (Vitest)

```javascript
import genericProxyHandler from "utils/proxy/handlers/generic";

test("Sonarr queue", async () => {
  const req = {
    method: "GET",
    query: { group: "Medien", service: "Sonarr", index: 0, endpoint: "queue" },
  };
  const res = { status: () => res, json: (body) => (res.body = body) };
  await genericProxyHandler(req, res);
  expect(res.body.totalRecords).toBeDefined();
});
```

### Neuer Endpunkt in einem bestehenden Dienst

```javascript
// src/widgets/sonarr/widget.js – Ausschnitt
const widget = {
  api: "{url}/api/v3/{endpoint}?apikey={key}",
  proxyHandler: genericProxyHandler,
  mappings: {
    history: { endpoint: "history", validate: ["totalRecords"] },
    "series/detail": {
      endpoint: "series/{id}",
      segments: ["id"],
      map: (data) => ({ title: asJson(data).title, id: asJson(data).id }),
    },
  },
};
```

### Aufruf aus einem Skript (gegen die laufende Anwendung)

```bash
curl -s -H "Host: homepage.example.internal" \
  "http://localhost:3000/api/services/proxy?group=Medien&service=qBittorrent&index=0&endpoint=transfer%2Finfo"
```

Antwort (gekürzt):

```json
{ "speed": { "down": 1048576, "up": 20480 }, "queueing": { "active": 3, "inactive": 12 } }
```

## Rate Limits, Caching und Zeitverhalten

- **Prozess-Cache** über `memory-cache`; identische Anfragen innerhalb des Fensters treffen den Zieldienst nicht erneut
- **Keine Ratenbegrenzung** in der Schicht selbst – begrenzt durch Widget-Intervalle
- **Sitzungs-Logik**: Login-Cookies werden wiederverwendet; bei abgelaufener Sitzung erfolgt ein erneuter Login
- **Empfehlung**: Intervall nicht unter 10 Sekunden setzen, damit Medien- und DNS-Dienste nicht belastet werden

## Ereignisse und Webhooks

- **Keine Ereignisausgabe**: Die Schicht fragt ab (Pull), sie sendet nichts nach außen
- **Reaktiv im Browser**: SWR löst Intervall-Abfragen aus; `mutate` erzwingt einen neuen Abruf
- **Cache-Neuaufbau von außen**: `GET /api/revalidate` verwirft zusammengesetzte Dashboard-Daten

## SDKs und eigene Nutzung

- **Kein offizielles SDK oder npm-Paket** (geprüft: `@gethomepage/homepage` existiert nicht im npm-Register)
- **Nur Weg**: Quellbaum forken, Modul ergänzen, Tests schreiben, Pull Request einreichen
- **Für eigene Projekte**: die HTTP-Abrufe der Zieldienste direkt mit `fetch`/`axios` nachbauen oder die SDKs des jeweiligen Dienstes nutzen

## Hinweise für Entwickler

- Neue Endpunkte **immer** über `mappings` freigeben, nie per freier Pfadübergabe
- Antworten mit `validate` absichern, damit Umbauten im Zieldienst früh auffallen
- Keine Zugangsdaten in Log oder Fehlermeldungen ausgeben
- Sonderfälle (Login, RPC, XML) in einem eigenen `proxy.js` bündeln, nicht im Deskriptor
- Kurzdoku im Modul-Kommentar: welche Endpunkte warum freigeschaltet sind

## Siehe auch

- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menu.md) (Modul- und Paketverzeichnis)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [../homepage/api.md](../homepage/api.md)
