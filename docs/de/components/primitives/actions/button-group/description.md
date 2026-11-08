# Button-Gruppe

| Feld | Wert |
|-------|-------|
| **Category** | `actions` |
| **Inherits from** | `base` |
| **Variants** | `verbund`, `segment`, `split` |
| **States** | `selected` (Segment aktiv) |
| **Gestures** | `tap` |
| **Animations** | `press`, `highlight` |
| **Related** | `toolbar`, `tabs`, `tags-input`, `button`, `base` |
| **Status** | documented |

## Beschreibung

Eine Button-Gruppe fasst zusammengehörige Buttons zu einer optischen und logischen
Einheit zusammen. Die Zusammengehörigkeit erkennt man daran, wie die Flächen aneinanderstoßen.

## Zweck

- Alternativen, die gemeinsam angewendet werden können (Schriftstil, Ausrichtung)
- Genau eine Wahl ohne eigene Auswahlliste (segmentierte Steuerung)
- Hauptaktion mit erweitertem Angebot (Split-Button mit Pfeil für die Auswahlliste)

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **verbund** | Buttons nebeneinander aufgereiht, gemeinsame Außenecken, aber mehrere unabhängige Aktionen |
| **segment** | segmentierte Steuerung, genau ein Segment ist aktiv |
| **split** | Hauptaktion plus ein abgetrennter Pfeil für weitere Optionen |

## Funktionen

- Gemeinsame Höhe und Kanten der Gruppenelemente
- Auswahlverhalten entweder einzeln oder mehrfach
- Kann waagerecht oder senkrecht angeordnet werden

## Abgrenzung

- **Nicht verwechseln mit** [toolbar](../../../widgets/navigation/toolbar/): eine Werkzeugleiste
  sammelt unabhängige Werkzeuge, eine Gruppe teilt sich einen Wert oder eine Aktion.

- **Nicht verwechseln mit** [tabs](../../../widgets/navigation/tabs/): Tabs wechseln
  Ansichten, Segmente setzen eine Eigenschaft.

- **Nicht verwechseln mit** [tags-input](../../fields/tags-input/): dort entstehen
  Einträge, hier werden Aktionen oder Eigenschaften gewählt.

## Best Practices

- Höchstens fünf Segmente, sonst `select` verwenden.
- Segmente beschriften statt nur Icons zu nutzen, es sei denn, die Icons sind eindeutig
  (Ausrichtung, Lautstärke).

- Split-Buttons nur, wenn die Hauptaktion eindeutig ist.
- Den Auswahlzustand zusätzlich zur Farbe mit `aria-pressed`/`aria-checked` markieren.

## Siehe auch

- [Button](../button/)
- [Toolbar](../../../widgets/navigation/toolbar/)
- [Tabs](../../../widgets/navigation/tabs/)
- [Basiskomponente](../../basics/base.md)
