# Label (Beschriftung)

| Feld | Wert |
|------|------|
| **Kategorie** | `basics` |
| **Erbt von** | `base` |
| **Varianten** | `ueber-feld`, `inline`, `versteckt`, `pflicht` |
| **Zustände** | keine gegenüber `base` |
| **Gesten** | `tap` (Label fokussiert das Feld) |
| **Animationen** | keine — reine Beschriftung |
| **Verwandt** | `field`, `base`, `separator` |
| **Status** | dokumentiert |

## Beschreibung

Ein Label ist die Beschriftung eines Bedienelements oder Feldes. Es sagt,
was der Benutzer an dieser Stelle eingibt oder auslöst – sichtbar oder
nur für Screenreader.

## Verwendungszweck

- Jedes Eingabefeld beschriften (zusammen mit [field](../../fields/field/))
- Bedienelements ohne eigenen Text benennen
- Zugrifftasten kennzeichnen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **ueber-feld** | Standard: Label über dem Feld |
| **inline** | Label links neben dem Element |
| **versteckt** | visuell versteckt, für Screenreader wirksam |
| **pflicht** | mit Pflicht-Markierung und Text „erforderlich“ |

## Features

- Verknüpfung mit dem Element über `for`/`id`
- Zugrifftaste (`shortcut`) mit Unterstreichung
- Pflicht-Markierung immer mit Text, nie nur als Sternchen

## Abgrenzung

- **Nicht verwechseln mit** [field](../../fields/field/): der Wrapper ergänzt
  Hilfetext und Fehler; das Label ist nur der Text.

- **Nicht verwechseln mit** `placeholder`: ein Placeholder ist ein Beispiel,
  kein Ersatz für ein Label.

- **Nicht verwechseln mit** Bildunterschrift/caption: diese beschreibt ein Bild.

## Best Practices

- Kurz, im Singular, ohne Doppelpunkt am Ende.
- Kein Label als Icon oder Emoji.
- `versteckt` nur, wenn der Kontext das Label für Sehende ersetzt (z. B.
  Suchfeld mit Icon) – für Screenreader muss es wirksam bleiben.

## Siehe auch

- [Field](../../fields/field/)
- [Basiskomponente](../base/)
- [Separator](../separator/)
