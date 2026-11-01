# Separator (Trennlinie)

| Feld | Wert |
|------|------|
| **Kategorie** | `basics` |
| **Erbt von** | `base` |
| **Varianten** | `horizontal`, `vertical`, `mit-beschriftung`, `dekorativ`, `inset` |
| **Zustände** | - |
| **Gesten** | - |
| **Animationen** | - |
| **Verwandt** | `card`, `panel`, `label`, `menu`, `toolbar`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Ein Separator trennt Inhalte voneinander: horizontal zwischen Blöcken,
vertikal zwischen Spalten oder Werkzeuggruppen. Er kann eine Beschriftung
tragen oder rein dekorativ sein.

## Verwendungszweck

- Gruppen in Menüs und Werkzeugleisten trennen
- Abschnitte in Formularen und Detailansichten gliedern
- „oder“-Trenner zwischen gleichwertigen Wegen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **horizontal** | Linie über die volle Breite |
| **vertical** | Linie zwischen zwei Spalten oder Gruppen |
| **mit-beschriftung** | Text mittig in der Linie (z. B. „oder“) |
| **dekorativ** | reine Optik ohne Strukturwirkung |
| **inset** | eingerückt, passend zu Listen mit Icon-Spalte |

## Features

- Abstand (`spacing`) links/rechts bzw. oben/unten einstellbar
- Beschriftung setzt die Linie automatisch fort
- `inset` orientiert sich an der Einzugsbreite der Liste

## Abgrenzung

- **Nicht verwechseln mit** dem Rand von [card](../../containers/card/) oder
  [panel](../../containers/panel/): deren Rahmen gehört zum Container.

- **Nicht verwechseln mit** Abstandhaltern (spacer): die trennen ohne Linie.
- Ein Trenner im Menü ist ein Separator mit Rolle `separator` in der Menügruppe.

## Best Practices

- In Menüs Gruppen trennen, nicht jeden Eintrag einzeln.
- Pro Abschnitt höchstens ein Separator; zu viele wirken fragmentiert.
- Dekorative Linien erhalten `aria-hidden="true"`.
- Beschriftung kurz halten („oder“, „anschließend“).

## Siehe auch

- [Label](../label/)
- [Menu](../../navigation/menu/)
- [Toolbar](../../navigation/toolbar/)
- [Basiskomponente](../base/)
