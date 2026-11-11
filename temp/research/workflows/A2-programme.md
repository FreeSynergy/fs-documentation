# A2: Workflow-Programme im Vergleich

Stand: 2026-11-12. Nur Lesezugriff auf Primärquellen (GitHub-LICENSE-Dateien, offizielle Doku). Nichts installiert. `[nicht belegt]` = in den abgerufenen Seiten nicht gefunden oder Seite nicht abrufbar (404).

## Vergleichstabelle

| Programm | Lizenz (Primärquelle) | OSI? | Definitionsformat | Kanten/Verbindungen | Daten zwischen Schritten | Bedingungen / Wiederholung | Fehlerpfade | Human-in-the-loop | KI/LLM-Schritte | Diagramm = Quellformat? | Sprache/Laufzeit |
|---|---|---|---|---|---|---|---|---|---|---|---|
| n8n | Sustainable Use License 1.0 (LICENSE.md, Ausnahme `.ee`) | Nein. Interne/nicht-kommerzielle Nutzung | JSON-Export: [nicht belegt] | Canvas-Verbindungen, interne Form [nicht belegt] | [nicht belegt] | [nicht belegt] | [nicht belegt] | [nicht belegt] | Doku verlinkt "Integrate AI", Details [nicht belegt] | [nicht belegt] | TypeScript (Topic-Tag, nicht als Sprachstatistik belegt) |
| Node-RED | Apache-2.0 (LICENSE, Version 2.0 belegt) | Ja | Flow-Format-Seite nicht abrufbar (404); Editor-Seite: Flow = Tab, Format [nicht belegt] | Wires: nur Verweis, Mechanik [nicht belegt] | [nicht belegt] | [nicht belegt] | Catch-Node erwähnt nicht belegt | [nicht belegt] | [nicht belegt] | [nicht belegt] | JavaScript/Node.js (aus Lizenzkontext nicht belegt; Laufzeit nur als Vermutung) |
| Kestra | Apache-2.0 (LICENSE belegt) | Ja | YAML: `id`, `namespace`, `tasks` belegt | Sequenziell, parallel, bedingt belegt; Abhängigkeitssyntax [nicht belegt] | Task-Outputs via `{{ outputs.<task>.values... }}` belegt | Retries als Policy belegt | `errors`- und `finally`-Tasks belegt | [nicht belegt] | [nicht belegt] | No-Code-Editor vorhanden; Quelle YAML oder Editor [nicht belegt] | [nicht belegt] (Laufzeit nicht geprüft) |
| Windmill | AGPLv3 (LICENSE belegt; teils Apache-2.0, proprietäre EE-Teile) | Ja (AGPLv3), aber Mischlizenz | OpenFlow-Format (OpenAPI-Spec `openflow.openapi.yaml` im Repo belegt); Speicherung als JSON-Serialisierung belegt, YAML-Definition belegt | DAG, belegt | Über Step-Inputs; Syntax [nicht belegt] | Branches, Schleifen (for/while), Retries belegt | Error-Handler-Skript belegt | Approval-Schritt `waitForApproval` belegt; Suspend-Details teils | AI-Agent-Schritte in Flows belegt; Detail [nicht belegt] | YAML oder Visual Editor; Quelle nicht eindeutig belegt | Backend Rust, Frontend Svelte 5 (belegt) |
| Temporal | MIT (LICENSE belegt) | Ja | Kein Format: Workflows als Code (Go, Java, TypeScript, Python belegt) | Im Code [nicht belegt als Diagramm] | Im Code | Timer/Signale in Event History belegt; Retry-Mechanik [nicht belegt] | [nicht belegt] | Signale belegt; Approval als Anwendungsfall [nicht belegt] | [nicht belegt] | Nein, Code ist die Definition | Server-Sprache [nicht belegt] |
| Argo Workflows | Apache-2.0 (LICENSE belegt) | Ja | Kubernetes-CRD `Workflow` in YAML belegt | DAG über `dependencies` belegt; Steps als Listenliste belegt | Outputs via `{{tasks.<n>.outputs.result}}` / `{{steps...}}` belegt; Parameter/Artefakte explizit [nicht belegt] | `when:` für Steps belegt; Retry [nicht belegt] | Exit-Handler [nicht belegt] | `suspend` (Pause bis manuelle Fortsetzung) belegt | [nicht belegt] | Nein (YAML); visueller Graph als Quelle [nicht belegt] | Laufzeit Kubernetes; Sprache [nicht belegt] |
| GitHub Actions | GitHub-Plattform, kein OSS-Lizenzfall geprüft | [nicht belegt] (Plattform, nicht Lizenz der Syntax) | YAML in `.github/workflows` belegt | `jobs.<id>.needs` belegt; Parallel-Default belegt | `jobs.<id>.outputs` belegt; `steps.<id>.outputs` [nicht belegt] | `if:` belegt; Matrix [nicht belegt] | `continue-on-error` [nicht belegt] | Environments mit Reviewern [nicht belegt] (nur Input-Typ belegt) | [nicht belegt] | Nein (YAML) | Plattform-intern [nicht belegt] |
| Activepieces | MIT (Kern) + separate Lizenz für `ee`-Verzeichnisse (Inhalt nicht abgerufen) | Ja (Kern) | JSON-Flows [nicht belegt] | DAG-Schritte belegt (Form [nicht belegt]) | [nicht belegt] | [nicht belegt] | [nicht belegt] | Human-in-the-loop mit "require approval" belegt | Native AI-Pieces belegt | No-Code-Builder vorhanden; Quelle [nicht belegt] | TypeScript (Pieces belegt); Laufzeit [nicht belegt] |

## Fazit

- **Lizenz für Weiterverwendung:** Apache-2.0 (Node-RED, Kestra, Argo) und MIT (Temporal, Activepieces-Kern) sind unproblematisch als Vorbild und für Code-Übernahme mit Namensnennung. n8n (Sustainable Use) nur als Muster, kein Code. Windmill (AGPLv3) nur mit Vorsicht, da Copyleft.
- **Format-Vorbild:** Am klarsten dokumentiert sind Kestra (YAML mit `id`/`namespace`/`tasks`, Outputs per Template), Argo (YAML mit DAG und `when`, `suspend`) und Windmill (OpenFlow als OpenAPI-Spec). GitHub Actions ist das bekannteste YAML-Muster mit `needs` und `if`.
- **Grafik als Quelle:** Keines der geprüften Programme hat belegt ein Diagramm als alleiniges Quellformat. Windmill und Kestra erlauben YAML und Editor; Temporal und Argo nutzen kein Diagrammformat. Ein Whiteboard-Format als Quelle ist damit nicht durch Vorbilder gedeckt; eher YAML/JSON als Quelle und Diagramm als Ansicht.
- **Human-in-the-loop:** Belegt bei Argo (`suspend`), Windmill (`waitForApproval`), Temporal (Signale), Activepieces (Approval-Piece). Kestra und GitHub Actions nicht belegt.
- **KI-Schritte:** Belegt nur bei Windmill und Activepieces (ohne Details zum Format).
- **Offene Lücken:** Node-RED-Flow-Format und n8n-JSON-Format nicht abrufbar; Activepieces-Flow-JSON nicht belegt. Für eine saubere Format-Entscheidung müssten die Format-Spezifikationen direkt im Repo gelesen werden (z. B. Windmill `openflow.openapi.yaml`, Node-RED `flows.json` im Quellcode), was einen Clone erfordert und hier nicht gemacht wurde.

## Quellen

- n8n LICENSE: https://github.com/n8n-io/n8n/blob/master/LICENSE.md
- Node-RED LICENSE: https://github.com/node-red/node-red/blob/master/LICENSE
- Node-RED Flow-Editor-Doku: https://nodered.org/docs/user-guide/editor/workspace/flows (Flow-Format-Seite nicht abrufbar)
- n8n Workflow-Doku: https://docs.n8n.io/workflows/ und https://docs.n8n.io/workflows/components/
- Kestra LICENSE: https://github.com/kestra-io/kestra/blob/develop/LICENSE
- Kestra Flow-Doku: https://kestra.io/docs/workflow-components/flow
- Windmill LICENSE: https://github.com/windmill-labs/windmill/blob/main/LICENSE
- Windmill Flows-Doku: https://www.windmill.dev/docs/flows/flow_editor
- Windmill Repo: https://github.com/windmill-labs/windmill
- Temporal LICENSE: https://github.com/temporalio/temporal/blob/main/LICENSE
- Temporal Workflow-Doku: https://docs.temporal.io/workflows
- Argo LICENSE: https://github.com/argoproj/argo-workflows/blob/main/LICENSE
- Argo Workflow-Concepts: https://argo-workflows.readthedocs.io/en/latest/workflow-concepts/
- GitHub Actions Syntax: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- Activepieces LICENSE: https://github.com/activepieces/activepieces/blob/main/LICENSE
- Activepieces Repo: https://github.com/activepieces/activepieces
- Activepieces Flows-Doku: https://www.activepieces.com/docs/build-automations/flows/overview
