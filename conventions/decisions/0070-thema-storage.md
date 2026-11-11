# 0070 – Thema `storage`: ein Baum für alles, worauf man Zugriff hat

Status: akzeptiert (Strategie, 2026-11-11); Code erst nach 3b-grün · Entscheidungen der Strategie vom 2026-11-11 (Punkte 1 bis 7 unten) · baut auf ADR 0045 (Themen-Schnittstellen, Unsupported), 0050 (ein Programm, eine Schnittstelle), 0066 (Typen, `TypeCatalog`), 0067 (Tresor), 0020 (AS2-Aktivitäten), 0046 (Speichern ≠ Export), 0063 (ein Befehl)

Befund und Belege: `temp/research/files-umfang.md` und `temp/research/files-umfang-standards-belege.md` (beide Stand 2026-11-11). Aussagen, die laut Belegen falsch oder nicht belegbar sind, sind hier nicht übernommen.

## Voraussetzung (Regel)
**Kein Code in `fs-interfaces` (auch kein Schema `storage.capnp`), bevor die Strategie diesen ADR angenommen hat und die Runde 3b grün ist.** Bis dahin gilt dieser Text nur als Beschluss ohne Code; `files.capnp` (DRAFT 0.2) und `BlobBackend` bleiben unverändert.

## Ausgangslage
- `BlobBackend` (fs-files) ist ein Byte-Speicher unter Schlüsseln, begleitet von einer Datenbank (fs-objects); Schlüssel gehören dem Programm. Er kennt Pending/Commit/Papierkorb-Spots, die für fremde Bäume sinnlos sind.
- `FileSource` (fs-components, `file_manager`) ist die Sicht des Fensters auf „mein“ fs-files: synchron, auf dem Oberflächen-Faden, nur „ganze Datei in einen Pfad“, ohne Bereich, Strom, Offline-Zustand.
- `files.capnp` kennt nur Uuid-Einträge („Programme sehen nie Pfade oder Backends“): ein fremder Baum passt nicht hinein.
- Vorhanden sind die Muster: Unsupported-Regel (ADR 0045), `SupportReport`, `Cursor`, `ChangeListener`/`Subscription`, `Problem` (RFC 9457), `Blob.read(offset,length)`, `BackendRegistry` (atomarer Tausch), `TypeCatalog` (ADR 0066), `call_limited` (fs-interfaces v0.0.18).

## Entscheidung (Strategie, 2026-11-11)

### 1. Neues Thema `storage`, neben `BlobBackend`
- `storage` ist ein **eigenes Thema** (Themen-Schnittstelle nach ADR 0045), es **erweitert `BlobBackend` nicht**.
- `BlobBackend`/fs-files werden **je ein Anbieter** von `storage` (Adapter über `Files`/`Folders`, damit die Datenbank die Wahrheit bleibt). `FileSource` wird **Adapter** über `storage`; Papierkorb und offene Uploads werden Wurzel bzw. Anbieter-Zustand.
- `opendal` bleibt **als Abhängigkeit draußen** (`fs-files/DESIGN.md`: der Writer versteckt die Multipart-Id, ein Upload wäre nach Neustart nicht fortsetzbar). Nur das **Layer-Modell** dient als Muster (Zeitlimit, Wiederholung, Protokoll außen um den Anbieter, Decorator nach ADR 0043).
- Fähigkeit eines Anbieter-Pakets: `storage.provider 1.0` (ADR 0068).

### 2. Files zeigt alles, worauf man Zugriff hat
Home, USB, DAV, S3, fremde Rechner, virtuelle Link-Ordner, Ressourcen anderer Programme, Baum von Websites. **Files zeigt nur an und ruft auf**; es hält keine Wahrheit (nur Registry der Anbieter, Ansichtszustand, Auswahl). **Streaming gehört nicht zu Files** (`fs-streaming`); Files liefert **Bereichs-Downloads** (Range): `Blob.read(offset,length)` gibt es schon, neu ist nur der HTTP-Zugang (`Range`, 206, `Content-Range`, `ETag`/`If-Range`, Token des Menschen). Naht zu `fs-streaming` ist allein `read`.

### 3. Schreiben
Sofort lesend **und** schreibend: **lokal (Home/USB)**, die **eigene fs-files-Ablage** und **S3**. Alle anderen Anbieter **zuerst nur lesend**. Schreiben kommt je Anbieter, **sobald seine `caps()` es belegt** (Flag gesetzt und Test grün).

### 4. Fremde Rechner
- **Eigene** Rechner: SFTP mit Zugangsdaten **aus dem Tresor** (ADR 0067). **Bis `fs-vault` steht: noch nicht.**
- Rechner **anderer**: nur **auf Einladung des Eigentümers**, standardmäßig **nur lesend**, mit **Protokoll beim Eigentümer** (`fs-history`).

### 5. Programm-Bäume
Zuerst **nur anzeigen** und „**öffnen im Besitzerprogramm**“. Schreiben nur über **Fachbefehle des Besitzers**, **später** (ADR 0050). Programme liefern ihre Daten über ihre **eigene Schnittstelle** als Baum, **nie direkt aus der Datenbank**; die Abbildung entscheidet der Besitzer.

### 6. Websites
Eigene und geteilte: voll. Bei **fremden** Websites: **nur das veröffentlichte `sitemap.xml` lesen**, `robots.txt` beachten, **kein eigenes Crawlen, kein Folgen von Links**.

### 7. Offline-Cache fremder Anbieter
**Später**, erst wenn `fs-vault` (Verschlüsselung) steht; dann **verschlüsselt, mit Größengrenze, abschaltbar**. Bis dahin: kein Cache; Files zeigt „nicht erreichbar“ statt eines alten Stands.

## Schnittstelle `StorageProvider` (Entwurf, nicht Code)

### Leitgedanken
1. **Ort** = `fs://<anbieter-id>/<pfad>`; die **Eintrags-Id** ist ein opaker Text, Pfade sind Anzeige, die Id ist Wahrheit.
2. **Kern** (immer): `caps`, `roots`, `list`, `stat`, `open`. Alles andere hat die **Standardantwort `Unsupported`** (ADR 0045) **und** ein Flag (ADR 0066: Fenster zeigt gesperrt).
3. Bereich, Seiten, Zeitlimit, Abbruch, Watch sind **Teil des Vertrags**.
4. Der Anbieter beschreibt Orte, nicht Aussehen (ADR 0066).

### Rust-Trait (Entwurf)
```rust
#[async_trait]
pub trait StorageProvider: Send + Sync {
    fn capabilities(&self) -> StorageCaps;
    async fn roots(&self) -> Result<Vec<Root>>;
    async fn list(&self, at: &EntryId, page: PageReq) -> Result<EntryPage>;   // eine Ebene, Cursor, Sort
    async fn stat(&self, id: &EntryId) -> Result<Entry>;
    async fn open(&self, id: &EntryId, ctl: &Ctl) -> Result<Blob>;   // Blob.read(offset, length), wie heute
    // Standard "Unsupported":
    async fn write(&self, at: &EntryId, name: &str, src: ByteSource, o: WriteOpts, ctl: &Ctl) -> Result<Entry>;
    async fn create(&self, at: &EntryId, name: &str, kind: Kind, on: OnConflict) -> Result<Entry>;
    async fn rename(&self, id: &EntryId, name: &str, on: OnConflict) -> Result<Entry>;
    async fn move_to(&self, id: &EntryId, to: &EntryId, on: OnConflict) -> Result<Entry>;
    async fn copy_to(&self, id: &EntryId, to: &EntryId, on: OnConflict, ctl: &Ctl) -> Result<Entry>;
    async fn delete(&self, id: &EntryId, how: Delete /* Trash | Purge */) -> Result<()>;
    async fn restore(&self, id: &EntryId, to: Option<&EntryId>, on: OnConflict) -> Result<Entry>;
    async fn watch(&self, at: &EntryId, l: Listener) -> Result<Subscription>;
    async fn changes(&self, since: Token) -> Result<ChangeSet>;
}
```
- **`OnConflict` kennt nie „ersetzen“** (`keepBoth`, `fail`; wie `files.capnp`).
- **`Ctl`** trägt `deadline` (Zeitlimit über `call_limited`, **fs-interfaces v0.0.18**), `cancel` (Abbruch) und `progress` (Fortschritt). Lange Aufgaben (`copy`, `write`, rekursives Löschen) sind Jobs mit Fortschritt und Abbruch.
- **Zugangsdaten nur als Tresor-Verweis** (`credential: vault://<id>`, ADR 0067), nie im Klartext in der Anbieter-Konfiguration; ohne Zugang meldet `caps().state = needsLogin`.

### Ort der Schnittstelle
Schema `storage.capnp` **und** der Rust-Trait `StorageProvider` kommen nach **`fs-interfaces`** (wie bei jedem Thema), sonst müssten fs-tasks, fs-wiki u. a. für ihre Programm-Bäume von fs-files abhängen. **fs-files ist Besitzer des Themas** (ADR 0050) und baut Registry (`StorageRegistry`), Anbieter und HTTP-Zugang.

### Cap'n Proto (Entwurf `storage.capnp`)
```capnp
struct StorageCaps {
  create @0 :Bool; write @1 :Bool; rename @2 :Bool; move @3 :Bool; copy @4 :Bool;
  trash @5 :Bool; restore @6 :Bool; range @7 :Bool; watch @8 :Bool; versions @9 :Bool;
  share @10 :Bool; quota @11 :Bool; atomicMove @12 :Bool; serverCopy @13 :Bool;
  preview @14 :Bool; search @15 :Bool; deltaSince @16 :Bool;
}
enum EntryKind { unknown @0; file @1; folder @2; link @3; app @4; }
struct Entry {
  id @0 :Text;  name @1 :Text;  kind @2 :EntryKind;
  size @3 :Int64 = -1;            # -1 = unbekannt
  modified @4 :Timestamp;  mediaType @5 :Text;
  preview @6 :PreviewHint;  caps @7 :EntryCaps;   # Fähigkeiten je Eintrag
  etag @8 :Text;  owner @9 :Text;  open @10 :Text; envelope @11 :Envelope;
}
interface StorageProvider {
  supportReport @0 () -> (report :SupportReport);
  caps    @1 () -> (caps :StorageCaps, state :ProviderState);  # ready | needsLogin | offline | readOnly
  roots   @2 () -> (roots :List(Root));
  list    @3 (at :Text, cursor :Cursor, sort :Sort) -> (page :EntryPage);
  stat    @4 (id :Text) -> (entry :Entry);
  open    @5 (id :Text) -> (blob :Blob);
  write   @6 (at :Text, name :Text, mediaType :Text, onConflict :OnConflict) -> (upload :Upload);
  create  @7 (at :Text, name :Text, kind :EntryKind, onConflict :OnConflict) -> (entry :Entry);
  rename  @8 (id :Text, name :Text, onConflict :OnConflict) -> (entry :Entry);
  move    @9 (id :Text, to :Text, onConflict :OnConflict) -> (entry :Entry);
  copy    @10 (id :Text, to :Text, onConflict :OnConflict) -> (entry :Entry);
  delete  @11 (id :Text, purge :Bool) -> ();
  restore @12 (id :Text, to :Text, onConflict :OnConflict) -> (entry :Entry);
  watch   @13 (at :Text, listener :ChangeListener) -> (subscription :Subscription);
  changes @14 (since :Data) -> (changes :List(Change), token :Data);
  types   @15 () -> (catalog :TypeCatalog);                    # ADR 0066
}
```
Ordinale nur anhängen; neue Flags ans Ende (ADR 0045: nach 1.0 nur Sprünge). Bei `kind=app` ist `size = -1`, `open` verweist ins Besitzerprogramm.

### Watch
`watch` (Push, `ended` bedeutet neu abonnieren und neu lesen) **oder** `changes(since)` (Delta mit Token, Muster Graph `delta`/Drive `changes`), beides unter den Flags `watch`/`deltaSince`. Fehlt beides: Files fragt `stat` (ETag) des offenen Ordners oder zeigt „Aktualisieren“. Ist das Token zu alt (Graph: 410 Gone), neu vollständig lesen.

### Fehlermodell (RFC 9457)
Wie überall `Problem`, Typen unter `https://freesynergy.net/problems/storage/…`. Übernommen: `name-conflict`, `invalid-name`, `not-found`, `unsupported` (501), `backend-failed`, `too-large`. Neu: `offline` (503), `needs-login` (401), `forbidden` (403), `timeout` (504), `cancelled` (499), `quota-exceeded` (507), `changed` (412, ETag stimmt nicht), `cycle` (508).

### AS2-Mapping und Undo (ADR 0014, 0020)
Jede ändernde Handlung ist eine Aktivität im Protokoll des Besitzers: `Create`; `Update` (rename); `Remove` + `Add` (move, mit `origin`/`target`); `Delete` (Papierkorb); `Undo` (Wiederherstellen/zurück verschieben). Bei Anbietern ohne Objekte (WebDAV, S3, SFTP) ist die Aktivität **lokal** (Files-Sicht), `object` = Anbieter-URI. Undo nennt **was und wo** und springt dorthin. `purge` ist nicht rückgängig und sagt das vorher; ohne Flag `trash` wird kein Undo fürs Löschen versprochen.

### Programm-Bäume (Punkt 5, Abbildung beim Besitzer)
Jedes Programm liefert neben seiner Fachschnittstelle **selbst** einen dünnen `StorageProvider` und entscheidet die Abbildung (ADR 0050: eine Wahrheit, ein Weg); fs-files baut keine Adapter für fremde Programme. Beispiele: fs-tasks (Projekt, Liste, Aufgabe), fs-calendar (Kalender, Jahr, Monat, Ereignis), fs-wiki (Bereich, Seite), fs-people (Facetten, Karten). Regeln: (1) `read` eines `app`-Eintrags liefert die abgeleitete **Export-Darstellung im Standardformat** (ADR 0030, 0046), nie die Wahrheit; (2) `sensitive`/`to` der Hülle gelten weiter (ADR 0029); (3) Kopieren nach außen ist **Export**; (4) Löschen ruft den Besitzer.

## Standards und Vorbilder (nur Belegtes; Quellen unten, Abruf 2026-11-11)
- **WebDAV (RFC 4918):** `PROPFIND` mit `Depth` 0/1/infinity (Server muss 0 und 1 können; ohne Header gilt infinity), `Overwrite: T/F` bei COPY/MOVE (Standard T), **Sperren sind verbindlich** (der Server verlangt das Sperr-Token). Lehre: Tiefe ist ein Parameter; wir erlauben nur eine Ebene (eigene Designentscheidung). `OnConflict` kennt kein Ersetzen.
- **HTTP (RFC 9110):** 206 Partial Content, `If-Range`: Grundlage der Bereichs-Downloads.
- **Solid/LDP:** LDP-Container sind Ressourcen mit `ldp:contains` (W3C-Empfehlung 2015). WAC/ACP und Notifications gehören zum **Solid Protocol** (Community-Group-Bericht, kein W3C-Standard), nicht zum LDP. Wir übernehmen kein RDF.
- **SFTP:** `draft-ietf-secsh-filexfer-02` (Version 3, abgelaufener Draft, kein RFC): Handles (`opendir`/`readdir`), `read` mit 64-Bit-Offset, Attribut-Flags; `rename` scheitert bei vorhandenem Ziel. Der Draft -13 (Version 6) kennt Rename-Flags (Überschreiben, atomar).
- **S3:** `ListObjectsV2` mit undurchsichtigem `ContinuationToken` (bis 1000 Schlüssel je Antwort), `prefix`/`delimiter` mit `CommonPrefixes`; `GetObject` mit `Range` (ein Bereich je Aufruf); Multipart (Teile 1 bis 10000); Ordner sind Präfixe. Ob S3 „kein Umbenennen“ hat, ist nicht belegt und wird nicht behauptet.
- **Microsoft Graph:** `delta` mit Token (Ende: `@odata.deltaLink`, zu altes Token: 410 Gone; Einträge nach Id verfolgen); **`GET …/content` antwortet mit 302 auf die `downloadUrl`, der `Range`-Header geht an diese URL**; `createUploadSession` (Fragmente in Reihenfolge, je höchstens 60 MiB, Vielfaches von 320 KiB); `conflictBehavior` fail/replace/rename (wir nutzen nur die Entsprechung ohne replace).
- **Google Drive:** **eine Datei hat genau einen Elternordner**; Verknüpfungen über `shortcut` (Eintrag mit Ziel); `capabilities` je Datei; `changes.list` mit `pageToken`; Workspace-Dokumente über `files.export` in ein gewähltes Format (Muster für `kind=app`). Range-Downloads sind offiziell nicht belegt, wir verlassen uns nicht darauf.
- **Nextcloud:** Chunked Upload v2 (MKCOL, nummerierte PUT, Abschluss per MOVE von `.file`), Eigenschaften `oc:fileid`, `oc:permissions`, `nc:has-preview`, `oc:size` nur auf Anforderung im PROPFIND, `getetag` standardmäßig. Pfade, Trash/Versions-Wurzeln, Preview und OCS-Shares sind nicht belegt.
- **rclone:** optionale Schnittstellen (`Copier`, `Mover`, `DirMover`, `PublicLinker`, `About`, `ChangeNotifier`, `PutStreamer`) und eine `Features`-Struktur, die das Backend füllt (`fs/features.go`). Lehre: Kern plus gemeldete Fähigkeiten; bei uns zusätzlich Standardantwort `Unsupported`.
- **`object_store` (MIT oder Apache-2.0):** schmaler Trait (`put_opts`, `put_multipart_opts`, `get_opts` mit Bereich, `delete_stream`, `list`, `list_with_delimiter`, `copy_opts`); `rename_opts` ist standardmäßig Kopieren, dann Löschen. Wird schon im S3-Anbieter genutzt.
- **OpenDAL (nur Muster, keine Abhängigkeit):** `Operator` mit `stat`/`list`/`read_with` (Bereich)/`write`/`copy`/`rename`; **Layer** legen Verhalten um den Dienst; die Fähigkeiten stehen in `info()`.
- **GVfs/KIO, SMB, FUSE:** nur als grobe Anregung (URI-Orte, Watch, Zugang nach außen); Einzelheiten sind **nicht belegt** und fließen nicht in die Entscheidung. FUSE/WinFsp ist (Schritt 12) ein späterer **Zugang nach außen**, nicht die Form der Schnittstelle.

## Risiken und Gegenvorschläge
1. **Rechte.** Jeder Aufruf trägt die Identität des Menschen; der Besitzer prüft (ADR 0050, 0029). Nie mit Dienstrechten alles zeigen. Fremde Rechner nur auf Einladung (Punkt 4).
2. **Offline/Anmeldung.** `ProviderState` in `caps`; Zeitlimit statt Hängen (`call_limited`); Schreiben gesperrt; keine stille Warteschlange. USB/Netz kommen und gehen als Registry-Änderung (Hot-Plug, ADR 0045).
3. **Riesige Bäume.** `list` nur eine Ebene mit Cursor, nie rekursiv; Ordnergröße `-1`; Suche im Anbieter (Flag `search`); virtuelles Scrollen im Fenster.
4. **Zyklen bei Link-Ordnern.** Links sind Einträge mit Ziel, nie automatisch aufgelöst; „Besucht“-Satz und Tiefengrenze (z. B. 32), Treffer ergibt `cycle`; `copy`/`delete` folgen Links nie.
5. **Abgrenzung zu `fs-streaming`.** Files liefert Bytes eines vorhandenen Eintrags, keine Segmente, Codecs oder Live-Ströme; Naht ist `read`.
6. **Programm-Bäume täuschen Dateien vor.** `kind=app` sichtbar gekennzeichnet, `caps` ehrlich, Kopieren nach außen = Export, Löschen im Sinn des Besitzers.
7. **Zwei Wahrheiten bei fs-files.** Der fs-files-Adapter spricht `Files`/`Folders`, nicht `BlobBackend`. Fremde Verzeichnisse haben keine Hülle; Objekte entstehen nur, wenn der Mensch sie übernimmt (Import/`rescan`).
8. **Schnittstelle zu breit zu früh.** ADR 0045 verlangt zwei Anbieter vor 1.0: zuerst die kleine Lese-Schnittstelle mit lokalem Ordner und S3, dann ein zweiter (SFTP oder WebDAV). Protokoll-Zoo als Hot-Plugins, nicht im Kern.
9. **Sicherheit.** SSRF (Anbieter-URL auf interne Adressen), Pfad-Traversierung und Symlinks (bestehende Regeln `key.rs`, `confined.rs`), Steuerzeichen in Namen, lügende Größen/Zeiten: gleiche Namensregeln wie `files.capnp`, Normalisierung vor der Anzeige, Anbieter in eigenem Prozess.
10. **Namenskonflikte** (Groß/Klein, Unicode, Länge) fallen oft erst beim Schreiben auf: `name-conflict` mit `detail`, `keepBoth`, nie ersetzen.
11. **Websites (Punkt 6)** belasten fremde Server und berühren Datenschutz: darum nur `sitemap.xml`, `robots.txt` beachten, kein Crawl. Eine fremde `sitemap.xml` wird **nur auf ausdrückliche Handlung des Menschen** geholt, nie im Hintergrund, weil jeder Abruf die eigene IP verrät; mit Zeitlimit und Größengrenze.

## Aufwand und Reihenfolge (12 Schritte)
| Schritt | Inhalt | Repo(s) | Größe |
|---|---|---|---|
| S1 | Schema `storage.capnp`, Doku `docs/en/interfaces`; **erst nach 3b grün** | fs-interfaces, fs-documentation | klein |
| S2 | Rust-Trait `StorageProvider`, Null-Objekt, `Ctl` (in fs-interfaces); `StorageRegistry` (Muster `BackendRegistry`) in fs-files | fs-interfaces, fs-files | mittel |
| S3 | Anbieter lesend: lokaler Ordner, S3 (`list_with_delimiter`, `get_opts` mit Bereich) | fs-files | mittel |
| S4 | fs-files selbst als Anbieter (Papierkorb als Wurzel); `FileSource` wird Adapter, async; `FileProblem` um `offline`, `timeout`, `cancelled` … erweitert | fs-components, fs-files | mittel |
| S5 | HTTP-Zugang `Range`/206/ETag mit Token; Test mit echtem Player | fs-files | klein-mittel |
| S6 | Schreibweg für lokal, fs-files, S3 (Punkt 3): `write`, `create`, `rename`, `move`, `copy`, `delete`, `restore`, Jobs | fs-files | mittel |
| S7 | Watch: inotify lokal, `changes(token)` entfernt; Ersatz für nur-`rescan` | fs-files | mittel |
| S8 | SFTP (eigene Rechner) und WebDAV (lesend) mit Tresor-Verweis; **braucht `fs-vault`** | fs-files, fs-vault | mittel |
| S9 | Programm-Bäume, nur anzeigen und „öffnen im Besitzerprogramm“ (zuerst fs-tasks, fs-wiki) | je Programm | je klein |
| S10 | Virtuelle Orte (Link-Ordner mit Zyklenschutz, Papierkorb aller, Zuletzt); Websites per `sitemap.xml` | fs-files | mittel |
| S11 | Frontend: jede Wurzel, Menüs aus `caps`/`TypeCatalog`, Fortschritts-/Abbruchleiste | fs-components, fs-files | groß |
| S12 | Später: Offline-Cache (nach `fs-vault`), Einladung für fremde Rechner, Schreiben je Anbieter und Programm-Befehle, FUSE/WinFsp, weitere Anbieter als Hot-Plugins | eigene Repos `fs-files-<anbieter>` | später |

Abhängigkeiten: S1 → S2 → S3 → S4; S5 nach S3; S6, S7 nach S4; S8 braucht `fs-vault`; S9 nach S2. `call_limited` ist mit fs-interfaces v0.0.18 vorhanden.

## Folgen
- `fs-interfaces`: Schema `storage.capnp` erst nach Annahme und 3b grün (siehe Voraussetzung); `files.capnp` bleibt.
- `fs-files`: Trait, Registry, Anbieter, HTTP-Zugang; `fs-components`: `FileSource` als Adapter.
- Katalog `docs/en/interfaces/index.md`: Zeile „File storage“ wird Thema „Storage“ (bei S1).

## Offene Fragen
- Die Einladung für fremde Rechner (samt Protokoll beim Eigentümer) wird ein eigenes späteres ADR auf Basis von ADR 0059 (iroh); hier nur der Verweis.
- Größengrenze und Standardwert des Offline-Caches: später.

## Quellen (Abruf 2026-11-11)
RFC 4918 `https://www.rfc-editor.org/rfc/rfc4918` · RFC 3253 · RFC 5323 · RFC 9110 `https://www.rfc-editor.org/rfc/rfc9110` · W3C LDP `https://www.w3.org/TR/ldp/` · Solid Protocol 0.11.0 `https://solidproject.org/TR/protocol` · `draft-ietf-secsh-filexfer-02` und `-13` (`https://www.ietf.org/archive/id/draft-ietf-secsh-filexfer-02.txt`) · S3 `ListObjectsV2`, `GetObject`, Multipart (`https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html`) · Graph `driveitem-delta`, `-get-content`, `-createuploadsession` (`https://learn.microsoft.com/en-us/graph/api/driveitem-delta`) · Google Drive v3 `files`, `changes.list` (`https://developers.google.com/workspace/drive/api/reference/rest/v3/files`) · Nextcloud WebDAV `basic`, `chunking` (`https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/chunking.html`) · rclone `fs/features.go` (`https://raw.githubusercontent.com/rclone/rclone/master/fs/features.go`) · `object_store` (`https://docs.rs/object_store/latest/object_store/trait.ObjectStore.html`) · OpenDAL `Operator` (`https://opendal.apache.org/docs/rust/opendal/struct.Operator.html`). Einzelnachweise mit Status: `temp/research/files-umfang-standards-belege.md`.

## English summary
**Decision (accepted by the Strategy, 2026-11-11; code only after round 3b is green):** a new topic interface `storage` sits beside `BlobBackend` and does not extend it. `BlobBackend`/fs-files become one provider each; `FileSource` becomes an adapter; `opendal` stays out as a dependency (only its layer model is a pattern). Files shows everything the person has access to (home, USB, DAV, S3, other machines, link folders, other programs' resources, website trees), only displays and calls the owner; streaming stays in `fs-streaming`, Files serves byte ranges.

**Rules:** writing is immediate for local, the own fs-files store and S3; all other providers are read-only until their `caps()` prove writing. Own machines via SFTP with credentials from the vault (not before `fs-vault`); other people's machines only on the owner's invitation, read-only by default, logged at the owner. Program trees: display and "open in owner program" first; writes only through the owner's domain commands, later; data comes through the owner's own interface, never from its database. Websites: own and shared in full; foreign ones only the published `sitemap.xml`, `robots.txt` respected, no crawling. Offline cache for foreign providers only after `fs-vault`, encrypted, size-limited, switchable. Schema and Rust trait live in `fs-interfaces`; fs-files owns the topic and builds registry, providers and the HTTP access; every program supplies its own `StorageProvider`. Interface: `caps/roots/list/stat/open` (`open` returns a `Blob` with `read(offset,length)`) plus write operations answering `Unsupported` by default (ADR 0045), `OnConflict` never replaces, `Ctl` with deadline (`call_limited`, fs-interfaces v0.0.18), cancel, progress; credentials only as vault references; errors as RFC 9457; changes map to AS2 activities with `Undo`. Only standards confirmed in the source check are used. **Precondition:** no code in `fs-interfaces` before the Strategy accepts this ADR and round 3b is green. Remote sitemaps are fetched only on an explicit human action (the request reveals the IP), with timeout and size limit. The invitation for other people's machines will be its own later ADR based on ADR 0059.
