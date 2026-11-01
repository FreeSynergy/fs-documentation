# Kbd (Tastenkennung)

| Feld | Wert |
|------|------|
| **Kategorie** | `basics` |
| **Erbt von** | `base` |
| **Varianten** | `einzeln`, `kombination` |
| **Zustände** | `active` (Taste gedrückt) |
| **Gesten** | keine — reine Anzeige |
| **Animationen** | `press` |
| **Verwandt** | `badge`, `tooltip`, `base` |
| **Status** | dokumentiert |

## Beschreibung

Kbd stellt eine einzelne Taste oder eine Tastenkombination optisch dar –
wie auf einer Tastaturkappe. Es wird in Hilfetexten, Tooltips und den
Shortcut-Dokumentationen der Programme verwendet.

## Verwendungszweck

- Shortcuts in Tooltipps und Kontexthilfen (`Strg + S`)
- Kurzbefehle in Übersichten und Onboarding-Touren
- Druck-/Aktiv-Zustand beim Lernen von Shortcuts

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **einzeln** | eine Taste, z. B. `Esc` |
| **kombination** | mehrere Kbd-Elemente mit „+“ dazwischen |

## Features

- Kappe mit Rand und leichtem Schatten, wie eine Tastenoberfläche
- Modifikatoren (`Strg`, `Alt`, `⇧`) als eigene Kappen
- `active` zeigt den gerade gedrückten Zustand

## Abgrenzung

- **Nicht verwechseln mit** `code`: Code-Ausschnitte sind Fließtext in
  Monospace; Kbd ist eine Taste.

- **Nicht verwechseln mit** [badge](../../feedback/badge/): ein Badge zeigt
  Status, keine Taste.

- Kurzbefehle immer als Kombination aus Kbd-Elementen setzen, nicht als
  ein Textblock.

## Best Practices

- Pro Sprache korrekt benennen (deutsch `Strg`, englisch `Ctrl`) – die
  Beschriftung folgt der UI-Sprache.

- In Tooltipps: Kbd rechts im Text, mit Abstand.
- Nicht mehr als drei Modifikatoren + eine Taste.

## Siehe auch

- [Tooltip](../../overlays/tooltip/)
- [Konzept und Plan](../../konzept-und-plan.md) (u. a. geplantes `command`)
- [Basiskomponente](../base/)
