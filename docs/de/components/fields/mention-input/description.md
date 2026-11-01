# Mention Input (Erwähnungsfeld)

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
Ein Mention Input ist ein Textfeld mit Benutzer-/Kontakt-Erwähnung.

## Verwendungszweck

- Chat
- Kommentare
- Messages

## Features

- @-Mention
- Auto-complete
- Selected Users

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **feld** | eigenes Feld nur für Erwähnungen (z. B. Empfänger) |
| **inline** | Erwähnung mitten im Fließtext eines Kommentars |
| **mehrzeilig** | Chat-Editor mit mehreren Zeilen und Erwähnungen |

## Abgrenzung

- **Nicht verwechseln mit** [tags-input](../tags-input/): Tags sind freie Begriffe,
  eine Erwähnung zeigt auf einen Kontakt und löst eine Benachrichtigung aus.
- **Nicht verwechseln mit** [combobox](../combobox/): die Combobox schreibt einen Wert ins Feld,
  die Erwähnung bettet die Person in einen laufenden Text ein.
- Getippter Text wie „@john“ ohne Auswahl ist **keine** Erwähnung und erzeugt keine Meldung.

## Best Practices

- Vorschlagsliste erst nach `@` und einem weiteren Zeichen öffnen, Treffer nach Nähe sortieren.
- Eine eingefügte Erwähnung mit einer einzigen Rücktaste löschen (atomar behandeln).
- Sichtbar immer der Anzeigename, intern die Kontakt-ID – niemals den Namen speichern.
- Bei `long-press` die Kontaktkarte öffnen ([hover-card](../../overlays/hover-card/) am Desktop).

## Siehe auch

- [fields – Übersicht](../index.md)
- [Tags Input](../tags-input/) — freie Begriffe statt Kontakte
- [Emoji Picker](../emoji-picker/) — Zeichen einfügen
- [Basiskomponente](../../basics/base/)
