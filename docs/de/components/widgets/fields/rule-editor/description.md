# Rule Editor (Regeleditor)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `list`, `simple` |
| **Zustände** | `enabled`, `disabled`, `invalid`, `unsaved` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `reorder`, `fade-in` |
| **Verwandt** | `repeater`, `select`, `text-input`, `switch`, `tags-input` |
| **Status** | Skizze |

## Beschreibung

Ein Regeleditor bearbeitet Regeln der Form „wenn ... dann ...“: Bedingungen, Aktionen und einen Ein-/Aus-Schalter pro Regel. Regeln werden als **Sieve** gespeichert.

## Verwendungszweck

- Mailfilterregeln (sortieren, markieren, verschieben, stummschalten)
- Wort- und Benutzerfilter im Chat
- Automatische Behandlung pro Unterhaltung

## Varianten

| Variante | Beschreibung |
|---|---|
| **list** | eine Zeile pro Regel, direkt bearbeitet |
| **simple** | eine einzelne Regel, z. B. ein Wortfilter |

## Features

- Zeilen aus [repeater](../../data/repeater/), [select](../../../primitives/fields/select/), [text-input](../../../primitives/fields/text-input/) und [switch](../../../primitives/fields/switch/)
- Mehrere Bedingungen (alle oder beliebige) und mehrere Aktionen
- Umsortieren, Duplizieren, Testlauf (`rule.run`)
- Prüfung vor dem Speichern

## Datenbindung

Bindet Sieve (RFC 5228; für Mail über JMAP Sieve, RFC 9661). Dasselbe Regelmodell wird auf Chat-Unterhaltungen angewendet (Messenger-Anforderung `rule.create`, `rule.run`). Darstellungsregister (ADR 0023): `Rule → rule-editor | text` (Sieve-Quelltext).

## Abgrenzung

- **Nicht verwechseln mit** [repeater](../../data/repeater/): Der Repeater wiederholt nur eine Vorlage; der Regeleditor kennt das Sieve-Vokabular.
- **Nicht verwechseln mit** [code-editor](../../../workbenches/special/code-editor/): Dieser bearbeitet rohen Text, der Regeleditor strukturierte Regeln. Rohes Sieve darf als Expertenansicht angeboten werden ⚠️.

## Best Practices

- Die Regel als Satz zeigen („Wenn Absender ..., dann verschieben nach ...“).
- Vor Regeln warnen, die alles treffen.
- Nur gültiges Sieve speichern; den Fehler an der Zeile zeigen.

## Hinweis zu Blinc

Kein Blinc-Gegenstück (`repeater` ist auch nicht vorhanden). In unserer Schicht gebaut, weil es Sieve bindet. Backlog-ID: keine ⚠️.

## Offene Punkte

- ⚠️ Im ersten Release unterstützte Sieve-Teilmenge
- ⚠️ Rundreise handgeschriebener Sieve-Skripte, die die strukturierte Ansicht nicht darstellen kann

## Siehe auch

- [fields – Übersicht](../index.md)
- [Repeater](../../data/repeater/)
- [Select](../../../primitives/fields/select/)
- [Switch](../../../primitives/fields/switch/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
