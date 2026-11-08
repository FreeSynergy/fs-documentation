# Menu

| Feld | Wert |
|------|------|
| **Kategorie** | `navigation` |
| **Erbt von** | `base` |
| **Varianten** | `horizontal`, `vertical`, `dropdown`, `menubar`, `hamburger` |
| **Zustände** | `open`, `expanded`, `selected` |
| **Gesten** | `tap`, `swipe` |
| **Animationen** | `expand`, `collapse`, `fade-in` |
| **Verwandt** | `context-menu`, `breadcrumb`, `tabs`, `bottom-navigation`, `sidebar` |
| **Rolle** | `menubar` |
| **Status** | dokumentiert |

!!! info "Vereinheitlichung"
    Die frühere Komponente `hamburger-menu` ist eine Variante von `menu` geworden:
    `dropdown`, `menubar`, `hamburger` (eingeklapptes Mobil-Menü).

## Beschreibung

Ein Menü ist eine geordnete Liste von Menüeinträgen, die Aktionen auslösen oder Ansichten
wechseln. Einträge können Untermenüs haben. Ein Menü ist der gemeinsame Oberbau für Leisten,
Aufklappmenüs und das Mobil-Menü.

## Verwendungszweck

- Programmweite Navigation in einer Leiste (`menubar`, `horizontal`)
- Gebündeltes Anbieten von Aktionen, ohne die Fläche zu überladen (`dropdown`)
- Navigation in der Seitenleiste (`vertical`)
- Navigation auf kleinen Bildschirmen (`hamburger`)

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **horizontal** | Leiste über dem Inhalt, Standard am Desktop |
| **vertical** | Liste neben dem Inhalt, in Seitenleisten |
| **dropdown** | Einträge erscheinen erst beim Öffnen |
| **menubar** | mehrere Menüs nebeneinander, jeweils mit Untermenü |
| **hamburger** | eingeklapptes Menü mit Icon, für Mobilgeräte und schmale Fenster |

## Funktionen

- Untermenüs mit beliebiger Tiefe
- Tastaturnavigation (Pfeiltasten, `Esc`, Pfeil rechts öffnet das Untermenü)
- Gruppen und Trenner zwischen Einträgen (`separator`)
- Icons und Beschriftungen einzeln ein- und ausschaltbar
- Öffnet und schließt sich mit einer Animation; ein Klick außerhalb schließt es

## Abgrenzung

- **Nicht verwechseln mit** [context-menu](../../overlays/context-menu/): das Kontextmenü gehört zum
  angeklickten Objekt und erscheint an der Zeigerposition (andere ARIA-Rolle).
- **Nicht verwechseln mit** [tabs](../tabs/): Tabs wechseln innerhalb einer Ansicht, ein Menü ändert
  Adressen oder führt Aktionen aus.
- **Nicht verwechseln mit** [bottom-navigation](../bottom-navigation/): feste Hauptbereiche auf Mobilgeräten,
  immer sichtbar.

## Best Practices

- Höchstens sieben Einträge pro Ebene; mehr gruppieren.
- Zerstörerische Aktionen gehören nicht ins Hauptmenü, sondern in den Kontext des Objekts.
- Biete das Menü auf Mobilgeräten nicht doppelt an (Hamburger *oder* Seitenleiste).
- Menüeinträge beginnen mit einem Verb; für den aktiven Eintrag `aria-current` oder `activeItem` verwenden.

## Siehe auch

- [navigation – Übersicht](../index.md)
- [Basiskomponente](../../../primitives/basics/base.md)
