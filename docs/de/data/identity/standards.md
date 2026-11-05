# Identität (Web of Trust) – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.** Für diese Domäne gilt der Abschnitt „Nachrecherche 2026-11-02: Identität / Web of Trust“ dort als Volltext-Ersatz.

## Bestand

| Stück | Beleg | Rolle bei FreeSynergy |
|-------|-------|-----------------------|
| ❌ **keine etablierte WoT-Spec im Standardisierungsgremium** | ❌ | eigene/mitgestaltete Spec — Spec-Kandidat Nr. 2 |
| **WoT Spec v0.1.0-draft (real-life-org/web-of-trust)** | ✅ Repo gesichtet 2026-11-02 | kombiniert W3C **Verifiable Credentials** + **DIDComm v2.1** + **Ed25519** + **ECIES**; Grundsatz „Verification ≠ Trust“; BIP39 → HKDF → Ed25519/X25519; `did:key`; Relays sehen nur Chiffretext; Autorisierung UCAN-inspiriert, offline-verifizierbar |
| **RLTP (Real Life Trust Protocol), Gen 3** (`real-life-org/trust-protocol`) | ✅ Existenz gesichtet | Nachfolger — Fixes bei Anton laufen dorthin; wir orientieren unsere Andockpunkte daran |
| **AS2-Typ `Relationship`** (Vocabulary) | ✅ Vokabular gelesen | formaler Andockpunkt: „A beglaubigt B für Key K“ |
| **AS2-Akteursschlüssel** | ✅ | `Multikey` (FEP-521a), `publicKey` alt — Schlüssel, an die Beglaubigungen andocken |
| **Signatur-Mechanismen für ActivityPub-Objekte** | ❌ alte Referenz war 404 (Korrekturliste im Register) | muss neu recherchiert werden, bevor Signatur spezifiziert wird |

## Vorläufige Regeln (Standards-nahe Festlegungen)

1. Beglaubigungen sind **eigene Objekte** (Subjekt – Relation – Objekt + Schlüssel + Zeit + Methode), nicht Felder am Profil.
2. Sie reisen im AS2-Envelope als `Create` auf `Relationship` (Beschluss 2).
3. **Ein Login beweist keine Identität** — [login/](../login/index.md) und Vertrauen sind getrennte Schichten.
4. Schlüssel werden als `Multikey` veröffentlicht (FEP-521a, ✅), `publicKey` nur für Kompatibilität. Ein Akteur kann mehrere Schlüssel haben; Attestationen zeigen auf **Schlüssel**, Personen-Vertrauen aggregiert über Schlüssel (aggregieren = App-Rechnung, nicht Speicher).

## Offene Standard-Punkte

- ~~Beleg DID Core / VC~~ → ✅ 2026-11-05 (Status weiter oben); feldgenauer Abgleich mit RLTP noch offen
- ~~Signatur-Mechanismus~~ → ✅ RFC 9421 (Transport) + FEP-8b32 (Objekte) + FEP-521a (`Multikey`)
- **Pairwise Kennungen (RLTP):** eine Person hat pro Beziehung ein anderes DID → Hub-Zuordnung (ADR 0019) kann nicht mit einem DID pro Person rechnen; offen
- `identity/mapping.md` schreiben: WoT-Spec-Begriffe ↔ AS2-`Relationship`/`publicKey` (Auftrag in [requirements.md §7](../requirements.md))
