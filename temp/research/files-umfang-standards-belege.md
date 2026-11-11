# Standards-Belege zum Befund „Umfang von Files und StorageProvider“

Stand: 2026-11-11 (Abrufdatum aller Quellen). Nur gelesen, keine Repo-Änderungen. Gehört zu `files-umfang.md` (dort Abschnitt b). Status je Aussage: belegt / teilweise / falsch / nicht belegbar.

---

## WebDAV

**1. "WebDAV (RFC 4918, mit RFC 3253 Versionen, RFC 5323 SEARCH)"**
- Status: belegt.
- Korrektur: RFC 4918 ist ein Proposed Standard von Juni 2007 (Dusseault, Ed.); er ersetzt RFC 2518 und wurde durch RFC 5689 ergänzt. RFC 3253 ("Versioning Extensions to WebDAV") stammt von März 2002. RFC 5323 ("WebDAV SEARCH") stammt von November 2008.
- Quelle: https://www.rfc-editor.org/rfc/rfc4918 ; https://www.rfc-editor.org/rfc/rfc3253 ; https://www.rfc-editor.org/rfc/rfc5323
- Lizenz: RFC-Texte sind IETF-Dokumente; Nutzung nach IETF-Bedingungen, nicht geprüft.

**2. PROPFIND mit Depth 0/1/infinity**
- Status: belegt.
- Korrektur: Der Client sendet Depth 0, 1 oder infinity. Der Server muss 0 und 1 unterstützen, infinity soll er unterstützen. Ohne Depth-Header gilt infinity.
- Quelle: https://www.rfc-editor.org/rfc/rfc4918 (Abschnitt 9.1)

**3. "Überschreiben ist Overwrite: T/F" (COPY/MOVE)**
- Status: belegt.
- Korrektur: Der Header Overwrite hat T oder F, Standard ist T (Abschnitt 10.6; Wirkung in 9.8.4 und 9.9.3).
- Quelle: https://www.rfc-editor.org/rfc/rfc4918

**4. "MKCOL" und "COPY/MOVE"**
- Status: belegt (Existenz). Die Detailtexte wurden nur teilweise gelesen.
- Quelle: https://www.rfc-editor.org/rfc/rfc4918 (MKCOL Abschnitt 9.3)

**5. "Sperren sind Ratschläge"**
- Status: **falsch**.
- Korrektur: Eine Schreibsperre in WebDAV verhindert Änderungen durch andere Akteure als den Sperr-Inhaber. Der Server muss das Sperr-Token für Änderungen an gesperrten Ressourcen verlangen. Also: serverseitig erzwungen, nicht bloß beratend.
- Quelle: https://www.rfc-editor.org/rfc/rfc4918 (Sperr-Abschnitte; Stichprobe, nicht vollständig gelesen)

**6. "Range per HTTP (RFC 9110)"**
- Status: belegt.
- Korrektur: RFC 9110 (HTTP Semantics, STD 97, Copyright 2022) definiert 206 Partial Content (Abschnitt 6.4.1) und If-Range (Abschnitt 13.1.5): Bei passendem Validator wird Range beachtet, sonst die volle Darstellung gesendet. Range-Abschnitte selbst im Volltext nicht gelesen.
- Quelle: https://www.rfc-editor.org/rfc/rfc9110

**7. "Tiefe ist ein Parameter" / "Tiefe 1 erlauben"**
- Status: belegt als Eigenschaft des Protokolls; "wir erlauben nur Tiefe 1" ist eine Designentscheidung, keine Standardaussage.

---

## GVfs / KIO

**8. GVfs: URI-Schemata smb://, sftp://, trash:///, recent:///, network:///**
- Status: **teilweise**.
- Korrektur: Die Schema-Tabelle im GNOME-Wiki stammt aus einem alten Stand ("Supported schemes by GVfs 1.37.90"); die Wiki-Seite ist laut Hinweis eingestellt. trash:///, recent:/// und network:/// tauchen dort auf (network:/// fasst smb:// und dns-sd:// zusammen). smb:// und sftp:// wurden nicht gegen eine aktuelle Quelle geprüft.
- Quelle: https://wiki.gnome.org/Projects/gvfs/schemes (eingestellt, Stand 1.37.90, nur über Suchergebnis gesehen); https://gitlab.gnome.org/GNOME/gvfs (Projektseite, bestätigt: "Virtual filesystem implementation for GIO", LGPL-2.0-only)
- Lizenz: GVfs LGPL-2.0-only (Projektseite).

**9. GVfs: "Einhängen (mount) ist eigener Schritt", "Anbieter sind eigene Daemons"**
- Status: **nicht belegbar** im gelesenen Material. Ein Hinweis auf den Prozess gvfsd-trash (Trash-Backend) kam nur aus einem Suchauszug.
- Quelle: https://wiki.gnome.org/Projects/gvfs/schemes (Suchauszug)

**10. KIO: Worker/"Slaves", KIO::stat und listDir, Job-Objekte mit Fortschritt und Abbruch**
- Status: **teilweise**.
- Korrektur: Die Klassen SlaveBase (älterer Name) und WorkerBase (neuerer Name) sind in der API-Doku belegt. kio_smb überschreibt listDir und stat (laut Quellindex). Job-Fortschritt und Abbruch als KIO-Muster wurden nicht belegt; die Seite api.kde.org/.../classKIO_1_1WorkerBase.html war nicht abrufbar (404).
- Quelle: https://api.kde.org/frameworks/kio/html/classKIO_1_1SlaveBase.html (Suchtreffer); https://sources.debian.org/src/kio-extras/4:25.04.2-1/smb/kio_smb.h (Quelltext-Header, Sekundärquelle)
- Lizenz: KIO LGPL (nicht geprüft im Detail).

---

## Solid / LDP

**11. "Container = Ressource mit ldp:contains"**
- Status: belegt.
- Korrektur: LDP 1.0 ist W3C Recommendation vom 26.02.2015. Container sind LDP-RS-Ressourcen; enthaltene Dokumente sind per Containment-Triple `ldp:contains` verknüpft.
- Quelle: https://www.w3.org/TR/ldp/
- Lizenz: W3C-Dokumentlizenz, nicht geprüft.

**12. "Zugriff über WAC/ACP" (der Befund ordnet das LDP zu)**
- Status: **teilweise / falsch in der Zuordnung**.
- Korrektur: WAC und ACP sind im Solid Protocol beschrieben, nicht im W3C-LDP-Dokument. LDP definiert keine Rechte-Schicht.
- Quelle: https://solidproject.org/TR/protocol (Solid Protocol 0.11.0, Draft Community Group Report vom 12.05.2024, kein W3C-Standard)

**13. "Benachrichtigungen (Solid Notifications)"**
- Status: belegt (im Solid Protocol referenziert, Rollen Resource Server, Subscription Server, Notification Sender/Receiver).
- Quelle: https://solidproject.org/TR/protocol

**14. "Ein Container ist selbst Ressource mit Eigenschaften"**
- Status: belegt (Container sind LDP-Ressourcen).

---

## SFTP (draft-ietf-secsh-filexfer)

**15. "draft-ietf-secsh-filexfer-02, v3": Handles opendir/readdir/close, read mit Offset, Attribut-Flags**
- Status: belegt.
- Korrektur: Draft -02 nennt sich Protokollversion 3. Enthalten: SSH_FXP_OPENDIR, SSH_FXP_READDIR, SSH_FXP_READ mit uint64-Offset, Attribut-Flags (SIZE, UIDGID, PERMISSIONS, ACMODTIME, EXTENDED). Rename: Fehler, wenn der Zielname existiert (kein eigenes Flag).
- Quelle: https://www.ietf.org/archive/id/draft-ietf-secsh-filexfer-02.txt
- Hinweis: Es handelt sich um einen abgelaufenen Internet-Draft (kein RFC). Datatracker-Seite: https://datatracker.ietf.org/doc/draft-ietf-secsh-filexfer/ (als abgelaufen markiert).

**16. "v4+ kennt Ordner-rename mit Flags (Überschreiben, atomar)"; "Version 6"**
- Status: **teilweise**.
- Korrektur: Draft -13 nennt Protokollversion 6 und definiert Rename-Flags SSH_FXF_RENAME_OVERWRITE, SSH_FXF_RENAME_ATOMIC, SSH_FXF_RENAME_NATIVE (Abschnitt 8.3). Version 4 und 5 wurden nicht einzeln gelesen. Das Datatracker-Eintrag zu -13 nennt 2006-07-18.
- Quelle: https://www.ietf.org/archive/id/draft-ietf-secsh-filexfer-13.txt

---

## SMB (MS-SMB2)

**17. QUERY_DIRECTORY mit Fortsetzung, CHANGE_NOTIFY, ACL, Leases/Oplocks, FSCTL_SRV_COPYCHUNK**
- Status: **teilweise / nicht belegbar im Detail**.
- Korrektur: Das Dokument existiert und ist aktuell (Revision 88.0, 28.09.2026; Titel "Server Message Block (SMB) Protocol Versions 2 and 3"). Die Übersichtsseite listet die Befehle nicht. Einzelne Abschnitte wurden nicht geöffnet, daher bleibt die Befehlsliste unbestätigt.
- Quelle: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-smb2/5606ad47-5ee0-437a-817e-70c366052962
- Lizenz: Microsoft Open Specifications; laut IP-Hinweis darf man Kopien zur Implementierung anfertigen, Patente sind separat zu prüfen.

---

## Nextcloud

**18. Chunked Upload v2 (Ordner /uploads/, Chunks per PUT, Abschluss per MOVE)**
- Status: belegt.
- Korrektur: Das Dokument nennt "Chunked upload v2" als empfohlene Version. Ablauf: MKCOL-Ordner unter dav/uploads/<userid>, nummerierte Chunks per PUT, Abschluss per MOVE der Datei ".file". MKCOL, PUT und MOVE benötigen einen Destination-Header. Die Release-Version, in der v2 eingeführt wurde, nennt die Seite nicht.
- Quelle: https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/chunking.html (Abruf 2026-11-11)
- Lizenz: Nextcloud-Dokumentation; Nutzungsbedingungen nicht geprüft.

**19. Eigenschaften oc:fileid, oc:permissions, nc:has-preview, oc:size, getetag**
- Status: belegt.
- Korrektur: getetag wird standardmäßig geliefert. Die anderen vier nur, wenn sie im PROPFIND-Body angefordert werden. Depth: 0 liefert nur den Knoten selbst.
- Quelle: https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/basic.html

**20. Pfad /remote.php/dav/files/<user>/; Trash und Versionen als eigene DAV-Wurzeln; /core/preview; OCS /shares**
- Status: **nicht belegt** (Pfad, Trash/Versionen-Wurzeln, Preview-Endpunkt, OCS-Shares nicht in den gelesenen Abschnitten bestätigt; die Index-Seite nennt nur "Trashbin" und "Versions" als Unterseiten).
- Quelle: https://docs.nextcloud.com/server/latest/developer_manual/client_apis/WebDAV/index.html

---

## Microsoft Graph (driveItem)

**21. delta mit Token (Änderungen ab Token)**
- Status: belegt.
- Korrektur: Aufruf ohne Token liefert den vollen Stand, mit @odata.nextLink weiter blättern, am Ende @odata.deltaLink speichern. Bei zu altem Token kommt HTTP 410 Gone mit einem Neustart-Link (resync-Fehler). Gelöschte Einträge kommen mit der Facette "deleted". Remarks: Items nach ID verfolgen, nicht nach Pfad.
- Quelle: https://learn.microsoft.com/en-us/graph/api/driveitem-delta?view=graph-rest-1.0 (Abruf 2026-11-11)
- Hinweis zum Befund: "Watch ohne Push" passt (Polling mit Token, kein Push).

**22. "content mit Range"**
- Status: **falsch** in der Form, wie der Befund es sagt.
- Korrektur: GET .../content antwortet mit 302 auf eine vorsignierte downloadUrl. Der Range-Header muss an diese URL gesendet werden, nicht an /content. Die Antwort ist 206 mit Content-Range; der Server darf den Range ignorieren und 200 liefern.
- Quelle: https://learn.microsoft.com/en-us/graph/api/driveitem-get-content?view=graph-rest-1.0 (Abschnitt "Partial range downloads")

**23. createUploadSession: fortsetzbar, Chunks; conflictBehavior fail|replace|rename**
- Status: belegt, mit Ergänzungen.
- Korrektur: Fragmente müssen in Reihenfolge kommen; jede Anfrage höchstens 60 MiB; Fragmentgrenzen ein Vielfaches von 320 KiB. conflictBehavior hat drei Werte, darunter replace. Der Befund sagt "entspricht OnConflict ohne replace": der Vergleich stimmt, nur die API selbst hat replace.
- Quelle: https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession?view=graph-rest-1.0 (Abruf 2026-11-11)

---

## Google Drive API v3

**24. "Dateien tragen mehrere parents (Mehrfach-Elternschaft! kein Baum)"**
- Status: **falsch** (laut aktueller Referenz).
- Korrektur: Laut Files-Referenz hat eine Datei nur einen Elternordner; mehrere Eltern werden nicht unterstützt. Der Befund beschreibt einen älteren Stand oder einen Irrtum. Für die Entscheidung: Ein Baum mit genau einem Elternteil ist aktuell der Fall; Verknüpfungen laufen über shortcut.
- Quelle: https://developers.google.com/workspace/drive/api/reference/rest/v3/files (Abruf 2026-11-11)

**25. mimeType folder "application/vnd.google-apps.folder"**
- Status: **nicht belegt** im gelesenen Text (Seite nennt den Wert nicht).

**26. Google-Dokumente haben keine Bytes, nur export**
- Status: **teilweise**.
- Korrektur: files.export exportiert Workspace-Dokumente in ein gewähltes MIME-Format. webContentLink und md5Checksum gelten nur für Binärdateien. Dass alt=media bei Google-Dokumenten fehlschlägt, stammt aus Community-Quellen, nicht aus der offiziellen Referenz.
- Quelle: https://developers.google.com/workspace/drive/api/reference/rest/v3/files (Abruf 2026-11-11)

**27. shortcut ist ein Eintrag mit Ziel**
- Status: belegt (shortcutDetails mit targetId; mimeType application/vnd.google-apps.shortcut).

**28. capabilities je Datei (canRename, canTrash, canDownload)**
- Status: belegt (per-file output-only booleans).

**29. changes.list mit pageToken (Watch)**
- Status: belegt. nextPageToken bei Fortsetzung, newStartPageToken am Ende.
- Korrektur: Ob getStartPageToken zwingend der erste Aufruf ist, sagt die Seite nicht. Sie nennt es als eine von zwei Quellen für den pageToken.
- Quelle: https://developers.google.com/workspace/drive/api/reference/rest/v3/changes/list (Abruf 2026-11-11)

**30. files.list mit Seiten/Token**
- Status: **nicht belegt** auf der Files-Seite (dort fehlt pageToken im gelesenen Text). Müsste auf der files.list-Seite geprüft werden.

**31. Range-Download bei Google Drive**
- Status: **nicht offiziell belegbar**, nur Community-Quellen.
- Korrektur: Die Suche fand Hinweise, dass files.get mit alt=media und Range-Header 206 liefert. Eine offizielle Drive-Aussage fand ich nicht (die Range-Doku in der Suche betrifft die Chat-API). Die Python-Bibliothek MediaIoBaseDownload ignoriert einen eigenen Range-Header (Community).
- Quelle: Suchergebnisse (z. B. https://developers.google.com/drive/manage-downloads, nicht im Detail gelesen); Community-Quellen nur als Hinweis.

---

## Amazon S3

**32. ListObjectsV2 mit ContinuationToken (= Cursor), prefix/delimiter -> CommonPrefixes**
- Status: belegt.
- Korrektur: Das Token ist undurchsichtig; NextContinuationToken ist gesetzt, wenn IsTruncated true ist. Bis zu 1000 Schlüssel pro Antwort. CommonPrefixes entstehen nur bei gesetztem delimiter.
- Quelle: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html (Abruf 2026-11-11)

**33. GetObject mit Range**
- Status: belegt.
- Korrektur: Range lädt einen Bytebereich; mehrere Bereiche pro GET sind nicht unterstützt. Verweis auf RFC 9110.
- Quelle: https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html (Abruf 2026-11-11)

**34. Multipart**
- Status: belegt. Ablauf: CreateMultipartUpload, UploadPart (Teilenummern 1 bis 10000), CompleteMultipartUpload. Abbruch über AbortMultipartUpload.
- Quelle: https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html (Abruf 2026-11-11)

**35. "kein Umbenennen/Verschieben (nur Kopieren+Löschen)"**
- Status: **nicht belegbar** in den gelesenen Seiten (die Multipart-Seite nennt kein Rename-API). Die CopyObject-Seite wurde nicht gelesen. Nebenbei: rename_opts in object_store ist ein Standardwert, der kopiert und löscht (siehe 42).

**36. "Ordner sind Schein" / Präfixe**
- Status: belegt.
- Korrektur: Ordner sind Präfixe mit Delimiter "/". Die Konsole legt zusätzlich 0-Byte-Objekte mit Schlüssel "ordner/" an.
- Quelle: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html (Beispiel 5-8)

**37. "Versionen, Pre-signed URL"**
- Status: **nicht geprüft** (nicht in den gelesenen Abschnitten).

---

## rclone Backend-Interface

**38. Fs (List, NewObject, Put, Mkdir, Rmdir), Object (ModTime, Size, Open, Update, Remove)**
- Status: **teilweise**.
- Korrektur: Die Interfaces Fs und Object sind in fs/types.go definiert (nicht in fs/fs.go; dort stehen nur Hilfsfunktionen und Fehler). Die einzelnen Methodennamen wurden nicht vollständig gegen den Quelltext gelesen.
- Quelle: https://raw.githubusercontent.com/rclone/rclone/master/fs/types.go ; https://raw.githubusercontent.com/rclone/rclone/master/fs/fs.go (Korrektur der Dateizuordnung des Befunds)

**39. Optionale Interfaces Copier, Mover, DirMover, PublicLinker, About, ChangeNotifier, PutStreamer; Features-Struktur**
- Status: belegt.
- Korrektur: Alle genannten Optionalinterfaces stehen in fs/features.go. Features hat Felder für Copy, Move, DirMove, About, ChangeNotify; das Backend füllt sie über die Methode Fill(), die die Funktionszeiger der implementierten Interfaces kopiert. Die Stelle, an der Features() Fill aufruft, nicht im gelesenen Ausschnitt.
- Quelle: https://raw.githubusercontent.com/rclone/rclone/master/fs/features.go

**40. Object.Open mit RangeOption; Hash-Arten melden**
- Status: **nicht belegt** (fs/options.go war nicht abrufbar, HTTP 404 bei GitHub-Blob und Raw-URL). Der Befund-Hinweis "rclone.org/docs" wurde nicht getestet.

**41. rclone-Lizenz**
- Status: nicht geprüft.

---

## Rust-Crates

**42. object_store (Trait ObjectStore: put_opts, put_multipart_opts, get_opts mit range, delete_stream, list, list_with_delimiter, copy_opts)**
- Status: belegt.
- Korrektur: Pflichtmethoden sind genau diese sieben. Zusätzlich gibt es provided methods wie get_ranges, list_with_offset und rename_opts (Standard: kopieren, dann löschen). Bereichsabruf erfolgt über GetOptions::with_range (Beispiel auf der Seite; das interne Feldnamen-Detail nicht bestätigt).
- Quelle: https://docs.rs/object_store/latest/object_store/trait.ObjectStore.html (Abruf 2026-11-11)
- Lizenz: MIT oder Apache-2.0 (doppelt lizenziert). Der Befund nennt nur Apache-2.0: **korrigieren**.

**43. OpenDAL (Operator: stat, list/lister, read/read_with-Bereich, write/writer, delete, copy, rename, presign_*; Capability; Layer)**
- Status: **teilweise**.
- Korrektur: Die Methoden stat, list, lister, read_with (range), write, writer, delete, copy, rename, presign_read/write sind belegt. Layer: layer() hängt eine Schicht an. "Capability" wird nicht über eine Methode capability() gelesen; die Doku verweist auf info() und einen Typ Capability.
- Quelle: https://opendal.apache.org/docs/rust/opendal/struct.Operator.html (Abruf 2026-11-11; Seite lang, nur erste 100000 Zeichen gelesen)
- Lizenz: Apache-2.0 laut Befund, nicht geprüft.

---

## FUSE

**44. FUSE-Kern: getattr, readdir, read(off,size), write, rename, unlink, mkdir, statfs; lookup**
- Status: **teilweise**.
- Korrektur: libfuse fuse.h (High-Level-API) enthält in struct fuse_operations getattr, readdir, read, write, rename, unlink, mkdir, statfs. lookup gehört nicht zu dieser Struktur (es steht in der Low-Level-API, nicht gelesen). Die kernel.org-Seite war nicht abrufbar (404).
- Quelle: https://github.com/libfuse/libfuse/blob/master/include/fuse.h (Abruf 2026-11-11)
- Lizenz: fuse.h unter LGPL-2.0 (laut Kopf der Datei).

**45. "Auf Windows nur WinFsp/Dokan"**
- Status: **nicht belegt** (nicht geprüft).

---

## Querschnitt

- Der Befund-Satz "Gemeinsames Muster aller" (Seiten/Token, Delta oder Watch, Fähigkeiten je Eintrag) ist durch die Einzelbelege gestützt, soweit sie oben belegt sind. Fähigkeiten je Eintrag: belegt bei Google Drive (capabilities); Nextcloud permissions belegt.

---

## Zusammenfassung Status

| # | Eintrag | Status |
|---|---|---|
| 1-4, 6, 7 | RFC 4918/3253/5323/9110, PROPFIND, COPY/MOVE Overwrite, MKCOL | belegt |
| 5 | WebDAV-Sperren "Ratschläge" | **falsch** |
| 8 | GVfs-Schemata | teilweise (alter Stand) |
| 9 | GVfs mount/Daemons | nicht belegbar |
| 10 | KIO Worker/stat/listDir/Job | teilweise |
| 11, 13, 14 | LDP ldp:contains, Solid Notifications | belegt |
| 12 | WAC/ACP dem LDP zugeordnet | teilweise / falsch in der Zuordnung |
| 15 | SFTP-02 = v3, Handles, Offset-Read | belegt |
| 16 | SFTP v4+/v6 Rename-Flags | teilweise (v6 belegt, v4/5 nicht) |
| 17 | MS-SMB2 Details | teilweise / nicht belegbar |
| 18, 19 | Nextcloud chunked v2, Properties | belegt |
| 20 | Nextcloud Pfad, Trash/Versions, Preview, OCS | nicht belegt |
| 21 | Graph delta | belegt |
| 22 | Graph "content mit Range" | **falsch** (Range an downloadUrl) |
| 23 | Graph createUploadSession, conflictBehavior | belegt (replace vorhanden) |
| 24 | Google "mehrere parents" | **falsch** |
| 25 | Google folder-mimeType | nicht belegt |
| 26 | Google Docs export | teilweise |
| 27, 28 | Google shortcut, capabilities | belegt |
| 29 | Google changes.list | belegt |
| 30 | Google files.list Paging | nicht belegt |
| 31 | Google Range | nur Community |
| 32-34 | S3 ListObjectsV2, Range, Multipart | belegt |
| 35 | S3 "kein Rename" | nicht belegbar |
| 36 | S3 Ordner = Präfixe | belegt |
| 37 | S3 Versionen/Presign | nicht geprüft |
| 38 | rclone Fs/Object | teilweise |
| 39 | rclone optionale Interfaces, Features | belegt |
| 40 | rclone RangeOption, Hash | nicht belegt |
| 42 | object_store Methoden | belegt (Lizenz: MIT oder Apache-2.0) |
| 43 | OpenDAL | teilweise (capability() nicht als Methode) |
| 44 | FUSE-Operationen | teilweise (lookup nicht in fuse_operations) |
| 45 | FUSE auf Windows | nicht belegt |

Nicht gegengeprüft (zeitlich nicht im Rahmen): Nextcloud-Preview und OCS, MS-SMB2-Abschnitte, KIO-Job-Modell, GVfs-Mounts, rclone-Hash- und Range-Interfaces.
