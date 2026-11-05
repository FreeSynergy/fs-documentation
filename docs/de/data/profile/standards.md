# Profil – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.**

## Stand 2026-11-05

Beleg: `temp/research/geodata-projects-profile-login.md` (2026-11-05).

| Standard | Beleg | Rolle |
|----------|-------|-------|
| schema.org `Person` | ✅ Kern, als äquivalent zu `foaf:Person` erklärt | Exportprojektion (Web/SEO) |
| FOAF 0.99 (2014-01) | ✅ ungepflegt | nicht genutzt |
| DSGVO Art. 9 „Verarbeitung besonderer Kategorien personenbezogener Daten“ | ✅ (über den Mirror gdpr-info.eu) | rechtliche Grundlage der Markierung (ADR 0029) |
| **W3C DPV 2.3** (2026-02-25, Final CG Report — keine Recommendation) | ✅ | Markierungsvokabular (ADR 0029): `dpv:SpecialCategoryPersonalData`; `pd:SexualPreference`, `pd:Sexual` (kein `SexualOrientation`); die DSGVO-Erweiterung enthält die Rechtsgrundlagen Art. 9(2)(a)–(j) |

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **AS2-`Actor`** (Core/Vocabulary) | ✅ gelesen | Hülle der öffentlichen Ansicht: `id` (absoluter IRI, Core §4.1), `name`/`nameMap`, `preferredUsername`, `publicKey` |
| **AS2-`Profile`-Typ** (Vocabulary) | ✅ geprüft 2026-11-05: „describes another object, usually an actor“; Eigenschaft `describes` | **Envelope der öffentlichen Ansicht**: ein `Profile`, dessen `describes` auf **mich selbst** zeigt (mein Schauspieler/DID). Gleicher Typ wie eine Kontakt-Card, die *jemand anderen* beschreibt (ADR 0020) |
| **AS2-Audience `to`/`cc`/`bto`/`bcc`** | ✅ Core gelesen | Offenlegungssteuerung pro Feld/Feldgruppe; **keine** Zugriffskontrolle (Beschluss 2) |
| **JSContact `Card`** (RFC 9553) | ✅ | Quelle der angezeigten Felder |
| **schema.org `Person`** | ⚠️ nicht verifiziert; `name` ✅ | Web-/SEO-Exportprojektion |
| **FOAF** | ⚠️ nicht belegt (bisher nur als Vokabular bekannt) | Alt-Vokabular für Person-Links; nur bei Interop-Bedarf belegen |

## Kanonische Regel (Beschluss 1)

Profil = **AS2-`Actor`-Projektion auf JSContact**. Der Handle (Actor) ist die soziale Identität; die Inhalte kommen aus der Card; die Regeln entscheiden die Sichtbarkeit.

## Was die Standards hier NICHT regeln (Lücken → eigene Festlegung)

1. **Feldgruppen/Zweckbindung:** kein Standard sagt, welche Felder zusammen ausgegeben werden dürfen → unsere Feldgruppen-Tabelle in [technical.md](technical.md) (noch nicht beschlossen).
2. **Sensible Felder:** kein Datenstandard markiert „besonders schutzwürdig“; das ist Rechtsanwendung (DSGVO Art. 9 — ⚠️ Zitat nicht belegt) plus unsere Produktregel.
3. **Profil-Vollständigkeitsanzeige** (Progress-Ringe etc.) ist UI, kein Datenstandard.

## Offene Standard-Punkte

- ~~`Profile`-Typ belegen~~ → ✅ 2026-11-05: Profil = AS2 `Profile`, das mich selbst beschreibt; der Schauspieler (`Person` mit `Multikey`, FEP-521a) bleibt die Identität
- schema.org `Person` verifizieren, bevor der SEO-Export gebaut wird
- Antons `wot-profiles` (JWS-signierte Profil-Auffindbarkeit, ✅ gesichtet) als Referenz für signierte Profil-Auslieferung — Signaturen: FEP-8b32-Objekt-Proofs + RFC 9421 Transport (✅ 2026-11-05)
