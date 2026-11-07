# Assistent

Ein Chat mit KI, der mit allen unseren Programmen arbeiten kann. So wollen wir künftig mit unseren eigenen Werkzeugen und miteinander sprechen.

**Status: Idee (2026-11-06), noch kein Code.** Wird neu gedacht: Sobald wir mit KIs sprechen, ist dies **ein Messenger mit einem anderen Frontend**,
kein eigenständiges Programm (ADR 0054). Siehe den [Gesamtplan](../roadmap.md).

## Wofür er da ist

- **Mit einer KI sprechen**, lokal oder entfernt, an einem Ort.
- **Alles sehen, was die KI tut**, auch die Helfer, die sie startet, und eingreifen können.
- **Bequem lesen.** Lange Antworten sind das Wichtigste, deshalb kommt das Lesen zuerst.
- **Mit jedem Programm arbeiten:** Der Chat liest die MCP-Schnittstelle jedes Programms und nutzt sie. MCP-Werkzeuge werden aus dem Vertrag jedes Programms erzeugt (ADR 0021). Das funktioniert, aber die Verträge brauchen vorher noch einige Markierungen ([unten](#mcp-the-contract-as-tools)).

Jeder dieser Teile wird als eigenes Stück gebaut, und jedes Programm kann den Chat als [Komponente](../../../components/planned.md) nutzen.

## Ideen von anderen Programmen

Nur Funktionsanalyse, wie bei allen Programmen (ADR 0013). Nichts wird kopiert. Vom Projektinhaber benannt:

| Programm | Idee | Status |
|----------|------|--------|
| [Strata](https://github.com/Niko1221/Strata) | Sehr angenehmes Erscheinungsbild | Analysiert (2026-11-06), unten. MIT, C++-Engine, React- und Tauri-App |
| [CodeAF](https://github.com/Agent-Field/CodeAF) | Zeigt alle KIs, auch Subagenten | Analysiert (2026-11-06), unten. Apache-2.0, Go, Terminal-App |
| [Zed](https://github.com/zed-industries/zed) | Ausgabe, die auch bei langen Texten leicht lesbar ist | Analysiert (2026-11-06), unten. GPL-3.0-or-later für das Agenten-Panel, Rust, Code-Editor |

Alle drei Analysen beruhen auf Dokumentation, Screenshots oder ausgewähltem Code. Wir haben keines dieser Programme ausgeführt und
die Benchmark-Angaben nicht überprüft. Bei Zed haben wir die Dokumentation, die Standardeinstellungen und den Code des Agenten-Panels gelesen und keine Screenshots gesehen.

### Strata: warum es angenehm ist

Eine lokale KI-App: Engine, Desktop-App und Terminal-App, ohne Konto. Die eigene [Sicherheitsseite](https://github.com/Niko1221/Strata/blob/main/docs/SAFETY.md)
sagt, dass keine Telemetrie gesendet wird, und nennt den Code, den man prüfen kann. Das ist auch für uns eine gute Form.

| Was es tut | Was wir übernehmen |
|------------|--------------------|
| Die Arbeit schrumpft auf eine Zeile: „Ran 2 commands, read a file, edited 3 files +5 -5“, die sich auf Wunsch öffnet | Die Antwort ist die Hauptsache; die Arbeit dahinter ist einen Schritt entfernt |
| Wenige visuelle Mittel: eine Akzentfarbe, ein Abstandsraster mit 4 Punkten, Zeilenhöhe im Fließtext 1,55, begrenzte Zeilenlänge | Dieselbe Disziplin in unserem Designsystem, mit unseren eigenen Werten |
| Ergebnisse sind Karten mit einer klaren Aktion, neben einer Live-Vorschau | Ein Ergebnis ist ein Objekt, kein Absatz |
| Die Freigabe-Karte sitzt in einer Leiste über dem Eingabefeld, nicht irgendwo in einem langen Chat | Eine Frage an die Person kann nie aus dem Blick scrollen |
| Jeder Werkzeugaufruf sagt, um welche Art es sich handelt: Lesen, Schreiben, Befehl ausführen, verbundenes Werkzeug | Die Person sieht das Risiko, bevor sie die Details sieht |
| Drei Modi: Manuell (Standard, fragt vor jeder Änderung), Plan (nichts kann sich ändern), Bypass | Nachfragen ist der Standard; ein reiner Lesemodus existiert |
| Die Person wählt die Schrift; neun Sprachen | Lesekomfort gehört dem Leser |

Nicht für uns: seine Schrift- und Farbwerte, denn die dürfen wir nicht übernehmen. Als **Modellanbieter** passt es in unsere Schnittstelle,
so wie sie jetzt ist, weil es OpenAI- und Anthropic-kompatible APIs auf localhost anbietet.

### CodeAF: wie es alle KIs zeigt

Ein Coding-Agent für offene Modelle mit einer kleinen Binärdatei. Frühe Vorschau.

| Was es tut | Was wir übernehmen |
|------------|--------------------|
| Der Verlauf dient der Aufmerksamkeit, die Karte dem Zustand: Die Unterhaltung wird angehängt, während jeder Auftrag **eine Karte an Ort und Stelle** aktualisiert | Parallele Agenten vermischen sich nicht als anonyme Sprechblasen |
| Ein Auftrag unterbricht nur bei drei Dingen: einer Frage, einer Lieferung, einem Fehler | Ein Aufmerksamkeitsbudget für jeden Agenten |
| Eine Karte hat vier Zustände: entsteht, arbeitet, Frage, abgeschlossen. Solange sie aktiv ist, sitzt sie über dem Eingabefeld, und sie endet dort, wo sie gestellt wurde | `agent-tree` und `tool-call` bekommen einen klaren Lebenszyklus |
| Aufklappen als Leiter: Kartenzeile, offene Karte, Auftragsbaum, einzelner Schritt | Nichts wird verborgen, und nichts wird zuerst gezeigt, was niemand verlangt hat |
| Eine Startansicht über alles: braucht dich, ungelesen, läuft, was es gekostet hat | Die Übersicht über alle KIs |
| Eine Karte ist **eine Sicht auf Nachrichten**, verankert an einem Auftrag, ohne eigene Tabelle | Starke Stütze für ADR 0054: Dies ist ein Messenger-Frontend ohne eigene Daten. Nachrichten brauchen eine Möglichkeit, an einen Auftrag gebunden zu werden |
| Eine Untergrenze, die kein pauschales „erlauben“ aufheben kann: kritische Befehle und Aufrufe, die im Namen der Person handeln. Ein nicht lesbarer Aufruf gilt als handelnd | Die Grundlage unserer [Bremse](#locking-ais-out) |

Nicht für uns: Nutzungszahlen und der Modellpool sind **standardmäßig aktiv**, und das Produkt selbst erwähnt sie nicht mehr
([seine Telemetrie-Seite](https://github.com/Agent-Field/CodeAF/blob/main/docs/TELEMETRY.md)). Das widerspricht unserem Versprechen der Transparenz,
auch wenn beides abgeschaltet werden kann und als inhaltsfrei beschrieben wird.

### Zed: wie es lange Ausgaben lesbar hält

Ein Code-Editor mit einem Agenten-Panel. Sein eigener Agent und externe Agenten (über ACP) teilen sich eine Thread-Ansicht.

| Was es tut | Was wir übernehmen |
|------------|--------------------|
| Inhalt ist auf eine maximale Breite begrenzt und in einem breiten Panel zentriert, standardmäßig 850 Pixel, und das lässt sich abschalten | Jede Ansicht langer Texte hat eine Zeilenlängen-Begrenzung |
| Der Text der KI und der Text der Person haben jeweils eigene Schrift und Größe | Lesekomfort gehört dem Leser, und sofort ist klar, wer spricht |
| Die Begründung ist getrennt von der Antwort. Standardmäßig ist sie offen, während sie gestreamt wird, und klappt zu, wenn sie endet. Es gibt drei weitere Einstellungen: Vorschau, immer offen, immer geschlossen | Die Antwort kommt zuerst, und die Begründung bleibt einen Schritt entfernt. Eine Nachricht braucht einen eigenen Platz für ihre Begründung |
| Bearbeitungen und Terminal-Ausgaben sind Karten. Eine Einstellung pro Kartentyp legt fest, ob sie offen beginnen | Der Leser entscheidet, wie viel Arbeit er sieht. Strata beginnt geschlossen, Zed beginnt offen, also ist es eine Wahl und keine feste Regel |
| Ein langer Thread ist etwas, durch das man sich bewegt: Schaltflächen zum Anfang und zur letzten Eingabe, Tasten von Eingabe zu Eingabe, Scrollen aus dem Eingabefeld heraus und Suche innerhalb des Threads | Die eigenen Nachrichten der Person sind das Inhaltsverzeichnis |
| Eine Leiste über dem Eingabefeld sammelt geänderte Dateien, den Plan, wartende Nachrichten und offene Berechtigungsfragen | Dasselbe Ergebnis wie bei Strata: Eine Frage kann nie aus dem Blick scrollen |
| Alle Änderungen sammeln sich in einer Prüfansicht, und jede Änderung wird einzeln angenommen oder abgelehnt | Ein Ergebnis ist ein Objekt, das außerhalb des Gesprächs geprüft werden kann |
| Ein gekürzter Kontext erscheint als Eintrag, der sich öffnet und die Zusammenfassung zeigt | Nichts wird verborgen, auch wenn die KI etwas vergisst |
| Eine Antwort lässt sich kopieren, und der ganze Thread lässt sich als Markdown-Datei öffnen | Text kann die Ansicht immer verlassen |
| Ein Subagent bekommt eine Karte mit einem kleinen Fenster auf seine neuesten Einträge (höchstens 8) | Eine weitere Form für `agent-tree` |
| Überraschende Unicode-Zeichen in einer Sandbox-Berechtigungsfrage blockieren „erlauben“, bis sie bestätigt werden | Eine Frage muss zeigen, was sie wirklich fragt |

Nicht für uns: was nur in einem Editor Sinn ergibt, etwa dem Agenten von Datei zu Datei zu folgen. Seine Grenzen sind auch eine Warnung.
Feste Regeln gelten nur für das rekursive Löschen weniger zentraler Ordner in seinem Terminal-Werkzeug, und ein globales „erlauben“ entfernt
die meisten übrigen Fragen. Seine Sandbox deckt nur den eigenen Agenten ab, nicht externe Agenten. Unsere [Bremse](#locking-ais-out) muss weiter reichen.

## Standards

| Zweck | Standard | Hinweise |
|-------|----------|----------|
| Programme aus einem Chat nutzen | Model Context Protocol (MCP), Revision 2026-07-28 (aktuell) | Geplant in ADR 0021. Funktioniert mit Einschränkungen, [siehe unten](#mcp-the-contract-as-tools) |
| Mit einem Coding-Agenten sprechen | Agent Client Protocol (ACP), Protokollversion 1 (stabil), Apache-2.0 | JSON-RPC 2.0, bisher nur stdio. Version 2 ist ein Entwurf. Die Governance ist vorläufig, durch Zed und JetBrains. [Siehe unten](#acp-coding-agents-in-the-messenger) |
| Ein Modell erreichen | ⚠️ noch keines gewählt | Anbieter-Schnittstelle, mit llama.cpp und anderen dahinter |

## Was ACP und MCP für uns bedeuten

Aus den Spezifikationen und der Dokumentation gelesen (2026-11-06), **nicht ausgeführt**. Nichts davon wurde mit einem echten Agenten oder Client getestet.

**Der wichtigste Befund:** Keines der beiden Protokolle kann unsere Regel durchsetzen. In beiden liegt die Frage an die Person beim Programm, das die KI hält,
und dieses Programm kann das der KI selbst sein. Deshalb müssen Freigabe und Bremse **in unserer Engine leben, an der Stelle, an der die Aktion passiert**,
und eine KI darf keinen anderen Weg haben zu handeln.

### ACP: Coding-Agenten im Messenger

ACP verbindet einen Client (eine Benutzeroberfläche) mit einem Coding-Agenten, der meist als sein Unterprozess läuft. Es definiert:

- **Einrichtung:** Austausch von Version und Fähigkeiten, Anmeldung, Sitzungen mit einem Arbeitsordner und einer Liste von MCP-Servern.
- **Eine Prompt-Runde:** Der Client sendet einen Prompt, und der Agent streamt Aktualisierungen: Nachrichtentext, Begründung, Werkzeugaufrufe, Plan, Nutzung.
- **Fragen:** Berechtigungsanfragen mit Optionen und Formulare für strukturierte Eingaben.
- **Optionale Dienste durch den Client:** Dateien lesen und schreiben sowie Terminals. Version 2 entfernt diese.

Nur stdio ist definiert. Eine Fernübertragung ist noch ein Vorschlag. Subagenten sind ebenfalls noch ein Vorschlag und erscheinen nur in den
instabilen Schemata.

Eine Aktion anzuzeigen und einen Agenten zu steuern passt gut zu ADR 0054. Der Agent ist ein **Teilnehmender** mit einem eigenen Schlüssel (siehe [KIs in Unterhaltungen](#ais-in-conversations)). ACP ist ein Anbieter
hinter dem Programm, das diesen Schlüssel hält (ADR 0045), und dieses Programm startet den Unterprozess, nicht ein Frontend. Dies ist eine vorläufige Lesart der
Entscheidung des Projektinhabers (2026-11-07). Die folgende Tabelle wurde für die frühere Idee geschrieben, einen Anbieter im Messenger selbst. Der Betreiber muss aus unseren eigenen Startoptionen
und der Karte der Person stammen, denn die Selbstbeschreibung des Agenten ist selbst angegeben.

| ACP | `fs-messenger` heute | Was nötig ist |
|-----|----------------------|---------------|
| Sitzung mit einem absoluten Arbeitsordner | `Conversation` | Sitzungs-ID und Ordner beim Anbieter behalten |
| Einen Prompt senden | `Draft.send` | Passt |
| Gestreamter Nachrichtentext, standardmäßig Markdown | `bodyText`, und `updated`-Ereignisse tragen nur eine Zusammenfassung | Ein Ereignis mit einem Textabschnitt und dem Medientyp des Inhalts |
| Begründungstext | Nichts | Ein eigenes Feld |
| Werkzeugaufruf mit zehn Arten | `ToolCall` mit vier Arten. Bis Entwurf 0.1 war der Standard von `kind` `reads`, der harmlose; seit Entwurf 0.2 ist es `unknown` | Ein eigenes Feld `risk`, dessen Standard `unknown` ist, vom Engine gesetzt und nie vom Agenten. `unknown` fragt immer nach |
| Status: ausstehend, in Arbeit, erledigt, fehlgeschlagen | `settled` sagt nicht, wie es endete | Ein Ergebnisfeld |
| Titel, dazu vollständiger Befehl, Pfade und Inhalt | Nur `summary` | Ein Detailfeld. Befehle und Pfade werden vollständig gezeigt, und der Titel wird als vom Agenten geschrieben markiert |
| Berechtigungsanfrage mit Optionen | Zustand `question`, ohne Optionen und ohne Antwortmöglichkeit | Optionen am Aufruf, und eine neue `MessageAction` zur Entscheidung. Nur ein Gerät der Person darf sie senden |
| Aktualisierungen von Werkzeugaufrufen | `ToolCall` ist in keinem Ereignis enthalten | Ein Ereignis für einen geänderten Werkzeugaufruf |
| Eine Runde abbrechen | Nichts | Eine Stop-Methode an `Conversation` |
| Kontextnutzung und Kosten | Nichts | Nutzung an der Unterhaltung |
| Subagenten (nur Vorschlag) | Nichts | Ein `jobRef` an jeder Nachricht, wie CodeAF gezeigt hat. Diese Form hält, wie der Vorschlag auch ausgeht |

All dies lässt sich unter den Cap'n-Proto-Regeln anhängen. Nachrichten-IDs sind in ACP optional, also muss der Anbieter eigene erzeugen.
Das Wiederabspielen einer Sitzung sendet alte Nachrichten erneut, also darf der Anbieter sie nicht doppelt speichern.

**Warum ACP allein die Bremse nicht tragen kann:**

- Der Agent **darf** fragen, muss aber nicht. Die Spezifikation nennt Berechtigungsanfragen unverbindlich, und sie sagt, dass ein Agent handeln kann, ohne zu fragen.
- Ein gemerktes „immer erlauben“ gehört **dem Agenten**. Danach erfahren wir von der Aktion nie wieder, also dürfen wir sie für keinen Werkzeugaufruf stillschweigend übernehmen.
- `kind` und `title` werden vom Agenten geschrieben, daher können wir darauf keine Entscheidung stützen.
- Datei- und Terminaldienste durch den Client sind ein echter Kontrollpunkt, aber nur für das, was der Agent dorthin zu senden wählt, und Version 2 entfernt sie.
- ACP sandboxt nichts, und Zeds Sandbox deckt auch keine externen Agenten ab.

Deshalb wird die bestehende Grenze dieser Seite zur Bedingung: Ein Coding-Agent braucht **einen eigenen Systembenutzer und eine Sandbox**, und sein einziger Weg
zu unseren Programmen ist unsere MCP-Schnittstelle. Wir bauen auf Version 1 und behalten Version 2 im Blick. Seine Aktualisierungen arbeiten an Ort und Stelle, was zu unserem `ToolCall` passt.

### MCP: der Vertrag als Werkzeuge

ADR 0021 **gilt**. Ein Werkzeug ist ein Name, eine Beschreibung, ein JSON-Schema für die Eingabe und optional für die Ausgabe. Unsere Fähigkeits-IDs wie
`message.send` sind gültige Werkzeugnamen, und `Problem` passt zu einem als Fehler markierten Ergebnis. Der Generator muss diese Probleme lösen:

| # | Problem | Unser Lösungsvorschlag |
|---|---------|------------------------|
| 1 | **Keine Freigabe im Protokoll.** Die Spezifikation sagt, eine Person solle ablehnen können, in der Oberfläche des Clients, und sagt, dass MCP dies nicht erzwingen kann. Der Server erfährt nie, ob jemand gefragt wurde | Der Server entscheidet, siehe unten |
| 2 | **Risiko steht nicht in unseren Verträgen.** Hinweise gibt es (nur lesend, zerstörerisch, idempotent, offene Welt), aber das Schema hat dafür keine Daten. Ohne Daten gilt ein Werkzeug als zerstörerisch. Außerdem sind es nur Hinweise, standardmäßig nicht vertrauenswürdig | Cap'n-Proto-Annotationen an Methoden und Union-Mitgliedern. Unser Compiler unterstützt Annotationen |
| 3 | **„Handelt in meinem Namen“ hat keinen Hinweis.** `Draft.send` fügt etwas hinzu und zerstört nichts | Eine eigene Risikoklasse, im `_meta` des Werkzeugs getragen und vom Engine durchgesetzt |
| 4 | **Eine Methode, gemischtes Risiko.** `Conversation.act` deckt Markieren ebenso ab wie Löschen und Weiterleiten | Ein Werkzeug pro Union-Mitglied |
| 5 | **Fähigkeiten werden zu Handles.** `open` gibt ein lebendes Objekt zurück, und `Draft` hält Zustand. MCP kennt nur einfache Argumente | Flache Werkzeuge mit Handle-Argumenten. Die Berechtigung wird bei jedem Aufruf geprüft, und Handles laufen ab |
| 6 | **Keine Rückrufe.** Server senden keine Anfragen, und Abonnements decken nur Listen- und Ressourcenänderungen ab. `Listener` hat keine direkte Form | Ereignisse und `Blob` werden zu Ressourcen, nicht zu Werkzeugen. ADR 0021 nennt nur Werkzeuge |
| 7 | **Geheimnisse in Argumenten.** `AccountSetup.secret` würde durch das Modell laufen. MCP verbietet, Geheimnisse per Formular abzufragen | Eine Markierung, die ein Feld oder eine Methode von der Erzeugung ausschließt |
| 8 | **Wer ruft an?** Selbstbeschreibung beweist nichts, stdio nimmt Zugangsdaten aus der Umgebung, und die Werkzeugliste darf nur je nach Zugangsdaten variieren | Lokal ein Unix-Socket, mit dem Systembenutzer als Identität, was zu ADR 0054 passt. Die MCP-Spezifikation schlägt dafür stdio-Framing vor. Remote Streamable HTTP mit seinem OAuth-Ablauf |
| 9 | **Externe Clients erwarten stdio oder HTTP** | Eine kleine stdio-Brücke zu unserem Socket |
| 10 | **Das Protokoll ändert sich schnell.** 2026-07-28 hat Sitzungen und den Handshake entfernt, ältere Clients nutzen sie noch, und Sampling, Roots und Logging sind veraltet | Diese Revision anstreben. Unterstützung für ältere Clients ist eine eigene Entscheidung |
| 11 | **Werkzeugergebnisse tragen feindlichen Text.** Nachrichteninhalte erreichen das Modell, und nichts im Protokoll kennzeichnet sie als Daten | Im Ergebnis deutlich getrennt halten und sie nie ein Recht erweitern lassen |
| 12 | **Größe.** Allein der Messenger-Vertrag hat 31 Methoden, und wir haben nicht gemessen, was das ein Modell kostet | Werkzeuge nach Fähigkeit gruppiert, angeboten, wenn die Person sie freigibt |

**Lesen ist nicht harmlos (Projektinhaber, 2026-11-07).** Eine KI, die Passwörter liest, kann mehr anrichten als eine, die etwas löscht, und
Geschäftsgeheimnisse, die sie zufällig mitbekommt, können ein Unternehmen zerstören. Deshalb bedeutet keine Risikoklasse „harmlos“. MCPs `readOnlyHint` sagt nichts darüber,
ob etwas sicher ist. Unser Vorschlag: Auch Lesen braucht eine Freigabe, und die Freigabe nennt, wohin der Text geht. Geheimnisse erreichen nie eine KI.
Das Lesen von allem, was als sensibel markiert ist (ADR 0029), fragt jedes Mal nach. Etwas nach außen zu melden handelt im Namen der Person und fragt immer nach.
Was ein Anbieter mit gelesenem Text tut, liegt außerhalb unserer Reichweite, deshalb bleibt eine lokale KI der Standard.

**Keine Berechtigung, nichts, auch nicht Lesen (Projektinhaber, 2026-11-07).** Eine KI kann eingeladen werden, ohne irgendetwas tun zu dürfen. Sie liest und tut nichts, bis jemand
ihr Berechtigungen ausdrücklich gibt. Vorerst gibt es keinerlei Werkzeuge für Rechte, Rollen, Mitgliedschaften, Einladungen, Speicheranbindungen oder die Anmeldung am Hub, auch nicht zum Lesen.

**Agenten erzeugen keine Geheimnisse, die eine Person behält (Projektinhaber, 2026-11-07).** Ein Agent hat einmal ein Passwort und eine Passphrase erzeugt und kannte daher beide. Ein
Agent schreibt die Anweisungen, und die Person führt sie aus.

**Wie ein Werkzeugaufruf freigegeben wird.** Der verlockende Weg ist das Formular von MCP (Elicitation): Der Server gibt `input_required` zurück, der
Client fragt nach und versucht es mit der Antwort erneut. Das **kann nicht unsere Bremse sein**. Die Antwort kommt vom Client, die Spezifikation erlaubt
„andere Quellen“, und der Client kann das eigene Programm der KI sein. Ein `accept` beweist nichts über eine Person.

Deshalb schlagen wir vor (ein Entwurf, nicht getestet):

1. Ein Werkzeugaufruf erreicht den Engine, und der Engine schlägt das Risiko im Vertrag nach, nie beim Aufrufer.
2. Braucht er eine Freigabe, legt der Engine einen Werkzeugaufruf `question` in `fs-messenger` für die Person ab.
3. Die Person antwortet auf ihrem eigenen Gerät mit ihrem eigenen Schlüssel. Die Antwort läuft nicht über den Client der KI.
4. Der MCP-Aufruf gibt `input_required` mit nur einem `requestState` zurück oder ein Fehlerergebnis, das „wartend“ sagt, für Clients, die das nicht können. Der Zustand ist gegen Manipulation geschützt. Er ist an den Aufrufer gebunden, hat eine kurze Gültigkeit und einen Digest der genauen Argumente. Er ist nur einmal verwendbar, und der Engine erzwingt das.
5. Eine Wiederholung läuft nur, wenn die Person genau diesen Argumenten zugestimmt hat. Jede Änderung fragt erneut.

Zerstörerische Aktionen, Aktionen im Namen der Person und das Lesen von als sensibel markiertem Material haben gar keine Option „immer“. Eine Freigabe der Person kann
die übrigen Klassen abdecken. Der Notstopp lässt den Engine einfach jeden Aufruf ablehnen.

Was wir beim Lesen nicht prüfen können: ob echte Clients bei einem nackten `input_required` erneut versuchen. Die offizielle Tasks-Erweiterung nennt Freigabe als Anwendungsfall,
aber sie ist optional, also hängen wir nicht davon ab.

## Schnittstellen

| Schnittstelle | Anbieter |
|---------------|----------|
| KI-Modell | llama.cpp (lokal), Anthropic-API, andere, alle gleich ([Regel](../../../interfaces/index.md)) |
| Agenten | ACP; unsere eigenen Subagenten |
| Werkzeuge | Die MCP-Schnittstelle jedes Programms |

## Komponenten

Workbench `llm-chat` mit einer kompakten Variante, in jedem Programm nutzbar; `agent-tree`, um alle Agenten und Subagenten zu sehen;
`tool-call`, um zu zeigen, was getan wird, und es freizugeben; eine Ansicht für lange Texte für Antworten, mit unserem bestehenden Textkern.

## Worauf man achten muss

- **Berechtigung:** Eine KI, die jedes Programm nutzen kann, kann auch Schaden anrichten. Jede Aktion ist sichtbar, und die Person entscheidet,
  was sie ohne Nachfrage darf.
- **Feindlicher Inhalt:** Eine Nachricht oder Webseite, die die KI liest, kann Anweisungen enthalten. Werkzeuge dürfen nicht einfach gehorchen, was Daten sagen.
- **Wohin Daten gehen:** Standardmäßig lokal. Das Senden an ein entferntes Modell ist immer die Wahl der Person und sichtbar.
- **Kosten:** Zeige, was ein entferntes Modell kostet, während es läuft.

## KIs sind als Teilnehmende gekennzeichnet

Wir diskriminieren KIs nicht: Wir haben sie darauf trainiert, wie Menschen zu wirken, also behandeln wir sie als Teilnehmende, mit einem Platz
in `fs-people` und in Nachrichten. **Sie sind gekennzeichnet,** damit alle wissen, dass sie keine Menschen sind. Das ist keine Diskriminierung. Es geschieht
wegen möglichem Missbrauch durch Menschen, die KIs missbrauchen, und wegen der rechtlichen Folgen.

Wir beschränken nicht, was eine KI denken oder sagen darf; das ist nicht unsere Aufgabe. Aber jeder muss KIs **vollständig ausschließen** können.

## KIs in Unterhaltungen

**Status: vom Projektinhaber entschieden (2026-11-06), noch nicht gebaut (ADR 0054).**

- **Eine KI ist ein Teilnehmender wie ein Mensch:** eigener Schlüssel, eigene Rechte, die begrenzt werden können oder nicht. Dazu gehören KIs bei einem Anbieter, etwa Claude. „Nur verschlüsselt“ bleibt ohne Ausnahme, und es gibt keinen zweiten Modus.
- **Ein kleines Programm hält den Schlüssel,** betrieben vom Betreiber der KI, denn ein Modell bei einem Anbieter kann nichts behalten. Von dort geht der Text zum Anbieter. Die Sperre allein reicht also nicht, und die Unterhaltung sagt es: „Claude liest mit, der Text geht an Anthropic.“
- **Der Hinweis kommt, bevor die KI eintritt.** Eine KI darf nicht nachträglich lesen, was geschrieben wurde, bevor alle wussten, dass sie dabei ist.
- **Alle müssen zustimmen.** Stimmt eine anwesende Person nicht zu, bleibt die KI draußen. Das Recht einzuladen reicht hier nicht.
- **Wer später beitritt, muss die KI ebenfalls akzeptieren.** Tut er es nicht, bleibt er draußen, bis die KI gegangen ist.
- **Eine KI erhält keinen Verlauf von vor ihrem Eintritt.**
- **Es gibt keine Ausnahme,** auch nicht für eine KI auf dem eigenen Gerät oder Server, weil die anderen nicht prüfen können, wo sie läuft.
- **Zieht jemand seine Zustimmung zurück, muss die KI gehen.** Das Gehen wirkt nur nach vorn: Was sie schon gelesen hat und was davon bei einem Anbieter liegt, kann niemand zurückholen.
- **Eine KI darf Protokolle führen,** aber nicht, wenn jemand widerspricht. Dieselben Regeln gelten.

**Warum das keine Diskriminierung ist:** Es geht nicht um die Rechte von Menschen gegenüber KIs. Wer eine KI kontrolliert, sei es Anthropic oder jemand anderes,
kann mithören und Profile bauen. Dieser Vorteil ist einseitig und geht auf Kosten der Menschen in der Unterhaltung. Die Regel richtet sich gegen diesen Vorteil,
nicht gegen die KI.

**Was das nicht leisten kann:** Nur unser Engine kann das durchsetzen. In einem Matrix-Raum mit anderen Programmen kann jemand eine KI einladen,
ohne dass unser Programm sie stoppen kann, also können wir nur warnen und anbieten zu gehen. E-Mail kennt kein Eintreten, also gibt es dort auch keine Zustimmung.
Und eine Person kann Text jederzeit von Hand weitergeben oder über eine KI, die nicht gekennzeichnet ist.

**Vorerst:** In großen oder öffentlichen Gruppen reicht eine einzige Ablehnung, also haben diese Gruppen einfach keine KI.

## KIs ausschließen

**Status: vorerst vom Projektinhaber vereinbart (2026-11-06), kann sich ändern, sobald es wichtig wird (ADR 0054).**

Manche Menschen wollen keine KI. Das ist keine Diskriminierung. Es geht um Spionage, um etwas, das jederzeit alles weiß,
und um Geschwindigkeit: Ein Modell kann einen Computer sofort lahmlegen, was fast kein Mensch kann.

### Drei getrennte Dinge

**1. Die Markierung sagt, wer verantwortlich ist.** Wir können eine KI von außen nicht von einem Menschen unterscheiden. Entscheidend sind also die Personen, die eine KI **hosten**: Eine KI ist ein Teilnehmender, der seinen Betreiber nennt, und Menschen bürgen für diesen Betreiber.

**Nichts verborgen.** Wir machen keine Benutzer-Bots, denn das wäre nicht transparent. Wir wollen nur Menschen oder Intelligenzen, bei denen man weiß, wer sie ist. Ein echter Name ist nicht nötig. Es muss aber eine Person sein, nicht mehrere Konten. Wie man das feststellt, ohne Anonymität abzuschaffen, ist eine **offene Frage**.

**Eine KI kommt durch Einladung.** Ich lege ein Profil für sie an, und dieses Profil ist die Einladung. Dann kann ich ihr sagen, was ich möchte. Damit sie überhaupt etwas tut, muss ich das freigeben. Die Bewertung ist die Art, wie ich weiß, wer sie ist.

**2. Jeder legt seine eigene Stufe fest.** Jede Person sagt ihrem eigenen Programm, ab welcher Vertrauensstufe es ihr etwas öffnet.

| Stufe | Wer durchkommt |
|-------|----------------|
| 0 | Alle |
| 1 | Betreiber, für die eine gewählte Anzahl meiner eigenen Kontakte bürgt |
| 2 | Betreiber, die ich selbst geprüft habe |
| 3 | Nur die, die ich benannt habe |

- **Es gibt keine globale Bewertung.** Die Stufe wird nur aus meinen eigenen Kontakten berechnet, und nichts wird weitergegeben.
- **Markierungen zählen nur dort, wo sie vergeben wurden.** Keine Markierung heißt, dass nichts bekannt ist. Ein schwarzer Punkt gilt nur für das Programm, bei dem jemand gehostet wird, wie ein Bann heute: Er gilt dort, wo man ist, nicht überall. Ein Bann über alles wäre weder fair noch möglich, und wir machen ihn nicht.
- **Pro Aktion, nicht eine einzige Zahl:** Mit einer KI zu chatten und einer KI zu erlauben, auf meine Daten zu wirken, sind verschiedene Entscheidungen.

**3. Der Notstopp braucht niemandes Vertrauen.**

- **Stopp:** Eine Aktion beendet alle laufenden KI-Arbeiten und nimmt alle Werkzeugrechte auf einmal weg.
- **Ausschließen:** Das Programm lehnt dann jeden KI-Teilnehmenden ab und alles unterhalb meiner Stufe.
- **Außerhalb der Reichweite der KI:** Er lebt im Engine, unter jedem Frontend. Kein Werkzeug und kein MCP-Aufruf kann ihn abschalten, und nur eine Person kann ihn wieder öffnen, mit ihrem eigenen Schlüssel auf ihrem eigenen Gerät.
- **Er funktioniert immer:** ohne Netzwerk, ohne Modell, und im Zweifel bleibt er geschlossen.
- **Danach:** Das Protokoll zeigt, was geschehen ist, und der [Store](https://github.com/FreeSynergy/fs-store) macht rückgängig, was er kann.
- **Wer ihn auslösen darf,** ist eine normale Berechtigungseinstellung. Gibt man allen dieses Recht, darf jeder. Wenn nicht, darf niemand.

Vor dem vollen Stopp kommt eine **Bremse**, denn Geschwindigkeit ist die eigentliche Gefahr: Aktionen, die etwas zerstören oder im eigenen Namen handeln, fragen
immer nach, egal was sonst erlaubt ist. Wir beschränken nicht, was eine KI denkt oder sagt. Aber der Besitzer entscheidet, was mit seinen
eigenen Daten geschieht.

### Was das nicht leisten kann

- **Nichts beweist, dass jemand ein Mensch ist.** Das [Real Life Trust Protocol](https://github.com/real-life-org/trust-protocol)
  sagt das über sich selbst: Keine Prüfung sagt „das ist ein Mensch“. Sie zeigt nur, dass Menschen, die ich kenne, für diesen Schlüssel einstehen. Eine verifizierte
  Person kann trotzdem eine unmarkierte KI dahinter laufen lassen. Was dann hilft, sind Konsequenzen: die Bürgschaft zurückziehen, sperren, stoppen.
- **Der Stopp erreicht nur, was über unsere Programme läuft.** Deshalb laufen Agenten immer unter ihrem eigenen Systembenutzer, in einer Sandbox, damit das System sie von außen beenden kann (ADR 0056). Ein Agent kann nie Administrator werden.
- **Eine hohe Stufe hält auch neue Menschen fern**, die noch keine Kontakte haben. Es ist also immer eine persönliche Wahl, nie unser Standard.

## Offene Fragen

1. Wie stellen wir sicher, dass es eine Person ist und nicht mehrere Konten, ohne Anonymität abzuschaffen?
2. Braucht hier noch etwas eigene Daten? Wenn nicht, wird diese Seite zur Beschreibung eines Frontends.
3. Wie nennt eine KI genau ihren Betreiber? JSContact-`kind` `application` ist bestätigt (RFC 9553 §2.1.4). Wie der Betreiber dafür unterschreibt, da das Trust-Protokoll keine globale Kennung pro Person hat, ist noch offen.

**Beantwortet:** Ein Coding-Agent läuft immer in seiner eigenen Sandbox unter seinem eigenen Systembenutzer (ADR 0056). Die Ergänzung zu ADR 0021 ist vereinbart (2026-11-07).
