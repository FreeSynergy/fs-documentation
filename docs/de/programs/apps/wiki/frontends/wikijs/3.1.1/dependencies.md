# Wiki.js 3.1.1: Abhängigkeiten

Welche UI-Komponenten ein Frontend „in diesem Stil“ braucht und welche Operationen unseres `texts.capnp` sie aufrufen. Gelesener Vertrag: `/srv/FreeSynergy/fs-interfaces/schema/texts.capnp` (ENTWURF 0.1, 15 Methoden auf `Texts`). Nur `texts.capnp` wurde gelesen; `common.capnp` wurde für `Cursor`, `Change`, `ChangeListener`, `Problem`, `Envelope` gelesen. Andere Verträge in `fs-interfaces/schema/` (Dateien, Verlauf, Personen, Gruppen, …) wurden nicht geprüft, daher kann eine Lücke unten dort abgedeckt sein. Mit „hier nicht geprüft“ markiert.

## A. Benötigte UI-Komponenten

| Nr. | Komponente | Was sie zeigt oder tut | Wiki.js-Referenz |
|---|-----------|----------------------|-------------------|
| 1 | App-Gerüst | Kopfzeile, Schublade, Inhalt, Seitenleiste | `layout.md` |
| 2 | Navigationsbaum | Menü aus der Standortnavigation, Durchsuchen-Menü | `NavSidebar.vue`, `NavBrowseMenu.vue` |
| 3 | Seitenansicht | gerenderte Seite mit Titel, Tags, letzter Bearbeitung, Inhaltsverzeichnis | `pages/Index.vue`, `common.page.*` |
| 4 | Editor-Host | ein Host, mehrere Editoren je nach Typ | `EditorMarkdown.vue`, `EditorVisual.vue`, `EditorAsciidoc.vue` |
| 5 | Dialog „Seite anlegen“ | Pfad, Editor, Locale | `PageActionsCol.vue`, `helpers/editors.js` |
| 6 | Dialog umbenennen / verschieben | Baum-Browser zur Wahl des neuen Pfads | `TreeBrowserDialog.vue` |
| 7 | Löschdialog und Papierkorb | weiches Löschen, Wiederherstellen | `PageDeleteDialog.vue` |
| 8 | Verlaufsliste und Versionsansicht | Versionen auflisten; eine lesen | `PageVersion.vue`, `.../history` |
| 9 | Quellansicht | Rohquelle des gespeicherten Texts | `viewPageSource` |
| 10 | Suche | Abfrage mit Filtern und Paging | `HeaderNav.vue`, `/_search` |
| 11 | Panel für Rückverweise und Links | was hierher verweist, worauf dies verweist | `pages.ts` (`backlinks`, `links`) |
| 12 | Tags | Tag-Liste, Tag-Durchsuchen | `/_tags` |
| 13 | Live-Aktualisierung | Ansicht aktualisieren, wenn ein anderer Autor speichert | `collab.js` (Yjs), keine Listenaktualisierung |
| 14 | Posteingang und Beobachten | Benachrichtigungen; beobachtete Seiten | `/_inbox/*` |
| 15 | Admin | Standorte, Nutzer, Gruppen, Speicher, Theme | `routes.js` (`/_admin/*`) |
| 16 | Import und Export | Markdown hinein und heraus | `backend/api/import.ts`, `pages.ts` (render) |

## B. Zuordnung: UI-Bedarf zu `texts.capnp`-Operationen

| `texts.capnp`-Methode | Zweck dort | Von der UI-Komponente genutzt |
|----------------------|---------------|----------------------|
| `supportReport` | was der Provider kann | 15 (Fähigkeitsprüfungen) |
| `create (path, markdown)` | neue Seite aus Markdown | 5 (nur für Markdown) |
| `edit (id, document)` | Seite speichern (Dokument als JSON) | 4 |
| `move (id, path)` | einen Text umbenennen oder verschieben; Links folgen | 6 |
| `delete (id)` | löschen | 7 |
| `get (id)` | eine Seite lesen | 3, 4, 9 |
| `getByPath (path)` | nach Pfad lesen | 3 |
| `list (prefix, cursor)` | Texte unter einem Pfad auflisten | 2 (Baum, teilweise) |
| `find (term, cursor)` | nach Begriff suchen | 10 |
| `links (id)` | ausgehende Links | 11 |
| `backlinks (path)` | eingehende Links | 11 |
| `importText (path, mediaType, text)` | Markdown oder anderes importieren | 16 |
| `exportText (id, mediaType)` | exportieren | 9, 16 |
| `subscribe (listener)` | Änderungsfeed (`Change`-Union) | 13 |
| `moveFolder (prefix, path)` | einen Ordner und seine Texte verschieben | 6 |
| `editIf (id, revision, document)` | nur speichern, wenn niemand anders zuerst gespeichert hat | 4 (Konfliktbehandlung) |

Hinweise zur Zuordnung:

- `editIf` ist der einzige Speicherweg, der vor einem parallelen Speichern schützt. Seine Konfliktantwort ist ein Text-Grund, der mit `conflict:` beginnt, kein typisiertes `Problem` (siehe Abschnitt D).
- `subscribe` liefert `Change`-Werte mit einem `Envelope` für angelegt und aktualisiert, und nur eine `Uuid` für gelöscht. Der Listener-Vertrag hat `ended` für einen abgebrochenen Feed; ein Verbraucher muss nach dem erneuten Abonnieren neu lesen (`common.capnp`).
- `TextEntry.revision` existiert für `editIf` und wird nie zurückgesetzt. Die UI kann sie anzeigen, aber es gibt keine Liste früherer Revisionen.

## C. Was `texts.capnp` für diese Art Frontend fehlt

| Lücke | Benötigt von | Wiki.js 3.1.1 hat | Vorgeschlagene Ergänzung (nur anhängen, ADR-0045-Regel) |
|-----|-----------|-------------------|------------------------------------------------|
| Ordnerliste, anlegen, löschen | 2, 6 | Ordner-Endpunkte unter `tree/folders` | `listFolders`, `createFolder`, `deleteFolder`; oder eine `Node`-Union in `list` |
| Frühere Versionen: auflisten, lesen, wiederherstellen | 8 | Endpunkte `history`, `versions` | `history (id, cursor)`, `revisionAt (id, revision)`, `restore (id, revision)` |
| Papierkorb: gelöschte auflisten, wiederherstellen | 7 | Endpunkte `pages/deleted`, `restore` | `listDeleted (prefix, cursor)`, `restore (id)` |
| Editor-Typ beim Anlegen und Speichern | 4, 5 | Feld `editor` in der Seiteneingabe | `create` mit einer Editor-ID; `edit` nimmt schon JSON, also muss der Typ im Dokument oder als Feld stehen |
| Locales: je Text und je Pfad | 3, 5, 10 | `locale` an der Seite; Locale-Beziehungen | Feld `locale` in `TextEntry`; `localeRelations (id)` |
| Suchfilter und Sortierung | 10 | `tags`, `editor`, `publishState`, `creatorId`, `orderBy` | `find` mit einer Filterstruktur und `orderBy` |
| Tags: auflisten, hinzufügen, zählen | 12 | Tag-Endpunkte und Zähler | `tags (prefix)`, `setTags (id, tags)` |
| Veröffentlichungsstatus | 3, 10 | Filter `publishState`, Warnung bei unveröffentlicht | Feld in `TextEntry` oder im Dokument, mit einer Methode `publish` |
| Titel und Beschreibung als Felder | 3, 10 | `title`, `description` in der Seiteneingabe | heute nur innerhalb von `document` (Format im Vertrag nicht definiert) |
| Gerendertes HTML oder Vorschau | 3, 9 | Endpunkt `render` | `render (id)`, das HTML liefert; oder festlegen, dass `exportText` `text/html` annimmt |
| Einen Text beobachten und nicht beobachten | 14 | Beobachten-Endpunkte | `watch (id)`, `unwatch (id)` |
| Kommentare | 3 (Seitenpanel) | Kommentar-Endpunkte | nicht in `texts`; ein eigener Vertrag |
| Bewertungen | 3 | Bewertungs-Endpunkte | nicht in `texts`; ein eigener Vertrag |
| Änderungsvorschläge und Prüfwarteschlange | 14 | Freigabe-Endpunkte | nicht in `texts`; ein eigener Vertrag |
| Seitenrechte und Zugriffsregeln | 2, 3, 6 | Endpunkt `userPermissions`, Gruppen und Seitenregeln | hängt von den Verträgen für Personen und Gruppen ab (hier nicht geprüft) |
| Seitensperre mit Passwort | 3 | Endpunkt `unlock` | `unlock (id, secret)` (nur, wenn wir die Funktion behalten) |
| Navigationsmenü | 2 | Navigations-Endpunkte | nicht in `texts`; ein eigener Vertrag |
| Assets einer Seite | 3, 16 | Asset-Endpunkte | `files.capnp` (hier nicht geprüft) |
| Gemeinsames Live-Bearbeiten | 4, 13 | Yjs-Websocket | `editIf` liefert nur Konflikte zur Speicherzeit. Echtzeitbearbeitung braucht einen eigenen Kanal. |
| Entwürfe (ungespeicherter Text) | 4 | lokaler Puffer | nicht im Vertrag; beim Client belassen |
| Typisierte Fehler bei `editIf` | 4 | RFC-9457-`Problem` in common | der Konflikt ist ein Textpräfix `conflict:`; auf ein typisiertes `Problem` mit Status 409 umstellen |

## D. Unstimmigkeiten in `texts.capnp` (nicht geändert, nur gemeldet)

1. `editIf` meldet Konflikte als Textgrund, der mit `conflict:` beginnt. `common.capnp` definiert `Problem` (Form RFC 9457) für Fehler. Beides kann nicht die Regel sein. Vorschlag: die Form `Problem`.
2. `subscribe` sagt nichts darüber, welche Texte gemeldet werden (alle oder ein Präfix). Die UI braucht einen Filter nach Präfix für den Baum und für eine Seitenansicht.
3. `delete (id)` hat keine Möglichkeit zu sagen „ist schon weg“. Wiederholungen können einen Fehler liefern. Nicht verifiziert: wie der Provider einen zweiten Löschversuch beantwortet.
4. `list` und `find` nehmen einen `Cursor`, aber der Vertrag sagt nicht, was ein leeres `next` für den Aufrufer bedeutet, außer „Anfang oder Ende“ (siehe `common.capnp`, wo das gesagt wird).

## E. Operationen von `texts.capnp`, die ein Frontend im Wiki.js-Stil nicht braucht

Keine wird von der UI in Abschnitt A benötigt. `importText` und `exportText` werden nur für die Import- und Exportfunktionen (16) gebraucht.

## F. Minimalsatz für eine erste Version

Um Seiten anzuzeigen, sie mit Konfliktschutz zu bearbeiten, zu verschieben, zu löschen, zu suchen und Links anzuzeigen, braucht das Frontend: `get`, `getByPath`, `list`, `find`, `create`, `editIf`, `move`, `delete`, `links`, `backlinks`, `subscribe`, `supportReport`. Alles aus Abschnitt C ist ein zweiter Schritt.
