# Befund: Server-Repos fs-kanidm, fs-zentinel, fs-tuwunel (Schritt 1, nur gelesen)

Stand 2026-11-11. Nichts angelegt, nichts gepusht, nichts auf node1. Heruntergeladen nur: Zentinel-Tarball + Prüfsumme + Sigstore-Bündel (`.scratch/server-befund/zentinel/`, nicht ausgeführt) und PPA-Metadaten (`.scratch/server-befund/kanidm-ppa/`). Gelesen: ADR 0047, 0054, 0067, 0068, Sprint-Eintrag (Server).

## (i) Zentinel-Control-Plane

- Repo: https://github.com/zentinelproxy/zentinel-control-plane (Elixir/Phoenix), Lizenz **Apache-2.0** (LICENSE-Datei und GitHub-SPDX geprüft). Status laut README: **Beta**. Kein Release, nur Quellcode. Unser Fork `FreeSynergy/zentinel-control-plane-archive` ist archiviert.
- Apache-2.0: Nachbau, Verteilung, kommerzielle Nutzung erlaubt; Pflichten nur beim Weitergeben fremden Codes (Lizenztext, Hinweise, Änderungen kennzeichnen, NOTICE). Weil wir **nur die Funktionen** nachbauen und nichts kopieren, entstehen keine Pflichten. Funktionsbeschreibungen sind frei. Namen/Logo „Zentinel“ sind keine Lizenzsache (Apache gibt kein Markenrecht): in unserem Repo Name nur beschreibend benutzen.
- **Funktionen (für den Rust-Nachbau):**
  1. KDL-Konfiguration hochladen, mit `zentinel test --config` prüfen.
  2. Bündel bauen: unveränderlich, inhaltsadressiert (SHA-256), tar.zst mit Manifest, Prüfsummen und CycloneDX-1.5-SBOM, **Ed25519-signiert**.
  3. Rollout auf Knoten nach Label-Auswahl: Batches, Gesundheitsprüfung, Fristen, Pause/Fortsetzen/Rollback; geplante Rollouts; Genehmigungen; Rollout-Vorlagen.
  4. Knoten: Registrierung mit Projekt-Token, Heartbeats, Gruppen, Veraltet-Erkennung, Drift-Erkennung (gemeldet vs. erwartet).
  5. Umgebungen (dev, staging, prod) mit Beförderung; Mandanten (Organisationen, Projekte, API-Schlüssel mit Rollen).
  6. GitOps (Webhook baut Bündel bei Push); Audit-Log jeder Änderung mit Diff.
  7. SLOs und Alarme, Benachrichtigungen (Slack, PagerDuty, Teams, Mail, Webhook), Dienst-Topologie-Graph, WAF-Richtlinien (ca. 60 Regeln aus OWASP CRS), Prometheus/OpenTelemetry.
  8. Anmeldung: OIDC (PKCE), SAML 2.0, TOTP; REST + GraphQL; Zustand PostgreSQL (SQLite in Entwicklung), Bündel in S3 (RustFS).
  9. Agent `zentinel-cp-agent` am Knoten (der Proxy selbst hat keinen Control-Plane-Client): registrieren, Heartbeat, Bündel laden, Prüfsumme/Signatur/Manifest prüfen, `zentinel test`, atomar installieren, Neuladen, bei Fehler zurückrollen, Ereignis melden. Schnittstelle: Knoten-API (docs/PROXY-REGISTRATION.md).
- Empfehlung: für uns reichen zuerst 2, 3, 4, 6 (Audit), 8 (über Kanidm statt eigene Anmeldung); WAF, SLO, Topologie später/streichen. Die Knoten-API ist dokumentiert; wir könnten **ihren Agenten wiederverwenden** (Apache-2.0, Quellspiegel) statt neu zu bauen: Entscheidung für die Strategie.

## (ii) Pakete der Hersteller: Formate, Signatur, Versionen

| Programm | Aktuell | Was der Hersteller anbietet | Signatur / Prüfsumme |
|---|---|---|---|
| **Zentinel** | **26.11_1** (2026-11-07; CalVer) | Tarballs linux amd64/arm64, darwin; Container `ghcr.io/zentinelproxy/zentinel`; `cargo install zentinel-proxy`; `install.sh`. **Kein deb/rpm.** SBOM (CycloneDX, SPDX) | **Sigstore cosign keyless** (`.bundle` je Datei, Identität GitHub-Actions-OIDC, Regex `github.com/zentinelproxy/zentinel`, Issuer `https://token.actions.githubusercontent.com`), SLSA-v1-Herkunft (`multiple.intoto.jsonl`), `checksums.txt` + `.sha256`. Container: `.sig`-Tags in ghcr. **Kein fester Schlüssel/Fingerprint**: Vertrauen = Zertifikatsidentität + Rekor-Log. |
| **Kanidm** | **1.12.0** (2026-11-01) | Container `kanidm/server`, `/radius`, `/tools` (Docker Hub, 1.12.0, Digest `sha256:71b6ff5a…5ce9`) und ghcr `kanidmd`. **GitHub-Releases ohne Dateien.** Hersteller sagt: bevorzugt Container; Pakete (deb-PPA, OpenSUSE, AUR, Nix, Alpine, FreeBSD) sind **Community**. | Container: keine Signatur gefunden (keine `.sig`-Tags, kein cosign in Workflows). Git-Tag v1.12.0 **ungesignt**, Commit ungesignt. Debian-PPA `kanidm.github.io/kanidm_ppa`: apt-Repo mit **GPG-Schlüssel EA20 E95D 68A6 5191 FE8C E795 76CC 8140 60B2 3E66** (RSA4096, James Hodgkinson, „Kanidm PPA Signing Key 2023-10-29"; InRelease-Signatur von mir mit gpg geprüft: gültig). PPA bietet **trixie** (auch bookworm, noble) amd64/arm64, aber **hinkt hinterher: stable = 1.11.2, Stand 2026-09-20**, nicht 1.12.0. Prüfsummen: SHA256 in `Packages`. |
| **Tuwunel** | **2.0.0** (2026-11-10; Release-Tag `v2.0.0-assets`, Quell-Tag `v2.0.0`) | Binär `.zst`, **`.deb`, `.rpm`**, Container (docker.tar.gz, oci.tar.zst), Nix, je x86-64 v1/v2/v3 und aarch64, Varianten `default`/`logging`/`debuginfo` | **Keine Signatur** (kein gpg, kein cosign), Git-Tag und Commit ungesignt. Nur die von GitHub berechneten SHA-256-Digests je Asset (z. B. deb x86_64-v1 `sha256:21086773…97a0d`, 53 MB). Das ist Vertrauen in GitHub/Konto, nicht in einen Schlüssel. Nur `SECURITY.md.asc` (Meldeschlüssel). |

- Folge für ADR 0068 („Signatur und Prüfsumme beim Übernehmen prüfen"): Zentinel voll prüfbar (cosign + SHA256, Container-Signatur); Kanidm nur über die Community-PPA-Signatur (veraltet) oder über Container-Digest; Tuwunel nur SHA-256 (+ Vergleich Quell-Tag). Das **Spiegel-Manifest muss je Paket ein Feld „Prüfart" tragen** (`sigstore`, `gpg-repo`, `digest-only`) und ehrlich ausweisen. Zusätzlich möglich und empfohlen: **selbst aus dem Quell-Tag bauen** (reproduzierbar belegen, ADR 0068 „Selbst gebaut wird nur, wo ein Format fehlt" – bei Kanidm fehlt ein aktuelles signiertes deb für Debian 13, das ist so ein Fall; dafür gibt es den Fork).
- Kanidm deb-Paketnamen (PPA): `kanidm`, `kanidmd`, `kanidm-unixd`, `libnss-kanidm`, `libpam-kanidm`.

## (iii) Lizenzen und Folgen

| Programm | SPDX | Folge |
|---|---|---|
| Kanidm (kanidm/kanidm, `LICENSE.md`) | **MPL-2.0** | Schwaches, dateibezogenes Copyleft. Binär verteilen ist erlaubt, wenn Lizenztext und **Quellcode der MPL-Dateien in derselben Version** zugänglich sind (Quelle-Tarball im Spiegel erfüllt das). Änderungen an MPL-Dateien müssen offen bleiben; wir ändern nichts. Verknüpfung mit unserem MIT/Apache-Code unproblematisch. |
| Zentinel (Proxy, Control-Plane, Agenten meist) | **Apache-2.0** (einzelne Agenten MIT) | Verteilen frei; LICENSE + NOTICE beilegen, Quellcode mitspiegeln wie ADR 0068. |
| Tuwunel (matrix-construct/tuwunel) | **Apache-2.0** | wie oben. |

- Für alle drei ist der Spiegel (Binär + Quelle + Lizenztexte) zulässig. Keine Zustimmung der Hersteller nötig; Marken nicht als eigene ausgeben („nicht offiziell", Herkunft nennen).
- Kanidm-Projekt hat eine KI-Richtlinie (`book/src/developers/ai_llm_policy.md`); relevant erst, wenn wir etwas upstream einreichen (nicht ohne Rückfrage).

## (iv) Fähigkeiten-Tag-Matrix (ja / nein / instabil)

| Tag | Kanidm 1.12.0 | Zentinel 26.11_1 (+Agent auth 0.3.0) | Tuwunel 2.0.0 |
|---|---|---|---|
| OIDC | **ja**: Core 1.0 + Discovery, ES256 (RS256 nur als Ausnahme), PKCE S256, Webfinger bewusst nein. [supported_features.md](https://github.com/kanidm/kanidm/blob/master/book/src/supported_features.md), [oauth2.md](https://github.com/kanidm/kanidm/blob/master/book/src/integrations/oauth2.md) | **instabil**: nur Prüfung von Bearer-Tokens gegen JWKS im Auth-Agenten, laut README „experimental"; **kein** Browser-Login (Code-Flow) als Relying Party. [zentinel-agent-auth](https://github.com/zentinelproxy/zentinel-agent-auth) | **ja** (als Client/Anmeldung über fremde IdPs: GitHub, Google, Keycloak, Authelia, Authentik; und eigener OIDC-Server für Matrix-Clients, MAS-kompatibel). [docs/authentication.md](https://github.com/matrix-construct/tuwunel/blob/main/docs/authentication.md) |
| OAuth2 | **ja**: Code Grant, Client Credentials, Token-Exchange (RFC 8693), Introspection, Widerruf, JWT-Access-Tokens | **instabil**: Bearer/JWT-Prüfung (HS*/RS*/ES*), SAML/mTLS/Token-Exchange werden **abgelehnt** (unsicher, Issue #6) | **ja**: eingebauter OAuth2/OIDC-Server inkl. Refresh, Device-Grant |
| LDAP | **ja**, aber **nur lesend** (Bind einfach, Suche, Vergleich, whoami; LDAPS). Import per RFC 4533 aus fremdem LDAP | **nein** | **ja** als Client (Passwort-Anmeldung gegen LDAP-Verzeichnis, Build-Feature, Standard) – Tuwunel *nutzt* LDAP, bietet keinen an. [ldap.md](https://github.com/matrix-construct/tuwunel/blob/main/docs/authentication/ldap.md) |
| RADIUS | **ja** (Container `kanidm/radius`, MSCHAPv2, EAP-TLS; eigenes RADIUS-Passwort je Konto). [radius.md](https://github.com/kanidm/kanidm/blob/master/book/src/integrations/radius.md) | nein | nein |
| PAM | **ja** (`kanidm-unixd`, `libpam-kanidm`, `libnss-kanidm`). [pam_and_nsswitch.md](https://github.com/kanidm/kanidm/blob/master/book/src/integrations/pam_and_nsswitch.md) | nein | nein |
| SSH-Schlüssel | **ja** (öffentliche Schlüssel an Personen und Dienstkonten, Verteilung über `kanidm_ssh_authorizedkeys`). [ssh_key_distribution.md](https://github.com/kanidm/kanidm/blob/master/book/src/integrations/ssh_key_distribution.md) | nein (Proxy, kein Schlüsselverzeichnis) | nein |
| Passkeys | **ja**: WebAuthn Level 3, FIDO-MDS-Attestierung, Passkeys und Attested Passkeys | nein | nein (Matrix-Anmeldung über Provider; QR-Login ist etwas anderes) |
| SCIM | **instabil**: nur **Einlesen** aus fremdem IdP (RFC 7644 Bulk) und `/scim/v1/Entry|Sync` mit TODO im Quelltext; kein stabiler Provisionierungs-Server. ADR 0047 gilt: vorerst nicht nutzen. [supported_features.md](https://github.com/kanidm/kanidm/blob/master/book/src/supported_features.md) | **instabil**: SCIM-2.0-Nutzerspeicher im Auth-Agenten (experimentell) | **nein** (nichts dokumentiert) |

Hinweis: „ja" bei Tuwunel/Zentinel heißt nicht „bietet an", sondern „nutzt"; für den Katalog braucht es zwei Tag-Arten: **provides** (bietet an) und **uses** (kann anbinden). Vorschlag: Tags `identity.oidc.provider` (Kanidm) und `identity.oidc.client` (Tuwunel) unter dem Namen der Themen-Schnittstellen aus `fs-interfaces`. Je Tag: Wert, `source` (URL), `version`, `checked` (Datum).

## (v) Vorschlag Repo-Gerüst und Test-Plan

**Lizenz:** wie fs-files/fs-store/fs-catalog: `LICENSE-MIT` + `LICENSE-APACHE`, „MIT OR Apache-2.0", Autor `FreeSynergy <support@freesynergy.net>`. Spiegel-Inhalte behalten ihre eigene Lizenz in `upstream/LICENSES/`.

```
fs-<name>/
  README.md                 (EN, Kurzfassung, Verweis auf docs; AI-Attribution wie in eigenen Repos)
  LICENSE-MIT  LICENSE-APACHE
  mirror.toml               Spiegel-Beschreibung (ADR 0068): Version, Herkunft, URL, Prüfart (sigstore|gpg-repo|digest-only),
                            Fingerprint/Identität, SHA256 je Datei, Quellcode-Archiv+SHA256 derselben Version, SPDX, Lizenzdateien
  capabilities.toml         Fähigkeiten-Tags (provides/uses/requires) mit Wert ja|nein|instabil, source, version, checked
  config/                   öffentliche Voreinstellungen: zentinel.kdl | server.toml | tuwunel.toml;
                            Geheimnisse nur als Platzhalter `${vault:fs/<name>/<key>}` (ADR 0067), nie Werte
  config/schema/            Beschreibung der Felder (Name, Typ, Standard, secret=true/false) – Grundlage für Doku + Export
  docs/en/  docs/de/        index.md, configuration.md (aus Schema erzeugt), capabilities.md, mirror.md (so prüft man selbst)
  export/                   erzeugte Ausgabe (`fs-<name> export` -> Datei + Prüfsumme); Speichern ≠ Export (Grundsatz)
  scripts/verify-mirror.sh  Prüft Signatur/Prüfsumme (gpg, cosign, sha256sum); scripts/test/ (Test-Plan unten)
  .github/workflows/        check.yml (Schema, Platzhalter-Scan, Link-Check), mirror.yml (Prüfen, Spiegeln als Release-Dateien)
  LICENSES/upstream/        Lizenztexte der Hersteller
```
Dateien (Pakete, Quellarchive) liegen nicht in Git, sondern als Release-Dateien (ADR 0068). Katalog-Eintrag in `fs-catalog/packages.toml` danach (Signatur mit Projekt-Teilschlüssel 16A4 A3EE …). Vorgängerbezug: Fork-Repos `FreeSynergy/kanidm`/`tuwunel` bleiben nur Paketbau; Fork `FreeSynergy/zentinel` und `-control-plane-archive` bestehen. Kein Programm-Code (Cargo) in diesen Repos; eine Rust-Hülle (Export, Schema) wäre erst später ein Crate, **Entscheidung nötig**.

**Test-Plan (lokal, Podman):** Podman 6.1.3 vorhanden, **rootless ja**, cgroup v2, Controller `cpu io memory pids` delegiert; `podman run --memory=64m` setzt `memory.max` nachweislich (67108864 gemessen). Host 124 GiB RAM, Images debian:13, alpine:3 und `jevolk/tuwunel` schon da.
1. Netz `podman network create fs-test`; alle Container `--memory=…` (+ gleich `--memory-swap`), `--read-only`, `--cap-drop=all`, nur Loopback-Ports.
2. **Zentinel zuerst:** Paket-Prüfung (SHA256 immer; cosign über Container `ghcr.io/sigstore/cosign` – Netzzugriff nötig), dann Container mit unserer `zentinel.kdl` (Speicher 256 MB), Prüfung `zentinel test`, Upstream = Platzhalter-Dienst.
3. **Kanidm hinter Zentinel** (Speicher 512 MB; 1.12.0-Image per Digest festgelegt): TLS-Zertifikat selbstsigniert zur Laufzeit; Zentinel leitet `idm.test.local` an Kanidm.
4. **OIDC-Anmeldung:** Testskript im Container legt Konto/Gruppe/OAuth2-Client an und führt den Code-Flow mit PKCE gegen ein winziges Test-Client-Programm aus; prüft id_token (ES256, Aussteller, Zielgruppe) via Discovery. Danach Tuwunel 2.0.0 (512 MB) mit Kanidm als OIDC-Anbieter (SSO-Anmeldung), prüft Matrix-Anmeldung.
5. **Geheimnisse (ADR 0054):** nur das Skript erzeugt sie im Container zur Laufzeit (zufällig, `/dev/urandom`), nur in `tmpfs`/Umgebung des Containers, nie in Datei im Host, nie auf stdout/Log; Ausgabe des Skripts nur „bestanden/durchgefallen" je Schritt, `set +x`, Logs vor Ausgabe mit Muster-Scan geprüft; nach Test `podman rm -f`, Netz löschen. Ich lese keine Container-Umgebung, keine Tokens.
6. Zusatz: Platzhalter-Scan über Repo (kein Wert, nur `${vault:…}`), Konfig-Export-Rundlauf (Export -> Import -> gleich).

## (vi) Risiken / offene Fragen

1. **Kanidm hat kein signiertes Debian-13-Paket in 1.12.0** (PPA = 1.11.2, Community, Schlüssel einer Person). Entscheiden: (a) PPA-1.11.2 spiegeln (signiert, alt), (b) Container-1.12.0 per Digest spiegeln (unsigniert), (c) aus Quell-Tag selbst bauen mit Fork (empfohlen, wie ADR 0068 „Format fehlt") und in `mirror.toml` die Herkunft (Commit, Quell-Tag) angeben. Das Versionsgebot: Server und Client `unixd` höchstens 1 Minor Unterschied (support.md).
2. **Tuwunel ohne jede Signatur**: Vertrauen nur GitHub-Digest. Vorschlag: aus Quell-Tag selbst bauen/oder Digest mit zweiter Quelle (GHCR-Image-Digest) vergleichen; im Katalog „digest-only" sichtbar machen. Tuwunel 2.0 ändert Konfiguration (Tabellen `[global.…]`, Altnamen bleiben in 2.x), Artefaktnamen (`-default-` statt `-all-`); unsere `tuwunel.toml` direkt in kanonischer Form schreiben. Release-Tag heißt `v2.0.0-assets` (nicht `v2.0.0`).
3. **Zentinel-OIDC ist kein Anmelde-Fluss**: Wenn „Login über OIDC" an Zentinel gemeint war, fehlt dort ein Relying-Party-Flow (nur Bearer/JWKS, experimentell; SAML/mTLS/Token-Exchange verweigert). Im Plan loggt man **bei Kanidm** an, Zentinel ist Proxy davor. Frage an die Strategie, ob Zentinel selbst Login übernehmen soll (dann fehlt Code oder wir nutzen einen Auth-Proxy).
4. **Control-Plane-Nachbau**: Upstream „Beta", Agent-Protokoll/Knoten-API ist Apache-2.0-dokumentiert; Agent könnte wiederverwendet statt nachgebaut werden. Umfang festlegen (siehe (i)).
5. **Zentinel-Pakete: nur Tarball/Container**, kein deb/rpm; für Debian 13 baut unser Paket (fs-release) die Tarball-Binärdatei selbst ein. cosign nicht installiert (auf diesem Rechner Container nötig; Prüfen braucht Netz zu Sigstore/Rekor).
6. **SCIM**: bleibt „instabil" (ADR 0047). Kanidm hat keinen stabilen Provisionierungs-Server; Tag so eintragen, im Katalog nicht als `identity.scim` anbieten.
7. **Tuwunel-Unterstützung für Kanidm als IdP** ist nicht dokumentiert (nur Keycloak, Authelia, Authentik, MAS, GitHub, Google): Test-Plan Schritt 4 prüft es; bei Misserfolg ggf. Meldung an Tuwunel (kein Upstream-PR ohne Rückfrage).
8. Namen/Marken, `fs-matrix` ist bewusst nicht der Repo-Name (Sprint-Entscheid). Repos öffentlich: Konfigurations-Voreinstellungen enthalten keine Hostnamen/IPs (node1) – nur Beispiele.
9. Offene Frage zum Katalog: provides/uses/requires-Namen müssen mit der Liste in `fs-interfaces` (Thread T) abgestimmt werden, bevor `capabilities.toml` endgültig wird.
