# ENTWURF: Workflow-Standard für FreeSynergy (Opus, 2026-11-12)

Status: Entwurf, kein ADR, kein Code. Grundlage: `A1-standards.md`, `A2-programme.md`, `B-arbeitsweise.md`, `C-install.md` (alle in `/srv/FreeSynergy/.scratch/workflows/`), ADR 0050 (origin/main), ADR 0063 (origin/main), ADR 0073 (Entwurf, Branch `adr-kollaboration`), Tasks-Plan `/srv/FreeSynergy/.wt-tasks-q0/todo/plan-comments-and-dependency-evaluation.md`, `fs-interfaces` v0.0.19 (`/srv/FreeSynergy/.wt-interfaces-19/schema/tasks.capnp`, `enum Readiness`).

Nutzerentscheid (gesetzt): Installieren ist eine Anweisung (ein Workflow), Paket schnüren ist derselbe Workflow rückwärts. Workflows werden standardisiert UND gezeigt (Knoten und Linien wie auf einem Whiteboard). Handelnde: Mensch, LLM, Maschine, Programm. Zuerst nur eine feste Liste standardisierter Befehle. Was immer gleich abläuft, wird Standard und spart Tokens.

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
- nicht in Stufe 0: `fork`, `for`, `run.*` (kein freies Shell im Workflow; Shell lebt nur **in** einem Katalogbefehl), `call http/openapi/grpc/asyncapi/a2a/mcp`, jq-Ausdrücke außer reinen Pfaden `${ .eingabe.repo }` (keine Logik in Ausdrücken, kein Injektionsweg).

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

## (2) Wem gehört das Thema

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
2. Besitzer: erst Bibliothek, später eigenes Programm (Arbeitsname `fs-workflows`); fs-tasks bekommt nur die Haltepunkte als Aufgaben. Einverstanden, und welcher Name?
3. Risikostufen: Die Skala (ansehen … systemweit) gilt für den eigenen Rechner. Veröffentlichen (push, Tag, Release, Katalog) trifft alle Nutzer. Eigene Stufe 6 „veröffentlichen“ oder eine zweite Achse „Reichweite“?
4. Release-Kette Stufe 0 vor dem Meilenstein als Entwicklerwerkzeug bauen (spart sofort Tokens), oder erst danach?
5. Opus-JA: darf die Kette danach selbst weiterlaufen bis Tag/Release, oder bleibt vor `tag` immer ein Halt für Strategie?
6. Signatur der Workflows: gleicher Projektschlüssel (Unterschlüssel) wie der Katalog, oder eigener Schlüssel?
