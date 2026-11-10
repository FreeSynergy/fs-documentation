# ADR 0067: Tresor (`fs-vault`) und Verschlüsselung: wer einbricht, kann mit den Daten nichts anfangen

- **Status:** akzeptiert (Nutzer, 2026-11-10)
- **Bezug:** ADR 0054 (keine Geheimnisse für Agenten), ADR 0066 (Datentypen), `docs/en/data/login/`, Personen mit sensiblen Angaben (DSGVO Art. 9)

## Kontext
Schlüssel liegen heute verstreut: Anmeldung über Kanidm (Passkeys, OIDC), GPG, der Speicherschlüssel des Messengers, Streaming-Schlüssel. Die Verfahren ändern sich laufend. Gleichzeitig wird immer öfter in Server eingebrochen. Ziel des Nutzers: **Einbrecher sollen die Daten stehlen können, aber nichts damit anfangen.** Trotzdem müssen Daten auf einem Server für Gruppen zusammen funktionieren.

## Entscheidung

### 1. Tresor als eigenes Programm `fs-vault`
- Ein Ort für alle Geheimnisse: Passwörter, Passkeys, Einmal-Codes (TOTP, RFC 6238), OpenPGP-, SSH- und age-Schlüssel, OIDC-Zugangsdaten, Zertifikate, Datenbank- und Gruppenschlüssel. Jede Art ist ein eigener Datentyp; neue Arten kommen dazu, ohne den Tresor umzubauen.
- Für die anderen Programme spricht der Tresor die Schnittstellen der Systeme: Secret Service (freedesktop) unter Linux, Credential Manager unter Windows. Kein Programm hält eigene Geheimnisse.
- Umzug: FIDO **CXF/CXP** (Credential Exchange) für Passkeys und Passwörter, Einlesen von KeePass (KDBX). Stand von CXF prüft Haiku.
- Entsperren: Passphrase (Argon2id), **Passkey mit PRF-Erweiterung** (WebAuthn Level 3) oder Hardware-Schlüssel (CTAP2 `hmac-secret`). Ein zweiter Weg zum Entsperren ist Pflicht.
- Passkeys ohne Online-Zwang: Anmelden ist ein Frage-Antwort-Austausch ohne Internet. Ein Passkey ist an einen Namen (Domain) gebunden, nie an eine IP; unsere eigenen Programme können lokal damit arbeiten, Browser brauchen eine Domain. Ob der Tresor unter Linux als Passkey-Anbieter für Browser dienen kann, prüft Haiku (unter Windows gibt es eine Schnittstelle für Drittanbieter).
- „Nie an eine KI“ (ADR 0054) wird im Tresor technisch durchgesetzt.
- Vorbilder: 1Password (UX), Apple Passwörter; Funktionen aus Bitwarden und KeePassXC (ADR 0066, Regel „bestes Programm“).

### 2. Verschlüsselung: der Server hält nur Zeichensalat
Vorbild ist **CryptPad** (Office mit Ende-zu-Ende-Verschlüsselung: der Server speichert und verteilt, lesen kann er nicht).

| Ort | Wie | Suche |
|---|---|---|
| Eigenes Gerät | Datenbankdatei immer verschlüsselt, Schlüssel im Tresor | voll, das eigene Programm entschlüsselt |
| Server, Daten einer Person | verschlüsselt mit dem Schlüssel der Person | auf dem Gerät der Person |
| Server, Daten einer Gruppe | verschlüsselt mit dem **Gruppenschlüssel** | auf den Geräten der Mitglieder |
| Öffentliches | nicht verschlüsselt (ist ohnehin öffentlich) | überall |

- **Gruppenschlüssel:** jede Gruppe hat einen; er liegt für jedes Mitglied mit dessen öffentlichem Schlüssel verpackt auf dem Server. Standard für Gruppenschlüssel: **MLS** (RFC 9420): Aufnahme und Austritt ohne alles neu zu verschlüsseln, Schlüssel wechseln bei jedem Austritt (neue Daten mit neuem Schlüssel; wer ging, liest nichts Neues mehr).
- Der Server bleibt nötig: er ist immer erreichbar, speichert, gleicht ab, verteilt, prüft Rechte über Signaturen. Lesen kann er nicht.
- Was der Server nicht kann (suchen, sortieren, automatisch handeln), machen die Geräte der Mitglieder. Soll etwas auf dem Server automatisch laufen (Bot, KI, Workflow), nimmt die Gruppe es **ausdrücklich als Mitglied** mit eigenem Schlüssel auf: sichtbar, jederzeit entziehbar.
- Felder, die der Server finden muss (z. B. „gibt es diese E-Mail?“), bekommen auf Wunsch einen **blinden Index** (HMAC des Werts): exakte Suche ohne den Wert zu kennen; sichtbar wird nur, dass zwei Werte gleich sind. Je Feld in der Typbeschreibung festgelegt.
- **Teilen** ist Standardbefehl jeder Typbeschreibung (Component in `fs-components`): innerhalb des Systems neu verschlüsselt für die Empfänger, nie im Klartext; nach außen als Link mit dem Schlüssel im Link-Fragment (der Server sieht ihn nie) und Ablaufzeit.

### 3. Später
- Geschützte Rechenkerne (AMD SEV-SNP, Intel TDX) mit Nachweis (Attestation) für Server, die doch lesen müssen.
- Homomorphe Verschlüsselung (rechnen auf verschlüsselten Daten) als Forschungspunkt, zuerst für Auszählungen in Umfragen und Abstimmungen.

## Folgen
- `fs-vault` kommt in die Programmkarte (Kategorie Identität); Kanidm bleibt Anmeldedienst.
- Typbeschreibungen bekommen je Feld eine Markierung „verschlüsselt“ und „blinder Index“ (Thread T, nächste Runde).
- Suche über verschlüsselte Daten ist Aufgabe des Geräts; Frontends zeigen das, statt still weniger zu finden.
- Offen zu prüfen (Haiku): Stand CXF/CXP, Passkey-Anbieter unter Linux, Rust-Umsetzungen von MLS (z. B. OpenMLS) und Lizenz.
