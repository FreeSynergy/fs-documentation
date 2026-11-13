# 0073 – Kollaboration überall mit Loro

Status: Entwurf (Strategie, 2026-11-12; Nutzerwunsch „Kollaboration überall“); Code erst nach 3b und Wiki · baut auf ADR 0014 (Standards zuerst, AS2), 0020 (Speicherformat), 0021 (Cap'n Proto), 0042 (Datenbank ist die Wahrheit), 0046 (Speichern ≠ Export), 0050 (Besitzer), 0054 (KI-Teilnehmer), 0059 (iroh), 0067 (Tresor), 0071 (Versionen, Backup), 0072 (Blöcke)

Befund und Quellen: `temp/research/kollaboration.md` (Opus-Empfehlung) und `temp/research/kollaboration-befund.md` (Stand 2026-11-11, Primärquellen: crates.io, npm, GitHub inkl. LICENSE-Dateien).

## Kontext
Mehrere Menschen (und markierte KIs, ADR 0054) sollen **gleichzeitig** am selben Dokument, Board oder Plan arbeiten, auch **offline und ohne Server** (ADR 0059). Dafür braucht es ein CRDT, ein Bild davon, **wer gerade da ist** (Awareness), einen Änderungsstrom und Regeln für Rechte und Löschen.

## Entscheidung (Entwurf)

### 1. Bibliothek: Loro
**Loro** (`loro` in Rust, `loro-crdt` als Wasm aus demselben Kern; Lizenz MIT laut LICENSE-Datei; 1.x, aktiv gepflegt). Gründe:
- **Ein Kern**: Engine (nativ) und Frontends (Wasm) verhalten sich gleich.
- **Blockmodell eingebaut**: `LoroTree` (verschiebbarer Baum) mit Metadaten je Knoten passt zu ADR 0072 (Block mit Id und Metadaten); Rich Text mit Marken in `LoroText`.
- **Anwesenheit eingebaut** (`EphemeralStore`), **Verlaufskürzung** (`shallow_snapshot`), `checkout`/`fork_at` für Versionen.
- **Transportneutral**: Updates sind Bytes mit Versionsvektoren; sie sind Nutzlast in Cap'n Proto (ADR 0021) und laufen über iroh (ADR 0059).

**Ehrliche Gegenargumente:** Loro ist kein De-facto-Standard (Yjs hat das größere Ökosystem; auch Yjs ist keine formale Norm); kleines Team dahinter. Darum wird das CRDT **hinter einer eigenen Schnittstelle `CollabDoc`** gekapselt (Version gepinnt, ein Ort; wie bei `BackupEngine`, ADR 0071), und der Export in offene Formate geht jederzeit (ADR 0046).
**Dokumentierte Alternative: `yrs`** (MIT, 0.x, Yjs-kompatibel, Wiki.js-Ökosystem); sie wird gewählt, falls Yjs-Kompatibilität schwerer wiegt. **Nicht verwenden:** `y-sync` (Repo archiviert, in `yrs::sync` aufgegangen), `diamond-types` (nur Text, ISC, kein Release seit 2022). Automerge ist nicht gewählt (Blöcke nur als Textmarker, Verlauf ohne Kürzung).

### 2. Awareness: immer sichtbar, wer da ist
- In jedem gemeinsam bearbeiteten Dokument und Board ist **jederzeit sichtbar, wer gerade darin ist** (Name, Farbe, Gerät, Status aktiv/untätig/abwesend, Ort im Dokument).
- **Cursor und Auswahl anderer sind standardmäßig sichtbar; jeder kann seine eigenen abschalten** (dann zeigt nur noch die Anwesenheit „ist im Dokument“). Es gibt keinen Zwang, den eigenen Cursor zu zeigen.
- Anwesenheit ist **flüchtig** (`EphemeralStore`, Zeitlimit etwa 30 s), wird **nie gespeichert** und läuft **nie im Änderungsstrom**. Jeder Eintrag ist signiert (ADR 0059). Schema siehe `temp/research/kollaboration.md` §4 (Vorschlag, anhängbar).
- KIs erscheinen als **markierte Teilnehmer** (ADR 0054), nie als Mensch.

### 3. Wahrheit
Bei gemeinsam bearbeiteten Objekten ist das **Loro-Dokument (Schnappschuss plus Änderungen) die Wahrheit**. Es liegt im **Store des Besitzers** (ADR 0050); damit gilt **ADR 0042 weiter: die Datenbank hält die Wahrheit**. Task-Objekte und Abfrage-Indizes sind **daraus abgeleitete Projektionen**, nach jedem Merge neu berechnet. JSCalendar und iCal sind **Exporte** (ADR 0046). **Ohne Kollaboration** (rein lokal) ändert sich für den Menschen nichts: es ist ein Loro-Dokument mit einem einzigen Teilnehmer.

### 3a. Datenmodell
Ein `LoroDoc` je Seite (Wiki, ADR 0072) bzw. je Board/Projekt. Wiki-Seite: `LoroTree` der Blöcke. **Die Block-Id (UUIDv7, ADR 0072) steht als Metadatum am Knoten des Blockbaums; die internen CRDT-Knoten-Ids sind nicht die Block-Id** und werden nie als Verweis nach außen benutzt (sie überleben Export und Import nicht). Speicherformat: Loro-Snapshot als Nutzlast in einer AS2-Hülle (ADR 0020); **Export** (Markdown/HTML/AS2-JSON) ist eine getrennte, verlustbehaftete Projektion. Benannte Stände sind `Frontiers` plus AS2-`Update` (Zusammenspiel mit ADR 0071 Versionen).

### 4. Änderungsstrom: AS2
Lokale Änderungen werden gebündelt (`set_change_merge_interval`) und als AS2-Aktivität (`Update`, `Create`, `Add`, `Remove`, `Move`) mit `object` = Block-/Task-Id und `attributedTo` = Actor verschickt (ADR 0014/0020). Die CRDT-Bytes sind **Nutzlast**, nicht die Aktivität selbst.

### 5. Transport
Cap'n Proto (ADR 0021) als Vertrag, **iroh** (ADR 0059) als Weg zwischen Geräten, über den Hub (`fs-hub`) als Rückfall; kein fremdes Websocket-Protokoll. Der Transport hinter einer Schnittstelle, wie in ADR 0059 vorgesehen.

### 6. Rechte: vor dem Import prüfen
Ein CRDT kennt keine Rechte. Darum: **jede Änderung ist signiert** (ADR 0059), Peer-Id und Identität (Kanidm hinter eigenem Wrapper, ADR 0047) sind fest gebunden. Der Empfänger **prüft „darf dieser Autor das?“ VOR dem Import** (ADR 0050, Gruppen ADR 0055). Eine bereits gemergte unerlaubte Änderung lässt sich nicht sauber zurücknehmen; deshalb wird sie gar nicht erst importiert, abgelehnte Änderungen werden **sichtbar gemeldet**, nicht stillschweigend verworfen. Gruppendaten sind mit dem Gruppenschlüssel verschlüsselt (ADR 0067).

### 7. Löschen: Verlauf standardmäßig voll, „wirklich löschen“ als Pflicht
- **Standard:** der volle Verlauf bleibt (Tombstones), damit Rückgängig und Verlauf funktionieren. **Es gibt keine automatische Kürzung** und keinen Standardwert dafür. Gekürzt wird nur auf **ausdrücklichen Wunsch des Menschen**: über „wirklich löschen“ oder über eine von ihm gesetzte, einstellbare Obergrenze (Dauer oder Größe); danach liegt Älteres nur noch in Sicherungen (ADR 0071).
- **Pflicht „wirklich löschen“** (DSGVO-Recht auf Löschung): auf Wunsch wird der Inhalt **aus dem Verlauf entfernt bzw. der Verlauf neu geschrieben** (`shallow_snapshot` ab dem Zeitpunkt nach dem Inhalt, anschließend alte Verläufe verwerfen).
- **Ehrlicher Hinweis, immer vorher gezeigt:** **Peers, die einen alten Stand haben, können die Daten noch besitzen**; Files kann das auf fremden Geräten nicht erzwingen. Der Dialog nennt, welche bekannten Geräte/Menschen betroffen sind und welche Sicherungen den Inhalt noch halten (ADR 0071, „bleibt in Sicherungen bis …“). Ältere Peers brauchen danach einen vollständigen Snapshot statt inkrementellem Abgleich.

### 8. Aufgaben (Kanban, Plan, Gantt) ohne Schiedsrichter
Ein `LoroDoc` je Board mit Maps und beweglichen Listen (Aufgaben, Spalten, Reihenfolge, Abhängigkeiten), **nicht serverautoritativ** (ADR 0059: kein Moderator). Das CRDT erzwingt keine Invarianten (Zyklen in Abhängigkeiten, WIP-Limits, Karte in zwei Spalten). **Die Engine prüft nach jedem Merge deterministisch, zeigt Konflikte an und bietet eine Auflösung an; sie lehnt nichts still ab.** **Planungsdaten** (frühester Start, Puffer, kritischer Pfad, Gantt-Termine) werden **berechnet statt gespeichert**. Zyklen, die erst **nach einem Merge** entstehen, bekommen `Readiness::Conflict`: sie werden **angezeigt, nicht abgelehnt**. Das Gantt rechnet **nominal** und sagt das **sichtbar** („nominal“); ein Arbeitszeit-Kalender kommt später aus `fs-calendar` **über dessen Schnittstelle**, Tasks hat keinen eigenen Kalender. Lange Beschreibungen sind eigene Wiki-Blöcke.

### 9. Spike vor dem Festschreiben
Wasm-Größe von `loro-crdt` und Leistung bei großen Seiten/vielen Peers sind **nicht gemessen**. Sobald das Wiki dran ist, läuft ein **kleiner Spike** mit echten Wiki-Seiten (Größe des Wasm-Pakets, Zeit für Öffnen/Merge, Speicher). Fällt er schlecht aus, greift die dokumentierte Alternative `yrs` hinter `CollabDoc`.

## Entwurfsmuster (ADR 0043)
**Adapter/Facade** (`CollabDoc` kapselt Loro), **Observer** (Änderungs- und Anwesenheitsströme), **Strategy** (austauschbarer Transport und CRDT), **Memento** (benannte Stände), **Specification** (Rechteprüfung vor Import als reine Funktion, für sich getestet).

## Risiken
1. **Speicherwachstum** durch vollen Verlauf: Kürzen (`shallow_snapshot`) nur auf Wunsch des Menschen, vorher Sicherung; Anzeige des Platzes (Platz schonen, ADR 0071); Grenze: ältere Peers brauchen einen vollen Snapshot.
2. **Abhängigkeit von einem kleinen Team:** `CollabDoc`, gepinnte Version, offener Export.
3. **Springende Blöcke bei gleichzeitigem Verschieben:** in der Oberfläche kennzeichnen.
4. **Falsche Sicherheit beim Löschen:** darum der ehrliche Hinweis in Punkt 7.
5. **Datenschutz der Anwesenheit:** Cursor abschaltbar, Anwesenheit nie gespeichert.

## Folgen
- `fs-interfaces`: Thema `collab` (Dokument öffnen, Änderungen senden/empfangen, Anwesenheit; Rechteprüfung als Eingang), nach Annahme und 3b. `fs-wiki` und Aufgaben-Programm: Loro hinter `CollabDoc`. Code erst nach Runde 3b grün und nach dem Wiki.
- Entschieden (Strategie): Standard ist der volle Verlauf, ohne automatische Kürzung.

## English summary
**Decision (draft):** Loro (MIT, Rust core plus Wasm) behind our own `CollabDoc` interface; yrs documented as the alternative; `y-sync` and `diamond-types` not used. Awareness is always visible (who is in the document); cursors and selections are visible by default and everyone can turn their own off; presence is ephemeral and never stored. Change stream as AS2 with the CRDT bytes as payload; transport Cap'n Proto plus iroh. Every change is signed and rights are checked before import. History is kept in full by default, with no automatic trimming (only on explicit request or a limit the human sets); "really delete" is mandatory (remove from history / rewrite) with an honest warning that peers holding an old state may still have the data. The Loro document (snapshot plus changes) is the truth for shared objects, held in the owner's store (so ADR 0042 still holds); task objects and query indexes are projections recomputed after each merge, JSCalendar/iCal are exports; purely local use is a document with one participant. Tasks have no referee: the engine checks cycles and WIP limits after a merge, shows conflicts (`Readiness::Conflict` for cycles created by a merge) and never silently rejects; planning data (earliest start, slack, critical path) is computed, not stored; the Gantt is nominal and says so, a working-time calendar comes later from `fs-calendar` through its interface. The block id (UUIDv7) is metadata on the block-tree node, not the internal CRDT node id. A small spike measures Wasm size and speed once the wiki is under way. **Status: draft; code only after round 3b and the wiki.**
