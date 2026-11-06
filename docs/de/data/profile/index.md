# Profil

Was man **von sich zeigen möchte** — die öffentlich sichtbare, publikumsgesteuerte Ansicht der Personendaten.

## Grundmodell (Beschluss 1+2)

Ein Profil ist **keine zweite Kopie der Personendaten**, sondern eine **Projektion**:

- Speicherechte Daten: JSContact-`Card` in [people/](../people/)
- Soziale Identität: AS2-`Actor` (`id` = URI nach Beschluss 3, `name`, `preferredUsername`, `publicKey`)
- Sichtbarkeit: **Audience-Felder** `to`/`cc`/`bto`/`bcc` entscheiden, welche Felder an wen herausgegeben werden — Offenlegungssteuerung, keine Zugriffskontrolle (Beschluss 2)

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **AS2-`Actor` / `Profile`** | ✅ (2026-11-05) | öffentliche Ansicht = `Profile` mit `describes` → ich selbst; Kontakte nutzen denselben Typ für andere (ADR 0020) |
| **JSContact `Card`** | ✅ | Quelle der angezeigten Felder |
| **schema.org `Person` / `name`** | `name` ✅, `Person` ⚠️ | Export-Projektion für Web/SEO |
| **AS2-Audience (`to`/`cc`/`bto`/`bcc`)** | ✅ Core gelesen | Publikumsregeln pro Feld/Feldgruppe |

## Offene Punkte

- Feldgruppen-Modell („Arbeit", „Privat", „Öffentlich") als eigene Festlegung? Noch nicht beschlossen.
- Profilwechsel (`Update` auf Actor) und Verfolgung (`Follow`) gehören in den Envelope, nicht hierhin.

## Siehe auch

- [people/](../people/index.md), [identity/](../identity/index.md)
- [standards.md → Aktivitäten](../standards.md)
