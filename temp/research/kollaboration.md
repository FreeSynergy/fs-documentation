# Empfehlung: Kollaboration (CRDT, Anwesenheit, Änderungsstrom)

Stand: 2026-11-11 · Opus-Prüfung von `BEFUND.md` gegen Primärquellen (crates.io-API, npm-Registry, GitHub-API inkl. LICENSE-Dateien und Quelltext). Nichts installiert, nichts geklont.

## 1. Geprüfte Fakten (Primärquellen)

| Bibliothek | Version (Registry) | Lizenz (LICENSE-Datei / Manifest) | Reife / Aktivität |
|---|---|---|---|
| `yrs` (y-crdt) | 0.28.1, 2026-11-04 | MIT (LICENSE-Datei: Sypytkowski, Jahns) | aktiv; noch 0.x; enthält `yrs::sync::{awareness, protocol}`; Wasm über `ywasm` |
| `y-sync` | 0.4.0, 2023-11-17 | MIT (LICENSE-Datei); crates.io zeigt „non-standard“ nur wegen Metadaten | **Repo archiviert**, Inhalt in `yrs::sync` aufgegangen → nicht verwenden |
| Yjs (JS) | 13.6.33 stabil; 14.0.0 in Beta/RC (`@y/y`) | MIT (LICENSE-Datei; GitHub-Erkennung „NOASSERTION“ wegen Zusatz-Copyright RWTH) | Umbruch v13→v14 läuft |
| `automerge` | 0.12.0, 2026-09-16; JS 3.5.0 | MIT | aktiv; Blöcke über `split_block`/Spans; Sync-Repo `samod` 0.16.0 (nicht 0.12) |
| `loro` | 1.17.1 (crates.io), 1.18.0 im Repo; npm `loro-crdt` 1.17.1 | MIT (LICENSE-Datei) | aktiv (Push 2026-11-10); 1.x stabil; Wasm aus demselben Rust-Kern |
| `diamond-types` | 1.0.0 vom 2022-08-25; Repo-Manifest 2.0.0 unveröffentlicht | ISC (Manifest + README „published under the ISC license“) | nur Text-CRDT, kein Release seit 2022 → raus |

**Widersprüche aus BEFUND §4 geklärt:**
1. diamond-types: **ISC** ist richtig. GitHub zeigt „None“, weil keine LICENSE-Datei im Repo liegt; die Lizenz steht in README und Cargo.toml.
2. Liveblocks: **beides stimmt** – Repo überwiegend Apache-2.0, aber `@liveblocks/server` und `liveblocks`-CLI sind AGPL-3.0-or-later (Root-LICENSE). Für uns egal: nur das Muster `useOthers`/Presence dient als Vorbild, kein Code.
3. y-sync: **MIT** (LICENSE-Datei). „Custom/other“ kommt aus fehlendem SPDX-Feld. Repo ist archiviert.
4. Yjs-Awareness: Die README von `y-protocols@1.0.7` sagt „This API is unstable and subject to change“; die aktuelle README auf `master` hat den Satz nicht mehr und dokumentiert Awareness fest (Map clientID→Zustand, 30 s Ablauf). Fazit: Protokoll faktisch stabil, aber offiziell nie als stabil versioniert.
5. Versionen in `docs/de/data/documents/standards.md` (automerge 0.12, yrs 0.28): **stimmen**.

## 2. Entscheidung: **Loro** (`loro` + `loro-crdt` für Wasm)

**Begründung**
- **Ein Kern für alles:** Rust-nativ; das Wasm-Paket wird aus demselben Kern gebaut. Engine (native) und Frontends (Wasm) verhalten sich gleich, es gibt keine zwei Implementierungen wie bei Yjs/yrs.
- **Blockmodell eingebaut:** `LoroTree` (verschiebbarer Baum mit Fractional Index), dazu `get_meta(node) -> LoroMap` je Knoten. Das passt genau zu „Block mit stabiler Id + Metadaten“: Verschieben und Verschachteln ohne Duplikate. Yjs v13 hat kein Move. Automerge kennt Blöcke nur als Marker im Text, nicht als Baum.
- **Rich Text in Rust:** `LoroText::mark/unmark/to_delta/apply_delta` (Peritext-artig) sind im Rust-API vorhanden. Der Hinweis „nicht bereitgestellt“ aus docs.rs 1.6.0 ist überholt.
- **Anwesenheit eingebaut:** `EphemeralStore` (Zeitlimit je Schlüssel, eigene Bytes-Codierung) ersetzt seit 1.4.6 das alte `Awareness`. Er ist transportneutral und passt damit auf `iroh-gossip`.
- **Versionen und GC:** `checkout`, `fork_at`, `ExportMode::{Snapshot, updates(vv), shallow_snapshot}`, `compact_change_store`, `set_record_timestamp`. Damit lassen sich „Speichern ≠ Exportieren“ und gekürzter Verlauf direkt abbilden.
- **Transportneutral:** Updates sind `Vec<u8>` mit Versionsvektoren. Sie passen als Nutzlast in Cap'n Proto (ADR 0021) und laufen über iroh (ADR 0059). Ein fremdes Websocket-Protokoll ist nicht nötig.
- Lizenz MIT, aktive Pflege, Editor-Bindungen `loro-prosemirror` (MIT) und `loro-codemirror` (MIT) vorhanden.

**Gegenargumente (ehrlich)**
- **Kein De-facto-Standard:** Yjs ist der Branchenstandard mit dem größten Ökosystem (y-prosemirror: 467 Sterne gegenüber 145 bei loro-prosemirror) und wird von Wiki.js genutzt. ADR 0014 „Standards zuerst“ spricht eher für Yjs. Allerdings ist auch Yjs keine formale Norm; das Protokoll ist nur durch die Implementierung festgelegt.
- **Abhängigkeit von einem kleinen Team** (loro-dev). Gegenmittel: CRDT hinter eigenem Trait (`CollabDoc`) kapseln, so wie es ADR 0059 für den Transport vorsieht.
- **Keine Interoperabilität mit dem Yjs-Ökosystem** (z. B. Wiki.js-Live-Bearbeitung). Ein Wiki.js-Frontend als Gegenprobe müsste über unsere Engine laufen, nicht über y-websocket.
- **Zweitplatzierter: yrs.** Wählen, falls der Nutzer Yjs-Kompatibilität höher gewichtet. Zu beachten: 0.x-Version, der Umbruch Yjs v14 kommt, und Move fehlt.
- Automerge ist nicht gewählt: Blöcke nur als Textmarker, Verlauf ohne Kürzung (kein Shallow-GC), Anwesenheit nur in `samod`/automerge-repo.

## 3. Datenmodell-Skizze Wiki-Seite (ein `LoroDoc` je Seite)

```
LoroDoc (peer = Geräte-Id, abgebildet auf Kanidm-Identität)
├─ "page"   : LoroMap   { title: LoroText, lang, tags: LoroList, as2_id }
└─ "blocks" : LoroTree  (Fractional Index an)
     node TreeID  ── stabile Block-Id = TreeID (peer@counter), zusätzlich
     │               meta.uid = UUIDv7 für externe Links/AS2 (überlebt Export/Import)
     └─ get_meta(node): LoroMap
          uid       : String (UUIDv7, einmal gesetzt)
          type      : "paragraph" | "heading" | "list" | "code" | "embed" | "table" …
          attrs     : LoroMap   { level, lang, checked, … }        (LWW je Schlüssel)
          meta      : LoroMap   { created_by, labels, review_state, … }
          content   : LoroText  (Rich Text; Marks: bold, link{href}, mention{actor}, …)
                      | LoroMap (strukturierte Blöcke, z. B. embed{ref})
```
- Verschieben ist `tree.mov()`, Verschachteln läuft über den Elternknoten. Gelöschte Knoten bleiben als Tombstone im Verlauf.
- Speicherformat: Loro-Snapshot-Bytes in AS2-Hülle (ADR 0020) als Nutzlast. **Export** (Markdown/HTML/AS2-JSON) ist eine getrennte, verlustbehaftete Projektion.
- Versionen: benannte Stände = `Frontiers` + AS2-`Update`-Aktivität. Gesicherte Snapshots kommen über rustic_core (ADR 0071) in `fs-store`.

## 4. Awareness-Schema (flüchtig, nicht gespeichert, kein AS2-Ereignis)

`EphemeralStore` je Dokument, Zeitlimit 30 s (passt zum 30-s-Vorhalt von iroh-gossip). Schlüssel = `actor_id/device_id`, Wert (Cap'n-Proto-Struct, signiert nach ADR 0059):
```
Presence {
  actor      : Text   # AS2-Actor-IRI (Kanidm)
  device     : Text
  name, color: Text
  status     : enum { active, idle, away }        # Vorbild: Matrix m.presence
  location   : { doc: Text, block_uid: Text? }    # wo bin ich
  cursor     : { anchor: LoroCursor, head: LoroCursor }?   # stabile Cursor (`get_cursor`)
  selection  : List(block_uid)?                    # Blockauswahl
  typing     : Bool
  view       : { app: "wiki"|"tasks", mode: "kanban"|"gantt"|… }?
  ts         : UInt64
}
```
Globale Anwesenheit (online/offline) ist ein eigener App-weiter Store. Die Anwesenheit im Dokument hängt am jeweiligen Dokument.

## 5. Tasks (Kanban / Projektplan / Gantt live)

**Empfehlung: ebenfalls Loro, aber nur Map/MovableList statt Text. Nicht serverautoritativ.** Grund: ADR 0059 nimmt den Moderator weg, offline und P2P sind gesetzt. Mit einem Modell bleiben Sync-Pfad, Verlauf und Anwesenheit gleich. Das entspricht der Roadmap-Vorgabe „Eigenschaften mit logischer Uhr“: LoroMap ist LWW je Feld mit Lamport-Uhr.

```
LoroDoc je Projekt/Board
├─ "tasks"   : LoroMap<task_uid, LoroMap{ title: LoroText, status, assignee, start, due,
│                                         estimate, column_uid, labels: LoroList, desc_ref }>
├─ "columns" : LoroMovableList<LoroMap{ uid, name, wip_limit }>
├─ "order"   : LoroMap<column_uid, LoroMovableList<task_uid>>   # Kartenreihenfolge
└─ "deps"    : LoroMap<"from→to", LoroMap{ type: FS|SS|FF|SF, lag }>  # Kante = Schlüssel
```
- **Invarianten kann das CRDT nicht erzwingen** (Zyklen in `deps`, WIP-Limits, Karte in zwei Spalten nach gleichzeitigem Verschieben). Die Engine prüft nach jedem Merge deterministisch, markiert Verstöße als „Konflikt“ (AS2-`Flag`/Hinweis) und bietet eine Auflösung an. Sie lehnt aber nichts ab. Die Gantt-Termine werden aus `deps` abgeleitet und nicht gespeichert.
- Lange Beschreibungen liegen als eigener Wiki-Block bzw. eigenes Doc (`desc_ref`), damit das Board-Doc klein bleibt.

## 6. Änderungsstrom (AS2)

Lokale Commits werden gebündelt (`set_change_merge_interval`) und als AS2-Aktivität `Update` (bzw. `Create`/`Add`/`Remove`/`Move`) mit `object` = Block-/Task-uid und `attributedTo` = Actor versendet. Die CRDT-Update-Bytes sind Nutzlast (Cap'n Proto), nicht die Aktivität selbst. Anwesenheit läuft nie im Strom.

## 7. Risiken

- **Speicherwachstum:** Loro behält standardmäßig den vollen Verlauf. Gegenmittel: periodisch `shallow_snapshot` ab einer Version; alte Abschnitte vorher als rustic-Snapshot sichern; `compact_change_store`. **Grenze:** Peers, die älter als der Shallow-Start sind, können nicht mehr inkrementell mergen und brauchen einen vollständigen Snapshot. Zeitreisen vor den Shallow-Start gehen nur über das Backup.
- **Löschen/DSGVO:** Gelöschter Text bleibt im CRDT-Verlauf. Echtes Entfernen geht nur über Shallow-Snapshot und das Verwerfen alter Verläufe auf allen Peers. Das ist ein Prozess, keine Funktion.
- **Rechte:** Ein CRDT kennt keine Autorisierung. Jede Änderung muss signiert sein (ADR 0059). Empfänger prüfen „Autor darf X“ je Change; Peer-Id und Kanidm-Identität müssen fest gebunden sein. Eine unerlaubte Änderung lässt sich nach dem Merge nicht sauber zurücknehmen → **vor** dem Import filtern.
- **Herstellerbindung/Format:** Loro-Format seit 1.0 stabil (laut Projekt). Trotzdem CRDT hinter einem eigenen Trait halten und den Export in offene Formate jederzeit möglich machen.
- **Wasm-Größe** von `loro-crdt` im Frontend [nicht gemessen]. **Leistung** bei großen Seiten bzw. vielen Peers [nicht gemessen] → Benchmark mit echten Wiki-Seiten vor dem Festschreiben.
- Gleichzeitiges `mov` mit Zyklusgefahr löst LoroTree intern. Bei Konflikten springen Blöcke trotzdem sichtbar → im UI kennzeichnen.

---
### Offene Fragen für den Nutzer
1. Loro (bessere Passung: Baum, Rust/Wasm aus einem Kern, GC) oder yrs (größeres Ökosystem, „Quasi-Standard“ Yjs, Wiki.js-kompatibel)? Empfehlung: Loro.
2. Wie lange soll der vollständige Bearbeitungsverlauf im CRDT bleiben, bevor er gekürzt wird und nur noch im rustic-Backup liegt (z. B. 90 Tage)?
3. Tasks P2P ohne Server-Schiedsrichter, Konflikte werden nur angezeigt: einverstanden? Oder soll bei Zyklen/WIP-Limits ein Knoten (z. B. Projekt-Owner) verbindlich entscheiden?
4. Soll Anwesenheit Cursor und Ansicht anderer **standardmäßig** zeigen, oder muss jede Person das einschalten (Privatsphäre)?
