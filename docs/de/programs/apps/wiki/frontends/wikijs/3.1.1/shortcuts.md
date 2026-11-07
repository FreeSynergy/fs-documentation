# Wiki.js 3.1.1: Tastenkürzel

„Mod“ bedeutet Ctrl unter Windows und Linux, Cmd unter macOS. Nur Belegungen, die im Quellcode von 3.1.1 gefunden wurden, sind aufgelistet. Die Quellen sind je Tabelle genannt. Quellbaum: https://github.com/requarks/wiki/tree/3.1.1/frontend/src

Es wurden keine app-weiten globalen Tastenkürzel gefunden. Die Liste der alten Seite (Befehlspalette, Dateisuche, Live-Vorschau, neue Seite, Dateibaum und ähnliches) steht nicht im Quellcode von 3.1.1 und wurde entfernt. Siehe `../changelog.md`.

## Visual-Editor

Quelle: `frontend/src/editor/visual/commands.js` (`buildKeymap`). Der Kommentar in dieser Datei sagt, die Belegung sei „deliberately close to what the Markdown editor binds“.

| Tastenkürzel | Aktion |
|----------|--------|
| Mod+Z | Rückgängig (Yjs-Undo bei Zusammenarbeit) |
| Mod+Shift+Z | Wiederholen |
| Mod+Y | Wiederholen |
| Mod+B | Stark (fett) |
| Mod+I | Betonung (kursiv) |
| Mod+U | Unterstrichen |
| Mod+Shift+X | Durchgestrichen |
| Mod+Shift+H | Markierung (Highlight) |
| Mod+E | Code im Text |
| Mod+Shift+8 | Aufzählungsliste |
| Mod+Shift+9 | Nummerierte Liste |
| Mod+Shift+. | Blockzitat |
| Mod+Shift+Enter | Aufgabe als erledigt umschalten |
| Mod+Shift+1 … 6 | Überschrift Ebene 1 bis 6 |
| Enter | Listenelement oder Definitionselement teilen |
| Tab | nächste Tabellenzelle, oder Listenelement einrücken |
| Shift+Tab | vorherige Tabellenzelle, oder Listenelement ausrücken |
| Shift+Enter | harter Zeilenumbruch (verlässt einen Codeblock, wenn man in einem ist) |
| Mod+Enter | Codeblock oder den letzten Block verlassen |
| Backspace, Delete | eigene Behandlung für Tabellen und Listenanfänge |

### Slash-Menü (im Visual-Editor)

Quelle: `frontend/src/editor/visual/slash.js`.

| Taste | Aktion |
|-----|--------|
| ArrowDown, ArrowUp | Markierung bewegen |
| Enter oder Tab | markierten Eintrag einfügen |
| Escape | Menü schließen |

Das Menü öffnet sich, wenn ein `/` getippt wird (`handleTextInput`), nicht wenn der Cursor in eine Zeile springt, die mit `/` beginnt, und nicht beim Einfügen.

## Markdown-Editor (Monaco)

Quelle: `frontend/src/components/EditorMarkdown.vue` (Aufrufe von `editor.addAction`).

| Tastenkürzel | Aktion |
|----------|--------|
| Mod+B | fett umschalten (`**`) |
| Mod+I | kursiv umschalten (`*`) |
| Mod+Alt+Right | Überschriftenebene erhöhen |
| Mod+Alt+Left | Überschriftenebene verringern |
| Mod+S | Speichern. Lässt den Speichern-Knopf der Seitenkopfzeile ausführen, damit der Dialog zum Änderungsgrund und der Speicherzustand dieselben sind wie auf dem Bildschirm. In einer Live-Notiz beansprucht Mod+S die Taste und tut nichts. |

Die eigenen Kürzel von Monaco (Suchen, Ersetzen, Mehrfachcursor und so weiter) sind hier nicht aufgelistet, weil es Monaco-Standards sind und keine Wiki.js-Belegungen.

## AsciiDoc-Editor (Monaco)

Quelle: `frontend/src/components/EditorAsciidoc.vue`. Dieselben Belegungen wie beim Markdown-Editor: Mod+B, Mod+I, Mod+Alt+Right, Mod+Alt+Left, Mod+S.

## Andere Editoren

Excalidraw, Feedback, Blog, Weiterleitung: in den durchsuchten Quelldateien wurden keine eigenen Tastenbelegungen gefunden. Nicht verifiziert.

## Global (app-weit)

Eine Suche nach `keydown` im Frontend-Quellcode fand Listener nur in `frontend/src/graph/engine.js`, `frontend/src/composables/previewScrollSync.js`, `frontend/src/editor/visual/nodeviews.js` und `frontend/src/editor/visual/slash.js`. Es wurde kein app-weites Tastenkürzel-Register gefunden. Nicht verifiziert: globale Tastenkürzel für Suche oder Navigation.
