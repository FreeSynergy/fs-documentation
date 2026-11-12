# Syncthing – API

!!! warning "Maschinell übersetzt, noch nicht geprüft / Machine-translated, not yet reviewed"
    Diese Seite wurde maschinell aus der englischen Fassung übersetzt und noch nicht von einem Menschen geprüft.
    This page was machine-translated from the English version and has not yet been reviewed by a person.

| Merkmal | Wert | Gesehen |
|---------|------|---------|
| API | REST, gleicher Port wie die Oberfläche | ✅ |
| Authentifizierung | API-Schlüssel in `X-API-Key` oder als Bearer-Token; `/rest/noauth` braucht keinen | ✅ |
| Gruppen | system, config, cluster (ausstehend), folder, database, events, statistics, misc, debug | ✅ |
| Ereignisse | `/rest/events`, `/rest/events/disk`; Parameter offen | ✅ |
| Seitenweise Abfrage | `page`, `perpage` (Standard 65536) bei einigen GET-Anfragen | ✅ |
| Übertragung zwischen Geräten | TLS 1.2/1.3, Prüfung des Zertifikat-Fingerabdrucks | ✅ |

Quelle: https://docs.syncthing.net/dev/rest.html (gelesen 2026-11-10).
