# Scroll Area (Laufbereich)

| Feld | Wert |
|------|------|
| **Kategorie** | `containers` |
| **Erbt von** | `base` |
| **Varianten** | `vertikal`, `horizontal`, `beides` |
| **Zustände** | `atTop`, `atBottom` |
| **Gesten** | `swipe`, `drag` |
| **Animationen** | `fade-in` |
| **Verwandt** | `split-view`, `list-view`, `sidebar` |
| **Rolle** | `group` |
| **Status** | dokumentiert |

## Beschreibung

Ein Laufbereich ist eine Fläche mit festem Maß, deren Inhalt läuft. Er ergänzt
Bildlauf indicators, Randverläufe und Tastaturnavigation und nimmt Inhalt in einer
Konstante Höhe auf.

## Verwendungszweck

- Chats und Verläufe mit fester Höhe in einer Spalte
- Lange Listen innerhalb einer Karte oder eines Panels
- Waagerechte Bereiche wie Werkzeugleisten oder Bildreihen

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **vertikal** | nur höhenbegrenzt, Standard |
| **horizontal** | nur breitenbegrenzt |
| **beides** | Fläche mit beiden Laufrichtungen |

## Features

- Randverlauf zeigt an, dass es weitergeht
- Bildlauf folgt dem Inhalt automatisch (`follow`), etwa bei neuen Nachrichten
- Leiste blendet ein, wenn gelaufen wird, und aus bei Ruhe
- Tastatur: `Pfeiltasten`, `Page Up/Down`, `Pos1`/`Ende`

## Abgrenzung

- **Nicht verwechseln mit** [list-view](../../data/list-view/): die Liste ordnet Inhalte,
  der Laufbereich regelt nur das Laufen.
- **Nicht verwechseln mit** `overflow: auto`: ohne Verläufe, ohne Indikatoren,
  ohne Follow-Verhalten.

## Best Practices

- Pro Bildschirm-area höchstens zwei voneinander unabhängige Laufbereiche.
- Beim Nachladen oben die Scroll-Position halten, sonst springt der Inhalt.
- Reduzierte Bewegung beachten: kein sanftes Nachziehen bei `respectReducedMotion`.

## Siehe auch

- [Split View](../split-view/)
- [List View](../../data/list-view/)
- [Basiskomponente](../../basics/base/)
