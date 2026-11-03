# LaunchBoard - API Dokumentation

## Übersicht

LaunchBoard ist ein kommerzielles Produkt mit REST-ähnlicher HTTP-Schnittstelle und OAuth2/OIDC. **Wichtig für die Faktentreue**: Der Hersteller veröffentlicht **keine frei zugängliche Endpunkt-Referenz**; die maßgebliche Dokumentation liegt im Kundenportal hinter der Anmeldung. Die folgenden Tabellen trennen deshalb klar zwischen **standardisierten Protokoll-Endpunkten** (durch OAuth2/OIDC definiert) und dem **Schema dieser Skin-Dokumentation**, das die typischen Ressourcen abbildet, aber vor jeder Integration im Kundenportal geprüft werden muss.

**API-Arten im Überblick**

| Art | Verwendung | Dokumentationsstand |
|-----|------------|---------------------|
| REST/JSON (Ressourcenpfade) | Boards, Widgets, Integrationen, Nutzer verwalten | nur im Kundenportal referenziert |
| OAuth2 / OIDC | Anmeldung, Single-Sign-On, Token für Automatisierung | Standardprotokoll, öffentlich definiert |
| Webhooks (aushend) | Ereignisse an externe Systeme melden | Umfang je Tarif, im Portal dokumentiert |
| GraphQL | ❌ Nicht vorhanden | — |

## Authentifizierung

- **Sitzungs-Cookie**: Nach Login über lokale Konten oder OIDC setzt die Instanz ein Sitzungs-Cookie. Die Web-Oberfläche nutzt ausschließlich diesen Weg.
- **OAuth2/OIDC**: Als Client konfiguriert die Instanz Issuer, Client-ID und Secret. Für Automatisierung wird der **Client-Credentials-Flow** des Identity-Providers verwendet; die Instanz akzeptiert deren Access-Token.
- **API-Token (langlebig)**: Im Verwaltungsbereich „Integrationen/API“ werden Tokens mit Namen und Gültigkeit erzeugt. Übergabe üblicherweise als `Authorization: Bearer <token>`.
- **Scopes und Rollen**: Tokens folgen den Rechten des zugeordneten Kontos. Administrator-/Editor-/Betrachter-Rolle bestimmen, welche Ressourcen schreibbar sind.
- **Kein anonymer Zugriff**: ohne Token oder Sitzung antwortet die Schnittstelle mit `401`, bei fehlenden Rechten mit `403`.
- **Transport**: HTTPS ist Pflicht (Cloud-Variante vorgegeben, Container-Variante über Reverse Proxy sicherstellen).

## Standardisierte OIDC-Endpunkte

Diese Pfade definiert das Protokoll; die **Basis-URL** setzt sich aus Konfiguration und Installation zusammen und ist der Instanzdokumentation zu entnehmen.

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/.well-known/openid-configuration` | Metadaten des OIDC-Anbieters (Token-, Authorize-, JWKS-URL) |
| `GET` | `<authorize-URL>` | Umleitung zur Anmeldung des Identity-Providers |
| `GET` | `<redirect-URI>` | Rückkehr zur Instanz mit Authorization-Code |
| `POST` | `<token-URL>` | Code gegen Token tauschen; Client-Credentials für Skripte |
| `GET` | `<userinfo-URL>` | Profilattribute des angemeldeten Nutzers |
| `GET` | `<jwks-URL>` | Signaturschlüssel zur Token-Prüfung |

## Ressourcen-Schema (nicht öffentlich referenziert – im Portal prüfen)

Das nachfolgende Muster entspricht der üblichen Form solcher Dashboard-Produkte und wird in dieser Dokumentation als **Arbeits-Schema** verwendet.

### Boards

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/boards` | zugängliche Boards auflisten |
| `POST` | `/api/v1/boards` | Board anlegen (Name, Vorlage, Sichtbarkeit) |
| `GET` | `/api/v1/boards/{id}` | Einzelboard mit Layout laden |
| `PATCH` | `/api/v1/boards/{id}` | Name, Sichtbarkeit, Einstellungen ändern |
| `DELETE` | `/api/v1/boards/{id}` | Board löschen |
| `PUT` | `/api/v1/boards/{id}/layout` | Layout (Desktop oder Mobil) speichern |

### Widgets

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/boards/{id}/widgets` | Kacheln eines Boards auflisten |
| `POST` | `/api/v1/boards/{id}/widgets` | Kachel anlegen (Typ, Integration, Layout) |
| `GET` | `/api/v1/widgets/{widgetId}` | Einzelkachel lesen |
| `PATCH` | `/api/v1/widgets/{widgetId}` | Einstellungen ändern |
| `DELETE` | `/api/v1/widgets/{widgetId}` | Kachel entfernen |
| `POST` | `/api/v1/widgets/{widgetId}/duplicate` | Kachel duplizieren |
| `GET` | `/api/v1/widget-types` | verfügbare Widget-Typen samt Feldschema |
| `POST` | `/api/v1/widget-data/preview` | Antwort einer Datenquelle vorab prüfen |

### Integrationen

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `GET` | `/api/v1/integrations` | angebundene Dienste auflisten |
| `POST` | `/api/v1/integrations` | Dienst anlegen (Typ, URL, Schlüssel) |
| `PATCH` | `/api/v1/integrations/{id}` | Zugang oder URL ändern |
| `DELETE` | `/api/v1/integrations/{id}` | Verbindung entfernen |
| `POST` | `/api/v1/integrations/{id}/test` | Verbindung testen, Fehlerbeschreibung erhalten |
| `POST` | `/api/v1/certificates` | eigenes Root-Zertifikat hinterlegen |

### Nutzer, Rollen und System

| Methode | Endpoint | Beschreibung |
|---------|----------|--------------|
| `POST` | `/api/v1/users` | Nutzer anlegen oder Einladung erzeugen |
| `PATCH` | `/api/v1/users/{id}` | Rolle, Status, Profil ändern |
| `DELETE` | `/api/v1/users/{id}` | Nutzer entfernen |
| `GET` | `/api/v1/groups` | Gruppen und Freigaben |
| `GET` | `/api/v1/health` | Status der Instanz |
| `POST` | `/api/v1/backup` | Datenbank-Export anstoßen |

## Beispiele

### Token über einen OIDC-Provider holen

```bash
curl -s -X POST "https://id.example.internal/realms/homelab/protocol/openid-connect/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=launchboard" \
  -d "client_secret=$OIDC_SECRET"
```

Antwort (gekürzt):

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "expires_in": 300,
  "token_type": "Bearer"
}
```

### Boards auflisten

```bash
curl -s "https://launchboard.example.internal/api/v1/boards" \
  -H "Authorization: Bearer $LAUNCHBOARD_TOKEN"
```

Antwort (gekürzt):

```json
{
  "data": [
    { "id": "brd_01H", "name": "Homelab", "visibility": "team", "updatedAt": "2026-10-30T18:22:04Z" }
  ]
}
```

### Widget anlegen

```bash
curl -s -X POST "https://launchboard.example.internal/api/v1/boards/brd_01H/widgets" \
  -H "Authorization: Bearer $LAUNCHBOARD_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "container-status",
    "integrationId": "int_14",
    "layout": { "x": 0, "y": 0, "w": 3, "h": 2 },
    "settings": { "showActions": true, "intervalSeconds": 30 }
  }'
```

Antwort:

```json
{ "data": { "id": "wdg_92", "type": "container-status", "boardId": "brd_01H" } }
```

## Rate Limits

- **Keine öffentlich dokumentierten Zahlen.** Die Kontingente hängen vom Tarif und davon ab, ob Cloud- oder Container-Variante genutzt wird.
- Beobachtbare Praxis solcher Dienste: begrenzte Anfragen pro Minute und Token, Antwort `429` mit Hinweis auf Wartezeit.
- Empfohlene Client-Strategie: Request-Serialisierung, exponentielles Backoff bei `429`/`5xx`, Caching unveränderlicher Ressourcen (Widget-Typen, Integrationen).
- Widget-Intervalle in der Oberfläche sind der eigentliche Hebel: kurze Intervalle erzeugen den größten Teil des Traffics.
- Bei der Container-Variante zusätzlich Begrenzung am Reverse Proxy setzen (`limit_req` bei nginx, `ratelimit`-Middleware bei Traefik).

## Webhooks

- **Ausgehende Webhooks sind vorgesehen**, der genaue Ereigniskatalog steht im Kundenportal. Typischer Umfang:

| Ereignis | Auslösung |
|----------|-----------|
| `board.created` / `board.updated` / `board.deleted` | Board-Änderungen |
| `widget.created` / `widget.updated` / `widget.deleted` | Kachel-Änderungen |
| `integration.failed` / `integration.recovered` | Verbindungsstatus einer Integration |
| `auth.login` / `auth.logout` | Anmeldeereignisse |

- **Sicherung**: Signaturen prüfen, idempotent verarbeiten, fehlschlagende Zustellungen mit Backoff erneut versuchen (Wiederholversuche laut Anbieter).
- **Alternative**: Intervallabfrage von `/api/v1/health` und Integrationsstatus, wenn keine Webhooks im Tarif enthalten sind.

## SDKs und Client-Bibliotheken

- **Kein öffentliches SDK.** Genutzt werden HTTP-Clients (`curl`, `fetch`, `requests`, `httpx`).
- **OpenAPI-Datei**: Ob und in welcher Fassung sie im Kundenportal angeboten wird, ist **nicht öffentlich dokumentiert**; wenn vorhanden, eignet sie sich für Codegenerierung.
- **OIDC-Seite**: Für den Anmeldefluss lassen sich Standard-OIDC-Bibliotheken jeder Sprache verwenden (Keycloak-, Authentik- und Entra-ID-Clients funktionieren unverändert).
- **Skript-Tipp**: Ein dediziertes Konto mit Reader-Rechten für Abfragen, ein separates Konto mit Editor-Rechten für Änderungen – übersichtlicher und protokollierbar.

## Hinweise für den Betrieb

- **Lizenzstatus beachten**: Bei auslaufender Subscription schränkt die Instanz Schreibzugriffe ein; Automatisierungen laufen dann möglicherweise nicht mehr.
- **Secrets stabil halten**: Sitzungs- und Verschlüsselungssecrets der Container-Variante sichern, sonst sind gespeicherte Dienstschlüssel nicht mehr lesbar.
- **Token mit Mindestrechten** ausstellen und regelmäßig rotieren.
- **Versionsbindung**: Ressourcenpfade können sich zwischen Hauptversionen ändern; Automatisierungen an die Version aus `/api/v1/version` koppeln und Änderungen prüfen.

## Siehe auch

- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menu.md)
- [structure.md](structure.md)
- [shortcuts.md](shortcuts.md)
- [../homarr/api.md](../homarr/api.md) - Vergleich: offen dokumentierte tRPC-Schnittstelle
