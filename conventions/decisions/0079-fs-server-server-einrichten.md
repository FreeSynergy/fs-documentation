# 0079 – `fs-server`: Server einrichten und verwalten, jeder Schritt protokolliert

Status: **akzeptiert** (Strategie, 2026-11-14; Nutzerentscheidung 14.11.) · baut auf ADR 0021 (Motor und Frontend), 0063 (ein Befehl), 0066 (vier Frontends), 0067 (Tresor), 0076 (Grundmodell), 0077 (Server im Katalog) · hängt ab von ADR 0078 (Paketquellen apt/dnf)

## Kontext
Ein Server wird heute von Hand aufgebaut. Der Nutzer: Mit SSH-Zugang muss ein Server **korrekt** aufgebaut werden, und daraus entsteht ein Workflow, mit dem der nächste Server **automatisch genauso** aufgebaut wird, anbietbar für alle, mit und ohne Oberfläche. Bestand (gelesen): ADR 0077 nimmt `fs-kanidm`, `fs-zentinel`, `fs-tuwunel` als Art `server` in den Katalog („Server: rpm, deb, Container“), und lässt „Installation von Systemdiensten“ offen (Folge 6). `fs-store` installiert Nutzer-Pakete, startet aber keinen Dienst und kennt kein `podman`/`quadlet` (Bestandsaufnahme 2026-11-14). `fs-workflows` hat nur README und DESIGN, **keinen Code**; Serverless Workflow 1.0 mit FS-Profil ist festgelegt (ADR 0076 §1). Kein ADR behandelt SSH-Ausführung, Plattenaufbau oder Protokollierung von Befehlen auf fremden Rechnern.

## Einschlägige ADRs (Zitate)
- 0076 §1: „Ablauf … Schritte, Aktionen der Programme, Akteur je Schritt“ = **fs-workflows**; „Ziel ≠ Ablauf“; „Geschehen ist unveränderlich“ = **fs-history**. §2: „Jedes Programm veröffentlicht **ein** Manifest“; Prüffrage „wessen Daten?“ (§1, Regel 3).
- 0021: „Programm ↔ Frontend wie Backend ↔ Frontend … JSON-API, CLI und MCP-Tools werden **daraus erzeugt**“; Risikomarken „gesetzt von der Engine und nie vom Aufrufer“.
- 0066: „Admin: alle Felder, alle Einstellungen, alle Befehle. **Aus der Typbeschreibung erzeugt**“; „Das Programm liefert nur Daten und die Schnittstelle“; Befehle melden `supported`.
- 0063: „`fs-x` … Server und Rechner ohne Bildschirm bauen mit `--no-default-features`“ (Feature `gui`).
- 0067: „Kein Programm hält eigene Geheimnisse“; 0071: „Zugang über Tresor-Verweis … im Ziel steht nur der Verweis; nie in Dateien, auf der Kommandozeile oder in der URL“; SSH nur über System-`ssh` hinter Adapter, „`Unsupported` mit Hinweis“; Hostschlüssel beim ersten Verbinden dem Menschen zeigen.
- 0020: Aktivitätsprotokoll „nur anhängen“. 0056: „Agenten laufen immer in einer eigenen Sandbox“; „Ein Agent darf niemals Admin werden“. 0077: Server kommen als rpm/deb/Container mit systemd-Unit und Systembenutzer. 0068: fremde Pakete gespiegelt und signiert, Fähigkeiten provides/requires.

## Einordnung („wessen Daten?“)
`fs-server` ist ein **Programm** (nicht Facette, nicht Suite): Es besitzt **Server-Inventar** (welche Server es gibt, Anbieter, Adresse), **Variablen-Sätze** je Server (Host, Platten, Partitionsgrößen, RAID, Dateisystem, Hostname, Netz, Dienste), **Ausführungsprotokolle** und **Verweise** auf Zugangsdaten. Kein anderes Programm besitzt diese Daten. Abgrenzung: **fs-workflows** liefert die Engine und die Ablauf-Beschreibung, besitzt aber keine Server-Daten; **fs-store/fs-marketplace** installieren Programme auf einem Gerät, `fs-server` baut das Gerät (Betriebssystem, Platten, Dienste) und nutzt dafür Katalogpakete (0077); **fs-hub** verbindet Programme auf einem Gerät und bleibt unberührt; **fs-vault** hält die Schlüssel; **fs-history** ist der unveränderliche Verlauf; die Admin-Workbench (0066) ist ein Frontend, kein Besitzer.

## Entscheidung
1. **Programm `fs-server`**, Befehl `fs-server` mit Unterbefehlen (0063), Feature `gui` abschaltbar. Engine und Frontends getrennt (0021): **CLI zuerst**, später TUI, GUI, Admin (0066, aus der Typbeschreibung erzeugt).
2. **Die Engine führt Workflows per SSH aus.** Ein Ablauf ist ein Serverless-Workflow (FS-Profil) in `fs-workflows`; `fs-server` liefert die SSH-Aktionen (Befehl ausführen, Datei schreiben, Paket installieren …) als Manifest (0076 §2) und die Variablen. Mit und ohne GUI dieselbe Engine.
3. **Keine Wartezeit auf die fs-workflows-Engine (F1).** Eine minimale Ausführung entsteht jetzt als **Keim der fs-workflows-Engine, in `fs-workflows`** (Crate): Workflow-YAML lesen, Schritte nacheinander, Gates, Wiederaufnahme, Protokoll. Brücke für `node1` bis dahin: ein **protokollierendes Wrapper-Skript** (jeder Befehl, Ausgabe, Exit-Code, Dauer); sein Protokoll wird zur Workflow-YAML.
4. **Protokoll (F5):** je Befehl Befehl, Ausgabe (Standard, Fehler), Exit-Code, Beginn, Dauer, Schritt, Lauf-ID. Das **volle Protokoll hängt nur an** und liegt in `fs-server` (0020); je Schritt geht eine **Zusammenfassung als AS2-Aktivität** an `fs-history`. Geheimnisse werden vor dem Schreiben geschwärzt und stehen nie im Befehl (Übergabe über Umgebung oder Standardeingabe).
5. **Variablen je Server** in einem Satz (Schema Teil der Typbeschreibung): Host, Platten, Partitionsgrößen, RAID, Dateisystem, Hostname, Netz, Dienste. Der Ablauf bleibt gleich, nur der Satz wechselt; so wird der nächste Server „genauso“ gebaut.
6. **Rückwärts (F7, Phase 2):** Der Schritt `bestand` liest einen vorhandenen Server (`lsblk`, Pakete, Units, Netz) und erzeugt daraus einen Variablen-Satz.
7. **Anbieter austauschbar** (Ports and Adapters, 0043/0066); Anbieter-Adapter sind **optional** (siehe Nachtrag). Der Adapter **Hetzner** kann Rescue-System und `installimage` mit einer aus den Variablen erzeugten Konfiguration bündeln; ein **ZFS-Spiegel** ist ein eigener Schritt danach (F2). Standard ist „ein System mit SSH“: Absicherung, Paketquelle (0078), Dienste. **NixOS (nixos-anywhere) später als Anbieter-Adapter (F8).**
8. **Katalogart `workflow` (F3):** anbietbare Abläufe kommen als neue Art `workflow` in den Katalog (Nachtrag in ADR 0077; AppStream `addon` mit `<extends>` `fs-workflows`, **unsere Zuordnung**). Das Angebot läuft über den Katalog, `fs-marketplace` später.
9. **SSH (F4):** System-`ssh` hinter einem Adapter (Trait, wie ADR 0071); eine Rust-Bibliothek kann später hinter denselben Trait.
10. **Sicherheitsregeln:**
   - SSH-Schlüssel **nie im Klartext**: im Satz nur ein Verweis auf Tresor/ssh-agent (0067, 0071); Schlüsselmaterial wird nie gespeichert, protokolliert oder an eine KI gegeben. Hostschlüssel beim ersten Verbinden dem Menschen zeigen und merken (0071).
   - **Gate `human`** vor jedem Schritt mit Datenverlust (Neuinstallation, Platten löschen/partitionieren, RAID neu).
   - **Trockenlauf:** Plan (alle Befehle, aufgelöste Variablen) vor der Ausführung; Ausführung nur nach Bestätigung.
   - **Idempotenz:** jeder Schritt prüft den Ist-Zustand; **Wiederaufnahme** ab dem letzten gelungenen Schritt.
   - **Agenten (F6)** geben **nie** `human`-Gates frei (0056). Läufe, deren Schritte alle `gate=none` sind (z. B. Sicherheitsupdates), dürfen Agenten und Zeitpläne starten; Protokoll wie immer.
11. **Tests ohne echten Server:** SSH-Fake (Aufzeichnung/Wiedergabe), Container und VM (QEMU) für Platten-, RAID- und ZFS-Schritte.

## Nachtrag 2026-11-14 (Nutzer): Ausgangspunkt immer SSH-Zugang
1. Ausgangspunkt ist **immer ein vorhandenes System mit SSH-Zugang** (Root-Server, VServer). Rescue, Robot und vKVM sind **keine Voraussetzung**; ein Neustart geschieht nur per `reboot` aus der Sitzung.
2. Anbieter-Adapter mit Rescue/`installimage` sind **optional**, nicht Standard; die Phase „Rescue → installimage“ ist ein optionaler Adapter-Workflow.
3. **Standardweg:** unsere Schicht („Biotop“: Paketquelle, Dienste, Daten unter `/srv/freesynergy`) auf das vorhandene System, unabhängig von der Plattenaufteilung.
4. **Plattenumbau** ist ein eigener, optionaler Workflow mit Risiko-Hinweis und Gate `human` (z. B. Root per abgebautem RAID1-Spiegel verkleinern, ZFS-Spiegel auf den Rest).
5. Der Workflow `server-einrichtung` richtet sich danach aus.

## Alternativen
| Option | Lizenz (Quelle: LICENSE-Datei im Repo, gelesen 2026-11-14) | Bewertung |
|---|---|---|
| Ansible | GPL-3.0 (`ansible/ansible`) | Nur Werkzeug, kein Eigentümer der Server-Daten, kein Protokoll jedes Befehls in unserem Format, Python, Abläufe in eigener Sprache statt Serverless Workflow; als Ausführer ersetzbar, nicht als Kern. |
| Terraform | BUSL-1.1 (`hashicorp/terraform`) | Nicht frei im Sinn von ADR 0016/0051; OpenTofu (MPL-2.0) frei, aber auf Cloud-Ressourcen, nicht auf Platten/RAID per Rescue-SSH ausgelegt [Eignung nicht geprüft]. |
| NixOS / nixos-anywhere | nixos-anywhere MIT | Deklarativ, sehr nah am Ziel „genauso“; aber an ein Betriebssystem gebunden und Nix-Sprache; wir wollen Debian/Fedora mit Katalogpaketen (0077). Als **Anbieter-Adapter später** (Entscheidung 7). |
| cloud-init | Apache-2.0 oder GPL-3.0 (Dateien `LICENSE-Apache2.0`, `LICENSE-GPLv3` in `canonical/cloud-init`) | Läuft beim ersten Start des Systems, nicht für Rescue/Platten; ergänzend nutzbar. |
| Hetzner `installimage` | eigene Lizenz „can be used and modified freely“ (`hetzneronline/installimage`) | Wird **genutzt**, nicht ersetzt (Entscheidung 7). |
| Eigene Engine auf fs-workflows | MIT OR Apache-2.0 (0016) | Gewählt: einheitlich mit 0076, Gates (`actor`, `gate`) sind im FS-Profil vorgesehen. Dass der Aufwand geringer ist als Ansible, ist **[nicht belegt]**. |

## Folgen
- Repo `fs-server` jetzt zulässig; Crates (Vorschlag): `-core` (Modell, Variablen), `-ssh` (Trait, System-`ssh`), `-log`, `-provider-hetzner`, `-cli`; Frontends später.
- `fs-workflows`: Keim-Crate der Engine (Entscheidung 3); Workflow `server-einrichtung` zuerst als YAML im Stil von `fs-release/workflows`, FS-Profil.
- ADR 0077: Nachtrag Katalogart `workflow`. ADR 0078: Schritt „Paketquelle“ nutzt die apt/dnf-Quellen.

## Offen
- `installimage` und ZFS: ob ZFS direkt unterstützt wird, ist **[nicht belegt]**; der eigene Schritt danach gilt unabhängig davon.
- Aufbewahrungsdauer des vollen Protokolls und Umgang mit Ausgaben, die Geheimnisse enthalten (Schwärzung reicht ggf. nicht).
- Umfang von `bestand` (Phase 2): welche Angaben sich zuverlässig auslesen lassen, ist **[nicht belegt]**.
- Eignung von OpenTofu für Rescue/Platten **[nicht geprüft]**.
