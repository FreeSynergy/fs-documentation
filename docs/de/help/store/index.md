# Store-Hilfe

Der Store ist das Programm, mit dem du alles andere bekommst. Du installierst darüber Programme, Frontends, Komponenten und Themes, und er hält sie aktuell. Jeder Download wird vor dem Speichern auf deinem Rechner gegen eine Signatur geprüft. Du kannst den Store als Fenster oder als Befehl `fs-store` nutzen.

## Ansichten des Fensters

Das Fenster zeigt jeweils eine Seite. Du wechselst die Seiten oben im Menü **Store**.

- [Programme](programs.md): eine Karte für jedes Programm, mit Install, Open und Update.
- [Installieren und Aktualisieren](installing.md): die Leiste, die die Schritte eines laufenden Auftrags zeigt.
- [Quellen](sources.md): die Git-Quellen, die der Store liest, und das Formular zum Hinzufügen einer Quelle.
- [Einstellungen](settings.md): wann nach Updates gesucht wird, ob sie installiert werden, und der tägliche Timer.
- [Über](about.md): Name, Version, Lizenz und Projektadresse.

## Kommandozeile

- [Kommandozeile](command-line.md): `fs-store sources`, `available`, `install`, `update`, `installed` und die übrigen, jeweils mit einem Beispiel.

## So fängst du an

- Für das Fenster startest du `fs-store` ohne weitere Angaben. Beim ersten Start wird der Store außerdem in dein Menü eingetragen.
- Für die Kommandozeile startest du `fs-store` mit einem Unterbefehl, zum Beispiel `fs-store installed`.
- Starte ihn nicht als root. Der Store arbeitet in deinen eigenen Ordnern und fragt selbst nach einem Passwort, wenn er eins braucht.

Neu hier? Lies zuerst [Den Store installieren](../../start/install.md) und danach [was der Store ist](../../programs/platform/store.md) für die ausführlichere Geschichte.

[Zurück zu aller Hilfe](../index.md)
