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
| **fix** | feste Höhe, längere Eingaben scrollen im Feld |
| **mitwachsend** | die Höhe wächst mit dem Text bis zu einer Obergrenze |
| **chat** | wächst bis zu drei Zeilen. Enter sendet, `Shift+Enter` macht einen Zeilenumbruch. |

## Funktionen

- Automatische Größenanpassung
- Platzhalter
- Validierung

## Abgrenzung

- **Nicht verwechseln mit** [text-input](../text-input/): Hier stehen Absätze und lange
  Sätze, dort genau eine Zeile.
- **Nicht verwechseln mit** [rich-text-editor](../../../workbenches/fields/rich-text-editor/): Dieses Feld speichert
  reinen Text ohne Formatierung.
- **Nicht verwechseln mit** [code-editor](../../../workbenches/special/code-editor/): Fließtext braucht
  keine Zeilennummern und keine Syntaxhervorhebung.

## Best Practices

- Die Starthöhe nach der erwarteten Länge wählen (Kommentar drei Zeilen, Beschreibung acht Zeilen).
- `mitwachsend` immer mit einer Obergrenze versehen. Sonst drückt das Feld die ganze Ansicht weg.
- Einen Zeichenzähler nur zeigen, wenn es eine Grenze gibt.
- `Tab` verlässt das Feld. Einen Tabulator nur anbieten, wenn Code eingegeben wird.
- Senden mit `Enter` nur im Chat-Modus, sonst `Strg+Enter`. Versehentliches Senden ist teuer.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Text Input](../text-input/) — eine Zeile
- [Rich Text Editor](../../../workbenches/fields/rich-text-editor/) — formatierter Text
- [Base-Komponente](../../basics/base.md)
