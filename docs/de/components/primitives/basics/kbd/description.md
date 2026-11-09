# Kbd

| Feld | Wert |
|------|------|
| **Category** | `basics` |
| **Inherits from** | `base` |
| **Variants** | `einzeln`, `kombination` |
| **States** | `active` (Taste gedrückt) |
| **Gestures** | keine – nur Anzeige |
| **Animations** | `press` |
| **Related** | `badge`, `tooltip`, `base` |
| **Status** | documented |

## Beschreibung

Kbd zeigt eine einzelne Taste oder eine Tastenkombination optisch an – so, wie sie
auf einer Tastenkappe steht. Verwendet wird es in Hilfetexten, Tooltips und in der
Tastenkürzel-Dokumentation der Programme.

## Zweck

- Tastenkürzel in Tooltips und Kontexthilfe (`Strg + S`)
- Tastaturkürzel in Übersichten und Einführungen
- Gedrückt-/Aktiv-Zustand beim Lernen von Tastenkürzeln

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | eine Taste, z. B. `Esc` |
| **kombination** | mehrere Kbd-Elemente mit einem "+" dazwischen |

## Funktionen

- Tastenkappe mit Rahmen und leichtem Schatten, wie eine Tastenfläche
- Modifikatoren (`Strg`, `Alt`, `⇧`) als eigene Kappen
- `active` zeigt den Zustand, der gerade gedrückt wird

## Abgrenzung

- **Nicht verwechseln mit** `code`: Code-Schnipsel sind Fließtext in Festbreitenschrift;
  Kbd ist eine Taste.

- **Nicht verwechseln mit** [badge](../../feedback/badge/): Ein Badge zeigt einen Status,
  keine Taste.

- Tastenkürzel immer als Kombination aus Kbd-Elementen setzen, nicht als einen Textblock.

## Best Practices

- Die Namen je nach Sprache richtig setzen (Deutsch `Strg`, Englisch `Ctrl`) – die Beschriftung
  folgt der Oberflächensprache.

- In Tooltips: Kbd rechts neben dem Text, mit Abstand.
- Nicht mehr als drei Modifikatoren plus eine Taste.

## Siehe auch

- [Tooltip](../../../widgets/overlays/tooltip/)
- [Command](../../../widgets/navigation/command/) – Tastenkürzel finden und ausführen
- [Basiskomponente](../base.md)
