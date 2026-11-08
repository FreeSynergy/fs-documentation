# Wiki-Hilfe

Im Wiki liegen die Texte. Heute ist sein Fenster ein Leser: links ein Baum aus Seiten, rechts die Seite, die du gewählt hast. Du kannst Links folgen, suchen, eine Seite bearbeiten und speichern und eine Seite als Markdown-Datei ausgeben.

## Die Ansichten

- [Seitenbaum](page-tree.md): die Seiten, als Ordner und Seiten.
- [Suchergebnisse](search-results.md): was du bekommst, wenn du in das Suchfeld tippst.
- [Seite](page.md): eine Seite lesen, Links folgen, zurückgehen.
- [Bearbeiten](edit.md): eine Seite ändern, speichern und einen nicht gespeicherten Entwurf zurückholen.
- [Export](export.md): eine Seite in eine Markdown-Datei schreiben.
- [Importprobleme](import-problems.md): Dateien, die nicht sauber importiert wurden.

## So startest du

Das Wiki läuft in einem Server, also starte ihn zuerst: `fs-wiki-server`, mit `--socket PATH` und `--data DIR`, wenn du eigene Pfade willst. Dann startest du das Fenster mit `fs-wiki-app --socket PATH` und `--docs FOLDER` für den Markdown-Ordner, der importiert werden soll. Der erste Start importiert den Ordner, etwa 30 Sekunden für 1400 Seiten. Eine kurze Zusammenfassungszeile erscheint im Terminal, bevor sich das Fenster öffnet. Läuft der Server nicht, stoppt die App und nennt dir den Befehl, um ihn zu starten.
