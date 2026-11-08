# Tasks

## Kurz gesagt

Tasks hält fest, was du oder deine Gruppe zu erledigen habt. Jede Aufgabe kann ein Fälligkeitsdatum, einen Status, Labels und Verknüpfungen zu anderen Aufgaben haben. Es beantwortet eine Frage: Was tue ich oder tun wir als Nächstes?

## Was hier anders ist

- Eine Aufgabe folgt dem offenen Standard JSCalendar (RFC 8984). Dieses Programm besitzt diesen Standard für Aufgaben, sodass der Kalender und jedes andere Programm über eine Schnittstelle auf Aufgaben zugreifen, statt eine eigene Vorstellung von einer Aufgabe zu führen.
- Listen, Statusansichten und später Boards und Zeitleisten sind verschiedene Arten, dieselben Aufgaben zu betrachten.
- Deine Aufgaben werden als iCalendar (VTODO) importiert und exportiert, und der Originaltext bleibt erhalten.
- Als sensibel markierte Aufgaben bleiben aus Exporten heraus, außer du gibst sie namentlich frei.
- Eine Aufgabe kann zunächst nur dir gehören und später geteilt werden.

## Wo es heute steht

Neuester Tag: `v0.8.0`. Du kannst Aufgaben anlegen, bearbeiten, zuweisen, mit Labels versehen, verknüpfen, auflisten und löschen sowie nach Fälligkeitsspanne, Fortschritt, Label oder einem Wort im Titel oder in der Beschreibung finden. Der Import und Export von iCalendar-Aufgaben funktioniert. Andere Programme werden benachrichtigt, wenn sich eine Aufgabe ändert, und ein Überschreiben wird abgelehnt, wenn jemand anders die Aufgabe inzwischen geändert hat. Ein kleiner Server bietet all das über einen lokalen Socket an, und ein erstes, vorläufiges Fenster zeigt eine Liste und eine Statusansicht. Der Kalender zeigt Aufgaben bereits über diese Schnittstelle an.

Noch nicht vorhanden: echte Boards (die Statusansicht ist kein Board; das Verschieben einer Karte ändert den Status der Aufgabe für alle), wiederkehrende Aufgaben über das Beibehalten hinaus, das Zuweisen von Personen, Beziehungen, Checklisten, Kommentare, Anhänge und Erinnerungen im Fenster sowie Rückgängig. Das Fenster liest die Daten direkt, und es gibt noch keine Anmeldung. Die Schnittstelle ist ein Entwurf mit einem Nutzer (dem Kalender).

## Geplante Facetten

Vorgeschlagen, nicht gebaut:

- To-dos: Aufgaben als einfache Listen von Dingen, die zu tun sind.
- Tickets: Aufgaben als Anfragen, die jemand abarbeitet.

`FreeSynergy.Tasks` (`fs-tasks`) beantwortet eine Frage: **Was tue ich oder tun wir als Nächstes?** Kanban-Boards, Listen und Zeitleisten sind verschiedene Arten, dieselben Aufgaben zu betrachten.

Den Code findest du [hier](https://github.com/FreeSynergy/fs-tasks). Siehe den [Gesamtplan](../roadmap.md).

- [Design](design.md)
- [Anforderungen](requirements.md), analysiert aus acht Projektwerkzeugen, geschrieben, als dies noch als `fs-kanban` geplant war

Bisher analysierte Frontends liegen unter [Projektmanagement](../../suites/projectmanagement/index.md).
