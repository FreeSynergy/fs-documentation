# Syncthing - API

| Item | Value | Seen |
|------|-------|------|
| API | REST, same port as the GUI | ✅ |
| Authentication | API key in `X-API-Key` or as Bearer token; `/rest/noauth` needs none | ✅ |
| Groups | system, config, cluster (pending), folder, database, events, statistics, misc, debug | ✅ |
| Events | `/rest/events`, `/rest/events/disk`; parameters Open | ✅ |
| Pagination | `page`, `perpage` (default 65536) on some GETs | ✅ |
| Transport between devices | TLS 1.2/1.3, certificate fingerprint check | ✅ |

Source: https://docs.syncthing.net/dev/rest.html (read 2026-11-10).
