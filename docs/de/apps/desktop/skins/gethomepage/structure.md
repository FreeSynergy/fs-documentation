# gethomepage (Bibliothek) - Struktur & Aufrufpfad

## Übersicht

Die Bibliothek hat kein Fenster; der Äquivalent-Begriff ist ihr **Schichten-Aufbau**. Er ist in **fünf Ebenen** gegliedert: Browser-Hook, API-Route, Deskriptor/Registry, Handler und Werkzeuge. Darunter liegen die Konfigurationsleser, die aus YAML Objekte machen. Dieser Artikel beschreibt diese Struktur, nicht die Bildschirmaufteilung des Dashboards.

## Fenster-Struktur (Schichten der Bibliothek)

```
┌──────────────────────────────────────────────────────────────────────┐
│  Browser (Dashboard)                                                 │
│  component.jsx ──► useWidgetAPI(widget, endpoint, queryParams)       │
│                        │  formatProxyUrl() → /api/services/proxy     │
├──────────────────────────────────────────────────────────────────────┤
│  Next.js-Prozess                                                     │
│  withAuth → withAllowedHost → services/proxy.js                      │
│      │  getServiceWidget(group, service, index)   (utils/config)     │
│      │  widgets[type]  (Registry: Deskriptor + Felder)               │
│      │  mappings[endpoint] → echter Endpunkt, Methode, Parameter      │
├──────────────────────────────────────────────────────────────────────┤
│  Handler-Schicht (utils/proxy/handlers)                              │
│  generic │ credentialed │ jsonrpc │ synology │ unifi │ <dienst>/proxy│
│      │  formatApiCall(api-Schablone, werte)                          │
│      │  cookie-jar (Login-Cookies)  ·  http.js (httpProxy/cached)    │
├──────────────────────────────────────────────────────────────────────┤
│  Ziel                                                                │
│  Sonarr · Pi-hole · qBittorrent · Proxmox · Docker-Socket · K8s-API   │
│      Antwort (JSON/XML/RPC) → map() → validate() → JSON an den Hook   │
└──────────────────────────────────────────────────────────────────────┘
```

## Ebenen und Dateien

| Ebene | Ort im Quellbaum | Aufgabe | Ergebnis |
|-------|------------------|---------|----------|
| Anzeige | `src/widgets/<dienst>/component.jsx` | Werte darstellen | Kachel im Raster |
| Daten-Hook | `src/utils/proxy/use-widget-api.js` | Abfrage, Intervall, Fehler | `{data, error, mutate}` |
| Route | `src/pages/api/services/proxy.js` | Parameter prüfen, Endpunkt abbilden | HTTP-Antwort |
| Schutz | `src/utils/auth.js` | Host- und Sitzungsprüfung | `400`/`401` |
| Registry | `src/widgets/widgets.js` | Typ → Deskriptor | Handlerauswahl |
| Deskriptor | `src/widgets/<dienst>/widget.js` | Schablonen, `mappings`, `fields` | erlaubte Anfragen |
| Handler | `src/utils/proxy/handlers/*`, `src/widgets/<dienst>/proxy.js` | Anfrage ausführen | Rohdaten |
| Werkzeuge | `src/utils/proxy/{api-helpers,http,cookie-jar,validate-widget-data}.js` | URL, Cookies, Prüfung | saubere Antwort |
| Config | `src/utils/config/*` | YAML → Objekte | Widget-Objekt |
| Plattform | `src/utils/{docker,kubernetes,weather,logger,env}/**` | Systemdaten, Log | Zusatzwerte |

## Aufrufpfad (Beispiel Sonarr-Queue)

```
1  services.yaml:  - Jellyfin …  - Sonarr, _sonarr: {}
2  getServiceWidget("Medien", "Sonarr", 0)
      → { type: "sonarr", url: "http://192.168.1.20:8989", key: "…", fields: […] }
3  Deskriptor sonarr: api = "{url}/api/v3/{endpoint}?apikey={key}"
4  mappings["queue"] → endpoint "queue", validate ["totalRecords"]
5  genericProxyHandler: formatApiCall →
      http://192.168.1.20:8989/api/v3/queue?apikey=…
6  http.js: follow-redirects, Timeout, Statusprüfung
7  validate-widget-data: "totalRecords" vorhanden?
8  Antwort → { totalRecords, records: […] } → Hook → Kachel
```

## UI/UX der Bibliothek

### Design-Prinzipien der Schicht

- **Whitelist statt Freiheit**: Nur hinterlegte Endpunkte sind erreichbar
- **Dünne Adapter**: Der Deskriptor enthält keine Geschäftslogik, nur Zuordnungen
- **Ein Ausgang**: Alles läuft über `http.js`, damit Redirects, Cookies und Caching einheitlich sind
- **Fehler als Daten**: Antworten enthalten `error`-Felder statt Ausnahmen bis ganz nach oben

### Namens- und Ablagekonventionen

- **Modulname klein**, identisch mit dem Widget-`type`
- **Dateinamen fest**: `widget.js`, `proxy.js`, `component.jsx`
- **Tests daneben**: `widget.test.js`, `proxy.test.js`, `component.test.jsx`
- **Konstanten im Deskriptor**, keine Hardcodierung im Handler

### Interne „Interaktionen"

- **Caching**: `cachedRequest(url, sekunden)` entscheidet über Netzwerkanfrage oder Cache-Treffer
- **Bündelung**: gleiche Schlüssel im Zeitfenster lösen nur eine Anfrage aus
- **Cookies**: werden je Dienstziel in einem Jar gehalten, bis die Sitzung abläuft
- **Neuladen des Caches**: `GET /api/revalidate` verwirft Dashboard-Daten

### Wartbarkeit und Testbarkeit

- **Kein UI nötig**, um Handler zu prüfen: Tests rufen `handler(req, res)` mit Fake-Objekten auf
- **Mock-Profile** für Dienste mit Login (Login zuerst, danach Fachanfrage)
- **Snapshot-artige Prüfungen**: erwartete Felder werden über `validate` abgesichert

### Responsive Design und Zugänglichkeit

- **Nicht anwendbar**: Die Bibliothek rendert keine Oberfläche; Zugänglichkeit ist Sache des Dashboards ([../homepage/structure.md](../homepage/structure.md))
- **Textliche Ausgaben**: Nur Fehlermeldungen, die in Komponenten erscheinen – kurz und ohne Zugangsdaten

### Performance

- **Ein Prozess, kein Pool**: Anfragen laufen nebenläufig über Node.js; lange Timeout-Ketten blockieren nicht
- **Cache-Fenster** begrenzen die Last auf Zieldienste
- **Antwortgröße reduzieren**: `map` schneidet Felder weg, bevor Daten den Browser erreichen
- **Träge Dienste** bremsen nur ihre eigene Kachel, da jeder Hook separat lädt
- **Empfehlung**: Pro Kachel höchstens ein Endpunkt pro Intervall; große Listen über `map` begrenzen

## Siehe auch

- [menu.md](menu.md) - Modul- und Paketverzeichnis
- [features.md](features.md) - Funktionen der Schicht
- [api.md](api.md) - Clients und Methoden
- [shortcuts.md](shortcuts.md) - Build- und Dev-Kommandos
- [../homepage/api.md](../homepage/api.md) - Endpunkte der Anwendung
