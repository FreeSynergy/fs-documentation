# BEFUND: Datei-Metadaten für FreeSynergy Files

Stand: 2026-11-11. Nur Recherche per Web-Primärquellen. Nichts installiert, keine Desktop-Sitzung, keine Änderungen am Repo.
Markierung: [nicht belegt] = in dieser Recherche nicht aus Primärquelle bestätigt.

## Tabelle

| # | Standard | Was er trägt | Lizenz / Offenheit (belegt) | Reife | Rust | Eignung als Speicherort | Grenzen |
|---|---|---|---|---|---|---|---|
| 1 | freedesktop Shared File Metadata / CommonExtendedAttributes (wiki.freedesktop.org/www/CommonExtendedAttributes/) | xattr: `user.xdg.origin.url` (Download-URL), `user.xdg.comment`, `user.xdg.language`, `user.xdg.publisher`, `user.mime_type`, `user.xdg.robots.*`; `user.dublincore.*` nur als Namen, unspezifiziert. **`user.xdg.tags` steht nicht auf der Wiki-Seite** [nicht belegt] | Wiki-Seite, Einträge als "Proposed"; keine Lizenzangabe [nicht belegt]. Die "Shared File Metadata"-Spec (wiki.freedesktop.org/www/Specifications/shared-filemetadata-spec/) ist ein Namensschema ohne Version/Status (letzte Änderung 2013), sagt nichts zu xattr | Proposed; Unterstützung lückenhaft (GNOME Discourse, KDE-Bug 473809; laut Suche) | `xattr` 1.7.0, MIT/Apache-2.0; Linux, macOS, FreeBSD, NetBSD, MidnightBSD, Android | Gut für Herkunfts-URL am Datei-Blob. Für Sammlungen/Katalog/Vertrauen ungeeignet | Wiki: "viele Anwendungen und Dateisysteme unterstützen xattrs nicht". Verhalten bei Kopieren/Verschieben nicht spezifiziert [nicht belegt] |
| 2 | XMP, ISO 16684-1 (developer.adobe.com/xmp/docs/XMPSpecifications/) | Strukturierte Metadaten IN der Datei: Dublin Core (dc:subject, dc:description, dc:rights), eigene Namespaces | Adobe-PDFs frei auf GitHub (XMP-Toolkit-SDK); Part 1 = ISO 16684-1:2012; Lizenz der PDFs nicht genannt; ISO-Bezugskosten nicht geklärt | Reif: Part 1 2012, Part 2 2022, Part 3 2020 | Rust-Crate: nicht belegt (lib.rs-Seite nicht abrufbar) | In der Datei, nur für unterstützte Formate (JPEG, PDF, ...). Ändert den Dateiinhalt (Hash ändert sich) | Nur Formate mit XMP-Unterstützung; beliebige Dateien nicht |
| 3 | AppStream 1.2 (freedesktop.org/software/appstream/docs/) | Komponenten-Metadaten für Software-Center: Name, Beschreibung, Lizenz, Icons; Katalog | Doku GFDL-1.3+ oder CC-BY-SA-4.0 (belegt) | Reif | nicht belegt | Katalog-Ebene (Anbieter/Komponente), nicht pro Datei. Passt zu "Katalog = anbietende Seite" | Paket-zu-Komponenten-Feld auf der Seite nicht belegt; keine Datei-Ebene |
| 4 | OCI-Annotationen (github.com/opencontainers/image-spec, annotations.md) | `org.opencontainers.image.`: created, authors, url, documentation, source, version, revision, vendor, licenses (SPDX-Ausdruck), title, description, base.digest, base.name | Lizenz der Seite nicht genannt [nicht belegt]; Keys frei verwendbar | Reif | oci-spec 0.10.0, Apache-2.0; Annotations-Unterstützung nicht belegt | Image-/Manifest-Ebene, nicht Datei. Gut für Container-Pakete | Nur OCI-Artefakte; Annotationen auf Config-Ebene nicht belegt |
| 5a | SPDX 3.0.1 (spdx.github.io/spdx-spec/v3.0.1/) | Herkunft (originatedBy, createdBy, suppliedBy), Prüfsumme (hashValue, algorithm), Verifikation (verifiedUsing), Lizenzen, Bestandteile | Spec-Lizenz laut Seite: Community Specification License 1.0 bzw. CC-BY-3.0 (belegt). ISO/IEC 5962 auf Seite nicht genannt [nicht belegt] | Version 3.0.1 | spdx-rs 0.5.5, MIT; letzter Release 2023; SPDX-Version nicht belegt | Sidecar-Dokument (z. B. `*.spdx.json`), nicht xattr. Bindung an Datei über Hash | Dokument, kein Datei-Attribut; Aktualität des Rust-Crates fraglich |
| 5b | CycloneDX 1.7 / ECMA-424 (cyclonedx.org/specification/overview/) | Komponenten mit Pedigree/Provenance; Citations (wer hat Daten wann beigesteuert); SBOM, SaaSBOM, HBOM | ECMA-424 als Ecma-Standard, veröffentlicht 2025-12-10 (belegt); Spec-Lizenz nicht genannt [nicht belegt] | 1.7 vom 2025-10-21 | cyclonedx-bom 0.9.0, Apache-2.0; unterstützt CycloneDX 1.3-1.7 (belegt) | Sidecar/Paket-/Build-Ebene | Hash-Unterstützung auf der Übersichtsseite nicht belegt [nicht belegt] |
| 6 | rpm/dpkg-Datenbank: `rpm -qf FILE` (Paket, das FILE besitzt; `--path` auch für nicht installierte Pfade); `rpm -q --qf ...` (Dateiliste, Digests); `dpkg -S MUSTER`, `dpkg -L PAKET` | Datei → Paket, Dateiliste, Digests (rpm) | rpm.org-Doku-Index ohne Lizenzangabe [nicht belegt]; dpkg-Man-Page: "Search for a filename from installed packages" (Mustertyp nicht spezifiziert) | Sehr reif | nicht belegt (Abfrage per Befehl oder DB-Lesen) | Keine Ablage in der Datei; Quelle ist die System-DB. Nur installierte Pakete | Nur installierte Pakete; User-Dateien ohne Paket; dpkg-Diversions nicht belegt |
| 7 | OpenCloud (Vorbild) | README: "The OpenCloud backend does not use a database. It stores all data in the filesystem." Standard-Root `$HOME/.opencloud/`. Lizenz Apache-2.0 (belegt) | Apache-2.0 (belegt) | Projekt aktiv (Copyright 2026) | nicht belegt | Vorbild für datei-basierte Speicherung ohne DB. Ablage von Metadaten (xattr oder Datei) und Spaces-Modell auf den geprüften Seiten nicht belegt [nicht belegt] | Konkrete Metadaten-Ablage muss im Quellcode oder Developer-Doku geprüft werden |
| 8a | Mark of the Web, Zone.Identifier (Windows) | Herkunftszone (ZoneId) als Begleitdatenstrom | [nicht belegt]: abgerufene Microsoft-Seite war die archivierte "URL Security Zones"-Doku und enthält keine MOTW-Beschreibung | - | - | Muster für Herkunft als Begleitdaten; Verlust beim Kopieren auf Nicht-NTFS [nicht belegt] | Keine Primärquelle für Details in dieser Recherche |
| 8b | macOS `com.apple.quarantine` | Herkunftsflag: Flags, Zeitstempel, Agent-Name, UUID (semikolon-getrennt); Auslöser für Gatekeeper-Prüfung | Keine Apple-Primärquelle abgerufen; nur Sekundärquellen (eclecticlight.co, MITRE ATT&CK T1553.001) [nicht belegt primär] | Flag seit 10.5 (2007), Gatekeeper seit 10.7 (Sekundärquelle) | - | Muster: Herkunft als xattr. Setzen durch Browser/Mail; CLI-Tools wie curl/scp setzen es nach Sekundärquelle nicht | Entfernbar mit `xattr -d`; Sekundärquellen widersprüchlich zu Wirkung bei Sandboxing |

## Antworten

**Was trägt JEDE Datei?**
- Herkunft: optional `user.xdg.origin.url` (xattr, "Proposed"); Plattform-Muster MOTW / quarantine. Nicht portabel garantiert.
- Paket: nicht in der Datei. Nur über System-DB (`rpm -qf`, `dpkg -S`), und nur für installierte Systempakete. User-Dateien haben kein Paket.
- Vertrauen/Signatur: kein belegter Dateistandard in dieser Recherche [nicht belegt]. SPDX `verifiedUsing` ist Dokumentebene.
- Prüfsumme: kein xattr-Standard belegt. SPDX `hashValue` belegt; rpm-DB enthält Digests für Paketdateien.
- Schlagworte: XMP `dc:subject` (belegt); `user.xdg.tags` [nicht belegt, nicht auf der Wiki-Seite].
- Sammlungen: [nicht belegt], kein Standard gefunden; OpenCloud-"Spaces" nicht belegt.
- Beschreibung: `user.xdg.comment` (Wiki), XMP `dc:description`.
- Rechte: XMP `dc:rights` / `user.dublincore.rights` (unspezifiziert); POSIX-Rechte als Basis.

**Was kommt bei Paketen dazu?**
- Paket-DB-Zuordnung (rpm/dpkg), AppStream-Komponente (Katalog), OCI-Annotationen (Images), SPDX/CycloneDX-Dokument mit Herkunft, Lieferant, Hashes, Bestandteilen.

## Empfehlung Speicherort (Entwurf, nicht umgesetzt)
- Kern (Herkunft, Hash, Sammlungen, Katalog-Bezug) in einer eigenen DB oder Sidecar, weil xattr-Unterstützung und Verhalten beim Kopieren nicht spezifiziert und lückenhaft sind.
- xattr nur als optionaler Zusatz (origin.url, comment). Wiki bestätigt: nicht alle Dateisysteme/Apps unterstützen xattrs.
- Für Standards-Konformität: SPDX/CycloneDX als Sidecar-Export, XMP nur wenn Datei-Formate es tragen.

## Offen (nicht belegt, vor Entscheidung klären)
- `user.xdg.tags` und Sammlungs-Standard.
- Verhalten von xattr beim Kopieren (cp, rsync -X) und auf Zielsystemen.
- Apple-Primärquelle für quarantine; Microsoft-Primärquelle für MOTW.
- Rust-Crates für XMP, rpm, AppStream (nicht abrufbar bzw. nicht geprüft).
- OpenCloud-Quellcode zur tatsächlichen Metadaten-Ablage und Spaces.
