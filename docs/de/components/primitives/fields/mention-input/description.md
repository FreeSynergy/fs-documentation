# Mention Input (Erwähnungseingabe)

| Feld | Wert |
|------|------|
| **Kategorie** | `fields` |
| **Erbt von** | `base`, `text-input` |
| **Varianten** | `feld`, `inline`, `mehrzeilig` |
| **Zustände** | `open`, `loading` |
| **Gesten** | `tap`, `long-press` |
| **Animationen** | `fade-in`, `pop-in` |
| **Verwandt** | `tags-input`, `combobox`, `emoji-picker`, `text-input` |
| **Status** | dokumentiert |

## Beschreibung
Ein Mention Input ist ein Textfeld mit Erwähnungen von Benutzern oder Kontakten.

## Verwendungszweck

- Chat
- Kommentare
- Nachrichten

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **feld** | ein eigenes Feld nur für Erwähnungen (z. B. Empfänger) |
| **inline** | eine Erwähnung mitten im laufenden Text eines Kommentars |
| **mehrzeilig** | Chat-Editor mit mehreren Zeilen und Erwähnungen |

## Funktionen

- Erwähnung mit @
- Autovervollständigung
- Ausgewählte Benutzer

## Abgrenzung

- **Nicht verwechseln mit** [tags-input](../tags-input/): Tags sind freie Begriffe.
  Eine Erwähnung verweist auf einen Kontakt und löst eine Benachrichtigung aus.
- **Nicht verwechseln mit** [combobox](../combobox/): Die Combobox schreibt einen Wert in das
  Feld. Die Erwähnung bettet die Person in den laufenden Text ein.
- Getippter Text wie „@john“ ohne Auswahl ist **keine** Erwähnung und erzeugt
  keine Benachrichtigung.

## Best Practices

- Die Vorschlagsliste erst nach `@` und einem weiteren Zeichen öffnen. Treffer nach Nähe sortieren.
- Eine eingefügte Erwähnung mit einem einzigen Backspace löschen (wie ein unteilbares Element behandeln).
- Immer den Anzeigenamen zeigen, intern die Kontakt-ID speichern. Den Namen nie speichern.
- Bei `long-press` die Kontaktkarte öffnen ([hover-card](../../../widgets/overlays/hover-card/) am Desktop).

## Siehe auch

- [fields – Übersicht](../index.md)
- [Tags Input](../tags-input/) — freie Begriffe statt Kontakte
- [Emoji Picker](../../../widgets/fields/emoji-picker/) — Zeichen einfügen
- [Base-Komponente](../../basics/base.md)
