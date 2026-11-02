# Profil – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.**

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **AS2-`Actor`** (Core/Vocabulary) | ✅ gelesen | Hülle der öffentlichen Ansicht: `id` (absoluter IRI, Core §4.1), `name`/`nameMap`, `preferredUsername`, `publicKey` |
| **AS2-`Profile`-Typ** (Vocabulary) | ✅ im Vocabulary vorhanden; Feld-Details ⚠️ Abschnitt noch belegen | „A profile object contains minimal information about its owner.“ — Kandidat für die Minimal-Ansicht |
| **AS2-Audience `to`/`cc`/`bto`/`bcc`** | ✅ Core gelesen | Offenlegungssteuerung pro Feld/Feldgruppe; **keine** Zugriffskontrolle (Beschluss 2) |
| **JSContact `Card`** (RFC 9553) | ✅ | Quelle der angezeigten Felder |
| **schema.org `Person`** | ⚠️ nicht verifiziert; `name` ✅ | Web-/SEO-Exportprojektion |
| **FOAF** | ⚠️ nicht belegt (bisher nur als Vokabular bekannt) | Alt-Vokabular für Person-Links; nur bei Interop-Bedarf belegen |

## Kanonische Regel (Beschluss 1)

Profil = **AS2-`Actor`-Projektion auf JSContact**. Der Handle (Actor) ist die soziale Identität; die Inhalte kommen aus der Card; die Regeln entscheiden die Sichtbarkeit.

## Was die Standards hier NICHT regeln (Lücken → eigene Festlegung)

1. **Feldgruppen/Zweckbindung:** kein Standard sagt, welche Felder zusammen ausgegeben werden dürfen → unsere Feldgruppen-Tabelle in [technical.md](technical.md) (noch nicht beschlossen).
2. **Sensible Felder:** kein Datenstandard markiert „besonders schutzwürdig“; das ist Rechtsanwendung (DSGVO Art. 9 — ⚠️ Zitat nicht belegt) plus our product rule.
3. **Profil-Vollständigkeitsanzeige** (Progress-Ringe etc.) ist UI, kein Datenstandard.

## Offene Standard-Punkte

- `Profile`-Typ feldgenau belegen und entscheiden, ob wir ihn als Antwort-Form nutzen oder Actor-Direktdarstellung
- schema.org `Person` verifizieren, bevor SEO-Export gebaut wird
- Antons `wot-profiles` (JWS-signierte Profil-Auffindbarkeit, ✅ gesichtet) als Referenz für signierte Profil-Auslieferung aufnehmen — Signaturmechanismus bleibt ⚠️/❌ offen
