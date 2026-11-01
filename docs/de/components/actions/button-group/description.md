# Button Group (Schaltflächengruppe)

| Feld | Wert |
|------|------|
| **Kategorie** | `actions` |
| **Erbt von** | `base` |
| **Varianten** | `verbund`, `segment`, `split` |
| **Zustände** | `selected` (Segment aktiv) |
| **Gesten** | `tap` |
| **Animationen** | `press`, `highlight` |
| **Verwandt** | `toolbar`, `tabs`, `tags-input`, `button`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Eine Button Group fasst zusammengehörige Buttons zu einer optischen und
logischen Einheit zusammen. Die Zugehörigkeit ist schon am Zusammenschluss
der Flächen erkennbar.

## Verwendungszweck

- Alternativen, die zusammen ausgeführt werden können (Schrift schnitt, ausrichten)
- Genau-eine-Auswahl ohne eigenes Dropdown (Segmented Control)
- Hauptaktion mit erweitertem Angebot (Split-Button mit Dropdown-Pfeil)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **verbund** | Buttons aneinandergereiht, gemeinsame Außenecken, aber mehrere unabhängige Aktionen |
| **segment** | Segmented Control, genau ein Segment ist aktiv |
| **split** | Hauptaktion plus abgetrennter Dropdown-Pfeil mit weiteren Optionen |

## Features

- Gemeinsame Höhe und Kanten der Gruppenelemente
- Auswahlverhalten wahlweise einfach oder mehrfach
- Horizontal oder vertikal anordbar

## Abgrenzung

- **Nicht verwechseln mit** [toolbar](../../navigation/toolbar/): eine Werkzeugleiste
  versammelt unabhängige Werkzeuge, eine Gruppe teilt sich einen Wert oder eine Aktion.

- **Nicht verwechseln mit** [tabs](../../navigation/tabs/): Tabs wechseln Ansichten,
  Segmente setzen eine Eigenschaft.

- **Nicht verwechseln mit** [tags-input](../../fields/tags-input/): dort entstehen
  Datensätze, hier werden Aktionen oder Eigenschaften gewählt.

## Best Practices

- Höchstens fünf Segmente, sonst `select` verwenden.
- Segmente beschriften statt nur zu iconisieren, außer die Icons sind eindeutig
  (Ausrichtung, Lautstärke).

- Split-Buttons nur, wenn die Hauptaktion eindeutig ist.
- Auswahlzustand zusätzlich zur Farbe mit `aria-pressed`/`aria-checked` markieren.

## Siehe auch

- [Button](../button/)
- [Toolbar](../../navigation/toolbar/)
- [Tabs](../../navigation/tabs/)
- [Basiskomponente](../../basics/base/)
