# Kbd

| Feld | Wert |
|-------|-------|
| **Kategorie** | `basics` |
| **Erbt von** | `base` |
| **Varianten** | `einzeln`, `kombination` |
| **Zustände** | `active` (Taste gedrückt) |
| **Gesten** | keine – nur Anzeige |
| **Animationen** | `press` |
| **Verwandt** | `badge`, `tooltip`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Kbd zeigt eine einzelne Taste oder eine Tastenkombination optisch an – so, wie sie auf einer
Tastenkappe steht. Sie wird in Hilfetexten, Tooltips und in der Tastenkürzel-Dokumentation der
Programme verwendet.

## Verwendungszweck
- Tastenkürzel in Tooltips und Kontexthilfe (`Strg + S`)
- Tastenkürzel in Übersichten und Einführungstouren
- Gedrückt-Zustand beim Lernen von Tastenkürzeln

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **einzeln** | eine Taste, z. B. `Esc` |
| **kombination** | mehrere kbd-Elemente mit einem „+“ dazwischen |

## Funktionen

- Tastenkappe mit Rahmen und leichtem Schatten, wie eine Tastenoberfläche
- Modifikatoren (`Strg`, `Alt`, `⇧`) als eigene Kappen
- `active` zeigt den Zustand, der gerade gedrückt wird

## Abgrenzung

- **Nicht verwechseln mit** `code`: Code-Schnipsel sind Fließtext in Festbreitenschrift;
  kbd ist eine Taste.

- **Nicht verwechseln mit** [badge](../../feedback/badge/): ein Badge zeigt einen Status,
  keine Taste.

- Tastenkürzel immer als Kombination aus kbd-Elementen setzen, nicht als ein Textblock.

## Best Practices

- Die Namen je nach Sprache richtig setzen (Deutsch `Strg`, Englisch `Ctrl`) – die Beschriftung
  folgt der Oberflächensprache.

- In Tooltips: kbd rechts neben dem Text, mit Abstand.
- Nicht mehr als drei Modifikatoren plus eine Taste.

## Siehe auch

- [Tooltip](../../../widgets/overlays/tooltip/)
- [Command](../../../widgets/navigation/command/) – Tastenkürzel finden und ausführen
- [Basiskomponente](../base.md)
