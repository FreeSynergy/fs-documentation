# 0071 – Versionen, Git und Backup in Files

Status: akzeptiert (Strategie, 2026-11-11); Code erst nach 3b und Wiki/Groups · Entscheidungen der Strategie vom 2026-11-11 (Punkte 1 bis 5 unten) · erweitert das Flag `versions` aus ADR 0070 · baut auf ADR 0067 (Tresor), 0050 (Besitzer), 0069 (Zustand), 0045 (Unsupported), 0020 (AS2, Undo), 0046 (Speichern ≠ Export)

Befund und Quellen: `temp/research/versionierung-backup.md` (Opus-Empfehlung), `versionierung-backup-vergleich.md`, `versionierung-backup-rust-bausteine.md` (alle Stand 2026-11-11).

## Voraussetzung (Regel)
**Kein Code vor Runde 3b grün und nicht vor Wiki/Groups.** Bis dahin ist dies ein Beschluss ohne Code.

## Ausgangslage
- fs-files speichert lokal unter echten Namen und berechnet beim Hochladen `blake3:<hex>`; es gibt keinen Inhalts-Speicher nach Hash und keinen Vorgang „Inhalt einer Datei ersetzen“. Von außen geänderte Dateien sind „changed outside“, `rescan` legt sie neu an. Papierkorb und offene Uploads liegen in `<root>/.fs-files/{trash,pending}`.
- ADR 0070 führt das Flag `versions`, aber noch keine Aufrufe.
- Syncthing dokumentiert offen, dass es lokale Änderungen nicht sichern kann; wer die alte Fassung nicht **vorher** hat, kann sie nicht halten. Darum entsteht eine Version schon beim Speichern jeder Fassung.

## Entscheidung (Strategie, 2026-11-11)

### 1. Drei Schichten, die sich ergänzen
Versionen schützen vor Fehlern, Git hält bewusste Stände fest, Backup schützt vor Verlust des Geräts. Keine ersetzt eine andere. Abgrenzung zu ADR 0069: der **Klon** (Sitzungszustand der Ansicht) ist weder Version noch Backup; er enthält keine Dateiinhalte.

**Schicht 1: automatische Versionen für alle Dateien**
- **Ort:** `.fs-files/versions/blake3/<2 Zeichen>/<rest>` gilt **nur für die eigene fs-files-Ablage**. Für **andere lokale Ordner** (Home …) wird nur versioniert, wenn der Mensch es **für den Ordner einschaltet**; der Speicher liegt dann **zentral** unter `$XDG_DATA_HOME/freesynergy/files/versions/` (Reflink nur auf demselben Dateisystem, sonst gilt die 100-MiB-Regel). **Nie versteckte Ordner in fremde Ordner des Menschen schreiben.** **Wechseldatenträger (USB) standardmäßig ohne Versionen.** Der Speicher ist adressiert über die vorhandene BLAKE3-Prüfsumme (gleicher Inhalt liegt einmal da). Ablage per **Reflink** auf Btrfs/XFS (fast kein Platz), sonst echte Kopie.
- **Kopie schon beim Speichern jeder Fassung:** Files legt beim Veröffentlichen jeder Fassung den Reflink/die Kopie in den Versions-Speicher. Neuer Vorgang „neuen Inhalt speichern“: Upload nach `pending`, hashen, alte Fassung in den Versions-Speicher, dann neue veröffentlichen. Nichts wird überschrieben; ein Absturz lässt beide Fassungen zurück.
- **Gestaffelte Aufräumregel:** erste Stunde alle 2 Minuten eine, danach stündlich, 30 Tage täglich, danach wöchentlich bis 1 Jahr; **höchstens 20 % der Platte**. Die Regel ist eine reine Funktion (Zeitpunkte rein, behalten/weg raus) und wird für sich getestet. Die jüngste Version jeder Datei bleibt immer.
- **Ohne Reflink:** Dateien bis **100 MiB** werden versioniert; die Grenze ist einstellbar. **Das Fenster zeigt ehrlich an, welche Datei nicht versioniert ist** (und warum).
- **Benannte Versionen bleiben immer** (nie von der Aufräumregel entfernt).
- **Wiederherstellen überschreibt nie:** „Diese Version wieder aktuell machen“ (die bisherige aktuelle wird selbst Version) oder „Als Kopie wiederherstellen“.
- **Papierkorb behält Versionen**; `purge` und „Papierkorb leeren“ löschen sie mit und **sagen das vorher** (Anzahl, Größe; benannte Versionen verlangen eine eigene Bestätigung). Inhalte, die eine andere Datei/Version noch nutzt, bleiben (Referenzzählung im Datensatz, Aufräumen als Job).
- Datensatz je Version in fs-objects: Datei-Id, Prüfsumme, Größe, Zeitpunkt, Anlass (`saved`, `changedOutside`, `restored`), Urheber, optional Name. Die Datenbank bleibt die Wahrheit.

**Schicht 2: Git für Projekt-Ordner**
- Ein Ordner wird auf Wunsch zum Projekt: normales `.git` im Ordner. Vorhandene `.git`-Ordner erkennt Files und zeigt den Verlauf lesend.
- **Commit auf Knopfdruck** („Stand festhalten“, Autor aus der Identität des Menschen). Zusätzlich ein **Schalter je Projekt „automatisch beim Speichern“, standardmäßig AUS**.
- **Abgleich anbieterneutral:** jedes Git-Remote über SSH oder HTTPS. Getestet zuerst gegen ein **lokales Bare-Repo**, später Codeberg/Forgejo und GitHub. Nie Force-Push, kein automatisches Zusammenführen („beide Seiten geändert“, beides behalten). Zugangsdaten nur als Tresor-Verweis.
- Große Binärdateien (Vorschlag über 10 MiB und Medientypen) bleiben aus Git. In Projekten, die **Files selbst anlegt**, pflegt Files dafür einen markierten Abschnitt in `.gitignore`; in **vorhandenen** Repos schreibt Files **nichts** in `.gitignore`, dort gilt `.git/info/exclude`; sie sind durch Schicht 1 und 3 geschützt, das Fenster sagt es. **LFS später.**
- **Rust:** `gix` für Lesen, Diff, Commit. **Push übergangsweise über das vorhandene System-`git` hinter einem Adapter** (`GitRepo`-Schnittstelle); der Adapter wird erkannt, fehlt `git`, lautet die Antwort **`Unsupported` mit Hinweis**. **Kein libgit2/C-Code.** Kann `gix` pushen, wird der Adapter getauscht.
- **Zugangsdaten beim System-`git`:** nie auf der Kommandozeile oder in der URL (in `ps` sichtbar); nur über SSH-Agent bzw. einen `GIT_ASKPASS`-/Credential-Helper, der den Tresor-Verweis auflöst; die Umgebung des git-Prozesses ist auf das Nötige reduziert.
- Geheimnisse: Prüfung vor Commit und Push (Schlüssel, `.env`); ADR 0054 gilt.
- Ein Git-Zurücksetzen sichert den aktuellen Inhalt zuerst als Version.

**Schicht 3: Backup im restic-Format**
- Offen dokumentiert, zwei unabhängige Umsetzungen (restic in Go, rustic in Rust). `rustic_core` **nur gekapselt hinter unserer eigenen Schnittstelle `BackupEngine` an einer einzigen Stelle**, **feste Version gepinnt** (die API bricht alle 1 bis 3 Monate; Bibliothek ist synchron, läuft im Job-Faden mit Fortschritt und Abbruch). **`rustic_backend` nicht** (bringt opendal, ADR 0070 schließt es aus); `WriteBackend` setzen wir selbst um (lokal/USB über den lokalen Anbieter, S3 über `object_store`).
- **Gegenprobe mit echtem `restic` gehört in die CI** (`restic check`, `restic restore` auf einem von Files geschriebenen Repository). **Probe-Wiederherstellung nach jeder Sicherung** (zufällige Dateien, BLAKE3-Vergleich); Ergebnis sichtbar, Fehler als Meldung.
- Gesichert werden die Dateien **und** ein Export der Datensätze (Ids, Ordner, Versionsliste), damit Ids nach einer Wiederherstellung wieder stimmen. Nur Files räumt sein Repository auf (Prune mit Vorschau); fremdes `restic` liest und prüft.
- Ziele in dieser Reihenfolge: USB (Ziel 1), später S3, node1.

### 2. Backup-Schlüssel
**Nicht auf `fs-vault` warten.** Übergangsweise der **System-Schlüsselbund über den Standard Secret Service** (KWallet/GNOME) **hinter einer kleinen Schnittstelle, die später `fs-vault` bedient** (ADR 0067). Ein **Notfall-Schlüssel wird immer angelegt** (zweite restic-Schlüsseldatei). Ablauf: (a) er wird **einmal** angezeigt; (b) zusätzlich als **Ausdruck/PDF angeboten**, das PDF **nur auf ausdrücklichen Wunsch**, **zur Laufzeit erzeugt und nie dauerhaft gespeichert** (Hinweis dazu); (c) Files bittet **einmal um Bestätigung, dass er aufgeschrieben ist**, mit **Tipp-Probe** (z. B. zwei zufällige Stellen eingeben), **bevor die erste Sicherung startet**; (d) er **liegt nie in einer Datei auf der Platte**. Ihn schreibt nur der Mensch auf, **Agenten sehen ihn nie** (ADR 0054). Ohne beide Schlüssel sind die Daten weg; das sagt Files beim Einrichten deutlich.

### 3. Reihenfolge
Versionen mit Ansicht in der Detailansicht, dann Git nur lesend, dann Backup auf USB (Ziel 1), dann Git schreibend, dann Forgejo/GitHub-Abgleich, dann S3/node1/Zeitleiste.

### 4. Erweiterung von `versions` aus ADR 0070
Alle Aufrufe mit Standardantwort `Unsupported` (ADR 0045); Ordinale nur anhängen.
```capnp
# StorageCaps: versions @9 (vorhanden); neu ans Ende: namedVersions @17 :Bool; timeline @18 :Bool;
struct VersionInfo {
  id @0 :Text;  at @1 :Timestamp;  size @2 :Int64 = -1;  checksum @3 :Text;
  reason @4 :VersionReason;  author @5 :Text;  name @6 :Text;
  source @7 :VersionSource;           # automatic | git | backup | provider
}
enum VersionReason { saved @0; changedOutside @1; restored @2; other @3; }
enum VersionSource { automatic @0; git @1; backup @2; provider @3; }
# EntryCaps: versions @n :Bool (je Eintrag; nicht versionierte Datei meldet false mit Grund)
# interface StorageProvider (anhängen):
#   versions       (id :Text, cursor :Cursor) -> (page :VersionPage);
#   openVersion    (id :Text, versionId :Text) -> (blob :Blob);          # read(offset,length), auch für Vorschau/Diff
#   restoreVersion (id :Text, versionId :Text, asCopy :Bool, onConflict :OnConflict) -> (entry :Entry);
#   nameVersion    (id :Text, versionId :Text, name :Text) -> ();         # leer = Namen entfernen
#   später listAt  (at :Text, time :Timestamp, cursor :Cursor) -> (page :EntryPage);   # Flag timeline
```
- **Fehlermodell** (RFC 9457, Typen unter `…/problems/storage/`): `unsupported` (501), `quota-exceeded` (507, Platzgrenze), **`not-versioned`** (neu; Datei ohne Version, z. B. über der Größengrenze), dazu die vorhandenen (`not-found`, `forbidden`, `name-conflict`, `timeout`, `cancelled`).
- **AS2 (ADR 0020):** `restoreVersion` ist `Update` mit `origin` = Version; `nameVersion` ist `Update`; Wiederherstellen ist mit `Undo` rückgängig; `purge` mit Versionen ist nicht rückgängig und sagt das vorher. Andere Anbieter können `versions` aus eigenen Mitteln liefern (Git-Verlauf, Backup-Snapshots, S3-Versionen); die Ansicht zeigt die **Quelle** jeder Fassung und „korrigiert“ nie still eine Quelle aus einer anderen.
- **Besitzer (ADR 0050):** fs-files besitzt Versionen der Dateien; Programme, die eigene Daten als Baum liefern, entscheiden selbst, ob sie `versions` anbieten.

### 5. Voraussetzung
Code erst nach 3b grün und nach Wiki/Groups (siehe oben).

## Risiken und Gegenvorschläge
1. **Platz.** Ohne Reflink doppelt sich der Platz; große, oft geschriebene Dateien. Gegen: Platzgrenze 20 %, Mindestabstand 2 Minuten, Größengrenze, Ausschlussliste, Anzeige „Versionen belegen …“. Eigene Datenbankdateien der Programme gehören nur ins Backup.
2. **Datenschutz.** Versionen und Backups halten, was der Mensch gelöscht glaubt. `purge` nimmt Versionen mit; Snapshots einzeln zu bereinigen ist aufwendig und in `rustic_core` nicht geprüft: Files sagt ehrlich, „bleibt in Sicherungen bis …“. **Sensible Dateien (ADR 0029):** ihre Versionen bleiben sensibel und werden genauso geschützt bzw. verschlüsselt wie die Datei.
3. **Schlüsselverlust.** Daten ohne Schlüssel sind verloren (gewollt). Notfall-Schlüssel, Probe-Wiederherstellung; der Schlüssel liegt nicht im selben Backup, das er schützt.
4. **Geheimnisse im Verlauf.** Ein gepushtes Geheimnis ist nicht zurückzuholen: Prüfung vor Commit und Push, Standard-Ausschlüsse, Warnung.
5. **Rechte.** Versionen erben die Rechte der Datei; Empfänger geteilter Dateien sehen ältere Fassungen nur, wenn der Eigentümer es will. Gruppendaten (ADR 0067): Versionen mit dem Gruppenschlüssel verschlüsselt.
6. **Dateien, die andere Programme direkt ändern.** Files kennt die alte Fassung nur, weil es beim Veröffentlichen schon eine Kopie hat; eine Änderung zwischen zwei Kopien (innerhalb der 2 Minuten) bleibt ungesichert. Der Watcher (ADR 0070 S7) und `rescan` legen die neue Fassung an; das Fenster zeigt „von außen geändert“.
7. **Abhängigkeiten.** `rustic_core` und `gix` sind 0.x: eigene Schnittstellen, gepinnte Versionen, Gegenprobe mit den Originalen. Systemabhängigkeit `git` für Push wird erkannt.
8. **Einfrieren und Abstürze.** Hashen, Kopieren, Backup, Abgleich nur als Jobs mit Zeitlimit (`call_limited`); zuerst Version anlegen, dann veröffentlichen.
9. **Drei Quellen derselben Datei** (automatisch, Git, Backup): Quelle immer sichtbar.

## Aufwand und Reihenfolge
| Stufe | Inhalt | Braucht | Größe |
|---|---|---|---|
| V1 | Versions-Speicher (BLAKE3, Reflink, Referenzzählung), Datensätze, Aufräumregel mit Tests, „neuen Inhalt speichern“, `versions`/`openVersion`/`restoreVersion`/`nameVersion` | 3b, ADR 0070 S4/S6 | mittel |
| V2 | Reiter „Versionen“ in der Detailansicht (Liste, Vorschau, Diff, wieder aktuell, Kopie, benennen, Platzanzeige) | V1 | mittel |
| V3 | Änderungen von außen (Watcher) | V1, ADR 0070 S7 | klein |
| V4 | Git nur lesend (gix): Verlauf, Diff, Status | ADR 0070 S4 | klein |
| V5 | Backup auf USB (`BackupEngine`, Secret-Service-Schlüssel, Notfall-Schlüssel, Probe, restic-Gegenprobe in der CI) | V1 | mittel |
| V6 | Git schreibend (Commit auf Knopfdruck, Schalter „automatisch“ AUS, Binär-Ausschluss, Geheimnis-Prüfung) | V4 | mittel |
| V7 | Abgleich: lokales Bare-Repo, dann Codeberg/Forgejo, GitHub (Push über System-`git`) | V6 | mittel |
| V8 | S3, node1, Zeitleiste (`listAt`) | V5, `fs-vault` für node1 | mittel bis groß |

Bewusst nicht jetzt: eigenes Backup-Format, Chunking im Versions-Speicher, libgit2, LFS/git-annex, Merge in Files, eigener Sync-Dienst, FUSE-Einhängen von Snapshots, Kopia/borg.

## Folgen
- `fs-interfaces`: `StorageCaps`/Aufrufe/Fehler aus Punkt 4 (nach Annahme und 3b); `fs-files`: Versions-Speicher, `GitRepo`, `BackupEngine`; `fs-components`: Reiter „Versionen“.
- ADR 0070 bleibt gültig; dieser ADR füllt dessen Flag `versions`.

## Quellen (Abruf 2026-11-11; Einzelnachweise in `versionierung-backup.md`)
gitoxide `crate-status.md` (`https://github.com/GitoxideLabs/gitoxide/blob/main/crate-status.md`; Hinweis „Generated by Codex“ nur über einem Abschnitt) · crates.io `gix` 0.90.0 (MIT OR Apache-2.0), `rustic_core` 0.13.0 (Apache-2.0 OR MIT, „early development stage“, `forget`/`prune`/`copy`/`repair` exportiert, synchron, API-Sprünge alle 1 bis 3 Monate) · restic-Repository-Format `https://github.com/restic/restic/blob/master/doc/design.rst` (AES-256-CTR + Poly1305-AES, mehrere Schlüsseldateien, Format 1/2) · restic 0.19.1, BSD-2-Clause · Syncthing-Versionierung `https://docs.syncthing.net/users/versioning.html` (nur Änderungen anderer Geräte) · Nextcloud Versionen `https://docs.nextcloud.com/server/latest/user_manual/en/files/version_control.html` · Forgejo-Konfiguration (LFS) `https://forgejo.org/docs/latest/admin/config-cheat-sheet/` · Git LFS (MIT) · Duplicati (MIT, laut Korrektur) · git-annex (AGPL-3.0, laut Korrektur) · Secret Service als Standard des Freedesktop-Projekts (nicht neu geprüft). Vorhandenes Code-Wissen: `fs-files/DESIGN.md`.

## English summary
**Decision:** three layers that complement each other. (1) Automatic versions for all files of the own fs-files store in `.fs-files/versions/blake3/…` (other local folders such as Home only when the human enables it per folder, stored centrally under `$XDG_DATA_HOME/freesynergy/files/versions/`, never hidden folders in the human's own folders; removable media without versions by default), reflink on Btrfs/XFS, a copy is made when every revision is saved; staggered clean-up (first hour every 2 minutes, then hourly, 30 days daily, then weekly up to 1 year, at most 20 % of the disk); without reflink only files up to 100 MiB (adjustable) and the window says honestly which file is not versioned; named versions stay forever; restoring never overwrites; trash keeps versions, `purge` removes them and says so first. (2) Git for project folders (plain `.git`, commit on a button, per-project "automatic on save" switch default OFF; any remote over SSH/HTTPS, tested first against a local bare repo; large binaries stay out, LFS later; `gix` for read/diff/commit, push temporarily through the system `git` behind an adapter, `Unsupported` with a hint if missing; no libgit2/C code; git credentials never on the command line or in the URL, only via SSH agent or a `GIT_ASKPASS`/credential helper resolving the vault reference, reduced environment; in existing repos Files writes nothing to `.gitignore`, it uses `.git/info/exclude`). (3) Backup in restic format via `rustic_core` encapsulated behind our own interface in one place, version pinned (API changes every 1 to 3 months, synchronous), not `rustic_backend` (pulls opendal); real `restic` as a check in CI; restore probe after every backup.

**Keys:** do not wait for `fs-vault`: the system keyring via Secret Service behind a small interface that `fs-vault` serves later (ADR 0067); an emergency key is always created, shown once and optionally offered as a print/PDF (only on explicit request, generated at runtime, never stored), Files asks once for confirmation that it was written down (typing check of two random positions) before the first backup, it never lies in a file on disk, agents never see it. Versions of sensitive files (ADR 0029) stay sensitive and are protected like the file. **Order:** versions with a detail view, Git read-only, backup to USB, Git writing, Forgejo/GitHub sync, S3/node1/timeline. **Interface:** extends `versions` of ADR 0070 with `versions`, `openVersion`, `restoreVersion`, `nameVersion`, capability flags, errors (`unsupported`, `quota-exceeded`, `not-versioned`), AS2 mapping with `Undo`. A clone (ADR 0069) is neither a version nor a backup. **Accepted by the Strategy on 2026-11-11. Precondition:** code only after round 3b is green and after Wiki/Groups.

## Ergänzung (Nutzer, 2026-11-12)
Antworten des Nutzers zu Platz, Zielen, Git und Backup in allen Programmen. Der Beschluss oben bleibt lesbar; wo diese Ergänzung ihm widerspricht, **gilt die Ergänzung**: Die **feste Platzgrenze von 20 % der Platte** (Schicht 1) wird durch die **Profil-Grenzen** aus Ergänzung 1 ersetzt, und das Backup-Ziel „USB, später S3, node1“ (Schicht 3) durch Ergänzung 2 (USB und SFTP zuerst). In der Reihenfolge (Punkt 3) kommen das Git-Nebenfenster (mit V4) und die Schnittstelle `backup` für alle Programme (Ergänzung 4, Stufe V5b nach V5, jedes Programm schließt sich einzeln an) hinzu. Ordinale und Fehlertypen aus Punkt 4 bleiben; Code erst nach 3b und Wiki/Groups.

#### Ergänzung 1: Lokal zuerst, Platz schonen (Nutzer, 2026-11-11)
Automatische Versionen werden **nie stillschweigend groß**. Der Mensch sieht jederzeit, wie viel Platz sie belegen und wo die Grenze liegt. Wir liefern **Standards, schreiben nichts vor**: **was** versioniert wird, **wann** (Abstände, Aufräumregel) und **wie viel** (Grenze) ist einstellbar.
- **Profil „Heim-PC“** (Standard auf dem Desktop): Versionen nur für die **eigene fs-files-Ablage** (andere Ordner bleiben aus, bis der Mensch sie einschaltet, wie in Schicht 1). Grenze **5 % der Platte und höchstens 10 GiB**, die niedrigere gilt; die Grenze steht **deutlich sichtbar** im Reiter „Versionen“ und in den Einstellungen („Versionen belegen 2,1 von 10 GiB“).
- **Profil „Server“**: großzügiger (Vorschlag: 20 % der Platte, keine feste Obergrenze in GiB); wird beim Einrichten eines Servers gewählt, nicht erraten.
- **Beim Erreichen der Grenze** räumt die Aufräumregel auf (älteste, nicht benannte Versionen zuerst); reicht das nicht, **stoppt Files das Anlegen neuer Versionen und sagt es** (`quota-exceeded`, 507), statt Dateien zu verweigern. Nie stillschweigend.
- Ein Profil ist nur ein Satz Standardwerte; Ordner, Abstände, Grenze und Größengrenze ohne Reflink sind einzeln einstellbar.

#### Ergänzung 2: Backup-Ziel trägt der Mensch ein (Nutzer, 2026-11-11)
Der Mensch wählt und trägt das Ziel selbst ein; Files rät keines. Mögliche Ziele: **USB**, **SFTP/SSH** (z. B. eine Hetzner Storage Box), **S3**, **node1**. **Zuerst USB und SFTP**, S3 und node1 später (V8).
- **SFTP ist belegt:** restic unterstützt SFTP-Repositories (`restic -r sftp:user@host:/srv/restic-repo init`; für automatische Sicherung ist Anmeldung ohne Passwortabfrage nötig), restic-Handbuch „Preparing a new repository“, Abschnitt „SFTP“ (`https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html`). Hetzner dokumentiert für die Storage Box den SSH-/SFTP-Dienst auf Port 23 und schreibt „Restic is natively supported with the SFTP backend“ (`https://docs.hetzner.com/storage/storage-box/access/access-ssh-rsync-borg/`). Abruf 2026-11-11.
- Das Repository-Format bleibt restic. Den SFTP-`WriteBackend` setzen wir hinter der `BackupEngine` um; eine SSH-Bibliothek in reinem Rust ist noch zu prüfen, bis dahin gilt wie bei Git: vorhandenes System-`ssh`/`sftp` hinter einem Adapter, `Unsupported` mit Hinweis, wenn es fehlt.
- **Zugang über Tresor-Verweis** (ADR 0067): Benutzer und Schlüssel/Passwort liegen im Tresor, im Ziel steht nur der Verweis; nie in Dateien, auf der Kommandozeile oder in der URL. Den SSH-Hostschlüssel zeigt Files beim ersten Verbinden dem Menschen zur Bestätigung und merkt ihn dann.
- Die Oberfläche zeigt je Ziel Namen, letzten erfolgreichen Lauf und Ergebnis der Probe-Wiederherstellung.

#### Ergänzung 3: Git-Nebenfenster im Reiter „Versionen“ (Nutzer, 2026-11-11)
Liegt eine Datei in einem Git-Repository (Schicht 2, auch ein vorhandenes), zeigt der Reiter „Versionen“ **zusätzlich ihre Git-Versionen** (Commit, Autor, Zeit, Nachricht). Jede Fassung zeigt ihre **Quelle** (`automatic`, `git`, `backup`; `VersionSource` aus Punkt 4); Quellen werden nie vermischt oder still gegeneinander korrigiert.
- **„Zurückgehen“** auf eine Git-Fassung ist `restoreVersion` und erzeugt eine **neue Fassung** (die bisherige aktuelle wird zuerst selbst automatische Version). **Es geht nie etwas verloren**, und es wird **kein Git-Verlauf umgeschrieben** (kein `reset --hard`, kein Force).
- Lesen über `gix` (V4); fehlt `git` oder das Schreibrecht, bleibt die Anzeige lesend.

#### Ergänzung 4: Backup in JEDEM Programm (Nutzer, 2026-11-11)
**Beschluss:** Backup ist nicht nur Sache von Files. Es gibt ein **Thema `backup` in `fs-interfaces`** (ADR 0045: jedes Thema eine Schnittstelle). Jedes Programm liefert einen **konsistenten Schnappschuss seiner Daten** und kann ihn **wiederherstellen**. Jedes Programm darf eine **eigene Strategie** haben (was, wie oft; z. B. Messenger täglich, Whiteboard bei Änderung). Die **`BackupEngine`** aus Schicht 3 **sammelt ein**: sie fragt die Programme, schreibt deren Schnappschüsse (je Programm ein eigener Pfad) zusammen mit den Dateien in dasselbe restic-Repository und kennt die Programme nur über die Schnittstelle.
```capnp
# Thema backup (Vorschlag; nur Beschluss, Code nach 3b; Ordinale nur anhängen, Standardantwort Unsupported, ADR 0045)
struct BackupPolicy { what @0 :List(Text); everySeconds @1 :UInt32; onChange @2 :Bool; }  # Strategie des Programms
interface BackupProvider {
  policy   () -> (policy :BackupPolicy);
  snapshot (jobId :Text) -> (stream :Blob, manifest :BackupManifest);   # konsistent: Transaktion/Kopie, nie mitten im Schreiben
  restore  (stream :Blob, mode :RestoreMode) -> (report :RestoreReport); # mode: asCopy | replaceAfterSafetySnapshot
}
```
- **Konsistenz ist Sache des Programms** (Datenbank-Schnappschuss statt Datei mitten im Schreiben); `fs-objects` liefert den Export der Datensätze (Schicht 3).
- **Wiederherstellen überschreibt nie still:** vorher sichert das Programm den Ist-Zustand als Schnappschuss (wie ADR 0069), dann erst Ersetzen; oder „als Kopie“.
- **Sensible Daten** (ADR 0029) und Tresor-Inhalte stehen nur verschlüsselt im Schnappschuss (ADR 0067); Schlüssel nie darin.
- **Fehlermodell** (RFC 9457, `…/problems/backup/`): `unsupported` (501), `busy` (503, Programm kann gerade nicht konsistent sichern), `timeout`, `cancelled`, `corrupt` (409, Prüfung der Wiederherstellung schlug fehl).
- Jeder Lauf ist ein Job mit Zeitlimit und Abbruch (Risiko 8) samt Probe-Wiederherstellung. **Ein Programm ohne `backup` zeigt die Übersicht als „nicht gesichert“**, es wird nicht still ausgelassen.
- Besitzer (ADR 0050): jedes Programm besitzt die Bedeutung seiner Schnappschüsse; die `BackupEngine` besitzt Ziele, Zeitplan und Repository.
- Entwurfsmuster: **Strategy** (eigene Sicherungsstrategie je Programm), **Adapter** (Ziele hinter `WriteBackend`), **Memento** (Schnappschuss und Wiederherstellung).

**Summary of the amendment (2026-11-12):** local first, save space: profile "home PC" (default desktop) versions only the own fs-files store, limit 5 % of the disk and at most 10 GiB, shown clearly; profile "server" 20 % without a GiB cap; everything adjustable (what, when, how much). The human enters the backup target (USB and SFTP/SSH such as a Hetzner Storage Box first, then S3, node1), access via vault reference; restic supports SFTP natively. For a file inside a Git repo the "Versions" tab also shows its Git versions (source visible); "go back" creates a new revision, never a loss. New topic `backup` in `fs-interfaces`: every program delivers a consistent snapshot and can restore it, with its own strategy; the `BackupEngine` collects them. Code only after 3b.
