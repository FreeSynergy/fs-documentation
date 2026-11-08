# 0027 – IDs: UUIDv7 (RFC 9562)

Status: akzeptiert (2026-11-05) · ersetzt in `data/standards.md` Entscheidung 3 „ULID“ · ADR 0026

## Entscheidung
- Interne IDs sind **UUIDv7** (RFC 9562, Mai 2024, ersetzt RFC 4122): zeitlich sortierbar,
  ein echter Standard statt der ULID-Konvention.
- Nach außen bleibt die ID eine absolute IRI `https://<instanz>/<domäne>/<uuid>` (AS2 Core §4.1).
- JSContact-`uid` darf ebenfalls UUIDv7 sein (RFC 9553 empfiehlt v4, v7 ist gültig).
