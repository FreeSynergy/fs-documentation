# Separator

| Feld | Wert |
|-------|-------|
| **Category** | `basics` |
| **Inherits from** | `base` |
| **Variants** | `horizontal`, `vertical`, `mit-beschriftung`, `dekorativ`, `inset` |
| **States** | keine – nicht bedienbar |
| **Gestures** | keine – nicht bedienbar |
| **Animations** | `cross-fade` (Wechsel `vertical` → `horizontal`) |
| **Related** | `card`, `panel`, `label`, `menu`, `toolbar`, `base` |
| **Status** | documented |

## Beschreibung

Ein Separator trennt Inhalte voneinander: waagerecht zwischen Blöcken, senkrecht zwischen
Spalten oder Werkzeuggruppen. Er kann eine Beschriftung tragen oder rein dekorativ sein.

## Zweck

- Gruppen in Menüs und Werkzeugleisten trennen
- Abschnitte in Formularen und Detailansichten gliedern
- Ein „oder“-Trenner zwischen gleichwertigen Wegen

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **horizontal** | Linie über die volle Breite |
| **vertical** | Linie zwischen zwei Spalten oder Gruppen |
| **mit-beschriftung** | Text mittig in der Linie (z. B. „oder“) |
| **dekorativ** | reines Aussehen ohne strukturelle Wirkung |
| **inset** | eingerückt, passend zu Listen mit Icon-Spalte |

## Funktionen

- Der Abstand (`spacing`) nach links/rechts oder oben/unten ist einstellbar
- Eine Beschriftung unterbricht die Linie automatisch
- `inset` folgt der Einzugsbreite der Liste

## Abgrenzung

- **Nicht verwechseln mit** dem Rahmen einer [card](../../../widgets/containers/card/) oder
  eines [panel](../../../widgets/containers/panel/): deren Rahmen gehört zum Container.

- **Nicht verwechseln mit** Abstandshaltern: die trennen ohne Linie.
- Ein Trenner im Menü ist ein Separator mit der Rolle `separator` in der Menügruppe.

## Best Practices

- In Menüs Gruppen trennen, nicht jeden einzelnen Eintrag.
- Höchstens ein Separator pro Abschnitt; zu viele wirken zerstückelt.
- Dekorative Linien erhalten `aria-hidden="true"`.
- Die Beschriftung kurz halten („oder“, „dann“).

## Siehe auch

- [Label](../label/)
- [Menü](../../../widgets/navigation/menu/)
- [Toolbar](../../../widgets/navigation/toolbar/)
- [Basiskomponente](../base.md)
