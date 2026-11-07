# Notion — Ereignisse (Webhooks, 2026-11-07)

Quelle: [S4] Einrichtung der Webhooks, [S5] Ereignisse und Zustellung.

## Einrichtung

- Webhooks werden in den Verbindungseinstellungen der Integration erstellt, im Reiter **Webhooks**, mit **+ Create a subscription** [S4]. Auf den gelesenen Seiten gibt es keinen Endpunkt `POST /v1/webhooks`. Die frühere Seite war falsch [changelog.md].
- Die Webhook-URL muss HTTPS verwenden und öffentlich erreichbar sein. `localhost` funktioniert nicht [S4].
- Nach der Erstellung sendet Notion einen einmaligen JSON-Body mit `verification_token` per POST an die URL [S4].
- Das Abonnement wird im Reiter Webhooks aktiviert: Verify, Token einfügen, Verify subscription. Token erneut senden ist verfügbar [S4].
- Die URL kann nur vor der Verifizierung geändert werden. Danach das Abonnement löschen und neu anlegen [S4].
- Pausierte, nicht verifizierte oder gelöschte Abonnements erhalten nichts [S4].

## Signatur [S4]

- Header `X-Notion-Signature` mit dem Wert `sha256=<hex>`.
- Der Wert ist HMAC-SHA256 des rohen Bodys, mit `verification_token` als Schlüssel.
- Vergleich in konstanter Zeit.
- JavaScript-SDK v5.23.0 hat `verifyWebhookSignature()` (Changelog 8. Juli) [S8].

## Ereignistypen [S5]

| Entität | Typen |
|---------|-------|
| page | `page.content_updated`, `page.created`, `page.deleted`, `page.locked`, `page.moved`, `page.properties_updated`, `page.undeleted`, `page.unlocked` |
| database | `database.created`, `database.deleted`, `database.moved`, `database.undeleted`; `database.content_updated` und `database.schema_updated` sind für 2025-09-03 veraltet |
| data_source | `data_source.content_updated`, `data_source.created`, `data_source.deleted`, `data_source.moved`, `data_source.schema_updated`, `data_source.undeleted` |
| comment | `comment.created`, `comment.deleted`, `comment.updated` |

Hinweis: [S4] nennt `page.content_updated` als zusammengefasst und `comment.created` als Ereignis, das die Berechtigung zum Lesen von Kommentaren benötigt [S4, S16]. Auf den gelesenen Seiten gibt es kein Ereignis `file_upload` oder `view`.

## Nutzlast [S5]

| Feld | Bedeutung |
|------|-----------|
| `id` | UUID des Ereignisses |
| `timestamp` | Zeitpunkt des Ereignisses nach ISO 8601 |
| `workspace_id` | UUID des Arbeitsbereichs |
| `subscription_id` | ID des Abonnements |
| `integration_id` | ID der Verbindung |
| `type` | Ereignistyp |
| `authors` | Array aus `{id, type}`; Typ `person`, `bot` oder `agent` |
| `accessible_by` | Benutzer und Bots mit Zugriff (nur öffentliche Verbindungen) |
| `attempt_number` | 1–8 |
| `entity` | `{id, type}`; Typ `page`, `block`, `database`, `data_source`, weitere in Beispielen |
| `data` | ereignisspezifische Details |

Nutzlasten enthalten Metadaten, nicht den vollständigen Inhalt. Der Verbraucher ruft den aktuellen Stand über die API ab [S5].

## Zustellung [S5]

- Ziel: Zustellung höchstens einmal (at-most-once). Ereignisse sollten innerhalb von 5 Minuten ankommen.
- Fehlgeschlagene Zustellungen werden bis zu 8-mal mit exponentiellem Backoff wiederholt; der letzte Versuch etwa 24 Stunden nach dem Ereignis.
- Ereignisse können außer der Reihenfolge ankommen. `timestamp` verwenden.
- Manche Ereignisse werden zusammengefasst und gebündelt (zum Beispiel `page.content_updated`) und kommen daher später an.
- Nutzlasten spiegeln womöglich nicht den aktuellen Stand wider. Frische Daten abrufen.

## Verwendung für unser Frontend

- Webhooks als Hinweise zum erneuten Abrufen behandeln, nicht als Änderungsstrom mit Inhalt.
- Die Signaturprüfung beibehalten.
- Bei der Zustellung höchstens einmal mit Duplikaten oder Lücken rechnen: durch Abfragen oder Suche abgleichen.
