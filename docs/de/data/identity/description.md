# Identität (Web of Trust) – Beschreibung

**Was diese Domäne ist:** die Frage, **wem man glaubt** — Beglaubigungen (Attestations) zwischen Akteuren, Schlüssel und die Gewissheit, dass ein Konto/die Person wirklich die ist, für die man sie hält. Ansatz: **Web of Trust mit Treffen in der realen Welt** — Anton führt dazu ein Real-Life-Projekt (`real-life-org/web-of-trust`), Repo **gesichtet am 2026-11-02**; alle Fakten im zentralen Register ([standards.md → Nachrecherche](../standards.md)).

**Kernprinzip (aus Antons Projekt, ✅ gesichtet):** **Verification ≠ Trust.** Verifikation bestätigt nur: „Das ist wirklich diese Person“ (persönliches Treffen + QR-Scan). **Vertrauen** entsteht erst durch Beglaubigungen über die Zeit.

**Was sie abdeckt:**

- Beglaubigungs-Objekte: Subjekt – Relation – Objekt, plus Schlüssel, Zeit, Ort/Methode des Treffens
- Schlüssel-Andockung: `publicKey` am Actor, `cryptoKeys` in der Contact-Card, `did:key` (aus Antons Stack)
- Vertrauensfragen beantworten: „Wie stark ist die Kette von mir zu X?“ (Berechnung ist App-Thema, Daten hier)

**Abgrenzung:**

| Schicht | Domäne | Merksatz |
|---------|--------|----------|
| Zugang | [login/](../login/index.md) | Ein Login beweist **keine** Identität |
| Mensch-Daten | [people/](../people/index.md) | Was über die Person bekannt ist |
| Selbstbild | [profile/](../profile/index.md) | Was sie von sich zeigt |
| **Fremdbild-Vertrauen** | **identity/** | **Wem man glaubt** |

**Standard-Status:** ❌ keine etablierte WoT-Spec **im Standardisierungsgremium** gefunden. Aber: Antons **WoT Spec v0.1.0-draft** (✅ Repo gesichtet) kombiniert W3C **Verifiable Credentials**, **DIDComm v2.1**, **Ed25519**, **ECIES**; Nachfolger **RLTP** (Gen 3) in `real-life-org/trust-protocol`. Das ist unser Andockpunkt — eigene/mitgestaltete Spec, Spec-Kandidat Nr. 2.
