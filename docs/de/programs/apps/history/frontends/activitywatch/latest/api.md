# ActivityWatch latest — API

REST, JSON, Basispfad `/api/0/` auf dem lokalen Server (Playground unter `/api/`). Zeitstempel nach RFC 3339 mit Zeitzone; Dauern in Sekunden.

| Methode und Pfad | Zweck |
|------------------|-------|
| `GET /info` | Serverinformationen |
| `GET /buckets/`, `GET/POST/DELETE /buckets/<id>` | Buckets auflisten, lesen, anlegen, löschen (Löschen braucht `force=1`) |
| `GET/POST /buckets/<id>/events` | Lesen (start, end, limit) oder Ereignisse hinzufügen |
| `GET /buckets/<id>/events/count` | Anzahl |
| `GET/DELETE /buckets/<id>/events/<event>` | Ein Ereignis |
| `POST /buckets/<id>/heartbeat?pulsetime=` | Ereignis hinzufügen, mit dem vorherigen gleichen verschmelzen |
| `POST /query/` | Abfrage über Zeiträume ausführen |
| `GET /export`, `GET /buckets/<id>/export`, `POST /import` | Export und Import |
| `GET/POST/DELETE /settings/<key>` | Einstellungen |

Authentifizierung: standardmäßig keine; der Rust-Server bietet einen optionalen API-Schlüssel, der als Bearer-Token gesendet wird. Rate Limits: offen. Die beiden Server-Implementierungen unterscheiden sich in der Fehlerbehandlung; auf Fehlerinhalte nicht verlassen.
