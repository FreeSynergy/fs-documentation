# Wiki — Anforderungen

Was `FreeSynergy.Wiki` muss und kann, abgeleitet aus den [Frontends](frontends/index.md) (ADR 0006, 0013). Jede Fähigkeit nennt ihren Datenstandard (ADR 0014) und unseren Stand.

Stand: `implemented` · `planned` · `proposed`

## Pflicht (allen analysierten Programmen gemeinsam)

| Fähigkeit | Gesehen in | Daten / Standard | Stand |
|------------|---------|-----------------|--------|
| Versionshistorie lesen, eine Version wiederherstellen | Confluence, MediaWiki, Notion, Wiki.js, Tango | Texte-Vertrag | proposed |
| Papierkorb mit Wiederherstellung | Confluence, MediaWiki, Notion, Wiki.js | Texte-Vertrag | proposed |
| Berechtigungen und Freigabe | Confluence, Notion, Wiki.js, Tango | Schnittstelle Freigabe (offen) | proposed |
| Bereiche / Ordner / Namensräume, Reihenfolge von Geschwisterseiten | Confluence, MediaWiki, Wiki.js | Texte-Vertrag | proposed |
| Vorlagen, Weiterleitungen | Confluence, MediaWiki, Wiki.js | Texte-Vertrag | proposed |
| Suche mit Ausschnitten und Filtern, Präfixsuche | Confluence, MediaWiki, Wiki.js | Texte-Vertrag | proposed |
| Kommentare, Diskussionsseiten | Confluence, MediaWiki, Notion | Nachrichten, mit Verweis auf die Seite | proposed |
| Anhänge | Confluence, Notion, Tango | Dateien, mit Verweis | proposed |
| Labels, Tags, Kategorien | Confluence, MediaWiki, Wiki.js | gemeinsames Tag-Feld (offen) | proposed |
| Beobachten, Benachrichtigungen | Confluence, MediaWiki, Wiki.js | `subscribe` im Hub | proposed |

Bekannter Mangel: `editIf` meldet einen Konflikt als Textpräfix, nicht als typisiertes `Problem`.

## Optional (bemerkenswerte Ideen)

| Fähigkeit | Gesehen in | Daten / Standard | Stand |
|------------|---------|-----------------|--------|
| Blöcke und Datenbanken mit Ansichten | Notion | offen, größere Entscheidung | proposed |
| Gemeinsames Bearbeiten in Echtzeit | Wiki.js (Yjs) | offen, gehört zu P2P (ADR 0059) | proposed |
| Klicks in eine Schritt-für-Schritt-Anleitung aufzeichnen | Tango | offen | proposed |

## Nicht geplant (bewusst)

Noch nichts.
