# Unraid - API Dokumentation

## Übersicht

Unraid hatte über Jahre **keine offiziell dokumentierte Kern-API**: Automatisierung lief über Config-Dateien auf dem USB-Stick und über die (undokumentierten) Endpunkte der PHP-WebUI. Das ändert sich mit aktuellen Versionen: Unraid ergänzt offiziell eine **GraphQL-API** (`unraid-api`) mit API-Keys, Session-Cookies und optionaler OIDC-Authentifizierung. Beide Welten koexistieren — für bestandskritische Skripte gilt weiter: Nur dokumentierte GraphQL-Felder verwenden, Dateiabfragen nur als Übergangslösung.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| GraphQL (`/graphql`) | Systeminfo, Array, Docker, Connect-Einstellungen | Offiziell dokumentiert (aktuelle Versionen) |
| WebUI-Endpunkte (PHP) | Formulare, Pluginaufrufe | Undokumentiert, nicht stabil |
| Config-Dateien (`/boot/config`) | Shares, Identifikation, Array-Metadaten | Stabiles Format, aber kein Dienst |
| Webhooks (ausgehend) | Benachrichtigungen an externe Dienste | Offiziell, ab Version 6.12 (versionabhängig) |
| Webhooks (eingehend) | — | ❌ Nicht vorhanden |

## Authentifizierung

- **API-Keys**: Verwaltet unter **Settings → Management Access → API Keys** (Anlegen, Rollen, Widerrufen). Der Key wird im Header `x-api-key` mitgeführt.
- **Rollen**: `admin` (voller Zugriff), `connect` (Remote-Access-Funktionen), `guest` (eingeschränkt lesend).
- **Session-Cookies**: Im Browser angemeldete WebUI-Sitzungen funktionieren direkt gegen `/graphql` — praktisch zum Testen, ungeeignet für Skripte.
- **SSO/OIDC**: Bei konfiguriertem externen Provider (versionabhängig) läuft die API-Authentifizierung darüber.
- **Historisch**: WebUI-Formulare nutzten die WebUI-Anmeldung; für undokumentierte Endpunkte gab es keine offizielle Token-Authentifizierung.

## GraphQL-Endpunkte und Schema

| Endpunkt | Methode | Beschreibung |
|----------|---------|--------------|
| `/graphql` | `POST` | GraphQL-Operationen (Abfragen und Mutationen) |
| `/graphql` (Sandbox) | Browser | interaktiver Playground; aktivieren unter Settings → Management Access → Developer Options |

Wurzelfelder (Auswahl, vollständiges Schema in der Apollo-Studio-Referenz):

| Feld | Inhalt |
|------|--------|
| `info` | Betriebssystem, CPU, Arbeitsspeicher, Mainboard |
| `array` | Array-Status, Kapazität, Laufwerksliste mit Temperatur/Status |
| `dockerContainers` | Container mit Name, Zustand, Autostart |
| `config` | Serverkonfiguration (lesend) |
| `connect` | Remote-Access-/Connect-Einstellungen (Rolle `connect`/`admin`) |

## Beispiele

### Abfrage: Systemstatus (curl)

```bash
curl -s -X POST http://UNRAID_IP/graphql \
  -H "Content-Type: application/json" \
  -H "x-api-key: DEIN_API_KEY" \
  -d '{"query": "query { info { os { platform distro release uptime } cpu { manufacturer brand cores threads } } }"}'
```

Antwort (gekürzt):

```json
{
  "data": {
    "info": {
      "os": { "platform": "linux", "distro": "Unraid", "release": "7.x", "uptime": "..." },
      "cpu": { "manufacturer": "Intel", "brand": "...", "cores": 8, "threads": 16 }
    }
  }
}
```

### Abfrage: Array- und Laufwerksstatus

```bash
curl -s -X POST http://UNRAID_IP/graphql \
  -H "Content-Type: application/json" \
  -H "x-api-key: DEIN_API_KEY" \
  -d '{"query": "query { array { state capacity { disks { free used total } } disks { name size status temp } } }"}'
```

### Abfrage: Container

```bash
curl -s -X POST http://UNRAID_IP/graphql \
  -H "Content-Type: application/json" \
  -H "x-api-key: DEIN_API_KEY" \
  -d '{"query": "query { dockerContainers { id names state status autoStart } }"}'
```

### Fehlerformat

```json
{
  "errors": [
    { "message": "Error description", "locations": ["..."], "path": ["..."] }
  ]
}
```

### Mutationen (Array, Container)

Das Schema enthält Mutationen für Array-Operationen und Docker-Verwaltung; die exakten Feldnamen stehen ausschließlich in der offiziellen Schema-Referenz (Apollo Studio bzw. Sandbox). Für Skripte vor Produktionsnutzung dort prüfen — diese Dokumentation nennt keine unbelegten Mutationsnamen.

## CLI-Werkzeuge

| Befehl | Funktion |
|--------|----------|
| `unraid-api developer --sandbox true` | GraphQL-Sandbox aktivieren (interaktiv: `unraid-api developer`) |
| `unraid-api status` | Status der API-Komponente prüfen |
| `unraid-api report` | Berichts-/Debug-Ausgabe für Support |
| `unraid-api --help` | Übersicht aller Kommandos |

## Rate Limits und Betriebshinweise

- Die API implementiert **Ratenbegrenzungen** (Details nicht öffentlich beziffert); Antworten bei Überschreitung sauber behandeln.
- Abfragekomplexität begrenzen — viele Felder und verschachtelte Listen auf einmal erhöhen die Last.
- API-Keys rotationfähig halten und nach Rolle trennen (`guest` für Überwachung, `admin` nur für Wartungsskripte).
- undokumentierte WebUI-Endpunkte können sich mit jedem Update ändern — nicht für Produktionsautomatisierung verwenden.

## Webhooks

- **Ausgehend**: Der Benachrichtigungsdienst kann Ereignisse (Array-Fehler, Vollmeldungen u. a.) als **Webhooks** an externe Endpunkte senden (einrichten unter Settings → Notifications, ab Version 6.12, versionabhängig).
- **Eingehend**: Es gibt keine Webhooks/Callbacks, mit denen externe Systeme Unraid steuern; dafür ist die GraphQL-API zuständig.

## SDKs und Client-Bibliotheken

- **Kein offizielles SDK**; der Server ist ein Apollo-/GraphQL-Server, jeder GraphQL-Client (`axios-fetch`, `graphql-request`, `ApolloClient`) funktioniert.
- **`pyunraid`** (Community, Python) spricht die WebUI-Endpunkte an — praktisch, aber an undokumentierte Details gebunden.
- **Schema-Referenz**: Apollo GraphQL Studio (`Unraid-API`, Variante *current*) als einzige maßgebliche Feldreferenz.
- **Cron-Skripte** mit `curl` + `x-api-key` bleiben der einfachste Weg für Homelab-Automatisierung.

## Dateibasierte Automatisierung (Legacy)

Solange GraphQL nicht reicht (ältere Versionen, Detailwerte), lesen Skripte direkt auf dem Server mit:

```bash
# Grundkonfiguration und Metadaten liegen auf dem Bootmedium
ls /boot/config            # XML-Dateien, super.dat, shares-Verzeichnis
cat /boot/config/ident.cfg # Geräte-ID, Benennung, Netz-Identifikation

# Diagnosepaket für Support/Troubleshooting
diagnostics
```

Hinweise:

- Dateiformate sind nicht als Schnittstelle versioniert — Patcher halten, Fehler tolerieren.
- Geschrieben wird in dieser Ebene **nicht**: Änderungen immer über WebUI oder API, sonst droht Statusdesync.

## Testen und Sandbox

1. **Settings → Management Access → Developer Options** → *GraphQL Sandbox* aktivieren (oder `unraid-api developer --sandbox true`).
2. `http://UNRAID_IP/graphql` im Browser öffnen — Playground mit autocompletierendem Schema.
3. Queries zuerst ohne API-Key testen (nutzt die WebUI-Session), dann auf `x-api-key` umstellen.
4. Ergebnisse mit `jq` validieren, bevor sie in Cron-Skripte wandern.

## Siehe auch

- [index.md](index.md)
- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menu.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
