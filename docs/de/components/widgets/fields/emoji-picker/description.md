# Emoji Picker

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base` |
| **Varianten** | `inline`, `overlay`, `reaktion` |
| **Zustände** | `open`, `no-results` |
| **Gesten** | `tap`, `swipe`, `long-press` |
| **Animationen** | `pop-in`, `stagger` |
| **Verwandt** | `mention-input`, `rich-text-editor`, `icon`, `text-input` |
| **Status** | dokumentiert |

## Beschreibung
Ein Emoji Picker ist eine Emoji-Auswahl für Chat und Kommentare.

## Verwendungszweck

- Chat
- Kommentare
- Nachrichten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **inline** | die Auswahl bleibt dauerhaft unter dem Feld sichtbar (Schreibmodus) |
| **overlay** | Klappe am Cursor, schließt sich nach der Auswahl |
| **reaktion** | minimales Raster mit wenigen Emojis über einer Nachricht |

## Funktionen

- Kategorien
- Suche
- Zuletzt verwendet

## Abgrenzung

- **Nicht verwechseln mit** [mention-input](../../../primitives/fields/mention-input/): eine Erwähnung wählt eine Person
  aus einem Datensatz und erzeugt einen Verweis, ein Emoji ist nur ein Zeichen.
- **Nicht verwechseln mit** [icon](../../../primitives/media/icon/): Emojis gehören zum Inhalt, Icons zur
  Benutzeroberfläche. Für Schaltflächen und Menüs immer `icon` verwenden.
- Der Picker trifft eine Auswahl, er erzeugt selbst keinen Inhalt.

## Best Practices

- Die meistgenutzten Emojis oben halten; Kategorien über Reiter, nicht über endloses Scrollen.
- Immer an der Cursorposition einfügen, nicht am Textende.
- Hautton- und Geschlechtsvarianten nur anbieten, wenn der Nutzer sie ausdrücklich wählt.
- Reaktionen auf eine Nachricht begrenzen (max. eine pro Person und Emoji), sonst wird
  die Auswertung unlesbar.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Mention Input](../../../primitives/fields/mention-input/) — Personen statt Zeichen
- [Rich Text Editor](../../../workbenches/fields/rich-text-editor/) — Eingabe für Chat und Kommentare
- [Basiskomponente](../../../primitives/basics/base.md)
