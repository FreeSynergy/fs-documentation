# 0077 – Katalog-Arten (`kind`) und Store-Gruppen; Server nur mit rpm/deb

Status: **akzeptiert** (Strategie, 2026-11-14; Nutzerregel zu Punkt 3: alle Server kommen in den Katalog und sind überall installierbar) · baut auf ADR 0061 (Facetten), 0062 (ein Katalog-Repo), 0064 (Versionen), 0068 (gespiegelte Pakete), 0074 (Schichten, Gruppen im Store), 0075 (Store zeigt Server)

## Kontext
Kein ADR legt die `kind`-Werte des Katalogs fest. Ist-Zustand `fs-catalog` main: nur `kind = "program"`, AppStream-Typ fest `desktop-application`. Schema 2 (Branch `unreviewed/catalog-schema2`) kennt `server`, `icon-theme`, `component` (Entwurf). Der Store-Leser verwirft unbekannte Werte (`Skipped`); `PackageKind` in `store.capnp` hat 4 Werte. ADR 0074 verlangt je Schicht eine Store-Gruppe, „ebenso Programme und Server“, nennt aber keinen Wert für Programm und Server. Auslöser: `fs-kanidm` soll als Server in den Katalog.

## Entscheidung
### 1. `kind` ist die Store-Gruppe
Eine Eigenschaft, keine zweite Kategorie daneben. Werte: `program`, `server`, `frontend`, `theme`, `icon-theme`, `motion`, `sound-theme`, `haptics`, `shortcuts`, `language`. Abweichungen von der Tabelle in ADR 0074: `program` und `server` stehen dort nicht (nur im Satz zu den Gruppen); der Schema-2-Entwurf kennt zusätzlich `component`, das hier **nicht** übernommen wird (Bausteine gehören zum Stil, 0074). **Facette** (0061) bleibt ein eigener Begriff (Ausschnitt eines Programms) und ist **kein** `kind`; ein Katalogeintrag je Facette bleibt nach 0061 §7 möglich und trägt das `kind` seines Programms.

### 2. AppStream-Typ je `kind`
Belegt gegen die AppStream-Spezifikation (freedesktop.org/software/appstream/docs, gelesen 2026-11-14):

| kind | AppStream `type` | Beleg |
|---|---|---|
| `program` | `desktop-application` (Programm nur mit Kommandozeile: `console-application`) | „A console application is any application that has a command-line or text-based interface“; `desktop-application` im Bestand (`gen_catalog.py`) |
| `server` | `service` | „A service component is any software that is started and supervised by the Operating Systems ‚init‘ facility, such as systemd.“ |
| `icon-theme` | `icon-theme` | „`type` set to `icon-theme` … describing an icon theme following the Freedesktop specification“ |
| `language` | `localization` | „describes language packs for individual software components“ |
| `frontend`, `theme`, `motion`, `sound-theme`, `haptics`, `shortcuts` | `addon` | „Some components are not standalone, but rather extend existing software“; `<extends/>` nennt das erweiterte Programm. Dass diese sechs Arten darunter fallen, ist **unsere Zuordnung**, die Spezifikation nennt sie nicht |

Das Feld `fs:kind` bleibt zusätzlich im Katalog; der AppStream-Typ ersetzt es nicht.

### 3. Server: rpm, deb, Container
Für `kind = server` Pflicht: **rpm, deb und OCI-Container**, jeweils signiert (OpenPGP, 0062), mit systemd-Unit und Systembenutzer. Der Tarball bleibt zusätzlich (Quellcode-Tarball nach 0068 ohnehin). **Ein Server kommt erst in den Katalog, wenn mindestens rpm ODER deb vorliegt**; ein Tarball allein genügt nicht (Systemdienst, Root, PAM-Module lassen sich mit der Nutzer-Tarball-Installation des Stores nicht abbilden). Nutzerregel: **alle Server im Katalog, überall installierbar** (Store-Programm, Repo für deb/rpm, Container, Kommandozeile `fs-store`), so viele Schnittstellen wie möglich.

### 4. Versionen, Namen, Icons gespiegelter Server
- **Version:** Upstream-Version (ADR 0064 gilt nur für eigene Programme). Eigene Paketänderungen als **Paket-Revision** (`1.12.1-1`, `-2` …, wie Debian-Revision und RPM-Release). Tag im Paket-Repo `v1.12.1`.
- **Name:** der Upstream-Name („Kanidm“, nicht `FreeSynergy.*`); Beschreibung z. B. „Identitätsserver, gespiegelt und signiert von FreeSynergy“.
- **AppStream-ID:** Upstream-rDNS, wenn Upstream eine führt. Gelesen: `kanidm/kanidm` (Zweig `master`) enthält **keine** `.metainfo.xml`/`.appdata.xml`/`.desktop`-Datei; eine Upstream-ID ist daher **[nicht belegt]**. Vorschlag: aus der Upstream-Domain `kanidm.com` abgeleitet, `com.kanidm.Kanidm`, bis Upstream eine nennt (dann Wechsel mit `<provides><id>` für die alte ID).
- **Icon:** `kanidm/kanidm` `artwork/README.md`: „All artworks are licensed as CC-BY-NC-ND.“ (das Repo selbst: MPL-2.0). „NC“ und „ND“ erlauben weder freie Weitergabe in unserem Sinn noch Anpassung (Größen, Symbolic-Fassung); das Upstream-Logo wird **nicht** verwendet. Stattdessen ein **neutrales Server-Icon aus unserem Icon-Satz**. Fragt Upstream später ausdrücklich um Erlaubnis, kann das geändert werden [nicht belegt].

## Folgen
Reihenfolge der Umsetzung (aus dem Bericht):
1. fs-interfaces: `PackageKind` um `server`, `iconTheme` (und die übrigen Werte) erweitern, Tag.
2. fs-store: Leser (`catalog.rs`), `words.rs`, `wire.rs`, Gruppen in der Oberfläche; `min_store` prüfen.
3. fs-catalog: Schema 2 reviewen und nach main (`kind`, `min_store`, AppStream-Typ aus der Tabelle, Prüfung „Server braucht rpm oder deb“).
4. fs-kanidm: rpm, deb, Container bauen und signieren; Icon aus unserem Satz; Revision-Zählung.
5. Katalog-Eintrag `fs-kanidm`, erst nach 2 und 3 (`gen_catalog.py --check`).
6. Installation von Servern im Store (Systempaket statt Nutzer-Tarball): eigenes Konzept, größtes Risiko.

## Alternativen (verworfen)
- **A: `kind = server` im alten Schema 1:** setzt den Typ fest auf `desktop-application` (falsch), kein `min_store`, alte Stores werfen den Eintrag still weg; jeder Umstieg auf Schema 2 fasst ihn erneut an.
- **C: zweiter Katalog für Server:** widerspricht ADR 0062 (ein Katalog-Repo, ein Vertrauenskreis, eine TUF-Kette) und dem Nutzerwunsch „alle Server im Katalog“.
- Eigene Kategorie neben `kind`: zwei Wahrheiten für dieselbe Gruppe.

## Offen
- Upstream-AppStream-ID von Kanidm [nicht belegt]; Vorschlag oben.
- Ob Upstream das Logo freigibt [nicht belegt].
- Zuordnung der sechs Stil-Arten zu `addon` ist keine Vorgabe der Spezifikation.
- Container-Registry und Signatur der Container (z. B. Sigstore/OpenPGP) noch nicht entschieden.
- Installationskonzept für Systemdienste (Folge 6).
- Module/Handler für eingebettete Inhalte (Embed: jedes eingebettete Ding nennt Medientyp und nötiges Modul, Files holt den Handler): eigene Art `module` oder `addon` mit `<extends/>`. Die Entscheidung folgt, sobald Embed gebaut wird.

## Nachtrag 2026-11-14: Katalogart `workflow`
Der `kind`-Wert `workflow` (anbietbare Abläufe, z. B. `server-einrichtung`, ADR 0079) kommt zur Tabelle in §1 hinzu. AppStream-Typ: `addon` mit `<extends>` `fs-workflows`. Diese Zuordnung ist **unsere**, die Spezifikation gibt sie nicht vor (wie bei den Stil-Arten in §2). Das Angebot läuft über den Katalog, `fs-marketplace` später.

| kind | AppStream `type` | Beleg |
|---|---|---|
| `workflow` | `addon` (`<extends>` `fs-workflows`) | Unsere Zuordnung; „Some components are not standalone, but rather extend existing software“ (Spezifikation, nur zur Art `addon`) |
