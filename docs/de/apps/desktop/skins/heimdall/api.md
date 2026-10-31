# Heimdall - API Dokumentation

## Übersicht

Heimdall hat **keine offiziell dokumentierte API**. Das Projekt richtet sich an Menschen, die ihr Dashboard in der Oberfläche pflegen, und verzichtet bewusst auf Automatisierungsschnittstellen. Existierende HTTP-Routen sind die internen Laravel-Routen des Frontends; sie sind nicht versioniert und können sich ohne Ankündigung ändern.

**Schnittstellen im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| Laravel-Routen (Web/JSON) | Apps, Panels, Layout, Konten verwalten | Intern, undokumentiert |
| Externe Dienst-APIs | Von Enhanced Apps aufgerufen (Pi-hole, Sonarr, Emby, Portainer …) | API des jeweiligen Dienstes |
| Serverstatistik | Lokal auf dem Heimdall-Rechner ausgelesen | Kein Netzwerk-Endpunkt |
| Webhooks | ❌ Nicht vorhanden | — |
| API-Schlüssel für Heimdall selbst | ❌ Nicht vorhanden | — |

## Authentifizierung

- **Sitzung (Session-Cookie)**: Nach der Anmeldung setzt Laravel ein Sitzungs-Cookie (`LaravelApplicationCookie` o. ä.). Alle internen Routen setzen eine gültige Sitzung voraus.
- **CSRF-Schutz**: Schreibende Anfragen benötigen das im HTML hinterlegte CSRF-Token (Meta-Tag oder Formularfeld) plus Header `X-CSRF-TOKEN`. Ohne dieses Token antwortet Heimdall mit HTTP 419.
- **Rollen**: Verwaltungsrouten sind Administratoren vorbehalten (rollenabhängig, versionsabhängig).
- **Deaktivierte Anmeldung**: Ist die Anmeldung abgeschaltet, sind die Routen für jeden erreichbar, der die Seite erreicht — Schutz dann ausschließlich über Proxy oder Netzwerk.
- **Verschlüsselte Dienstschlüssel**: API-Keys der Enhanced Apps liegen verschlüsselt in der Datenbank und werden mit `APP_KEY` geschützt.

## Interne Routen (nicht offiziell dokumentiert)

Die folgende Tabelle zeigt typische Routen des Frontends. **Vorbedingungen**: gültige Sitzung, CSRF-Token, korrekte `APP_URL`. Die Namen sind eine Hilfe zum Verständnis des Frontends, keine zugesicherte Schnittstelle.

### Apps

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/` | Startseite, rendert Panels und Apps |
| `GET` | `/apps` | Apps des Kontos auflisten (Ansicht/JSON je nach Version) |
| `POST` | `/apps` | App anlegen (Titel, URL, Icon, Farbe) |
| `GET` | `/apps/{id}` | Einzelne App laden |
| `PUT` | `/apps/{id}` | App ändern |
| `DELETE` | `/apps/{id}` | App löschen |
| `POST` | `/apps/{id}/icon` | Icon-Datei hochladen |

### Layout und Panels

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/layout` | Aktuell gespeichertes Layout des Kontos |
| `POST` | `/layout` | Layout speichern (Reihenfolge und Panel-Zuordnung) |
| `POST` | `/layout/reset` | Layout auf den Standard zurücksetzen |

### Konto und Nutzer

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/login` | Anmeldeformular |
| `POST` | `/login` | Anmelden (E-Mail, Passwort) |
| `POST` | `/logout` | Abmelden |
| `GET` | `/settings` | Einstellungsübersicht |
| `POST` | `/settings/account` | Eigene Zugangsdaten ändern |
| `GET` | `/settings/users` | Nutzerliste (neuere Versionen, Admin) |
| `POST` | `/settings/users` | Nutzer anlegen (Admin) |
| `DELETE` | `/settings/users/{id}` | Nutzer löschen (Admin) |

## Beispiel: interne Route mit Sitzung und CSRF

```bash
# 1. Anmeldeseite laden, CSRF-Token und Cookie merken
curl -s -c cookies.txt https://heimdall.example/login \
  | grep -o 'name="_token" value="[^"]*"'

# 2. Anmelden
curl -s -b cookies.txt -c cookies.txt -X POST https://heimdall.example/login \
  -d "email=admin@example.com" \
  -d "password=geheim" \
  -d "_token=<token>"

# 3. App anlegen (CSRF-Token aus einer geladenen Seite)
curl -s -b cookies.txt -X POST https://heimdall.example/apps \
  -H "X-CSRF-TOKEN: <token>" \
  -H "Content-Type: application/json" \
  -d '{"title":"Grafana","url":"https://grafana.local","colour":"#4a90d9"}'
```

Mögliche Antwort (nicht garantiert, da undokumentiert):

```json
{
  "success": true,
  "app": {
    "id": 12,
    "title": "Grafana",
    "url": "https://grafana.local",
    "colour": "#4a90d9"
  }
}
```

## Beispiel: API-Key einer Enhanced App nutzen

Enhanced Apps rufen die **API des angebundenen Dienstes** auf, nicht eine Heimdall-API. Der hinterlegte Schlüssel wird serverseitig verwendet. Beispiel Pi-hole:

```bash
# Prüfen, ob die hinterlegten Daten funktionieren (Pi-hole v6-API)
curl -s "http://pihole.local/api.php" \
  -d "token=<api-key>&num=10"
```

Erwartete Werte (vereinfacht) und ihre Verwendung in der Kachel:

```json
{
  "status": "enabled",
  "ads_blocked_today": 1284,
  "dns_queries_today": 21450
}
```

**Wichtig**: Scheitert die Anfrage, zeigt die Kachel einen Fehlerzustand; Heimdall selbst protokolliert keine Webhooks oder Ereignisse.

## Konfiguration als „Schnittstelle"

Die belastbarste Automatisierung läuft über Dateien und Umgebungsvariablen, nicht über HTTP.

### `.env` (Auswahl)

| Variable | Beschreibung |
|----------|--------------|
| `APP_KEY` | Schlüssel zum Verschlüsseln der Dienstschlüssel; **darf sich nicht ändern**, sonst sind alle Keys unbrauchbar |
| `APP_URL` | Öffentliche Adresse, wichtig für Icons und Weiterleitungen |
| `APP_DEBUG` | Fehlerausgabe; im Betrieb auf `false` belassen |
| `DB_CONNECTION` | `sqlite` (Standard), `mysql`, `pgsql` |
| `DB_DATABASE` | Pfad zur SQLite-Datei oder Name der externen Datenbank |
| `TZ` | Zeitzone, beeinflusst Datumsangaben in Kalendern und Statistiken |
| Auth-Schalter | Anmeldung an/aus (Variantname versionsabhängig, z. B. `AUTH_ENABLED=false`) |

### Persistente Daten

| Pfad | Inhalt |
|------|--------|
| SQLite-Datei im Datenverzeichnis | Apps, Panels, Layouts, Konten, verschlüsselte Schlüssel |
| `app/public/uploads` | Hochgeladene Icons |
| Eigenes CSS/Theme-Dateien | Visuelle Anpassungen |

Ein Backup besteht aus Datenbankdatei plus Uploads. Nach einem Austausch der Datei müssen Container neu gestartet und Migrationen ausgeführt werden.

## Rate Limits

- Heimdall bringt **keine eingebaute Ratenbegrenzung** mit.
- Die Belastung entsteht vor allem durch serverseitige Abfragen der Enhanced Apps beim Seitenaufruf.
- Schutz über den Reverse Proxy empfohlen (nginx `limit_req`, Traefik-Middleware, Fail2ban für Anmeldeversuche).
- Empfehlung: Anzahl der Enhanced Apps klein halten und langsame Dienste nicht im Dashboard einbinden.

## Webhooks und internes Eventing

- **Keine Webhooks**, keine Ereignisausgang, keine Benachrichtigungen.
- **Internes Eventing**: Das Frontend aktualisiert Statistikwerte und Kacheln durch erneutes Nachfragen beim Seitenaufruf; Layoutänderungen werden sofort in der Datenbank gespeichert.
- **Workaround für Automatisierung**: Externe Skripte schreiben Änderungen indirekt über die Datenbank (riskant, nicht empfohlen) oder ersetzen die gesamte Instanz aus einem gesicherten Volume.

## SDKs und Client-Bibliotheken

- **Kein SDK** für Heimdall.
- Wer Heimdall erweitern will, schreibt ein **Enhanced-App-Paket** (Laravel-Klasse, Service-Provider, Blade-Template) und nutzt die SDKs des jeweiligen Dienstes.
- Für Automatisierung gilt: die APIs der angebundenen Dienste direkt ansprechen, statt Heimdall einzubeziehen.

## Siehe auch

- [menu.md](menu.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
