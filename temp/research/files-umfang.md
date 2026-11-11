# Befund: Umfang von Files und Schnittstelle "Speicher-Anbieter" (StorageProvider)

Stand 2026-11-11. Nur gelesen, nichts geändert. Die Standards-Aussagen in Abschnitt (b) sind in `files-umfang-standards-belege.md` gegengeprüft; wo die Belege widersprechen, steht hier „**laut Belegen:**“ (Beleg-Nummer in Klammern). Auftrag: todo/sprint.md Zeilen 89-94 (`origin/main`, fs-documentation). Kürzel der Repos auf GitHub: `FreeSynergy/<repo>`, Stand `main`.
Zeilenangaben Code: lokale Arbeitskopie unter `/srv/FreeSynergy/<repo>`; URL = `https://github.com/FreeSynergy/<repo>/blob/main/<Pfad>#L<Zeile>`.

## Kurzfassung

1. Es gibt schon zwei **verschiedene** Schichten, und keine ist ein Baum-Anbieter: `BlobBackend` (fs-files) ist ein **Byte-Speicher unter Schlüsseln**, der von einer Datenbank (fs-objects) begleitet wird; `FileSource` (fs-components) ist die **Sicht des Fensters** auf "mein" fs-files (Papierkorb, Rescan, Uploads). Keine von beiden kann "einen fremden Baum anzeigen" (WebDAV, Programmdaten, Website).
2. Die Strategie hat recht: dazwischen fehlt eine **Themen-Schnittstelle `storage`** (Baum lesen, schreiben, Fähigkeiten). Sie darf nicht `BlobBackend` erweitert werden (der kennt Pending/Commit/Trash-Spots, die für fremde Bäume sinnlos sind), sondern sitzt **darüber**: `BlobBackend` wird einer von vielen Anbietern (`LocalFolder` und `S3Backend` bekommen einen dünnen Adapter), und `FileSource` wird zu einem Adapter über die neue Schnittstelle.
3. Fast alles Nötige ist als **Muster** da: Unsupported-Regel (ADR 0045), `SupportReport`, Cursor-Seiten, `ChangeListener`/`Subscription`, RFC-9457-Probleme, `Blob.read(offset,length)`, Registry mit atomarem Tausch, `TypeCatalog` (ADR 0066). Neu zu schreiben sind: das Schema `storage.capnp`, Orte/Wurzeln, Tresor-Verweis in der Anbieter-Konfiguration, der Baum-Dienst der Programme.
4. Range-Download gibt es **schon** (`Blob.read(offset,length)`, `BlobBackend.get`, S3 `get_range`). Fehlt nur der HTTP-Zugang (`Range`-Header, 206) und der Fortschritt/Abbruch.
5. Größte Risiken: Zyklen bei Link-Ordnern, riesige Bäume, Rechte (wessen Zugriff gilt, wenn Files für jemanden liest), Offline-Anbieter, und dass Programm-Bäume "Dateien vortäuschen" (Schreiben = Fachbefehl, nicht Dateischreiben).

## (a) Was es schon gibt (mit Belegen)

### Provider-Schicht in fs-files
- `BlobBackend` (Trait): `/srv/FreeSynergy/fs-files/crates/fs-files-core/src/backend/provider.rs:34` ([URL](https://github.com/FreeSynergy/fs-files/blob/main/crates/fs-files-core/src/backend/provider.rs#L34)). Methoden `capabilities()` (36), `kind()` (38), `get(key, offset, length)` (41), `stat` (43), `put`/`commit`/`pending` (47-58), `delete` (60), nur für Namens-Backends `publish`, `relocate`, `discard`, `make_dir`, `remove_dir`, `scan(dir)` (78-120). Alles Nicht-Gelesene hat Standard "Unsupported" (Null Object, Kopf Z. 1-6). **`get` hat schon Bereich (offset/length), `scan` ist eine Ebene, ohne Seiten im Trait** (Schema hat Cursor, Trait nicht; `DESIGN.md` listet es als offenen Punkt).
- Kern-Einschränkung: Schlüssel gehören dem Programm. `Naming::ById` (S3: Schlüssel sind undurchsichtige Ids, Umbenennen ist nur eine DB-Änderung) gegen `Naming::ByName` (lokal): `backend/place.rs:8-13`. Der Inhalt der Ordner wird **nicht** vom Backend gelistet, sondern aus der Datenbank; `scan` dient nur dem `rescan`.
- Registry: `BackendRegistry` `backend/registry.rs:22-143` (Snapshot in `Arc`, atomar getauscht, `add`/`remove`/`list`/`active`). `BackendInfo{id,kind,active}` `files.capnp:107`. Fabrik/Prüfung: `backend/factory.rs` (`check_backend` prüft vor dem Tausch).
- Vorhandene Backends: `LocalFolder` (`backend/local/`), `S3Backend` über `object_store 0.14` (`fs-files-core/Cargo.toml:12,26`; schmaler Adapter `backend/s3/api.rs:24-40` mit `get_range`, `list(prefix)`, Multipart). WebDAV: "nicht gebaut, wie vereinbart" (`DESIGN.md`, Zeile "sharing ... WebDAV ... not built"). `opendal` bewusst **nicht** genommen, weil der Writer die Multipart-Id versteckt und ein Upload nach Neustart nicht fortsetzbar wäre (`/srv/FreeSynergy/fs-files/DESIGN.md:253`).
- Datentypen der Files-Programms (`file`, `folder`, `picture`, `storage`, `album`): `/srv/FreeSynergy/fs-files/crates/fs-files-types/src/` (`storage.rs` beschreibt `StorageBackend` als Typ für `Files.types`).

### Vertrag (fs-interfaces)
- `files.capnp` (DRAFT 0.2, "Consumers: none (0 of 2)", Z. 1-5): `/srv/FreeSynergy/fs-interfaces/schema/files.capnp`. `Files` (113) mit `folders`, `transfer`, `search`, `backends`, `sharing` (leer, 201), `subscribe` (118), `types` (122); `Folders.list` mit `Cursor` + `Sort` (126); `Transfer.open -> Blob` (187); `BlobBackend` als Schnittstelle (213-233) mit Spot/Scanned (236-252). Alle Einträge haben nur Uuid, keine Pfade: "Programme sehen nie Pfade oder Backends" (Z. 8-9). Das ist die Ursache, warum ein Fremdbaum nicht hineinpasst.
- Gemeinsam (`common.capnp`): `Blob{size, read(offset,length)}` Z. 33-36; `Cursor` Z. ~21; `Problem` (RFC 9457) Z. ~23-31; `ChangeListener`/`Subscription` Z. 91-95 (Strom mit `ended`, Regeln: bei `ended` neu abonnieren und neu lesen); `Support`/`SupportReport` Z. 103-126; `unsupportedProblemType` Z. 101; Hüllenfeld `Envelope` mit AS2-Typ, `to/cc/audience`, `sensitive` Z. 53-71; `Change{created,updated,deleted}` Z. 76-82.
- `types.capnp` (ADR 0066): Typbeschreibung je Datentyp (Felder, Grundtyp, Befehle mit `supported`), `BasicType.reference` (AS2-IRI eines Objekts) Z. 16 ff. Jeder Anbieter bietet `TypeCatalog.describe`.
- `resources.capnp` ist das Programm "Dinge/Räume/Material" (fs-resources), **nicht** "Ressourcen anderer Programme": Missverständnis vermeiden; im Sprint heißt es "Ressourcen der Programme aus deren Daten" (Z. 93).

### FileSource (fs-components)
- Trait `FileSource`: `/srv/FreeSynergy/fs-components/crates/fs-components-workbenches/src/file_manager/source.rs:17` ([URL](https://github.com/FreeSynergy/fs-components/blob/main/crates/fs-components-workbenches/src/file_manager/source.rs#L17)). **Synchron**, auf dem Oberflächen-Faden (Z. 3-7: "ein langer Upload friert das Fenster ein ... provisorisch"). Methoden: `capabilities`, `list(request, after)`, `entry`, `folder`, `subfolders`, `preview(key, limit)`, `create_folder`, `rename`, `move_to`, `copy_to`, `trash`, `delete_folder`, `restore`, `restore_to`, `purge`, `trash_count`, `empty_trash`, `rescan`, `upload(path)`, `pending_uploads`, `resume_upload`, `drop_upload`, `download(key, path)`.
- `FileCapabilities` `file_manager/reports.rs:9-32`: Bool-Flags `change, keep_both, trash, restore_to, upload, download, rescan, sort, type_descending, search, dates`. **Es fehlen** `range`, `watch`, `versions`, `share`, `quota`, `move`/`copy` getrennt, `stream`.
- Fehler: `FileProblem{NotFound, NameConflict, InvalidName, ChangedOutside, MarkedNeedsRelease, Unsupported, Failed}` `file_manager/error.rs:10-25`. Es fehlen `Offline`, `Unauthorized`, `Timeout`, `TooLarge`, `Cancelled`.
- Konsequenz: `download(key, path)` kennt nur "ganze Datei in einen Pfad"; kein Bereich, kein Strom.

### ADRs (gelesen: `git show origin/main:conventions/decisions/<n>*.md`)
- **0014/0020** AS2-Hülle + Fachstandard + Aktivitätsprotokoll; Leihen = Live-Verweis, Entziehen = `Undo` (0020 Z. 11-16). Basis für unser Undo-Mapping.
- **0021** Schnittstelle = Cap'n Proto, JSON/CLI/MCP werden **erzeugt**; Frontend ist Paket mit benötigten Fähigkeiten (Z. 5-14).
- **0045** Jedes Thema eine Schnittstelle, Ziel statt Wachstum; "wie Elternklasse: jeder Anbieter alle Methoden, sonst ausdrücklich nicht möglich"; Bedingung 1.0: bei Anbieter-Schnittstellen **zwei Anbieter** (Z. 17-19). Katalog `docs/en/interfaces/index.md`: Zeile "File storage - Local folder, RustFS over S3, git, WebDAV" steht unter **Providers** ("Database", "File storage" ...), Thema "Files" unter Topics, Besitzer `fs-files`.
- **0043** Muster, Schnittstellen zuerst, kleine Dateien (Z. 9-18).
- **0046** Speichern ist nicht Exportieren: Kopie in DB, Export ist ein eigener Schritt; große Dateien bleiben im Dateispeicher (Z. 5-15).
- **0050** Ein Standard, ein Programm, eine Schnittstelle, **IMMER** (Z. 6-8). Das ist die Rechtfertigung für Punkt (2) der Strategie: andere Programme liefern Daten nur über Besitzer-Schnittstelle.
- **0061** Facetten (Gallery, Music, Videos, Documents als Facetten von fs-files), Admin-Frontend Pflicht.
- **0063** Ein Programm, ein Befehl (`fs-files serve`).
- **0066** Typbeschreibung meldet `supported` je Befehl; "keine Darstellung im Programm"; Galerie zeigt Quellen von weiter weg wie YouTube/PeerTube, "angebunden wie KIs in People (Anbieter hinter einer Schnittstelle)" (Z. 42). Das ist ein zweites Beispiel für Anbieter-Schnittstellen.
- **0067** Tresor `fs-vault`: "Kein Programm hält eigene Geheimnisse" (Z. 11-13), Secret Service / Credential Manager; Gruppenschlüssel MLS; Server-Daten verschlüsselt, Suche auf dem Gerät (Z. 20-34).
- **0068** Fähigkeiten statt fester Anforderungen: Pakete melden `provides`/`requires` als Namen der Themen-Schnittstellen, z. B. `people.persons 1.2`; zur Laufzeit meldet die Schnittstelle selbst, was geht (`supported`) (Z. 7-13). Passt für `storage.provider 1.0` als Fähigkeit eines Anbieter-Pakets (WebDAV-Plugin, Programm-Baum).
- 0069 (update schließt und stellt wieder her): `call_limited`. **Laut Korrektur der Strategie (2026-11-11):** ist in fs-interfaces **v0.0.18** vorhanden, die frühere Aussage „nicht in main“ war falsch. (Ursprünglich stand hier „noch nicht in `main`/v0.0.17“.)
- `docs/en/programs/apps/files/requirements.md` Z. 27 (Backend wählen: local, S3, WebDAV, "proposed"), Z. 51 (Dateien an mehreren Orten: Aliase, `file.link`, AS2 `Collection`), Z. 53 (entfernten Speicher als lokal spiegeln mit Cache-Grenze). `design.md` Z. 47 (WebDAV "later"), Z. 61 (`opendal` nur als Möglichkeit), Z. 124 ("Zoo von Protokollen kommt als BlobBackend in den Kern, nicht ins Fenster").
- Recherche `temp/research/dateimanager.md` (fs-documentation, origin/main) Z. 52: "Änderungen von außen live: nur `rescan`, kein Watcher"; Z. 101: Watcher fehlt, `rescan` hält die Schreibsperre ("friert"); Z. 124: Protokoll-Zoo gehört in den Kern. `temp/research/dateimanager-vergleich.md`: ForkLift/Commander One/Files zeigen, dass Nutzer viele Protokolle erwarten; Spacedrive: Index plus Jobs.
- Im Sprint: Z. 89-94 (Files zeigt alles, ADR 0050; Bereichs-Downloads), Z. 68 (Files zuerst, Standardfenster), Z. 340 (`fs-files` Contract vorläufig).

### Lücke gegenüber dem Vorschlag
| Vorschlag | Stand |
|---|---|
| Themen-Schnittstelle "Speicher-Anbieter" mit Baum/Einträge/Fähigkeiten | gibt es nicht; `BlobBackend` ist Byte-Speicher, kein Baum |
| Baum über Programm-eigene Schnittstellen | nirgends vorhanden; Programme haben Listen (`list`/`query` mit Cursor), aber keinen Baum |
| Files zeigt nur an | heute nicht: `FileSource` bündelt Papierkorb, Rescan, Upload, also "mein fs-files" |
| Range | Kern ja, HTTP/Fortschritt nein |
| Watcher | Hülle `subscribe` ja (Änderungen der Objekte), Datei-Watcher fehlt |

## (b) Standards und Vorbilder (Vorbild, keine Abhängigkeit)

Hinweis: Alles unten ist nachträglich gegen `files-umfang-standards-belege.md` geprüft (Abrufdatum 2026-11-11). Ursprünglicher Hinweis: object_store und OpenDAL habe ich auf docs.rs nachgelesen (https://docs.rs/object_store/latest/object_store/trait.ObjectStore.html, https://opendal.apache.org/docs/rust/opendal/struct.Operator.html). Der Rest ist Allgemeinwissen, **nicht neu geprüft** (rclone-Seite lieferte 404).

- **WebDAV (RFC 4918, mit RFC 3253 Versionen, RFC 5323 SEARCH):** HTTP-Erweiterung: `PROPFIND` (Eigenschaften, `Depth: 0/1/infinity`), `MKCOL`, `COPY`/`MOVE`, `LOCK`, Range per HTTP (RFC 9110). Lehre: Baum = Sammlungen + Eigenschaften (`getcontentlength`, `getlastmodified`, `resourcetype`), Tiefe ist ein Parameter (wir erlauben nur Tiefe 1, wegen riesiger Bäume), Überschreiben ist `Overwrite: T/F` (wir: nie überschreiben, `OnConflict`), ~~Sperren sind Ratschläge.~~ **Laut Belegen: falsch (Beleg 5)**: WebDAV-Schreibsperren sind verbindlich, der Server verlangt das Sperr-Token (RFC 4918).
- **GVfs / KIO:** Orte sind URIs mit Schema (`smb://`, `sftp://`, `trash:///`, `recent:///`, `network:///`), Einhängen ist ein eigener Schritt (`mount` mit Rückfrage nach Zugangsdaten), Anbieter sind eigene Daemons; Datei-Info hat Attribut-Mengen, die man abfragt (`standard::*`). Lehre: **Ort = URI mit Schema, Mount/Unmount und Zustand (nicht erreichbar, Passwort gefragt) gehören zur Schnittstelle**; "virtuelle" Orte (Trash, Recent) sind gleichrangige Anbieter; KIO hat zusätzlich Job-Objekte mit Fortschritt und Abbruch. Warnung: Dolphin-Bug 451745 (Undo springt unbemerkt in einen anderen Ordner; `dateimanager.md`).
- **Solid / LDP (W3C Linked Data Platform, Solid Protocol):** Container = Ressource mit `ldp:contains`; **laut Belegen (12):** Zugriff über WAC/ACP und Solid Notifications gehören zum Solid Protocol (Community-Group-Bericht, kein W3C-Standard), nicht zum W3C-LDP, das keine Rechte-Schicht definiert. Lehre: ein Container ist selbst Ressource mit Eigenschaften; Rechte am Ort; wir brauchen RDF nicht. Eher Gegenstück zu unserer AS2-Hülle als Vorlage der Schnittstelle.
- **S3:** flach (Schlüssel + `prefix`/`delimiter` -> "common prefixes"), `ListObjectsV2` mit `ContinuationToken` (= Cursor), `GetObject` mit `Range`, Multipart, Versionen, Pre-signed URL; **kein Umbenennen/Verschieben** (nur Kopieren+Löschen) [laut Belegen (35): nicht belegbar, nicht übernehmen; belegt ist nur, dass `object_store` `rename_opts` standardmäßig als Kopieren+Löschen anbietet], Ordner sind Schein. Lehre: Fähigkeit `rename/move` als Flag, `move` darf Kopieren+Löschen sein (nicht atomar: Flag `atomicMove`), Ordner sind Präfixe.
- **SFTP (draft-ietf-secsh-filexfer-02, v3):** Handles (`opendir`/`readdir`/`close`), `stat`/`fstat`, `rename` (ohne Überschreiben), `read(handle, offset, len)`, `write`, Attribute mit Flag-Menge. Lehre: Handles für Listen (statt "alles auf einmal"), Offset-basiertes Lesen, Attribut-Flags melden, was der Server weiß; v4+ kennt Ordner `rename` mit Flags (Überschreiben, atomar).
- **SMB (MS-SMB2):** Verzeichnisse per `QUERY_DIRECTORY` mit Fortsetzung, `CHANGE_NOTIFY` (Watch), Berechtigungen als ACL, Leases/Oplocks, Server-seitiges Kopieren (`FSCTL_SRV_COPYCHUNK`). Lehre: Watch ist eine feste Fähigkeit mit Neuanfrage nach Überlauf (genau unser `ended`-Muster); serverseitig kopieren spart Verkehr (Flag `serverCopy`).
- **rclone Backend-Interface (aus Wissen):** `Fs` (List, NewObject, Put, Mkdir, Rmdir), `Object` (ModTime, Size, Open mit `RangeOption`, Update, Remove) und **optionale Schnittstellen** (`Copier`, `Mover`, `DirMover`, `PublicLinker`, `About`, `ChangeNotifier`, `PutStreamer`...) plus `Features`-Struktur, die der Anbieter beim Start meldet; Hash-Arten melden. Lehre: **Mindestkern + gemeldete Fähigkeiten**; wir haben nach ADR 0045 stattdessen "alles da, nicht möglich = Unsupported", beides lässt sich vereinen: ein Flag je Methode plus Standardantwort. Gut: Anbieter melden unterstützte Hash-Arten und `About` (Quota).
- **FUSE:** Kern-Operationen `lookup`, `getattr`, `readdir`, `read(off,size)`, `write`, `rename`, `unlink`, `mkdir`, `statfs`, Inode/Handle. Lehre: Das Betriebssystem erwartet POSIX-Semantik (Rechte, Symlinks, Sperren), also ist FUSE **ein Zugang zu** unserer Schnittstelle (später: Fremdprogramme sehen unsere Bäume), nicht deren Form. Auf Windows nur WinFsp/Dokan.
- **Nextcloud (WebDAV + OCS Files API):** WebDAV unter `/remote.php/dav/files/<user>/` mit eigenen Eigenschaften (`oc:fileid`, `oc:permissions`, `nc:has-preview`, `oc:size`); Chunked Upload v2 (`/uploads/`), Vorschau-Endpunkt `/core/preview`, Trash und Versionen als eigene DAV-Wurzeln, Freigaben über OCS `/shares`, Aktivitäten, Sync-Client über ETag (`getetag`). Lehre: **Fileid + Berechtigungs-String + "hat Vorschau" als Metadaten**, Trash/Versions als Nebenbäume (Wurzeln), Teilen getrennt von Dateien.
- **Microsoft Graph drive API:** `driveItem` (id, name, size, `file`/`folder`-Facette, `parentReference`, `lastModifiedDateTime`, `@microsoft.graph.downloadUrl`), `GET /drives/{id}/items/{id}/children` mit `@odata.nextLink`, `delta` (Änderungen ab Token = Watch ohne Push), `content` (**laut Belegen (22): `GET …/content` antwortet mit 302 auf eine vorsignierte `downloadUrl`; der `Range`-Header gehört an diese URL, Antwort 206 mit `Content-Range`, der Server darf Range ignorieren und 200 liefern**), Uploads über `createUploadSession` (fortsetzbar, Chunks), `thumbnails`, `permissions`, `versions`, Konflikte `@microsoft.graph.conflictBehavior: fail|replace|rename`. Lehre: **`delta` mit Token** ist der robusteste Watch (auch für Anbieter ohne Push); `conflictBehavior` entspricht unserem `OnConflict` ohne `replace`; "Wurzeln" sind Laufwerke (`drives`).
- **Google Drive API v3:** ~~Dateien tragen mehrere `parents`~~ **laut Belegen (24): falsch, eine Datei hat genau einen Elternordner; Verknüpfungen laufen über `shortcut`**, `mimeType` `application/vnd.google-apps.folder`, Google-Dokumente haben **keine Bytes** (nur `export` in ein Format), `shortcut` ist ein Eintrag mit Ziel, `changes.list` mit `pageToken` (Watch), `trashed`, Revisionen, `capabilities` **je Datei** (`canRename`, `canTrash`, `canDownload` ...), `quota` über `about`. Lehre (wichtig): **Fähigkeiten je Eintrag, nicht nur je Anbieter**; Programm-Ressourcen ohne Bytes brauchen `export` (genau unsere Programm-Bäume); Shortcuts = unser Link-Ordner-Problem (Mehrfach-Eltern gibt es bei Drive laut Belegen nicht).
- **`object_store` (Rust, MIT oder Apache-2.0 laut Belegen (42)):** Trait `ObjectStore` mit `put_opts`, `put_multipart_opts`, `get_opts` (`GetOptions` mit `range`, `if_match` ...), `delete_stream`, `list`, `list_with_delimiter` (eine Ebene, "common prefixes"), `copy_opts`; Rest hat Standard. Lehre: schmal, Bereich und Bedingungen (ETag) sind **Optionen eines Aufrufs**, Auflisten ist Strom, eine Ebene mit Trennzeichen. Nutzen wir schon im S3-Backend. Schmaler als nötig für Ordnerbäume (kein Umbenennen, keine Ordner).
- **OpenDAL (Rust, Apache-2.0):** `Operator` mit `stat`, `list` (+ `lister` Strom), `read` (+ `read_with` Bereich), `write`/`writer`, `delete`, `copy`, `rename`, `presign_*`; `Capability` (laut Belegen (43): gelesen über `info()`, nicht über eine Methode `capability()`) meldet, was der Dienst kann; **Layer** (`operator.layer(...)`: Retry, Timeout, Logging, Cache, Concurrency Limit, Metrics) legen Verhalten außen um jeden Dienst. Lehre: **Layer-Modell für Zeitlimit, Wiederholung, Cache, Protokoll** statt in jedem Anbieter; `Capability` als Struktur von Flags. Wir nehmen es nicht als Abhängigkeit (`fs-files/DESIGN.md:253`), aber als Muster: Decorator (ADR 0043).

Gemeinsames Muster aller: kleiner Kern (stat, list, read mit Bereich, write), **gemeldete Fähigkeiten**, **Seiten/Token**, **Delta oder Watch mit Neustart**, **Konfliktregel**, **Anbieter-Zustand (verbunden/Anmeldung nötig)**, **Fähigkeiten je Eintrag** (Drive, Nextcloud `permissions`).

## (c) Kleinste tragfähige Schnittstelle: `StorageProvider`

### Leitgedanken
1. Ein **Ort** wird als URI geschrieben, `fs://<anbieter-id>/<pfad>`; der Anbieter vergibt Pfad-Teile, die **Eintrags-Id** ist ein opaker Text (kein UUID zwingend; ein Programm-Eintrag hat seine Objekt-Id, ein WebDAV-Eintrag seinen Pfad). Pfade sind Anzeige, die Id ist Wahrheit (Drive hat Mehrfach-Eltern).
2. Alles lesen ist Pflicht (Kern: `roots`, `list`, `stat`, `read`); alles andere hat eine Standardantwort "Unsupported" (ADR 0045) **und** ein Flag (ADR 0066: Frontend zeigt gesperrt "kommt noch").
3. Der Anbieter beschreibt Orte, nicht Aussehen (ADR 0066).
4. Bereich, Seiten, Zeitlimit, Abbruch, Watch sind **Teil des Vertrags**, nicht Anbau.

### Rust-Trait (Entwurf, 10 Zeilen Kern)

```rust
#[async_trait]
pub trait StorageProvider: Send + Sync {
    fn capabilities(&self) -> StorageCaps;                    // Flags, s. u.; ein Satz je Anbieter
    async fn roots(&self) -> Result<Vec<Root>>;               // Orte: id, Name, Art (home/drive/trash/app/web), Quota
    async fn list(&self, at: &EntryId, page: PageReq) -> Result<EntryPage>;      // eine Ebene, Cursor, Sort
    async fn stat(&self, id: &EntryId) -> Result<Entry>;
    async fn read(&self, id: &EntryId, range: ByteRange, ctl: &Ctl) -> Result<ByteStream>;
    // Standard "Unsupported":
    async fn write(&self, at: &EntryId, name: &str, src: ByteSource, o: WriteOpts, ctl: &Ctl) -> Result<Entry>;
    async fn create(&self, at: &EntryId, name: &str, kind: Kind, on: OnConflict) -> Result<Entry>;
    async fn rename(&self, id: &EntryId, name: &str, on: OnConflict) -> Result<Entry>;
    async fn move_to(&self, id: &EntryId, to: &EntryId, on: OnConflict) -> Result<Entry>;
    async fn copy_to(&self, id: &EntryId, to: &EntryId, on: OnConflict, ctl: &Ctl) -> Result<Entry>;
    async fn delete(&self, id: &EntryId, how: Delete /* Trash | Purge */) -> Result<()>;
    async fn restore(&self, id: &EntryId, to: Option<&EntryId>, on: OnConflict) -> Result<Entry>;
    async fn watch(&self, at: &EntryId, l: Listener) -> Result<Subscription>;   // oder changes(since: Token)
}
```
`Ctl` trägt `deadline` (Zeitlimit, `call_limited`), `cancel` (Abbruch) und `progress` (Fortschritts-Rückruf). Kleinster Kern für ein erstes Release: `capabilities, roots, list, stat, read` (nur lesen); **Schreiben folgt je Anbieter über die Flags**.

### Cap'n Proto (Entwurf `storage.capnp`, Besitz: fs-files, Thema "Storage")

```capnp
struct StorageCaps {                 # je Anbieter; Eintrag kann sie einschränken (EntryCaps)
  create @0 :Bool; write @1 :Bool; rename @2 :Bool; move @3 :Bool; copy @4 :Bool;
  trash @5 :Bool; restore @6 :Bool; range @7 :Bool; watch @8 :Bool; versions @9 :Bool;
  share @10 :Bool; quota @11 :Bool; atomicMove @12 :Bool; serverCopy @13 :Bool;
  preview @14 :Bool; search @15 :Bool; deltaSince @16 :Bool;
}
enum EntryKind { unknown @0; file @1; folder @2; link @3; app @4; }   # link = Verweis, app = Ressource ohne Bytes
struct Entry {
  id @0 :Text;  name @1 :Text;  kind @2 :EntryKind;
  size @3 :Int64 = -1;                 # -1 = unbekannt (Ordner, Programm-Ressource)
  modified @4 :Timestamp;  mediaType @5 :Text;
  preview @6 :PreviewHint;             # keine, Bytes im Eintrag, Id eines Vorschau-Eintrags
  caps @7 :EntryCaps;                  # was HIER erlaubt ist (Drive-Muster)
  etag @8 :Text;                       # Änderungsmarke, für Bedingungen und Watch
  owner @9 :Text;                      # Programm / Anbieter, der den Eintrag besitzt (ADR 0050)
  open @10 :Text;                      # bei kind=app: AS2-IRI/Verweis zum Aufrufen im Besitzerprogramm
  envelope @11 :Envelope;              # optional: AS2-Hülle, wenn es ein Objekt ist
}
interface StorageProvider {
  supportReport @0 () -> (report :SupportReport);              # ADR 0045, wie überall
  caps    @1 () -> (caps :StorageCaps, state :ProviderState);  # state: ready | needsLogin | offline | readOnly
  roots   @2 () -> (roots :List(Root));
  list    @3 (at :Text, cursor :Cursor, sort :Sort) -> (page :EntryPage);
  stat    @4 (id :Text) -> (entry :Entry);
  open    @5 (id :Text) -> (blob :Blob);                       # Blob.read(offset,length) gibt es schon
  write   @6 (at :Text, name :Text, mediaType :Text, onConflict :OnConflict) -> (upload :Upload);  # Upload wie in files.capnp
  create  @7 (at :Text, name :Text, kind :EntryKind, onConflict :OnConflict) -> (entry :Entry);
  rename  @8 (id :Text, name :Text, onConflict :OnConflict) -> (entry :Entry);
  move    @9 (id :Text, to :Text, onConflict :OnConflict) -> (entry :Entry);
  copy    @10 (id :Text, to :Text, onConflict :OnConflict) -> (entry :Entry);
  delete  @11 (id :Text, purge :Bool) -> ();
  restore @12 (id :Text, to :Text, onConflict :OnConflict) -> (entry :Entry);
  watch   @13 (at :Text, listener :ChangeListener) -> (subscription :Subscription);
  changes @14 (since :Data) -> (changes :List(Change), token :Data);  # Delta für Anbieter ohne Push (Graph/Drive)
  types   @15 () -> (catalog :TypeCatalog);                    # ADR 0066: Befehle mit supported
}
```
Alle Ordinale nur anhängen. Neue Flags kommen ans Ende (ADR 0045: nach 1.0 nur Sprünge).

### Wurzeln und Orte
`Root{id, name, kind (home|drive|trash|recent|app|web|link), provider, readOnly, quotaUsed, quotaTotal}`. Ein Anbieter hat eine oder mehrere Wurzeln; Orte wie Home, USB, DAV, S3, fremder Rechner sind je ein **Anbieter-Exemplar** in der Registry (`BackendRegistry` ist das Vorbild, `registry.rs:22`). Virtuelle Orte (Papierkorb aller Anbieter, "Zuletzt", Link-Ordner) sind Anbieter für sich.

### Eintrags-Metadaten
Name, Art, Größe (`-1` = unbekannt), geändert, Mimetyp, `etag`, `caps`, Vorschau-Hinweis (`none | inline | child(id)`, Muster: Nextcloud `has-preview`, Graph `thumbnails`), `owner`, `open` (Aufruf). Programm-Eigenes (Aufgabe: Status, Fälligkeit) kommt nicht in `Entry`, sondern über `types` (ADR 0066) und über den Besitzer: Files zeigt nur Name, Art, Zeit, Symbol.

### Fehlermodell
RFC 9457 wie überall (`Problem`), Typen unter `https://freesynergy.net/problems/storage/…`: übernehmen `name-conflict`, `invalid-name`, `not-found`, `unsupported` (501), `backend-failed`; **neu:** `offline` (503), `needs-login` (401), `forbidden` (403), `timeout` (504), `cancelled` (499), `too-large` (existiert), `quota-exceeded` (507), `changed` (412, `etag` stimmt nicht), `cycle` (508, Link-Zyklus). `FileProblem` (`error.rs:10`) bekommt dieselben Werte.

### Auth und Tresor (ADR 0067)
Die Anbieter-Konfiguration (`backend.add`, `files.capnp:197`) darf **nie ein Geheimnis enthalten**, sondern `credential: <Tresor-Verweis>` (`vault://<id>`). Der Anbieter holt das Geheimnis bei Bedarf selbst vom Tresor (Secret Service unter Linux, Credential Manager unter Windows, ADR 0067 Z. 12). Ohne Zugang meldet `caps().state = needsLogin`, nicht ein Fehler beim Auflisten. `S3Backend` hat schon "Zugangsdaten nie in Debug oder Fehlern" (DESIGN); heute stehen sie noch in der Konfiguration, das ist der erste Umbau. Für Rechte: Anbieter handelt **im Namen des angemeldeten Menschen**, nie mit Allgemeinrechten (siehe Risiken).

### Zeitlimits, Fortschritt, Abbruch, Seiten
- Jeder Aufruf hat ein Zeitlimit (Vorgabe, Anbieter-abhängig: `list` 10 s, `stat` 5 s, `read` Verbindung 10 s, Daten ohne Limit mit Fortschritt). Technik: `call_limited` aus fs-interfaces (v0.0.18, vorhanden).
- Fortschritt/Abbruch: lange Aufgaben (copy, write, recursive delete) sind **Jobs** (yazi-/KIO-Muster): Aufruf liefert `JobId`, Fortschritt per Strom, `cancel(job)`. Für `read` genügt `Blob.read` pro Bereich; Abbruch heißt: nicht mehr lesen.
- Seiten: `Cursor` wie bei allen Listen (`common.capnp`), Standardgröße 200-1000, Sortierung am Anbieter oder gemeldet (`sort` in Flags). `list` kennt **nie** "alles rekursiv".

### Watch
Zwei Wege, beide unter einer Fähigkeit: `watch(at, listener)` (Push; `ChangeListener` mit `ended` wie `common.capnp:91`; bei `ended` neu abonnieren und neu lesen) und `changes(since token)` (Delta, wie Graph `delta`/Drive `changes`). Ein Anbieter ohne beides: Files fragt alle N Sekunden `stat` des offenen Ordners (Etag) oder zeigt "Aktualisieren". Das löst den heutigen Engpass "nur `rescan`" (`dateimanager.md` Z. 52, 101), sofern der Lokal-Anbieter `notify` (inotify) nutzt.

### Wie Programme "als Baum" liefern (ADR 0050, nie aus der Datenbank)
Jedes Programm bietet **neben** seiner Fachschnittstelle ein dünnes `StorageProvider` an (oder `fs-files` baut den Adapter über die **öffentliche Schnittstelle** des Besitzers, z. B. `tasks.capnp` `query`/`get`, nie über dessen Datenbank). Die Abbildung ist eine Entscheidung des **Besitzers**, nicht von Files (Point of Truth):

| Programm | Wurzel | Baum | Eintrag (`kind=app`) |
|---|---|---|---|
| fs-people | "Personen" | Facetten: Kontakte, Nutzer, KIs, Partner -> Karten (Buchstaben oder Gruppen) | Person (JSContact `.jscontact`, Export: vCard); `open` = Person im Contacts-Frontend |
| fs-tasks | "Aufgaben" | Projekt -> Liste -> Aufgabe | Aufgabe (`.jstask`), Export ICS |
| fs-calendar | "Kalender" | Kalender -> Jahr -> Monat -> Ereignis | Ereignis (`.jsevent`), Export ICS |
| fs-wiki | "Wiki" | Bereich -> Seite -> Unterseite (Baum ist echte Gliederung) | Text (Markdown-Export) |
| fs-maps | "Orte" | Ebene -> Orte | GeoJSON-Objekt |
| fs-messenger | "Chats" | Raum -> Tag -> Nachricht/Anhang | Anhänge als echte Dateien (`kind=file`, `read` gibt Bytes) |
| fs-groups, fs-whiteboard, fs-surveys | je Programm | je Programm | Objekt |
| Website | "Webseite <host>" | Baum aus `sitemap.xml`, sonst nach Pfad, **nur lesend** | Seite (`text/html`), Medien als Dateien |

Regeln: (1) `read` eines `app`-Eintrags liefert die **Export-Darstellung im Standardformat** des Besitzers (JSContact JSON, JSCalendar JSON, Markdown); sie ist abgeleitet, nicht die Wahrheit (ADR 0030, 0046). (2) Schreiben auf `app`-Einträge heißt **Fachbefehl des Besitzers** (Umbenennen einer Aufgabe = `task.update`), nie Dateischreiben; `caps` des Eintrags zeigt, was geht. (3) Datenschutz: `sensitive`/`to` der Hülle gilt weiter (ADR 0029): Files zeigt nichts, was der Besitzer dem Menschen nicht zeigt. (4) Löschen ruft `Delete` des Besitzers.

### Wie Files nur anzeigt und aufruft
Files hält **keine Wahrheit**: Registry der Anbieter-Exemplare (`StorageRegistry`, vom Muster `BackendRegistry`), Zustand der Ansicht, Auswahl. Aktionen gehen als Befehle an den Besitzer des Eintrags (`Entry.owner`/`open`):
- Doppelklick auf `kind=file`: Standardprogramm oder Vorschau (`read` mit Bereich).
- Doppelklick auf `kind=app`: ruft das **Besitzerprogramm** mit Id auf (`fs-tasks open <iri>`, ADR 0063) statt eine Datei zu öffnen.
- Ziehen/Kopieren zwischen Anbietern: Files liest `read` des Quell- und `write` des Zielanbieters (Strom, kein Zwischenspeicher), oder `copy` im selben Anbieter (Flag `serverCopy`).
- Menüs und gesperrte Elemente kommen aus `caps` und dem `TypeCatalog` (ADR 0066), kein Code je Anbieter im Fenster.
- Das Fenster selbst ist reine Component (ADR 0066 "keine Darstellung im Programm"); `FileSource` wird zu einem Adapter und verliert Papierkorb-/Upload-Besonderheiten (sie werden `Root{kind: trash}` bzw. Anbieter-Zustand "pendingUploads").

### Mapping zu AS2 und Undo
Jede ändernde Handlung wird (wie in ADR 0020 Z. 11-12) eine **Aktivität** im Protokoll des Besitzers (`fs-history`, `fs-objects`): `Create`, `Update` (rename), `Add`/`Remove` (move: `Remove` aus altem Ordner + `Add` in neuen, mit `origin`/`target`), `Delete` (Papierkorb, `trashed`), `Undo` (Wiederherstellen/Verschieben zurück). Ein Eintrag hat IRI und Hülle nur, wenn der Anbieter Objekte führt (fs-files, Programme); bei WebDAV/S3 ist die Aktivität **lokal** (Files-Sicht), `object` = Anbieter-URI. Undo-Regeln aus `dateimanager.md`: Aufzählbare Liste mit Klartext, Undo sagt, **was und wo**, und springt dorthin (Lehre Dolphin 451745). `purge` ist nicht rückgängig und sagt das vorher. Ein Anbieter ohne `trash` kann kein Undo für Löschen versprechen (Flag).

### Mapping zu Bereichs-Downloads (Medien)
- Kern: `Blob.read(offset, length)` (`common.capnp:35`) und `BlobBackend.get(key, offset, length)` (`provider.rs:41`), S3 `get_range` (`s3/api.rs:28`). Der Anbieter meldet `range`; ohne `range` liest Files ganz (oder cached).
- Neu zu bauen: ein **HTTP-Zugang** (lokal oder im Server `fs-files serve`): `GET /storage/<provider>/<id>` mit `Range: bytes=a-b` -> `206 Partial Content`, `Accept-Ranges: bytes`, `ETag`/`If-Range`, `Content-Type`; mit Token des Menschen. Ein Player (Blinc-Videokomponente, Browser, VLC) spielt sofort ab, weil er nur die Anfangsbereiche holt und springt (MP4 `moov` am Anfang oder Ende: zwei Bereichs-Anfragen).
- Grenze: **kein** Live-Strom, keine Segmente, keine Transkodierung, keine Mitschnitte; das ist `fs-streaming` (`streaming.capnp`, Sprint Z. 94). Files liefert Bytes eines **vorhandenen** Eintrags; fs-streaming veröffentlicht einen Eintrag ggf. aus einer Files-Quelle (WHEP/HLS), liest ihn dazu über `read`. Eine gemeinsame Regel: Files hat keine Codecs und kein Zeitverhalten (Pufferung nur Lesevorgriff).

## (d) Risiken und Gegenvorschläge

1. **Rechte und Datenschutz.** Files liest "für" den Menschen; ein Server-Files darf nie mit Dienstrechten alles zeigen. *Gegenvorschlag:* jeder Aufruf trägt die Identität des Menschen (Capability/Token); der Besitzer prüft (ADR 0050: Rechte beim Besitzer, `to/cc/audience`, `sensitive` ADR 0029). Fremde Rechner: nur auf **ausdrückliche Freigabe des Eigentümers** (Einladung, ADR 0059 iroh, Freigabe beim Eintritt), Standard ist "nur lesen", Protokoll jedes Zugriffs im `fs-history` des Eigentümers, Ende-zu-Ende nach ADR 0067 (Server sieht nur Zeichensalat; Suche auf dem Gerät: Files sagt es, statt still weniger zu finden). Caches fremder Inhalte verschlüsselt, mit Größengrenze und Löschknopf.
2. **Offline-Anbieter.** Anbieter wechselt jederzeit auf `offline`/`needsLogin`. *Gegenvorschlag:* `ProviderState` als Teil von `roots`/`caps`; Zeitlimit statt Hängen; Files zeigt letzten bekannten Stand (Cache, markiert "alt") und sperrt Schreiben; Warteschlange für Schreibaufträge nur, wenn der Nutzer es einschaltet (sonst überrascht Nachträgliches). USB/Netz erscheinen und verschwinden: Mount-Ereignisse als Registry-Änderung (Hot-Plug, ADR 0045).
3. **Riesige Bäume.** `list` nur eine Ebene mit Cursor; keine rekursive Zählung/Größe ohne Auftrag; Ordnergrößen "unbekannt" (`-1`); virtuelles Scrollen im Fenster (Sprint: >10 000 Einträge zu messen, `dateimanager.md` Z. 148); Suche **im Anbieter** (Flag `search`) statt im Fenster; flache Ansicht nur als Job mit Obergrenze.
4. **Zyklen bei virtuellen Link-Ordnern.** Link-Ordner (`kind=link`, Drive-Shortcut, AS2 `Collection`, `requirements.md` Z. 51) können in sich zeigen oder in einen eigenen Elternordner. *Gegenvorschlag:* Links sind **Einträge mit Ziel**, die Files nie automatisch rekursiv auflöst; beim Betreten ein "Besucht"-Satz (Ids) und Tiefengrenze (z. B. 32), bei Treffer `cycle`-Problem; rekursive Operationen (copy, delete) folgen Links **nie**, sie wirken auf den Link; Mehrfach-Eltern gelten als Link, nicht als Baum (Drive).
5. **Abgrenzung zu fs-streaming.** Gefahr: "damit Medien sofort abspielen" wächst zu Wiedergabe. *Regel:* Files liefert Bereiche, fs-streaming macht Zeit/Segmente/Live; Schnittstellen sind getrennt, nur `read` ist die Naht. Vorschaubilder (Frame) sind Sache von "Metadaten-Extraktoren" (`interfaces/index.md`), nicht von Files.
6. **Programm-Bäume täuschen Dateien vor.** Ein Mensch erwartet bei "Kopieren" einer Aufgabe nach USB eine Datei; Löschen im falschen Baum löscht Aufgabe. *Gegenvorschlag:* `kind=app` sichtbar gekennzeichnet, `caps` ehrlich, Kopieren nach außen = **Export** (ADR 0046), Löschen fragt im Besitzer-Sinn nach, Papierkorb des Besitzers statt dem von Files.
7. **Zwei Wahrheiten bei fs-files.** Eigene Dateien haben Datenbank + Backend (Ids, Hülle, Papierkorb). `fs-files` als Anbieter zu sehen heißt: der Adapter spricht `Files`/`Folders` (nicht `BlobBackend`), damit die DB-Wahrheit bleibt. Ein WebDAV/S3-Verzeichnis **außerhalb** von fs-files hat keine Hülle: Files darf dafür keine Objekte anlegen, außer der Mensch "übernimmt" es (heute `rescan`/Import).
8. **Anbieter-Schnittstelle zu breit/fest zu früh.** ADR 0045 verlangt zwei Anbieter vor 1.0: Entwurf zuerst mit `LocalFolder` und S3-Lesen, dann WebDAV; die kleine Lese-Schnittstelle zuerst festlegen. Gegen den Zoo: Protokolle als **Hot-Plugins** (Agenten-Prozesse, ADR 0045 Z. 20), nicht im Kern.
9. **Sicherheit der Anbieter.** SSRF (Anbieter-URL zeigt auf interne Adressen), Pfad-Traversierung (`..`, Symlinks: bestehende Regeln `key.rs`, `confined.rs`), Namen mit Steuerzeichen, Zeitstempel/Größe lügen. *Gegenvorschlag:* gleiche Namensregeln wie `files.capnp` Z. 11-17 für alle Anbieter, Namen-Normalisierung vor Anzeige, Anbieter in eigenem Prozess mit eigener Rechtebeschränkung.
10. **Mehrere Wahrheiten über Namen.** Verschiedene Anbieter ordnen Groß/Klein, Unicode-Normalform, Länge unterschiedlich: Konflikt kann erst beim Schreiben auffallen -> `name-conflict` mit `detail`; `keepBoth` bleibt, **kein `replace`** (wie heute, `files.capnp:57-62`).

### Offene Fragen an den Nutzer (≤ 5)
1. **Reihenfolge:** Erst nur Lesen aller Orte (Home, USB, DAV, S3, Programme) und Schreiben später, oder Lokal+S3 schreibend zuerst (heute schon da)? Vorschlag: Lesen zuerst.
2. **Fremde Rechner:** Nur auf ausdrückliche Einladung des Eigentümers, standardmäßig nur lesend, mit Protokoll beim Eigentümer. Stimmt das, oder soll es auch eigene Rechner ohne Einladung geben (SSH/SFTP mit eigenen Zugangsdaten aus dem Tresor)?
3. **Programm-Bäume:** Soll Schreiben (Aufgabe verschieben, Ereignis umbenennen) schon in Files gehen, oder zeigt Files zuerst nur an und öffnet im Besitzerprogramm? Vorschlag: nur anzeigen und aufrufen.
4. **Websites:** Nur lesen, eigene Seiten (die wir hosten, z. B. aus `fs-wiki`) oder auch **fremde** (Crawl über `sitemap.xml`, Abwägung Datenschutz, Last auf dem Zielserver)? Vorschlag: nur eigene und per Einladung geteilte.
5. **Offline-Cache:** Dürfen Inhalte fremder Anbieter lokal zwischengespeichert werden (verschlüsselt, mit Grenze)? Ohne Cache gibt es keinen Offline-Zugriff und Medien starten langsamer.

## (e) Aufwand in Schritten und Repos

| Schritt | Inhalt | Repo(s) | Größe |
|---|---|---|---|
| S1 | Schema `storage.capnp` (Entwurf, Orte, Entry, Caps, Probleme, `changes`) + Doku `docs/en/interfaces` (Zeile "File storage" zu Thema "Storage" erweitern); ADR "Speicher-Anbieter" (kurz, mit Bezug 0045, 0050, 0066) | fs-interfaces, fs-documentation | klein |
| S2 | Rust-Trait `StorageProvider` + Null-Objekt, `StorageRegistry` (Muster `BackendRegistry`), `Ctl` (Frist, Abbruch, Fortschritt) | fs-files (`fs-files-core`) oder neues Crate `fs-storage` (Entscheidung: Trait gehört in `fs-interfaces`, wenn zwei Programme ihn umsetzen, wegen ADR 0050 nur ein Besitzer, also fs-files) | mittel |
| S3 | Zwei erste Anbieter, nur lesend: Lokaler Ordner (frei, auch außerhalb fs-files; Namen-/Symlink-Regeln aus `local/`), S3 (`object_store::list_with_delimiter`, `get_opts` mit Bereich) | fs-files | mittel |
| S4 | Adapter `fs-files` selbst als Anbieter (über `Files`/`Folders`, mit Papierkorb als Wurzel); `FileSource` wird Adapter, `FileCapabilities`/`FileProblem` erweitert (range, watch, offline ...), asynchron statt Oberflächen-Faden | fs-components, fs-files | mittel |
| S5 | HTTP-Zugang mit `Range`/206/ETag + Token; Test mit echtem Player (Video, Audio) | fs-files (Server) | klein-mittel |
| S6 | Schreibweg: `write` (Upload-Muster aus `files.capnp:167`), `create/rename/move/copy/delete/restore`, `OnConflict`, Jobs mit Fortschritt/Abbruch | fs-files | mittel |
| S7 | Watch: inotify/ReadDirectoryChangesW für lokal, `changes(token)` für entfernte; Ersatz für nur-`rescan` | fs-files | mittel |
| S8 | Anbieter WebDAV (zweiter Entwurfs-Anbieter nach ADR 0045), Tresor-Verweis für Zugangsdaten (`fs-vault`, ADR 0067; bis dahin Platzhalter-Schnittstelle) | fs-files, fs-vault | mittel |
| S9 | Programm-Bäume: je Programm ein dünner Baum-Dienst über die eigene Schnittstelle (zuerst `fs-tasks`, `fs-wiki`, dann `fs-people`, `fs-calendar`) mit Export im Standardformat; `open` im Besitzerprogramm | fs-tasks, fs-wiki, fs-people, fs-calendar, … | je klein, zusammen groß |
| S10 | Virtuelle Orte: Link-Ordner (Zyklen-Schutz), Papierkorb-aller, Zuletzt; Websites (nur lesend) | fs-files | mittel |
| S11 | Frontend: Fenster zeigt jede Wurzel, Menüs aus `caps`/`TypeCatalog`; gesperrt "kommt noch"; Fortschritts-/Abbruch-Leiste | fs-components (Component), fs-files (Frontends) | groß |
| S12 | Optional: FUSE/WinFsp als Zugang nach außen, SFTP/SMB-Anbieter als Hot-Plugins | eigene Repos `fs-files-<anbieter>` | später |

Abhängigkeiten: S1 -> S2 -> S3 -> S4 (die ersten sichtbaren Orte); S5 unabhängig nach S3; S6 und S7 nach S4; S8 braucht `fs-vault` (noch nicht gebaut: bis dahin Konfiguration ohne Geheimnis nicht möglich, nur öffentliche Quellen); S9 nach S2. `call_limited` (fs-interfaces v0.0.18) liefert die harten Zeitlimits.

Schwerpunkt-Entscheidung zum Mitnehmen: **eigene `StorageProvider`-Schnittstelle neben `BlobBackend`** (`BlobBackend` bleibt der Byte-Speicher unter fs-files, geht nicht auf), nicht `BlobBackend` erweitern, nicht `opendal` einbinden (Begründung `fs-files/DESIGN.md:253`).
