# Entwurf: Files als Kern, Katalog als Anbieter, Installieren als Aktion

Stand: 2026-11-12 (Opus, Entwurf, **kein ADR**, kein Code). Grundlage: Nutzerentscheidung über die Strategie (2026-11-12, siehe unten),
`BEFUND.md` (Haiku) plus eigene Nachprüfung der Lücken (§9), ADR 0066, 0068, 0069, 0070, 0071 (`fs-documentation` `origin/main`),
ADR 0073 (Entwurf, nur in `/srv/FreeSynergy/.wt-docs-adr/conventions/decisions/0073-kollaboration-ueberall-mit-loro.md`, noch nicht auf `origin/main`),
Store-Empfehlung `/srv/FreeSynergy/.scratch/frontends/vorbilder-store/EMPFEHLUNG.md`, Store-Lückenliste `/srv/FreeSynergy/.wt-store-par/docs/gaps-adr-0068-0071.md`,
Code-Stand `fs-store` v0.0.11, `fs-files` v0.0.7, `fs-interfaces` v0.0.18, `fs-catalog` `02d9710`.
Markierung: **[nicht belegt]** = in keiner Primärquelle bestätigt; **[Vorschlag]** = eigene Designidee, nicht entschieden.

**Überarbeitung 2026-11-12 (Nutzer/Strategie):** (1) Herkunft wird als **unveränderliche AS2-Ereignisse im Verlauf (fs-history)** festgehalten, die Paket-Zugehörigkeit **speichert der Store selbst** je Datei (Korrektur 2026-11-12, §1.3, §3; rpm/dpkg nur Gegenprobe); Widerspruch zu ADR 0070 neu bewertet (§1.3). (2) Antworten F1–F7 eingearbeitet (§8): xattr werden geschrieben (abschaltbar), eigener Steckbrief für fremde Ordner ja, Kopie nicht in Sammlungen, unbekannte Programme nur mit Bestätigung, **PackageKit zuerst prüfen** (§5, Belege §9), Meilenstein festgelegt (§7). Repo-Frage (§6) ist **nicht festgezurrt**.

**Nutzerentscheidung, auf die alles aufbaut:**
- Installieren ist eine **Aktion auf einer Datei** wie „öffnen“ oder „starten“, nur gründlicher geprüft, je nach Risiko.
- Der Installer ist eine **Facette von Files**; alles, was er kann, kann auch Files. Galerie, Desktop (zuerst als Startseite) und Git sind ebenfalls Facetten.
- Der **Katalog** ist die anbietende Seite (Netz), **Files** die lokale.
- Files zeigt bei **jeder** Datei, **woher sie stammt und zu welchem Paket sie gehört** (wie `rpm -qf`), damit man bei Schadcode sofort die Quelle sieht.
- Workflows vorerst nur mit **fester Schritt-Liste und Klartext-Vorschau**. Keine Sterne, dafür **persönliche Sammlungen/Alben**.

## 0. Kurzfassung

1. Jede Datei hat **zwei Teile**: (a) einen **Verlauf aus unveränderlichen AS2-Aktivitäten** in fs-history (heruntergeladen, kopiert, installiert, aktualisiert, entfernt – je mit `actor`, `object` samt Prüfsumme, `origin`, `instrument`, `target`); daraus wird die **Herkunft** gelesen, auch nach Entfernen eines Pakets und für Forensik. (b) einen **veränderlichen Steckbrief** (Schlagworte, Sammlungen, Beschreibung) als Datensatz (fs-objects für die eigene Ablage, Begleit-Datenbank von fs-files für fremde Bäume – **entschieden: ja**). Die **Paket-Zugehörigkeit** („gehört gerade zu Paket X“) **speichert der Store selbst** je Datei (Pfad, Paket, Version, Quelle, Signatur, Prüfsumme) – auf allen Systemen gleich (Linux, Windows, macOS, Redox); `rpm -qf`/`rpm -V`/dpkg sind unter Linux nur **zusätzliche Gegenprobe** für Systemdateien, die wir nicht selbst installiert haben. **xattr werden zusätzlich geschrieben** (entschieden, abschaltbar), damit Dolphin & Co. profitieren; Wahrheit sind sie nie, weil `cp -p` und `rsync -a` sie verlieren und S3/WebDAV keine haben.
2. Der Katalog ist ein **`StorageProvider`** (ADR 0070) mit den Wurzeln **„Verfügbar“** (nur lesend) und **„Programme“** (installiert). Aktionen (Installieren, Aktualisieren, Entfernen, Zurück zu Version) kommen als **Befehle der Typbeschreibung** (ADR 0066), **nicht** als `copy`/`delete`.
3. Herkunft wird in fester Reihenfolge aufgelöst und **mit Beleg-Stufe** angezeigt: *belegt* (Verlauf, Dateiliste des Stores, Signatur) · *inhaltsgleich* (Hash-Treffer) · *vermerkt* (xattr, fälschbar) · *unbekannt*. „Geändert seit Installation“ wird rot gezeigt (`fs-store verify`, Prüfsumme gegen die eigene Dateiliste); „war Teil von Paket X 0.0.2, entfernt am …“ bleibt sichtbar.
4. Vier Risikostufen **ansehen < öffnen < starten < installieren** (installieren systemweit als 4b), je Stufe feste Prüfungen; jede Stufe ab „starten“ läuft als **Workflow mit Klartext-Vorschau**. Unbekannte Programme starten **nur mit Bestätigung** (entschieden); Sandbox später als Option.
5. Root bleibt **klein und getrennt**: heute `pkexec dnf install` (fs-store). Als Nächstes wird **PackageKit geprüft** (D-Bus-Dienst mit eigenen polkit-Aktionen, Backend `dnf5`, Aufruf `InstallFiles` mit Flag „nur vertrauenswürdig“); ein eigener Helfer nur, falls PackageKit durchfällt. Files rechnet nie selbst als root.
6. Repos: **Arbeitsstand** B jetzt, C nach dem Meilenstein – **noch nicht festgelegt** („besprechen wir noch“). Darum gilt: nichts tun, was C (oder eine noch unbekannte Variante) erschwert.
7. Laufende Store-Arbeit bleibt gültig; **vor dem Meilenstein** (GitHub + Releases, Store, Tasks als Arbeitsbrett, Wiki mit Doku, Files-Optik, Server-Pakete) wird nichts verschoben, umbenannt oder an `storage.capnp` gebaut. **Eingeplant** (klein, nur Store): eigene Dateiliste mit Hash je Datei, `fs-store owner <pfad>`, `fs-store verify`, dazu das Schreiben der Install-/Update-/Entfernen-Aktivitäten.

---

## 1. Was trägt jede Datei

### 1.1 Steckbrief jeder Datei

| Feld | Inhalt | Woher kommt der Wert | Standard / Abbildung | Fälschbar? |
|---|---|---|---|---|
| **Herkunft** (Ereignisse, unveränderlich) | Kette von **AS2-Aktivitäten** zur Datei: heruntergeladen, installiert, aktualisiert, entfernt, kopiert, verschoben, empfangen von Person, importiert, selbst erstellt, außerhalb von Files entstanden – je mit `actor` (Mensch oder markierte KI, ADR 0054), Zeit, `object` (Datei samt Prüfsumme), `origin`, `instrument`, `target` (§1.3) | Files bzw. Store **schreiben eine Aktivität je Vorgang**; nie geändert, nur angehängt; Fremdquellen siehe §3 | AS2 `Add`/`Update`/`Remove`/`Create`/`Move` (ADR 0014, 0020); nach außen zusätzlich `user.xdg.origin.url` | Verlauf: nein. xattr: ja |
| **Paket – aktueller Stand** | „gehört **gerade** zu Paket X Version Y“ oder „zu keinem Paket“; Zustand ok / geändert / fehlt | **Dateiliste des Store-Kerns** (vom Store selbst geschrieben, §1.3) = Wahrheit für „was WIR installiert haben“; rpm/dpkg nur Gegenprobe für fremde Systemdateien | AppStream-Komponenten-Id; rpm `Provides` (ADR 0068) | nein (Prüfsumme in der Liste) |
| **Paket – früher** | „war Teil von Paket X 0.0.2 bis zum Entfernen am …“; „liegengeblieben nach Entfernen“ | aus dem Verlauf (Aktivitäten `Add`/`Remove` mit `instrument` = Paket) | AS2 | nein |
| **Vertrauen / Signatur** | Stufe a/b/c aus der Store-Empfehlung (Macher+Spiegel / nur unser Schlüssel / nur Prüfsumme) **plus** Stufe „ohne“ für alles ohne Signatur; Schlüssel-Fingerprint, Prüfzeitpunkt | Prüfung beim Herunterladen/Installieren; **an den Hash gebunden** | OpenPGP (rPGP), TUF-Targets | nein, solange der Hash stimmt |
| **Prüfsumme** | `blake3:<hex>` (fs-files rechnet sie schon beim Hochladen) und, wo der Katalog sie nennt, `sha256` | fs-files beim Schreiben; Katalog/TUF | SPDX `hashValue` beim Export | nein |
| **Schlagworte** | freie Liste | Mensch | `user.xdg.tags` (de-facto, KDE, kommagetrennt, §9); XMP `dc:subject` nur beim Export in Formate, die XMP tragen | — |
| **Sammlungen** | Zugehörigkeit zu persönlichen Sammlungen/Alben (Verweis, nicht Kopie); **keine Sterne** | Mensch, Galerie | AS2 `Collection` (wie `Album` in `fs-files-types`) | — |
| **Beschreibung** | Text (später Wiki-Block, ADR 0072) | Mensch, beim Paket der Katalog | `user.xdg.comment`; XMP `dc:description` beim Export | — |
| **Rechte** | POSIX-Modus/Eigentümer (Anzeige), FreeSynergy-Rechte des Besitzers (ADR 0050), Empfindlichkeit `sensitive`/`to` der Hülle (ADR 0029), Lizenz falls bekannt (SPDX-Ausdruck) | Anbieter (`stat`), Hülle, Katalog | SPDX-Lizenzausdruck | — |
| **Ausführbar?** | ja/nein + warum (x-Bit, Medientyp, Skript mit `#!`) | Files beim `stat` | — | — (wird immer neu geprüft) |

Galerie, Desktop und Git lesen dieselben Daten: die Galerie zeigt Sammlungen als Alben, der Desktop (Startseite) zeigt Sammlungen und „Zuletzt“, Git (ADR 0071 Schicht 2) ergänzt nur den Verlauf.

### 1.2 Bei Paketen zusätzlich

| Feld | Quelle |
|---|---|
| Fähigkeiten provides/requires/recommends und ihre Auflösung | Katalog (ADR 0068), Resolver `fs-store-core/src/capability.rs` |
| Spiegel-Herkunft: Macher-Quelle, Macher-Signatur, Quellcode-Datei derselben Version | Katalog (A1/A7 der Lückenliste) |
| **Dateiliste mit Prüfsumme je Datei** (was das Paket auf die Platte gelegt hat) | **vom Store selbst geschrieben**, für jedes Format: tar.gz beim Entpacken; rpm aus dem Kopf der geprüften rpm-Datei **vor** der Installation (Crate `rpm` liest rpm-Dateien, §9) und nach der Installation gegen die Platte geprüft |
| Größe (Download, installiert), Datum, Änderungen je Version, Bilder, Icon | Katalog (A1) |
| Lizenz, Fehler melden, Quellcode-Link | Katalog |
| Gehaltene Vorversionen (`current/<name>`-Umschaltung) | Store |
| Export als SBOM | SPDX 3.0.1 / CycloneDX 1.7 als **Sidecar-Export**, nie als Wahrheit |

### 1.3 Speicherort: Ereignisse, Steckbrief, Dateiliste des Stores, xattr

Drei Arten von Daten, drei Regeln:

| Art | Beispiel | Veränderlich? | Ablage | Besitzer |
|---|---|---|---|---|
| **Ereignis** (was geschah) | „Kal hat am 2026-11-10 fs-tasks 0.0.3 aus Katalog FreeSynergy installiert; dabei entstand `…/bin/fs-tasks` mit sha256 …“ | **nein**, nur anhängen | Aktivitäten-Log des **Handelnden** (Store für Installieren/Aktualisieren/Entfernen, fs-files für Download/Kopie/Verschieben), über den Hub; **fs-history indiziert** sie nur (fs-history v0.0.1 ist ein abgeleiteter Index der Hub-Aktivitäten) | Store bzw. fs-files (ADR 0050) |
| **Steckbrief** (was der Mensch dazu sagt) | Schlagworte, Sammlungen, Beschreibung | ja | eigene Ablage: Datei-Objekt in **fs-objects**; fremde Bäume (Home, USB, S3, DAV, SFTP): **Begleit-Datenbank von fs-files** unter `$XDG_DATA_HOME/freesynergy/files/` (**entschieden F2: ja**), Schlüssel `(anbieter-id, eintrags-id)` plus Prüfsumme als zweiter Anker; nie versteckte Dateien in fremde Ordner (ADR 0071) | fs-files |
| **Installationsstand** (was WIR installiert haben) | je Datei: Pfad, Paket, Version, Quelle, Signatur(-Stufe), Prüfsumme | ja (bei Installieren/Aktualisieren/Entfernen) | **Dateiliste des Store-Kerns** (unten) | Store |
| **Dateizustand jetzt** | Rechte, Größe, Hash jetzt | – | nie gespeichert, immer vom Anbieter (`stat`) gelesen; der Vergleich Hash-jetzt gegen Liste ergibt ok/geändert/fehlt | Anbieter |

**Aktivitäten beim Installieren, Aktualisieren, Entfernen (Store) [Vorschlag zur Form]:** je Vorgang **eine** Aktivität:

| AS2-Feld | Installieren (`Add`) | Aktualisieren (`Update`) | Entfernen (`Remove`) |
|---|---|---|---|
| `actor` | Mensch (oder markierte KI); beim Timer der Mensch, der den Timer eingerichtet hat | wie links | wie links |
| `object` | Liste der gelegten Dateien, je `{pfad, sha256, blake3}` | neue Dateien mit Hash; ersetzte Dateien mit altem Hash | entfernte Dateien mit Hash; **liegengebliebene** Dateien ausdrücklich als solche |
| `origin` | Katalog-Quelle (URL, Serien-Nr. `fs-serial`), Artefakt-URL | wie links | — |
| `instrument` | Paket: Id, Version, Format, Artefakt-sha256, Signatur (Stufe a/b/c, Fingerprints, Prüfzeit) | alte und neue Version | Paket und Version |
| `target` | Installationsort (`current/<name>`, `~/.local/bin`, Menü; bei rpm „System“) | wie links | wie links |
| `result` | Erfolg / zurückgerollt (mit Grund) | wie links | wie links |

Die AS2-Felder `actor`, `object`, `origin`, `instrument`, `target` sind im W3C-Vokabular definiert (§9). Downloads: `Create` mit `origin` = URL, `instrument` = Programm (Files/Browser), `object` = Datei samt Hash. Kopien: `Create` mit `origin` = Quelldatei (`fs://…` samt Hash). Verschieben: `Move` mit `origin`/`target`.

Damit gilt: **Herkunft bleibt** nach Entfernen des Pakets, bei liegengebliebenen Dateien und für Forensik (Verlauf), und der **aktuelle Stand** steht in der Dateiliste des Stores (veränderlich, eine Wahrheit, ein Besitzer). Verlauf und Liste widersprechen sich nicht: die Liste ist der jüngste Stand, der Verlauf die Kette dorthin; aus dem Verlauf ließe sich die Liste neu aufbauen (Prüfung in Tests).

**Dateiliste des Store-Kerns (Korrektur Nutzer 2026-11-12) [Form: Vorschlag]:**
- **Inhalt je Datei:** Pfad (relativ zum Installationsort, plus Art des Orts: `store` / `bin-link` / `menu` / `system`), Paket-Id, Version, Format, Quelle (Katalog-URL + `fs-serial`), Signatur-Stufe + Fingerprints, `sha256` (wie im Katalog) und `blake3` (wie fs-files), Größe, Modus, Art (Datei/Link mit Ziel).
- **Ort:** im Store-Root (`$FS_STORE_ROOT`, sonst `~/.local/share/fs-store`; systemweit später ein System-Ort, [offen]). `installed.toml` behält je Paket nur Kopfdaten (Version, Quelle, `auto_update`, Signierer – Lücke A6) und **verweist** auf eine Liste je Paket und Version, z. B. `files/<paket>/<version>.toml` **[Vorschlag]**; so bleibt `installed.toml` klein und lesbar, und gehaltene Versionen behalten ihre Liste. Später kann eine Datenbank des Store-Kerns dasselbe halten; das Format ist hinter einer Schnittstelle (`FileIndex`, Repository-Muster) austauschbar.
- **Schreiben:** atomar (temp, `fsync`, `rename`) **vor** dem Umschalten von `current/<name>`; misslingt die Liste, wird nicht umgeschaltet (Zustandsautomat: gehört zu „installieren“, Rückrollen löscht sie).
- **Größe (Schätzung, [nicht gemessen]):** je Datei etwa 250–350 Byte als TOML (Pfad ~80, zwei Hashes à 64 Hex, Felder). Ein FreeSynergy-Programm mit 10–50 Dateien: 3–20 KiB je Version; 50 Pakete mit je 2 gehaltenen Versionen: wenige MiB. Systempakete mit tausenden Dateien (rpm) gehen in den MiB-Bereich je Paket; dann ist eine Datenbank statt TOML zu erwägen (Schwelle beim ersten großen Paket messen).
- **Suche „Pfad → Paket“** (`fs-store owner`): Rückwärts-Index Pfad → (Paket, Version), beim Laden aufgebaut oder als eigene Datei; Hash → Paket für „inhaltsgleich“.
- **Migration alter Installationen ohne Liste** (alles vor dieser Änderung): (1) tar.gz: liegt das geprüfte Artefakt noch vor oder ist es über Katalog/TUF mit bekanntem `sha256` wieder ladbar, wird die Liste **aus dem Archiv** gebaut und mit der Platte verglichen; Abweichungen sind „geändert“ (rot). (2) Ist das Artefakt nicht mehr zu haben: Liste aus dem Ordner `current/<name>/<version>` **so wie er jetzt ist**, sichtbar markiert „**nachträglich erfasst am … – ohne Beleg der Originalfassung**“ (nicht grün, nicht rot). (3) rpm-Installationen des Stores: Liste aus der rpm-Datei, falls noch vorhanden, sonst unter Linux aus der rpm-DB als Gegenprobe übernommen und ebenso markiert. Migration als **einmaliger, wiederholbarer Job** (`fs-store verify --rebuild`), nie still beim Start. Eine Aktivität „nachträglich erfasst“ kommt in den Verlauf.

**xattr: werden geschrieben (entschieden F3), abschaltbar.** Files schreibt auf lokalen Anbietern `user.xdg.tags`, `user.xdg.comment`, `user.xdg.origin.url`, damit Dolphin und andere Programme die Werte sehen. Ein Schalter (global und je Ort) stellt das ab. Beim Erkennen werden xattr **gelesen** und als „vermerkt“ (fälschbar) eingestuft; weichen sie vom Steckbrief ab (z. B. Dolphin hat ein Schlagwort ergänzt), übernimmt Files die Änderung als **Steckbrief**-Änderung mit Vermerk „von außen“ **[Vorschlag]**. Herkunft aus xattr wird nie zu „belegt“. Auf USB/Wechselmedien standardmäßig **aus**, pro Gerät einschaltbar (entschieden F9); auf Netz-Anbietern nicht möglich. Wechseldatenträger und fremde Ordner: xattr sind keine versteckten Dateien, die Regel aus ADR 0071 bleibt eingehalten.
- **Sidecar-Dateien** (`*.spdx.json`) nur als Export, nie als Ablage.

**Begründung (belegt, §9):**
- GNU `cp`: `-p` bewahrt nur `mode,ownership,timestamps`, also **keine** xattr; erst `--preserve=xattr` oder `-a` (dort ohne Fehlermeldung bei Misserfolg).
- `rsync -a` schließt `-X` ausdrücklich **nicht** ein.
- S3, WebDAV, SFTP-v3 haben keine xattr im Sinne von Linux; der Steckbrief muss aber auch dort gelten.
- freedesktop-Schlüssel sind „Proposed“; das Wiki selbst sagt, viele Programme und Dateisysteme unterstützen xattr nicht.
- Vorbild OpenCloud nutzt beides: Metadaten-Präfix `user.oc.` (xattr) und für das „decomposed“-Laufwerk `.mpk`-Dateien (msgpack), dazu einen Cache in NATS-KV. Also auch dort nicht „nur xattr“.
- Herkunft ist ein **Sicherheitsmerkmal**: was jeder mit `setfattr` ändern kann, darf nie als „belegt“ gelten.

**Widerspruch zu ADR 0070 §2 neu geprüft** („Files hält keine Wahrheit, nur Registry, Ansichtszustand, Auswahl“):
- **Ereignisse:** kein Widerspruch. Eine Aktivität ist keine Wahrheit *über den Eintrag*, sondern ein Protokoll *eigener Handlungen*; ADR 0070 verlangt das selbst („Jede ändernde Handlung ist eine Aktivität im Protokoll des Besitzers … bei Anbietern ohne Objekte ist die Aktivität lokal (Files-Sicht)“). Herkunft aus Ereignissen ist also schon angelegt. Unveränderlich, darum keine zweite veränderliche Wahrheit.
- **Installationsstand:** kein Widerspruch zu ADR 0070, weil **nicht Files** ihn hält, sondern der **Store-Kern** als Besitzer (ADR 0050). Files zeigt ihn über den Anbieter `fs://catalog` bzw. fragt `owner(pfad)` – genau das Muster „Programm-Bäume, Abbildung beim Besitzer“ (ADR 0070 §5). **Folge für ADR 0070 (Hinweis, kein neues ADR):** neben „Files hält keine Wahrheit über Inhalt und Struktur fremder Anbieter“ festhalten: „Die Wahrheit über Installationen hält der Store-Kern (Dateiliste); Files liest sie.“ Achtung bei einer späteren Repo-Variante A (Store-Crates in fs-files): dann hielte fs-files diese Wahrheit selbst – ein Grund mehr, den Store-Kern als eigenen Besitzer zu behalten, gleich wo der Code liegt.
- **Steckbrief fremder Bäume:** **echter Zusatz** zu ADR 0070 – veränderliche Daten, die fs-files besitzt. Entschieden (F2: ja); beim nächsten Überarbeiten von ADR 0070 so zu formulieren: „Files hält keine Wahrheit **über Inhalt und Struktur** fremder Anbieter; es besitzt den Datentyp **Steckbrief** (Schlagworte, Sammlungen, Beschreibung) und das Protokoll eigener Handlungen.“ (kein neues ADR hier, nur Hinweis)
- **Neue Spannung: Vergessen gegen Forensik.** fs-history kann Einträge **vergessen** (nur Index; das Hub-Log bleibt). Für Forensik muss die Install-Aktivität im Hub-Log/Store-Log bleiben; Entschieden (F8): Standard behalten; der Mensch darf seine Aktivitäten wirklich löschen (mit Hinweis, dass die Herkunft dann fehlt); systemweite Software-Aktivitäten bleiben mindestens 1 Jahr, löschen nur durch Admin. Außerdem: fs-history setzt `actor` heute leer und `at` = Empfangszeit – das ist ein **Fehler** (git-bug-Kandidat, §8); Original-Actor und -Zeit sind beim Hub schon angefragt.

### 1.4 Kopieren, Verschieben, Umbenennen

Jede Zeile erzeugt **zusätzlich eine Aktivität** (Spalte „Ereignis“); der Verlauf wird nie umgeschrieben.

| Vorgang | Ereignis | Steckbrief | Paket | Vertrauen | Sammlungen |
|---|---|---|---|---|---|
| Umbenennen / Verschieben **im selben Anbieter** | `Update` bzw. `Move` | folgt der Eintrags-Id, unverändert | bleibt; wird ein Paket-Datei verschoben, gilt sie als **„fehlt im Paket“** und die neue Stelle als „Kopie aus Paket X“ (Warnung vorher) | bleibt (Hash gleich) | bleiben |
| Verschieben **zwischen Anbietern** (Files vermittelt: kopieren, prüfen, dann löschen) | `Move` mit `origin` = alter Ort, `target` = neuer Ort, Hash | wird übertragen | wie oben | bleibt, wenn der Hash nach der Übertragung stimmt (Files prüft) | bleiben |
| **Kopieren** | `Create` mit `origin` = Quelldatei samt Hash; die Herkunft der Quelle bleibt über den Verweis lesbar | neu; Schlagworte und Beschreibung werden übernommen | **nicht** übernommen; Anzeige „inhaltsgleich mit Datei aus Paket X 1.2“ | übernommen, weil an den Hash gebunden | **nicht** übernommen (**entschieden F4**) |
| Inhalt ändern (speichern) | `Update` mit altem und neuem Hash; alte Fassung wird Version (ADR 0071) | bleibt | Paket-Datei heißt **„geändert seit Installation“** (rot) | **fällt weg** (neuer Hash) | bleiben |
| Änderung **außerhalb** von Files (`cp` im Terminal, anderes Programm) | beim Erkennen (Beobachten/`rescan`) eine Aktivität „außerhalb entstanden/geändert“, `actor` unbekannt | trifft der Hash eine bekannte Datei: Angebot „inhaltsgleich mit …, Steckbrief übernehmen?“; nie still | wie Kopieren | über den Hash | nein |
| Weitergabe nach außen (USB, Mail, Export) | `Create`/`Move` am Ziel bzw. Export-Aktivität | xattr werden mitgeschrieben (Schalter, F3), sonst Sidecar-Export | nicht | nicht (der Empfänger prüft selbst) | nein |

---

## 2. Katalog als Speicher-Anbieter (ADR 0070)

### 2.1 Bäume

```
fs://catalog/
├── Verfügbar/                     (nur lesend; je Quelle, signiert, TUF)
│   ├── <Quelle: FreeSynergy>/
│   │   ├── Programme/  Frontends/  Server/  Themes/  Icons/     (Art = fs:kind)
│   │   │   └── fs-tasks/                     (Ordner = Paket; stat liefert Paketseite)
│   │   │       ├── 0.0.3/                    (Ordner = Version, Änderungstext)
│   │   │       │   ├── fs-tasks-0.0.3-linux-x86_64.tar.gz   (Datei = Artefakt)
│   │   │       │   ├── …tar.gz.asc                         (Signatur)
│   │   │       │   └── Quellcode-0.0.3.tar.gz               (Spiegel, ADR 0068)
│   │   │       └── 0.0.2/
│   └── <weitere Quellen>/
├── Programme/                     (installiert; Wahrheit beim Store bzw. rpm)
│   └── fs-tasks/  → Version 0.0.3 (aktuell), 0.0.2 (gehalten)
│       └── Dateien des Pakets (Dateiliste, je Datei Prüfsumme + Zustand ok/geändert/fehlt)
├── Updates/                       (virtuell: Programme mit neuerer Version)
└── Übersprungen/                  (Katalog-Einträge, die abgelehnt wurden, mit Grund; nie still)
```

Ort `fs://catalog/<pfad>`, Eintrags-Id opak (ADR 0070 Leitgedanke 1), z. B. `pkg:<quelle>/<id>@<version>/<artefakt>`.

### 2.2 Anbieter-Schnittstelle

| Aufruf (ADR 0070) | „Verfügbar“ | „Programme“ |
|---|---|---|
| `caps` | `range`, `search`, `preview` ja; alles Schreibende nein; `state` = `offline`, wenn keine Quelle erreichbar | `watch` ja (Installationen ändern den Baum); `versions` ja (gehaltene Versionen); Schreibendes nein |
| `roots` | `Verfügbar`, `Programme`, `Updates`, `Übersprungen` | |
| `list` / `stat` | Katalog lesen (signiert, offline aus dem Cache des Stores) | `installed.toml` + Dateiliste; bei rpm `rpm -q` |
| `open` → `Blob.read(offset,length)` | liefert das Artefakt **erst nach Prüfung** (TUF `read_target` bzw. OpenPGP + sha256), Bereichs-Lesen für Fortsetzen | liefert eine installierte Datei (nur lesen) |
| `write`, `create`, `rename`, `move`, `copy_to`, `delete`, `restore` | `Unsupported` | `Unsupported` (**bewusst**, siehe 2.3) |
| `types` (ADR 0066) | Typ `Paket`, `Paketversion`, `Artefakt` mit Befehlen | Typ `InstalliertesPaket` mit Befehlen |
| `versions` / `restoreVersion` (ADR 0071) | — | „zurück zu gehaltener Version“ |

**Neu nötig [Vorschlag, erst mit `storage.capnp` nach 3b]:** `EntryKind` bekommt hinten `package @5` (Ordinale nur anhängen) und `Entry` einen Verweis auf den Steckbrief (`provenance @12`). Ohne das bliebe nur der Medientyp `application/vnd.freesynergy.package` **[Vorschlag]** als Kennzeichen.

### 2.3 Aktionen statt Dateioperationen

**Installieren ist ein Befehl auf dem Eintrag**, gemeldet über die Typbeschreibung (ADR 0066, `supported` je Befehl), **nicht** „kopieren von Verfügbar nach Programme“. Gründe: Ein Kopieren darf nie still zu einer Installation werden (Risiko-Prüfung muss sichtbar sein); `delete` hätte sonst die Bedeutung „deinstallieren“ und landete im Papierkorb-Modell, das hier nicht passt.

| Befehl | Auf | Stufe (§4) |
|---|---|---|
| `install` | Artefakt/Paketversion in „Verfügbar“ **und jede lokale Paketdatei** (heruntergeladene `.rpm`, `.tar.gz`, `.AppImage`, `.flatpakref`) | 4 / 4b |
| `update`, `updateAll` | „Programme“, „Updates“ | 4 |
| `remove` | „Programme“ | 4 (4b bei rpm) |
| `rollback` | gehaltene Version | 4 |
| `verify` | installiertes Paket: eigene Dateiliste gegen Platte (`fs-store verify`); unter Linux optional zusätzlich `rpm -V` | 1 |
| `openSource` | Quellcode-Datei | 2 |
| `start` | installiertes Programm/Facette | 3 |

Weil der Befehl am **Typ** hängt, kann Files ihn auch für eine Paketdatei im Home anbieten: Files erkennt sie am Medientyp, sucht ihren Hash im Katalog („diese Datei ist fs-tasks 0.0.3 aus Quelle FreeSynergy, Signatur ok“) und ruft denselben Installationsweg. **Das ist der Kern von „Installieren ist eine Aktion auf einer Datei“.**

---

## 3. Herkunft je Datei

### 3.1 Auflösung (feste Reihenfolge, erster Treffer gewinnt je Feld)

1. **Verlauf** (AS2-Aktivitäten des Stores und von fs-files, über den Hub, indiziert in fs-history): Suche nach der Datei per Ort **und** per Prüfsumme → *belegt* (wer, wann, woher, mit welchem Paket/Signatur). Findet auch „war Teil von Paket X, entfernt am …“ und liegengebliebene Dateien.
2. **Dateiliste des Store-Kerns** (`fs-store owner <pfad>`): Pfad steht in der Liste eines installierten Pakets → „gehört gerade zu …“, Hash jetzt gegen Liste → ok / geändert (rot) / fehlt → *belegt*. Auf allen Systemen gleich.
3. **Nur Linux, nur Gegenprobe, keine Pflichtquelle:** für Dateien, die **nicht** in unserer Liste stehen (Systempakete), `rpm -qf <pfad>` / `dpkg -S <pfad>`, Zustand über `rpm -V` → *belegt (System, Gegenprobe)*. Fehlt das Werkzeug (Windows, macOS, Redox, Linux ohne rpm/dpkg), zeigt Files ehrlich „nicht von uns installiert, keine Systemprüfung verfügbar“. Flatpak-Pfade **[nicht belegt, offen]**.
4. **Hash-Abgleich**: Prüfsumme gegen den Hash-Index von fs-files und gegen sha256 im signierten Katalog → *inhaltsgleich mit …* (der Inhalt ist sicher derselbe, der Weg dorthin nicht).
5. **xattr**: `user.xdg.origin.url` (setzen u. a. Browser/KDE), auf macOS `com.apple.quarantine`, auf NTFS-Datenträgern der Strom `Zone.Identifier` → *vermerkt* (fälschbar, nur Hinweis). Ob Linux-Treiber `Zone.Identifier` lesbar machen: **[nicht belegt]**.
6. Sonst: **„Herkunft unbekannt“** – ehrlich, nie geraten.

### 3.2 Anzeige (Detailbereich jeder Datei, auch ohne Paket)

```
Woher      heruntergeladen von https://example.org/tool.AppImage
           am 2026-11-03 14:12 durch Kal (über Files)            [belegt]
Paket      gehört zu keinem Paket
           inhaltsgleich mit: nichts Bekanntem                    [Hash-Abgleich]
Vertrauen  keine Signatur · Prüfsumme blake3:9f2c…  (aufklappen)
Ausführbar ja (x-Bit, ELF)   →  „Starten“ verlangt Bestätigung (§4)
           [Alle Dateien dieser Quelle zeigen]  [Quelle sperren]
```

```
Woher      installiert aus Katalog „FreeSynergy“ am 2026-11-10
Paket      fs-tasks 0.0.3 (tar.gz) · Datei 14 von 37
Vertrauen  Stufe a: Macher-Schlüssel ABCD… ✔ · Katalog-Schlüssel 16A4…4342 ✔
Zustand    ⚠ GEÄNDERT seit Installation (Prüfsumme weicht ab)    [Paket prüfen] [Neu installieren]
Verlauf    2026-11-03 Add  fs-tasks 0.0.2 (Kal)  ·  2026-11-10 Update → 0.0.3 (Kal)   [ganzer Verlauf]
```

```
Woher      installiert aus Katalog „FreeSynergy“ am 2026-11-03 als Teil von fs-maps 0.0.4   [Verlauf]
Paket      gehört zu KEINEM Paket mehr – liegengeblieben nach Entfernen von fs-maps am 2026-11-09
Vertrauen  Inhalt gleich wie bei der Installation (sha256 stimmt mit dem Verlauf)
           [Datei entfernen]  [Behalten und als eigene Datei übernehmen]
```

**Bei Schadcode-Verdacht** führt jede Datei in zwei Klicks zu: Quelle → alle Dateien dieser Quelle → Paket entfernen / Quelle abschalten. Die Rückrichtung („welche Dateien hat Paket X gelegt?“) ist der Ordner unter `Programme/`.

---

## 4. Aktionen mit Risikostufen

| Stufe | Aktion | Was passiert | Prüfungen |
|---|---|---|---|
| 1 | **ansehen** | Vorschau, Steckbrief, Inhalt als Text/Bild | Größengrenze; Vorschau-Decoder **in eigenem Prozess** (fremde Bilder/PDFs sind Angriffsfläche) **[Vorschlag: welche Sandbox, offen]**; keine Netzzugriffe aus der Vorschau |
| 2 | **öffnen** | Datei geht als Daten an ein Programm | Medientyp aus Inhalt und Name, bei Widerspruch Hinweis; Besitzerprogramm statt „irgendein“ Programm; Empfindlichkeit (ADR 0029) |
| 3 | **starten** | Datei wird ausgeführt (Programm, AppImage, Skript) | Herkunft anzeigen; **Prüfsumme** gegen Katalog, falls bekannt; **Signatur**, falls vorhanden; Herkunft *unbekannt/vermerkt* ⇒ **Bestätigung mit Klartext** („Diese Datei stammt aus … und ist nicht signiert. Sie kann alles tun, was du darfst.“) – **entschieden F5**; Sandbox **später als Option**, ob und wie wird noch geprüft; nie automatisch nach Download; der Start wird als Aktivität protokolliert |
| 4 | **installieren** (Benutzer) | dauerhaft unter `current/<name>`, Links in `~/.local/bin`, Menü-Einträge | alles aus 3, dazu **Signatur Pflicht** (heute: OpenPGP gegen `16A4…4342`, sonst kein `VerifiedPackage`); **Quelle** (Katalog, Signatur-Stufe a/b/c); **Fähigkeiten** auflösen (ADR 0068: fehlt / Auswahl / ok), **Zuwachs gegenüber installierter Version hervorheben**; **Workflow-Vorschau** (4.1); Bestätigung |
| 4b | **installieren systemweit** (rpm) | Root-Teil (§5) | alles aus 4, plus polkit-Abfrage durch das System; Flag „nur vertrauenswürdig“ (PackageKit `ONLY_TRUSTED`, §5) bzw. Hash am übergebenen Dateideskriptor erneut prüfen |

Regeln:
- Eine Stufe erbt alle Prüfungen der Stufen darunter.
- Die **Stufe richtet sich nach der Aktion, die Strenge nach der Herkunft**: ein signiertes Katalogpaket startet ohne Rückfrage, eine unbekannte ausführbare Datei nie.
- Abgelehnte Prüfungen werden **sichtbar** gemeldet (RFC 9457 `Problem`), nie still übergangen; Beispiel `…/problems/files/untrusted-origin`.
- Stufe 4b, **neue** Software: immer Admin-Bestätigung in unserer Vorschau, zusätzlich zur polkit-Regel der Distribution (entschieden F10); Updates installierter signierter Pakete nach Distributions-Standard.

### 4.1 Workflow mit fester Schritt-Liste und Klartext-Vorschau

```
Installieren: fs-tasks 0.0.3 aus „FreeSynergy“
 1. Katalog-Signatur prüfen (Schlüssel 16A4…4342)                ✔ schon geprüft
 2. fs-tasks-0.0.3-linux-x86_64.tar.gz laden (14 MiB)
 3. Signatur und Prüfsumme der Datei prüfen
 4. Fähigkeit „identity.oidc ≥1.0“ → erfüllt durch Kanidm
 5. Entpacken in den Store-Root (~/.local/share/fs-store/…/fs-tasks/0.0.3)
 5a. Dateiliste schreiben: je Datei Pfad, Paket, Version, Quelle, Signatur, Prüfsumme
 6. Umschalten current/fs-tasks → 0.0.3 (0.0.2 bleibt gehalten)
 7. Befehl „fs-tasks“ in ~/.local/bin, Menü-Eintrag „FreeSynergy.Tasks“
 8. Läuft fs-tasks? Dann schließen und am selben Punkt neu starten (ADR 0069)
 9. Vorgang festhalten: Aktivität „Add“ mit allen Dateien und Prüfsummen (§1.3)
                                        [Abbrechen]   [Ausführen]
```
Die Schritte sind fest pro Aktion (kein Baukasten). Jeder Schritt meldet Fortschritt und lässt sich abbrechen; nach Schritt 6 ist Abbruch = Zurückrollen (heutiger Zustandsautomat des Stores). Pfad in Schritt 5 ist Beispiel; der echte Store-Root gilt.

---

## 5. Root-Teil: klein, getrennt, polkit

**Heute** (fs-store DESIGN): rpm wird als private Datei (0700-Ordner, 0600, `O_EXCL|O_NOFOLLOW`) abgelegt, dann `pkexec dnf install -y <datei>`; root fragt pkexec, nie der Store. Das bleibt, bis PackageKit geprüft und entschieden ist.

**Als Nächstes: PackageKit prüfen (entschieden F6), eigener Helfer nur als Rückfall.**

Was PackageKit laut Primärquellen bietet (Abruf 2026-11-12, Repo `github.com/PackageKit/PackageKit`, `main`; Einzelnachweise §9):
- D-Bus-Schnittstelle `org.freedesktop.PackageKit.Transaction` mit `InstallFiles(transaction_flags, files)`, `InstallPackages`, `RemovePackages`; Fortschritt über die Signale `Progress`, `Status`, `Error`, `Packages`; Flag `SIMULATE` liefert vorab, was installiert/entfernt würde (passt zur **Klartext-Vorschau**, §4.1).
- Flag **`ONLY_TRUSTED`**: unsignierte Dateien werden abgelehnt (`ErrorCode(missing-gpg-signature)`).
- Eigene polkit-Aktionen, u. a. `org.freedesktop.packagekit.package-install` (aktive Sitzung: `auth_admin_keep`), `…package-install-untrusted` (`auth_admin`), `…package-remove` (`auth_admin_keep`), `…system-update` (aktive Sitzung: `yes`, also **ohne Passwort**), `…system-trust-signing-key` (`auth_admin`). Mitgelieferte Regel: Gruppen `wheel`/`sudo` dürfen Systemupdates ohne Passwort auslösen.
- Backend-Ordner u. a. `dnf5`, `apt`, `zypp`, `alpm`, `nix` (also auch Debian/Ubuntu und Arch, ein Weg statt zwei).
- Lizenz des Repos: GPL-2.0 (GitHub-Angabe, `COPYING`). Wir würden **nur über D-Bus sprechen** (z. B. `zbus`), nichts linken; ob das lizenzrechtlich unberührt bleibt: **[nicht rechtlich geprüft]**.

Befunde, die vor einer Entscheidung geklärt werden müssen:
- **Widerspruch im Schema:** Der Kommentar zu `InstallFiles` nennt `@full_paths` (Pfade), die Signatur ist aber `ah` (Liste von **Dateideskriptoren**). Welche Form der Dienst auf Fedora erwartet, ist **[nicht belegt]** – für uns ist der Dateideskriptor die gewünschte Form (kein TOCTOU).
- **Zweiter Widerspruch:** Der Kommentar nennt die Berechtigung `org.freedesktop.packagekit.localinstall-untrusted`, die Policy-Datei kennt nur `…package-install-untrusted`. **[nicht belegt]**, welche gilt.
- `auth_admin_keep` heißt: nach einer Passwortabfrage bleibt die Erlaubnis eine Weile gültig. **Entschieden (F10):** wir folgen der polkit-Regel der Distribution und überstimmen nichts; **neue Software systemweit** verlangt zusätzlich **immer eine Admin-Bestätigung in unserer Vorschau**; Updates installierter signierter Pakete laufen nach Distributions-Standard. Test auf dem Rechner nach dem Meilenstein.
- Ob PackageKit auf Fedora 45 standardmäßig installiert ist und `dnf5` dort das Backend ist: **[nicht belegt]**.
- Wessen Schlüssel PackageKit bei `ONLY_TRUSTED` prüft: die **rpm-Schlüssel des Systems**. Unser Projektschlüssel müsste also als rpm-Schlüssel importiert sein (`system-trust-signing-key`). Ablauf **[nicht geprüft]**.

**Ablauf mit PackageKit [Vorschlag]:**
```
Store-Engine (Benutzer)                                   PackageKit (Systemdienst, root)
  prüft Signatur (unser Schlüssel), Hash, Fähigkeiten
  legt Datei privat ab (0700/0600, O_EXCL|O_NOFOLLOW)
  InstallFiles(SIMULATE, [fd])  ───────────────────────▶  meldet, was passieren würde
  zeigt Klartext-Vorschau, Mensch bestätigt
  InstallFiles(ONLY_TRUSTED, [fd]) ────────────────────▶  polkit fragt (System-Dialog), installiert über dnf5
  ◀──── Progress/Status/Packages/Error ────────────────
  schreibt Aktivität „Add“ (§1.3)
```

**Rückfall, falls PackageKit durchfällt:** eigener Helfer `fs-store-root` mit genau zwei Aufrufen (`install(fd, sha256)`, `remove(name)`), einer polkit-Aktion je Aufruf, Hash-Prüfung am Deskriptor, kein Netz, kein Katalog-Parser, keine Shell. Bis zur Entscheidung bleibt `pkexec dnf`.

Files ruft den Root-Teil **nie direkt**, sondern über den Installationsweg der Engine (§6); so gibt es genau einen Weg nach root.

---

## 6. Was wird aus `fs-store` und `fs-catalog`

**Stand der Entscheidung (F1):** Arbeitsstand ist B jetzt, C nach dem Meilenstein; der Nutzer will das **noch besprechen**, weitere Ideen kommen. Die Varianten unten sind darum **Denkstand, keine Festlegung**. Regel bis dahin: **nichts tun, was C oder eine noch unbekannte Variante erschwert** (Liste in §7).

`fs-catalog` bleibt in allen bisher gedachten Varianten **das Daten-Repo** (Paketliste, Generator, signierter Katalog, später TUF-Layout und `catalog.freesynergy.net`, ADR 0068 §3). Es wird kein Code-Repo.

### Variante A: fs-store geht in fs-files auf
Die Crates `fs-store-core`, `-catalog`, `-tuf`, `-pgp`, `-engine`, `-sources` wandern nach `fs-files` (z. B. `fs-files-install`); das Store-Fenster wird Facette „Programme“; Repo `fs-store` wird archiviert.
- **+** Wörtlich „Installer ist Facette von Files“; ein Repo, ein Release.
- **+** Keine Schnittstelle zwischen Files und Store nötig.
- **−** fs-files wird sehr groß (12 Crates kommen dazu) und vermischt zwei Besitzer-Wahrheiten (Dateien und Installationen), entgegen ADR 0050.
- **−** **Selbst-Update-Falle:** Files aktualisiert Files, während es das Fenster ist, das gerade aktualisiert (ADR 0069 Weg B setzt einen *anderen* Prozess als Auslöser voraus).
- **−** Großer Umzug mitten in Runde 3b/Store-Lücken; Historie, Tags, CI, Paketnamen `fs-store` im Katalog, `installed.toml`-Pfade ändern sich.
- **−** Alle Programme, die nur installieren wollen (CLI, Server-Knoten ohne Files), hängen an fs-files.

### Variante B: fs-store bleibt Installations-Kern, liefert seinen Baum selbst (Arbeitsstand jetzt)
fs-store bleibt Programm und Repo (Engine, CLI, Dienst, Selbst-Update). Es liefert **selbst** einen `StorageProvider` `fs://catalog` (genau das Muster „Programm-Bäume“ aus ADR 0070 §5: der Besitzer bildet ab). Files zeigt ihn als Wurzel und ruft die Befehle aus der Typbeschreibung. Das Store-Fenster bleibt vorerst bestehen.
- **+** Passt ohne Änderung zu ADR 0050 (eine Wahrheit: Installationen beim Store) und ADR 0070 §5.
- **+** Kein Umzug; laufende Store-Arbeit (Katalogfelder, Frontend B/C, Update-Neustart) bleibt, wo sie ist.
- **+** Selbst-Update sauber: der Store aktualisiert Files und umgekehrt kann Files den Store als Paket behandeln.
- **+** Installieren geht auch ohne Files (CLI, Server-Knoten, Timer `update --all`).
- **−** Zwei Wege zur gleichen Ansicht (Store-Fenster und Files-Wurzel), bis C erreicht ist.
- **−** Braucht `storage.capnp` (frühestens nach 3b) für die Files-Seite; bis dahin nur Store-Fenster.

### Variante C: fs-store wird kopflos, die Oberfläche lebt in Files (möglicher Schritt nach dem Meilenstein)
Wie B, aber das Store-Fenster entfällt: Raster/Tabelle/Paketseite werden die **Facette „Programme“ von Files** (gleiche fs-components). fs-store liefert nur noch Engine, CLI, Dienst und Anbieter.
- **+** Erfüllt die Nutzerentscheidung auch in der Bedienung: ein Programm (Files), mehrere Facetten.
- **+** Eine Liste-/Raster-/Detail-Component für Dateien und Pakete (ADR 0066: Darstellung nur in fs-components).
- **−** Store-Selbst-Update braucht weiterhin einen Prozess außerhalb des Files-Fensters (Dienst/CLI) – das ist gewollt.
- **−** Erst sinnvoll, wenn Files `storage` kann (S1–S4 aus ADR 0070) und die Files-Oberfläche steht.

### Einschätzung (nicht festgelegt)
**B als Arbeitsstand, C als möglicher nächster Schritt, A eher nicht** – vorbehaltlich der Besprechung mit dem Nutzer. Damit C (oder Neues) offen bleibt: Engine und Oberfläche im Store getrennt halten, Darstellung nur aus fs-components, Aktionen nur über die Typbeschreibung, keine Annahme „der Store hat ein eigenes Fenster“ in Engine, CLI oder Schnittstelle. Bei C gälte für den Menschen: „Installieren“ ist eine Aktion in Files, die Facette „Programme“ zeigt den Katalog; im Code bleibt der Installations-Kern ein eigener Besitzer mit eigenem Repo. Dass der Installer „Facette von Files“ ist, wird in C über die Oberfläche erfüllt, nicht über den Ort des Codes. (Nach ADR 0061 gehört eine Facette zu genau einem Programm; die Facette „Programme“ wäre also eine Facette von fs-files, deren Daten vom Anbieter fs-store kommen – wie die Galerie, deren Quellen YouTube/PeerTube sind.)

---

## 7. Auswirkung auf die laufende Store-Arbeit

| Arbeit | Bleibt gültig? | Anmerkung |
|---|---|---|
| **Katalogfelder** A1 (`Details`), Resolver A2, Generator A7 | **ja, unverändert** | sie sind der Steckbrief der Katalog-Einträge (§1.2) |
| **A3: `store.capnp`-Felder in `fs-interfaces` v0.0.19** (size, released, changes, origin, provides/requires/recommends, signer, trust, releases, screenshots, iconSha256, description) | **ja** | v0.0.19 trägt laut Plan ohnehin `end_server` und Fortschritt/Heartbeat; die Felder nur anhängen. **Bitte Namen so wählen, dass sie später 1:1 im Steckbrief auftauchen:** `origin`, `signer`, `trust`, `sha256` (nicht `upstreamSig2` o. ä.). `Control.suspend` gehört **nicht** in v0.0.19 (ADR 0069). |
| **Store-Frontend Variante B** (Raster/Tabelle), **C** (Liste+Detail) als Gegenprobe | **ja** | Tabelle und Paketseite **aus fs-components** bauen (Liste/Zelle/Detail), damit sie in Variante C ohne Umbau die Facette „Programme“ werden. |
| **Update-Neustart** (ADR 0069, B1–B6) | **ja, unverändert** | bleibt im Store; Weg B braucht den Store als eigenen Prozess (Argument für B/C). |
| A6 Signierer in `installed.toml` | **ja, vorziehen** | Grundlage für „Vertrauen“ installierter Dateien. |
| **Eingeplant vor dem Meilenstein (Nutzer, 2026-11-12), nur Store:** (1) Dateiliste je Paket und Version mit Pfad, Paket, Version, Quelle, Signatur, `sha256`/`blake3` (Form §1.3), geschrieben vor dem Umschalten; (2) `fs-store owner <pfad>` (Pfad → Paket); (3) `fs-store verify [<paket>]` (Liste gegen Platte, geändert = rot), `--rebuild` für die Migration alter Installationen | **ja, eingeplant** | Wahrheit für „was WIR installiert haben“, auf allen Systemen gleich; liefert §3 Schritt 2 ohne Files und ohne neue Schnittstelle. Tests: Liste vor Umschalten, Rückrollen entfernt sie, geänderte Datei wird rot, Migration markiert „nachträglich erfasst“. |
| **Neu [Vorschlag]:** Aktivität `Add`/`Update`/`Remove` je Vorgang (§1.3) | **erlaubt vorher, klein** | Der Store schreibt sie zunächst **lokal, nur anhängend** (z. B. JSON-Lines mit AS2-Objekten im Store-Root) und reicht sie an den Hub, sobald der Weg steht. Herkunft geht so ab sofort nicht mehr verloren. Nur anhängen, nie umschreiben. |
| **PackageKit-Prüfung** (F6, F10) | **Test auf dem Rechner erst nach dem Meilenstein** | dann: `InstallFiles` mit `SIMULATE` und `ONLY_TRUSTED` gegen ein eigenes signiertes rpm; bis dahin bleibt `pkexec dnf`. |

**Meilenstein „Wir benutzen es selbst“ (bestätigt, F7):** GitHub + Releases, Store, Tasks als Arbeitsbrett, Wiki mit Doku, Files-Optik, Server-Pakete. Die Store-Arbeit oben dient genau diesem Meilenstein; alles andere wartet.

**Vor dem Meilenstein „Wir benutzen es selbst“ NICHT umbauen:**
1. Keine Repo-Verschiebung, kein Umbenennen, kein Archivieren von `fs-store`; keine Crates zwischen Repos verschieben.
2. Kein `storage.capnp`, kein `StorageProvider`-Code, kein Katalog-Anbieter (ADR 0070: erst nach 3b grün und Annahme).
3. Kein Steckbrief-Datensatz in fs-objects/fs-files, keine Begleit-Datenbank, kein xattr-Schreiben.
4. Kein eigener Root-Helfer; `pkexec dnf` bleibt, bis die PackageKit-Prüfung entschieden ist.
5. Keine Änderung am Install-Ablauf oder Zustandsautomaten des Stores außer den Lücken der Liste und dem Schreiben der Aktivitäten.
6. Kein Wegfall des Store-Fensters (Repo-Frage F1/F11 noch offen).
7. Keine Sandbox-Einführung für „starten“ (erst Auswahl, dann Gegenprobe).

**Damit C (oder Neues) nicht erschwert wird, gilt schon jetzt:**
- Engine/CLI/Schnittstelle des Stores setzen **kein eigenes Store-Fenster** voraus; alles, was das Fenster kann, geht auch über `store.capnp`/CLI.
- Store-Darstellung nur aus **fs-components** (keine Store-eigenen Widgets).
- Aktionen (installieren, aktualisieren, entfernen, zurück) als **Befehle mit `supported`** beschreiben (ADR 0066), nicht als Knöpfe mit eigener Logik im Fenster.
- Keine neuen Abhängigkeiten **von fs-files auf fs-store** oder umgekehrt im Code; die spätere Naht ist nur `storage` + Typbeschreibung.
- Neue Felder in `store.capnp` nur anhängen, Namen passend zum späteren Steckbrief (`origin`, `signer`, `trust`, `sha256`).

---

## 8. Offene Fragen an den Nutzer

### Entschieden (Nutzer über Strategie, 2026-11-12)
- **F1 Repos – vorläufig:** B jetzt, C nach dem Meilenstein; **wird noch besprochen**, weitere Ideen kommen. Nichts festzurren, was C erschwert (§6, §7).
- **F2 Steckbrief für fremde Ordner: JA** (Begleit-Datenbank von fs-files, §1.3).
- **F3 xattr: JA, schreiben**, damit alle Programme (Dolphin u. a.) profitieren; Schalter zum Abschalten bleibt (§1.3).
- **F4 Kopie in Sammlungen: NEIN**, nicht automatisch (§1.4).
- **F5 Unbekannte Programme:** nur mit Bestätigung starten; Sandbox später als Option, ob/wie wird noch geprüft (§4).
- **F6 Root-Weg:** zuerst **PackageKit** prüfen, eigener polkit-Helfer nur als Rückfall (§5).
- **F7 Meilenstein bestätigt:** GitHub + Releases, Store, Tasks als Arbeitsbrett, Wiki mit Doku, Files-Optik, Server-Pakete (§7).
- **Korrektur Herkunft:** Installieren/Aktualisieren/Entfernen, Downloads und Kopien werden als **unveränderliche AS2-Aktivitäten** festgehalten; der aktuelle Paket-Stand wird **vom Store selbst gespeichert** (Dateiliste je Datei, Korrektur 2026-11-12; rpm/dpkg nur Gegenprobe unter Linux) (§1.3, §3).

### Entschieden (Strategie, 2026-11-12, Nachtrag)
- **F8 Vergessen gegen Forensik:** Standard = **behalten**. Der Mensch darf **seine** Aktivitäten löschen (DSGVO, „wirklich löschen“, ADR 0073 §7), mit Hinweis, dass dann die Herkunft fehlt. **Software-Aktivitäten auf Systemebene** (systemweit installieren/aktualisieren/entfernen) behält der Rechner **mindestens 1 Jahr**; löschen nur durch Admin, mit Hinweis.
- **F9 xattr auf USB/Wechselmedien:** Standard **AUS** (fremde Geräte; FAT/exFAT kann laut Strategie ohnehin keine xattr – von mir nicht nachgeprüft, [nicht belegt]); **pro Gerät einschaltbar**.
- **F10 PackageKit:** Wir folgen der **polkit-Regel der Distribution** und überstimmen nichts. **Neue Software systemweit** verlangt **immer eine Admin-Bestätigung in unserer Vorschau**, zusätzlich zur polkit-Regel. **Updates bereits installierter signierter Pakete** laufen nach Distributions-Standard. Test auf dem Rechner **nach dem Meilenstein**.
- **F11 Repo-Besprechung:** kein Termin; der Nutzer bringt seine Ideen, wenn sie reif sind.
- **fs-history:** „Aktivitäten ins Log des Handelnden bzw. des Hubs, fs-history nur Index“ **angenommen**. `actor` leer ist ein **Fehler** (siehe unten).

### git-bug-Kandidat (fs-history)
**Titel:** Aktivität ohne `actor` wird still angenommen. **Befund:** fs-history v0.0.1 setzt `Entry.actor` leer, weil der Hub heute nur den Programmnamen liefert (`/srv/FreeSynergy/fs-history/DESIGN.md`); eine AS2-Aktivität ohne `actor` ist unvollständig und für Herkunft/Forensik wertlos. **Test:** Eine Aktivität ohne `actor` wird abgelehnt bzw. sichtbar gemeldet (Problem), nie still als leer gespeichert. **Behebung:** beim gemeinsamen Heben von fs-history (zusammen mit Original-Actor und -Zeit in `hub.capnp` `Activity`, dort schon angefragt).

### Offen
- Keine offenen Fragen aus diesem Entwurf. Ausstehend sind nur die Repo-Ideen des Nutzers (F11) und der PackageKit-Test nach dem Meilenstein (F10).

---

## 9. Lückenschluss zum Befund (eigene Nachprüfung, Abruf 2026-11-11/12)

| Lücke aus `BEFUND.md` | Ergebnis | Quelle |
|---|---|---|
| Microsoft MOTW | **belegt:** Strom `Zone.Identifier` (voll `datei: Zone.Identifier:$DATA`), Textform `[ZoneTransfer]` / `ZoneId=3`; „Windows Internet Explorer uses the stream name Zone.Identifier for storage of URL security zones“. Weitere Felder (z. B. `HostUrl`) dort **nicht** genannt → [nicht belegt]. | learn.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/6e3f7352-d11c-4d76-8c39-2516a9df36e8 ([MS-FSCC]) |
| Apple quarantine | **teilweise belegt:** Apple dokumentiert nur `LSFileQuarantineEnabled` („whether the files this app creates are quarantined by default“, macOS 10.0+). Eine Apple-Seite zum Attribut `com.apple.quarantine` selbst und zu seinem Format wurde **nicht** gefunden → Format [nicht belegt primär]; nur Sekundärquellen (MITRE T1553.001, eclecticlight.co). | developer.apple.com/documentation/bundleresources/information-property-list/lsfilequarantineenabled |
| `user.xdg.tags` | **belegt als De-facto-Schlüssel in KDE-Code:** KFileMetaData `usermetadata.cpp` schreibt/liest `xdg.tags` (kommagetrennt, leer = entfernen), `xdg.comment`, `xdg.origin.url`, `baloo.rating` (Präfix `user.` in `xattr_p.h`, dort nicht eingesehen). **Nicht** auf der freedesktop-Wiki-Seite, kein Standard. KDE-Bug 473808 (XDG-Spec-Unterstützung) offen. | codebrowser.dev/kde/kfilemetadata/src/usermetadata.cpp.html; bugs.kde.org/show_bug.cgi?id=473808 |
| xattr beim Kopieren | **belegt:** GNU `cp -p` = `mode,ownership,timestamps` (ohne xattr); `--preserve=xattr` bewahrt sie oder scheitert mit Meldung; `-a` versucht es und ignoriert Fehler. `rsync -a` = `-rlptgoD`, „does not include … xattrs (-X)“; normaler Benutzer kopiert mit `-X` nur `user.*`. `mv` über Dateisysteme: [nicht belegt]. | gnu.org/software/coreutils/manual/html_node/cp-invocation.html; download.samba.org/pub/rsync/rsync.1 |
| OpenCloud-Metadaten | **belegt (README des Dienstes):** Metadaten-Präfix `user.oc.` (nativ), alt `user.ocis.`; „decomposed“-Ablage nutzt `.mpk`-Dateien (msgpack); Stat/Metadaten-Cache standardmäßig in NATS-JetStream-KV. Welche Ablage (xattr oder `.mpk`) bei PosixFS gilt, ist dort nicht ausgeführt → [nicht belegt]. Die oCIS-ADR 0024 („msgpack statt xattr“) wurde nicht vollständig abgerufen → Begründung [nicht belegt primär]. Spaces-Modell: nicht geprüft. | raw.githubusercontent.com/opencloud-eu/opencloud/main/services/storage-users/README.md |
| Rust-Crates | **belegt (crates.io-API):** `xmp_toolkit` 1.12.1, MIT OR Apache-2.0, Adobe – **Bindings an das C++-XMP-Toolkit** (widerspricht der Linie „kein C-Code“ wie in ADR 0071; nur für späteren Export erwägen). `rpm` 0.30.2, Apache-2.0 OR MIT, reines Rust, **baut und liest rpm-Dateien** (nicht die rpm-Datenbank; `rpm -qf` bleibt ein Befehlsaufruf). `appstream` 0.2.2, MIT, letzte Änderung 2022-01-16 (alt; fs-store parst AppStream heute selbst). `xattr` 1.7.0, MIT OR Apache-2.0, 2026-10-28. | crates.io/api/v1/crates/{xmp_toolkit,rpm,appstream,xattr} |
| Flatpak „Datei → App“ | nicht geprüft → [nicht belegt] | — |
| PackageKit als Root-Weg (Abruf 2026-11-12) | **belegt:** `InstallFiles(t transaction_flags, ah files)`; Kommentar: „installs local package files“, unsignierte Dateien bei vertrauenswürdig-Flag → `ErrorCode(missing-gpg-signature)`; `InstallPackages` nennt `ONLY_TRUSTED`; Flags `SIMULATE`, `ONLY_DOWNLOAD`; Signale `Progress`, `Status`, `Error`, `Packages`. Polkit-Aktionen und Standardwerte wie in §5 (`package-install` `auth_admin_keep`, `package-install-untrusted` `auth_admin`, `package-remove` `auth_admin_keep`, `system-update` `yes`, `system-trust-signing-key` `auth_admin`); Regel-Datei erlaubt `wheel`/`sudo` Systemupdates ohne Passwort. Backends u. a. `dnf5`, `apt`, `zypp`, `alpm`, `nix`. Repo nicht archiviert, letzter Push 2026-11-11, Lizenz GPL-2.0. **Widersprüche im Schema** (Pfade vs. `ah`; `localinstall-untrusted` vs. `package-install-untrusted`) → [nicht belegt], Spike nötig. Standard-Installation auf Fedora 45: [nicht belegt]. | github.com/PackageKit/PackageKit: `src/org.freedesktop.packagekit1.Transaction.xml`, `data/policy/org.freedesktop.packagekit.policy.in`, `data/policy/org.freedesktop.packagekit.rules`, `backends/`, `COPYING` |
| AS2-Felder für Aktivitäten | **belegt:** `instrument` „objects used … in the completion of an Activity“; `origin` „indirect object … from which the activity is directed“; `target` „indirect object, or target“; `actor`; `object`; `Add` „actor has added the object to the target“; `Remove`; `Update`. | w3.org/TR/activitystreams-vocabulary/ |
| fs-history als Ablage | **eigener Code-Stand:** fs-history v0.0.1 ist ein **abgeleiteter Index** der Hub-Aktivitäten (nur Zusammenfassung, kein `payload`), kann **vergessen**; `actor` heute leer, `at` = Empfangszeit. Darum Aktivitäten beim Handelnden/Hub ablegen, fs-history nur zum Suchen. | `/srv/FreeSynergy/fs-history/README.md`, `/srv/FreeSynergy/fs-history/DESIGN.md` |
| Sandbox für „ansehen/starten“ (bubblewrap, Landlock …) | nicht geprüft → [nicht belegt] | — |
