# Confluence (Cloud, latest) · Abhängigkeiten

Was ein Frontend "im Confluence-Stil" auf unserer Wiki-Engine von der Engine benötigt. Vertrag: `fs-interfaces/schema/texts.capnp`, DRAFT 0.1 (2026-11-06), Schnittstelle `Texts`, plus `common.capnp` für `Envelope`, `Change`, `ChangeListener`, `Cursor`, `Problem`.

## 1. Operationen von `texts.capnp`, die Confluence-Funktionen abbilden

| Operation in texts.capnp | Confluence-Funktion, die sie bedient |
|--------------------------|--------------------------------------|
| `create(path, markdown)` @1 | Seite erstellen (kein Vorlagenparameter) |
| `edit(id, document)` @2 | Im Editor speichern |
| `editIf(id, revision, document)` @15 | Speichern mit Konflikterkennung (Compare-and-set) |
| `move(id, path)` @3 | Seite verschieben (Links folgen) |
| `moveFolder(prefix, path)` @14 | Seite mit ihrem Teilbaum verschieben |
| `delete(id)` @4 | Löschen (endgültig; kein Papierkorb) |
| `get(id)` @5, `getByPath(path)` @6 | Seite öffnen, Breadcrumbs aus dem Pfad |
| `list(prefix, cursor)` @7 | Baum in der Seitenleiste und Unterseitenlisten (prefix = Pfad) |
| `find(term, cursor)` @8 | Suche (kein Ausschnitt, kein Filter) |
| `links(id)` @9, `backlinks(path)` @10 | Links im Detailbereich, "verknüpfte Seiten" |
| `importText(path, mediaType, text)` @11 | Markdown oder anderen Text importieren |
| `exportText(id, mediaType)` @12 | Export (nur Textformate; siehe Lücken) |
| `subscribe(listener)` @13 | Live-Aktualisierungen (`Change` created/updated/deleted) |
| `supportReport()` @0 | Funktionsprüfung (nicht unterstützt = `Problem` mit Status 501) |

## 2. UI-Komponenten und was sie benötigen

| UI-Komponente | Benötigt | Durch den Vertrag abgedeckt | Status |
|---------------|----------|-----------------------------|--------|
| Suche in der oberen Leiste | Suche mit Ausschnitten, Filter nach Bereich oder Typ | `find` (TextPage) | Teilweise: keine Ausschnitte, keine Filter |
| Erstellen in der oberen Leiste | Erstellen mit Vorlagenauswahl | `create` | Teilweise: keine Vorlage |
| Benachrichtigungen und Erwähnungen in der oberen Leiste | Benachrichtigungsfeed, Erwähnungen | keine | Lücke |
| Baum der Seitenleiste | Untergeordnete Elemente in eigener Reihenfolge | `list(prefix)` | Teilweise: kein Feld für die Geschwisterreihenfolge |
| Bereichsauswahl und Bereichsübersicht | Bereich als Container mit Name, Schlüssel, Berechtigungen | keine (nur Pfad-Präfix) | Lücke |
| Seitenansicht | Inhalt aus dem Dokument-JSON | `TextEntry.document` | Abgedeckt, aber kein Schema für das JSON referenziert |
| Breadcrumbs | Pfad der Vorfahren | aus `path` abgeleitet | Abgedeckt |
| Kopfzeile "Zuletzt aktualisiert" und Editor | Zeitpunkt und letzter Bearbeiter der Aktualisierung | `Envelope.updated`, `Envelope.attributedTo` | Teilweise: `attributedTo` kann der Ersteller sein, nicht der letzte Bearbeiter |
| Titelbereich: Eigentümer, Status, Klassifizierung, Aufrufe, Lesezeit | Eigentümer, Status, Klassifizierung, Anzahl Aufrufe | keine | Lücke |
| Detailbereich: Labels | Labels | keine | Lücke |
| Detailbereich: Anhänge und verknüpfte Dateien | Anhangsliste, Blobs | `Blob` in common.capnp vorhanden, aber nicht aus texts referenziert | Lücke |
| Detailbereich: Mitwirkende | Bearbeitungsverlauf pro Benutzer | keine | Lücke |
| Detailbereich: Links | Links und Rückverweise | `links`, `backlinks` | Abgedeckt |
| Versionsverlauf und Vergleich | Versionen auflisten, alte Versionen lesen, wiederherstellen | nur Zähler `revision` | Lücke |
| Kommentare | Kommentarstränge | keine | Lücke |
| Beobachten, Favorit, Teilen | Zustand pro Benutzer | keine | Lücke |
| Berechtigungen und Einschränkungen | Lese- und Schreibregeln pro Text | keine | Lücke |
| Papierkorb und Wiederherstellen | Weiches Löschen, Wiederherstellen | `delete` ist endgültig | Lücke |
| Vorlagen und Blueprints | Vorlagenspeicher | keine | Lücke |
| Export nach PDF oder Word | Binäre Ausgabe | `exportText` liefert `Text` | Lücke (binär) |
| Präsentationsmodus, Layouts auf Seitenebene | Nur im Frontend | nicht nötig | Kein Engine-Bedarf |
| Tastenkürzel und Themes | Nur im Frontend | nicht nötig | Kein Engine-Bedarf |
| Live-Aktualisierungen | Änderungsfeed | `subscribe` / `ChangeListener` | Abgedeckt; `deleted` enthält nur die `Uuid` |
| Identität des Aufrufers für Berechtigungen | Wer fragt an | in keinem Aufruf enthalten | Lücke |
| Reihenfolge der Geschwister beim Ziehen und Ablegen | Positionswert | keine | Lücke |

## 3. Was `texts.capnp` fehlt (Zusammenfassung)

1. Bereiche oder andere Container oberhalb des Pfadbaums.
2. Liste der Versionen, Lesen früherer Versionen und Wiederherstellen.
3. Papierkorb und Wiederherstellen.
4. Labels oder Tags.
5. Kommentare.
6. Berechtigungen, Einschränkungen, Zustand von Beobachten und Favorit.
7. Vorlagenspeicher und Vorlagenparameter in `create`.
8. Anhänge und binärer Export (PDF oder Word).
9. Geschwisterreihenfolge (Position) für die Seitenleiste.
10. Ausschnitte in Suchergebnissen und Filter.
11. Dokumentschema: `document` ist "das Dokument als JSON" ohne Schema-ID oder Version.
12. Identität des Aufrufers und Akteur bei Schreibvorgängen.
13. Status, Klassifizierung sowie Aufruf- oder Lesestatistiken.
14. Blogbeiträge oder andere Inhaltsarten (es gibt nur Textelemente; der Unterschied ist im Vertrag nicht abgebildet).
15. Benachrichtigungen und Erwähnungen.

## 4. Confluence-Konzepte, die einem bestehenden Vertragsfeld entsprechen

| Confluence-Konzept | Zuordnung |
|--------------------|-----------|
| Seitenbaum | `path` mit `/` als Trennzeichen (`list`-Präfix) |
| Seiten-ID | `TextEntry.envelope.id` (Uuid) |
| Revisionszähler | `TextEntry.revision` (für editIf) |
| Letzte Aktualisierung | `Envelope.updated` |
| Darstellung des Seiteninhalts | `document` (JSON), nicht das Speicherformat von Confluence |

## 5. Hinweis zum Speicherformat von Confluence

Die eigenen Inhaltsformate von Confluence (`storage`, `atlas_doc_format`, `wiki`) erscheinen in der v2-API [S4]. Unser Vertrag speichert das Dokument als JSON und tauscht Markdown über Import und Export aus. Wir müssen kein Confluence-Format implementieren; die frühere Behauptung, Confluence verwende für seinen Haupteditor Wiki-Markup, ist für die Cloud ungeprüft.

Quellen: [index.md](../index.md) S-Nummern (S4 für Inhaltsformate).
