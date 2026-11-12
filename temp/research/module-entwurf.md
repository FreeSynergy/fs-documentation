# Entwurf: Module – die Schicht zwischen Components und Programmen

Stand: 2026-11-12 (Opus, Entwurf, **kein ADR**, kein Code, niedrige Priorität – der Meilenstein geht vor).
Grundlage: Nutzeridee über die Strategie (unten), Befund `/srv/FreeSynergy/.scratch/module/BEFUND.md` (Haiku) plus eigene Nachprüfung (§8),
ADR 0021, 0045, 0050, 0059, 0061, 0062, 0063, 0065, 0066, 0068, 0070 (`fs-documentation` `origin/main`), ADR 0073 (Entwurf, `/srv/FreeSynergy/.wt-docs-adr/conventions/decisions/0073-kollaboration-ueberall-mit-loro.md`),
Files-Kern-Entwurf `/srv/FreeSynergy/.scratch/datei-metadaten/ENTWURF-files-kern.md`, Workflow-Entwurf `/srv/FreeSynergy/.scratch/workflows/ENTWURF-workflow-standard.md`,
Code-Stand `fs-whiteboard` 0.0.1 (`/srv/FreeSynergy/fs-whiteboard/DESIGN.md`), `fs-capnpc` v0.0.1, `fs-catalog` (`packages.toml`), Blinc `Cargo.lock`.
Markierung: **[nicht belegt]** = in keiner Primärquelle bestätigt; **[Vorschlag]** = eigene Designidee, nicht entschieden.

**Nutzeridee, auf die alles aufbaut:**
- „Module“ sind eine Schicht **zwischen Components und Programmen**; sie sind **keine Facetten**.
- Programm = **Hülle + Kern + Module**, die es erweitern (Files: Galerie, Installieren, Git …).
- Dieselben Module lassen sich **in anderen Programmen** einsetzen (ein Export-Dialog braucht nur das Auswahl-Modul).
- Ein **Programm ohne Module** ist als **Dialog** aufrufbar (Dateiauswahl für andere Programme).
- Vorbild: Zentinel-Agenten; ADR 0045 „Hot-Plugins nach Vorbild Zentinel“.

## 0. Kurzfassung

1. **Sechs Begriffe, je eine Aufgabe** (§1): *Component* zeichnet, *Anbieter* liefert Daten hinter einer Themen-Schnittstelle, *Modul* fügt einem Kern eine Fähigkeit hinzu, *Programm* besitzt ein Thema, *Facette* ist ein Ausschnitt mit Namen, *Dialog* ist ein Programm im Auswahl-Modus. Neu ist nur das Modul. **Facette = Filter + Auswahl von Modulen + Menüeintrag** – so bleibt der Files-Kern-Entwurf („Installer, Galerie, Git sind Facetten“) für den Menschen gültig, und im Code sind es Module.
2. **Ein Modul hat keine eigene Wahrheit** (ADR 0050). Braucht es Daten, gehören sie einem Programm, und das Modul spricht dessen Schnittstelle. Darum kann es in mehreren Programmen laufen.
3. **Ein Vertrag, zwei Laufweisen** (§2, Variante D): Jedes Modul hat eine **Cap'n-Proto-Schnittstelle plus Rust-Trait** (wie jedes Thema). Eigene, vertrauenswürdige Module laufen **im Prozess** (Rust-Crate), fremde oder gefährliche **als Agent** in eigenem Prozess. Der Aufrufer merkt keinen Unterschied; ein Modul kann später ohne Änderung der Aufrufer nach außen wandern.
4. **Cap'n Proto bleibt** (ADR 0021). Zentinel ist Vorbild für das **Muster** (eigener Prozess, Fähigkeiten melden, Gesundheit, Abbruch, atomarer Tausch), nicht für den Draht: Zentinel nutzt JSON über Unix-Socket oder gRPC (belegt, §8). ADR 0045 ist also **keine falsche Angabe, sondern eine bewusste Abweichung**, die im ADR so benannt werden sollte. Wasm (WIT) ist eine spätere Option für fremde Logik, nicht jetzt.
5. **Oberfläche:** Module zeichnen nie selbst (ADR 0066). Ein Modul im Prozess setzt Components zusammen; ein Agent liefert eine **Ansichtsbeschreibung** aus dem Wortschatz von fs-components, und **der Host misst und legt aus**. Damit ist „Textmessung ungelöst“ (ADR 0045) für Agenten aufgelöst: sie messen nicht.
6. **Dialog** (§3): zuerst intern `fs-files pick` mit Dialog-Hülle (ADR 0065) für alle eigenen Programme; danach Files als **xdg-desktop-portal-Backend** (`FileChooser`, `ashpd` hat dafür ein Backend-Trait, im Code gesehen), nur **auf Wunsch** in `portals.conf`. Beides erst nach dem Meilenstein.
7. **Paket** (§4): AppStream kennt dafür den Typ **`addon`** mit `<extends>` (mehrfach erlaubt, belegt). Katalog: neuer Wert `fs:kind = "module"`. Fähigkeiten nach ADR 0068; Steckplätze des Hosts sind Themen-Schnittstellen (Ziele, ADR 0045). Laden nur, was der Store signiert installiert hat.
8. **Vektor** (§5): SVG ist Austausch- und Exportformat, nicht Wahrheit (ADR 0046). **Befund:** Blinc (und damit fs-whiteboard) hängt an `resvg`/`usvg` **0.44.0 = MPL-2.0**; erst ab **0.45.0** (2025-02-26) sind sie Apache-2.0 OR MIT (heute 0.50.0). `kurbo` und `lyon` sind MIT/Apache. Graphite (Alpha, MIT oder Apache-2.0) ist **Vorbild für die Modul-Schnitte** (Knoten-Bibliotheken `vector`, `path-bool`, `text`, `brush` …), keine Abhängigkeit. **Nachtrag (Nutzer):** Vektor-Grundlage wird **VectorCraft** (`vectorcraft-geom` + `-pathops` für Geometrie und Boolesch; Darstellung bleibt Blinc) – Prüfung in `/srv/FreeSynergy/.scratch/module/VECTORCRAFT.md`; ihr Plug-in-Modell (Wasm in `wasmi`) ist der bessere erste Weg für Variante B.

---

## 1. Begriffe

### 1.1 Die sechs Begriffe

| Begriff | Was es ist | Besitzt Daten? | Zeichnet? | Wo im Code | Quelle |
|---|---|---|---|---|---|
| **Component** | Darstellung eines Grundtyps oder einer Ansicht (Eingabe, Anzeige, kompakt, Zelle; bis hin zu Raster, Kanban, Zeichenfläche) | nein | **ja, nur hier** | `fs-components` | ADR 0066 |
| **Anbieter** (provider) | Umsetzung einer **Themen-Schnittstelle** für eine Quelle (S3, SFTP, YouTube als Galerie-Quelle, Mail, Matrix) – liefert Daten **unter** den Kern | Daten der Quelle, nicht unsere | nein | eigenes Crate bzw. `fs-<prog>-<anbieter>` | ADR 0045, 0070 |
| **Modul** (neu) | fügt einem Kern eine **Fähigkeit** hinzu – Befehle, Ansichten, Aktionen – **neben** bzw. **über** den Kern; steckt in einem **Steckplatz** des Hosts | **nein** (Regel 1.2) | nein; setzt Components zusammen oder beschreibt eine Ansicht | Crate oder Agent (§2) | dieser Entwurf |
| **Programm** | **Besitzer** eines Themas (eine Wahrheit, ein Weg); Kern + Hülle + Module + Frontends; ein Befehl `fs-<prog>` | ja | nein | `fs-<prog>` | ADR 0050, 0063, 0065 |
| **Facette** | Ausschnitt eines Programms mit festem Filter, eigenem Namen, Logo, Menüeintrag; nach außen „App“ | nein | nein | Manifest des Programms | ADR 0061 |
| **Dialog** | ein Programm, gestartet im **Auswahl-Modus**: Dialog-Hülle, nur die nötigen Module, liefert ein Ergebnis an den Aufrufer zurück | nein (gibt Verweise heraus) | nein | Unterbefehl `fs-<prog> pick …` | §3 |

**Abgrenzungen in einem Satz:**
- *Anbieter vs. Modul:* Ein Anbieter beantwortet die Fragen des Kerns („was liegt in diesem Ordner?“), ein Modul stellt dem Menschen neue Fragen zur Verfügung („zeig das als Galerie“, „installiere das“). Anbieter stecken unten, Module seitlich.
- *Modul vs. Component:* Eine Component weiß nichts über Programme; ein Modul weiß, welche Schnittstelle es braucht, und wählt die Components (bzw. beschreibt die Ansicht).
- *Modul vs. Facette:* Die Facette ist, was der Mensch im Menü sieht; das Modul ist, was dafür gebaut wurde. **Facette = Filter + Auswahl von Modulen + Menüeintrag** [Vorschlag, Ergänzung zu ADR 0061 Punkt 1]. Eine Facette hat weiterhin keine eigenen Daten.
- *Modul vs. Programm:* Ein Modul kann nicht allein starten und besitzt kein Thema. Wächst ein Modul zu einer eigenen Wahrheit (es braucht eigene Objekte), wird es ein Programm, und das alte Modul spricht dann dessen Schnittstelle.
- *Achtung Wortwahl:* „Modul“ ist in Rust schon belegt (`mod`). In Code und englischer Doku braucht es ein eindeutiges Wort (Frage 1, §7).

### 1.2 Regeln für Module [Vorschlag]

1. **Keine eigene Wahrheit.** Ein Modul liest und ändert nur über Schnittstellen von Besitzern (ADR 0050). Eigene Einstellungen liegen in den Einstellungen des Hosts (Admin-Frontend, ADR 0061 Punkt 4), unter dem Modul-Namen.
2. **Steckplätze sind Themen-Schnittstellen.** Der Host bietet benannte Steckplätze an (z. B. `files.actions`, `files.views`, `files.panels`); jeder ist ein Ziel nach ADR 0045 (Entwurf → zwei Nutzer → 1.0 → nur Sprünge). Ein Modul sagt, welche Steckplätze es füllt und welche Schnittstellen es braucht (ADR 0068).
3. **Alles oder `Unsupported`.** Wie bei Anbietern (ADR 0045): jede Methode des Steckplatzes hat die Standardantwort `Unsupported`; das Frontend zeigt das Element gesperrt mit „kommt noch“ (ADR 0066). Fehlt ein Modul ganz, gilt dasselbe – Bedienelemente bleiben sichtbar, Funktionen werden nur angeschaltet.
4. **Befehle über die Typbeschreibung.** Was ein Modul an Aktionen bringt, meldet es als Befehle mit `supported` und Risikostufe (ADR 0066; Stufen aus dem Files-Kern-Entwurf §4). So erscheint „Installieren“ auf jeder Paketdatei, ohne dass Files den Store kennt.
5. **Nie still.** Lädt ein Modul nicht (Signatur, fehlende Fähigkeit, Absturz), sagt der Host es sichtbar (ADR 0065 Punkt 5, RFC 9457 `Problem`).

### 1.3 Beispiele

**Files** (Kern: `StorageRegistry`, Auswahl-Zustand, Steckbrief; ADR 0070, Files-Kern-Entwurf)

| Teil | Art | Steckplatz / Schnittstelle | Läuft | Begründung |
|---|---|---|---|---|
| Auswahl (Einträge wählen, Filter, Vorschau-Leiste) | Modul | `files.selection` | im Prozess | wird von **jedem** Dialog gebraucht; klein, eigener Code |
| Galerie (Raster nach Datum, Sammlungen/Alben) | Modul | `files.views`, braucht `storage`, Steckbrief | im Prozess | eigene Logik (Zeitachse, Alben), keine eigenen Daten (Sammlungen gehören dem Steckbrief von fs-files) |
| Galerie-Quellen YouTube, PeerTube, Vimeo | **Anbieter** | `storage` bzw. Galerie-Quelle | Agent | fremdes Netz, fremde Daten (ADR 0066 „Galerie und Studio“) |
| Installieren / Prüfen / Zurück | Modul | `files.actions`, braucht die Befehle des Store-Kerns | im Prozess, ruft **fs-store** | Wahrheit „Installationen“ bleibt beim Store (Files-Kern-Entwurf §1.3, §6 B) |
| Git (Verlauf, Vergleich, Zurückholen) | Modul | `files.panels`, `files.actions`, braucht `versions` (ADR 0071) | im Prozess | Verlauf gehört dem Repo bzw. ADR 0071, nicht Files |
| Vorschau-Decoder (Bild, PDF, Video-Standbild) | Modul | `files.preview` | **Agent** | fremde Dateien sind Angriffsfläche (Files-Kern-Entwurf §4 Stufe 1) |
| Herkunft (Steckbrief-Anzeige) | Kern | – | – | gehört zu jeder Datei, kein Zusatz |
| Facetten Galerie, Programme, Desktop | Facette | Filter + Module | – | was der Mensch im Menü sieht |

**Whiteboard** (Kern: Board, Seiten, Elemente, Merge, Undo, Raumindex – `fs-whiteboard-core`)

| Teil | Art | Steckplatz |
|---|---|---|
| Formen, Freihand, Text, Verbinder (heute) | Module | `whiteboard.tools` (Werkzeug: Zeiger-Ereignisse → Commands auf dem Kern) |
| Workflow-Graph-Ansicht (Workflow-Entwurf §3) | Modul | `whiteboard.views` + `whiteboard.palettes` (Palette nur aus Katalogbefehlen) |
| Pfad-Bearbeitung, Boolesche Operationen, Ausrichten an Kurven | Module (später) | `whiteboard.tools`, `whiteboard.ops` (§5) |
| Export SVG (heute), PDF, PNG | Module | `whiteboard.export` (Speichern ≠ Export, ADR 0046) |

**Wiki** (Kern: Blöcke mit Id, ADR 0072; Loro hinter `CollabDoc`, ADR 0073)

| Teil | Art | Steckplatz |
|---|---|---|
| Blocktypen Tabelle, Formel, Diagramm, eingebettetes Board | Module | `wiki.blocks` (Block-Art: lesen, bearbeiten, exportieren) |
| Hilfe-Modus für andere Programme (ADR 0065 Punkt 3) | Facette bzw. Dialog | `fs-wiki pick`/`show` mit Hilfe-Adresse |
| Export Markdown, HTML | Module | `wiki.export` |

Gemeinsam genutzt: das Auswahl-Modul von Files steckt im **Dialog** `fs-files pick` (§3); Export-Module können in mehreren Programmen stecken, wenn sie nur Standardformate über eine Themen-Schnittstelle lesen.

---

## 2. Modulform

### 2.1 Varianten

| | **A Rust-Crate (Übersetzungszeit)** | **B Wasm-Komponente (WIT)** | **C Prozess-Agent (IPC)** | **D Mischung: ein Vertrag, zwei Laufweisen** |
|---|---|---|---|---|
| Form | Crate mit Trait, Eintrag in eine Registry (Muster Registry/Strategy, ADR 0043); per Cargo-Feature an/aus | `.wasm` mit WIT-Welt, Host `wasmtime` (50.0.1, Apache-2.0 WITH LLVM-exception, crates.io) | eigener Prozess, lokale Verbindung, meldet Fähigkeiten (Zentinel-Muster) | Cap'n-Proto-Schnittstelle + Rust-Trait je Steckplatz; Umsetzung im Prozess (A) **oder** als Agent (C) |
| Hot-Plug | **nein** – nur an/aus zur Laufzeit; neue Version = Programm neu starten (ADR 0069, Sitzung bleibt) | ja (laden/entladen) | **ja** (starten, Handschlag, atomar tauschen) | je Modul wählbar |
| Absturz | reißt das Programm mit | gefangen | gefangen, Neustart mit Wartezeit | je Laufweise |
| Sandbox | keine | stark (nur importierte Funktionen) | Betriebssystem (eigener Nutzer/Namespace, Landlock, seccomp – **[nicht geprüft]**) + nur übergebene Cap'n-Proto-Referenzen | je Laufweise |
| Geschwindigkeit | direkt | nah an nativ, Kopieren an der Grenze **[nicht gemessen]** | IPC je Aufruf **[nicht gemessen]** | je Laufweise |
| Oberfläche | setzt fs-components direkt zusammen | **kein Standard für Oberflächen** (Befund) | nur Beschreibung (2.3) | je Laufweise |
| Sprachen | Rust | jede mit WIT-Bindings (Rust über `wit-bindgen`, CLI instabil – Befund) | jede | je Laufweise |
| Reife | voll | Component Model/WASI in Previews, Brüche möglich (Befund) | Muster erprobt (Zentinel v2) | – |
| Hauptnachteil | widerspricht wörtlich ADR 0045 „Plugins sind immer Hot-Plugins“ | zweite Schnittstellensprache neben Cap'n Proto (WIT) | Lebenszyklus, Startzeit, mehr bewegliche Teile | zwei Laufweisen zu testen |

### 2.2 Draht für Agenten: Cap'n Proto oder JSON/gRPC wie Zentinel

| | Cap'n Proto (ADR 0021, 0045) | JSON über Unix-Socket (Zentinel v2) | gRPC/Protobuf (Zentinel v2) |
|---|---|---|---|
| Ein Vertrag | **ja** – ADR 0021: „Cap'n Proto ist Quelle der Wahrheit, JSON/CLI/MCP werden daraus erzeugt“ | nein, zweiter Vertrag von Hand (verletzt ADR 0021) | nein, zweite IDL |
| Bauen ohne C++ | ja: `fs-capnpc` (reines Rust, v0.0.1) + `capnp` 0.27.3 (MIT) | ja | `protoc` bzw. Rust-Ersatz nötig **[nicht geprüft]** |
| Fähigkeiten-Sicherheit | **eingebaut**: ein Agent bekommt nur die Objekt-Referenzen, die der Host ihm gibt (z. B. eine nur-lesende `storage`-Referenz auf einen Teilbaum); Rückgabe von Objekten (`Subscription`, `Blob`) | nein | nein |
| Im Prozess gleich wie außen | ja: eine lokale Umsetzung lässt sich als Client derselben Schnittstelle benutzen (`capnp-rpc` 0.27.5, MIT) – Grundlage von Variante D; Kosten im Prozess **[nicht gemessen]** | nein | nein |
| Lesbar beim Fehlersuchen | nein (binär); JSON-Abbild aus dem Schema erzeugbar (ADR 0021) | ja | nein |
| Lizenz | C++-Referenz MIT (`LICENSE`, Repo `capnproto/capnproto`, Zweig `v2`); Rust-Crates MIT (crates.io) | – | – |

**Empfehlung: Cap'n Proto bleibt.** Von Zentinel übernehmen wir das **Muster**, nicht den Draht: eigener Prozess je Agent, Handschlag mit Fähigkeiten (bei uns `supportReport`/`TypeCatalog`), Zeitlimit je Aufruf (`call_limited`, fs-interfaces v0.0.18), Abbruch laufender Aufrufe, Größengrenze je Nachricht, Gesundheitsprüfung, Neuladen mit atomarem Tausch (`BackendRegistry`-Muster), festgelegtes Verhalten bei Ausfall (sperren und melden; nie still weiter). **ADR 0045 beim nächsten Überarbeiten präzisieren:** „Vorbild Zentinel für Prozess-Muster und Hot-Reload; Draht Cap'n Proto (ADR 0021) – bewusste Abweichung von Zentinel, das JSON/UDS oder gRPC nutzt.“

### 2.3 Oberfläche: Szenen- bzw. Ansichtsbeschreibung (ADR 0045, 0066)

- **Im Prozess (A):** Das Modul setzt Components aus `fs-components` zusammen, wie ein Frontend (ADR 0066 „Das Frontend setzt zusammen“). Kein eigenes Zeichnen.
- **Agent (C):** liefert eine **Ansichtsbeschreibung** [Vorschlag]: Baum aus Component-Namen und -Varianten (Eingabe/Anzeige/kompakt/Zelle), Daten nach Grundtypen, Befehle mit `supported`, Abstände als Stil-Token – **ohne** Pixelmaße. **Der Host misst Text und legt aus.** Damit muss kein Agent Schrift messen; die offene Stelle aus ADR 0045 („Textmessung ungelöst“) verschwindet, solange Agenten nur beschreiben.
- **Zeichnende Agenten** (z. B. ein Diagramm-Generator für das Whiteboard) liefern **Elemente des Whiteboard-Vertrags** bzw. SVG als Import (§5), nie Bildschirm-Pixel.
- Dieselbe Beschreibung erzeugt heute schon das Admin-Frontend aus der Typbeschreibung (ADR 0066). Die Ansichtsbeschreibung ist dessen Erweiterung, kein zweites System.

### 2.4 Empfehlung je Aufgabe

| Aufgabe | Laufweise | Warum |
|---|---|---|
| Eigene Module mit Oberfläche und viel Zusammenspiel (Auswahl, Galerie-Ansicht, Installieren-Aktionen, Git-Leiste, Whiteboard-Werkzeuge, Wiki-Blocktypen) | **A im Prozess**, Vertrag nach D | schnell, Components direkt; signiert mit dem Programm |
| Alles, was **fremde Eingaben** parst (Vorschau-Decoder, Import fremder Formate, SVG-Import) | **C Agent** | Absturz und Angriff bleiben draußen |
| Anbieter mit Netz (S3, SFTP, WebDAV, YouTube, PeerTube) | **C Agent** | ADR 0070 Risiko 9: „Anbieter in eigenem Prozess“ |
| Module Dritter | **C Agent** (später ggf. B) | keine fremde Software im eigenen Prozess |
| KI-Teilnehmer, Runner (`fs-tasks runner`) | C | sind ohnehin eigene Handelnde (Workflow-Entwurf N2) |
| Reine Rechenlogik Dritter, auch im Web-Frontend; Effekte, Filter, Shader | **B später** | erster Weg nach Vorbild VectorCraft: Interpreter **`wasmi`** (2.0.0, MIT/Apache-2.0, reines Rust, auch wasm32) ohne WASI, mit Befehlsbudget, Zeitlimit, Speicherdeckel, frischer Instanz je Lauf und Rechten im Manifest (`VECTORCRAFT.md` §4.1); Component Model/`wasmtime` erst, wenn stabil und nötig |

**Zum Konflikt mit ADR 0045 („Plugins sind immer Hot-Plugins“):** A-Module lassen sich zur Laufzeit an- und abschalten, aber nicht nachladen. Vorschlag: „Hot-Plug“ heißt bei uns **an/aus ohne Neustart**; **Nachinstallieren ohne Neustart** gibt es nur für Agenten. Neue A-Module kommen mit einem Update des Programms, das sich am selben Punkt neu startet (ADR 0069). Das muss der Nutzer bestätigen (Frage 2).

### 2.5 Lebenszyklus eines Agenten [Vorschlag]

`entdecken` (Manifest des installierten Pakets, nur aus der Dateiliste des Stores) → `prüfen` (Signatur und Prüfsumme gegen die Dateiliste, Fähigkeiten nach ADR 0068) → `starten` (eigener Prozess, nur die erlaubten Referenzen) → `Handschlag` (Version des Steckplatzes, `supportReport`) → `eintragen` (Registry, atomar) → `beobachten` (Gesundheit, Zeitlimits) → bei Absturz: Steckplatz gesperrt mit Meldung, Neustart mit wachsender Wartezeit, nach Grenze aus → bei Update: neuen Agenten starten, Handschlag, tauschen, alten beenden.

---

## 3. Programm als Dialog; Files als Portal-Backend

### 3.1 „Programm als Dialog“ allgemein [Vorschlag]

- Jedes Programm darf einen Unterbefehl **`pick`** haben (ADR 0063): `fs-files pick --open|--save|--save-files [--multiple] [--directory] [--filter …] [--folder …] [--name …]`, `fs-people pick` (Kontakt wählen), `fs-calendar pick` (Termin), `fs-tasks pick` (Aufgabe verknüpfen), `fs-wiki pick` (Seite/Block verlinken).
- **Dialog-Hülle** als Variante der Mindest-Hülle (ADR 0065): Titel, Abbrechen/Übernehmen, Esc schließt, Tastatur wie überall; kein Programm-Menü.
- **Geladen werden nur die Module, die der Modus braucht** (bei Files: Kern + Auswahl; Galerie-Raster nur, wenn der Filter Bilder verlangt).
- **Vertrag** (eigene kleine Themen-Schnittstelle `chooser` [Vorschlag], Muster wie Portal-Request): Eingabe = Modus, Filter (Medientypen/Datentypen), Vorauswahl, Titel, Aufrufer; Ausgabe = `ok` mit Liste von **Verweisen** (`fs://…`, IRIs) oder `abgebrochen` oder `Problem`. Codes wie beim Portal (0 = ok, 1 = abgebrochen, 2 = anders beendet).
- **Rechte:** Der Aufrufer bekommt **nur das Gewählte**, nie Lese-Rechte auf den ganzen Baum (Cap'n-Proto-Referenz auf die gewählten Einträge). Das ist das Sicherheitsmodell des Portals und passt zu ADR 0050.
- Die vorhandene Component `share_dialog` (`/srv/FreeSynergy/fs-components/crates/fs-components-widgets/src/share_dialog/`) ist ein Kandidat für denselben Rahmen (Teilen = Personen wählen über `fs-people pick`) **[Vorschlag, nicht geprüft, ob sie heute Personen selbst lädt]**.

### 3.2 Files als xdg-desktop-portal-Backend

**Belegt:**
- Vorder-Schnittstelle `org.freedesktop.portal.FileChooser` (Version 4 laut Doku): `OpenFile(parent_window, title, options)` u. a.; Optionen `accept_label`, `modal`, `multiple`, `directory` (ab Version 3), `filters` …; „The selected files will be made accessible to the application (which may involve adding it to the Documents portal)“ – das Freigeben an Sandbox-Programme macht der **Portal-Dienst**, nicht das Backend (flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.FileChooser.html).
- Backend-Schnittstelle `org.freedesktop.impl.portal.FileChooser`: `OpenFile`, `SaveFile`, `SaveFiles` mit `handle, app_id, parent_window, title, options`, Antwort `response, results` (`uris` als `file://`) (Befund).
- Rust: `ashpd` (0.14.0, MIT, crates.io) hat ein Feature `backend` (zieht `tokio`, `async-trait`) und im Code ein Trait **`FileChooserImpl`** mit `open_file`, `save_file`, `save_files` (gesehen in 0.11.1, `src/backend/file_chooser.rs` Z. 189–208). Darunter `zbus` 6.2.1, **MIT** (crates.io; im Cargo-Cache auch 5.19.0 MIT).
- Registrierung: `.portal`-Datei mit `DBusName` und `Interfaces`; Auswahl über `portals.conf` (Befund, Doku-Seite `portals.conf` vorhanden).

**Aufwand [Schätzung]:** Gerüst (Unterbefehl `fs-files portal`, D-Bus-Aktivierung, `.portal`-Datei, Weiterleitung an `pick`) klein; vollständige Optionen (`filters`, `current_filter`, `choices`, `current_folder`, `current_name`, `current_file`, `SaveFiles`) mittel; Fensterbindung und Tests mit echten Programmen (GTK, Qt, Firefox, Flatpak) mittel.

**Risiken:**
1. **Ein Fehler trifft alle Programme.** Hängt oder stürzt unser Backend, hat kein Programm mehr einen Dateidialog. Darum: **nur auf Wunsch** in `portals.conf` (Nutzer-Datei unter `~/.config/xdg-desktop-portal/`), mit Knopf „zurück zum Standard“; nie still beim Installieren. Ob der Portal-Dienst bei Ausfall auf ein anderes Backend ausweicht: **[nicht belegt]**.
2. **Fensterbindung.** `parent_window` kommt als `x11:<id>` oder `wayland:<handle>`; unter Wayland braucht das Anhängen als modaler Dialog das Protokoll xdg-foreign. Ob Blinc/winit das kann: **[nicht belegt]**. Ohne geht es als freies Fenster.
3. **Startzeit.** Ein Dialog muss sofort erscheinen. Ein vollständiges Files mit allen Anbietern ist dafür zu schwer → nur Kern + Auswahl laden (genau die Modul-Idee), Anbieter lazy.
4. **Rechte.** Das Backend läuft mit den Rechten des Menschen und sieht alles; der Aufrufer bekommt nur das Gewählte (Portal-Dienst). Entfernte Anbieter (S3, SFTP) liefern keine `file://`-URI → nur lokale Orte anbieten oder vorher herunterladen (Kopie, Export-Regel ADR 0070 §5) **[Vorschlag]**.
5. **Wer den Portal-Weg überhaupt nutzt.** Flatpak-Programme immer; GTK/Qt/Firefox/Chromium ohne Sandbox nur mit passender Einstellung – Einzelheiten **[nicht belegt]**.
6. **Reife von `ashpd`-Backend:** Trait vorhanden, Erfahrung im Einsatz **[nicht belegt]** → kleiner Spike vor der Entscheidung.

**Reihenfolge [Vorschlag]:** (1) nach dem Meilenstein: `fs-files pick` + Dialog-Hülle, zuerst nur lokale Orte (braucht `storage` noch nicht); (2) alle eigenen Import-/Export-Dialoge darauf umstellen; (3) mit ADR 0070 S4 (fs-files als Anbieter): alle Wurzeln im Dialog; (4) Spike Portal-Backend mit `ashpd`, Test mit einem Flatpak-Programm; (5) Portal-Backend als Opt-in. Windows/macOS: eigener Dialog nur für eigene Programme; Systemdialoge dort ersetzen wir nicht.

---

## 4. Fähigkeiten, Installation, Signatur, Sandbox

### 4.1 Fähigkeiten (ADR 0068)

- **Modul meldet:** `provides` = sein Name als Fähigkeit (`freesynergy-module(files.gallery) = 1.0` [Vorschlag zur Form]) und die Steckplätze, die es füllt; `requires` = Steckplätze und Themen des Hosts mit Mindestversion (`files.views ≥ 1.0`, `storage ≥ 1.0`); `recommends` z. B. Galerie-Quellen.
- **Facette meldet:** welche Module sie einschaltet; „Galerie installieren“ zieht über `requires` die Module mit (wie „Kontakte“ `people.persons` zieht, ADR 0068 §1).
- **Gleiches Modul, mehrere Hosts:** Ein Modul hängt an **Steckplätzen**, nicht an einem Programm. Jeder Host, der den Steckplatz anbietet, kann es laden (Export-Module, Auswahl).
- Laufzeit wie gehabt: der Store prüft beim Installieren, die Schnittstelle beim Benutzen (`supported`).

### 4.2 Installation, Paketart

- **AppStream (belegt):** Komponenten-Typ **`addon`**: „Some components are not standalone, but rather extend existing software … `<extends>` refers to the ID of the component this addon is extending … may be specified multiple times“; Pflicht: `id`, `name`, `summary`, `metadata_license`, `extends` (freedesktop.org/software/appstream/docs/sect-Metadata-Addon.html). Das ist der Standard für Module; kein eigenes Format.
- **Katalog:** heute nur `kind = "program"` (`/srv/FreeSynergy/fs-catalog/packages.toml`, `catalog.xml` `fs:kind`). Neu: `kind = "module"` ↔ AppStream `type="addon"`. Paketart „module“ gibt es noch nicht (Befund bestätigt).
- **Wo der Code liegt:**
  - A-Module (im Prozess) sind **Teil des Programmpakets**; im Katalog trotzdem als `addon`-Komponente sichtbar (wie Facetten, ADR 0061 Punkt 7: mehrere Komponenten je Paket). „Installieren“ heißt hier „einschalten“.
  - C-Agenten und Dritte sind **eigene Pakete** `fs-<host>-<modul>` (wie `fs-files-<anbieter>`, ADR 0070 S12) mit eigener Version.
- Store schreibt für Module dieselbe Dateiliste und dieselben AS2-Aktivitäten wie für Programme (Files-Kern-Entwurf §1.3).

### 4.3 Signatur

- Gleiche Kette wie Programme: TUF-Metadaten im Katalog, OpenPGP je Artefakt, Spiegel neu signiert (ADR 0062, 0068). **Kein eigener Schlüssel je Modul** [Vorschlag]; Dritte bekommen später eine **TUF-Delegation** (Unterrolle je Herausgeber) statt unseres Schlüssels.
- **Laden nur aus der Dateiliste des Stores:** Der Host lädt kein Modul aus einem beliebigen Pfad; er fragt den Store („ist diese Datei Teil eines installierten, signierten Pakets, Prüfsumme ok?“, `fs-store verify`). Eine geänderte Datei (rot) wird nicht geladen.

### 4.4 Sandbox und Berechtigungen

- **A:** keine Sandbox, deshalb nur eigene, mit dem Programm signierte Module.
- **C:** eigener Prozess, eigene Umgebung; **Berechtigungen = übergebene Cap'n-Proto-Referenzen** (nur lesen, nur Teilbaum, kein Netz, sofern nicht gemeldet und genehmigt). Betriebssystem-Schranken (Namespaces, Landlock, seccomp, bubblewrap) **[nicht geprüft]** – gleiche offene Prüfung wie „starten“ im Files-Kern-Entwurf §4.
- **Bei der Installation sichtbar:** was das Modul braucht (Steckplätze, Themen, Netz, Schreiben), Zuwachs gegenüber der vorigen Version hervorgehoben (wie Fähigkeiten, Files-Kern-Entwurf §4 Stufe 4).
- **Risikostufen** der Befehle eines Moduls stehen in seiner Typbeschreibung; ein Modul kann keine höhere Stufe auslösen, als der Host freigibt.

---

## 5. Vektor-Grundlage und ein modulares Whiteboard

### 5.1 Standard und Crates

**Nachtrag (Nutzer, 2026-11-12):** Geometrie und Pfad-Operationen kommen aus **VectorCraft** (`vectorcraft-geom`, `vectorcraft-pathops`, MIT OR Apache-2.0, auf `kurbo` 0.13 und `linesweeper`); die Tabelle unten bleibt für Darstellung (Blinc: `lyon`, `usvg`) und SVG-Import gültig. Einzelheiten, Risiken (`[patch]`, keine crates.io-Veröffentlichung) und Abbildung auf fs-whiteboard: `/srv/FreeSynergy/.scratch/module/VECTORCRAFT.md`.

- **SVG** ist Austausch- und Exportformat; **Wahrheit bleibt das eigene Modell** (Elemente in fs-objects bzw. später Loro, ADR 0073; Speichern ≠ Export, ADR 0046). fs-whiteboard exportiert schon SVG (DESIGN.md).

| Crate | Version / Lizenz (crates.io, 2026-11-12) | Kann | Grenzen | Rolle |
|---|---|---|---|---|
| `usvg` / `resvg` | 0.50.0, **Apache-2.0 OR MIT** (seit 0.45.0, 2025-02-26; **davor MPL-2.0**) | SVG parsen und vereinfachen (`usvg`), rendern (`resvg`, CPU über tiny-skia); Text wird **ohne Systembibliotheken** gesetzt (Schriften über `fontdb`) | keine Animation, kein `script`, `a`, `view`, `cursor`, keine Ereignisse; SVG 2 „being worked on“; nur UTF-8 (README „Limitations“) | **Import** fremder SVG (als Agent, fremde Eingabe), Vorschau, Export-Prüfung |
| `kurbo` | 0.13.1, Apache-2.0 OR MIT | 2D-Kurvengeometrie (Bezier, Affine, Formen) | Boolesche Operationen **[nicht belegt]** | Geometrie im Kern (Treffer, Grenzen, Pfadbearbeitung) |
| `lyon` | 1.0.19 (`lyon_tessellation` 1.0.23), MIT OR Apache-2.0 | Pfade in Dreiecke für die GPU zerlegen | – | Zeichnen auf der GPU (steckt schon in Blinc `blinc_gpu`) |
| `vello` | 0.12.0, Apache-2.0 OR MIT | GPU-Renderer für 2D-Vektoren | Eignung für Blinc **[nicht geprüft]** | nur zur Kenntnis |

**Befund Abhängigkeit (wichtig, aber nicht dringend):** Blinc `blinc_svg` hängt an `resvg`/`usvg` **0.44.0**, `kurbo` 0.11.3 (`/srv/FreeSynergy/blinc/Cargo.lock`; dieselben Versionen in `/srv/FreeSynergy/fs-whiteboard/Cargo.lock`). 0.44.0 steht im eigenen Manifest als **MPL-2.0** (Cargo-Cache und crates.io). MPL-2.0 ist mit unseren Lizenzen verträglich, verlangt aber den Quellcode der MPL-Dateien bei Weitergabe (unser Spiegeln mit Quellcode, ADR 0068 §2, deckt das); die Aussage „permissiv“ im Befund stimmt erst ab 0.45.0. Anheben ist eine Änderung **in Blinc** (Upstream-Regel: dort ohne KI-Zuschreibung, git-bug-Trailer) → als git-bug-Kandidat notieren, nicht vor dem Meilenstein.

**Korrektur zum Befund:** „Kein natives Text-Rendering“ heißt bei resvg nicht „kein Text“, sondern „Text ohne Systembibliotheken“ – das ist für uns ein **Vorteil**: gleiche Maße auf allen Systemen, also eine mögliche gemeinsame Textmessung für Host und Export **[Vorschlag, nicht gemessen]**.

### 5.2 Graphite als Vorbild (nicht als Abhängigkeit)

- Belegt (README): „vector and raster graphics engine … in alpha … nondestructive editing workflow that combines layer-based compositing with node-based generative design“, „built more like a game engine“; „The editor's tools wrap its node graph core“. Lizenz MIT oder Apache-2.0 nach Wahl (README; GitHub zeigt nur Apache-2.0, die README ist maßgeblich).
- Aufbau (Ordnernamen, GitHub-API): `node-graph/` mit `nodes/` = `vector`, `path-bool`, `text`, `brush`, `raster`, `transform`, `blending`, `repeat`, `vectorize`, `math`, `graphic`, `gcore`, `gstd`; daneben `node-macro`, `graph-craft`, `interpreted-executor`; `libraries/` u. a. `snapping`, `math-parser`. Wie Knoten gebaut und geladen werden: **[nicht belegt]** (nicht im Code gelesen).
- Lehre für uns: **Werkzeuge sind eine dünne Schicht über einem Kern aus Operationen**; jede Fähigkeit (Boolesch, Text auf Pfad, Wiederholen, Vektorisieren) ist eine eigene Bibliothek. Genau das sind unsere Modul-Schnitte.

### 5.3 Modul-Schnitte, damit das Whiteboard zu einem vollen Vektorprogramm wachsen kann [Vorschlag]

| Schicht | Inhalt | Steckplatz | Heute |
|---|---|---|---|
| Kern | Board, Seite, Element, Stil, Gruppe, Reihenfolge, Merge je Eigenschaft, Undo als Command, Raumindex | – | da (`fs-whiteboard-core`) |
| **Element-Arten** | Rechteck, Ellipse, Freihand, Text, Verbinder, Bild … neue Art = Modul mit Geometrie (Grenzen, Treffer), Merge-Einheiten, Export-Abbild | `whiteboard.kinds` | im Kern fest verdrahtet |
| **Werkzeuge** | Zeiger-Ereignisse → Commands (Formen, Stift, Pfad-Knoten, Messer, Pipette) | `whiteboard.tools` | – |
| **Operationen** | reine Funktionen Element(e) → Element(e): Boolesch, Versatz, Vereinfachen, Ausrichten, Verteilen, Wiederholen; jede als Command mit `invert` | `whiteboard.ops` | Ausrichten, Gruppen im Kern |
| **Ansichten** | freie Fläche, Workflow-Graph, Folien, Raster | `whiteboard.views` | – |
| **Import/Export** | SVG (heute Export), PDF, PNG, später fremde Formate als Agent | `whiteboard.export`, `whiteboard.import` | SVG-Export im Kern |
| Darstellung | Zeichenfläche, Griffe, Lineale als Components | `fs-components` | ADR 0066 |

Zwei Bedingungen, damit das trägt:
1. **Neue Element-Arten müssen sich ohne Kern-Änderung anhängen lassen.** Heute steht die Liste der Arten im Vertrag `whiteboard.capnp` (fs-interfaces). Vorschlag für den nächsten Sprung des Vertrags: eine Art „Pfad“ (SVG-Pfaddaten + Stil) als allgemeine Form; Spezial-Arten bleiben, wo sie Merge-Vorteile haben. Unbekannte Arten werden gelesen und unverändert weitergegeben (wie unbekannte Werte in `tasks.capnp`).
2. **Operationen sind reine Funktionen** (ohne Store), wie `merge` und `readiness` – testbar und als Modul austauschbar.

---

## 6. Was vor dem Meilenstein NICHT angefasst wird

Meilenstein „Wir benutzen es selbst“ (GitHub + Releases, Store, Tasks als Arbeitsbrett, Wiki mit Doku, Files-Optik, Server-Pakete) geht vor. Bis dahin:
1. **Kein ADR, kein Code, kein neues Repo** für Module, Steckplätze, Agenten oder `chooser`.
2. **Keine Schema-Änderung** in `fs-interfaces` (kein Steckplatz, kein `chooser.capnp`, keine neue Whiteboard-Art).
3. **Kein Portal-Backend**, kein `fs-files pick`, kein Eintrag in `portals.conf`.
4. **Kein `kind = "module"`** im Katalog, keine `addon`-Komponenten.
5. **Keine Abhängigkeits-Anhebung** in Blinc (resvg 0.44 → ≥ 0.45) – nur als git-bug-Kandidat notieren.
6. **Kein Umbau** von Files, Store, Whiteboard in Module; Facetten-Manifest bleibt, wie es ist.
7. **Kein Wasm-Host**, kein Agenten-Rahmen.

**Schon jetzt erlaubt, weil es nichts erschwert (nur beim ohnehin Anfassen):**
- Neue Funktionen hinter **Traits mit Standardantwort `Unsupported`** bauen und als Befehle mit `supported` melden (gilt ohnehin, ADR 0045/0066) – das ist schon die Modulnaht.
- Keine Darstellung außerhalb von `fs-components` (ADR 0066).
- Im Whiteboard Operationen als reine Funktionen halten.
- Keine Abhängigkeit von fs-files auf fs-store oder umgekehrt (Files-Kern-Entwurf §7).

---

## 7. Offene Fragen an den Nutzer

---
1. **Wort:** „Modul“ ist in Rust schon belegt (`mod`). Deutsch „Modul“ für Menschen, im Code und auf Englisch **„extension“**? Oder ein anderes Wort („Baustein“, „Zusatz“)?
2. **Hot-Plug:** Darf „Hot-Plug“ für eigene Module **an/aus ohne Neustart** bedeuten, während **Nachinstallieren ohne Neustart** nur für Agenten (eigene Prozesse) gilt? Sonst müsste jedes Modul ein eigener Prozess sein (langsamer, mehr Teile).
3. **Draht:** Cap'n Proto bleibt für Agenten (ADR 0021), Zentinel nur Vorbild für das Prozess-Muster – einverstanden? Dann wird ADR 0045 nur klarer formuliert, nicht geändert.
4. **Facette = Filter + Module + Menüeintrag:** So in ADR 0061 ergänzen? Dann bleiben Galerie, Programme (Installer), Git für den Menschen Facetten bzw. Apps, im Code sind es Module.
5. **Portal-Backend:** Soll Files später auf Wunsch der Dateidialog **aller** Programme werden (xdg-desktop-portal), oder reicht `fs-files pick` für unsere eigenen Programme?
6. **Module Dritter:** Erlauben wir später Module von anderen Herausgebern (eigene TUF-Unterrolle, immer als eigener Prozess)? Oder vorerst nur eigene?
7. **Whiteboard-Ziel:** Soll das Whiteboard wirklich zu einem vollen Vektorprogramm wachsen (dann jetzt schon eine allgemeine Art „Pfad“ beim nächsten Vertragssprung vormerken), oder bleibt es Tafel und Diagramm, und ein Vektorprogramm wird ein eigenes Programm mit denselben Modulen?

---

## 8. Nachprüfung zum Befund (Abruf 2026-11-12)

| Punkt | Ergebnis | Quelle |
|---|---|---|
| Zentinel-Agentenprotokoll | **belegt:** „Dual Transport Support: Unix Domain Sockets (default) and gRPC“; „UDS Message Format: 4-byte big-endian length prefix + 1-byte type prefix + JSON payload“; „gRPC Format: Protocol Buffers over HTTP/2“; max. 16 MB (UDS) / 4 MB (gRPC); Abbruch laufender Anfragen; `AgentCapabilities`. `docs/v2/protocol.md` lieferte keinen Inhalt. | `raw.githubusercontent.com/zentinelproxy/zentinel/main/crates/agent-protocol/README.md` |
| ADR 0045 vs. Zentinel | „Bei uns mit Cap'n Proto“ ist mit ADR 0021 („Cap'n Proto ist Quelle der Wahrheit“) gewollt; Abweichung von Zentinel bewusst, nicht Irrtum | ADR 0021, 0045 (`origin/main`) |
| Cap'n Proto Lizenz | C++-Referenz **MIT** („Licensed under the MIT License“); `capnp` 0.27.3 und `capnp-rpc` 0.27.5 **MIT** | `raw.githubusercontent.com/capnproto/capnproto/v2/LICENSE`; crates.io API |
| zbus | 6.2.1 **MIT** (rust-version 1.89); Cache 5.19.0 MIT | crates.io API; `zbus-6.2.1/Cargo.toml` |
| ashpd | 0.14.0 **MIT**; Feature `backend`; Trait `FileChooserImpl` (`open_file`, `save_file`, `save_files`) in 0.11.1 | crates.io API; `ashpd-0.11.1/Cargo.toml`, `src/backend/file_chooser.rs` |
| kurbo | 0.13.1 **Apache-2.0 OR MIT** | crates.io API |
| lyon | 1.0.19 **MIT OR Apache-2.0**; `lyon_tessellation` 1.0.23 | crates.io API |
| resvg/usvg | 0.50.0 **Apache-2.0 OR MIT**; Lizenzwechsel von **MPL-2.0** mit **0.45.0** (2025-02-26); Blinc und fs-whiteboard nutzen **0.44.0 (MPL-2.0)** | crates.io API (Versionsliste); `Cargo.lock` beider Repos |
| resvg Grenzen | keine Animation, „No native text rendering“ = ohne Systembibliotheken, SVG-Teilmenge ohne `a`, `script`, `view`, `cursor`, SVG 2 in Arbeit | `raw.githubusercontent.com/linebender/resvg/main/README.md` |
| wasmtime | 50.0.1, Apache-2.0 WITH LLVM-exception | crates.io API |
| vello | 0.12.0, Apache-2.0 OR MIT | crates.io API |
| Graphite | Alpha; MIT oder Apache-2.0 nach Wahl (README „License“); Ordner `node-graph/nodes/*` wie in §5.2; letzter Push 2026-11-11 | README; GitHub-API `contents/`, `repos/GraphiteEditor/Graphite` |
| AppStream `addon` | belegt, Zitat §4.2 | freedesktop.org/software/appstream/docs/sect-Metadata-Addon.html |
| Portal FileChooser (Vorderseite) | Version 4, Optionen und Documents-Portal belegt, Zitat §3.2 | flatpak.github.io/xdg-desktop-portal/docs/doc-org.freedesktop.portal.FileChooser.html |
| Paketart „module“ | nicht vorhanden, nur `kind = "program"` | `/srv/FreeSynergy/fs-catalog/packages.toml`, `catalog.xml` |
| Nicht geprüft | Sandbox-Werkzeuge (Landlock, bubblewrap, seccomp); Portal-Ausweichen bei Backend-Ausfall; xdg-foreign in Blinc/winit; Booleans in kurbo; Graphite-Knotenmechanik im Code; Leistung Cap'n Proto im Prozess | – |
