# Notion — API (Version 2026-03-11)

Aktuelle API-Version: `2026-03-11` [S1, S8]. Jede REST-Anfrage muss `Notion-Version` senden [S1].

## Basis und Header [S6]

- Basis-URL: `https://api.notion.com` (nur HTTPS).
- `Authorization: Bearer <token>`.
- `Notion-Version: 2026-03-11`.
- `Content-Type: application/json` für JSON-Inhalte. Datei-Uploads verwenden Multipart-Formulardaten [S6].

```bash
curl https://api.notion.com/v1/pages/<page_id> \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2026-03-11"
```

## Authentifizierung [S3]

| Typ | Wer | Wie er ausgestellt wird | Hinweise |
|-----|-----|-------------------------|----------|
| Token einer internen Integration | Ein einzelner Arbeitsbereich | Developer Portal, Reiter Configuration; nur der Eigentümer | Jede Seite muss vor dem Zugriff mit der Verbindung geteilt werden [S3] |
| Persönliches Zugriffstoken (PAT) | Ein Benutzer, der als er selbst handelt | Developer Portal | Gleicher Bearer-Header. Die Gültigkeit kann zwischen 7 Tagen und 1 Jahr gewählt werden (Changelog 2. Juli) [S8] |
| Öffentliche Integration (OAuth 2.0) | Jeder Arbeitsbereich, der sie autorisiert | Autorisierungsablauf unten | Zugriffstoken plus Refresh-Token |

### OAuth-2.0-Ablauf [S3]

1. Den Benutzer per Weiterleitung zu `https://api.notion.com/v1/oauth/authorize` schicken, mit `client_id`, `redirect_uri`, `response_type=code`, `owner=user`, optional `state`.
2. Der Benutzer wählt Seiten aus. Notion leitet zu `redirect_uri` weiter, mit `code`, oder mit `error` bei Abbruch.
3. Den Code einlösen: `POST https://api.notion.com/v1/oauth/token` mit HTTP-Basisauthentifizierung (`client_id:client_secret`), Body `grant_type=authorization_code`, `code` und wo nötig `redirect_uri`.
4. Die Antwort enthält `access_token`, `refresh_token`, `bot_id`, `workspace_id`, `owner` und weitere Felder.
5. Erneuern: gleicher Endpunkt mit `grant_type=refresh_token` und `refresh_token`. Jede Erneuerung liefert ein neues Zugriffstoken und ein neues Refresh-Token. Beide jedes Mal speichern [S3].

Die Gültigkeitsdauer der OAuth-Zugriffstoken steht nicht in den gelesenen Seiten: ungeprüft.

## Endpunkte

Pfade wie in der offiziellen Referenz angegeben. Nur Pfade mit Quelle sind aufgeführt. Andere sind als ungeprüft markiert.

### Seiten

| Methode und Pfad | Zweck | Quelle |
|------------------|-------|--------|
| `POST /v1/pages` | Seite erstellen. Übergeordnet: `page_id`, `database_id`, `data_source_id` oder `workspace: true`. Maximal 100 Blöcke in `children` | [S20] |
| `GET /v1/pages/{page_id}` | Seiteneigenschaften abrufen. Inhalt ist nicht enthalten; stattdessen die Kinder des Seitenblocks lesen | [S19] |
| `PATCH /v1/pages/{page_id}` | Seite aktualisieren; `in_trash: true` verschiebt in den Papierkorb, `in_trash: false` stellt wieder her | [S21] |
| `GET /v1/pages` (alle auflisten) | In der Referenz nicht gefunden. Ungeprüft; stattdessen Suche verwenden | (404 in der Referenz) |
| `DELETE /v1/pages/{id}` | Nicht als Löschen dokumentiert. Papierkorb über PATCH | [S21] |

### Blöcke

| Methode und Pfad | Zweck | Quelle |
|------------------|-------|--------|
| `PATCH /v1/blocks/{block_id}/children` | Kinder anhängen. Standard: Ende. `position`: `{"type":"start"}` oder `{"type":"after_block","after_block":{"id":...}}`. Maximal 100 pro Anfrage. Der alte Parameter `after` ist veraltet | [S18] |
| `GET /v1/blocks/{block_id}/children` | Kinder lesen (wird verwendet, um den Seiteninhalt zu lesen) | [S19] (dort referenziert; Pfad nicht abgerufen) |
| `PATCH /v1/blocks/{block_id}`, `DELETE /v1/blocks/{block_id}` | Block aktualisieren oder entfernen | ungeprüft (nicht abgerufen) |

### Datenbanken und Datenquellen

| Methode und Pfad | Zweck | Quelle |
|------------------|-------|--------|
| `POST /v1/databases` | Datenbank mit `initial_data_source` erstellen | [S7] |
| `GET /v1/databases/{database_id}` | Datenbank abrufen; liefert die Liste der untergeordneten `data_sources` mit `id` und `name` | [S7] |
| `PATCH /v1/databases/{database_id}` | Felder auf Datenbankebene: `parent`, `title`, `is_inline`, `icon`, `cover`, `in_trash` | [S7] |
| `GET /v1/data_sources/{data_source_id}` | Schema einer Datenquelle lesen | [S7] |
| `PATCH /v1/data_sources/{data_source_id}` | Schema (`properties`), `title`, `in_trash` ändern | [S7] |
| `POST /v1/data_sources/{data_source_id}/query` | Zeilen abfragen: `filter`, `sorts`, `start_cursor`, `page_size`; `filter_properties` ist ein Abfrageparameter. Hinweis: Die Zusammenfassung des Upgrade-Leitfadens sagt PATCH, die Referenz sagt POST | [S17], [S7] |

Datenbank-IDs und Datenquellen-IDs sind nicht austauschbar [S7]. Seit `2025-09-03` gilt der alte Aufruf `POST /v1/databases/{id}/query` nicht mehr [S7].

### Suche

| Methode und Pfad | Zweck | Quelle |
|------------------|-------|--------|
| `POST /v1/search` | Seiten und Datenquellen durchsuchen. Body: `query`, `filter`, `sort`, `start_cursor`, `page_size` | [S10] |

- `filter`: `{"property":"object","value":"page"|"data_source"}`, optional mit `in_trash`. `"database"` ist kein gültiger Wert [S10, S7].
- `sort`: `{"timestamp":"last_edited_time","direction":"ascending"|"descending"}` oder `{"property":"relevance"}` [S10].
- Unbekannte Body-Schlüssel werden abgelehnt [S10].
- Ergebnisse verwenden `next_cursor` und `has_more` [S10].

### Benutzer, Kommentare, Markdown

| Punkt | Status | Quelle |
|-------|--------|--------|
| Benutzer auflisten, Benutzer abrufen | vorhanden; benötigen eine Benutzerberechtigung außer "No user information" | [S16] |
| Bot-Benutzer des Tokens | vorhanden (nur-Kommentar-Verbindungen erlaubt) | [S16], [S8] (15. Okt.) |
| Kommentare (erstellen, aktualisieren, löschen) | vorhanden; Pfad nicht geprüft | [S16], [S8] (17. Apr.) |
| Markdown-Endpunkte für Inhalte | vorhanden (Changelog 26. Feb., 2. März, 29. Juni). Pfade nicht geprüft | [S8] |

Integrationsrechte (in den Verbindungseinstellungen festgelegt): Inhalte lesen, aktualisieren und einfügen; Kommentare lesen, einfügen; Stufe der Benutzerinformationen [S16].

## Paginierung [S6, S10, S8]

- Listen liefern `next_cursor` und `has_more`. `next_cursor` als `start_cursor` in der nächsten Anfrage übergeben [S6, S10].
- Cursor-Werte sind undurchsichtig (Changelog 22. Apr.) [S8].
- Paginierungsgrenze von 10.000 Ergebnissen, angegeben in `request_status` (Changelog 20. Apr.) [S8].
- Die maximale `page_size` steht nicht in den gelesenen Seiten: ungeprüft.

## Ratenbegrenzungen [S2, S8]

| Grenzwert | Wert |
|-----------|------|
| Pro Verbindung, die meisten Tarife | 180 Anfragen pro Minute (im Schnitt 3 pro Sekunde) |
| Pro Verbindung, Business und Enterprise | 600 Anfragen pro Minute (im Schnitt 10 pro Sekunde) |
| Datenquellen-Abfragen | etwa 3 Anfragen pro Sekunde pro Verbindung, getrennt gezählt |
| Arbeitsbereichsweit | Ein gemeinsamer Grenzwert gilt ebenfalls; Drosselung kann unter dem Verbindungslimit auftreten |

- Antwort bei Ratenbegrenzung: HTTP 429, Fehlercode `rate_limited`.
- Überlastung: HTTP 529 mit `service_overload`. Wie bei 429 wiederholen.
- `Retry-After`: ganze Sekunden. Außerdem im Body als `additional_data.retry_after` (Changelog 24. Sep.) [S8].
- Das Zeitfenster pro Verbindung beträgt 60 Sekunden (Changelog 9. Sep.) [S8].
- Eine 429 mit `public_api_request_blocked` nicht wiederholen [S2].

Payload-Grenzen: 100 Blockelemente pro Array; 1000 Blöcke und 500 KB pro Anfrage; 2000 Zeichen für Rich-Text-Inhalte und URLs; Validierungsfehler liefern HTTP 400 `validation_error` [S2].

## Versionierung [S1, S8]

- Eine neue `Notion-Version` wird nur für Breaking Changes veröffentlicht. Additive Änderungen gelten für alle Versionen [S1].
- `2022-06-28` und früher werden von SDK v5.0.0 und neuer nicht unterstützt [S1].
- Die nächste Version macht Notion-Markdown auf den Markdown-Endpunkten zum Standard (Changelog 30. Okt.). Name und Datum nicht angegeben [S8].

## SDK

- JavaScript: `@notionhq/client`; v5 ergänzt Methoden `notion.dataSources.*` [S7]. Die Hilfsfunktion für Webhook-Signaturen ist in v5.23.0 enthalten (Changelog 8. Juli) [S8].
- Python, Go und andere Clients: auf offiziellen Seiten nicht geprüft.

## Aus der früheren Seite entfernt

- `Notion-Version: 2022-06-28` (veraltet). Siehe [changelog.md](../changelog.md).
- `GET /v1/pages` (Liste), `DELETE /v1/pages/:id`, `POST /v1/databases/:id/query`, `POST /v1/webhooks`, Ratenbegrenzung "3 pro Sekunde / 1 pro Sekunde für Abfragen", `@notion/client`, `notion-client` (Python), Liste der Community-SDKs.
