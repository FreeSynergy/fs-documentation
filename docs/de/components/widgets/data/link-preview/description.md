# Link Preview (Linkvorschau)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `card`, `compact` |
| **Zustände** | `loading`, `ready`, `unavailable` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `fade-in` |
| **Verwandt** | `card`, `image`, `link`, `message-bubble`, `hover-card` |
| **Status** | Skizze |

## Beschreibung

Eine Linkvorschau ist eine Vorschaukarte für einen Link, die vom **Absender** erzeugt und an die Nachricht angehängt wird. Der Leser ruft das Ziel nie selbst ab.

## Verwendungszweck

- Vorschau eines Links innerhalb einer Nachricht
- Datenschutzfreundlich: keine Tracking-Anfrage vom Leser
- Ein Klick öffnet das Ziel nach einer Bestätigung

## Varianten

| Variante | Beschreibung |
|---|---|
| **card** | Titel, Beschreibung, Bild, Seite |
| **compact** | Titel und Seite in einer Zeile |

## Features

- Titel, Beschreibung, Bild und Seitenname
- Die Vorschaudaten kommen aus der Nachricht, nicht aus dem Netz
- Ein Klick läuft über den Host (Bestätigung bei externen Zielen)

## Datenbindung

Bindet ActivityStreams `Link` / `Page` als Anhang ⚠️ (nicht für alle Transporte standardisiert). Darstellungsregister (ADR 0023): `Link → link-preview | text`.

## Abgrenzung

- **Nicht verwechseln mit** [card](../../containers/card/): Die Card ist ein generischer Container; diese Komponente bindet die Linkdaten.
- **Nicht verwechseln mit** [hover-card](../../overlays/hover-card/): Diese erscheint beim Hover; die Vorschau ist Teil des Inhalts.
- **Nicht verwechseln mit** [embed](../../../workbenches/special/embed/): Es wird kein fremder Inhalt geladen.

## Best Practices

- Niemals entfernte Bilder laden; nur verwenden, was der Absender angehängt hat.
- Die echte Zieldomain zeigen.
- Die Vorschau in unverschlüsselten Unterhaltungen weglassen, wenn der Host es verlangt ⚠️.

## Hinweis zu Blinc

Teilweise in Blinc vorhanden (`cn::card`). In unserer Schicht gebaut wegen der Datenbindung. Backlog-ID: keine ⚠️.

## Offene Punkte

- ⚠️ Wer erzeugt die Vorschau (Client des Absenders) und wie wird sie verschlüsselt?
- ⚠️ Transportzuordnung für Matrix und Mail

## Siehe auch

- [data – Übersicht](../index.md)
- [Message Bubble](../message-bubble/)
- [Card](../../containers/card/)
- [Link](../../../primitives/basics/link/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
