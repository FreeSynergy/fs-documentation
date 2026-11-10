# Recherche: Vault-Verschlüsselung für fs-vault (ADR 0067)

Stand der Recherche: 2026-11-10. Alle Quellen wurden am 2026-11-10 abgerufen, sofern nicht anders vermerkt.

Kennzeichnung:
- **[geöffnet]** = Seite wurde selbst abgerufen und die Aussage steht dort.
- **[Suchtreffer]** = nur Ausschnitt aus Websuche gesehen, Seite nicht geöffnet. Nicht als gesichert zu behandeln.
- **nicht belegt** = keine Quelle gefunden oder Quelle nicht zugänglich.

---

## (1) Stand von FIDO CXF / CXP

- CXF 1.0 ist als "Proposed Standard" veröffentlicht, Datum 09.03.2026 (Errata-Version). [geöffnet] https://fidoalliance.org/specs/cx/cxf-v1.0-ps-errata-20260309.html (abgerufen 2026-11-10)
- Die CXF-Spezifikation nennt den Status wörtlich: "published by the FIDO Alliance as a Proposed Standard Specification." Version im Dokument: 1.0. [geöffnet] https://fidoalliance.org/specs/cx/cxf-v1.0-ps-errata-20260309.html
- CXF legt nach eigenem Scope keine Transportprotokoll-Annahmen fest, nennt aber CXP als bevorzugtes Transferprotokoll ("The preferred transfer protocol SHOULD be" CXP). [geöffnet] https://fidoalliance.org/specs/cx/cxf-v1.0-ps-errata-20260309.html
- Die FIDO-Ankündigung vom 14.10.2024 beschreibt CXP und CXF noch als **Working Draft**, "not yet intended for implementation as the specifications may change". [geöffnet] https://fidoalliance.org/fido-alliance-publishes-new-specifications-to-promote-user-choice-and-enhanced-ux-for-passkeys/ (abgerufen 2026-11-10)
- Die Ankündigung nennt Vertreter der Credential Provider Special Interest Group: 1Password, Apple, Bitwarden, Dashlane, Enpass, Google, Microsoft, NordPass, Okta, Samsung, SK Telecom. Sie beschreibt diese als Mitwirkende, **nicht** als Implementierer. [geöffnet] https://fidoalliance.org/fido-alliance-publishes-new-specifications-to-promote-user-choice-and-enhanced-ux-for-passkeys/
- Status von CXP heute (Working Draft oder höher): **nicht belegt**. Die Download-Seite konnte nicht abgerufen werden (HTTP 404 bzw. 300), die Spezifikationsübersicht enthält keine Versionsangaben. [geöffnet, ohne Ergebnis] https://fidoalliance.org/specifications/ ; https://fidoalliance.org/specifications/download-cx/ (404)
- Suchtreffer widersprechen sich: Ein Suchergebnis gibt CXP als Working Draft an, ein Suchtreffer-Ausschnitt eines 1Password-Beitrags sagt, CXP sei noch in Entwicklung und Übertragung heute nur lokal auf dem Gerät. [Suchtreffer] https://www.1password.community/blog/developer-blog/portability-without-compromise-1password-helps-author-a-new-standard-for-secure-/163208 (Seite selbst: HTTP 404 beim Abruf)
- Apple und Google APIs für Import/Export von Zugangsdaten: nur als Suchtreffer-Aussage erwähnt, nicht geöffnet. [Suchtreffer] https://www.1password.community/blog/developer-blog/portability-without-compromise-1password-helps-author-a-new-standard-for-secure-/163208
- Konkrete Produkt-Unterstützung von CXF/CXP (Export/Import in Produkten): **nicht belegt** über offizielle Quellen.

Quellen Frage 1: 4 geöffnet, 2 Suchtreffer, 2 nicht abrufbar.

---

## (2) Linux als Passkey-Anbieter für Browser; Windows-Plugin-API

### Linux
- Projekt credentialsd / Linux Credential Manager API: Vorschlag für eine D-Bus-Spezifikation nach Art eines xdg-portals, inkl. WebAuthn/Passkey-Unterstützung. Lizenz LGPL-3.0-only. Browser-Erweiterung und Firefox-Build sind als "Experimental" markiert. Keine Release-Angabe sichtbar. [geöffnet] https://github.com/linux-credentials/credentialsd (abgerufen 2026-11-10)
- Browser-Erweiterung laut Projektseite: Firefox 140+ (XPI), Chrome 111+ / Edge 111+ (unpacked), funktioniert nur für webauthn.io und demo.yubico.com. Ein experimenteller Firefox-Build mit Patch spricht credentialsd direkt an. [geöffnet] https://github.com/linux-credentials/credentialsd
- Der Projektansatz über D-Bus-Portal hat laut Suchtreffer ein Hauptproblem: Built-in Platform-Authenticator (TPM als Voraussetzung) sind offen. [Suchtreffer] https://github.com/iinuwa/linux-webauthn-platform-api
- FOSDEM 2026 Vortrag "Credentials for Linux": sandboxed Firefox nutzt credentialsd für Hardware-Keys und Telefone. [Suchtreffer] https://fosdem.org/2026/schedule/event/credentials-for-linux-bringing-passkeys-to-linux
- libwebauthn als Rust-Bibliothek für die D-Bus-Plattform-API. [Suchtreffer] https://docs.rs/crate/libwebauthn/0.8.0
- Firefox-Add-on "Linux Passkey Manager" (Drittanbieter, experimentell, Software-Schlüssel im Profil). [Suchtreffer] https://addons.mozilla.org/addon/linux-passkey-manager/
- Weitere Wege (Browser-Schnittstellen im System ohne D-Bus, Portal-Varianten für Chrome): **nicht belegt**.

### Windows
- Microsoft Learn: Windows 11 unterstützt ein Plugin-Modell für Passkeys. Demo-App "Contoso Passkey Manager" (nur zum Testen, nicht für produktive Passkeys). Aktivierung unter Einstellungen > Konten > Passkeys > Erweiterte Optionen. Windows Hello dient als Nutzerprüfung. Seite ms.date 2025-09-29, aktualisiert 2026-02-28. [geöffnet] https://learn.microsoft.com/en-us/windows/apps/develop/security/third-party
- Die Learn-Seite nennt keine API-Namen im abgerufenen Teil. [geöffnet] https://learn.microsoft.com/en-us/windows/apps/develop/security/third-party
- Beispiel-Code "Passkey Manager sample" in Windows-Classic-Samples: Registrierung als COM-Objekt in der Registry, Interface IPluginAuthenticator, Registrierung per WebAuthNPluginAddAuthenticator (Header im WebAuthn-Paket). [Suchtreffer] https://learn.microsoft.com/en-us/samples/microsoft/windows-classic-samples/passkeymanager (Seite nicht geöffnet; Namen nicht gegen Quelle geprüft)
- Start des Plugin-Modells laut Suchtreffer: Windows 11 November 2025 Security Update; 1Password und Bitwarden als erste Drittanbieter. [Suchtreffer] https://www.bleepingcomputer.com/news/security/microsoft-testing-windows-11-support-for-third-party-passkeys/amp/
- Anforderungen (Mindest-Windows-Version, Package-Identity, Signierung): **nicht belegt**, da nur der Einführungs-Teil der Seite gelesen wurde.

Quellen Frage 2: 2 geöffnet (Linux), 1 geöffnet (Windows), 6 Suchtreffer. Nicht zugänglich: Microsoft-API-Referenz (Header/Funktionsliste) nicht geöffnet.

---

## (3) WebAuthn-PRF-Unterstützung je Browser und OS

- W3C WebAuthn Level 3 ist laut Dokumentkopf eine **Recommendation** vom 25.08.2026. Der PRF-Abschnitt (10.1.4 / 16.17.1) wurde nicht gelesen. [geöffnet, Teil] https://www.w3.org/TR/webauthn-3/
- MDN Web Authentication API: keine PRF-Angabe, keine Browser-Tabelle für PRF. [geöffnet] https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API
- Tabelle laut Artikel (Stand Feb 2026, Artikel aktualisiert 05.08.2026):
  - Android: stabil, mit Google Password Manager.
  - macOS 15+: Safari 18+, Chrome 132+, Firefox 139+.
  - iOS/iPadOS 18+: Datenverlust-Bug in 18.0–18.3, behoben in 18.4.
  - Windows 11: eingeschränkt, Windows Hello unterstützt hmac-secret nicht, nur externe Security-Keys.
  - Firefox: nicht auf Android; macOS und Windows ab v139.
  [geöffnet] https://lilting.ch/en/articles/passkeys-prf-extension-encryption-risk (abgerufen 2026-11-10)
- Chrome unter Windows ab 147 (PRF bei create): [Suchtreffer] https://www.corbado.com/blog/passkeys-prf-webauthn — nicht geöffnet, **nicht belegt**.
- Edge mit Windows Password Manager (Windows 11 25H2+) und Google Password Manager (Android): [Suchtreffer] https://mera.category.xyz/authenticator-support/ — nicht geöffnet.
- Safari auf iOS/macOS, Linux (Chrome, Firefox, Edge): **nicht belegt** (Yubico-Browser-Support-Seite gab HTTP 300 zurück).
- Widerspruch: Ein Bitwarden-Community-Thread behauptet fehlende PRF-Unterstützung in Safari, eine spätere PR soll dies geändert haben. Nicht geprüft. [Suchtreffer] https://community.bitwarden.com/t/sign-into-bitwarden-with-a-passkey-login-with-passkeys-for-all-bw-apps/41053?page=4

Quellen Frage 3: 3 geöffnet (Teil), 3 Suchtreffer. Lücken: Linux komplett, Edge/Chrome-Versionen nur über Suchtreffer.

---

## (4) Rust-Implementierungen von MLS (RFC 9420)

### OpenMLS
- Lizenz: MIT (GitHub-Seite: "MIT license"; SPDX-Kennung nicht angegeben). [geöffnet] https://github.com/openmls/openmls
- RFC 9420: laut README "a Rust implementation of the Messaging Layer Security (MLS) protocol, as specified in RFC 9420". [geöffnet] https://github.com/openmls/openmls
- Letzte Veröffentlichung auf GitHub: nicht sichtbar (Releases-Bereich leer). Crate-Versionen laut docs.rs-Suchtreffern: 0.7.x, 0.9.0-rc.2; lib.rs-Seite zeigt laut Suchtreffer veraltet 0.6.0 (Sep 2024). Aktuelle Version: **nicht belegt** (crates.io nicht geöffnet). [Suchtreffer] https://docs.rs/crate/openmls/0.9.0-rc.2 ; https://lib.rs/crates/openmls
- Audit: Suchtreffer eines Hacker-News-Spiegels nennt ein von der Sovereign Tech Agency finanziertes Audit durch SRLabs, acht Befunde, einer davon "High", Fixes in openmls 8.1 und 7.3. Originalquelle nicht geprüft. [Suchtreffer] https://hackernews-dynamic.seasondane.workers.dev/news/48307020
- Gegenprüfung: Die GitHub-SECURITY.md erwähnt kein Audit. [geöffnet] https://github.com/openmls/openmls/blob/main/SECURITY.md — Widerspruch bzw. Quelle nicht vollständig geprüft. Der Audit-Status bleibt **nicht belegt** bis zur Originalquelle.
- Betreiber laut Suchtreffer: Phoenix R&D und Cryspen. [Suchtreffer] https://github.com/openmls/openmls

### mls-rs (AWS)
- Lizenz: "Apache-2.0 or MIT" (README). [geöffnet] https://github.com/awslabs/mls-rs
- RFC 9420: "An implementation of Messaging Layer Security (RFC 9420)", Anspruch "100% RFC 9420 conformance". [geöffnet] https://github.com/awslabs/mls-rs
- Audit: "has been validated for conformance to the RFC 9420 specification but has not yet received a full security audit by a 3rd party." [geöffnet] https://github.com/awslabs/mls-rs
- Letzte Veröffentlichung: nicht sichtbar (Releases leer). **nicht belegt**.

### Weitere Rust-Projekte
- Nicht recherchiert. Lücke.

### Lizenzkompatibilität mit Apache-2.0/MIT
- OpenMLS (MIT) und mls-rs (Apache-2.0 OR MIT) sind nach den oben genannten Lizenzangaben mit Apache-2.0 und MIT kompatibel. Diese Aussage ist eine rechtliche Einordnung, keine Rechtsberatung; die Lizenztexte selbst wurden nicht geprüft.

Quellen Frage 4: 3 geöffnet, 3 Suchtreffer. Lücken: weitere Implementierungen, Veröffentlichungsdaten, Audit-Original.

---

## (5) CryptPad-Modell: Teams und geteilte Schlüssel

- Der Schlüssel wird aus dem Hash der URL (Teil nach #) abgeleitet; der Browser sendet ihn nicht an den Server. [geöffnet] https://docs.cryptpad.org/en/dev_guide/general.html (Abschnitt "Encryption")
- "All users with access to this key can decrypt the 'patches' allowing them to rebuild the document." Lesezugriff bedeutet, dass der Schlüssel geteilt wird. [geöffnet] https://docs.cryptpad.org/en/dev_guide/general.html
- Edit-URL enthält zusätzlich eine Signatur; ein öffentlicher Verifikationsschlüssel erlaubt Prüfung, welche Nachricht von einem Editor stammt. [geöffnet] https://docs.cryptpad.org/en/dev_guide/general.html
- Channel-ID wird aus der Dokument-URL abgeleitet. [geöffnet] https://docs.cryptpad.org/en/dev_guide/general.html
- Jeder Account hat einen automatisch erzeugten öffentlichen Signaturschlüssel, "the only link between a user's data and their CryptPad account". [geöffnet] https://docs.cryptpad.org/en/dev_guide/basics.html
- Teams: "The team communication is encrypted with static keys." Ein ehemaliges Teammitglied behält laut Seite die Schlüssel. [geöffnet] https://docs.cryptpad.org/en/user_guide/security.html
- Ehemalige Mitglieder können laut Seite nur durch Änderung des Client-Codes weiter Zugriff auf Team-Dokumente haben; die offizielle Client-Software speichert keine Schlüssel verlassener Teams. [geöffnet] https://docs.cryptpad.org/en/user_guide/security.html
- Widerruf von Zugriff auf bereits geteilte Dokumente: auf der Security-Seite **nicht beschrieben**. Die Seite erwähnt Access-Listen als Begrenzung, nicht als Entzug bestehender Zugriffe. [geöffnet] https://docs.cryptpad.org/en/user_guide/security.html
- Team-Laufwerke: Mitglieder mit Bearbeitungsrecht können Zugriff weitergeben; laut Seite "Team members may even convert folders into shared folders and delegate their access". [geöffnet] https://docs.cryptpad.org/en/user_guide/security.html
- Getrennte Schlüssel für Team-Laufwerke oder geteilte Ordner: **nicht belegt** (nicht in der Security-Seite erwähnt).
- Whitepaper "CryptPad: End-to-End Encrypted Collaboration Suite", v1.1.0, 16.03.2023, Autor Theo von Arx. Im abgerufenen Teil nur Abstract: "a mix of asymmetric and symmetric encryption, as well as signing", Teamkollaboration. Abschnitte zu Schlüsselverteilung und Widerruf nicht gelesen. [geöffnet, Teil] https://blueprints.cryptpad.org/document/whitepaper/
- Seite "Team Key Revocation" im Blueprint-Menü verlinkt, nicht gelesen. Lücke.
- Quellcode-Stellen: nicht geprüft. Lücke.

Quellen Frage 5: 6 geöffnet, 0 Suchtreffer. Lücken: Quellcode, Widerruf, Team-Key-Details, Whitepaper-Abschnitte.

---

## (6) Vault-Vorlagen: Vergleich

Legende: + belegt; ~ teilweise; – nicht belegt.

| Funktion | 1Password | Apple Passwords | Bitwarden | KeePassXC | Proton Pass |
|---|---|---|---|---|---|
| Lizenz/Modell | – (nicht belegt) | – (nicht belegt) | – (nicht belegt) | + GPLv3 [geöffnet] keepassxc.org/docs | – (nicht belegt) |
| Passkeys | ~ (nur Standard-Teilnahme, nicht geprüft) | + Passkeys, Verifizierungscodes [geöffnet] | – (nicht belegt) | – nicht auf Seite [geöffnet] | – (nicht belegt) |
| Geteilte Tresore/Gruppen | + Shared Vaults, Vault-Ebene [Suchtreffer, AgileBits Security Design] | + Gruppen, Teilen/Entfernen [geöffnet, nur Themenliste] | + Organisation/Collections, Rollen [geöffnet] | – kein Teilen-Feature [geöffnet] | + Vault-Sharing, Schlüssel je Empfänger [Suchtreffer] |
| Verschlüsselung geteilter Daten | ~ Public-Key, Dienst hat keine Schlüssel [Suchtreffer] | – nicht belegt | ~ Org-Key pro Nutzer mit Public-Key [Suchtreffer, Drittquelle] | – (Datei-Ebene, kein Teilen) [geöffnet] | ~ Vault-Key je Nutzer verschlüsselt [Suchtreffer] |
| Import/Export | – (nicht belegt) | ~ Themen genannt, Formate nicht [geöffnet] | – (nicht belegt) | + KDBX 3.1/4 lesen, .kdb importieren [geöffnet] | – (nicht belegt) |
| Sync | – (nicht belegt) | + iCloud Keychain (macOS-Seite) [geöffnet] | – (nicht belegt) | – kein eingebauter Cloud-Sync [geöffnet] | – (nicht belegt) |
| Plattformen | – (nicht belegt) | ~ nur macOS auf der Seite [geöffnet] | – (nicht belegt) | + Linux, macOS, Windows, kein Mobil [geöffnet] | – (nicht belegt) |
| Browser-Integration | – (nicht belegt) | – nicht auf Seite | – (nicht belegt) | + KeePassXC-Browser für Firefox, Chrome [geöffnet] | – (nicht belegt) |

UX / UI:
- Apple Passwords: Themen wie Sicherheitsempfehlungen, Verlauf von Änderungen, Gruppenverwaltung werden als Themenliste genannt, Bedienabläufe nicht beschrieben. [geöffnet] https://support.apple.com/guide/passwords/welcome/mac (macOS 27)
- Microsoft Contoso Passkey Manager (nur Windows-Referenz für UX): Setup-Schritte und Windows-Hello-Bestätigung. [geöffnet] https://learn.microsoft.com/en-us/windows/apps/develop/security/third-party
- UX und UI von 1Password, Bitwarden, KeePassXC, Proton Pass: **nicht belegt** (Hilfeseiten nicht abrufbar oder nicht geprüft).

Quellen Frage 6 (Quelle je Zelle siehe oben): 5 Produkte, 9 geöffnete Seiten, 5 Suchtreffer. Nicht zugänglich: 1Password-Support (404), 1Password-Shared-Vaults-Support (404), Proton-Pass-Sharing (404), Proton-Support-Seite (404), Apple Credential Provider API (404), Proton Pass security model (nur Suchtreffer). Bitwarden Whitepaper nur als Suchtreffer-Fragment.

---

## Lücken

- Frage 1: CXP-Status heute nicht belegt; FIDO-Downloadseite nicht abrufbar; keine belegte Produktunterstützung für CXF/CXP.
- Frage 2: Linux-Browser-Wege außer credentialsd nicht belegt; Windows-API-Anforderungen (Version, Signierung) nicht belegt; Microsoft-API-Referenz nicht geöffnet; Apple-Credential-Provider nicht geprüft.
- Frage 3: Linux-Browser-Stand nicht belegt; Chrome/Edge-Versionsangaben nur Suchtreffer; Yubico-Browsertabelle nicht abrufbar; W3C-PRF-Abschnitt nicht gelesen.
- Frage 4: Weitere Rust-MLS-Implementierungen nicht recherchiert; OpenMLS-Audit nur über Spiegel; aktuelle crates.io-Version nicht geprüft.
- Frage 5: Quellcode-Stellen nicht geprüft; Whitepaper-Abschnitte zu Team-Schlüsseln und Widerruf nicht gelesen; Revocation-Seite nicht gelesen.
- Frage 6: Viele offizielle Support-Seiten nicht abrufbar (HTTP 404); UX/UI-Vergleich nicht belegt; Proton-Pass-Limits widersprüchlich (Suchtreffer: 20 vs. 50 Tresore).
- Abrufe mit Fehler: https://fidoalliance.org/specifications/download-cx/ (404), https://fidoalliance.org/specifications/ (ohne Ergebnis), https://developers.yubico.com/WebAuthn/WebAuthn_Browser_Support.html (300), https://developer.apple.com/documentation/authenticationservices/ascredentialproviderextension (404), https://support.1password.com/shared-vaults/ (404), https://proton.me/support/pass-sharing (404), https://developer.chrome.com/blog/webauthn-prf (404), https://www.1password.community/... (404).

Keine Empfehlung enthalten.

## Offen (für die nächste Runde, wenn fs-vault startet)

Diese Punkte sind in dieser Runde nicht belegt und werden nicht weiter recherchiert:

- **CXP-Status:** Stand des FIDO-Protokolls CXP nicht belegt (siehe Frage 1).
- **OpenMLS-Audit:** Das Audit (SRLabs) nur über Spiegel-Suchtreffer gesehen, nicht geprüft (siehe Frage 4).
- **Linux-Browserwege außer credentialsd:** nicht belegt (siehe Frage 2).
- **Windows-API-Anforderungen:** Version, Signierung und Registrierung des Drittanbieter-Providers nicht belegt (siehe Frage 2).
- **UX/UI-Vergleich der Vaults:** nicht belegt; nur Funktionsangaben aus Suchtreffern (siehe Frage 6).
