# Identität (Web of Trust)

Wer ist ein Akteur — und wem darf man glauben? Ansatz: **Web of Trust mit Treffen in der realen Welt** (externes Projekt, das wir mit unterstützen wollen, Standard in Arbeit).

## Bestand

| Stück | Beleg | Rolle bei FreeSynergy |
|-------|-------|-----------------------|
| ❌ **keine etablierte WoT-Spec im Standardisierungsgremium** | ❌ | eigene/mitgestaltete Spec — unser Spec-Kandidat Nr. 2 nach Block/Dokument |
| **WoT Spec v0.1.0-draft (real-life-org/web-of-trust)** | ✅ Repo gesichtet 2026-11-02 | kombiniert W3C Verifiable Credentials + DIDComm v2.1 + Ed25519 + ECIES; `did:key`; Grundsatz „Verification ≠ Trust“; Nachfolger RLTP (Gen 3). Alle Fakten in [standards.md → Nachrecherche](../standards.md) — **nicht erneut herunterladen** |
| **AS2-Typ `Relationship`** (Vocabulary) | ✅ Vokabular gelesen | formaler Andockpunkt für Aussagen wie „A beglaubigt B für PGP-Key K“ |
| **ActivityPub `publicKey` am Akteur** | ✅ Vokabular gelesen | Schlüssel, an den Beglaubigungen andocken |
| **Signatur-Mechanismen für ActivityPub-Objekte** | ❌ (alte Referenz war 404, siehe Korrekturliste) | muss vor jeder Verwendung neu recherchiert werden |

## Vorläufige Regeln

1. Beglaubigungen sind **eigene Objekte** (Subjekt – Relation – Objekt + Schlüssel + Zeit + Ort/Methode des Treffens), nicht Felder am Profil.
2. Beglaubigungen reisen im AS2-Envelope (`Create` auf einem `Relationship`-Objekt), damit WoT-Austausch wie alle Daten läuft (Beschluss 2).
3. Ein „Login“ beweist keine Identität — Login ([login/](../login/index.md)) und Vertrauen sind getrennte Schichten.

## Offene Punkte

- ~~Antons Repo sichten~~ → **erledigt 2026-11-02**, Fakten in standards.md; als `mapping.md` auf `Relationship`/`publicKey` abbilden ist noch offen
- Signatur-Recherche (welcher Mechanismus ist real belegt?) — Antons Stack liefert Indizien (Ed25519, JWS, UCAN-inspiriert), W3C-DIDs/VC noch ⚠️

## Siehe auch

- [standards.md → Korrekturliste](../standards.md) (Signatur-Referenz 404)
- [profile/](../profile/index.md), [login/](../login/index.md)
