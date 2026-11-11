# ENTWURF: Workflow-Standard für FreeSynergy (Opus, 2026-11-12)

Status: Entwurf, kein ADR, kein Code. Grundlage: `A1-standards.md`, `A2-programme.md`, `B-arbeitsweise.md`, `C-install.md` (alle in `/srv/FreeSynergy/.scratch/workflows/`), ADR 0050 (origin/main), ADR 0063 (origin/main), ADR 0073 (Entwurf, Branch `adr-kollaboration`), Tasks-Plan `/srv/FreeSynergy/.wt-tasks-q0/todo/plan-comments-and-dependency-evaluation.md`, `fs-interfaces` v0.0.19 (`/srv/FreeSynergy/.wt-interfaces-19/schema/tasks.capnp`, `enum Readiness`).

Nutzerentscheid (gesetzt): Installieren ist eine Anweisung (ein Workflow), Paket schnüren ist derselbe Workflow rückwärts. Workflows werden standardisiert UND gezeigt (Knoten und Linien wie auf einem Whiteboard). Handelnde: Mensch, LLM, Maschine, Programm. Zuerst nur eine feste Liste standardisierter Befehle. Was immer gleich abläuft, wird Standard und spart Tokens.

**Fassung 2 (gleicher Tag), Nutzerrichtung über Strategie:** „Ein Gantt ist nichts anderes als ein Workflow, also ist ein Workflow eine Facette des Projektmanagements.“ Der Abschnitt **N (Ein Modell)** direkt nach den Quellen ersetzt die frühere Besitzer-Empfehlung (Bibliothek → Programm `fs-workflows`) und schärft (3) und (5) nach. Wo die Teile unten widersprechen, gilt N.

## Neu geprüfte Primärquellen (Lücken aus A1 geschlossen)

| Frage | Befund | Quelle |
|---|---|---|
| SW-DSL Task-Typen | `call`, `do`, `emit`, `for`, `fork`, `listen`, `raise`, `run`, `set`, `switch`, `try`, `wait`. Gemeinsame Felder je Task: `if`, `input`, `output`, `export`, `timeout`, `then`, **`metadata`** („Additional information about the task“). Flusssteuerung `then`: `continue`, `exit`, `end` oder Name eines Tasks im selben Scope | https://raw.githubusercontent.com/serverlessworkflow/specification/main/dsl-reference.md |
| Einzelheiten | `call`: `http`, `openapi`, `grpc`, `asyncapi`, `a2a`, `mcp` + `with`. `switch`: Fälle mit `when` und `then`. `wait`: Dauer (ISO 8601). `listen.to`: `all`/`any`/`one`/`until`, `read`: `data`/`envelope`/`raw`. `emit.event`: CloudEvents-Felder (`id`, `source`, `type`, `time`, `subject`, `data` …). `try` + `catch` (`errors.with`, `as`, `when`, `exceptWhen`, `retry`, `do`). `run`: `container`/`shell`/`script`/`workflow`, `await` (Standard `true`), `return` (`stdout`/`stderr`/`code`/`all`/`none`). `raise.error` | dsl-reference.md |
| Kopf | `document`: Pflicht `dsl`, `namespace`, `name`, `version` (SemVer); optional `title`, `summary`, `tags`, `metadata`. `use`: `authentications`, `catalogs`, `errors`, `extensions`, `functions`, `retries`, `secrets`, `timeouts` | dsl-reference.md |
| Fehlertypen | Basis `https://open-workflow-specification.org/spec/1.0.0/errors/`: `configuration`, `validation`, `expression` (400), `authentication` (401), `authorization` (403), `timeout` (408), `communication`, `runtime` (500) | dsl-reference.md |
| Feste Befehlsliste im Standard | **Kataloge**: `use.catalogs` mit `endpoint`; Aufruf `call: <funktion>:<version>@<katalog>` (Beispiel `call: log:0.5.2@global`), Ablage `functions/<name>/<version>/function.yaml` mit `input`/`output`-Schema und `run`-Teil | https://raw.githubusercontent.com/serverlessworkflow/specification/main/dsl.md |
| Ausdrücke | jq ist Pflicht für konforme Laufzeiten, Syntax `${ }` | dsl.md |
| Konformität | Standard-Task-Typen sind Pflicht, Prüfung über die CTK; **keine Teilmengen-/Profilstufen definiert** | dsl.md |
| Lebenszyklus-Ereignisse | Präfix `org.open-workflow-specification.`; Workflow: started, suspended, resumed, cancelled, faulted, completed …; Task: created, started, suspended, resumed, retried, cancelled, faulted, completed | dsl.md |
| Aktuelle DSL-Version | Beispiele nutzen `dsl: '1.0.3'`; „aktuell“ ist nicht ausdrücklich benannt | dsl.md, sdk-typescript README |
| Diagramm | Kein Diagrammstandard in der Spec. Das offizielle TypeScript-SDK (Apache-2.0) erzeugt einen Graphen (`buildGraph`) und Mermaid (`convertToMermaidCode`) aus der Definition, also Diagramm = Ansicht | https://github.com/serverlessworkflow/sdk-typescript |
| BPMN-DI | Normative XSD/CMOF: `BPMNDI.xsd`, `DI.xsd`, `DC.xsd`; IPR-Modus „RF-RAND“. `di:Shape` trägt `dc:Bounds`, `di:Edge` trägt mind. 2 `waypoint` (`dc:Point`). Kein Lizenzkopf in der XSD | https://www.omg.org/spec/BPMN/2.0.2/About-BPMN, https://www.omg.org/spec/BPMN/20100501/DI.xsd |
| Lizenz SW-Spec | Apache-2.0 (aus A1, LICENSE-Datei) | A1 |
| [nicht belegt] | Ob `function.yaml` ein eigenes `metadata`-Feld hat; Lizenz von `serverless_workflow_core` und `swf-runtime`; ob BPMN-DI ohne OMG-Mitgliedschaft frei nutzbar ist (RF-RAND ist kein OSI-Lizenztext) | – |

**Machbarkeit Teilmenge mit offener Lizenz: ja.** Spec Apache-2.0, `swf-core` 1.0.0-alpha14 Apache-2.0 (A1) zum Lesen/Prüfen. Ehrliche Grenze: Die Spec kennt keine Profile; was wir bauen, ist eine **dokumentierte Teilmenge** („FS-Profil“), keine konforme Laufzeit. Jede FS-Datei ist gültiges SW-YAML, aber nicht jede SW-Datei läuft bei uns. Das ist der Preis für „feste Liste zuerst“ und wird so benannt.

## N. Ein Modell: Workflow ist eine Facette des Projektmanagements (Fassung 2)

Zusätzlich geprüft: RFC 8984 (https://www.rfc-editor.org/rfc/rfc8984.html): Participant `kind` = `individual` | `group` | `location` | `resource` („a non-human resource other than a location, such as a projector“); Rollen `owner`, `attendee`, `optional`, `informational`, `chair`, `contact`; **je Participant** `progress`, `progressUpdated`, `percentComplete` („only allowed for participants of a Task“); Task-`progress` ohne Wert wird aus den Participants abgeleitet (§5.2.5: alle completed → completed, einer failed → failed …); Task hat `estimatedDuration`, `relatedTo`, `participants` und `links` (Link: `href`, `contentType`, `size`, `rel`, `title`; laut IANA-Tabelle §8.2.6 für Task gültig). Code-Stand: `fs-jscalendar` `Participant` hat `name`, `email`, `kind`, `roles`, `participationStatus` … aber **kein** `progress` je Participant (`/srv/FreeSynergy/fs-jscalendar/crates/fs-jscalendar/src/model/participant.rs`); unbekannte und `freesynergy.net:`-Eigenschaften bleiben in `extra` erhalten (`fs-tasks-core/src/model/mod.rs`). `tasks.capnp` v0.0.19: `assign(id, name, email)` kennt nur Personen mit E-Mail; `editIf` (compare-and-set) und `Readiness` sind da; `Boards` ist Platzhalter.

### N1 Ein Modell, mehrere Ansichten

| Begriff | Ist im Projektmanagement | Wo (Besitzer fs-tasks) |
|---|---|---|
| Workflow-Definition | **Projekt-Vorlage** | eigenes Objekt `Template` (neben `Board`), Inhalt = SW-YAML im FS-Profil |
| Lauf | **Projekt** (Instanz der Vorlage, mit Eingaben) | ein Loro-Dokument je Projekt (ADR 0073 §8); Tasks sind Projektionen |
| Schritt | **Task** (JSCalendar) | `title`, `estimatedDuration`, `relatedTo` (RFC 9253), `participants` (Zuständiger), `progress` + berechnete `Readiness` |
| Abhängigkeit | Relation `FINISHTOSTART` / `DEPENDS-ON` (+ `freesynergy.net:gap`) | wie Plan Schritt 1 |
| Gantt, Kanban, Workflow-Graph, Liste | **Facetten/Ansichten** auf dasselbe Projekt | Gantt = `schedule`, Kanban = `Board`, Graph = Whiteboard-Ansicht + Layout-Objekt |

Übersetzung SW-DSL → Tasks beim Anlegen des Projekts: `do`-Folge → Kette `FINISHTOSTART`; `fork` → parallele Tasks ohne Relation untereinander (im Task-Graph natürlich, darf deshalb ins Profil); `call` → Maschinen-Task mit Ausführungs-Eigenschaft; `listen` (Freigabe) → menschlicher Task; `switch`, `for`, `try/catch`, `wait`, `raise` siehe N3. **Rückwärtssprünge mit `then: <früherer Task>` sind im Profil verboten** (ein Task-Graph ist azyklisch; ein Zyklus wäre `Readiness::conflict`); Wiederholung nur über `retry` oder `for`.

### N2 Handelnde sind gleich

Jeder Handelnde (Mensch, LLM-Agent, Maschine, Programm) **nimmt sich einen startklaren Task** (`readiness = ready`, er ist Zuständiger), setzt ihn auf `in-process`, arbeitet, schreibt Ergebnis und `completed`/`failed` zurück. Der Unterschied liegt nur im Zuständigen und in der Art der Ausführung:

| Handelnder | Zuständiger (Participant) | Ausführung |
|---|---|---|
| Mensch | AS2 `Person`, `kind: individual` | tut es, hakt ab |
| LLM-Agent | AS2 `Application` + KI-Marke (ADR 0054) | liest Task + Vorgänger-Ergebnisse, schreibt Urteil/Text als Ergebnis |
| Programm (fs-store, Release-Werkzeug) | AS2 `Application` | führt `freesynergy.net:run` aus |
| Maschine (CI, dnf, systemd) | AS2 `Service` | wird von einem Runner angestoßen und beobachtet |

Ein **Runner** ist nur ein weiterer Handelnder (`Application`): er hört auf den Feed (`TaskChange::Unblocked`, Plan Schritt 1), nimmt startklare Tasks mit Ausführungs-Eigenschaft, die ihm zugewiesen sind, ruft `call: befehl:version@fs` mit den Eingaben, schreibt Ergebnis und Status zurück. Der Nutzer sieht auf dem Kanban live, welcher Agent/welche Maschine woran arbeitet (Spalte aus `progress`, Symbol aus Akteurstyp). **Nehmen ohne Doppelarbeit:** lokal per `editIf` (Revision); über Geräte hinweg (Loro, kein Schiedsrichter) per Anspruch `freesynergy.net:claim {by, until}` und Regel „ein Runner nimmt nur Tasks aus dem Store seines Besitzers“; doppelte Ansprüche nach Merge werden angezeigt (wie Konflikte in ADR 0073 §8), die Idempotenz (N3) verhindert doppelte Wirkung.

### N3 Was das Task-Modell nicht von selbst kann (ehrlich)

| Bedarf | Definition (Vorlage, SW-YAML) | Task / Projekt (Laufzeit) | Bewertung |
|---|---|---|---|
| Datenfluss | `input`/`output`/`export` im FS-Profil, nur Pfade (`${ .vorgaenger.sha }`) | Ergebnis am Task: `freesynergy.net:result` (kleines JSON nach dem `output`-Schema des Befehls, Größengrenze) + JSCalendar `links` für Protokolle/Artefakte (Verweis auf fs-files, nie große Daten im Task). Projekt-Eingaben als Eigenschaft des Projekts | JSCalendar hat dafür nichts; Herstellerfeld nach RFC 8984 §3.3 |
| Bedingung (`switch`) | Fälle mit `when` | **Entscheidungs-Task**; erst wenn er fertig ist, legt der Runner (bzw. die Instanziierung) den gewählten Zweig als neue Tasks an. Nicht gewählte Zweige entstehen nie; Begründung im Ergebnis des Entscheidungs-Tasks (`chosen`, `reason`) | bewusst „verzögert anlegen“ statt „überspringen“: ein übersprungener Task als `cancelled` würde nach der Strategie-Regel die Nachfolger als `dependencyCancelled` blockieren. So bleibt `Readiness` unverändert |
| Schleife (`for`) | `for.in`, Obergrenze Pflicht im Profil | Tasks je Element zur Laufzeit angelegt, mit Herkunft (`freesynergy.net:template` + Index) | kein Zyklus im Graph |
| Wiederholung | `retry` (`limit`, `delay`, `backoff`) | Zähler `freesynergy.net:attempts`, letzter Fehler `freesynergy.net:error` (SW-Fehlertyp-URI). Grenze erreicht → `failed` → Nachfolger `dependencyCancelled` → **Mensch entscheidet** (genau die bestehende Strategie-Regel) | passt ohne Änderung |
| Zeitlimit | `timeout` | Runner erzwingt; `due` bleibt Planungstermin, nicht Ausführungsgrenze | zwei verschiedene Dinge, getrennt halten |
| Warten (`wait`) | Dauer | Task mit `estimatedDuration`, Runner als Zeitgeber | Gantt zeigt ihn als Balken |
| Gegenbefehl / Kompensation | `undo` je Befehl im Katalog | bei Fehler legt der Runner **Gegen-Tasks** in umgekehrter Abhängigkeitsfolge an (sichtbar auf dem Kanban); bei `undo: none` oder Stufe ≥ 4 vorher ein menschlicher Freigabe-Task | SW-DSL und JSCalendar haben keine Kompensation: FS-Erweiterung (Saga) |
| Freigabe | `listen` auf Freigabe | **menschlicher Task** (bzw. LLM-Task fürs Urteil); Freigabe = Abschluss, Ergebnis trägt `approvedRef` (Commit-SHA). Profil-Prüfung beim Anlegen: vor jedem Task ab Stufe 4 / „P“ liegt ein Freigabe-Task eines `Person`-Zuständigen | natürlich im Task-Modell |
| Idempotenz | Befehl deklariert seine Ergebnisprobe („schon erledigt?“) | `freesynergy.net:run.key` = Projekt-Id + Task-Uid; Runner prüft vor der Ausführung | nötig, weil Ansprüche über Geräte doppelt sein können |
| Lebenszyklus-Ereignisse | – | TaskFeed + AS2-Aktivitäten (`Update` mit `attributedTo` = Handelnder) | statt der SW-Ereignisse `org.open-workflow-specification.*` |

### N4 Format und Wahrheit

- **SW-YAML (FS-Profil) bleibt das Format für Vorlagen**: Definition, Import, Export, Signatur. Gespeichert als Text im `Template`-Objekt (AS2-Hülle), nicht als Muster-Tasks, weil `switch`/`retry`/`undo` als Tasks nicht verlustfrei darstellbar sind.
- **Wahrheit des Laufs = das Projekt in fs-tasks**: Loro-Dokument je Projekt (ADR 0073 §3/§8), Task-Objekte und Index sind Projektionen. Bis ADR 0073 angenommen und gebaut ist: die heutigen Store-Objekte (Plan, Abschnitt „Live Kanban“ Punkt e).
- Ehrliche Grenze: Ein Lauf lässt sich **nicht** verlustfrei zurück in YAML wandeln (Laufzeit-Tasks aus `switch`/`for`/Gegen-Tasks). Export eines Laufs = JSCalendar/iCal (Gantt/Liste); Export einer Vorlage = YAML (+ BPMN später).
- Whiteboard-Graph: Knoten tragen `freesynergy.net:template` (Vorlage, Version, Schritt-Pfad), damit die Ansicht Laufzeit-Tasks dem Vorlagen-Knoten zuordnet; Layout bleibt eigenes Objekt (Abschnitt 3).

### N5 Repos: fs-tasks besitzt Plan und Lauf (ersetzt die frühere Empfehlung)

| | Früher: Bibliothek → Programm `fs-workflows` | Jetzt: fs-tasks besitzt Vorlage + Projekt, Runner = eigener Handelnder |
|---|---|---|
| Modell | zwei Zustände (Lauf-Schritt + Haltepunkt-Task), Abbildung nötig | **ein** Modell; Readiness, Zyklen, `schedule`, Board gelten für alles |
| Sichtbarkeit | Lauf nur im Workflow-Programm, Haltepunkte im Kanban | alles live im Kanban/Gantt/Graph |
| ADR 0050 | SW-DSL als eigener Standard mit eigenem Besitzer | SW-YAML ist Import/Export-Format der Vorlage, wie iCal für Tasks; Besitzer je Objektart: `Template`, `Project`, `Task`, `Board` = Projektmanagement → fs-tasks |
| Größe | zusätzliches Repo, zusätzliche Schnittstelle | fs-tasks wächst (Gefahr „Gottprogramm“) → gegensteuern: Runner nicht in fs-tasks-core, eigener Prozess |
| Last | Sekundenschritte außerhalb des Task-Verlaufs | viele kleine Änderungen im vollen Loro-Verlauf (ADR 0073 §7, keine Kürzung): Runner bündelt Statusänderungen, Protokolle nur als `links` |
| Bootstrap | Läufer-Bibliothek ohne Tasks nutzbar | **Problem:** fs-store muss installieren können, ohne dass fs-tasks installiert ist (auch fs-tasks selbst). Lösung: Runner-Kern als Bibliothek, die eine Vorlage **im Speicher** als Projekt ohne Store ausführt (gleiches Modell, gleiche reine Funktionen `readiness`/`schedule`); ist fs-tasks da, wird der Lauf dort angelegt und sichtbar |

**Empfehlung: Nutzerrichtung übernehmen.** fs-tasks besitzt `Template` und `Project` (Lauf). Runner = eigener Prozess und eigener Akteur (`Application`), nach ADR 0063 als Unterbefehl (z. B. `fs-tasks runner`) oder kleines eigenes Programm (offene Frage), mit einem Runner-Kern-Crate, das auch fs-store für den Bootstrap einbindet. Die **Befehle** gehören ihren Besitzern (Install-Befehle: fs-store; Release-Befehle: Release-Werkzeug); der Katalog ist nur die Liste ihrer Beschreibungen, der Runner ruft sie über deren Schnittstelle bzw. Befehlszeile. Voraussetzung dafür: Graph, Readiness und `schedule` bleiben reine Funktionen ohne Store (so im Plan Schritt 1 vorgesehen) und sind ohne den Rest von fs-tasks-core nutzbar.

### N6 Folgen für den Tasks-Agenten JETZT (nur Felder/Schema, kein Runner)

Alles **angehängt** (neue Ordinals ab @17 in `TaskItems`, keine Änderung bestehender), Herstellerfelder mit `freesynergy.net:` in `extra`, damit nichts umgebaut wird:

1. **Zuständiger = Akteur beliebiger Art.** `assign(id, name, email)` reicht nicht (nur Person mit E-Mail). Neu vorsehen: `assignActor(id, actorIri, actorType, name)`; am Participant `freesynergy.net:actor` (IRI), `freesynergy.net:actorType` (`Person` | `Application` | `Service` | `Group` | `Organization`, AS2-Akteurstypen), `freesynergy.net:ai` (bool, ADR 0054). `kind` bleibt JSCalendar-Wert (`individual` für Personen; für Nicht-Menschen offene Frage `resource`). Indexfeld `assignee_actor` und Filter `assignee` + `ready` in `TaskFilter` („was ist für mich startklar“).
2. **Fortschritt je Zuständigem** (RFC 8984: `progress`, `progressUpdated`, `percentComplete` am Participant; Task-Fortschritt daraus abgeleitet nach §5.2.5). Fehlt heute in `fs-jscalendar` `Participant`: Bedarfsmeldung an fs-jscalendar; fs-tasks darf beim Lesen den Task-`progress` nicht ohne Rücksicht auf Participant-Werte setzen.
3. **Ausführungs-Eigenschaft reservieren:** `freesynergy.net:run` = `{ call, with, timeout, retry, risk, preview, key }` als undurchsichtiges JSON; fs-tasks prüft nur die Form, interpretiert nichts, gibt sie verlustfrei weiter (Rundreise-Test JSON und iCal; im iCal-Export als `X-`-Eigenschaft oder im Exportbericht genannt, nie still weg).
4. **Ergebnisfelder reservieren:** `freesynergy.net:result` (JSON, Größengrenze in DESIGN.md), `freesynergy.net:attempts`, `freesynergy.net:error` (Problem-Typ-URI), `freesynergy.net:claim {by, until}`; Artefakte über JSCalendar `links` (Standard, schon im Modell erlaubt).
5. **Herkunft aus Vorlage:** `freesynergy.net:template` = `{ id, version, path, index }`.
6. **Projekt = Lauf:** Zugehörigkeit eines Tasks zu einem Projekt als `Envelope.context` bzw. Indexfeld `project`; Platzhalter-Schnittstellen `Templates` und `Projects` neben `Boards` (ohne Methoden, wie `Boards` heute), Fähigkeits-Ids reserviert: `template.read`, `template.import`, `template.export`, `project.instantiate`.
7. **Readiness unverändert** lassen: der Entwurf vermeidet „übersprungen“ (verzögertes Anlegen, N3); `failed` nach erschöpftem `retry` → `dependencyCancelled` ist gewollt. Die Regel „Clients dulden unbekannte Werte“ steht schon im Schema.
8. **Feed:** `TaskChange::Unblocked` wie geplant bauen; er ist der Auslöser für jeden Runner. Kommentare bleiben Gespräch: Runner-Protokolle sind `links`/`result`, keine Kommentare (ein Runner darf eine Zusammenfassung kommentieren, Autor = seine Akteurs-IRI, das Modell erlaubt es schon).
9. **Board:** Standardspalte aus `progress` gilt auch für Maschinen-Tasks; Filter/Symbol nach `actorType` vorsehen.

Unberührt: die Release-Kette als ein Befehl (Stufe 0) bleibt, wie in (4) beschrieben; sie wird später die erste Vorlage (`release.sw.yaml`).

## (1) Format: Empfehlung

**Quelle: Serverless Workflow DSL 1.0.x als YAML, eingeschränkt auf ein FS-Profil. Diagramm ist Ansicht.** Kein Eigenbau, kein BPMN als Quelle.

Begründung:
- Offener Standard mit Apache-2.0-Spec, YAML, menschenlesbar, diffbar, in git signierbar (A1).
- Der **Katalog-Mechanismus** ist genau die gewünschte „feste Liste standardisierter Befehle“: Befehle sind Katalogfunktionen mit Ein-/Ausgabe-Schema, Workflows dürfen nur sie aufrufen.
- `listen` deckt Haltepunkte ab (Freigabe = Ereignis), `try/catch/retry` die Fehlerpfade, `switch` die Formatwahl (tar.gz vs. native), `emit` die Meldungen. `call: a2a/mcp` ist der spätere Weg für KI-Schritte.
- Vorbilder bestätigen YAML-Quelle + Diagramm-Ansicht (Kestra, Argo, Windmill, GitHub Actions; A2); keines nutzt das Diagramm als alleinige Quelle.
- BPMN als Quelle abgelehnt: XML-schwer, sehr großer Umfang, Lizenz RF-RAND statt offener Lizenz, kein KI-Typ, Rust-Crates unreif (`ebi_bpmn` ohne Sub-Prozesse, `bpmn-engine` 0.1.0). BPMN 2.0 + DI bleibt **Export** (ADR 0046: Speichern ≠ Export).
- Eigenbau abgelehnt (Vision: Standards zuerst, kein Kopieren; ADR 0014).

**FS-Profil, Stufe 0** (alles andere wird von der Prüfung abgelehnt, Specification-Muster):
- erlaubt: `do`, `call` **nur** `<befehl>:<version>@fs` (unser Katalog), `switch`, `try`/`catch`/`retry`, `wait`, `listen` (nur Freigabe- und CI-Ereignisse), `emit`, `raise`, `set` (nur Konstanten).
- Fassung 2: `fork` ist erlaubt (parallele Tasks), `for` mit Pflicht-Obergrenze erlaubt (Tasks zur Laufzeit), `then`-Rückwärtssprünge verboten (N1).
- nicht in Stufe 0 (Fassung 1): `fork`, `for`, `run.*` (kein freies Shell im Workflow; Shell lebt nur **in** einem Katalogbefehl), `call http/openapi/grpc/asyncapi/a2a/mcp`, jq-Ausdrücke außer reinen Pfaden `${ .eingabe.repo }` (keine Logik in Ausdrücken, kein Injektionsweg).

**Abbildung unserer Begriffe** (Schlüssel mit Herstellerpräfix wie RFC 8984 §3.3 und `freesynergy.net:gap` im Tasks-Plan):

| Begriff | Wo | Form |
|---|---|---|
| Befehl | Katalogfunktion `fs`: `functions/<name>/<version>/function.yaml` | Name, SemVer, `input`/`output`-Schema, `run` (ruft unsere Rust-Implementierung) |
| Handelnder | `metadata."freesynergy.net:actor"` an der Funktion (Standard) und am Task (Überschreiben) | `human` \| `llm` \| `machine` \| `program` |
| Risikostufe | `metadata."freesynergy.net:risk"` | 1 ansehen … 5 systemweit (siehe 5) |
| Klartext-Vorschau | `metadata."freesynergy.net:preview"` | Satz mit Platzhaltern, z. B. „Tag {{tag}} wird auf {{repo}} gesetzt.“ |
| Gegenbefehl | `metadata."freesynergy.net:undo"` | Name eines Katalogbefehls oder `none` (dann Pflicht-Freigabe) |
| Spiegel (Paketbau) | `metadata."freesynergy.net:mirror"` | Name des Bau-Befehls oder `none` |
| darf scheitern | `metadata."freesynergy.net:may-fail"` + Meldung | gegen stille `let _ =` (C-Lücke 2) |
| Vorbedingungen | `metadata."freesynergy.net:requires"` | Namen von Prädikaten (C-Lücke 5), im Befehl geprüft, nicht im Aufrufer |
| Haltepunkt | Task `listen` auf Ereignis `net.freesynergy.approval` | Freigabe gebunden an Lauf-Id + Commit-SHA |

Falls `function.yaml` kein `metadata` trägt [nicht belegt], steht derselbe Block im Katalogeintrag daneben (`function.fs.toml`); das ist vor dem Bau am Schema zu prüfen.

Crates: `swf-core` (gepinnt) hinter eigener Schnittstelle `WorkflowSource` (Adapter), eigener kleiner Läufer statt `swf-runtime` (Reife unbelegt). Diagramm-Ausgabe zuerst als Mermaid/SVG (wie das offizielle SDK), später Whiteboard.

## (2) Wem gehört das Thema (Fassung 1, überholt durch N5)

Unterscheidung: **Workflow** = Vorlage von Schritten mit Abhängigkeiten (Dokument nach SW-DSL). **Lauf** = Ausführung mit Zustand je Schritt. **Task** = JSCalendar-Aufgabe mit Readiness (fs-tasks, v0.0.19 `readiness`/`blockedBy`/`dependents`).

| Variante | Inhalt | Vorteile | Nachteile |
|---|---|---|---|
| A: alles in fs-tasks | Workflow = Projektvorlage, Lauf = Tasks mit Readiness | Readiness, Zyklusprüfung, Kanban/Gantt schon geplant; keine neue Repo | verletzt ADR 0050 (SW-DSL ist ein eigener Standard, JSCalendar ein anderer); Sekunden-Schritte (push, wait-ci) als JSCalendar-Tasks sind schwer und fluten das Board; `switch`/`try`/`retry` passen nicht in RFC-9253-Relationen |
| B: eigenes Programm `fs-workflows` (Name offen) | besitzt Workflow-Dokumente, Katalog, Läufe, Lauf-Protokoll; Mensch-/LLM-Haltepunkte werden über die Tasks-Schnittstelle zu echten Tasks | ADR 0050 „ein Standard, ein Programm, eine Schnittstelle“ wörtlich erfüllt; fs-tasks bleibt schlank; Install (fs-store) und Release nutzen denselben Läufer | neues Repo, neue Schnittstelle, mehr Pflege |
| C: Bibliothek `fs-workflow` (nur Typen + Läufer), kein Programm | wie `fs-jscalendar` (ADR 0050, Opus-Entscheid): Typen ohne Daten; fs-store und Release-Werkzeug binden sie ein | klein, kein Dienst; gut für Stufe 0/1 | keine Wahrheit für gespeicherte Workflows/Läufe; Whiteboard braucht später doch einen Besitzer |
| D: nur Skripte in fs-release | Release-Kette als Skript, kein Format | sofort nutzbar | kein Standard, keine Ansicht, Install bleibt getrennt |

**Empfehlung: C jetzt, B als Ziel.** Zuerst die reine Bibliothek (Typen des FS-Profils, Profil-Prüfung, Läufer, Katalog-Trait); sobald Workflows gespeichert, geteilt und auf dem Whiteboard bearbeitet werden, wird daraus das Programm `fs-workflows` als Besitzer (Workflow-Dokument + Lauf-Protokoll als AS2-Aktivitäten, Lebenszyklus-Ereignisse der Spec auf AS2 abgebildet). **fs-tasks bleibt Besitzer von `Task`**: Ein Haltepunkt (Opus-Urteil, Nutzertest) wird als Task über `TaskItems` angelegt, mit `depends-on` auf den vorigen Haltepunkt; seine `Readiness` (`ready`/`blocked`/`dependencyCancelled`) zeigt im Kanban, wer gerade dran ist. Maschinenschritte werden keine Tasks. Keine zweite Readiness: der Lauf hat eigene Schrittzustände (Lebenszyklus der Spec), die Tasks-Readiness gilt nur für die Haltepunkt-Tasks.

## (3) Darstellung auf fs-whiteboard

- **Quelle vs. Ansicht:** Quelle ist das YAML (signiert, in git bzw. im Store des Besitzers). Das Board ist eine **erzeugte Ansicht**: Task → Knoten (Form je Typ: Rechteck = `call`, Raute = `switch`, Sanduhr/Person = `listen`, Blitz = `raise`), Folge/`then` → Verbinder, `catch` → gestrichelter Fehler-Verbinder, Farbe = Risikostufe, Symbol = Handelnder.
- **Lage:** Positionen liegen getrennt vom YAML in einem Layout-Objekt, Schlüssel = Task-Pfad (`/do/3/tag`), Werte wie BPMN-DI (`Bounds` x/y/b/h je Knoten, `waypoint`-Liste je Kante). Ohne Layout ordnet die Ansicht automatisch (Strategy: Verbindungsführung, whiteboard design.md). So bleibt das YAML layoutfrei und diffbar, und ein späterer BPMN-Export bekommt DI geschenkt.
- **Bearbeiten im Diagramm:** jede Aktion (Knoten aus der Befehlspalette ziehen, Linie ziehen, Fehlerpfad anhängen) ist ein Command mit `apply`/`invert` auf dem **Workflow-Baum**, nicht auf Zeichnungen. Die Palette enthält **nur Katalogbefehle**. Nach jeder Änderung prüft die Profil-Prüfung; Ungültiges wird markiert, nicht still verworfen. Ergebnis ist ein **unsignierter Entwurf**; lauffähig erst nach Prüfung und Signatur (6).
- **Echtzeit (ADR 0073):** ein `LoroDoc` je Workflow-Entwurf: `LoroTree` der Tasks (verschiebbar, Task-Pfad/Id als Metadatum, nie die CRDT-Id), Layout als Map, Anwesenheit über `EphemeralStore`. Nach jedem Merge deterministische Prüfung (Profil, Sprungziele von `then`, Schleifen durch `then`-Sprünge) und Konfliktanzeige wie `Readiness::Conflict`. Export zu YAML ist die Projektion, die signiert wird.
- **Läufe live:** Schrittzustände färben die Knoten (Feed), werden aber nicht im Board gespeichert.
- Zeitpunkt: erst wenn fs-whiteboard Kern + ADR 0073 stehen. Bis dahin Mermaid/SVG aus dem YAML.

## (4) Erste Umsetzung: Release-Kette als EIN Befehl

Aufruf durch Agenten: `fs-flow run release --repo <r> --branch <b> --version <v>` (Name offen; Stufe 0 siehe unten). Ausgabe immer ≤ 3 Zeilen: `DONE …` | `HALT <grund> <was-wird-gebraucht>` | `RED <schritt> <erste Fehlerzeile>`. Exit 0 / 10 / 1. Wiederaufruf mit `--resume <lauf-id>` setzt nach dem Haltepunkt fort; jeder Befehl ist idempotent (prüft erst, ob sein Ergebnis schon da ist).

Schrittliste (B W1, Schritte 4–16):

| # | Befehl | Handelnder | Halt / Fehlerpfad |
|---|---|---|---|
| 1 | `gates` | program | rot → RED, P korrigiert |
| 2 | `typing-test` (nur UI-Repos, `switch`) | machine | rot → RED |
| 3 | **HALT `review`** | llm (Opus) | wartet auf Freigabe-Ereignis `approve` (JA, gebunden an Kopf-SHA). NEIN → RED mit Befundpfad; neuer Kopf macht JA ungültig |
| 4 | `push` | program | abgelehnt → RED |
| 5 | `wait-ci` | machine | rot → RED; Runner-DNS/apt → `retry` 1× (`rerun`); Queue-Stau → `wait` mit Obergrenze, dann HALT `ci-queue` |
| 6 | `merge-ff` | program | kein ff möglich → RED „rebase nötig“ (neue CI, neues JA) |
| 7 | `tag` | program | Vorbedingung: CI grün auf exakt diesem SHA und JA liegt vor |
| 8 | `release` (Draft abwarten, dann Pre-release schalten) | machine + program | Artefakt-Lauf rot → `retry` 1×, dann RED |
| 9 | `bump` | machine | fehlt packages.toml-Eintrag → RED mit Hinweis |
| 10 | `sign` (Signatur-Lauf abwarten) | machine | rot → RED |
| 11 | `check` (`fs-store check`) | program | rot → RED (zurück zu 9/10) |
| 12 | **HALT `user-test`** | human | Task in fs-tasks (später); Befund → neuer Auftrag |
| 13 | `report` | program | schreibt ≤10 Zeilen an K/S |

**Skript vs. Workflow-Lauf:** Stufe 0 (jetzt, Entwicklerwerkzeug, kein Produkt): die Befehle als kleine Unterbefehle **eines** Rust-Programms (ADR 0063: kein Shell als Weiche; vorhandene `gates.sh`/`lib.sh` werden aufgerufen, nicht ersetzt) plus die Datei `release.sw.yaml` im FS-Profil; ein Test prüft, dass der feste Ablauf im Programm und das YAML übereinstimmen. Stufe 1: der Läufer liest das YAML (via `swf-core`) und ruft die Katalogbefehle; der fest verdrahtete Ablauf entfällt. So spart Stufe 0 sofort Tokens (heute 8–12 Agentenrunden je Release → 1–3 Aufrufe), ohne auf den Läufer zu warten.

**Mini-Spezifikation der ersten Befehlsliste (Katalog `fs`, Version 0.1.0)**

Gemeinsam: Eingabe `repo`, `lauf-id`; jede Ausführung schreibt einen Eintrag ins Lauf-Protokoll (Befehl, Eingaben, SHA, Ergebnis, Dauer); Fehler als SW-Fehlertypen (`validation`, `timeout`, `communication`, `runtime`, `authorization`).

| Befehl | Eingabe → Ausgabe | Vorbedingung | Stufe* | Klartext-Vorschau | Gegenbefehl | Idempotenz |
|---|---|---|---|---|---|---|
| `gates` | Worktree → ok/rot + erste Fehlerzeile + Log-Pfad | sauberer Baum | 3 | „Die lokalen Prüfungen laufen in {{wt}}.“ | – | gleicher SHA grün → überspringen |
| `approve` (Ereignis, kein Befehl) | `{lauf, sha, urteil, wer}` | Absender ist Opus bzw. Mensch | – | „Freigabe von {{wer}} für {{sha}}.“ | Widerruf | – |
| `push` | Branch → Remote-SHA | JA zu diesem SHA; Push-Phase erlaubt | P | „{{branch}} wird nach {{remote}} geschoben.“ | `none` (öffentlich) | Remote = lokal → ok |
| `wait-ci` | SHA → grün/rot je Pflicht-Job | Push erfolgt | 1 | „Auf die CI für {{sha}} wird gewartet (höchstens {{t}}).“ | – | Ergebnis vorhanden → sofort |
| `merge-ff` | Branch → main-SHA | ff möglich, CI grün auf genau diesem SHA | P | „main wird ohne Merge-Commit auf {{sha}} vorgerückt.“ | `none` | main = SHA → ok |
| `tag` | main-SHA → `v{{version}}` | grün + JA; Tag frei | P | „Tag v{{version}} wird auf {{sha}} gesetzt und geschoben.“ | `none` nach Push (Tags sind unveränderlich zu behandeln) | Tag auf gleichem SHA → ok; auf anderem → RED |
| `release` | Tag → Release-URL, Status Pre-release | release.yml grün | P | „Das Release v{{version}} wird als Vorabversion veröffentlicht.“ | zurück auf Draft | Status stimmt → ok |
| `bump` | Version → Katalog-Commit | Release veröffentlicht | P | „Der Katalog bekommt {{repo}} v{{version}}.“ | `bump` auf alte Version | Eintrag vorhanden → ok |
| `sign` | Katalog-Commit → signierte Datei | bump erfolgt | P | „Der Katalog wird signiert.“ | – | Signatur zu Commit vorhanden → ok |
| `check` | Katalog → ok/rot (Signatur, Hash, Fähigkeiten) | sign erfolgt | 1 | „Der Katalog wird wie ein Nutzer ihn sieht geprüft.“ | – | rein lesend |
| `report` | Lauf-Protokoll → ≤10 Zeilen | – | 1 | „Der Bericht wird geschrieben.“ | – | – |

\* „P“ = veröffentlichen; passt nicht in die Maschinen-Skala (offene Frage 3).

## (5) C-install, Umkehrung, Risikostufen, Vorschau

- **Ein Katalog für beides.** Die Befehle aus C (`quelle.lesen` … `register.facetten`, Entfernen R1–R6) werden Katalogbefehle mit denselben Metadaten. Installieren = ein Workflow mit `switch` auf das Format (C-Lücke 6: tar.gz vs. native ist eine Verzweigung). Sammelschritte (Lücke 7) sind **ein Befehl mit Listen-Eingabe** (`paket.installieren` nimmt alle rpm, ein pkexec), kein `for`.
- **Rückgängig:** Die Spec hat keine Kompensation (A1). Der Läufer führt bei Fehler die `undo`-Befehle der gelungenen Schritte in umgekehrter Folge aus (Saga-Muster, als FS-Erweiterung dokumentiert). `undo: none` (10n, R3) verlangt vorher eine Freigabe des Menschen.
- **Paketbau = rückwärts:** Der Bau-Workflow wird aus dem Install-Workflow abgeleitet: Reihenfolge umkehren, je Schritt `mirror` einsetzen, Schritte mit `mirror: none` fallen weg (C §4); Bau-only-Schritte (`paket.beschreiben`, Fähigkeiten ableiten, Upstream-Signatur) kommen dazu. Das Ergebnis wird als Entwurf erzeugt und geprüft, nicht blind generiert. Voraussetzung: das Manifest als Quelle der Wahrheit (C §4 letzter Absatz).
- **Risikostufen 1 ansehen < 2 öffnen < 3 starten < 4 installieren < 5 systemweit:** je Befehl fest im Katalog; die Stufe eines Laufs = Maximum seiner Schritte. Ehrlich setzen: `quelle.lesen` schreibt `serials.toml` (Lücke 4) → Stufe 2, nicht 1.
- **Klartext-Vorschau:** Vor dem Lauf erzeugt der Läufer aus den `preview`-Sätzen aller Schritte des **gewählten Pfads** eine Liste, sortiert nach Ablauf, Schritte ab Stufe 4 hervorgehoben, Schritte ohne Gegenbefehl markiert. Eine Bestätigung je Lauf, nicht je Schritt; ab Stufe 5 steht die Vorschau **vor** dem pkexec-Passwort (Lücke 11).
- **Weitere C-Lücken, die das Format schließt:** 1 (CLI und Fenster laufen denselben Workflow, Abweichung verschwindet), 2 (`may-fail` + Meldung), 5 (Prädikate als `requires`), 8 (Umgebung und Grenzen als deklarierte Eingaben), 9 (`requires` aus ADR 0068 als Vorbedingung), 12 („Daten des Menschen nie entfernen“ als Invariante an jedem Entfernen-Befehl, Profil-Prüfung erzwingt den Eintrag).

## (6) Sicherheit

- **Workflows und Katalog sind Code:** in git, Review wie Code, Katalog signiert wie der Store-Katalog (gleiche Schlüsselkette, eigener Unterschlüssel); der Läufer lehnt unsignierte Workflows, unbekannte Befehle und Befehlsversionen außerhalb des Katalogs ab.
- **Kein freies Shell im Workflow**, keine Ausdrücke mit Logik (nur Pfade): keine Einschleusung über Eingaben. Geheimnisse nur per Namen (`use.secrets`), nie im YAML oder Protokoll.
- **Wer darf auslösen:** Rechte je Workflow und je höchster Stufe (Gruppen ADR 0055, Identität über Kanidm-Wrapper ADR 0047). Release: Koordinator und Programm-Agenten dürfen `run release` aufrufen; Haltepunkte kann der Aufrufer nicht selbst freigeben (Vier-Augen: Opus-JA kommt von Opus, Nutzertest vom Nutzer).
- **KI-Schritte nur mit Freigabe:** `actor: llm` darf urteilen (Review, Text) aber keinen Befehl ab Stufe 4 bzw. „P“ auslösen, ohne dass eine Freigabe von Mensch oder Strategie vorliegt. Freigaben sind signierte, an Lauf + SHA gebundene AS2-Aktivitäten (ADR 0054: KI als markierter Teilnehmer). Ein neuer SHA entwertet jede Freigabe.
- **Protokoll:** jeder Lauf mit Eingaben, SHAs, Freigaben, Ergebnissen; nachvollziehbar und nicht still kürzbar.

## (7) Was sich vor dem Meilenstein NICHT ändert

- fs-store: Installations- und Entfernen-Code bleibt, wie er ist; C-Lücken 1 und 2 nur als Befund/Ticket.
- fs-tasks: Plan Schritt 1/2 läuft unverändert; keine Workflow-Felder in `Task`, keine neue Readiness.
- fs-interfaces: kein Thema `workflows`, keine Schema-Änderung.
- fs-whiteboard: nichts; Darstellung erst nach Kern und ADR 0073.
- Kein neues Repo/Programm, kein ADR vor Nutzerentscheid. GitHub-Actions-Dateien (`release.yml`, `check.yml`, `sign.yml`) bleiben, `gates.sh` bleibt und wird aufgerufen.
- Einzig denkbar vorher (nur nach Freigabe): Stufe 0 der Release-Kette als Entwicklerwerkzeug, das bestehende Abläufe nur zusammenfasst.

## (8) Offene Fragen an den Nutzer

---
1. Format: Serverless Workflow DSL (Apache-2.0) als Quelle mit eigener Teilmenge „FS-Profil“, Diagramm nur als Ansicht, BPMN nur als Export. Einverstanden?
2. (Fassung 2) Besitzer fs-tasks (Vorlage = Projekt-Vorlage, Lauf = Projekt), Runner als eigener Handelnder: als Unterbefehl `fs-tasks runner` oder als kleines eigenes Programm?
2a. Bootstrap: Darf fs-store den Runner-Kern einbinden und eine Installation ohne fs-tasks im Speicher ausführen (sichtbar erst, wenn fs-tasks da ist)?
2b. Nicht-menschliche Zuständige: JSCalendar `kind: resource` („wie ein Beamer“) verwenden oder nur unser Feld `freesynergy.net:actorType`?
3. Risikostufen: Die Skala (ansehen … systemweit) gilt für den eigenen Rechner. Veröffentlichen (push, Tag, Release, Katalog) trifft alle Nutzer. Eigene Stufe 6 „veröffentlichen“ oder eine zweite Achse „Reichweite“?
4. Release-Kette Stufe 0 vor dem Meilenstein als Entwicklerwerkzeug bauen (spart sofort Tokens), oder erst danach?
5. Opus-JA: darf die Kette danach selbst weiterlaufen bis Tag/Release, oder bleibt vor `tag` immer ein Halt für Strategie?
6. Signatur der Workflows: gleicher Projektschlüssel (Unterschlüssel) wie der Katalog, oder eigener Schlüssel?
