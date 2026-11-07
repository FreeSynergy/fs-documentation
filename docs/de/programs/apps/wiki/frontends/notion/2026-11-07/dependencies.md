# Notion — Abhängigkeiten für ein Frontend in diesem Stil

Was ein Frontend "im Stil von Notion" von unseren Komponenten braucht. Grundlage sind die Funktionen in [features.md](features.md) und die Operationen in `fs-interfaces/schema/texts.capnp` (DRAFT 0.1, 2026-11-06).

## Aktuelles texts.capnp (Zusammenfassung)

Schnittstelle `Texts` (Vertrag fs-wiki, DRAFT 0.1):

| Operation | Signatur (kurz) | Hinweise |
|-----------|-----------------|----------|
| `supportReport` | → Bericht | |
| `create` | Pfad, Markdown → Text | Pfad und Markdown hinein |
| `edit` | id, document → Text | ganzes Dokument |
| `move` | id, Pfad → Text | Links folgen |
| `delete` | id → () | Semantik (Papierkorb oder endgültiges Löschen) nicht angegeben |
| `get` | id → gefunden, Text | |
| `getByPath` | Pfad → gefunden, Text | |
| `list` | Präfix, Cursor → Seite | Auflistung nach Pfadpräfix, Cursor-Seitenweise |
| `find` | Begriff, Cursor → Seite | nur Begriff |
| `links` / `backlinks` | id / Pfad → Zeilen | Linkzeilen: source, target, at |
| `importText` | Pfad, mediaType, Text → Eintrag | |
| `exportText` | id, mediaType → Text | |
| `subscribe` | listener → Abonnement | Änderungsstrom von `ChangeListener` |
| `moveFolder` | Präfix, Pfad → verschoben | ganzer Teilbaum |
| `editIf` | id, revision, document → Text | Compare-and-set auf `revision` |

`TextEntry`: `envelope` (AS2 Article oder Note), `path`, `document` (JSON, maßgeblich), `revision` (UInt64). `Envelope` (common.capnp) hat `published`, `updated`, `attributedTo`, `to`, `cc`, `inReplyTo`, `name`, `context`, `sensitive`.

## Komponenten, die ein Frontend im Notion-Stil braucht

| UI-Komponente | Benötigt | Durch texts.capnp abgedeckt? |
|---------------|----------|------------------------------|
| Baum der Seitenleiste (Seiten, Abschnitte, Favoriten) | Baum der Pfade, Verschachtelung, Reihenfolge | teilweise: `list` nach Präfix, `moveFolder`. Keine Reihenfolge, kein Favorit, keine Abschnitte |
| Seitenliste und Suche | Auflisten, Suche mit Filtern und Sortierung | teilweise: `list`, `find` (nur Begriff, ohne Filter/Sortierung) |
| Block-Editor | typisierter Blockbaum, Block-IDs, Block einfügen/verschieben/aktualisieren | nein: das Dokument ist undurchsichtiges JSON; kein Blockmodell im Vertrag |
| Schrägstrich-Menü, Markdown-Eingabe | Registry der Blocktypen, Umwandlungen | nein (auf Frontend-Seite; braucht ein Blockschema) |
| Inline-Erwähnungen, Seitenlinks | Linkzeilen mit Positionen | teilweise: `links`, `backlinks` (`at` ist Text). Keine Erwähnungszeilen |
| Rich Text | Spans mit Auszeichnungen und Links | nein: kein Schema für Spans |
| Datenbank-Ansichten (Tabelle, Liste, Board, Kalender, Galerie, Diagramm) | Sammlungen, Schema, Zeilen, Ansichten mit Filter/Sortierung/Gruppierung | nein: kein Konzept für Datenbank oder Ansicht |
| Eigenschaften (Status, Auswahl, Datum, Relation, Rollup, Formel) | Eigenschaftstypen, Werte, Relationen | nein |
| Kommentare und Diskussionen | Kommentarobjekte, an einen Text oder Block gebunden | nein |
| Seiteneinstellungen (Schrift, Breite, Icon, Titelbild, Inhaltsverzeichnis) | Darstellungsfelder pro Text | nein: passt nur in das JSON von `document`, wenn es festgelegt wird |
| Papierkorb und Wiederherstellen | Löschstatus, Wiederherstellen, Papierkorb auflisten | nein: Semantik von `delete` unbekannt; keine Wiederherstellungsoperation |
| Versionsverlauf | Liste der Versionen mit Zeitstempeln und Autoren | nein: nur Zähler `revision`; kein Lesen des Verlaufs |
| Berechtigungen und Teilen | ACL pro Text, Rollen | nein; `Envelope.to/cc/audience` ist ein Feld für den Nachrichtenkreis, kein Berechtigungsmodell |
| Benachrichtigungen und Live-Aktualisierungen | Änderungsstrom | ja: `subscribe` mit `ChangeListener`; Feingranularität nicht angegeben |
| Import und Export | Markdown und andere Medientypen | ja: `importText`, `exportText` |
| Datei- und Medien-Uploads | Blob-Speicher | nicht in diesem Vertrag; `common.capnp` hat eine Schnittstelle `Blob` |
| Vorlagen | Vorlagentexte | nein |
| Tastatur, Layout, Theme | keine | außerhalb des Vertrags |

## Lücken in texts.capnp (für den Eigentümer von fs-wiki)

1. **Blockmodell.** Kein typisierter Blockbaum, keine Block-IDs, keine Reihenfolge der Kinder. `document` als undurchsichtiges JSON kann keine Blockoperationen tragen (nach einem Block einfügen, verschieben, einen Block aktualisieren) oder Live-Bearbeitung pro Block.
2. **Datenbankmodell.** Keine Sammlungen, Schemata, Zeilen, Eigenschaften oder Ansichten.
3. **Ansichten und Filter.** Keine Ansichtsobjekte. `find` nimmt nur einen Begriff.
4. **Kommentare.** Keine.
5. **Berechtigungen und Teilen.** Keine ACL, keine Rollen, keine Sichtbarkeit pro Benutzer.
6. **Papierkorb und Wiederherstellen.** `delete` sagt nicht, ob es umkehrbar ist. Kein `restore`, kein `listTrashed`.
7. **Verlauf.** Kein Auflisten von Versionen, kein Lesen einer Version, kein Vergleich.
8. **Autorschaft.** `TextEntry` hat kein `createdBy`, `lastEditedBy` (nur `Envelope.attributedTo` am Envelope; nicht als Autor jeder Version definiert).
9. **Suchoptionen.** Keine Sortierung, keine Filter, keine festgelegten Garantien für die Reihenfolge der Paginierung.
10. **Darstellung.** Icon, Titelbild, Schrift, Breite: keine Felder.
11. **Erwähnungen.** Nur Links; keine typisierten Erwähnungszeilen.

Diese Lücken sind Fakten über den Vertrag, keine Entscheidungen. Der Eigentümer von fs-wiki entscheidet, wie sie geschlossen werden (ADR-Verfahren).

## Operationszuordnung für ein Frontend im Notion-Stil

| Aktion im Frontend | Heutige Operation in texts.capnp | Lücke |
|--------------------|----------------------------------|-------|
| Seite öffnen | `getByPath` oder `get` | keine für das Lesen |
| Seite speichern | `editIf` (mit `revision`) | Speichern auf Blockebene braucht Blockoperationen |
| Neue Seite | `create` | keine für einfachen Text |
| Seite verschieben | `move`, `moveFolder` | keine im einfachen Fall |
| Seite löschen | `delete` | Umkehrbarkeit unbekannt |
| Suche | `find` | Filter und Sortierung |
| Panel Rückverweise | `backlinks` | keine |
| Live-Aktualisierung | `subscribe` | Granularität unbekannt |
| Export | `exportText` | keine |
| Datenbankansicht | keine | gesamtes Modell fehlt |
| Kommentare | keine | gesamtes Modell fehlt |
| Versionsverlauf | keine | gesamtes Modell fehlt |

## Hinweise

- `editIf` ist atomar nur innerhalb eines einzelnen Provider-Prozesses (Kommentar in texts.capnp). Mehrknoten-Aufbauten brauchen einen anderen Plan.
- Der Vertrag ist DRAFT 0.1 ohne Verbraucher bisher (Kopfzeile von texts.capnp).
