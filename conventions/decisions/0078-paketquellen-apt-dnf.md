# 0078 – Paketquellen apt/dnf: ein Repo `fs-packages`, getrennt vom Katalog

Status: **akzeptiert** (Strategie, 2026-11-14) · ergänzt ADR 0062 (Katalog = TUF/AppStream) · baut auf ADR 0051 (offene Signatur), 0068 (gespiegelte Pakete), 0077 (Server als rpm/deb, überall installierbar)

## Kontext
ADR 0062 legt den Katalog fest (AppStream + TUF, Pakete als Git-Tags). Kein ADR beschreibt eine Paketquelle, die `apt` oder `dnf` direkt lesen. `dpkg-sig` (heutiger Weg für `.deb`) prüft `apt` nicht; Schutz gibt es nur über das Repo (`Release`/`InRelease`). ADR 0077 verlangt, dass jeder Server per rpm/deb überall installierbar ist. Paketquellen sind **Ausgabeformate** aus den Releases, nicht der Katalog.

## Entscheidung
1. **Ein Repo `fs-packages`** (Verzeichnisse `apt/` und `rpm/`), getrennt von `fs-catalog` (ein Vertrauenskreis, eine TUF-Kette bleibt dort). Ablage: GitHub Pages mit eigenem Actions-Deploy; früher Spiegel auf Codeberg (ADR 0062: „auch ohne GitHub“). Bis zur Domain gilt die `github.io`-Adresse; Vorschlag `packages.freesynergy.net` für apt und rpm (Nutzer entscheidet). Quelle der Wahrheit bleibt das Release (Asset + `.asc`); die Quelle ist eine abgeleitete Sicht und jederzeit aus den Releases neu baubar.
2. **APT:** `apt-ftparchive` (zustandslos, Teil von `apt`), `gpg` signiert `Release`, `InRelease`, `Release.gpg`. Suiten: `stable` = Releases, `testing` = Vorabversionen. Aufbewahrung: 3 Versionen je Paket und Architektur. Architekturen `amd64`, später `arm64` (nativer Runner). Client: deb822-Datei `freesynergy.sources` mit `Signed-By: /usr/share/keyrings/freesynergy-archive-keyring.pgp`; beim Einrichten wird der Fingerabdruck `16A4 A3EE 563A EF51 FCF0 C55D ED7B 57C4 A190 4342` geprüft. **DNF danach:** `createrepo_c`, `repomd.xml.asc`, `repo_gpgcheck=1`, `gpgcheck=1`.
3. **Signatur:** Die Release-Signaturen stammen vom Unterschlüssel `372A…C097` unter dem Projektschlüssel `16A4…4342` (belegt an `fs-kanidm` v1.12.1). Annahme: im CI-Secret liegt nur der Unterschlüssel; am Secret wird nichts geändert. Der Unterschlüssel **läuft am 2027-11-07 ab**: Verlängerung und ein Keyring-Paket (`freesynergy-archive-keyring`, im eigenen Repo) rechtzeitig einplanen; der Hauptschlüssel liegt offline beim Nutzer. RPM mit Ed25519: EL9 prüft EdDSA ab `rpm-4.16.1.3-4.el9` (Red Hat Bugzilla 1962234: „RPM now supports the EdDSA public key algorithm“, Status CURRENTRELEASE 2021-12-07). **FIPS-Modus ist keine Zielgruppe** und wird als `Unsupported` dokumentiert.
4. **Ziel-Distros (verbindlich):** Debian 12/13, Ubuntu 22.04/24.04, EL9/EL10, Fedora aktuell. Gebaut wird in per Digest gepinnten Containern mit glibc ≤ 2.34 (EL9); Smoke-Test (Quelle eintragen, `update`, `install`; Negativtest mit verändertem `Packages`/Paket) auf allen genannten Distros.
5. **OCI:** Pflicht ist das OCI-Archiv (`.tar`) mit `.asc` im Release. `ghcr.io` ist zweiter Weg. Vorschlag: OpenPGP „simple signing“ (`skopeo copy --sign-by`, Lookaside auf Pages; belegt in `containers-policy.json(5)` und `containers-registries.d(5)`). `cosign` ist ohne eigenen ADR ausgeschlossen.
6. **Veröffentlichen:** der Koordinator nach JA der Strategie, wie bei allen Releases (kein eigener Mensch-Schritt). Der Workflow `publish` hat die Jobs `build` (ohne Secrets) → `sign` (Secrets, kein fremder Code, Actions per Commit-SHA gepinnt) → `deploy`. Auf `node1` trägt der Workflow `server-einrichtung` die Quelle ein, erst nach Freigabe des Zugangs durch den Nutzer.

## Folgen
- Neues Repo `fs-packages`; neue Betriebsart `release-index` in `fs-release/actions/sign-files`.
- Nach dem Bau: Anleitung für Nutzer (Fingerabdruck prüfen, Quelle eintragen) unter `docs/en/`.
- Pages-Grenzen (docs.github.com, „GitHub Pages limits“: Seite höchstens 1 GB, weiche 100 GB/Monat) tragen den Anfang; die Aufbewahrung von 3 Versionen hält das Repo klein, der Codeberg-Spiegel mindert die GitHub-Abhängigkeit.

## Alternativen (verworfen)
- **Release-Assets als Repo:** `apt` braucht die feste Struktur `dists/…` und `pool/…` unter einer Basis-URL; Assets haben flache Namen und Weiterleitungen.
- **Im `fs-catalog` neben TUF:** vermischt Katalog (Metadaten, TUF) mit Binärdateien; Katalog bleibt klein und getrennt.
- **reprepro/aptly:** zustandsbehaftet (zweite Datenbank, die gesichert werden müsste); reprepro zusätzlich mit Auffälligkeit bei Debian (`5.4.6+really5.3.2`, Debian ist auf 5.3.2 zurückgegangen, Grund nicht geprüft). `aptly` (MIT) bleibt Rückfall, falls mehrere Suiten/Snapshots nötig werden.
- **cosign:** zweite Signaturwelt neben OpenPGP (ADR 0051 „offene Variante“); nur mit eigenem ADR.

## Offen
- Domain (`packages.freesynergy.net`?), `node1`-Betriebssystem/Zugang, Hauptschlüssel im CI-Secret oder nicht: beim Nutzer **[nicht belegt]**.
- Verhalten von `apt` bei abgelaufenem Unterschlüssel und Optionen von `apt-ftparchive` (`Valid-Until`, `Acquire-By-Hash`) **[nicht belegt]**, Testfall im Smoke-Test.
- `repo_gpgcheck`/`gpgcheck` gegen `dnf.conf(5)` und EL9-Test auf `almalinux:9` **[nicht belegt]**.
- Verzeichnisaufbau des Lookaside **[nicht belegt]**; EL9 im FIPS-Modus **[nicht belegt]**.
