# Tasks — Anforderungen (Board-Ansicht)

Geschrieben für den früheren Plan `fs-kanban`; jetzt die Board-Ansicht von [`fs-tasks`](design.md). Programmnamen unten folgen diesem Plan.

Was `FreeSynergy.Kanban` (Repository `fs-kanban`) muss und kann, abgeleitet aus den analysierten [Projektmanagement-Frontends](../projectmanagement/frontends/index.md) (ADR 0006, 0013). Jede Fähigkeit nennt ihren Datenstandard (ADR 0014) und unseren Status. Das Programm ist **nur ein Board-Programm**: Boards, Spalten, Karten. Planung (Gantt, Zeiterfassung, Budgets) wird einem späteren `fs-projectmanagement` überlassen. Nur Funktionsanalyse, eigene Formulierung, nichts kopiert.

Status: `implemented` · `planned` · `proposed`

**Gesehen in** — analysierte Frontends: [Tr](../projectmanagement/frontends/trello/index.md) Trello ·
[We](../projectmanagement/frontends/wekan/index.md) Wekan ·
[Pl](../projectmanagement/frontends/planka/index.md) Planka ·
[Ta](../projectmanagement/frontends/taiga/index.md) Taiga ·
[Ji](../projectmanagement/frontends/jira/index.md) Jira ·
[As](../projectmanagement/frontends/asana/index.md) Asana ·
[Op](../projectmanagement/frontends/openproject/index.md) OpenProject ·
[Re](../projectmanagement/frontends/redmine/index.md) Redmine.
*Arch.* = durch unsere Architektur oder Prinzipien gefordert, nicht durch Zählen.
⚠️ = in der Funktionsdatei unzuverlässig oder unklar, muss geprüft werden.
Gezählt werden nur board-bezogene Fähigkeiten. Issues und Arbeitspakete der tracker-artigen Frontends (Ji, Op, Re) zählen als „Karte“, wo die Fähigkeit die Aufgabe selbst betrifft; Board-Fähigkeiten (Spalten, Verschieben) zählen nur dort, wo es ein Board gibt. Redmine hat **kein Board in seinem Kern** (Kanban nur per Plugin), daher erscheint es nur in den Zeilen auf Kartenebene.

**Regel:** Eine Fähigkeit ist *Erforderlich*, wenn mindestens vier der acht Frontends sie zeigen oder unsere Architektur sie braucht. Die Fähigkeits-ID in Backticks (`<object>.<action>`) ist ein Vorschlag — eine Fähigkeit ist eine Aktion am Objekt, nie ein Menüpunkt oder eine Geste (ADR 0037).

**Kernfakten:** Eine Karte **ist** ein JSCalendar-2.0-`Task` (dasselbe Objekt, das `fs-calendar` zeigt — keine Kopie). Die Board-Struktur hat keinen Standard: eigene Spezifikation, Kandidat Nr. 3 (`Project`, `Board`, `List`, `Relation`; ein `task_link` weist eine Aufgabe genau einer Liste zu). Eine *Spalte* ist hier das `List`-Modell. Eine Karte zu verschieben ist eine AS2-Aktivität.

Datenverweise: [Projekte, Übersicht](../../../data/projects/index.md) ·
[Projekte-Standards](../../../data/projects/standards.md) ·
[Projekte, technisch](../../../data/projects/technical.md) ·
[Ereignisse (Task)](../../../data/events/index.md).

## Erforderlich (gemeinsam bei den analysierten Programmen)

| Fähigkeit | Gesehen in | Daten / Standard | Status |
|-----------|------------|------------------|--------|
| Board anlegen, bearbeiten und öffnen (`board.create`, `board.edit`, `board.open`) | Tr, We, Pl, Ta, Ji, As, Op | eigenes `Board`-Modell (kein Standard, Spezifikationskandidat Nr. 3); gehört zu einem `Project` | Vorschlag |
| Spalten hinzufügen, umbenennen und sortieren (`column.create`, `column.rename`, `column.move`) | Tr, We, Pl, As (Abschnitte), Op; Ta, Ji (Spalten = Status) | eigenes `List`-Modell; `position` = sortierbarer Zwischenwert (eigene Entscheidung, offen) | Vorschlag |
| Karte anlegen (`card.create`) | Tr, We, Pl, Ta, Ji, As, Op, Re | JSCalendar `Task` in `calobj`; `task_link` legt sie in eine Spalte | Vorschlag |
| Titel und Beschreibung einer Karte bearbeiten (`card.edit`) | Tr, We, Pl, Ta, Ji, As, Op, Re | JSCalendar `title`, `description` | Vorschlag |
| Karte in eine andere Spalte oder Position verschieben (`card.move`) | Tr, We, Pl, Ta, Ji, As, Op | `Update` auf `task_link`, nicht auf der Aufgabe (technical.md); AS2 `Move` (Ursprung/Ziel) ist ein Kandidat ⚠️ offen; Envelope-Ereignis `task.moved` | Vorschlag |
| Status einer Karte setzen (`card.setStatus`) ⚠️ Spalte gegen Status ist nicht geklärt: bei Ta und Ji sind Spalten Status, bei Tr und Pl freie Listen | Ta, Ji, Op, Re | JSCalendar `progress`; RFC 10051 `PENDING`/`FAILED`, `VSTATUS` (Herstellereigenschaft, bis JSCalendar sie hat) | Vorschlag |
| Personen einer Karte zuweisen (`card.assign`) | Pl, As, Op, Re | JSCalendar `participants` (Rolle) → JSContact/Identität | Vorschlag |
| Fälligkeitsdatum setzen (`card.setDue`) | Tr, We, Pl, As, Op, Re | JSCalendar `due` | Vorschlag |
| Karten mit Fälligkeitsdatum im Kalender zeigen, ohne zu kopieren (Wirkung von `card.setDue`) | Tr, Pl, As, Op, Re (Kalenderansichten); We (iCal-Feed); *Arch.* | derselbe `Task` in `calobj`, Projektion „Kalenderansicht“ (technical.md) | Vorschlag |
| Karten mit Name und Farbe beschriften (`label.assign`) | Tr, We, Pl, As (Tags) | JSCalendar `keywords` an der Aufgabe; Name und Farbe des Labels werden am Board festgelegt: Lücke → eigene | Vorschlag |
| Eine Karte in kleine Schritte mit Fortschritt zerlegen (`subtask.add`) — Checklisten (Tr, We, Pl) und Unteraufgaben (Ta, Ji, As) werden zusammen gezählt; Tr sagt, Karten dürfen keine Karten enthalten | Tr, We, Pl, Ta, Ji, As | `Relation` `kind: parent` (Vorschlag: kein `parent_id` am Task); Fortschritt aus den Kindern | Vorschlag |
| Karten verknüpfen: hängt ab von, blockiert, bezieht sich auf (`relation.create`) | Ji, As, Op, Re | RFC 9253 `DEPENDS-ON`, `FINISHTOSTART` usw.; „blocks“ ist eine **Lücke** (`relatedTo` nur first/next/child/parent) → eigene `Relation`-`kind`-Aufzählung | Vorschlag |
| Dateien an eine Karte anhängen (`attachment.add`) | Tr, We, Pl, Ta, Op, Re | JSCalendar `links`; Blob in `fs-store` | Vorschlag |
| Eine Karte kommentieren (`comment.add`) | Tr, We, Pl, Op, Re | AS2 `Note` mit `inReplyTo` die Karte | Vorschlag |
| Karte oder Board beobachten und Änderungen erhalten (`card.watch`) | Tr, Pl, Op, Re | Abonnementliste: Lücke → eigene | Vorschlag |
| Bei Änderungen an beobachteten oder zugewiesenen Karten benachrichtigen (`card.notify`) | Tr, We, Pl, Ta, As, Op, Re | AS2-Aktivität als Quelle; der Zustellkanal ist Sache der Plattform ⚠️ nicht in data/projects definiert | Vorschlag |
| Verlauf einer Karte und eines Boards zeigen (`card.history`) | Tr, We, Pl, Ta, Op, Re | AS2-Aktivitäten der Karte (verschieben, ändern, kommentieren) | Vorschlag |
| Eigene Felder definieren und füllen (`field.define`, `card.setField`) | We, Pl, Ji, As, Op, Re (Tr über Power-Up) | JSCalendar-Herstellereigenschaften `freesynergy.net:<name>`; die Definition liegt am Board | Vorschlag |
| Ein Board aus einer Vorlage starten (`template.apply`) | Tr, We, Pl (Pro), As | eigene `Board`-Kopie; JSON der Board-Struktur | Vorschlag |
| Mitglieder zu einem Board einladen und ihnen eine Rolle geben — Besitzer, Mitwirkende, Beobachter (`member.add`, `member.role`) | Tr, We, Pl, Ta, Op, Re | Rollen aus description.md; W3C-Organisationsontologie (✅ URL, Inhalt nicht gelesen); Anmeldung bleibt die Plattform-Identität | Vorschlag |
| Board-Ereignisse an externe Systeme senden (`webhook.create`) | Tr, We, Pl, Ta, Ji, As, Op; Re (nur Plugin) | AS2-Aktivität als Nutzlast (Envelope-Thema, index.md) | Vorschlag |
| Ein Board exportieren (`board.export`) | We (JSON), Pl (PDF/HTML), As, Op, Re (CSV) | eigenes Board-JSON + JSCalendar `Task`; CSV/PDF abgeleitet | Vorschlag |
| Änderungen erscheinen live für alle und funktionieren offline (`board.sync`) | We, Pl (Echtzeit); *Arch.* (ADR 0019); Ji, Pl, Op haben keinen Offline-Modus | `fs-store` + `fs-hub`, Sync auf Objektebene | Vorschlag |
| Mit unserem eigenen Vertrag skripten und automatisieren, ohne separate API (`Capabilities`-Vertrag) | Tr, We, Pl, Ta, Ji, As, Op, Re (REST); *Arch.* ADR 0021 | Cap'n Proto → JSON / CLI / MCP | Vorschlag |

## Optional (bemerkenswerte Ideen)

| Fähigkeit | Gesehen in | Daten / Standard | Status |
|-----------|------------|------------------|--------|
| Swimlanes: eine zweite Achse quer zu den Spalten (`swimlane.create`) | We, Ta | Lücke → eigene Ergänzung von `Board` | Vorschlag |
| WIP-Limit je Spalte (`column.limit`) | Ji, Op | Lücke → eigene Eigenschaft von `List` | Vorschlag |
| Epics: Karten unter einer größeren Karte gruppieren (`epic.create`) | Ta, Ji, Op | `Relation` `kind: parent` | Vorschlag |
| Eine Karte als Duplikat markieren (`relation.create` mit duplicates) | Re | „duplicates“ ist eine **Lücke** → eigene `Relation`-`kind` | Vorschlag |
| Kartentypen (Fehler, Aufgabe …) mit eigenen Feldern (`card.type`) | Ji, Op, Re | JSCalendar `categories`; Felder je Typ: Lücke | Vorschlag |
| Erlaubte Statusübergänge je Rolle (`workflow.define`) | Ji, Re; Op (Admin-Workflows) | Lücke → eigenes Regelmodell | Vorschlag |
| Priorität einer Karte (`card.priority`) | Op, Re | JSCalendar `priority` | Vorschlag |
| Erinnerung vor dem Fälligkeitsdatum (`card.remind`) | Tr | JSCalendar `alerts` | Vorschlag |
| Wiederkehrende Karten (`card.repeat`) | Pl (Pro) | JSCalendar `recurrenceRules` | Vorschlag |
| Eine Person im Kommentar erwähnen (`comment.mention`) | Tr | AS2 `tag` vom Typ `Mention` | Vorschlag |
| Ort einer Karte, auf einer Karte gezeigt (`card.locate`) | Tr (Kartenansicht, Premium) | JSCalendar `locations`; Karte wird vom Kartenprogramm gezeigt | Vorschlag |
| Eine Karte kopieren, auch in ein anderes Board (`card.copy`) ⚠️ Pl „eine Karte in mehreren Boards“ steht im Widerspruch zu `task_link` (genau eine Liste) | Pl, Op, Re | neuer `Task` + `task_link`; geteilte Karte: Modelländerung nötig | Vorschlag |
| Eine Karte per Link teilen (`card.share`) | Op, Re | URL `/projects/<uuid>` (Entscheidung 3); Zugriffsprüfung offen | Vorschlag |
| Kartenvorlagen (`template.apply` auf einer Karte) | Tr, Pl (Pro) | JSON eines `Task` | Vorschlag |
| Archivieren statt löschen (`card.archive`, `board.archive`) | Pl | eigenes Flag; JSCalendar `status` ist dafür nicht gedacht ⚠️ | Vorschlag |
| Board-Hintergrund und Kartenfarbe (`board.style`) | Pl, Tr | JSCalendar `color` für die Karte; Board-Hintergrund: eigene | Vorschlag |
| Karten filtern und suchen, einen Filter speichern (`card.search`, `query.save`) | Op, Re, Ji (JQL), As | gespeicherte Abfrage über `calobj`-Felder; keine Abfragesprache geplant | Vorschlag |
| Tabellenansicht der Karten (`board.open` als Tabelle) | Tr, As, Op | Ansichtsparameter von `board.open` | Vorschlag |
| „Meine Karten“ über alle Boards (`card.list` gefiltert) | As, Pl (Dashboard), Re (Meine Seite) | gespeicherte Abfrage | Vorschlag |
| Regeln: Wenn eine Karte wandert, dann setzen/benachrichtigen (`rule.create`) | Tr (Butler), Ji, As; We hat keine | Auslöser = AS2-Aktivität; Regelmodell: Lücke | Vorschlag |
| Eine Karte per eingehendem Webhook anlegen (`card.create` über Vertrag) | We | derselbe Vertrag wie alles andere (ADR 0021) | Vorschlag |
| Eine Karte aus einer E-Mail anlegen (`card.create` aus `message`) | Op (Mail-Eingang) | per Live-Referenz vom Messenger übernommen (ADR 0017) ⚠️ | Vorschlag |
| Eingabeformular, das Karten anlegt (`form.submit`) | As | Lücke | Vorschlag |
| Commits mit einer Karte verknüpfen (`card.linkCommit`) | Ta, Ji, Re | JSCalendar `links`; Forge-Seite nicht bewertet | Vorschlag |
| Ein Board aus anderen Werkzeugen importieren (`board.import`) | We (Trello, CSV), Ta (Jira, Asana, Trello, GitHub), Pl (versionsabhängig) | Zuordnung noch zu schreiben ⚠️ | Vorschlag |

## Nicht geplant (bewusst)

| Funktion | Gesehen in | Warum nicht |
|----------|------------|-------------|
| Gantt, Zeitleiste, Baselines, kritischer Pfad | Tr, Pl, As, Ta, Ji, Op, Re | Planung gehört zu `fs-projectmanagement` |
| Zeiterfassung, Stoppuhr, Schätzungen | Tr (Power-Up), Pl, Op, Re | `fs-projectmanagement` |
| Budgets, Kosten, Kostensätze | Op | `fs-projectmanagement` |
| Portfolios, Auslastung, Ziele, Roadmaps mehrerer Projekte | As, Op, Ji | `fs-projectmanagement` |
| Meilensteine, Versionen, Roadmap | Ta, Op, Re, Ji | Projektebene, `fs-projectmanagement` (JSCalendar `Event`) |
| Scrum: Backlog, Sprints, Punkte, Velocity, Burndown | Ta, Ji, Op | nicht nur Board; kann später in `fs-projectmanagement` folgen (offen) |
| Berichte und Diagramme (Durchlaufzeit, Durchsatz) | Tr, Ta, Ji, Op, Re | `fs-projectmanagement` |
| Eigene Kalenderansicht oder iCal-Feed im Kanban-Programm | Tr, Pl, As, Re, Op; We, Op, Re (iCal) | `fs-calendar` zeigt denselben `Task` (ADR 0017) |
| Unterprojekte, Projekthierarchie | Re, Op | Projektebene, `fs-projectmanagement` |
| Wiki, Foren, Nachrichten, Besprechungen, Dokumente | Ta, Op, Re | eigene Programme (Wiki, Messenger) |
| Repository-Browser | Re | keine Board-Funktion |
| Eingebaute Chat- und Push-Integrationen (Slack, Telegram, 100+ Dienste) | Ta, As, Pl | Benachrichtigungen laufen über die Plattform und den Messenger |
| KI-Zusammenfassungen in der Cloud | As, Ji | nur lokales Modell (ADR 0029) |
| Bezahlstufen, die Ansichten, Gäste, SSO freischalten | Tr, Pl, Ji, Op | für immer kostenlos (ADR 0016) |
| Eigene Anmeldung, 2FA, LDAP/SAML | Pl, Re, We | Plattform-Identität (Kanidm), nicht das Programm |
| App-Marktplätze und Plugin-Systeme | Tr, Ji, As, Re | andere Programme teilen Standarddaten; Automatisierung über den Vertrag (ADR 0017, 0021) |

## Hinweise zu den Quellen

- ⚠️ Planka mischt Community- und Pro-Funktionen ohne klare Grenze (Vorlagen, Gäste, Ansichten, wiederkehrende Karten sind Pro); die Datei sagt, die Versionen unterscheiden sich. Zeilen, die Pl für solche Funktionen nennen, sind markiert.
- ⚠️ Der Wortlaut ist in einigen Dateien verstümmelt (Jira: „No native Gantt cannon“, wörtlich „keine native Gantt-Kanone“; Planka: „No darkroom for anonymous opening“, wörtlich „keine Dunkelkammer für anonymes Öffnen“; Wekan: „trough levels“, wörtlich „Tröge-Ebenen“ = Swimlanes). Wörtlich übersetzt, zu prüfen.
- ⚠️ Die Dateien zu Taiga, Jira und Asana nennen keine Details auf Kartenebene (Bearbeiter, Kommentare); dass sie dort fehlen, heißt nicht, dass sie im Produkt fehlen.
