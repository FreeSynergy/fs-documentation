# ActivityWatch latest — API

REST, JSON, base path `/api/0/` on the local server (playground at `/api/`). Timestamps RFC 3339 with time zone; durations in seconds.

| Method and path | Purpose |
|-----------------|---------|
| `GET /info` | Server info |
| `GET /buckets/`, `GET/POST/DELETE /buckets/<id>` | List, read, create, delete buckets (delete needs `force=1`) |
| `GET/POST /buckets/<id>/events` | Read (start, end, limit) or add events |
| `GET /buckets/<id>/events/count` | Count |
| `GET/DELETE /buckets/<id>/events/<event>` | One event |
| `POST /buckets/<id>/heartbeat?pulsetime=` | Add an event, merge with the previous identical one |
| `POST /query/` | Run a query over time periods |
| `GET /export`, `GET /buckets/<id>/export`, `POST /import` | Export and import |
| `GET/POST/DELETE /settings/<key>` | Settings |

Authentication: none by default; the Rust server offers an opt-in API key sent as a bearer token. Rate limits: Open. The two server implementations differ in error handling; do not rely on error bodies.
