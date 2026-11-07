# FreeSynergy Simple

> Kategorie: [Messenger](../../index.md) · Typ: unser eigenes Referenz-Frontend Nr. 1 „sehr, sehr einfach“ (ADR 0038) · Lizenz: MIT OR Apache-2.0

## Was es ist

Unser eigener, bewusst minimaler Messenger-Client. Jede eingehende Nachricht wird **im Vollbild** angezeigt;
alles wird mit wenigen Gesten erledigt. Es zeigt, dass ein Frontend auf dem Vertrag `fs-messenger` nicht kompliziert sein muss. Entwurf vom Projektinhaber (2026-11-05).

## Bemerkenswerte Ideen

- Eine Nachricht nach der anderen, im Vollbild — kein Posteingang, den man verwalten muss.
- Der ganze Ablauf besteht aus Gesten: weiter, weiterleiten, löschen, antworten, senden, abbrechen.
- Die Wahl der Empfänger ist ein einziges Suchfeld: Was du eintippst, filtert deine Kontakte; passt niemand, öffnet sich ein Formular „Neuer Kontakt“ mit den Feldern, die nötig sind, um diese Person zu erreichen.

## Verwendete Protokolle und Standards

Keine direkt — es spricht nur den Vertrag `fs-messenger` (Cap'n Proto, ADR 0021). E-Mail, Matrix,
MIMI, Telegram usw. liegen hinter den Konnektoren des Programms (ADR 0018).

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|--------------------------|
| [0.1](0.1/description.md) | 7/7 |

### 0.1

| Datei | Inhalt |
|-------|--------|
| [description.md](0.1/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen es geeignet ist |
| [features.md](0.1/features.md) | Was das Programm kann — und was nicht |
| [layout.md](0.1/layout.md) | Fensteraufbau, Bereiche, Panels |
| [menus.md](0.1/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](0.1/shortcuts.md) | Tastenkürzel |
| [api.md](0.1/api.md) | APIs und Protokolle, Authentifizierung, Ratenlimits |
| [themes/index.md](0.1/themes/index.md) | Themes: Farben, Typografie, Abstände — was neu gebaut werden kann |
| [interaction.md](0.1/interaction.md) | Hover, Fokus, Ziehen, Gesten (Finger, Maus, Stift) |
| [dependencies.md](0.1/dependencies.md) | Welche unserer Komponenten ein Frontend in diesem Stil braucht |
<!-- /gen:versions -->

## Quellen

Design vom Projektinhaber im Gespräch vom 2026-11-05 vorgegeben.
