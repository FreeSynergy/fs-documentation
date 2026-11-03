# Textarea (Mehrzeiliges Textfeld)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `fix`, `mitwachsend`, `chat` |
| **Zustände** | `filled`, `error` |
| **Gesten** | `tap`, `double-tap`, `long-press`, `drag` |
| **Animationen** | `expand`, `highlight` |
| **Verwandt** | `text-input`, `rich-text-editor`, `field`, `scroll-area` |
| **Status** | dokumentiert |

## Beschreibung
Ein Textarea ist ein mehrzeiliges Eingabefeld für Text.

## Verwendungszweck

- Nachrichten
- Kommentare
- Beschreibungen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **fix** | vorgegebene Höhe, längere Eingabe scrollt im Feld |
| **mitwachsend** | Höhe wächst mit dem Text bis zu einer Obergrenze |
| **chat** | wächst bis drei Zeilen, Enter sendet, `Umschalt+Enter` bricht um |

## Features

- Auto-resize
- Placeholder
- Validation

## Abgrenzung

- **Nicht verwechseln mit** [text-input](../text-input/): hier stehen Absätze und lange Sätze,
  dort genau eine Zeile.
- **Nicht verwechseln mit** [rich-text-editor](../rich-text-editor/): dieses Feld speichert reinen
  Text ohne Formatierung.
- **Nicht verwechseln mit** [code-editor](../../special/code-editor/): Fließtext braucht keine
  Zeilennummern und keine Syntaxhervorhebung.

## Best Practices

- Anfangshöhe nach erwarteter Länge (Kommentar drei Zeilen, Beschreibung acht Zeilen).
- `mitwachsend` immer mit Obergrenze, sonst verdrängt das Feld die ganze Ansicht.
- Zeichenzähler nur anzeigen, wenn es ein Limit gibt.
- `Tab` verlässt das Feld; einen Tabsprung nur anbieten, wenn Code eingegeben wird.
- Senden per `Enter` nur im Chat-Modus, sonst `Strg+Enter` — Versehentliches Absenden ist teuer.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Text Input](../text-input/) — einzeilig
- [Rich Text Editor](../rich-text-editor/) — formatierter Text
- [Basiskomponente](../../basics/base/)
