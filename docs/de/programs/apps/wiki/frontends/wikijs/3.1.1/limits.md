# Wiki.js 3.1.1: Grenzen

Bekannte Grenzen des Produkts, aus dem Quellcode von 3.1.1 und der offiziellen Dokumentation. Mit „nicht verifiziert“ markierte Punkte wurden nicht bestätigt.

## Ratenlimits

| Geltungsbereich | Limit | Quelle |
|-------|--------|--------|
| Anmeldeversuche | festes Zeitfenster je Schlüssel (z. B. `auth:<ip>`), mit Sperre bei Überschreitung; Zahlen in Richtlinienobjekten gesetzt | `backend/models/rateLimits.ts` |
| Allgemeine API (`/_api`) | keines im Quellcode gefunden | Suche in `backend/api`, `backend/controllers`, `backend/helpers` nach Ratenlimit-Code: kein Treffer außer `rateLimits.ts` |
| Je API-Schlüssel oder Token | keines gefunden | ebenso |
| Antwort-Header `X-RateLimit-*` | im Quellcode nicht gefunden | ebenso |

Die alte Seite behauptete „100 requests per minute per token“ mit Headern `X-RateLimit-*`. Diese Behauptungen stehen nicht in 3.1.1 und sind in `../changelog.md` aufgeführt.

Die Zahlen des Anmeldelimiters (maximale Versuche, Zeitfenster, Sperrdauer) wurden nicht extrahiert. Bei Bedarf die Richtlinienwerte in `backend/models/rateLimits.ts` und `backend/models/authentication.ts` ansehen.

## Größe und Nutzlast

| Grenze | Wert | Quelle |
|-------|------|--------|
| Websocket-Nutzlast (Zusammenarbeit und Websocket-Routen) | 5 MiB (`maxPayload: 5242880`) | `backend/index.ts` (`fastifyWebsocket`) |
| Upload-Größe | eine Einstellung `maxUploadSize` in den Admin-Sicherheitseinstellungen; 3.1.1 hat geändert, wie dieses Admin-Feld gespeichert wird (Versionshinweis „drop maxUploadSize number prop“) | `backend/index.ts`, https://github.com/requarks/wiki/releases/tag/3.1.1 |
| Weitere Größenbegrenzungen des Anfrage-Bodys | nicht gelesen | — |

## Datenbank und Laufzeit

| Grenze | Wert | Quelle |
|-------|------|--------|
| Datenbank | nur PostgreSQL im Quellcode (pg-Treiber, Drizzle `node-postgres`) | `backend/core/db.ts`, `backend/package.json` |
| Node.js | >= 26 | `backend/package.json` (`engines`) |
| Datenbank-Pool der Worker | eine Verbindung je Worker-Thread; Transaktionen in Workern dürfen nicht auf andere Abfragen warten | `backend/CLAUDE.md` |
| Scheduler | Job-Warteschlange auf Postgres-Basis, Poolifier-Thread-Pool | `backend/CLAUDE.md` |
| Mehrere Instanzen | Startprüfungen laufen unter einem Advisory-Lock, damit gleichzeitig startende Instanzen übereinstimmen; Dateispeicher muss geteilt oder per git synchronisiert sein | `backend/CLAUDE.md`, Speicherregel |

Die Behauptung der alten Seite „Database: PostgreSQL, MySQL, SQLite“ ist für 3.1.1 falsch (im Quellcode nur PostgreSQL). Quelle: `backend/core/db.ts`.

## Speicher

| Grenze | Quelle |
|-------|--------|
| Die Datenbank ist immer ein Speicherziel (`db`) und kann nicht abgeschaltet werden | `.claude/rules/storage.md` |
| Die Ziele `disk` und `git` brauchen einen persistenten Datenträger oder ein geteiltes Repo für mehr als eine Instanz | `backend/modules/storage/git/definition.yml` (Hinweis zum lokalen Repo), Speicherregel |
| Git: Force-Push im Modus `push` überschreibt das Remote | `backend/modules/storage/git/definition.yml` (Hinweis zu `syncMode`) |
| SFTP: eine Verbindung je Ziel, seriell | `.claude/rules/storage.md` |
| Objektspeicher: Schlüssel sind Pfade; keine Ordner | `.claude/rules/storage.md` |

## Editoren

| Grenze | Quelle |
|-------|--------|
| Weiterleitungsseiten haben keinen Text und sind nie durchsuchbar | `backend/api/schemas/page.ts` |
| Das Umwandeln zwischen Editoren schreibt die Quelle neu und vergleicht Darstellungen, bevor gespeichert wird | `PageActionsCol.vue` (Kommentar zu `convertPage`) |

## Suche

| Grenze | Quelle |
|-------|--------|
| Die Kopfzeilen-Suche braucht mindestens 2 Zeichen | Locale `common.header.searchHint` („Type at least 2 characters“) |
| Filter und Sortierung sind die des Suchendpunkts (siehe `api.md`) | `backend/api/pages.ts` |
| Anzahl der Ergebnisse und Regeln für unscharfe Suche: nicht gelesen | — |

## Konten und Zugriff

| Grenze | Quelle |
|-------|--------|
| Persönliche Token können keine Admin-Routen erreichen | `.claude/rules/personal-access-tokens.md` |
| Persönliche Token nur auf `/_api` und `/_mcp` | `backend/index.ts` |
| Systemschlüssel handeln für ihre Gruppen und sind kein Nutzer, können daher keine Aktionen ausführen, die einen Nutzer brauchen | https://docs.js.wiki/dev/api |
| Token-Bereiche je Kategorie (keine Admin-Kategorie) | `frontend/src/helpers/personalTokens.js` |
| Zwei-Faktor und Passkeys: je Konto verfügbar | `backend/models/passkeys.ts`, Profil-Routen |

## Sicherheitskorrekturen in 3.1.x (Hinweise auf frühere Schwachstellen)

Diese stehen in den Versionshinweisen. Sie zeigen Klassen von Problemen, die das Produkt hatte; unser Frontend sollte gegen sie testen.

| Version | Problemklasse | Quelle |
|---------|-------------|--------|
| 3.1.0 | ungültige Linkziele in Navigationseinträgen | Versionshinweise (GHSA-35r7-33j8-ghwg) |
| 3.1.0 | clientseitiges HTML-Rendering ohne den serverseitigen Sanitizer bereinigt | Versionshinweise (GHSA-3c74-j8g3-p255) |
| 3.1.0 | URL-Attribute von Blöcken; CSP auf `/_files`; SVG-Prüfung bei Umbenennen und Übernehmen | Versionshinweise (GHSA-m4c7-x7x7-3ppw) |
| 3.1.0 | unveröffentlichte Seiten über Baum, Rückverweise und Tag-Zähler sichtbar | Versionshinweise (GHSA-jf48-pw92-vgrx) |
| 3.1.1 | Ordneraktionen prüften die Rechte nicht bei allen Unterelementen | Versionshinweise (GHSA-p5rv-hmh3-wrv8, GHSA-7mf7-wprw-7fjm) |

Quelle: https://github.com/requarks/wiki/releases/tag/3.1.0 und https://github.com/requarks/wiki/releases/tag/3.1.1

## Nicht verifiziert

- Maximale Seitengröße, maximale Anzahl an Tags, maximale Ordnertiefe.
- Verhalten der Warteschlange für ausstehende Asset-Uploads bei Netzwerkverlust.
- Stufe der Barrierefreiheits-Konformität. Weder im Quellcode noch in den gelesenen Dokumenten angegeben. Nicht verifiziert.
