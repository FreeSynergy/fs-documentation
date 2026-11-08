# History

## Kurz gesagt

History ist eine Zeitleiste deiner eigenen Arbeit, ohne dass dich jemand beobachtet. Es merkt sich, was in deinen FreeSynergy-Programmen passiert, und hält für jedes Ereignis eine kurze Zeile fest, etwa „diese Seite bearbeitet“ oder „jene Aufgabe erledigt“. Es beantwortet die Frage: Was habe ich, oder was haben wir getan?

## Was hier anders ist

- Es hält eine Zusammenfassung fest, nie den Inhalt. Ein Tagebuchtext bleibt eine Wiki-Seite, und History verweist nur darauf.
- Die Historie ist lokal bei dir. Vertrauliche Dinge gelangen nie hinein, und sie liest weder Beziehungen noch Umfrageantworten.
- Vergessen ist für die Vergangenheit echt: passende Einträge werden entfernt, und ein Datensatz behält nur gesalzene Hashes dessen, was du vergessen hast. So wird ein vergessener Projektname nicht in lesbarer Form gespeichert.
- Du kannst durch die Zeitleiste scrollen, sie filtern und eine volle Stunde in eine einzige Zeile zusammenfassen.
- History besitzt seine Schnittstelle selbst, `history.capnp` in `fs-interfaces`. Sie ist ein Entwurf und als vorläufig markiert.

## Wo es heute steht

Neueste Version: `v0.1.1`. Es gibt **noch kein Fenster und noch keinen Server**.

Heute gibt es eine Zeitleiste der Aktivitäten anderer Programme, neueste zuerst, mit Filtern und Seitenumbruch. Eine Zusammenfassung fasst Serien von Ereignissen auf demselben Objekt zusammen. Du kannst Einträge nach Filter vergessen, aber nur für die Vergangenheit. Es liest vom FreeSynergy-Hub über den Adapter `fs-history-hub`, getestet gegen einen echten Hub. Es hat 49 Tests und wurde in drei Runden von einem unabhängigen Prüfer geprüft.

Noch nicht da: Wer etwas getan hat, ist vorerst leer, und die Zeit ist der Zeitpunkt, an dem der Eintrag ankam, nicht unbedingt der, an dem es geschah. Vergessen betrifft nur diesen Index, nicht das eigene Protokoll des Hubs. Es gibt keine Freigabe und keine Gruppenansicht, keinen Import von Telemetrie und keine Zeiterfassung. Eine abgebrochene Hub-Verbindung wird nicht von selbst wiederhergestellt.

`FreeSynergy.History` (`fs-history`) beantwortet die Frage: **Was habe ich, oder was haben wir getan?** Es zeigt deine eigenen Daten als Zeitleiste, ob für eine Person oder für ein Projekt. Das wurde zuerst `fs-timeline` genannt.

**Status: [core](https://github.com/FreeSynergy/fs-history) v0.1.1, keine GUI; vorläufiger Entwurf der Schnittstelle (2026-11-06).** Siehe den [Gesamtplan](../roadmap.md).

## Idee

Ein **Beobachter** dessen, was geschieht. Jedes Programm führt bereits ein Aktivitätsprotokoll (ADR 0020), und `fs-history` hört zu:

- **Persönlich:** Was habe ich letzte Woche getan, über alle Programme hinweg? Ein Tagebuch (`fs-diary`) ist dann einfach genau das, gefiltert auf mich selbst: eine Oberfläche mit eingebautem Filter. Dort geschriebener Text ist ein Wiki-Eintrag wie jeder andere (ADR 0031).
- **Projekt:** Was ist wann und von wem passiert? Ein Projektbericht muss nicht aus dem Gedächtnis geschrieben werden.
- **Telemetrie als Import:** Auch technische Ereignisse können hinzukommen, etwa mit einem Standard wie OpenTelemetry (Kandidat, noch nicht gelesen). Sie bleiben **lokal, wenn du nicht anders entscheidest**: Telemetrie woanders heißt, Daten wegzuschicken, und hier geschieht das nicht.

## Offene Fragen

Alle Antworten sind vorläufig. Details: [`DESIGN.md`](https://github.com/FreeSynergy/fs-history/blob/main/DESIGN.md).

1. **Hat es eigene Daten?** Es hat keine eigenen Inhalte, aber einen abgeleiteten lokalen Index, weil der Hub nicht nach Zeit, Person oder Projekt suchen kann. Deshalb bleibt es ein kleines Programm und nicht nur eine Ansicht.
2. **Datenschutz:** Es bleibt lokal. Es gibt keine Freigabe und keine Gruppenansicht, bis die Schnittstelle für Freigaben existiert. Rollenzuweisungen und Umfrageantworten werden nie gelesen. `forget` entfernt einen Eintrag nur aus diesem Index; das Protokoll des Hubs behält ihn. Jedes Löschen leert Name und Kontext der Einträge dieses Objekts, weil ein Objekt, das vertraulich geworden ist, als einfaches Löschen ankommt, und die beiden Fälle sehen gleich aus.
3. **Zeiterfassung:** nicht gebaut.
4. **Welche Einträge zählen?** `digest` fasst Änderungen an einem Objekt durch ein Programm innerhalb eines Zeitfensters zusammen.

**Bekannte Grenzen:** Eine verlorene Verbindung zum Hub wird nicht wiederhergestellt. Der Hub liefert das Programm als Akteur und die Empfangszeit als Zeit. Bis er die Originale weitergibt, bedeutet „Person“ das `attributedTo` des Objekts. Deshalb kann „was ich in einem Objekt einer anderen Person geändert habe“ nicht beantwortet werden.
