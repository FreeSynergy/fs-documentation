# MediaWiki 1.46 — Tastenkürzel

Version: 1.46.2. Quellen:
- Tabelle der Zugriffstasten: https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts (dort steht selbst, dass der Abschnitt zu Abschnitten veraltet ist; Zeilen, die von Abschnitten abhängen, werden daher nicht verwendet).
- Logik der Modifikatoren: https://raw.githubusercontent.com/wikimedia/mediawiki/REL1_46/resources/src/mediawiki.util/jquery.accessKeyLabel.js
- Tasten des VisualEditor: https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts
- CodeMirror: https://www.mediawiki.org/wiki/Extension:CodeMirror (hat einen Hilfedialog für Tastenkürzel; seine Liste wurde nicht gelesen)

## Kernregel: Zugriffstasten

MediaWiki verwendet für Seitenaktionen kein Strg+Buchstabe. Jede Aktion hat einen Buchstaben, die Zugriffstaste. Der Browser ergänzt einen Modifikator. Der Buchstabe der Zugriffstaste ist auf jedem System gleich; der Modifikator hängt von Browser und Betriebssystem ab.

## Modifikator nach Browser und Betriebssystem (aus jquery.accessKeyLabel.js)

| Browser | Windows / Linux / ChromeOS | macOS |
|---------|----------------------------|-------|
| Firefox | Alt+Shift (Windows und Linux) | Ctrl+Option (Firefox 14+) |
| Chrome / Chromium | Alt (Windows und ChromeOS); Alt+Shift unter Linux | Ctrl+Option |
| Safari | Alt (Ersatz) | Ctrl+Option |
| Andere | Alt | Ctrl+Option oder Ctrl |

Quelle: Zweige `accessKeyModifiers` in `jquery.accessKeyLabel.js` (Zeilen 38 bis 78 in der Datei REL1_46). Die Seite https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts nennt dieselben Beispiele für Firefox und Safari. Maßgeblich ist der Code; die Zeile Chrome ist eine Zusammenfassung mehrerer Zweige, daher vor dem Verlassen darauf testen.

## Zugriffstasten (Kern, aus Help:Keyboard_shortcuts)

Die Buchstaben sind die Werte der Seite. Teilen sich zwei Aktionen einen Buchstaben, entscheidet der Kontext.

| Taste | Aktion | Kontext |
|-------|--------|---------|
| e | Diese Seite bearbeiten | jede Seite |
| h | Versionsverlauf anzeigen | jede Seite |
| m | Diese Seite verschieben | jede Seite (falls erlaubt) |
| d | Diese Seite löschen | jede Seite (falls erlaubt) |
| u | Datei hochladen | jede Seite |
| w | Diese Seite beobachten / nicht mehr beobachten | jede Seite (angemeldet); das Bearbeitungsformular hat einen Schalter mit derselben Taste |
| t | Diskussionsseite anzeigen | Nicht-Diskussionsseite |
| c | Inhaltsseite anzeigen (Reiter des Hauptnamensraums) | jeder Namensraum |
| r | Letzte Änderungen | jede Seite |
| x | Zufallsseite | jede Seite |
| z | Hauptseite | jede Seite |
| q | Verzeichnis der Spezialseiten | jede Seite |
| f | Suche (springt zum Suchfeld) | jede Seite; das Sucheingabefeld von Vector trägt diese Zugriffstaste |
| j | Links auf diese Seite | jede Seite |
| k | Verwandte Änderungen | jede Seite |
| l | Meine Beobachtungsliste | angemeldet |
| y | Meine Beiträge | jede Seite |
| n | Meine Diskussionsseite | jede Seite |
| . | Meine Benutzerseite | angemeldet |
| o | Anmelden | nicht angemeldet |
| p | Druckversion | jede Seite |
| p | Vorschau (Bearbeitungsformular) | Bearbeitungsformular (derselbe Buchstabe wie Druckversion) |
| s | Speichern ("Änderungen veröffentlichen") | Bearbeitungsformular (auf Spezialseiten auch "speichern") |
| v | Änderungen anzeigen (Vergleich) | Bearbeitungsformular |
| i | Als kleine Änderung markieren | Bearbeitungsformular |
| b | Feld Zusammenfassung der Bearbeitung | Bearbeitungsformular |
| = | Schützen oder Schutz aufheben | jede Seite |
| + | Neuer Abschnitt | Diskussionsseite |
| . (für IP) | Benutzerseite der IP | nicht angemeldet |

Tasten auf Spezialseiten (Sperren, Export, Import, Hochladen, Benutzerrechte, Bearbeitung der Beobachtungsliste) verwenden `s` ebenfalls für "speichern" innerhalb ihres eigenen Formulars. Vollständige Liste: https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts.

## Editor-Tastenkürzel (VisualEditor, Erweiterung)

Geprüft gegen https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts (letzte Bearbeitung laut eigenem Verlauf am 11. April 2026; die Seite hat keinen Hinweis auf Veraltung). Windows und Linux zuerst, Mac in der Spalte Mac.

| Windows / Linux | Mac | Funktion |
|-----------------|-----|----------|
| Ctrl+B | Cmd+B | Fett |
| Ctrl+I | Cmd+I | Kursiv |
| Ctrl+K | Cmd+K | Link einfügen |
| Ctrl+Shift+K | Cmd+Shift+K | Zitat einfügen (beschriftet "Cite") |
| Ctrl+Z | Cmd+Z | Rückgängig |
| Ctrl+Shift+Z | Cmd+Shift+Z | Wiederholen |
| Ctrl+Shift+V | Cmd+Shift+V | Als reinen Text einfügen |
| Ctrl+\ oder Ctrl+M | Cmd+\ oder Cmd+M | Formatierung entfernen |
| Tab / Shift+Tab | gleich | Liste einrücken / ausrücken |
| Alt+S | Ctrl+Option+S | Speichern ("Änderungen veröffentlichen") |
| Ctrl+Shift+X | Cmd+Shift+X | Schreibrichtung (LTR/RTL) im Editor umschalten |
| Ctrl+D | Cmd+D | Vorlage hinzufügen (im Vorlagendialog) |
| Ctrl+Shift+D | Cmd+Shift+D | Nicht dokumentierten Parameter hinzufügen (Vorlagendialog) |

Die VisualEditor-Seite nennt weitere Tasten für den Vorlagendialog. Nur die gängigen sind hier aufgeführt.

## Quelltext-Editor (Wikitext)

| Tastenkürzel | Status |
|--------------|--------|
| Ctrl+B, Ctrl+I, Ctrl+K im einfachen Editor | ungeprüft; die Liste der bestehenden Seite ist nicht bestätigt |
| Hilfedialog von CodeMirror | vorhanden (Erweiterung); Tastenliste nicht gelesen |
| Tasten der WikiEditor-Leiste | nicht gelesen; https://www.mediawiki.org/wiki/Help:WikiEditor lieferte in diesem Lauf HTTP 404 |

Kein Tastenkürzel des Quelltext-Editors aus der bestehenden Seite übernehmen, bevor es geprüft ist.

## Tastenkürzel speziell für Vector 2022

In den JavaScript-Quellen von Vector 2022 wurde kein `keydown`-Handler gefunden (durchsucht: `resources/skins.vector.js` und `resources/skins.vector.search`, REL1_46). Vector setzt daher über die Zugriffstasten der obigen Tabelle hinaus keine eigenen Tastenbelegungen. Das ist eine Suche in den in diesem Lauf gelesenen Dateien, kein vollständiges Audit.

## Hinweise für unser Frontend

- Zugriffstasten verwenden, wenn wir MediaWiki-ähnliche Tasten wollen. Mac und Windows unterscheiden sich, daher soll das Frontend je Plattform die richtige Tastenbeschriftung zeigen (die Logik in `jquery.accessKeyLabel.js` zeigt, wie).
- Tasten, die mit Browser-Kürzeln kollidieren (zum Beispiel Alt+E, Alt+D, Alt+F in Chromium), sind der Grund für den Ersatz Alt+Shift in Firefox und Chrome unter Linux (siehe Kommentare in `jquery.accessKeyLabel.js`).
- Unsere eigene Tastenliste wird separat entworfen. Die Liste Ctrl+Shift der bestehenden Seite nicht wiederverwenden.
