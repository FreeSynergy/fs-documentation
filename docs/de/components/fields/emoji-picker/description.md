# Emoji Picker (Emoji-Auswahl)

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
Ein Emoji Picker ist eine Emoji-Auswahl für Chat/Kommentare.

## Verwendungszweck

- Chat
- Kommentare
- Messages

## Features

- Categories
- Search
- Recent

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **inline** | Auswahl ist dauerhaft unter dem Feld eingeblendet (Komponiermodus) |
| **overlay** | Klappe am Cursor, schließt nach der Auswahl |
| **reaktion** | minimales Raster mit wenigen Emojis über einer Nachricht |

## Abgrenzung

- **Nicht verwechseln mit** [mention-input](../mention-input/): eine Erwähnung wählt eine Person
  aus einem Datensatz aus und erzeugt eine Verknüpfung, ein Emoji ist nur ein Zeichen.
- **Nicht verwechseln mit** [icon](../../media/icon/): Emojis gehören zum Inhalt, Icons zur
  Bedienoberfläche. Für Buttons und Menüs immer `icon` verwenden.
- Der Picker wählt aus, er erzeugt keine eigenen Inhalte.

## Best Practices

- Zuerstgenutzte Emojis oben halten; Kategorien über Reiter, nicht über endloses Scrollen.
- Einfügen immer an der Cursorposition, nicht am Ende des Textes.
- Haut- und Geschlechtsvarianten nur anbieten, wenn der Nutzer sie explizit wählt.
- Reaktionen auf eine Nachricht begrenzen (max. eine pro Person und Emoji), sonst wird
  die Auswertung unlesbar.

## Siehe auch

- [fields – Übersicht](../index.md)
- [Mention Input](../mention-input/) — Personen statt Zeichen
- [Rich Text Editor](../rich-text-editor/) — Chat- und Kommentar-Eingabe
- [Basiskomponente](../../basics/base/)
