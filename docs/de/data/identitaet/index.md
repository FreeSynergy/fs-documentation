# Identität (Web of Trust)

Wer ist ein Akteur — und wem darf man glauben? Ansatz: **Web of Trust mit Treffen in der realen Welt** (externes Projekt, das wir mit unterstützen wollen, Standard in Arbeit).

## Bestand

| Stück | Beleg | Rolle bei FreeSynergy |
|-------|-------|-----------------------|
| ❌ **keine etablierte WoT-Spec gefunden** | ❌ | eigene/mitgestaltete Spec — unser Spec-Kandidat Nr. 2 nach Block/Dokument |
| **AS2-Typ `Relationship`** (Vocabulary) | ✅ Vokabular gelesen | formaler Andockpunkt für Aussagen wie „A beglaubigt B für PGP-Key K“ |
| **ActivityPub `publicKey` am Akteur** | ✅ Vokabular gelesen | Schlüssel, an den Beglaubigungen andocken |
| **Signatur-Mechanismen für ActivityPub-Objekte** | ❌ (alte Referenz war 404, siehe Korrekturliste) | muss vor jeder Verwendung neu recherchiert werden |

## Vorläufige Regeln

1. Beglaubigungen sind **eigene Objekte** (Subjekt – Relation – Objekt + Schlüssel + Zeit + Ort/Methode des Treffens), nicht Felder am Profil.
2. Beglaubigungen reisen im AS2-Envelope (`Create` auf einem `Relationship`-Objekt), damit WoT-Austausch wie alle Daten läuft (Beschluss 2).
3. Ein „Login“ beweist keine Identität — Login ([login/](../login/index.md)) und Vertrauen sind getrennte Schichten.

## Offene Punkte

- Standard von Antons Projekt sichten und in dieser Domäne als `mapping.md` auf `Relationship`/`publicKey` abbilden
- Signatur-Recherche (welcher Mechanismus ist real belegt?)

## Siehe auch

- [standards.md → Korrekturliste](../standards.md) (Signatur-Referenz 404)
- [profil/](../profil/index.md), [login/](../login/index.md)
