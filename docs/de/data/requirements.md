# Daten – Gesprächsprotokoll und Arbeitsauftrag (2026-11-02)

Diese Datei hält fest, **was im Gespräch entschieden wurde**, damit der Stand erhalten bleibt und wir nicht von vorn anfangen müssen. Status: **Arbeitsdokument**, noch keine Spezifikation. Die Entscheidungen vom 2026-11-01 ([standards.md](standards.md)) gelten weiter; dieses Dokument baut darauf auf.

## 1. Grundauftrag

- Es geht um **die Daten — und wie man sie speichern kann**.
- Zuerst brauchen wir **alle Standards**. Ob **ISO, DIN, RFC, W3C** und so weiter.
- Was schon getan wurde (Standard-Register, Entscheidungen 1–5, Domänen-Verzeichnisse), wird **fortgeführt**, nicht neu erfunden.
- **Verzeichnisse auf Englisch benennen**, wie alle anderen Bereiche.
- **Vorerst nur `docs/de/` pflegen; `docs/en/` kommt später.** (ausdrückliche Anweisung 2026-11-02)
- Erst besprechen, dann aufschreiben — diese Datei ist das erhaltene Gesprächsprotokoll; Verbesserung in kleinen Schritten.

## 2. Die genannten Domänen (in den Worten der Person, die die Arbeit beauftragt hat)

| Domäne (englisches Verzeichnis) | Was dazu gesagt wurde |
|----------------------------|------------------------|
| `login/` | Anmeldungen — z. B. **OAuth**, **SCIM** — und **Antons Web of Trust**, für das er ein reales Projekt betreibt: <https://github.com/real-life-org/web-of-trust> |
| `person/` | **Der Mensch, der sich anmeldet.** (wahrscheinlich vCard — oder etwas Ähnliches) |
| `profile/` | Jede Person kann **Profile** haben, damit man **die Seiten von sich zeigt, die man zeigen will**. Beispiel: Beim Dating kann es **gefährlich** werden, wenn die Sexualität bekannt wird. → Sichtbarkeit ist ein Kernproblem dieser Domäne. |
| `events/` | Die Termine, die man in einem Kalender einträgt, und ähnliches. |
| `projects/` | Für PM (Projektmanagement) — offene Frage: **Gibt es dafür einen Standard?** → Recherche nötig. |
| `messages/` | Nachrichten — noch nicht ausgearbeitet; aus den Apps ableiten. |

Dazu kommen die bereits bestehenden Domänen: `contacts/` (Kontaktmodelle), `identity/` (Web of Trust), `geodata/` (Orte/Adressen).

## 3. Reihenfolge: aus den Apps ableiten

> „Schau dir die Apps an — und schau, was dort gespeichert werden könnte. All das muss irgendwie standardisiert werden. Finde heraus, was wohin gehört.“

→ Nächster konkreter Schritt: **Datenbestand pro App** in [docs/de/programs/](../programs/) (jede App hat oder bekommt eine `api.md`), die gefundenen Daten den Domänen zuordnen. Das Ergebnis kommt in dieses Dokument oder in die jeweilige Domäne.

## 4. Aufbau pro Domäne (neu festgelegt 2026-11-02)

Jedes Domänen-Verzeichnis enthält ab jetzt:

| Datei | Inhalt |
|------|--------|
| `index.md` | Übersicht + Standard-Tabelle + offene Punkte |
| `description.md` | **Beschreibung** — was die Domäne ist, was sie abdeckt, Abgrenzung zu anderen Domänen |
| `technical.md` | **technische Erklärung** — Speicher-Sicht, Schlüssel, Ablauf, Projektionen |
| `standards.md` | **Standardtexte** — die relevanten Standards mit Beleg-Status und Feldlisten/Auszügen |
| `examples.md` | **Beispiele** — konkrete JSON-/Textbeispiele |

Ergänzungen sind ausdrücklich erwünscht (z. B. pro Standard ein Unterverzeichnis mit `description.md` + `storage.md`, wie schon für JSContact geplant).

## 5. Verzeichnisnamen: Englisch (umbenannt am 2026-11-02)

| alt (deutsch) | neu (englisch) |
|--------------|---------------|
| `kontakt/` | `contacts/` |
| `profil/` | `profile/` |
| `projekte/` | `projects/` |
| `identitaet/` | `identity/` |
| `geodaten/` | `geodata/` |
| `events/`, `login/`, `messages/` | unverändert |
| — | `person/` **erwogen, aber noch nicht angelegt** — siehe Entscheidungskandidat 6 (offene Frage 6.4) |

**Neu erwogene Abgrenzung:** `person/` = der Mensch (die echte Person hinter einem Konto) · `contacts/` = Kontaktdatensätze (auch über andere) · `profile/` = was man **über sich zeigt** · `login/` = der **Zugang** · `identity/` = wem man **vertraut**.

## 5a. Beleg-Stand 2026-11-02 (Recherche abgeschlossen — **nicht erneut herunterladen**)

Alle abgerufenen Fakten stehen **vollständig** in [standards.md → „Folgerecherche 2026-11-02“](standards.md). Zusammenfassung:

- **OIDC Core 1.0 (Errata-Set 2, 2023-12-15)** ✅ belegt — ⚠️→✅
- **OAuth 2.0 RFC 6749** ✅ belegt (Aktualisierungen: RFC 8252, 8996, 9700) — ⚠️→✅
- **WebAuthn Level 2 (W3C Rec. 2021-04-08)** ✅ belegt — neu im Register
- **SCIM RFC 7643/7644** ⚠️ noch ungeprüft (Abruf abgebrochen, auf Anweisung nicht wiederholt)
- **Antons WoT-Repo geprüft:** WoT Spec v0.1.0-draft = W3C Verifiable Credentials + DIDComm v2.1 + Ed25519 + ECIES; `did:key`; Prinzip „Verifikation ≠ Vertrauen“; Nachfolger RLTP (Generation 3) in `real-life-org/trust-protocol`. Alle Details in standards.md.
- **Projekte:** ISO 21502:2020 ✅ (Prozessleitfaden, **kein Datenformat**); MSPDI/`mspdi_pj12.xsd` ✅ (de-facto-Exportformat); W6C ⚠️ nicht belegt; **keine offene RFC-/W3C-Datenspezifikation für Boards/Aufgaben** → eigene Spezifikation bleibt Kandidat Nr. 3.

## 6. Offene Fragen aus dem Gespräch

1. **projects:** Gibt es einen PM-Standard? → **beantwortet 2026-11-02:** kein offener Datenstandard; ISO 21502 = Prozess, MSPDI = proprietär. Eigene Spezifikation bleibt. (Details in standards.md → Folgerecherche)
2. **messages:** Was genau — Chat, Kommentare, Mail? → aus dem App-Bestand ableiten
3. **profile:** Feldgruppen und Zweckbindung umsetzen (Dating-Beispiel: sensible Felder wie `sexualOrientation` gehören **nicht** in den Arbeits- oder Kalenderkontext; BDSG/DSGVO-Sonderkategorien ⚠️ zu belegen)
4. **person:** **offen — Entscheidungskandidat Nr. 6.** Der Vorschlag des Agenten: **kein eigenes Verzeichnis `person/`.** Begründung: Die Personendaten des Menschen sind schon abgedeckt — eine JSContact-`Card` mit der Rolle „individual“ in `contacts/`, verknüpft mit dem Konto (`sub` aus `login/`) und dem sozialen Akteur (`profile/`). Übrig bleiben tatsächlich **zwei** Domänen, wie im Gespräch genannt: `identity/` (wem man vertraut — WoT, DIDs, Verifiable Credentials) und `profile/` (was man wem zeigt). `person/` wäre nur eine Projektion ohne eigene Daten. → **bitte bestätigen oder ablehnen.**
5. **identity:** Antons Repo `real-life-org/web-of-trust` **geprüft 2026-11-02** — Fakten in standards.md → Folgerecherche; `mapping.md` (AS2 `Relationship`/`publicKey`) steht noch aus

## 7. Nächste Schritte (Kästchen abhaken, damit man den Stand sieht)

- [x] Gespräch festgehalten (diese Datei)
- [x] Verzeichnisse umbenannt (englisch), `person/` neu angelegt
- [x] jede Domäne mit `description.md` / `technical.md` / `standards.md` / `examples.md` ausgestattet (erster Entwurf) — **am 2026-11-02 abgeschlossen** (8 Domänen × 4 Dateien; `person/` wartet auf Entscheidungskandidat 6)
- [ ] Datenbestand der Apps erfassen (docs/de/apps/) → Zuordnung „was gehört in welche Domäne“
- [x] Belege ergänzt 2026-11-02: OIDC ✅, OAuth ✅, WebAuthn ✅, Antons WoT ✅, Projekte recherchiert; **offen gelassen: SCIM ⚠️, MLS ⚠️, DID Core/VC ⚠️, W6C ⚠️** (nicht erneut herunterladen — alles Vorhandene steht in standards.md)
- [x] Antons WoT-Repo geprüft (Fakten in standards.md); → `identity/mapping.md` noch offen
- [ ] `en/`-Übersetzung, sobald `de/` vollständig ist
