# Label

| Feld | Wert |
|-------|-------|
| **Kategorie** | `basics` |
| **Erbt von** | `base` |
| **Varianten** | `ueber-feld`, `inline`, `versteckt`, `pflicht` |
| **Zustände** | keine gegenüber `base` |
| **Gesten** | `tap` (das Label fokussiert das Feld) |
| **Animationen** | keine – nur Beschriftung |
| **Verwandt** | `field`, `base`, `separator` |
| **Status** | dokumentiert |

## Beschreibung

Ein Label ist die Beschriftung eines Steuerelements oder Feldes. Es sagt, was die Person an dieser Stelle
eingibt oder auslöst – sichtbar oder nur für Screenreader.

## Verwendungszweck
- Jedes Eingabefeld beschriften (zusammen mit [field](../../fields/field/))
- Steuerelemente benennen, die keinen eigenen Text haben
- Zugriffstasten kennzeichnen

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **ueber-feld** | Standard: Label über dem Feld |
| **inline** | Label links vom Element |
| **versteckt** | optisch verborgen, bleibt für Screenreader aktiv |
| **pflicht** | mit Pflichtkennzeichnung und dem Text „Pflichtfeld“ |

## Funktionen

- Über `for`/`id` mit dem Element verknüpft
- Zugriffstaste (`shortcut`) unterstrichen dargestellt
- Die Pflichtkennzeichnung kommt immer mit Text, nie nur als Sternchen

## Abgrenzung

- **Nicht verwechseln mit** [field](../../fields/field/): die Hülle ergänzt den Hilfetext
  und den Fehler; das Label ist nur der Text.

- **Nicht verwechseln mit** `placeholder`: ein Platzhalter ist ein Beispiel, kein Ersatz
  für ein Label.

- **Nicht verwechseln mit** einer Bildunterschrift: die beschreibt ein Bild.

## Best Practices

- Kurz, im Singular, ohne Doppelpunkt am Ende.
- Kein Label als Icon oder Emoji.
- `versteckt` nur, wenn der Kontext das Label für Sehende ersetzt (z. B. ein Suchfeld
  mit Icon) – für Screenreader muss es aktiv bleiben.

## Siehe auch

- [Field](../../fields/field/)
- [Basiskomponente](../base.md)
- [Separator](../separator/)
