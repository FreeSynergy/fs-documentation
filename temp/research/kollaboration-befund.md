# Befund: Kollaboration in FreeSynergy (Anwesenheit, gleichzeitiges Bearbeiten, Änderungsstrom)

Stand: 2026-11-11 · Recherche nur gelesen/abgerufen, nichts installiert, nichts geklont.
Legende: **belegt** = in einer Quelle unten gefunden · **[nicht belegt]** = nicht gefunden oder nicht geprüft · **Lizenzen** nur aus Paket-Metadaten, nicht aus LICENSE-Datei, sofern nicht anders vermerkt.

## 0. Vorgaben aus dem Projekt (belegt)
- ADR 0014: Standards zuerst, ActivityStreams 2.0 (AS2) als gemeinsame Basis. ADR 0020: AS2-Hülle für Speicherformat (`/srv/FreeSynergy/fs-documentation`, `git show origin/main:conventions/decisions/0020-speicherformat-as2-huelle.md`).
- ADR 0021: Cap'n Proto ist der Schnittstellenvertrag zwischen Programmen; JSON/CLI/MCP daraus erzeugt.
- ADR 0059 (Richtung akzeptiert, nichts gebaut): iroh in jedem Client, `iroh-gossip` als Mesh (Nachrichten nur 30 s vorgehalten, Behalten muss `fs-store` leisten), Signierung nötig, weil gossip Zugehörigkeit nicht schützt; Transport hinter eigenem Trait; nur eigenes Relais. Offen laut ADR: Moderator fällt weg → "logische Uhr, CRDT für Text".
- Vorhandene Festlegungen, die sich widersprechen oder ergänzen:
  - `docs/de/data/documents/standards.md` (Zeile 48): CRDT-Standard "keiner"; `automerge` 0.12 (MIT), `yrs` 0.28 (MIT) nur falls nötig. **Versionen dort nicht gegen Registry geprüft.**
  - `docs/de/programs/apps/whiteboard/design.md`: Empfehlung zuerst Synchronisation je Objekt hinter einer Schnittstelle, CRDT nur für Notiztext; Anwesenheit als eigene `Presence`-Schnittstelle.
  - `docs/de/programs/apps/roadmap.md` (2026-11-06): gemeinsames Arbeiten führt Eigenschaften mit logischer Uhr zusammen, CRDT nur für gemeinsamen Text; `loro` und `yrs` zu vergleichen.
  - `docs/de/data/standards.md` (Zeile 225): `wot-relay`, Architektur "Yjs default, Automerge-Alternative".
- Bestand im Wiki-Referenzprodukt (Wiki.js 3.1.1, `docs/de/programs/apps/wiki/frontends/wikijs/3.1.1/`): Live-Bearbeitung über Yjs-Websocket mit `y-monaco` und `y-prosemirror`. Wiki.js zeigt damit, dass Yjs für Block-/Rich-Text-Wiki im Einsatz ist (belegt als Nutzung, nicht als Reife-Urteil).

## 1. Vergleich CRDT-Bibliotheken

| Kriterium | Yjs (JS) | yrs (Rust-Port von Yjs) | Automerge (Rust-Kern `automerge`, `samod`) | Loro | diamond-types |
|---|---|---|---|---|---|
| Lizenz | MIT (belegt: Aggregatoren + socket.dev „MIT License © Kevin Jahns“; LICENSE nicht geprüft) | MIT laut Projektdoku (`docs/…/standards.md`); Aggregatoren für `y-sync` "Custom license"/"other" (uneinig) | MIT (belegt: lib.rs, C-Bindings MIT) | MIT (belegt: npm `loro-crdt`) | ISC laut Crate 1.0.0 (belegt); GitHub-Metadaten "None" → **Widerspruch, Repo-LICENSE prüfen** |
| Letzte Releases | [nicht belegt] (y-protocols 1.0.7 gesehen) | Projektdoku nennt 0.28; **nicht gegen Registry geprüft** | automerge JS 3.2.5 (jsDelivr); Automerge 3.0 Blog, Juli 2025 (RSS); samod 0.12.0 (docs.rs) | 1.14.1 (Aggregator, evtl. nicht neueste); Loro 1.0 Blog | Crate 1.0.0; "work in progress" laut Metadaten |
| Rust-Unterstützung | nein (JS-Kern) | ja, nativ (Port) | ja, Rust-Kern (Referenzimplementierung der Familie: [nicht belegt], nur Rust-Crate gefunden) | ja, Rust-Kern (Crate `loro`, 1.6.0 und 1.9.0 gesehen) | ja, nativ |
| Wasm / Frontend in Wasm | Frontend-Standard JS, Wasm-Status [nicht belegt] | [nicht belegt] | JS-Paket Wasm-Kern: [nicht belegt] | Kern in Wasm, npm `loro-crdt` (belegt) | npm-Paket über Wasm (belegt, GitHub-Hinweis) |
| Rich Text / Blöcke | Bindungen für ProseMirror und Monaco (belegt, Wiki.js); Blockstruktur über Y-Typen [nicht belegt im Detail] | [nicht belegt] | Rich Text seit 2.2 mit ProseMirror-Binding (belegt); Speicher als Text mit überlappenden Spans/Blöcken, kein Baum (belegt) | Peritext-artige Rich-Text-CRDT (belegt); Rust-API für Rich Text in älteren Versionen als "nicht bereitgestellt" markiert (docs.rs 1.6.0, Stand jetzt [nicht belegt]) | nur Text (belegt: "text CRDT") |
| Verlauf / Versionen | [nicht belegt] (Snapshots existieren laut allgemeiner Kenntnis, nicht geprüft) | [nicht belegt] | Verlauf ist Kernmerkmal, "universal version control" (Ink & Switch, belegt) | [nicht belegt] (Versionen/Checkout nicht geprüft) | [nicht belegt] |
| Speicher / Größe | [nicht belegt] | [nicht belegt] | Anekdote: Moby Dick Einfügen ~700 MB (2.x) gegen ~1,3 MB (3.x), HN-Kommentar, **nicht offiziell** | [nicht belegt] | "fastest text CRDT" (Eigenbeschreibung, unbelegt) |
| Anwesenheit (Awareness) | Awareness-Protokoll in `y-protocols/awareness.js`; zustandsbasiert, für Cursor/Name/Online (belegt). README sagt "unstable", Forum "stable" → **Widerspruch** | `y-sync` enthält Awareness laut Aggregator (belegt, Lizenz unklar) | [nicht belegt] | [nicht belegt] | – |
| Sync-Transport | Y-Websocket-Protokoll (belegt via Wiki.js); `yrs-warp`, `yrs-tokio`, `yrs-ax` (MIT bei tokio/axum) | Warp/Tokio/Axum-Server | samod (Rust Repo-Sync) | [nicht belegt] | – |
| Eignung Block-Wiki (Real-time ab Anfang) | gut belegt durch Wiki.js-Nutzung; Blockmodell selbst zu bauen | gleiche Familie, Rust-nativ | Rich-Text und Verlauf stark; Block-Modell prüfen | Rich Text + Verlauf gut, Rust-API-Stand prüfen | ungeeignet (nur Text) |
| Eignung Tasks (Kanban/Gantt live) | ungeeignet als Hauptmodell (Dokument-CRDT) → Eigenschaften mit logischer Uhr laut ADR-Richtung | dito | dito (Eigenschaften je Objekt) | dito | ungeeignet |

**Einordnung:** Für Tasks sind CRDTs nach eigener Festlegung (Whiteboard-Design, Roadmap) nicht nötig; dort reichen Synchronisation je Objekt mit logischer Uhr je Eigenschaft. Für Block-Wiki ist Yjs (plus yrs als Rust-Gegenstück) der belegt meistgenutzte Weg; Automerge und Loro sind die ernsthaften Alternativen mit Rust- und Wasm-Vorteilen. Vor einer Entscheidung: Lizenzen aus LICENSE-Dateien bestätigen, aktuelle Releases in crates.io/npm prüfen, `yrs`-Wasm und `yrs`-Rich-Text prüfen.

## 2. Anwesenheit / Awareness

- **Yjs Awareness** (belegt): CRDT für Benutzerstatus und flüchtige Daten (Cursor, Name, Auswahl), netzwerkagnostisch, wird vom Provider transportiert. Quelle: docs.yjs.dev, y-protocols PROTOCOL.md.
- **Matrix** (belegt, aus Entwurfs- und Client-Quellen, nicht aus aktueller Spec): Typing und Read-Receipts sind Ephemeral-Events mit `room_id`, außerhalb des Event-Graphs; Presence ist global (`m.presence`, online/offline/unavailable). MSC3961 ergänzt Typing im Sliding Sync. Aktuelle Spec-Seite: spec.matrix.org **[nicht abgerufen]**.
- **Liveblocks-Muster** (belegt, nur Doku-Ausschnitt): `useOthers` liefert alle verbundenen Nutzer eines Raums. Lizenz laut Sekundärquellen Apache-2.0, AGPL-Hinweis für einzelne Komponenten (**Widerspruch, LICENSE prüfen**). Wir würden nur das Muster übernehmen, keine SaaS.
- **Passung zu ADR 0059:** Awareness ist flüchtig und kann über `iroh-gossip` laufen (30 s Vorhalt reicht, wenn Presence nicht gespeichert werden muss). Signierung nötig (ADR 0059). Matrix-Presence-Modell ist ein brauchbares Vorbild für Felder (online, zuletzt gesehen, Ort), [nicht belegt] für Client-Seite.

## 3. Änderungsstrom (ActivityStreams 2.0)

- AS2 ist laut ADR 0014 und 0020 die Hülle (`id`, `type`, `attributedTo`, `to`/`cc`, `published`, `updated`…). Die W3C-Spezifikation selbst wurde in dieser Recherche **nicht abgerufen** [nicht belegt im Detail]; die Felder stammen aus dem ADR-Text und aus allgemeiner Kenntnis.
- Trennung: Änderungsstrom (AS2-Aktivitäten `Create`/`Update`/`Add`/`Remove`) ist das Protokoll der Ereignisse. CRDT-Updates sind Nutzlast in einer Aktivität, nicht die Aktivität selbst. Anwesenheit ist kein AS2-Ereignis, sondern Ephemeral.
- Cap'n Proto (ADR 0021) als Vertrag für die Nutzlast; JSON-Form aus dem Schema erzeugt.

## 4. Offene Punkte / Widersprüche (vor Opus-Vergleich klären)
1. diamond-types-Lizenz: Crate ISC, Repo-Metadaten "None".
2. Liveblocks-Lizenz: Apache-2.0 vs. AGPL-Hinweis.
3. y-sync-Lizenz: "Custom license" vs. "other".
4. y-protocols-Awareness: "unstable" (README) vs. "stable" (Forum).
5. Versionen `automerge` 0.12 und `yrs` 0.28 aus der Projektdoku: gegen crates.io prüfen (Automerge-Rust-Crate taucht bei samod als 0.12.0 auf).
6. Speicher- und Performance-Werte: nur Anekdote, Benchmarks [nicht belegt].
7. Verlauf/Snapshots bei Yjs, yrs und Loro: [nicht belegt].
8. Matrix-Presence: Spec-Stand [nicht abgerufen].

## 5. Quellen (URLs aus Suchergebnissen; nicht alle einzeln abgerufen)
- Yjs Awareness: https://docs.yjs.dev/api/about-awareness
- y-protocols PROTOCOL.md: https://github.com/yjs/y-protocols/blob/master/PROTOCOL.md
- y-protocols README: https://cdn.jsdelivr.net/npm/y-protocols@1.0.7/README.md
- y-protocols Lizenz-Aggregator: https://socket.dev/npm/package/y-protocols/overview/1.0.7
- yrs: https://github.com/yjs/yrs
- y-sync (Lizenz unklar): https://lib.rs/crates/y-sync
- yrs-tokio (MIT): https://lib.rs/crates/yrs-tokio
- Automerge Rust, MIT: https://lib.rs/Automerge
- Automerge 2.2 Rich Text: https://automerge.org/blog/rich-text/
- Automerge 3.0: https://automerge.org/blog/automerge-3/
- Ink & Switch "universal version control": https://inkandswitch.com/newsletter/dispatch-004
- samod 0.12.0: https://docs.rs/crate/samod/0.12.0/source/Cargo.toml
- Automerge JS 3.2.5: https://cdn.jsdelivr.net/npm/@automerge/automerge@3.2.5/package.json
- Loro 1.0: https://loro.dev/blog/v1.0
- loro-crdt npm: https://npmjs.com/package/loro-crdt
- loro docs.rs 1.6.0: https://docs.rs/crate/loro/1.6.0
- diamond-types 1.0.0 Cargo: https://rust-digger.code-maven.com/src/diamond-types-1.0.0/Cargo.toml.orig
- diamond-types Repo: https://github.com/josephg/diamond-types
- Liveblocks Presence: https://liveblocks.io/docs/products/sync/presence
- Liveblocks Lizenz (Repo): https://github.com/liveblocks/liveblocks (über Suchergebnis cdn.jsdelivr.net/gh/liveblocks/liveblocks@main/README.md)
- Matrix Typing (Entwurf): https://git.sudo.is/matrix/matrix-doc/src/branch/proofing/specification/modules/typing_notifications.rst
- Matrix MSC3961 (Sliding Sync Typing): https://github.com/matrix-org/matrix-spec-proposals/blob/kegan/ssext-typing/proposals/3961-sliding-sync-typing.md
- Matrix Spec (nicht abgerufen): https://spec.matrix.org
- ActivityStreams 2.0 (nicht abgerufen): https://www.w3.org/TR/activitystreams-core/
- Projekt: fs-documentation ADR 0014, 0020, 0021, 0059; `docs/de/data/documents/standards.md`; `docs/de/programs/apps/whiteboard/design.md`; `docs/de/programs/apps/wiki/frontends/wikijs/3.1.1/features.md`.

Ende. Opus vergleicht danach.
