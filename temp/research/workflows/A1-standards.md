# A1 - Offene Standards und Muster fuer Workflows

Stand: 2026-11-12. Nur Lesen, keine Installation. Quellen per WebFetch/WebSearch. Unbelegtes ist als [nicht belegt] markiert.

## Quellen (Primaer)

- BPMN 2.0: OMG-Seite https://www.omg.org/spec/BPMN/2.0.2/ (formal/13-12-09, Jan. 2014). Die 2.0.1-Seite https://omg.org/spec/BPMN/2.0.1 nennt ISO/IEC 19510 (ISO-Release formal/13-11-03).
- Serverless Workflow DSL: Referenz https://raw.githubusercontent.com/serverlessworkflow/specification/main/dsl-reference.md (Repo-Pfad laut GitHub: open-workflow-specification/specification). Lizenz: LICENSE ist Apache-2.0, Copyright-Halter im Dokument nicht ausgefuellt.
- Ansible: https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html
- cloud-init: https://docs.cloud-init.io/en/latest/reference/modules.html (Seite abgeschnitten, Rest ungelesen)
- Quadlet: https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html

## Vergleichstabelle

| Aspekt | BPMN 2.0 | CNCF Serverless Workflow (DSL) | Ansible Playbook | cloud-init | systemd / Quadlet |
|---|---|---|---|---|---|
| Knoten / Kanten | Tasks, Events, Gateways; Sequence Flow [Abschnittsnr. nicht belegt] | Tasks mit `then`-Verweis; Scope-gebunden | Plays und Tasks, lineare Reihenfolge (oben nach unten) | Module in Stufen; Reihenfolge per Modulliste [nicht belegt] | Unit-Dateien; Kanten via `After=`, `Requires=`, `Wants=`, `Before=` |
| Daten zwischen Schritten | Data Objects [nicht belegt] | `export`/`input` [nicht belegt im Fetch] | `register`/`set_fact` [nicht belegt im Fetch] | nicht belegt | Umgebung/Drop-ins; keine Schritt-Daten |
| Bedingungen | Gateways (exklusiv, parallel, inklusiv, event-based) | `if` auf Task, `when` auf Switch/Catch/Retry | `when` [nicht belegt im Fetch] | `power_state.condition` (Exit-Code 0); Modul-Aktivierung per Schluessel | Suffix-Pruefungen, Typ-Defaults; keine Logik fuer Ablauf |
| Schleifen / Wiederholung | Multi-Instance / Loop [nicht belegt] | `for` (`each`/`in`/`at`), `while`, `do` | `loop`, `until`/`retries` [nicht belegt im Fetch] | keine allgemeine Schleife (nur Listen wie `pull`) | Keine Schleife; Wiederholung durch Template-Instanzen (`foo@.container`) |
| Fehlerpfade | Error-Events, Boundary Events [nicht belegt] | `try`/`catch` mit `errors.with`; `retry` mit `delay`, `limit`, `backoff`, `jitter`; `raise.error` mit Standard-Typen | `block`/`rescue`/`always`, `ignore_errors`, `failed_when` [nicht belegt im Fetch]; Host fliegt aus Rotation | `runcmd`-Fehlerverhalten [nicht belegt]; `power_state.timeout` | `Restart=`, `HealthOnFailure=kill`, `Retry=`/`RetryDelay=` fuer Image-Pull, `TimeoutStartSec` |
| Kompensation | Compensation Events/Handler [nicht belegt] | nicht belegt | nicht belegt | nicht belegt | nicht belegt |
| Menschliche Freigabe | User Task / Manual Task [nicht belegt] | `listen` mit `until`/`one`/`any`; Freigabe-Schritt [nicht belegt als eigener Typ] | `vars_prompt` nicht gefunden | nicht belegt | nicht belegt |
| KI-Schritt | kein Standard-Typ [nicht belegt] | `call` mit `a2a` (KI-Agenten) und `mcp` (MCP-Server); kein eigener LLM-Task | nicht belegt | nicht belegt | nicht belegt |
| Grafische Darstellung | BPMN DI (BPMNDI/DI/DC, XSD vorhanden) | kein Diagrammstandard gefunden [nicht belegt] | nicht belegt | nicht belegt | nicht belegt |
| Standardisierung | OMG-Spec, ISO/IEC 19510 | CNCF Sandbox (seit Juli 2020, laut WebSearch) | Community-Doku, Produkt von Red Hat | Community-Projekt | systemd-Standard, Quadlet im Podman-Projekt |
| Lizenz der Spec | OMG-IPR-Modus "RF-RAND" (Label laut Seite); Volltext-PDF nicht lesbar | Apache-2.0 (LICENSE-Datei) | Doku-Lizenz [nicht belegt]; ansible-core GPLv3 [nicht im Fetch bestaetigt] | GPLv3 [nicht im Fetch bestaetigt] | Quadlet-Lizenz nicht im Fetch |

## Antworten je Standard (Kurzform)

**BPMN 2.0.** Ein Prozess ist ein Graph aus Knoten (Tasks, Events, Gateways) und Kanten (Sequence Flow). Daten laufen ueber Data Objects. Bedingungen stehen an Gateways, Schleifen ueber Multi-Instance. Fehler laufen ueber Error-Events; Kompensation ist ein eigenes Konzept. Menschliche Freigaben sind User Tasks. Ein KI-Schritt hat keinen Standard-Typ [nicht belegt]. Die grafische Darstellung ist Teil des Standards (BPMN DI, XML-Schema vorhanden). Die Section-Nummern und die ISO-Lizenzkosten konnte ich nicht pruefen: das PDF war nicht lesbar und die ISO-Seite lieferte 403.

**CNCF Serverless Workflow DSL.** Die Task-Typen sind call, do, fork, emit, for, listen, raise, run, set, switch, try, wait. `run` deckt container, shell, script, workflow ab. `call` deckt AsyncAPI, gRPC, HTTP, OpenAPI, A2A und MCP ab. Die Flusssteuerung laeuft ueber `then`, `when` und `if`. Schleifen sind `for` mit `while`. Fehler laufen ueber `try`/`catch`/`retry` und `raise.error` mit Standard-Typen. Kompensation und ein Diagrammstandard fehlen im Fetch. Fuer KI gibt es keinen eigenen Task, aber `call` mit A2A oder MCP.

**Ansible.** Ein Playbook ist eine geordnete Liste von Plays; Tasks laufen von oben nach unten, je Task auf allen Hosts, bevor der naechste folgt. Bedingungen, Schleifen, Fehlerbehandlung und Datenuebergabe sind bekannte Keywords, aber im Fetch nicht belegt. Eine Freigabe-Schleife ist nicht vorgesehen [nicht belegt im Fetch].

**cloud-init.** Module laufen in Stufen. Gating laeuft ueber Top-Level-Schluessel und Distro-Filter. `power_state.condition` ist ein Exit-Code-Test. Eine allgemeine Schleife gibt es nicht. Es ist eine Konfigurations-Doku, kein Workflow-Standard.

**systemd / Quadlet.** Quadlet erzeugt aus `.container`, `.pod`, `.kube` usw. Units; Abhaengigkeiten laufen ueber systemd-Keys. Fehlerbehandlung ist Restart-Policy und Health-Check, keine Kompensation. Repetition gibt es nur ueber Template-Instanzen. Es ist ein Deployment-Muster, keine Ablaufbeschreibung.

**Offene KI-Standards (Stand Suche).** Kein ratifizierter Standard fuer Schritt-Workflows mit Freigabe gefunden. Kandidaten: IETF-Draft AAIF (Juni 2026, Ablaufdatum 27.12.2026, nur Agent-Definition, Freigabe als Policy), Snap Agent Format (vendor-led), OSOP (Community, Human-Knoten), MCP 2026-07-28 (`inputRequests`, Form-Elicitation). Nichts davon ist gesichert [nicht belegt als Standard].

## Rust-Bibliotheken (Crates)

| Crate | Zweck | Stand / Lizenz | Bewertung |
|---|---|---|---|
| `serverless_workflow_core` (sdk-rust, CNCF-Projekt) | DSL-Modelle | 1.0.0-alpha6.x; Lizenz [nicht geprueft] | offiziell, aber alpha |
| `swf-core` (ejfkdev/serverlessworkflow-rs) | DSL-Modelle, Serialisierung, Validierung fuer DSL 1.0 | 1.0.0-alpha14 (lt. lib.rs, 12.08.2026); Apache-2.0 | aktuellste gesehene Version; Pre-1.0 |
| `swf-runtime` | Ausfuehrung | alpha13 (lt. docs.rs); Lizenz/Stand nicht geprueft | Laufzeit, Reife unbelegt |
| `ebi_bpmn` | BPMN-Parser, Writer, Executor (State-Space) | bis 0.0.45; Lizenz [nicht geprueft] | eingeschraenkt: nur Start/End/Intermediate-None und Message-Events, keine expanded Sub-Prozesse |
| `bpmn-engine` | BPMN-2.0-Engine (JSON/XML) | 0.1.0, Apache-2.0 | frueh, nur 0.1.0 |
| `travailleur` | Workflow-Spec | Spec 0.8, "unstable" | veraltet |

Downloadzahlen und crates.io-Seiten wurden nicht geprueft.

## Empfehlung: kleine Teilmenge (feste Befehlsliste zuerst)

1. Start mit einer festen, geschlossenen Befehlsliste (kein Graph-Engine, keine Kompensation, keine KI-Schritte).
2. Befehle als Serverless-Workflow-kompatible Tasks benennen: `set`, `call` (HTTP/Shell als `run.shell`), `if`, `for` mit `limit`, `try`/`catch`/`retry`, `wait`, `raise`. Damit bleibt eine spaeter Umstellung auf den Standard moeglich.
3. Menschliche Freigabe als eigener Befehl (z. B. `listen`/Freigabe-Token), nicht als Nebeneffekt.
4. KI-Schritte nicht in der Teilmenge. Spaeter als `call` mit MCP/A2A, sobald ein Standard reift.
5. Diagramm: aus eigenem Modell erzeugen; BPMN-DI erst, wenn BPMN-Export gebraucht wird.
6. Vor Festlegung: BPMN-Section-Nummern und ISO-Lizenz pruefen (PDF/ISO-Zugang fehlte), Crate-Lizenzen auf crates.io bestaetigen.

## Offen / nicht belegt

- BPMN-Abschnittsnummern, Data Objects, Kompensation, Freigabe-Typ im Volltext: nicht gelesen (PDF nicht lesbar).
- ISO/IEC 19510 Lizenzkosten/Status: ISO-Seite 403.
- Ansible: Bedingungen, Schleifen, Fehler, `register`, `vars_prompt`: nicht im Fetch.
- cloud-init: Stufen-Reihenfolge, Fehlerverhalten `runcmd`: Seite abgeschnitten.
- Quadlet/Serverless-Workflow-Lizenz des Dokuments: nicht im Fetch.
- ebi_bpmn und serverless_workflow_core Lizenz: nicht geprueft.
