# Daten – Gesprächsprotokoll und Arbeitsauftrag (2026-11-02)

Diese Datei sichert, **was im Gespräch festgelegt wurde** — damit der Stand erhalten bleibt und wir nicht von vorne anfangen müssen. Status: **Arbeitsdokument**, noch keine Specification. Die Beschlüsse vom 2026-11-01 ([standards.md](standards.md)) gelten weiter; dieses Dokument führt sie fort.

## 1. Grundauftrag

- Es geht um **die Daten — und wie man sie abspeichern kann**.
- Als Erstes brauchen wir **die ganzen Standards**. Egal ob **ISO, DIN, RFC, W3C** usw.
- Was schon gemacht wurde (Standards-Register, Beschlüsse 1–5, Domänen-Verzeichnisse), wird **weitergemacht**, nicht neu erfunden.
- **Verzeichnisse auf Englisch benennen**, wie alle anderen Bereiche auch.
- **Zurzeit nur `docs/de/` pflegen; `docs/en/` kommt später.** (ausdrückliche Anweisung 2026-11-02)
- Erst besprechen, dann aufschreiben — diese Datei ist das gesicherte Gesprächsprotokoll; Verbesserung in kleinen Schritten.

## 2. Die genannten Domänen (in den Worten des Auftraggebers)

| Domäne (engl. Verzeichnis) | Was dazu gesagt wurde |
|----------------------------|-----------------------|
| `login/` | Logins — z. B. **OAuth**, **SCIM** — und das **Web of Trust von Anton**, der damit ein Real-Life-Projekt macht: <https://github.com/real-life-org/web-of-trust> |
| `person/` | **Der Mensch, der sich anmeldet.** (wahrscheinlich vCard — oder sowas) |
| `profile/` | Jeder Mensch kann **Profile** haben, damit man **die Seiten von sich zeigt, die man zeigen möchte**. Beispiel: bei Dating kann es **gefährlich** werden, wenn die Sexualität rauskommt. → Sichtbarkeit ist ein Kernproblem dieser Domäne. |
| `events/` | Die Termine, die man bei Kalender u. ä. angibt. |
| `projects/` | Für PMs (Projektmanagement) — offene Frage: **gibt es da einen Standard?** → Recherche nötig. |
| `messages/` | Messages — noch nicht weiter ausgeführt; aus den Apps ableiten. |

Dazu die bereits bestehenden Domänen: `contacts/` (Kontaktmodelle), `identity/` (Web of Trust), `geodata/` (Orte/Adressen).

## 3. Auftrag: aus den Apps ableiten

> „Schau Dir die Apps an — und schau an, was da gespeichert werden könnte. Das alles muss irgendwie standardisiert werden. Herausfinden, was wohin gehört.“

→ Nächster konkreter Schritt: **Dateninventur pro App** in [docs/de/programs/](../programs/) (jede App hat bzw. bekommt eine `api.md`), Zuordnung der gefundenen Daten zu den Domänen. Ergebnis kommt in dieses Dokument bzw. in die jeweilige Domäne.

## 4. Struktur pro Domäne (neu festgelegt 2026-11-02)

Jedes Domänen-Verzeichnis enthält künftig:

| Datei | Inhalt |
|-------|--------|
| `index.md` | Überblick + Standard-Tabelle + offene Punkte |
| `description.md` | **Beschreibung** — was die Domäne ist, was sie abdeckt, Abgrenzung zu anderen Domänen |
| `technical.md` | **Technische Erklärung** — Speicherperspektive, Schlüssel, Fluss, Projektionen |
| `standards.md` | **Standardtexte** — die einschlägigen Standards mit Belegstatus und Feldlisten/Auszügen |
| `examples.md` | **Beispiele** — konkrete JSON-/Textbeispiele |

Ergänzungen sind ausdrücklich erwünscht (z. B. pro Standard ein Unterverzeichnis mit `description.md` + `storage.md`, wie für JSContact bereits vorgesehen).

## 5. Verzeichnisnamen: Englisch (umbenannt am 2026-11-02)

| alt (deutsch) | neu (englisch) |
|---------------|----------------|
| `kontakt/` | `contacts/` |
| `profil/` | `profile/` |
| `projekte/` | `projects/` |
| `identitaet/` | `identity/` |
| `geodaten/` | `geodata/` |
| `events/`, `login/`, `messages/` | unverändert |
| — | `person/` **angedacht, aber noch nicht angelegt** — siehe Beschluss-Kandidat 6 (offene Frage 6.4) |

**Neu gedachte Abgrenzung:** `person/` = der Mensch (echte Person hinter einem Konto) · `contacts/` = Kontakt-Datensätze (auch über andere) · `profile/` = was man von sich **zeigt** · `login/` = der **Zugang** · `identity/` = wem man **glaubt**.

## 5a. Belegstand 2026-11-02 (Recherche abgeschlossen — **nicht erneut herunterladen**)

Alle abgerufenen Fakten stehen **vollständig** in [standards.md → „Nachrecherche 2026-11-02“](standards.md). Zusammenfassung:

- **OIDC Core 1.0 (errata set 2, 2023-12-15)** ✅ belegt — ⚠️→✅
- **OAuth 2.0 RFC 6749** ✅ belegt (Aktualisierungen: RFC 8252, 8996, 9700) — ⚠️→✅
- **WebAuthn Level 2 (W3C Rec. 2021-04-08)** ✅ belegt — neu im Register
- **SCIM RFC 7643/7644** ⚠️ weiterhin ungeprüft (Abruf abgebrochen, auf Anweisung nicht wiederholt)
- **Antons WoT-Repo gesichtet:** WoT Spec v0.1.0-draft = W3C Verifiable Credentials + DIDComm v2.1 + Ed25519 + ECIES; `did:key`; Grundsatz „Verification ≠ Trust“; Nachfolger RLTP (Gen 3) in `real-life-org/trust-protocol`. Alle Details in standards.md.
- **Projekte:** ISO 21502:2020 ✅ (Prozess-Leitfaden, **kein Datenformat**); MSPDI/`mspdi_pj12.xsd` ✅ (De-facto-Exportformat); W6C ⚠️ unbelegt; **keine offene RFC/W3C-Daten-Spec für Boards/Tasks** → eigene Spec bleibt Spec-Kandidat Nr. 3.

## 6. Offene Fragen aus dem Gespräch

1. **projects:** existiert ein PM-Standard? → **beantwortet 2026-11-02:** kein offener Daten-Standard; ISO 21502 = Prozess, MSPDI = proprietär. Eigene Spec bleibt. (Details in standards.md → Nachrecherche)
2. **messages:** was genau — Chat, Kommentare, Mail? → aus App-Inventur ableiten
3. **profile:** Feldgruppen / Zweckbindung umsetzen (Dating-Beispiel: sensible Felder wie `sexualOrientation` gehören **nicht** in den Arbeits-/Kalender-Kontext; BDSG/DSGVO-Besonderer Kategorien ⚠️ belegen)
4. **person:** **offen — Beschluss-Kandidat Nr. 6.** Vorschlag des Agenten: **kein eigenes `person/`-Verzeichnis.** Begründung: Die Personendaten des Menschen sind bereits abgedeckt — eine JSContact-`Card` mit Rolle „individual“ in `contacts/`, verknüpft mit dem Konto (`sub` aus `login/`) und dem sozialen Actor (`profile/`). Übrig bleiben wirklich **zwei** Domänen wie im Gespräch gesagt: `identity/` (wem glaubt man — WoT, DIDs, Verifiable Credentials) und `profile/` (was zeigt man wem). `person/` wäre nur eine Projektion ohne eigene Daten. → **bitte bestätigen oder verwerfen.**
5. **identity:** Antons Repo `real-life-org/web-of-trust` **gesichtet 2026-11-02** — Fakten in standards.md → Nachrecherche; `mapping.md` (AS2 `Relationship`/`publicKey`) noch ausstehend

## 7. Nächste Schritte (Häkchen setzen, damit man sieht, wo wir stehen)

- [x] Gespräch gesichert (diese Datei)
- [x] Verzeichnisse umbenannt (englisch), `person/` neu angelegt
- [x] Jede Domäne mit `description.md` / `technical.md` / `standards.md` / `examples.md` bestückt (Erstfassung) — **tatsächlich fertig am 2026-11-02** (8 Domänen × 4 Dateien; `person/` wartet auf Beschluss-Kandidat 6)
- [ ] App-Dateninventur (docs/de/apps/) → Zuordnung „was gehört in welche Domäne“
- [x] Beleglage ergänzt 2026-11-02: OIDC ✅, OAuth ✅, WebAuthn ✅, Antons WoT ✅, Projekte recherchiert; **offen geblieben: SCIM ⚠️, MLS ⚠️, DID Core/VC ⚠️, W6C ⚠️** (nicht erneut herunterladen — alles Bestehende steht in standards.md)
- [x] Antons WoT-Repo gesichtet (Fakten in standards.md); → `identity/mapping.md` noch offen
- [ ] `en/`-Übersetzung, wenn `de/` steht
