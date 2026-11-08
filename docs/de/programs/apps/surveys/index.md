# Surveys

## Kurz gesagt

FreeSynergy Surveys lässt eine Person oder eine Gruppe Fragen stellen, Antworten sammeln und das Ergebnis lesen. Es beantwortet die Frage: Wie können wir gemeinsam entscheiden und sicher sein, dass eine anonyme Antwort anonym bleibt? Antworten können einen Namen tragen oder anonym sein.

## Was hier anders ist

- Anonyme Antworten landen nicht im normalen Speicher. Sie gehen in einen separaten Behälter, der weder Protokoll noch Zeitstempel führt, und die Antworten werden durchmischt.
- Ergebnisse erscheinen nur in Paketen von mindestens einer Mindestgruppengröße, sodass das zweimalige Lesen keine einzelne Antwort einer Person verrät.
- Könnten zurückgehaltene Antworten das Ergebnis ändern, sagt das Programm, dass es noch keinen Gewinner nennen kann.
- Eine Umfrage kann in einer kleinen Gruppe beginnen und später auf die größere Gruppe um sie herum ausgeweitet werden, wobei die bereits abgegebenen Antworten erhalten bleiben.
- Eine Entscheidung kann mit den Aufgaben verknüpft werden, die daraus folgen. Surveys besitzt seine offene Schnittstelle selbst.

## Wo es heute steht

Neuester Tag: `v0.3.0`. Heute ist es der Kern, ohne Fenster. Du kannst Umfragen mit Fragen und Bedingungen über die Stufen Entwurf, offen und geschlossen anlegen und bearbeiten. Namentliche Antworten können als Entwurf gespeichert, fortgesetzt, abgeschickt und bei geöffneter Umfrage ersetzt werden. Anonyme Antworten gehen in den separaten Behälter, mit Einmal-Tokens für „eine Antwort pro eingeladener Person“. Für Ergebnisse gibt es eine Zusammenfassung, eine Auswertung mit Zählverfahren wie plurality, approval, majority und supermajority sowie einen CSV-Export. Umfragen lassen sich über Gruppen ausweiten, und eine Entscheidung kann mit Aufgaben-IDs verknüpft werden. Es hat 107 Tests mit echten Speichern und wurde in drei Runden von einer unabhängigen Prüferin oder einem unabhängigen Prüfer geprüft.

Noch nicht vorhanden (geplant): ein Fenster und ein Server. Tokens werden erst wirklich zugestellt, wenn der Messenger angebunden ist. Öffentliche Links und Einbettung sind nicht möglich, und DDI-Export wird nicht unterstützt. Anonymität hat klar benannte Grenzen: Wer die Maschine betreibt, kann den Speicher während einer Abstimmung trotzdem auslesen, und ein Fenster muss diese Grenzen zeigen. Es gibt nur einen Umfragespeicher pro Prozess. Die Schnittstelle ist ein Entwurf, als vorläufig markiert, weil noch keine Frontends für Umfragen analysiert wurden.

`FreeSynergy.Surveys` (`fs-surveys`) erstellt Umfragen und Abstimmungen, sammelt Antworten und zeigt Ergebnisse, mit Anonymität, wo sie nötig ist.

Den Plan findest du im [Gesamtplan](../roadmap.md); den aktuellen Stand siehe oben unter „Wo es heute steht“.

- [Design](design.md): wie es gebaut ist, Anonymität, offene Fragen
- [Anforderungen](requirements.md): was es können muss (vorläufig)

Für diese Kategorie wurden noch keine Frontends analysiert. Kandidaten für die Analyse sind LimeSurvey, Nextcloud Forms, Formbricks, Framadate, Google Forms und Microsoft Forms. Die [Demokratie-Suite](../../suites/democracy/index.md) ist ein verwandter Bereich.
